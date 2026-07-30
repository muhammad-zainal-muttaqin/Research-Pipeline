---
source_id: 177
bibtex_key: yin2023metric3d
title: Metric3D: Towards Zero-Shot Metric 3D Prediction from a Single Image
year: 2023
domain_theme: Estimasi Kedalaman
verified_pdf: 177_Metric3D.pdf
char_count: 100623
---

Metric3D: Towards Zero-shot Metric 3D Prediction from A Single Image

                                                                      Wei Yin1∗ , Chi Zhang2 *, Hao Chen3†, Zhipeng Cai4 , Gang Yu2 , Kaixuan Wang1 ,
                                                                                                Xiaozhi Chen1 , Chunhua Shen3
                                                                            1                    2            3                       4
                                                                              DJI Technology       Tencent      Zhejiang University     Intel Labs
                                                                                      1
                                                                               e-mail: {yvan.yin, halfbullet.wang, xiaozhi.chen}@dji.com;
                                                                                          2
                                                                                            {johnczhang, skicyyu}@tencent.com;
arXiv:2307.10984v1 [cs.CV] 20 Jul 2023

                                                                          3
                                                                            haochen.cad@zju.edu.cn, chunhua@me.com; 4 zhipeng.cai@intel.com

                                                                                                 RGB                                Point cloud                                   Point cloud
                                                                 iPhone 12 promax

                                                                  Meta Data:
                                                                  • Focal: 5.1𝑚𝑚
                                                                  • Pixelsize: 1.7𝜇𝑚
                                                                  • Size: 4032×3024
                                            Metrology

                                                                 Xiaomi 9

                                                                  Meta Data:
                                                                  • Focal: 4.8𝑚𝑚
                                                                  • Pixelsize: 1.6𝜇𝑚
                                                                  • Size: 4000×2250

                                                                             Ours (Metric reconstruction of photos captured by iPhone and Android phone)                   LeReS (No metric shape)
                                                                                                       Droid-SLAM                                 Droid-SLAM +Ours
                                            Dense SLAM Mapping

                                                                     Ground-                                      3D                                           3D
                                                                       truth                                    recon.                                       recon.
                                                                    trajectory

                                                                                                                                                           Blue: GT size
                                                                                                                                                           Red: measured size

                                                                                                        Predicted                                            Predicted
                                                                                                        trajectory                                           trajectory

                                         Figure 1 – Illustration and applications of our metric 3D reconstruction method. Top (metrology): we use two phones (iPhone 12 and an Android
                                         phone) to capture the scene and measure the size of tables. With the photos’ metadata, we perform 3D metric reconstruction and then measure tables’
                                         sizes (marked in red), which are very close to the ground truth (marked in blue). In contrast, the recent method LeReS [69] performs much worse and
                                         is unable to predict metric 3D by design. Bottom (dense SLAM mapping): existing SOTA mono-SLAM methods usually face scale drift problems (see
                                         the red arrows) in large-scale scenes and are unable to achieve the metric scale, while, naively inputting our metric depth, Droid-SLAM [52] can recover
                                         much more accurate trajectory and perform the metric dense mapping (see the red measurements). Note that all testing data are unseen to our model.

                                                                                       Abstract                                    art (SOTA) monocular metric depth estimation methods
                                                                                                                                   can only handle a single camera model and are unable
                                            Reconstructing accurate 3D scenes from images is a                                     to perform mixed-data training due to the metric ambigu-
                                         long-standing vision task. Due to the ill-posedness of the                                ity. Meanwhile, SOTA monocular methods trained on large
                                         single-image reconstruction problem, most well-established                                mixed datasets achieve zero-shot generalization by learning
                                         methods are built upon multi-view geometry. State-of-the-                                 affine-invariant depths, which cannot recover real-world
                                                                                                                                   metrics. In this work, we show that the key to a zero-shot
                                           * Equal contributions.                                                                  single-view metric depth model lies in the combination of
                                           † Corresponding author.

                                                                                                                               1
large-scale data training and resolving the metric ambi-           further or closer to another one. The application of relative
guity from various camera models. We propose a canoni-             depth is very limited. Learning affine-invariant depth finds
cal camera space transformation module, which explicitly           a trade-off between the above two categories of methods.
addresses the ambiguity problems and can be effortlessly           With large-scale data, they decouple the metric information
plugged into existing monocular models. Equipped with our          during training and achieve impressive robustness and gen-
module, monocular models can be stably trained over 8 mil-         eralization ability. The recent state-of-the-art LeReS [69]
lion of images with thousands of camera models, resulting          can recover 3D scenes in the wild, but only up to an un-
in zero-shot generalization to in-the-wild images with un-         known scale and shift.
seen camera settings.                                                  This work focuses on learning a zero-shot transferable
    Experiments demonstrate SOTA performance of our                model to recover metric 3D from a single image. First, we
method on 7 zero-shot benchmarks. Notably, our method              analyze the metric ambiguity issues in monocular depth es-
won the championship in the 2nd Monocular Depth Esti-              timation and study different camera parameters in depth, in-
mation Challenge. Our method enables the accurate recov-           cluding the pixel size, focal length, and sensor size. We ob-
ery of metric 3D structures on randomly collected internet         serve that the focal length is the critical factor for accurate
images, paving the way for plausible single-image metrol-          metric recovery. By design, LeReS [69] does not take the
ogy. The potential benefits extend to downstream tasks,            focal length information into account during training. As
which can be significantly improved by simply plugging             shown in Sec. 3.1, only from the image appearance, vari-
in our model. For example, our model relieves the scale            ous focal lengths may cause metric ambiguity, thus they de-
drift issues of monocular-SLAM (Fig. 1), leading to high-          couple the depth scale in training. To solve the problem of
quality metric scale dense mapping. The code is available          varying focal lengths, CamConv [15] encodes the camera
at https://github.com/YvanYin/Metric3D.                            model in the network, which enforces the network to im-
                                                                   plicitly understand camera models from the image appear-
                                                                   ance and then bridges the imaging size to the real-world
1. Introduction                                                    size. However, training data contains limited images and
    3D reconstruction from images is the core of many com-         types of cameras, which challenges data diversity and net-
puter vision applications, such as autonomous driving and          work capacity. In contrast, we propose a canonical cam-
robotics. Main-stream methods leverage multi-view geom-            era transformation method in training. It is inspired by the
etry [21] to confidently recover 3D structures. However,           human body reconstruction methods. To improve recon-
these methods cannot be applied to a single image, mak-            structed shape quality on countless poses, they map all sam-
ing 3D reconstruction hard without a prior. State-of-the-          ples to a canonical pose space [37] to reduce pose variance.
art transferable methods, such as MiDaS [40], LeReS [69],          Similarly, we transform all training data to a canonical cam-
and HDN [73], learn such a prior from a large dataset, but         era space where the processed images are coarsely regarded
they can only output affine-invariant depths, i.e., which are      as captured by the same camera. To achieve such transfor-
accurate only up to an unknown offset and scale. Though            mation, we propose two different methods. The first one
monocular metric depth estimation methods [71, 4] work             tries to adjust the image appearance to simulate the canoni-
on a single dataset with a single camera model, they cannot        cal camera, while the other one transforms the ground-truth
generalize to unseen cameras or scenes. This work aims to          labels for supervision. Camera models are not encoded in
address the above problems by learning a zero-shot, single         the network, making our method easily applicable to exist-
view, metric depth model.                                          ing architectures. During inference, a de-canonical trans-
    According to the predicted depth, existing methods are         formation is employed to recover metric information. To
categorized into learning metric depth [71, 64, 4, 63], learn-     further boost the depth accuracy, we propose a random pro-
ing relative depth [57, 58, 8, 7], and learning affine-invariant   posal normalization loss. It is inspired by the scale-shift
depth [69, 68, 40, 39, 73]. Although the metric depth meth-        invariant loss [69, 40, 73], which decouples the depth scale
ods [71, 64, 66, 4, 63] have achieved impressive accuracy on       to emphasize the single image’s distribution. However, they
various benchmarks, they must train and test on the dataset        perform on the whole image, which inevitably squeezes the
with the same camera intrinsics. Therefore, the training           fine-grained depth difference. We propose to randomly crop
datasets of metric depth methods are often small, as it is         several patches from images and enforce the scale-shift in-
hard to collect a large dataset covering diverse scenes us-        variant loss [69, 40] on them. Our loss emphasizes the local
ing one identical camera. The consequence is that all these        geometry and distribution of the single image.
models are not transferable – they generalize poorly to im-            With the proposed method, we can easily scale up model
ages in the wild, not to mention the camera parameters of          training to 8 million images from 11 datasets of diverse
test images can vary too. A compromise is to learn the rel-        scene types (indoor and outdoor) and camera models (tens
ative depth [8, 57], which only represents one point being         of thousands of different cameras), leading to zero-shot
transferability and a significantly improved accuracy. Our        methods [71, 66, 4] have dominated since then. Several ap-
model can accurately reconstruct metric 3D from randomly          proaches regress the continuous depth from the aggregation
collected Internet images, enabling plausible single-image        of information in an image [14]. As depth distribution cor-
metrology. Different from affine-invariant depth models,          responding to different RGBs can vary to a large extent,
our model can also directly improve various downstream            some methods [66, 4] discretize the depth and formulate
tasks. As an example (Fig. 1), with the predicted met-            this problem to a classification [64], which often achieves
ric depths from our model, we can significantly reduce the        better performance. The generalization issue of deep mod-
scale drift of monocular SLAM [52, 51] systems, achiev-           els for 3D metric recovery is related to two problems. The
ing much better mapping quality with real-world metric re-        first one is to generalize to diverse scenes, while the other
covery. Our model also enables large-scale 3D reconstruc-         one is how to predict accurate metric information under var-
tion [23]. The model achieves the championship in the             ious camera settings. The first problem has been well ad-
2nd Monocular Depth Estimation Challenge [50]. To                 dressed by recent methods. Some works [58, 57, 64] pro-
summarize, our main contributions are:                            pose to construct a large-scale relative depth dataset, such
                                                                  as DIW [7] and OASIS [8], and then they target learning
   • We propose a canonical and de-canonical camera               the relative relations. However, the relative depth loses ge-
     transformation method to solve the metric depth am-          ometric structure information. To improve the recovered
     biguity problems from various cameras setting. It en-        geometry quality, learning affine-invariant depth methods,
     ables the learning of strong zero-shot monocular met-        such as MiDaS [40], LeReS [69], and HDN [73] are pro-
     ric depth models from large-scale datasets.                  posed. By mixing large-scale data, state-of-the-art perfor-
   • We propose a random proposal normalization loss to           mance and the generalization over scenes are improved con-
     effectively boost the depth accuracy;                        tinuously. Note that by design, these methods are unable to
   • Our model achieves state-of-the-art performance on 7         recover the metric information. How to achieve both strong
     zero-shot benchmarks. It can perform high-quality 3D         generalization and accurate metric information over diverse
     metric structure recovery in the wild and benefit sev-       scenes is the key problem that we attempt to tackle.
     eral downstream tasks, such as mono-SLAM [52, 35],           Large-scale data training. Recently, various natural lan-
     3D scene reconstruction [23], and metrology [75].            guage problems and computer vision problems [65, 38, 29]
                                                                  have achieved impressive progress with large-scale data
