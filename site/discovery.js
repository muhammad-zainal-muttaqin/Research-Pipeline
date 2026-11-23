(() => {
  'use strict';

  const aliasesByTopic = [
    ['Kelapa sawit', 'oil palm', 'oil palms', 'kelapa sawit', 'sawit', 'tandan buah segar', 'fresh fruit bunch', 'fresh fruit bunches'],
    ['Apel', 'apple', 'apples', 'apel'],
    ['Anggur', 'grape', 'grapes', 'anggur', 'grapevine'],
    ['Jeruk', 'citrus', 'orange', 'oranges', 'jeruk'],
    ['Tomat', 'tomato', 'tomatoes', 'tomat'],
    ['Mangga', 'mango', 'mangoes', 'mangga'],
    ['Stroberi', 'strawberry', 'strawberries', 'stroberi'],
    ['Alpukat', 'avocado', 'avocados', 'alpukat'],
    ['Pelacakan objek', 'object tracking', 'multi object tracking', 'tracking', 'pelacakan objek', 'pelacakan', 'pelacak'],
    ['Kedalaman', 'depth', 'kedalaman', 'depth sensing', 'sensor kedalaman', 'depth estimation', 'estimasi kedalaman'],
    ['RGB-D', 'rgb d', 'rgb with depth', 'rgb dengan kedalaman'],
    ['Awan titik', 'point cloud', 'awan titik'],
    ['Rekonstruksi 3D', '3d reconstruction', 'rekonstruksi 3d', 'three dimensional reconstruction'],
    ['Beberapa sudut pandang', 'multi view', 'multisisi', 'multi sisi', 'multi pengamatan', 'cross view', 'lintas pandang', 'beberapa sudut pandang'],
    ['Hitung buah', 'fruit counting', 'fruits counting', 'counting fruit', 'counting fruits', 'fruit count', 'pencacahan buah', 'penghitungan buah', 'hitung buah'],
    ['Tandan buah', 'fruit bunch', 'fruit bunches', 'tandan buah', 'tandan sawit'],
    ['Set data', 'dataset', 'datasets', 'set data', 'data set'],
    ['Estimasi panen', 'yield estimation', 'yield prediction', 'estimasi hasil panen', 'estimasi panen', 'perkiraan panen'],
    ['Segmentasi instans', 'instance segmentation', 'segmentasi instans', 'segmentasi instance'],
    ['Kematangan', 'ripeness', 'maturity', 'ripening', 'kematangan'],
    ['Oklusi', 'occlusion', 'oklusi', 'buah tertutup'],
    ['Pose objek', 'object pose', 'pose estimation', 'estimasi pose', '6d pose'],
    ['YOLO', 'yolo', 'you only look once'],
    ['YOLOX', 'yolox', 'yolo x'],
    ['BoT-SORT', 'bot sort', 'botsort'],
    ['ByteTrack', 'bytetrack', 'byte track'],
    ['DeepSORT', 'deep sort', 'deepsort'],
    ['OC-SORT', 'oc sort', 'ocsort'],
    ['DETR', 'detr', 'detection transformer'],
    ['R-CNN', 'r cnn', 'rcnn'],
    ['SfM', 'sfm', 'structure from motion'],
    ['SLAM', 'slam', 'simultaneous localization and mapping'],
    ['NeRF', 'nerf', 'neural radiance field'],
    ['LiDAR', 'lidar', 'light detection and ranging']
  ];
  const namedMethods = new Set(['YOLO', 'YOLOX', 'BoT-SORT', 'ByteTrack', 'DeepSORT', 'OC-SORT', 'DETR', 'R-CNN', 'SfM', 'SLAM', 'NeRF']);
  const crops = new Set(['Kelapa sawit', 'Apel', 'Anggur', 'Jeruk', 'Tomat', 'Mangga', 'Stroberi', 'Alpukat']);
  const studyFocus = new Set([
    ...namedMethods, 'Set data', 'Pelacakan objek', 'Beberapa sudut pandang', 'Hitung buah',
    'Estimasi panen', 'Segmentasi instans', 'Rekonstruksi 3D', 'Pose objek'
  ]);
  const caseSensitive = new Set([...namedMethods, 'RGB-D', 'LiDAR']);
  const topicByAlias = new Map();
  const topicLabels = new Map();

  function normalize(value) {
    return String(value ?? '').normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase()
      .replace(/[łøßæœıȷ]/g, character => ({ ł: 'l', ø: 'o', ß: 'ss', æ: 'ae', œ: 'oe', ı: 'i', ȷ: 'j' })[character])
      .replace(/[^\p{L}\p{N}]+/gu, ' ').trim()
      .replace(/\bmultiview\b/g, 'multi view')
      .replace(/\brgbd\b/g, 'rgb d')
      .replace(/\byolo\s*v?\s*(?=\d)/g, 'yolov');
  }

  function boundary(variants, prefix = false) {
    const alternatives = variants.map(term => {
      if (prefix && term.length >= 3 && !term.includes(' ')) return term;
      return term + '(?= |$)';
    });
    return new RegExp('(?:^| )(?:' + alternatives.join('|') + ')', 'u');
  }

  const topics = aliasesByTopic.map(([label, ...values], i) => {
    const id = '@' + i;
    const variants = values.map(normalize);
    topicLabels.set(id, label);
    variants.forEach(variant => topicByAlias.set(variant, variants));
    const pattern = label === 'YOLO' ? /(?:^| )(?:yolo(?:v\d+[a-z]?)?|you only look once)(?= |$)/ : boundary(variants);
    const words = new Set(variants.flatMap(variant => variant.split(' ')));
    return { id, label, pattern, words };
  });

  function methodsInTitle(title) {
    const normalized = normalize(title);
    return topics.filter(topic => namedMethods.has(topic.label) && topic.pattern.test(normalized))
      .flatMap(({ label }) => {
        if (label !== 'YOLO') return label;
        const versions = normalized.match(/\byolov\d+[a-z]?\b/g);
        return versions ? Array.from(new Set(versions.map(version => 'YOLO' + version.slice(4)))) : label;
      });
  }

  function queryTerms(query) {
    const words = query.split(' ');
    const groups = [];
    for (let pos = 0; pos < words.length;) {
      let end = Math.min(pos + 5, words.length);
      while (end > pos + 1 && !topicByAlias.has(words.slice(pos, end).join(' '))) end--;
      const term = words.slice(pos, end).join(' ');
      const variants = topicByAlias.get(term) || [term];
      groups.push({ term, direct: boundary([term]), match: boundary(variants, true), variants });
      pos = end;
    }
    return groups;
  }

  function searchRecord(entry) {
    const authors = (entry.authors || []).map(name => normalize(name));
    return {
      entry,
      title: normalize(entry.title),
      titles: normalize([entry.title, ...(entry.aliases || [])].join(' ')),
      authors,
      names: authors.join(' '),
      overview: normalize(entry.ov || entry.summary || entry.desc),
      metadata: normalize([
        entry.theme, entry.venue, entry.bib, entry.id, entry.year,
        ...(entry.crops || []), ...(entry.methods || [])
      ].join(' '))
    };
  }

  function scoreSearch(record, query, identifier, terms) {
    const { entry, title, titles, authors, names, overview, metadata } = record;
    if ([entry.id, entry.bib, entry.doi].some(value => value?.toLowerCase() === identifier)) return 1000;
    if (title === query || (entry.aliases || []).some(alias => normalize(alias) === query)) return 750;
    const completeName = authors.some(name => terms.every(({ term, match }) =>
      match.test(name) || (term.length === 1 && name.split(' ').some(word => word.startsWith(term)))));
    let score = completeName ? 25 : 0;
    for (const { term, direct, match, variants } of terms) {
      if (direct.test(titles)) score += 18;
      else if (match.test(titles)) score += 14;
      else if (direct.test(names)) score += 14;
      else if (match.test(names) || (completeName && term.length === 1)) score += 10;
      else if (match.test(metadata)) score += 8;
      else if (match.test(overview)) score += 4;
      else {
        if (term.length < 3 || entry.id === 'katalog-pdf') return 0;
        record.body ??= normalize(entry.md);
        if (match.test(record.body)) score += 2;
        else {
          record.sourceText ??= (entry.src || '').toLowerCase();
          if (!variants.some(variant => record.sourceText.includes(variant))) return 0;
          score += 1;
        }
      }
    }
    if (query.length > 2 && title.startsWith(query + ' ')) score += 21;
    else if (titles.includes(query)) score += 15;
    return score;
  }

  const stopWords = new Set((
    'ada adalah agar akan akses antar atau bahwa baik bagi berbagai baru banyak berada berdasarkan karena ' +
    'bagian dalam dan dapat dari dengan digunakan dilakukan diperoleh diusulkan dua hanya juga hasil hingga ' +
    'informasi inti ini itu jadi kajian kamera kerja lain lebih lewat langkah maka memakai melalui melihat ' +
    'memberi membutuhkan memiliki meningkatkan menggunakan menjadi menunjukkan menyebut merupakan model ' +
    'nilai oleh pada paling penelitian penulis perlu satu sebagai sebelum sebuah secara sehingga selain ' +
    'seperti serta sesuai setelah sudah suatu tanpa telah tentang terhadap tersebut terlalu terdiri tidak ' +
    'tingkat teknik untuk waktu yang buah citra gambar data metode deteksi penghitungan hitung menghitung ' +
    'pencacahan kinerja pendekatan sistem perbandingan evaluasi akurasi pelatihan beberapa perangkat ' +
    'the a all along an and are because between both but can could each for from had has have how into its ' +
    'more most new not one only other our over per than that their them then these this those two use used ' +
    'using via was were what when where which while will with without work would based method model data ' +
    'dataset approach system detection detector fruit fruits counting count numbers estimate estimation ' +
    'study studies paper research results performance experimental evaluation accurate accuracy image images ' +
    'computer vision deep learning automated automatic improved analysis validation model proposed ' +
    'object objects objek visual multi view pandang models'
  ).split(/\s+/));

  function topicVector(record) {
    const { entry, titles, overview } = record;
    const strengths = new Map();
    const subject = normalize([...(entry.crops || []), ...(entry.methods || [])].join(' '));
    for (const [text, strength] of [[titles, 4], [subject, 3.5], [overview.slice(0, 2200), 0.8]]) {
      const groups = topics.filter(topic => topic.pattern.test(text));
      const words = new Set(text.split(' ').filter(word =>
        word.length > 3 && /\p{L}/u.test(word) && !stopWords.has(word) && !groups.some(group => group.words.has(word))));
      for (const word of words) {
        if (!strengths.has(word)) strengths.set(word, strength);
      }
      for (const group of groups) {
        if (!strengths.has(group.id)) strengths.set(group.id, strength * 1.65);
      }
    }
    return strengths;
  }

  function topicProfiles(records) {
    const vectors = records.map(record => topicVector(record));
    const frequency = new Map();
    for (const vector of vectors) {
      for (const word of vector.keys()) frequency.set(word, (frequency.get(word) || 0) + 1);
    }
    return records.map((record, i) => {
      const base = vectors[i];
      const weights = new Map();
      for (const [word, strength] of base) {
        const count = frequency.get(word);
        if (count < 2 || count > records.length * 0.45) continue;
        const rarity = Math.min(4, 1 + Math.log(records.length / count));
        weights.set(word, rarity * strength);
      }
      const length = Math.hypot(...weights.values());
      return { entry: record.entry, base, weights, length };
    });
  }

  function similarity(target, candidate) {
    const shared = [];
    for (const [word, weight] of target.weights) {
      const candidateWeight = candidate.weights.get(word);
      if (!candidateWeight) continue;
      const inTargetSubject = target.base.get(word) >= 3;
      const inCandidateSubject = candidate.base.get(word) >= 3;
      if (inTargetSubject || inCandidateSubject) {
        shared.push({ word, strength: weight * candidateWeight, direct: inTargetSubject && inCandidateSubject });
      }
    }
    if (!shared.length || !target.length || !candidate.length) return null;
    const score = shared.reduce((sum, item) => sum + item.strength, 0) / (target.length * candidate.length);
    if (score < 0.105 || !shared.some(item => item.direct)) return null;

    shared.sort((a, b) => Number(b.direct) - Number(a.direct) || b.strength - a.strength);
    const concepts = shared.filter(item => topicLabels.has(item.word));
    const cropMatch = concepts.find(item => item.direct && crops.has(topicLabels.get(item.word)));
    const focusMatch = concepts.find(item => item.direct && studyFocus.has(topicLabels.get(item.word)));
    if (!focusMatch && shared.length < 2) return null;
    const reasons = Array.from(new Set([focusMatch, cropMatch, ...concepts])).filter(Boolean);
    const labels = (reasons.length ? reasons : shared).slice(0, 2).map(({ word }) => {
      const label = topicLabels.get(word) || word;
      return caseSensitive.has(label) ? label : label.toLowerCase();
    });
    return {
      entry: candidate.entry,
      score: score + (cropMatch ? 0.2 : 0) + (focusMatch ? 0.14 : 0),
      reason: 'Sama-sama membahas ' + labels.join(' dan ')
    };
  }

  function createDiscovery(data) {
    let records;
    let profiles;
    const catalog = () => records ??= data.map(searchRecord);

    function search(value) {
      const text = String(value ?? '').trim();
      if (!text) return data.slice();
      const identifier = text.toLowerCase().replace(/^(?:https?:\/\/(?:dx\.)?doi\.org\/|doi:\s*)/, '');
      const query = normalize(text);
      if (!query) return [];
      const terms = queryTerms(query);
      const matches = [];
      for (const record of catalog()) {
        const score = scoreSearch(record, query, identifier, terms);
        if (score) matches.push({ entry: record.entry, score });
      }
      return matches.sort((a, b) => b.score - a.score || (b.entry.year || 0) - (a.entry.year || 0))
        .map(match => match.entry);
    }

    function related(entry, limit = 5) {
      if (entry.special || limit <= 0) return [];
      profiles ??= topicProfiles(catalog().filter(record => !record.entry.special));
      const target = profiles.find(profile => profile.entry.id === entry.id);
      if (!target) return [];
      const matches = [];
      for (const candidate of profiles) {
        const other = candidate.entry;
        if (other.id === entry.id) continue;
        if (entry.references?.includes(other.id)) {
          matches.push({ entry: other, score: 5, reason: 'Ditautkan dari ringkasan ini' });
        } else if (other.references?.includes(entry.id)) {
          matches.push({ entry: other, score: 4, reason: 'Ringkasannya menautkan kajian ini' });
        } else if ((entry.doi && other.doi?.toLowerCase() === entry.doi.toLowerCase()) || (entry.bib && other.bib === entry.bib)) {
          matches.push({ entry: other, score: 3, reason: 'Kajian yang sama di koleksi lain' });
        } else {
          const match = similarity(target, candidate);
          if (match) matches.push(match);
        }
      }
      return matches.sort((a, b) => b.score - a.score || b.entry.year - a.entry.year)
        .slice(0, limit).map(({ entry, reason }) => ({ entry, reason }));
    }

    return { search, related };
  }

  if (typeof module === 'object' && module.exports) module.exports = { methodsInTitle, createDiscovery };
  else window.createDiscovery = createDiscovery;
})();
