#!/usr/bin/env bash
# Laporan progres RT-DETR yang detail. Satu blok per pemanggilan.
cd /workspace/experiments
CSV=runs/rtdetr_l_e60_i1280/results.csv
LOG=logs-rtdetr.txt
BASE50=0.5218; BASE5095=0.2407; TGT50=0.60; TGT5095=0.30

# progres dalam-epoch dari log live — hanya bilah LATIH (mengandung "1280:"),
# bukan bilah validasi (mengandung "mAP50-95):")
live=$(tr '\r' '\n' < "$LOG" | grep -aE "1280: +[0-9]+%" | tail -1)
batch=$(echo "$live" | grep -oE "[0-9]+/[0-9]+ +[0-9.]+it/s +[0-9:]+<[0-9:]+" | tail -1)
pct=$(echo "$live" | grep -oE "1280: +[0-9]+%" | grep -oE "[0-9]+%" | tail -1)
# deteksi kalau sedang validasi
if tr '\r' '\n' < "$LOG" | tail -3 | grep -qaE "mAP50-95\): +[0-9]"; then
  vbar=$(tr '\r' '\n' < "$LOG" | grep -aE "mAP50-95\): +[0-9]+%" | tail -1 | grep -oE "[0-9]+%" | tail -1)
  batch="[validasi $vbar]"
fi

if [ ! -f "$CSV" ]; then
  echo "[RT-DETR] belum ada epoch selesai — dalam epoch 1 · $pct $batch"
else
  read ep tt P R m50 m5095 vg vc vl <<<"$(tail -1 "$CSV" | awk -F, '{printf "%s %s %s %s %s %s %s %s %s",$1,$2,$6,$7,$8,$9,$10,$11,$12}')"
  read tg tc tl <<<"$(tail -1 "$CSV" | awk -F, '{printf "%s %s %s",$3,$4,$5}')"
  # puncak
  read pk50 pe50 pk5095 pe5095 <<<"$(awk -F, 'NR>1{if($8>a){a=$8;ea=$1}; if($9>b){b=$9;eb=$1}}END{printf "%.4f %s %.4f %s",a,ea,b,eb}' "$CSV")"
  # ETA total: detik/epoch * sisa epoch
  eta=$(awk -F, -v ep="$ep" -v tt="$tt" 'BEGIN{spe=tt/ep; left=(60-ep)*spe; printf "%.0f mnt/epoch, sisa ~%.1f jam",spe/60,left/3600}')
  gpu=$(nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader 2>/dev/null | tr '\n' ' ')
  # selisih puncak vs baseline & target
  d=$(awk -v a="$pk50" -v b="$pk5095" -v bl="$BASE50" -v bl2="$BASE5095" -v t="$TGT50" -v t2="$TGT5095" \
      'BEGIN{printf "vs baseline: mAP50 %+.4f · mAP50-95 %+.4f  |  ke target: mAP50 %+.4f · mAP50-95 %+.4f",a-bl,b-bl2,a-t,b-t2}')
  printf "══ RT-DETR-L · epoch %s/60 · %s %s\n" "$ep" "$pct" "$batch"
  printf "   val    : P %.3f · R %.3f · mAP50 %.4f · mAP50-95 %.4f\n" "$P" "$R" "$m50" "$m5095"
  printf "   loss   : giou %.3f · cls %.3f · l1 %.3f  (val giou %.3f/cls %.3f)\n" "$tg" "$tc" "$tl" "$vg" "$vc"
  printf "   puncak : mAP50 %.4f (ep%s) · mAP50-95 %.4f (ep%s)\n" "$pk50" "$pe50" "$pk5095" "$pe5095"
  printf "   %s\n" "$d"
  printf "   GPU %s· %s\n" "$gpu" "$eta"
fi