2. Related Work                                                   training. CLIP [38] is a promising classification model,
                                                                  which is trained on billions of paired image and language
3D reconstruction from a single image. Reconstructing             descriptions data. It achieved state-of-the-art performance
various objects from a single image has been well stud-           over several classification benchmarks by zero-shot test-
ied [1, 54, 56]. They can produce high-quality 3D models          ing. For depth prediction, large-scale data training has been
of cars, planes, tables, and human body [41, 42]. The main        widely applied. Ranft et al. [40] mixed over 2 million data
challenge is how to best recover objects’ details, how to rep-    in training, LeReS [68] collected over 300 thousands data,
resent them with limited memory, and how to generalize to         Eftekhar et al. [13] also merged millions of data to build a
more diverse objects. However, all these methods rely on          strong depth prediction model.
learning priors specific to a certain object class or instance,
typically from 3D supervision, and can therefore not work         3. Method
for full scene reconstruction. Apart from these reconstruct-
ing objects works, several works focus on scene reconstruc-       Preliminaries. We consider the pin-hole camera model
tion [61] from a single image. Saxena et al. [43] construct       with intrinsic parameters are: [[fˆ/δ, 0, u0 ], [0, fˆ/δ, v0 ],
the scene based on the assumption that the whole scene can        [0, 0, 1]], where fˆ is the focal length (in micrometers), δ
be segmented into several small planes. With planes’ orien-       is the pixel size (in micrometers), and (u0 , v0 ) is the prin-
tation and location, the 3D structure can be represented. Re-     ciple center. f = fˆ/δ is the pixel-represented focal length
cently, LeReS [69] propose to use a strong monocular depth        used in vision algorithms.
estimation model to do scene reconstruction. However, they
                                                                  3.1. Metric Ambiguity Analysis
can only recover the shape up to a scale. Zhang et al. [74]
recently propose a zero-shot geometry-preserving depth es-            Fig. 3 presents an example of photos taken by different
timation model that is capable of making depth predictions        cameras and at different distances. Only from the image’s
up to an unknown scale, without requiring scale-invariant         appearance, one may think the last two photos are taken at
depth annotations for training. In contrast to these works,       a similar location by the same camera. In fact, due to differ-
our method can recover the metric 3D structure.                   ent focal lengths, these are captured at different locations.
Supervised monocular depth estimation. After several              Thus, camera intrinsic parameters are critically important
benchmarks [47, 17] are established, neural network based         for the metric estimation from a single image, as otherwise,
                    �   �   0   0
                                                                                                                                                         Metric 3D shape
                                                                  Canonical camera model

                                                                                                        De-canonical
                        Canonical                                                                      transformation
                          camera             Input Ic             Depth model Pred. depth D
                        transform.
                                                                                                       c                     Recov. metric
   Input I                module                (�� , �� , �� )                       Supervise                                depth D
    (�, �0 , �0 )                             �� , ��
                                                                  Transform                                                 : Unprojection
                                                                    Depth

                                                                              Transformed GT D*c                                                    Metric 3D shape
 Figure 2 – Pipeline. Given an input image I, we first transform it to the canonical space using CSTM. The transformed image Ic is fed into a standard
 depth estimation model to produce the predicted metric depth Dc in the canonical space. During training, Dc is supervised by a GT depth Dc∗ which
 is also transformed into the canonical space. In inference, after producing the metric depth Dc in the canonical space, we perform a de-canonical
 transformation to convert it back to the space of the original input I. The canonical space transformation and de-canonical transformation are executed
 using camera intrinsics.

                                                                                              (Fig. 4 (A)), the sensor size only affects the field of view
                                                                                              (FOV) and is irrelevant to α, thus does not affect the metric
                                                                                              depth estimation. For the pixel size, we assume two cam-
                                                                                              eras with different pixel sizes (δ1 = 2δ2 ) but the same focal
                                                                                              length fˆ to capture the same object locating at da . Fig. 4
                                                                                              (B) shows their captured photos. According to the prelimi-
                                                                                              naries, the pixel-represented focal length f1 = 12 f2 . As the
 focal=26 𝑚𝑚, depth=2 𝑚         focal=52 𝑚𝑚, depth=2 𝑚     focal=26 𝑚𝑚, depth=1 𝑚
                                                                                              second camera has a smaller pixel size, although in the same
 Figure 3 – Photos of a chair captured at different distances with dif-
 ferent cameras. The first two photos are captured at the same distance
                                                                                              projected imaging size Ŝ ′ , the pixel-represented image res-
                                                                                                                                                 ˆ         ˆ
 but with different cameras, while the last one is taken at a closer distance                 olution is S1′ = 21 S2′ . According to Eq. (1), δ1f·S ′ = δ2f·S ′ ,
                                                                                                                                                   1         2
 with the same camera as the first one.
                                                                                              i.e. α1 = α2 , so d1 = d2 . Therefore, different camera
the problem is ill posed. To avoid such metric ambigu-                                        sensors would not affect the metric depth estimation.
ity, recent methods, such as MiDaS [40] and LeReS [69],                                       O2: The focal length is vital for metric depth estimation.
decouple the metric from the supervision and compromise                                       Fig. 3 shows the metric ambiguity issue caused by the un-
learning the affine-invariant depth.                                                          known focal length. Fig. 5 illustrates this. If two cameras
    Fig. 4 (A) shows a simple pin-hole perspective projec-                                    (fˆ1 = 2fˆ2 ) are at distances d1 = 2d2 , the imaging sizes on
tion. Object A locating at da is projected to A′ . Based on                                   cameras are the same. Thus, only from the appearance, the
the principle of similarity, we have the equation:                                            network will be confused when supervised with different
                                       h fˆ i                                                 labels. Based on this observation, we propose a canonical
                            da = Ŝ  = Ŝ · α               (1)                               camera transformation method to solve the supervision and
                                Ŝ ′                                                          image appearance conflicts.
 where Ŝ and Ŝ ′ are the real and imaging size respectively.
                                                                                                                        𝐴
ˆ· denotes variables are in the physical metric (e.g., millime-
 ter). To recover da from a single image, focal length, imag-                                              𝐴′
 ing size of the object, and real-world object size must be                                       𝑂
 available. Estimating the focal length from a single image                                           𝑓መ
 is a challenging and ill-posed problem. Although several                                                       𝑑𝑎                      Resolution: 8 × 12    Resolution: 16 × 24
                                                                                                                  (A)                                        (B)
 methods [69, 22] have explored, the accuracy is still far
 from being satisfactory. Here, we simplify the problem by                                        Figure 4 – Pinhole camera model. (A) Object A at the distance da is
 assuming the focal length of a training/test image is avail-                                     projected to the image plane. (B) Using two cameras to capture the car.
                                                                                                  The left one has a larger pixel size. Although the projected imaging sizes
 able. In contrast, understanding the imaging size is much
                                                                                                  are the same, the pixel-represented images (resolution) are different.
 easier for a neural network. To obtain the real-world ob-
 ject size, a neural network needs to understand the semantic                                                               𝑑1 = 2𝑑2                                   𝑑2
 scene layout and the object, at which a neural network ex-                                                                                                                 𝑓෡2
                                                                                                                                    𝑓෡1 = 2𝑓෡2
 cels. We define α = fˆ/Sˆ′ , so da is proportional to α.
                                                                                              object 𝐴                                            object 𝐴           𝐴′2
    We make the following observations regarding sensor                                                                       𝐴1′
 size, pixel size, and focal length.
 O1: Sensor size and pixel size do not affect the met-
 ric depth estimation. Based on the perspective projection                                        Figure 5 – Illustration of two cameras with different focal length at
                                                                                                  different distance. As f1 = 2f2 and d1 = 2d2 , A is projected to two
                                                                                                                                                 ′    ′
                                                                                                  image planes with the same imaging size (i.e. A1 = A2 ).
3.2. Canonical Camera Transformation                               However, such normalization based on the whole image in-
                                                                   evitably squeezes the fine-grained depth difference, partic-
    The core idea is to set up a canonical camera space
                                                                   ularly in close regions. Inspired by this, we propose to ran-
((fxc , fyc ), fxc = fyc = f c in experiments) and transform
                                                                   domly crop several patches (pi(i=0,...,M ) ∈ Rhi ×wi ) from
all training data to this space. Consequently, all data can
                                                                   the ground truth D∗c and the predicted depth Dc . Then we
roughly be regarded as captured by the canonical camera.
                                                                   employ the median absolute deviation normalization [48]
We propose two transformation methods, i.e. either trans-
                                                                   for paired patches. By normalizing the local statistics, we
forming the input image (I ∈ RH×W ×3 ) or the ground-
                                                                   can enhance local contrast. The loss function is as follows:
truth (GT) label (D ∈ RH×W ). The original intrinsics are
{f, u0 , v0 }.                                                                   M N
                                                                                          d∗p ,j − µ(d∗pi ,j )
                                                                               1 XX
Method1: transforming depth labels (CSTM label).                   LRPNL =           | 1 PNi                   −
                                                                              MN p j             ∗           ∗
                                                                                           j dp ,j − µ(dp ,j )
Fig. 3’s ambiguity is for depths. Thus our first method di-                           i      N            i           i

rectly transforms the ground-truth depth labels to solve this                                         dpi ,j − µ(dpi ,j )
problem. Specifically, cwe scale the ground-truth depth (D∗ )                                    1
                                                                                                     PN                        | (3)
                                                                                                       j |dpi ,j − µ(dpi ,j )|
with the ratio ωd = ff in training, i.e., D∗c = ωd D∗ . The                                      N

original camera model is transformed to {f c , u0 , v0 }. In in-   where d∗ ∈ D∗c and d ∈ Dc are the ground truth and pre-
ference, the predicted depth (Dc ) is in the canonical space       dicted depth respectively. µ(·) and is the median of depth.
and needs to perform a de-canonical transformation to re-          M is the number of proposal crops, which is set to 32. Dur-
cover the metric information, i.e., D = ω1d Dc . Note the          ing training, proposals are randomly cropped from the im-
input I does not perform any transformation, i.e., Ic = I.         age by 0.125 to 0.5 of the original size. Furthermore, sev-
Method2: transforming input images (CSTM image).                   eral other losses are employed, including the scale-invariant
From another view, the ambiguity is caused by the similar          logarithmic loss [14] Lsilog , pair-wise normal regression
image appearance. Thus this method is to transform the in-         loss [69]LPWN , virtual normal loss [64] LVNL . Note Lsilog
put image to simulate the canonical camera imaging effect.    c    is a variant of L1 loss. The overall losses are as follows.
Specifically, the image I is resized with the ratio ωr = ff ,
i.e., Ic = T(I, ωr ), where T(·) denotes image resize. The               L = LPWN + LVNL + Lsilog + LRPNL .
optical center is resized, thus the canonical camera model
is {f c , ωr u0 , ωr v0 }. The ground-truth labels are resized     4. Experiments
without any scaling, i.e., D∗c = T(D∗ , ωr ). In inference,
the de-canonical transformation is to resize the prediction        Dataset details. We collect 11 public RGB-D datasets,
to the original size without scaling, i.e., D = T(Dc , ω1r ).      and over 8 million data for training. It spreads over diverse
    Fig. 2 shows the pipeline. After performing either trans-      indoor and outdoor scenes. Note that all datasets have pro-
formation, we randomly crop a patch for training. The crop-        vided camera intrinsic parameters. Apart from the test split
ping only adjusts the FOV and the optical center, thus not         of training datasets, we collect 7 unseen datasets for robust-
causing any metric ambiguity issues. c In the labels trans-        ness and generalization evaluation. Details of employed
formation method ωr = 1 and ωd = ff , while ωd = 1 and             data are reported in the supplementary materials.
        c                                                          Implementation details. We employ an UNet architec-
ωr = ff in the images transformation method. The training
                                                                   ture with the ConvNext-large [33] backbone. ImageNet-
objective is as follows:
                                                                   22K pre-trained weights are used for initialization. We
                    min |Nd (Ic , θ) − D∗c |                (2)    use AdamW with a batch size of 192, an initial learning
                     θ                                             rate 0.0001 for all layers, and the polynomial decaying
where θ is the network’s (Nd (·)) parameters, D∗c and Ic are       method with the power of 0.9. We train our final model
transformed ground-truth depth labels and images.                  on 48 A100 GPUs for 500K iterations. Following the Di-
   Mix-data training is an effective way to boost general-         verseDepth [64], we balance all datasets in a mini-batch to
ization. We collect 11 datasets for training, see the supple-      ensure each dataset accounts for an almost equal ratio. Dur-
mentary materials for details. In the mixed data, over 10K         ing training, images are processed by the canonical cam-
different cameras are included. All collected training data        era transformation module, flipped horizontally with a 50%
have included paired camera intrinsic parameters, which are        chance, and then randomly cropped into 512 × 960 pixels.
used in our canonical transformation module.                       For the ablation experiments, training settings are different
Supervision. To further boost the performance, we pro-             as we sample 5000 images from each dataset for training.
pose a random proposal normalization loss (RPNL). The              We trained on 8 GPUs for 150K iterations.
scale-shift invariant loss [40, 69] is widely applied for          Evaluation details. a) To show the robustness of our met-
the affine-invariant depth estimation, which decouples the         ric depth estimation method, we test on 8 zero-shot bench-
depth scale to emphasize the single image distribution.            marks, including NYUv2 [47], KITTI [17], NuScenes [6],
 Table 1 – Quantitative comparison on NYUv2 and KITTI benchmarks.             while ETH3D is 2000. We mainly compare with the SOTA
 Both datasets are unseen to our model, but we can achieve comparable
 performance with state-of-the-art methods.                                   metric depth estimation methods and take their NYUv2 and
                                NYUv2 Benchmark                               KITTI models for indoor and outdoor scenes evaluation re-
            Method       δ1 ↑    δ2 ↑    δ3 ↑  AbsRel↓   log10↓    RMS↓       spectively. From Tab. 3, we observe that although 7Scenes
       Li et al. [30]   0.788   0.958   0.991   0.143     0.063    0.635
   Laina et al. [28]    0.811   0.953   0.988   0.127     0.055    0.573      is similar to NYUv2 and NuScenes is similar to KITTI, ex-
         VNL [66]       0.875   0.976   0.994   0.108     0.048    0.416      isting methods face a noticeable performance decrease. In
      TrDepth [63]      0.900   0.983   0.996   0.106     0.045    0.365
        Adabins [4]     0.903   0.984   0.997   0.103     0.044    0.364
                                                                              contrast, our model is more robust.
    NeWCRFs [71]        0.922   0.992 0.998     0.095     0.041    0.334      Generalization over diverse scenes. Affine-invariant
 Ours CSTM image        0.925   0.983   0.994   0.092     0.040    0.341
  Ours CSTM label       0.944   0.986   0.995   0.083    0.035     0.310      depth benchmarks decouple the scale’s effect, which aims to
                                 KITTI Benchmark                              evaluate the model’s generalization ability to diverse scenes.
           Method        δ1 ↑    δ2 ↑    δ3 ↑ AbsRel ↓   RMS ↓    RMS log ↓   Recent impact works, such as MiDaS, LeReS, and DPT,
     Guo et al. [20]    0.902   0.969   0.986   0.090    3.258     0.168
         VNL [66]       0.938   0.990   0.998   0.072    3.258     0.117      achieved promising performance on them. Following them,
      TrDepth [63]      0.956   0.994   0.999   0.064    2.755     0.098      we test on 5 datasets and manually align the scale and shift
       Adabins [4]      0.964   0.995   0.999   0.058    2.360     0.088
    NeWCRFs [71]        0.974   0.997 0.999     0.052    2.129     0.079      to the ground-truth depth before evaluation. Results are re-
 Ours CSTM image        0.967   0.995 0.999     0.060    2.843     0.087      ported in Tab. 4. Although our method enforces the network
  Ours CSTM label       0.964   0.993   0.998   0.058    2.770     0.092
                                                                              to recover more challenging metric information, our method
7-scenes [46], iBIMS-1 [26], DIODE [53], ETH3D [45].                          outperforms them by a large margin on most datasets.
Following previous works [71], absolute relative error (Ab-
sRel), the accuracy under threshold (δi < 1.25i , i =                         4.2. Applications Based on Our Method
1, 2, 3), root mean squared error (RMS), root mean squared                        In these experiments, we apply the CSTM image model
error in log space (RMS log), and log10 error (log10) met-                    to various tasks.
rics are employed. b) Furthermore, we also follow current                     3D scene reconstruction . To demonstrate our work can re-
affine-invariant depth benchmarks [69, 73] (Tab. 4) to eval-                  cover the 3D metric shape in the wild, we first do the quan-
uate the generalization ability on 5 zero-shot datasets, i.e.,                titative comparison on 9 NYUv2 scenes, which are unseen
NYUv2, DIODE, ETH3D, ScanNet [11], and KITTI. We                              during training. We predict the per-frame metric depth and
mainly compare with large-scale data trained models. Note                     then fuse them together with provided camera poses. Re-
that in this benchmark we follow existing methods to apply                    sults are reported in Tab. 2. We compare with the video
the scale shift alignment before evaluation. c) To evaluate                   consistent depth prediction method (RCVD [27]), the unsu-
our metric 3D reconstruction quality, we randomly sample 9                    pervised video depth estimation method (SC-DepthV2 [5]),
unseen scenes from NYUv2 and use colmap [44] to obtain                        the 3D scene shape recovery method (LeReS [69]), affine-
the camera poses for multi-frame reconstruction. Cham-                        invariant depth estimation method (DPT [39]), and the
fer l1 distance and the F-score [25] are used to evaluate the                 multi-view stereo reconstruction method (DPSNet [23]).
reconstruction accuracy. d) In dense-SLAM experiments,                        Apart from DPSNet and our method, other methods have
following Li et al. [31], we test on the KITTI odometry                       to align the scale with the ground truth depth for each
benchmark [17] and evaluate the average translational RMS                     frame. Although our method does not aim for the video
drift (%, trel ) and rotational RMS drift (◦ /100m, rrel ) er-                or multi-view reconstruction problem, our method can
rors [17]. Note that all these depth and reconstruction eval-                 achieve promising consistency between frames and recon-
uations use the same trained model.                                           struct much more accurate 3D scenes than others on these
                                                                              zero-shot scenes. From the qualitative comparison in Fig. 6.
4.1. Zero-shot Generalization Test
                                                                              our reconstructions have much less noise and outliers.
Evaluation on metric depth benchmarks. To evaluate the                        Dense-SLAM mapping. Monocular SLAM is an important
accuracy of predicted metric depth, firstly, we compare with                  robotics application. It only relies on a monocular video in-
state-of-the-art (SOTA) metric depth prediction methods on                    put to create the trajectory and dense 3D mapping. Owing
NYUv2 [47], KITTI [18]. We use the same model to do                           to limited photometric and geometric constraints, existing
all evaluations. Results are reported in Tab. 1. Without any                  methods face serious scale drift problems in large scenes
fine-tuning or metric adjustment, we can achieve compara-                     and cannot recover the metric information. Our robust met-
ble performance with SOTA methods, which are trained on                       ric depth estimation method is a strong depth prior to the
benchmarks for hundreds of epochs.                                            SLAM system. To demonstrate this benefit, we naively in-
    Furthermore, We collect 6 unseen datasets to do more                      put our metric depth to the SOTA SLAM system, Droid-
metric accuracy evaluation. These datasets contain a wide                     SLAM [52], and evaluate the trajectory on KITTI. We do
range of indoor and outdoor scenes, including rooms, build-                   not do any tuning on the original system. Trajectory com-
ings, and driving scenes. The camera models are also var-                     parisons are reported in Tab. 5. As Droid-SLAM can access
ious, e.g. 7scenes has a short focal length (around 500),                     accurate per-frame metric depth, like an RGB-D SLAM, the
 Table 2 – Quantitative comparison of 3D scene reconstruction with LeReS [69], DPT [39], RCVD [27], SC-DepthV2 [5], and a learning-based MVS
 method (DPSNet [23]) on 9 unseen NYUv2 scenes. Apart from DPSNet and ours, other methods have to align the scale with ground truth depth for each
 frame. As a result, our reconstructed 3D scenes achieve the best performance.
               Basement 0001a Bedroom 0015 Dining room 0004 Kitchen 0008 Classroom 0004 Playroom 0002 Office 0024                      Office 0004 Dining room 0033
             Method
               C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑ C-l1 ↓ F-score ↑
    RCVD [27] 0.364 0.276 0.074 0.582 0.462               0.251   0.053 0.620 0.187 0.327 0.791 0.187 0.324 0.241 0.646 0.217 0.445                             0.253
SC-DepthV2 [5] 0.254 0.275 0.064 0.547 0.749              0.229   0.049 0.624 0.167 0.267 0.426 0.263 0.482 0.138 0.516 0.244 0.356                             0.247
   DPSNet [23] 0.243 0.299 0.195 0.276 0.995              0.186   0.269 0.203 0.296 0.195 0.141 0.485 0.199 0.362 0.210 0.462 0.222                             0.493
     DPT [69] 0.698 0.251 0.289 0.226 0.396               0.364   0.126 0.388 0.780 0.193 0.605 0.269 0.454 0.245 0.364 0.279 0.751                             0.185
    LeReS [69] 0.081 0.555 0.064 0.616 0.278              0.427   0.147 0.289 0.143 0.480 0.145 0.503 0.408 0.176 0.096 0.497 0.241                             0.325
         Ours 0.042 0.736 0.059 0.610 0.159               0.485   0.050 0.645 0.145 0.445 0.036 0.814 0.069 0.638 0.045 0.700 0.060                             0.663
    LeReS
    DPSNet
    Ours
    GT

 Figure 6 – Reconstruction of zero-shot scenes with multiple views. We sample several NYUv2 scenes for 3D reconstruction comparison. As our
 method can predict accurate metric depth, thus all frame’s predictions are fused together for scene reconstruction. By contrast, LeReS [69]’s depth is up
 to an unknown scale and shift, which causes noticeable distortions. DPSNet [23] is a multi-view stereo method, which cannot work well on low-texture
 regions.

translation drift (trel ) decreases significantly. Furthermore,                         4.3. Ablation Study
with our depths, Droid-SLAM can perform denser and more
accurate 3D mapping. An example is shown in Fig. 1 and                                  Ablation on canonical transformation. We study the ef-
more cases are shown in the supplementary materials.                                    fect of our proposed canonical transformation for the input
   We also test on the ETH3D SLAM benchmarks. Results                                   images (‘CSTM input’) and the canonical transformation
are reported in Tab. 6. Droid with our depths has much                                  for the ground-truth labels (‘CSTM output’). Results are
better SLAM performance. As the ETH3D scenes are all                                    reported in Tab. 7. We train the model on sampled mixed
small-scale indoor scenes, the performance improvement is                               data (55K images) and test it on 6 datasets. A naive base-
less than that on KITTI.                                                                line (‘Ours w/o CSTM’) is to remove CSTM modules and
Metrology in the wild. To show the robustness and accu-                                 enforce the same supervision as ours. Without CSTM, the
racy of our recovered metric 3D, we download Flickr pho-                                model is unable to converge when training on mixed met-
tos captured by various cameras and collect coarse cam-                                 ric datasets and cannot achieve metric prediction ability on
era intrinsic parameters from their metadata. We use our                                zero-shot datasets. This is why recent mixed-data training
CSTM image model to reconstruct their metric shape and                                  methods compromise learning the affine-invariant depth to
measure structures’ sizes (marked in red in Fig. 7), while                              avoid metric issues. In contrast, our two CSTM methods
the ground-truth sizes are in blue. It shows that our mea-                              both can enable the model to achieve the metric predic-
sured sizes are very close to the ground-truth sizes.                                   tion ability, and they can achieve comparable performance.
 Table 3 – Quantitative comparison with SOTA metric depth methods on 6 unseen benchmarks. For SOTA methods, we use their NYUv2 and KITTI
 models for indoor and outdoor scenes evaluation respectively, while we use the same model for all zero-shot testing.
                                               DIODE(Indoor) iBIMS-1            7Scenes                                                  DIODE(Outdoor) ETH3D              NuScenes
          Method
                                                        Indoor scenes (AbsRel↓/RMS↓)                                                              Outdoor scenes (AbsRel↓/RMS↓)
          Adabins [4]                          0.443 / 1.963      0.212 / 0.901 0.218 / 0.428                                            0.865 / 10.35       1.271 / 6.178 0.445 / 10.658
          NewCRFs [71]                         0.404 / 1.867      0.206 / 0.861 0.240 / 0.451                                            0.854 / 9.228       0.890 / 5.011 0.400 / 12.139
          Ours CSTM label                      0.252 / 1.440      0.160 / 0.521 0.183 / 0.363                                            0.414 / 6.934       0.416 / 3.017 0.154 / 7.097
          Ours CSTM image                      0.268 / 1.429      0.144 / 0.646 0.189 / 0.388                                            0.535 / 6.507       0.342 / 2.965 0.147 / 5.889
 Table 4 – Comparison with SOTA affine-invariant depth methods on 5 zero-shot transfer benchmarks. Our model significantly outperforms previous
 methods and sets new state-of-the-art. Following the benchmark setting, all methods have manually aligned the scale and shift.
                                                                                    NYUv2          KITTI         DIODE        ScanNet        ETH3D     Rank
                  Method Backbone                                     #Params
                                                                                AbsRel↓ δ1 ↑ AbsRel↓ δ1 ↑ AbsRel↓ δ1 ↑ AbsRel↓ δ1 ↑ AbsRel↓ δ1 ↑
 DiverseDepth [64] ResNeXt50 [60]    25M                                        0.117   0.875 0.190    0.704 0.376   0.631 0.108   0.882 0.228   0.694 7.7
       MiDaS [40] ResNeXt101         88M                                        0.111   0.885 0.236    0.630 0.332   0.715 0.111   0.886 0.184   0.752 7.2
        Leres [69] ResNeXt101                                                   0.090   0.916 0.149    0.784 0.271   0.766 0.095   0.912 0.171   0.777 5.4
     Omnidata [13] ViT-base                                                     0.074   0.945 0.149    0.835 0.339   0.742 0.077   0.935 0.166   0.778 4.9
        HDN [73] ViT-Large [12]      306M                                       0.069   0.948 0.115    0.867 0.246   0.780 0.080   0.939 0.121   0.833 3.7
    DPT-large [39] ViT-Large                                                    0.098   0.903 0.10     0.901 0.182   0.758 0.078   0.938 0.078   0.946 3.8
 Ours CSTM image ConvNeXt-large [33] 198M                                       0.058   0.963 0.053    0.965 0.211   0.825 0.074   0.942 0.064   0.965 1.3
  Ours CSTM label ConvNeXt-large                                                0.050   0.966 0.058    0.970 0.224   0.805 0.074   0.941 0.066   0.964 1.8
                                  Nikon                                                                                            Table 7 – Effectiveness of our CSTM. CamConvs [15] directly encodes
                                                                                     15.6m/GT: 26m

                                  D200
                                                                                                                                   various camera models in the network, while we perform a simple yet
                                                     49.2m /GT: 52m
                                                                                                                                   effective transformation to solve the metric ambiguity. Without CSTM,
                                                                                                                                   the model cannot achieve transferable metric prediction ability.
                                                                                                                                                     DDAD Lyft            DS             NS      KITTI NYU
                                                                                                                                   Method
                                                                                                                                                     Test set of train. data (AbsRel↓)   Zero-shot test set (AbsRel↓)
                                 iPhone X                                                                                          w/o CSTM          0.530      0.582 0.394              1.00    0.568      0.584
                                                                                                                                   CamConvs [15]     0.295      0.315 0.213              0.423 0.178        0.333
                                                                                                                                   Ours CSTM image   0.190      0.235 0.182              0.197 0.097        0.210
                                                                                                     2.2m/GT 1.7m

                                                                                                                                   Ours CSTM label   0.183      0.221 0.201              0.213 0.081        0.212
                                                     2.5m/GT 1.9m

                                 Canon
                                 600D
                                                                                                                                  Tab. 1 also shows comparable performance. Therefore,
                                                                                                                                  both adjusting the supervision and the input image appear-
                                                                                                                    3.1m/GT3.7m

                                                                                 10.9m /GT 12m
                                                                                                                                  ance during training can solve the metric ambiguity issues.
                                            2.6m/GT 2.5m                                                                          Furthermore, we compare with CamConvs [15], which en-
                                                                                                                                  codes the camera model in the decoder with a 4-channel
 Figure 7 – Reconstruction of in-the-wild scenes. We collect several                                                              feature. ‘CamConvs’ employ the same training schedule,
 Flickr photos, which are captured by various cameras. With photos’
                                                                                                                                  model, and training data as ours. This method enforces
 metadata, we reconstruct the 3D metric shape and measure structures’
 sizes. Red and blue marks are ours and ground-truth sizes respectively.                                                          the network to implicitly understand various camera mod-
 Table 5 – Comparison with SOTA SLAM methods on KITTI. We input
                                                                                                                                  els from the image appearance and then bridges the imaging
 predicted metric depth to the Droid-SLAM [52] (‘Droid+Ours’), which                                                              size to the real-world size. We believe that this method chal-
 outperforms others by a large margin on trajectory accuracy.                                                                     lenges the data diversity and network capacity, thus their
                                                                                                                                  performance is worse than ours.
               Seq 00    Seq 02     Seq 05       Seq 06        Seq 08   Seq 09         Seq 10
Method
                    Translational RMS drift (trel , ↓) / Rotational RMS drift (rrel , ↓)
                                                                                                                                  Ablation on canonical space. We study the effect of the
GeoNet [70]  27.6/5.72 42.24/6.14 20.12/7.67 9.28/4.34 18.59/7.85 23.94/9.81 20.73/9.1                                            canonical camera here, i.e., the canonical focal length. We
VISO2-M [49] 12.66/2.73 9.47/1.19 15.1/3.65 6.8/1.93 14.82/2.52 3.69/1.25 21.01/3.26
ORB-V2 [36] 11.43/0.58 10.34/0.26 9.04/0.26 14.56/0.26 11.46/0.28 9.3/0.26 2.57/0.32
                                                                                                                                  train the model on the small sampled dataset and test it on
Droid [52]   33.9/0.29 34.88/0.27 23.4/0.27 17.2/0.26 39.6/0.31 21.7/0.23 7/0.25                                                  the validation set of training data and testing data. The aver-
Droid+Ours   1.44/0.37 2.64/0.29 1.44/0.25 0.6/0.2             2.2/0.3 1.63/0.22 2.73/0.23
                                                                                                                                  age AbsRel error is calculated. We experiment on 3 differ-
                                                                                                                                  ent focal lengths, i.e., 500, 1000, 1500. Experiments show
 Table 6 – Comparison of VO error on ETH3D benchmark. Droid SLAM                                                                  that f ocal = 1000 has slightly better performance than oth-
 system is input with our depth (‘Droid + Ours’), and ground-truth depth
 (‘Droid + GT’). The average trajectory error is reported.
                                                                                                                                  ers, see Fig. 8 for details. Thus we set the canonical focal
                                                                                                                                  length to 1000 in our experiments.
               Einstein global    Manquin4     Motion1 Plantscene3 sfm house loop
                                                Average trajectory error (↓)
                                                                                    sfm lab room2
                                                                                                                                  Effectiveness of the random proposal normalization
Droid
Droid + Ours
               4.7
               1.5
                                  0.88
                                  0.69
                                               0.83
                                               0.62
                                                          0.78
                                                          0.34
                                                                          5.64
                                                                          4.03
                                                                                    0.55
                                                                                    0.53
                                                                                                                                  loss. To show the effectiveness of our proposed random
Droid + GT     0.7                0.006        0.024      0.006           0.96      0.013                                         proposal normalization loss (RPNL), we experiment on the
                                                                                                                                  sampled small dataset. Results are shown in Tab. 8. We test
                                                                                                                                  on the DDAD, Lyft, DrivingStereo (DS), NuScenes (NS),
 500       22.07
1000       19.82
1500       21.19

                                        Effect of Canonical Focal Length                                      Table 9 – Training and testing datasets used in experiments.
                                23      22.07                                                             Datasets                  Scenes    Label         Size        # Cam.
                   AbsRel (%)   22                                           21.19
                                21
                                                                                                                                   Training Data
                                                           19.82
                                20                                                                        DDAD [19]                 Outdoor LiDar           ∼80K        36+
                                19                                                                        Lyft [24]                 Outdoor LiDar           ∼50K        6+
                                18
                                         500               1000              1500                         Driving Stereo (DS) [62] Outdoor Stereo†          ∼181K       1
                                                       Focal Length                                       DIML [9]                  Outdoor Stereo†         ∼122K       10
                                                                                                          Arogoverse2 [55]          Outdoor LiDar           ∼3515K      6+
  Figure 8 – Effect of different canonical focal lengths. We experiment                                   Cityscapes [10]           Outdoor Stereo†         ∼170K       1
  on different canonical focal lengths and find that too large or small focal                             DSEC [16]                 Outdoor LiDar           ∼26K        1
  lengths will impact the performance.                                                                    Mapillary PSD [34]        Outdoor SfM‡            750K        1000+
                                                                                                          Pandaset [59]             Outdoor LiDar           ∼48K        6
  Table 8 – Effectiveness of random proposal normalization loss. Baseline                                 UASOL [2]                 Outdoor Stereo†         ∼137K       1
  is supervised by ‘LPWN + LVNL + Lsilog ’. SSIL is the scale-shift                                       Taskonomy [72]            Indoor    LiDar         ∼4M         ∼1M
  invariant loss proposed in [40].                                                                                                 Testing Data
                                     DDAD Lyft            DS             NS      KITTI NYUv2              NYU [47]                  Indoor    Kinect        654         1
  Method
                                     Test set of train. data (AbsRel↓)   Zero-shot test set (AbsRel↓)     KITTI [17]                Outdoor LiDar           652         4
  baseline                           0.204      0.251 0.184              0.207 0.104        0.230         ScanNet [11]              Indoor    Kinect        700         1
  baseline + SSIL [40]               0.197      0.263 0.259              0.206 0.105        0.216
                                                                                                          NuScenes (NS) [6]         Outdoor LiDar           10K         6
  baseline + RPNL                    0.190      0.235 0.182              0.197 0.097        0.210
                                                                                                          ETH3D [45]                Outdoor LiDar           431         1
 KITTI, and NYUv2. The ‘baseline’ employs all losses ex-                                                  DIODE [53]                In/Out    LiDar         771         1
 cept our RPNL. We compare it with ‘baseline + RPNL’ and                                                  7Scenes [46]              Indoor    Kinect        17k         1
                                                                                                          iBims-1 [26]              Indoor    LiDar         100         1
 ‘baseline + SSIL [40]’. We can observe that our proposed
                                                                                                          † ‘Stereo’: we use RaftStereo [32] to retrieve the pseudo ground truth.
 random proposal normalization loss can further improve the                                               ‡ ‘SfM’: pseudo ground truth is retrieved by structure from motion.
 performance. In contrast, the scale-shift invariant loss [40],
 which does the normalization on the whole image, can only
 slightly improve the performance.                                                                      images. We use draftstereo [32] to achieve pseudo ground-
                                                                                                        truth depths. Mapillary PSD [34] dataset provides paired
 5. Conclusion                                                                                          RGB-D, but the depth maps are achieved from a structure-
    In this paper, we tackle the problem of reconstructing the                                          from-motion method. The camera intrinsic parameters are
 3D metric scene from a single monocular image. To solve                                                estimated from the SfM. We believe that such achieved met-
 the depth ambiguity in image appearance caused by various                                              ric information is noisy. Thus we do not enforce learning-
 focal lengths, we propose a canonical camera space trans-                                              metric-depth loss on this data, i.e., Lsilog , to reduce the
 formation method. With our method, we can easily merge                                                 effect of noises. For the Taskonomy [72] dataset, we fol-
 millions of data captured by 10k cameras to train one metric                                           low LeReS [68] to obtain the instance planes, which are
 depth model. To improve the robustness, we collected over                                              employed in the pair-wise normal regression loss. During
 8M data for training. Several zero-shot evaluations show the                                           training, we employ the training strategy from [67] to bal-
 effectiveness and robustness of our work. We further show                                              ance all datasets in each training batch.
 the ability to do metrology on randomly collected internet                                                 The testing data is listed in Tab. 9. All of them are cap-
 images and dense mapping on large-scale scenes.                                                        tured by high-quality sensors. In testing, we employ their
                                                                                                        provided camera intrinsic parameters to perform our pro-
 Acknowledgements                                                                                       posed canonical space transformation.

    This work was in part supported by National Key R&D                                                 6.2. Details for Some Experiments
 Program of China (No. 2022ZD0118700).                                                                  Evaluation of zero-shot 3D scene reconstruction. In this
                                                                                                        experiment, we use all methods’ released models to predict
 6. Appendix                                                                                            each frame’s depth and use the ground-truth poses and cam-
                                                                                                        era intrinsic parameters to reconstruct point clouds. When
 6.1. Datasets and Training and Testing
                                                                                                        evaluating the reconstructed point cloud, we employ the it-
     We collect over 8M data from 11 public datasets for                                                erative closest point (ICP) [3] algorithm to match the pre-
 training. Datasets are listed in Tab. 9. The autonomous                                                dicted point clouds with ground truth by a pose transforma-
 driving datasets, including DDAD [19], Lyft [24], Driv-                                                tion matrix. Finally, we evaluate the Chamfer ℓ1 distance
 ingStereo [62], Argoverse2 [55], DSEC [16], and Pan-                                                   and F-score on the point cloud.
 daset [59], have provided LiDar and camera intrinsic and                                               Reconstruction of in-the-wild scenes. We collect several
 extrinsic parameters. We project the LiDar to image planes                                             photos from Flickr. From their associated camera metadata,
 to obtain ground-truth depths. In contrast, Cityscapes [10],                                           we can obtain the focal length fˆ and the pixel size δ. Ac-
 DIML [9], and UASOL [2] only provide calibrated stereo                                                 cording to fˆ/δ, we can obtain the pixel-represented focal
length for 3D reconstruction and achieve the metric infor-             scale high-resolution outdoor stereo dataset. Scientific data,
mation. We use meshlab software to measure some struc-                 6(1):1–14, 2019. 9
tures’ size on point clouds. More visual results are shown         [3] Paul Besl and Neil McKay. Method for registration of 3-d
in Fig. 11.                                                            shapes. In Sensor fusion IV: Control Paradigms and Data
Generalization of metric depth estimation. To evaluate                 Structures, volume 1611, pages 586–606. Spie, 1992. 9
our method’s robustness of metric recovery, we test on 8           [4] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.
                                                                       Adabins: Depth estimation using adaptive bins. In Proc.
zero-shot datasets, i.e. NYU, KITTI, DIODE (indoor and
                                                                       IEEE Conf. Comp. Vis. Patt. Recogn., pages 4009–4018,
outdoor parts), ETH3D, iBims-1, NuScenes, and 7Scenes.
                                                                       2021. 2, 3, 6, 8, 10
Details are reported in Tab. 9. We use the officially provided
                                                                   [5] Jia-Wang Bian, Huangying Zhan, Naiyan Wang, Tat-Jin
focal length to predict the metric depths. All benchmarks              Chin, Chunhua Shen, and Ian Reid. Auto-rectify network for
use the same depth model for evaluation. We don’t perform              unsupervised indoor depth estimation. IEEE Trans. Pattern
any scale alignment.                                                   Anal. Mach. Intell., 2021. 6, 7
Evaluation on affine-invariant depth benchmarks. We                [6] Holger Caesar, Varun Bankiti, Alex H Lang, Sourabh Vora,
follow existing affine-invariant depth estimation methods to           Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Gi-
evaluate 5 zero-shot datasets. Before evaluation, we em-               ancarlo Baldan, and Oscar Beijbom. nuscenes: A multi-
ploy the least square fitting to align the scale and shift with        modal dataset for autonomous driving. In Proc. IEEE Conf.
ground truth [69]. Previous methods’ performance is cited              Comp. Vis. Patt. Recogn., pages 11621–11631, 2020. 5, 9
from their papers.                                                 [7] Weifeng Chen, Zhao Fu, Dawei Yang, and Jia Deng. Single-
Dense-SLAM Mapping. This experiment is conducted on                    image depth perception in the wild. In Proc. Advances in
                                                                       Neural Inf. Process. Syst., pages 730–738, 2016. 2, 3
the KITTI odometry benchmark. We use our model to pre-
                                                                   [8] Weifeng Chen, Shengyi Qian, David Fan, Noriyuki Kojima,
dict metric depths, and then naively input them to the Droid-
                                                                       Max Hamilton, and Jia Deng. Oasis: A large-scale dataset
SLAM system as an initial depth. We do not perform any                 for single image 3d in the wild. In Proc. IEEE Conf. Comp.
finetuning but directly run their released codes on KITTI.             Vis. Patt. Recogn., pages 679–688, 2020. 2, 3
With Droid-SLAM predicted poses, we unproject depths               [9] Jaehoon Cho, Dongbo Min, Youngjung Kim, and
to the 3D point clouds and fuse them together to achieve               Kwanghoon Sohn.          DIML/CVL RGB-D dataset: 2m
dense metric mapping. More qualitative results are shown               RGB-D images of natural indoor and outdoor scenes. arXiv:
in Fig. 10.                                                            Comp. Res. Repository, 2021. 9
                                                                  [10] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo
6.3. More Visual Results                                               Rehfeld, Markus Enzweiler, Rodrigo Benenson, Uwe
                                                                       Franke, Stefan Roth, and Bernt Schiele. The cityscapes
Reconstructing 360◦ NuScenes scenes.          Current au-              dataset for semantic urban scene understanding. In Proc.
tonomous driving cars are equipped with several pin-hole               IEEE Conf. Comp. Vis. Patt. Recogn., 2016. 9
cameras to capture 360◦ views. Capturing the surround-            [11] Angela Dai, Angel X Chang, Manolis Savva, Maciej Hal-
view depth is important for autonomous driving. We sam-                ber, Thomas Funkhouser, and Matthias Nießner. Scannet:
pled some scenes from the testing data of NuScenes. With               Richly-annotated 3d reconstructions of indoor scenes. In
our depth model, we can obtain the metric depths for 6-ring            Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages 5828–
cameras. With the provided camera intrinsic and extrinsic              5839, 2017. 6, 9
parameters, we unproject the depths to the 3D point cloud         [12] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
and merge all views together. See Fig. 12 for details. Note            Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
that 6-ring cameras have different camera intrinsic param-             Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
eters. We can observe that all views’ point clouds can be              vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is
                                                                       worth 16x16 words: Transformers for image recognition at
fused together consistently.
                                                                       scale. Proc. Int. Conf. Learn. Representations, 2021. 8
Qualitative comparison of depth estimation.              In
                                                                  [13] Ainaz Eftekhar, Alexander Sax, Jitendra Malik, and Amir
Figs. 9, 13, 14, and 15, We show the qualitative compar-               Zamir. Omnidata: A scalable pipeline for making multi-task
ison of depth maps with Adabins [4], NewCRFs [71], and                 mid-level vision datasets from 3d scans. In Proc. IEEE Conf.
Omnidata [13]. Our results have much less artifacts.                   Comp. Vis. Patt. Recogn., pages 10786–10796, 2021. 3, 8,
                                                                       10
References                                                        [14] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map
                                                                       prediction from a single image using a multi-scale deep net-
 [1] Jonathan T Barron and Jitendra Malik. Shape, illumination,        work. In Proc. Advances in Neural Inf. Process. Syst., pages
     and reflectance from shading. IEEE Trans. Pattern Anal.           2366–2374, 2014. 3, 5
     Mach. Intell., 37(8):1670–1687, 2014. 3                      [15] Jose Facil, Benjamin Ummenhofer, Huizhong Zhou, Luis
 [2] Zuria Bauer, Francisco Gomez-Donoso, Edmanuel Cruz,               Montesano, Thomas Brox, and Javier Civera. CAM-
     Sergio Orts-Escolano, and Miguel Cazorla. Uasol, a large-         Convs: camera-aware multi-scale convolutions for single-
      RGB                     GT                      Ours                NewCRFs                   Adabins           Omnidata
                        Figure 9 – Depth estimation. The visual comparison of predicted on iBims, ETH3D, and DIODE.

     view depth. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn.,                monocular depth estimation. In Proc. IEEE Conf. Comp. Vis.
     pages 11826–11835, 2019. 2, 8                                            Patt. Recogn., 2020. 9
[16] Mathias Gehrig, Willem Aarents, Daniel Gehrig, and Davide          [20] Xiaoyang Guo, Hongsheng Li, Shuai Yi, Jimmy Ren, and
     Scaramuzza. Dsec: A stereo event camera dataset for driving             Xiaogang Wang. Learning monocular depth by distilling
     scenarios. IEEE Robotics and Automation Letters, 2021. 9                cross-domain stereo networks. In Proc. Eur. Conf. Comp.
[17] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel              Vis., pages 484–500, 2018. 6
     Urtasun. Vision meets robotics: The kitti dataset. Int. J.         [21] Richard Hartley and Andrew Zisserman. Multiple view ge-
     Robot. Res., 2013. 3, 5, 6, 9                                           ometry in computer vision. Cambridge university press,
[18] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we                 2003. 2
     ready for autonomous driving? the kitti vision benchmark           [22] Yannick Hold-Geoffroy, Kalyan Sunkavalli, Jonathan Eisen-
     suite. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages              mann, Matthew Fisher, Emiliano Gambaretto, Sunil Hadap,
     3354–3361. IEEE, 2012. 6                                                and Jean-François Lalonde. A perceptual measure for deep
[19] Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raven-              single image camera calibration. In Proc. IEEE Conf. Comp.
     tos, and Adrien Gaidon. 3d packing for self-supervised                  Vis. Patt. Recogn., pages 2354–2363, 2018. 4
                     Droid-SLAM

                                                                                          Droid-SLAM
                    Ours

                                                                                          Ours
         GT
      Trajectory                                                                GT
                                                                             Trajectory

                                                                                                Droid-SLAM
                                  Droid-SLAM

                       GT
                    Trajectory

                                                                                                Ours
                                  Ours

                                                                                GT
          GT                                                                 Trajectory
       Trajectory

 Figure 10 – Dense-SLAM Mapping. Existing SOTA mono-SLAM methods usually face scale drift problems in large-scale scenes and are unable to
 achieve the metric scale. We show the ground-truth trajectory and Droid-SLAM [52] predicted trajectory and their dense mapping. Then, we naively
 input our metric depth to Droid-SLAM, which can recover a much more accurate trajectory and perform the metric dense mapping.

[23] Sunghoon Im, Hae-Gon Jeon, Stephen Lin, and In-So                           erico Tombari, and Nassir Navab. Deeper depth prediction
     Kweon. Dpsnet: End-to-end deep plane sweep stereo. In                       with fully convolutional residual networks. In 2016 Fourth
     Proc. Int. Conf. Learn. Representations, 2019. 3, 6, 7                      international conference on 3D vision (3DV), pages 239–
[24] R. Kesten, M. Usman, J. Houston, T. Pandya, K. Nad-                         248. IEEE, 2016. 6
     hamuni, A. Ferreira, M. Yuan, B. Low, A. Jain, P. Ondruska,            [29] John Lambert, Zhuang Liu, Ozan Sener, James Hays, and
     S. Omari, S. Shah, A. Kulkarni, A. Kazakova, C. Tao, L.                     Vladlen Koltun. Mseg: A composite dataset for multi-
     Platinsky, W. Jiang, and V. Shet. Level 5 perception dataset                domain semantic segmentation. In Proc. IEEE Conf. Comp.
     2020. https://level-5.global/level5/data/,                                  Vis. Patt. Recogn., pages 2879–2888, 2020. 3
     2019. 9                                                                [30] Jun Li, Reinhard Klein, and Angela Yao. A two-streamed
[25] Arno Knapitsch, Jaesik Park, Qian-Yi Zhou, and Vladlen                      network for estimating fine-scaled depth maps from single
     Koltun. Tanks and temples: Benchmarking large-scale scene                   rgb images. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn.,
     reconstruction. ACM Trans. Graph., 36(4):1–13, 2017. 6                      pages 3372–3380, 2017. 6
[26] Tobias Koch, Lukas Liebel, Friedrich Fraundorfer, and                  [31] Shunkai Li, Xin Wu, Yingdian Cao, and Hongbin Zha. Gen-
     Marco Korner. Evaluation of cnn-based single-image depth                    eralizing to the open world: Deep visual odometry with
     estimation methods. In Eur. Conf. Comput. Vis. Worksh.,                     online adaptation. In Proc. IEEE Conf. Comp. Vis. Patt.
     pages 0–0, 2018. 6, 9                                                       Recogn., pages 13184–13193, 2021. 6
[27] Johannes Kopf, Xuejian Rong, and Jia-Bin Huang. Ro-                    [32] Lahav Lipson, Zachary Teed, and Jia Deng. Raft-stereo:
     bust consistent video depth estimation. In Proc. IEEE Conf.                 Multilevel recurrent field transforms for stereo matching. In
     Comp. Vis. Patt. Recogn., 2021. 6, 7                                        Int. Conf. 3D. Vis., 2021. 9
[28] Iro Laina, Christian Rupprecht, Vasileios Belagiannis, Fed-            [33] Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feicht-
                                                  Kodak
                                                  C913

                                                                                                      2.2m
                                                                                                             1.3m

                                                                3.3m

                                                                                3.4m
                                                                         3.4m
                                                 Olympus
                                                  X450

                                                                                 4.3m

                                                                                                                              4.5m
                                                 Panasonic
                                                 DMC-FS40

                                                                                                                    15.7m

                                                                                                                                     6.5m
                                                                                             5.6m

                                                  Fujifilm
                                                   X-T10
                                                                  4.9m

                                                                                                                      16.8m

                           RGB                            Point Cloud (view 1)                               Point Cloud (view 2)
Figure 11 – 3D metric reconstruction of in-the-wild images. We collect several Flickr images and use our model to reconstruct the scene. The focal
length information is collected from the photo’s metadata. From the reconstructed point cloud, we can measure some structures’ sizes. We can observe
that sizes are in a reasonable range.

                                                                                                                              Point Cloud of Car

             Ring RGBs & Depth                                              Point Cloud

Figure 12 – 3D reconstruction of 360◦ views. Current autonomous driving cars are equipped with several pin-hole cameras to capture 360◦ views.
With our model, we can reconstruct each view and smoothly fuse them together. We can see that all views can be well merged together without scale
inconsistency problems. Testing data are from NuScenes. Note that the front view camera has a different focal length from other views.

    enhofer, Trevor Darrell, and Saining Xie. A convnet for the                             11976–11986, 2022. 5, 8
    2020s. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages
                                                                                        [34] Manuel Lopez-Antequera, Pau Gargallo, Markus Hofinger,
            RGB                  GT                   Ours              NewCRFs                Adabins                Omnidata
                       Figure 13 – Depth estimation. The visual comparison of predicted on iBims, ETH3D, and DIODE.

     Samuel Rota Bulò, Yubin Kuang, and Peter Kontschieder.                 vision. In Proc. Int. Conf. Mach. Learn., pages 8748–8763.
     Mapillary planet-scale depth dataset. In Proc. Eur. Conf.               PMLR, 2021. 3
     Comp. Vis., volume 12347, pages 589–604, 2020. 9                   [39] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-
[35] Raul Mur-Artal and Juan D Tardós. Orb-slam2: An open-                  sion transformers for dense prediction. In Proc. IEEE Int.
     source slam system for monocular, stereo, and rgb-d cam-                Conf. Comp. Vis., pages 12179–12188, 2021. 2, 6, 7, 8
     eras. IEEE transactions on robotics, 33(5):1255–1262, 2017.        [40] René Ranftl, Katrin Lasinger, David Hafner, Konrad
     3                                                                       Schindler, and Vladlen Koltun. Towards robust monocular
[36] Raúl Mur-Artal and Juan D. Tardós. ORB-SLAM2: an                      depth estimation: Mixing datasets for zero-shot cross-dataset
     open-source SLAM system for monocular, stereo and RGB-                  transfer. IEEE Trans. Pattern Anal. Mach. Intell., 2020. 2, 3,
     D cameras. IEEE Trans. Robot., 33(5):1255–1262, 2017. 8                 4, 5, 8, 9
[37] Sida Peng, Shangzhan Zhang, Zhen Xu, Chen Geng, Boyi               [41] Shunsuke Saito, Zeng Huang, Ryota Natsume, Shigeo Mor-
     Jiang, Hujun Bao, and Xiaowei Zhou. Animatable neural                   ishima, Angjoo Kanazawa, and Hao Li. Pifu: Pixel-aligned
     implicit surfaces for creating avatars from videos. arXiv:              implicit function for high-resolution clothed human digitiza-
     Comp. Res. Repository, page 2203.08133, 2022. 2                         tion. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages
[38] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya                      2304–2314, 2019. 3
     Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,              [42] Shunsuke Saito, Tomas Simon, Jason Saragih, and Hanbyul
     Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learn-                Joo. Pifuhd: Multi-level pixel-aligned implicit function for
     ing transferable visual models from natural language super-             high-resolution 3d human digitization. In Proc. IEEE Conf.
             RGB                   GT                   Ours              NewCRFs                Adabins               Omnidata
                        Figure 14 – Depth estimation. The visual comparison of predicted on iBims, ETH3D, and DIODE.

     Comp. Vis. Patt. Recogn., pages 84–93, 2020. 3                      [46] Jamie Shotton, Ben Glocker, Christopher Zach, Shahram
[43] Ashutosh Saxena, Min Sun, and Andrew Y Ng. Make3d:                       Izadi, Antonio Criminisi, and Andrew Fitzgibbon. Scene co-
     Learning 3d scene structure from a single still image. IEEE              ordinate regression forests for camera relocalization in rgb-d
     Trans. Pattern Anal. Mach. Intell., 31(5):824–840, 2008. 3               images. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages
[44] Johannes Lutz Schönberger, Enliang Zheng, Marc Pollefeys,               2930–2937, 2013. 6, 9
     and Jan-Michael Frahm. Pixelwise view selection for un-             [47] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
     structured multi-view stereo. In Proc. Eur. Conf. Comp. Vis.,            Fergus. Indoor segmentation and support inference from
     2016. 6                                                                  rgbd images. In Proc. Eur. Conf. Comp. Vis., pages 746–760.
[45] Thomas Schops, Johannes L Schonberger, Silvano Galliani,                 Springer, 2012. 3, 5, 6, 9
     Torsten Sattler, Konrad Schindler, Marc Pollefeys, and An-          [48] Dalwinder Singh and Birmohan Singh. Investigating the im-
     dreas Geiger. A multi-view stereo benchmark with high-                   pact of data normalization on classification performance. Ap-
     resolution images and multi-camera videos. In Proc. IEEE                 plied Soft Computing, 2019. 5
     Conf. Comp. Vis. Patt. Recogn., pages 3260–3269, 2017. 6,           [49] Shiyu Song, Manmohan Chandraker, and Clark C Guest.
     9                                                                        High accuracy monocular sfm and scale correction for au-
            RGB                   GT                  Ours              NewCRFs                Adabins                Omnidata
                       Figure 15 – Depth estimation. The visual comparison of predicted on iBims, ETH3D, and DIODE.

     tonomous driving. IEEE Trans. Pattern Anal. Mach. Intell.,              In IEEE Conf. Comput. Vis. Pattern Recog. Worksh., pages
     38(4):730–743, 2015. 8                                                  3063–3075, June 2023. 3
[50] Jaime Spencer, C. Stella Qian, Michaela Trescakova, Chris          [51] Libo Sun, Wei Yin, Enze Xie, Zhengrong Li, Changming
     Russell, Simon Hadfield, Erich W. Graf, Wendy J. Adams,                 Sun, and Chunhua Shen. Improving monocular visual odom-
     Andrew J. Schofield, James Elder, Richard Bowden, Ali An-               etry using learned depth. IEEE Transactions on Robotics,
     war, Hao Chen, Xiaozhi Chen, Kai Cheng, Yuchao Dai,                     38(5):3173–3186, 2022. 3
     Huynh Thai Hoa, Sadat Hossain, Jianmian Huang, Mo-                 [52] Zachary Teed and Jia Deng. Droid-slam: Deep visual slam
     han Jing, Bo Li, Chao Li, Baojun Li, Zhiwen Liu, Ste-                   for monocular, stereo, and rgb-d cameras. volume 34, pages
     fano Mattoccia, Siegfried Mercelis, Myungwoo Nam, Mat-                  16558–16569, 2021. 1, 3, 6, 8, 12
     teo Poggi, Xiaohua Qi, Jiahui Ren, Yang Tang, Fabio Tosi,          [53] Igor Vasiljevic, Nick Kolkin, Shanyi Zhang, Ruotian Luo,
     Linh Trinh, S. M. Nadim Uddin, Khan Muhammad Umair,                     Haochen Wang, Falcon Z Dai, Andrea F Daniele, Moham-
     Kaixuan Wang, Yufei Wang, Yixing Wang, Mochu Xiang,                     madreza Mostajabi, Steven Basart, Matthew R Walter, et al.
     Guangkai Xu, Wei Yin, Jun Yu, Qi Zhang, and Chaoqiang                   Diode: A dense indoor and outdoor depth dataset. arXiv:
     Zhao. The second monocular depth estimation challenge.                  Comp. Res. Repository, page 1908.00463, 2019. 6, 9
[54] Nanyang Wang, Yinda Zhang, Zhuwen Li, Yanwei Fu, Wei             [67] Wei Yin, Xinlong Wang, Chunhua Shen, Yifan Liu, Zhi
     Liu, and Yu-Gang Jiang. Pixel2mesh: Generating 3d mesh                Tian, Songcen Xu, Changming Sun, and Dou Renyin. Di-
     models from single RGB images. In Proc. Eur. Conf. Comp.              versedepth: Affine-invariant depth prediction using diverse
     Vis., pages 52–67, 2018. 3                                            data. arXiv: Comp. Res. Repository, page 2002.00569, 2020.
[55] Benjamin Wilson, William Qi, Tanmay Agarwal, John Lam-                9
     bert, Jagjeet Singh, Siddhesh Khandelwal, Bowen Pan, Rat-        [68] Wei Yin, Jianming Zhang, Oliver Wang, Simon Niklaus, Si-
     nesh Kumar, Andrew Hartnett, Jhony Kaesemodel Pontes,                 mon Chen, Yifan Liu, and Chunhua Shen. Towards accurate
     Deva Ramanan, Peter Carr, and James Hays. Argoverse                   reconstruction of 3d scene shape from a single monocular
     2: Next generation datasets for self-driving perception and           image. IEEE Trans. Pattern Anal. Mach. Intell., 2022. 2, 3,
     forecasting. In Proc. Advances in Neural Inf. Process. Syst.,         9
     2021. 9                                                          [69] Wei Yin, Jianming Zhang, Oliver Wang, Simon Niklaus,
[56] Jiajun Wu, Chengkai Zhang, Xiuming Zhang, Zhoutong                    Long Mai, Simon Chen, and Chunhua Shen. Learning to
     Zhang, William Freeman, and Joshua Tenenbaum. Learning                recover 3d scene shape from a single image. In Proc. IEEE
     shape priors for single-view 3d completion and reconstruc-            Conf. Comp. Vis. Patt. Recogn., 2021. 1, 2, 3, 4, 5, 6, 7, 8, 10
     tion. In Proc. Eur. Conf. Comp. Vis., pages 646–662, 2018.       [70] Zhichao Yin and Jianping Shi. Geonet: Unsupervised learn-
     3                                                                     ing of dense depth, optical flow and camera pose. In Pro-
[57] Ke Xian, Chunhua Shen, Zhiguo Cao, Hao Lu, Yang Xiao,                 ceedings of the IEEE conference on computer vision and pat-
     Ruibo Li, and Zhenbo Luo. Monocular relative depth percep-            tern recognition, pages 1983–1992, 2018. 8
     tion with web stereo data supervision. In Proc. IEEE Conf.       [71] Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, and
     Comp. Vis. Patt. Recogn., pages 311–320, 2018. 2, 3                   Ping Tan. New CRFs: Neural window fully-connected CRFs
                                                                           for monocular depth estimation. In Proc. IEEE Conf. Comp.
[58] Ke Xian, Jianming Zhang, Oliver Wang, Long Mai, Zhe Lin,
                                                                           Vis. Patt. Recogn., 2022. 2, 3, 6, 8, 10
     and Zhiguo Cao. Structure-guided ranking loss for single
     image depth prediction. In Proc. IEEE Conf. Comp. Vis. Patt.     [72] Amir Zamir, Alexander Sax, , William Shen, Leonidas
     Recogn., pages 611–620, 2020. 2, 3                                    Guibas, Jitendra Malik, and Silvio Savarese. Taskonomy:
                                                                           Disentangling task transfer learning. In Proc. IEEE Conf.
[59] Pengchuan Xiao, Zhenlei Shao, Steven Hao, Zishuo Zhang,
                                                                           Comp. Vis. Patt. Recogn. IEEE, 2018. 9
     Xiaolin Chai, Judy Jiao, Zesong Li, Jian Wu, Kai Sun, Kun
                                                                      [73] Chi Zhang, Wei Yin, Zhibin Wang, Gang Yu, Bin Fu,
     Jiang, Yunlong Wang, and Diange Yang. Pandaset: Ad-
                                                                           and Chunhua Shen. Hierarchical normalization for robust
     vanced sensor suite dataset for autonomous driving. In IEEE
                                                                           monocular depth estimation. Proc. Advances in Neural Inf.
     Int. Intelligent Transportation Systems Conf., 2021. 9
                                                                           Process. Syst., 2022. 2, 3, 6, 8
[60] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and
                                                                      [74] Chi Zhang, Wei Yin, Gang Yu, Zhibin Wang, Tao Chen, Bin
     Kaiming He. Aggregated residual transformations for deep
                                                                           Fu, Joey Tianyi Zhou, and Chunhua Shen. Robust geometry-
     neural networks. In Proc. IEEE Conf. Comp. Vis. Patt.
                                                                           preserving depth estimation using differentiable rendering.
     Recogn., pages 1492–1500, 2017. 8
                                                                           In Proc. IEEE Int. Conf. Comp. Vis., 2023. 3
[61] Guangkai Xu, Wei Yin, Hao Chen, Chunhua Shen, Kai                [75] Rui Zhu, Xingyi Yang, Yannick Hold-Geoffroy, Federico
     Cheng, and Feng Zhao. Pose-free 3d scene reconstruction               Perazzi, Jonathan Eisenmann, Kalyan Sunkavalli, and Man-
     with frozen depth models. In Proc. IEEE Int. Conf. Comp.              mohan Chandraker. Single view metrology in the wild. In
     Vis., 2023. 3                                                         Proc. Eur. Conf. Comp. Vis., pages 316–333. Springer, 2020.
[62] Guorun Yang, Xiao Song, Chaoqin Huang, Zhidong Deng,                  3
     Jianping Shi, and Bolei Zhou. Drivingstereo: A large-scale
     dataset for stereo matching in autonomous driving scenarios.
     In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., 2019. 9
[63] Guanglei Yang, Hao Tang, Mingli Ding, Nicu Sebe, and
     Elisa Ricci. Transformer-based attention networks for con-
     tinuous pixel-wise prediction. In Proc. IEEE Int. Conf.
     Comp. Vis., 2021. 2, 6
[64] Wei Yin, Yifan Liu, and Chunhua Shen. Virtual normal: En-
     forcing geometric constraints for accurate and robust depth
     prediction. IEEE Trans. Pattern Anal. Mach. Intell., 2021. 2,
     3, 5, 8
[65] Wei Yin, Yifan Liu, Chunhua Shen, Anton van den Hengel,
     and Baichuan Sun. The devil is in the labels: Semantic seg-
     mentation from sentences. arXiv: Comp. Res. Repository,
     page 2202.02002, 2022. 3
[66] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     forcing geometric constraints of virtual normal for depth pre-
     diction. In Proc. IEEE Int. Conf. Comp. Vis., 2019. 2, 3, 6
