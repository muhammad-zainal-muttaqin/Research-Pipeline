---
source_id: 100
bibtex_key: hwang2015kaist
title: Multispectral Pedestrian Detection: Benchmark Dataset and Baseline
year: 2015
domain_theme: Pedestrian RGB-T
verified_pdf: 100_KAIST Multispectral Pedestrian.pdf
char_count: 64370
---

Multispectral Pedestrian Detection: Benchmark Dataset and Baseline

              Soonmin Hwang Jaesik Park Namil Kim Yukyung Choi In So Kweon
             Korea Advanced Institute of Science and Technology (KAIST), Republic of Korea
                 [smhwang,jspark,nikim,ykchoi]@rcv.kaist.ac.kr, iskweon77@kaist.ac.kr

                         Abstract

   With the increasing interest in pedestrian detection,
pedestrian datasets have also been the subject of research
in the past decades. However, most existing datasets focus
on a color channel, while a thermal channel is helpful for
detection even in a dark environment. With this in mind,
we propose a multispectral pedestrian dataset which pro-
vides well aligned color-thermal image pairs, captured by
beam splitter-based special hardware. The color-thermal
dataset is as large as previous color-based datasets and
provides dense annotations including temporal correspon-
dences. With this dataset, we introduce multispectral ACF,
which is an extension of aggregated channel features (ACF)
to simultaneously handle color-thermal image pairs. Multi-
spectral ACF reduces the average miss rate of ACF by 15%,
and achieves another breakthrough in the pedestrian detec-
tion task.

1. Introduction
   Pedestrian detection is an active research area in the field
                                                                      Figure 1. Examples of our multispectral pedestrian dataset. It has
of computer vision, since it is an essential and significant
                                                                      aligned pair of color (left column) and thermal (right column) im-
task for a surveillance or tracking system [6, 14, 24, 27, 28],
                                                                      ages captured from day/night traffic scenes. The dense annotations
as well as for pedestrian safety [9, 13, 15]. Although many           provided with the dataset such as green, yellow, and red boxes
researchers have studied various methods for a long time,             indicate no-occlusion, partial occlusion, and heavy occlusion re-
pedestrian detection is still regarded as a challenging prob-         spectively. Images are cropped for better visualization.
lem, limited by tiny and occluded appearances, cluttered
backgrounds, and bad visibility at night. In particular, even
though color cameras have difficulty getting useful infor-            infrared light wavelength of 9.3µm [25], which supports the
mation at night, most of the current pedestrian detectors are         suitability of thermal cameras for capturing humans.
based on color images.                                                    Based on these facts, in this paper we introduce a mul-
   To address these challenges for automobile applications,           tispectral pedestrian dataset1 which provides thermal im-
generally two types of infrared sensors are used: near in-            age sequences of regular traffic scenes as well as color im-
frared (0.75 ∼ 1.3µm) cameras or long-wavelength infrared             age sequences. This work is motivated by other computer
(7.5 ∼ 13µm, also known as the thermal band) cameras.                 vision datasets such as Caltech 101 [19], Oxford build-
Physically, pedestrians are more visible in thermal cam-              ings [23], Caltech pedestrian [10], and so on. These datasets
eras than in near infrared cameras. This is because long-             have been contributed to stimulate their respective research
wavelength infrared cameras are more robust to the interfer-          fields. Likewise, our multispectral dataset designed to sup-
ences produced by headlights and traffic signals. Even more             1 Our multispectral pedestrian dataset is available online:

importantly, a human body radiates in the long-wavelength             http://rcv.kaist.ac.kr/multispectral-pedestrian/

                                                                  1
port the study of appropriate use of color-thermal images
and to ultimately improve the accuracy of pedestrian detec-                            Three-axis
                                                                      Thermal          Camera Jig
tion.                                                                 Camera
   Our contributions are threefold: (1) We introduce the
multispectral pedestrian dataset, which provides aligned             Beam Splitter
color and thermal image pairs. Our dataset has num-
ber of image frames as large as widely used pedestrian                               RGB Camera
datasets [10, 15]. The dataset also contains nighttime traffic
sequences which are rarely provided or discussed in previ-       Figure 2. Our hardware configuration for capturing multispectral
ous datasets. (2) We analyze the complementary relation-         images. (Left) Top view. (Right) Mounted on the rooftop of a car.
ship between the color and thermal channels, and suggest
how to combine the strong points of the two channels in-
stead of using the color or thermal channel independently.
(3) We propose several combinations of extended ACF with
the thermal channel. One of our extensions reduces the
average miss rate by 15% on the proposed multispectral
                                                                 Figure 3. A hole pattern used for the color-thermal camera cali-
pedestrian dataset.
                                                                 bration. (Left) thermal image. (Middle) color image having color
   In constrast to most previous datasets utilizing a color-     distortion due to beam splitter. (Right) after color correction.
thermal stereo setup, we use beam splitter-based hardware
to physically align the two image domains. Therefore, our
dataset is free from parallax and does not require an image      has 320 × 256 pixels of spatial resolution with a 39◦ ver-
alignment algorithm for post processing. To the best of our      tical field of view. Note that the color camera has a larger
knowledge, this is the first work that provides aligned color    field of view than the thermal camera. We intended to use
and thermal image pairs captured in day and night. Exam-         the original thermal image in the aligned image domain by
ples of our dataset are shown in Fig. 1.                         sacrificing the border area of the color image. The frame
   We introduce our new dataset and analyze its statistics       rate of the two cameras is equal to 20 fps.
in Sec. 2. With our new dataset, in Sec. 3 we discuss the ex-
tensions of ACF [9] to handle additional information from        Camera calibration. The concept for our hardware was
the aligned thermal image. In Sec. 4, we evaluate the ef-        previously introduced by Bienkowski et al. [3] for nonde-
fectiveness of the additional channel in various conditions      structive evaluation purposes. Since the calibration method
by means of pedestrian detection performances. Lastly, we        for aligning two image domains is not mentioned in [3], we
summarize our findings and suggest future directions with        briefly introduce our calibration approach here. First, we
our dataset.                                                     compute a translation between the two cameras mounted
                                                                 on the hardware using stereo camera calibration. Here, we
                                                                 can regard that the optical axes of the two camera beyond
2. Multispectral Pedestrian Dataset
                                                                 the beam splitter are parallel due to the hardwired arrange-
    This section introduces our imaging hardware and the         ment. Therefore, there is only translation between the two
calibration procedure for capturing the aligned multispec-       image domains, and we only adjust the camera positions
tral images. An analysis of the dataset is described in the      using the three-axis jig until the translation becomes zero.
next section.                                                    After the adjustment, the two image domains are rectified to
                                                                 have the same virtual focal length. After these procedures,
2.1. Imaging Hardware                                            the two image domains share the same focal length and the
                                                                 same principal point and there is no baseline. The virtu-
Hardware specification. As shown in Fig. 2, we devel-            ally aligned image domain has 640 × 512 pixels of spatial
oped imaging hardware consisting of a color camera, a ther-      resolution, and has a 39◦ vertical field of view, which is as
mal camera, a beam splitter, and a three-axis camera jig.        similar to human vision. As a conventional checker board
The beam splitter in the system transmits the thermal band       pattern is not observable in a thermal camera, we used a
of the incident light and reflects the visible band. It also     special calibration board [16, 17] having a number of holes.
helps the optical center of the two cameras to be coincident.    When it is heated, there is a temperature difference between
The beam splitter is made of Zinc coated Silicon wafer for       the board and holes, which are therefore observable in the
this optical purpose. We used the PointGrey Flea3, a global      thermal camera. Examples of the hole pattern images are
shuttered color camera and the FLIR-A35 thermal camera.          shown in Fig. 3.
The color camera has 640 × 480 pixels of spatial resolution
with a 103.6◦ vertical field of view. The thermal camera         Color correction. The captured color image shows color
                                                                                                                                                                           200
                                                                                                    Far                Medium       Near
                                                                                       0.08 10.38%                     75.95%      13.67%
                                                                                                                                                                           160          Near
                                                                                                                                                                                         Near
                                                                                                                                                                                         Near

                                                                                                                                                person’s height (pixels)
                                                                                       0.06                                                                                                             115  pixel
                                                                                                                                                                                                        1.1e+002
                                                                                                                                                                                                        115 pixel pixel
                                                                                                                                                                           120

                                                                                prob
                                                                                       0.04
                                                                                                                                                                            80          Medium

                                                                                                                                                                                                                                45  pixel
                                                                                                                                                                                                                                45 pixel
                                                                                       0.02                                                                                 40
Figure 4. Image pairs captured by our hardware. (Left) thermal                                                                                                                          Far
                                                                                         0
image. (Middle) color image. (Right) blending of the two images.                                      32           64        128        256                                     0
                                                                                                                                                                                    0         5    10     15     20   25     30             35   40
                                                                                                                height (pixels)                                                                      Distance from camera (m)

                                                                                       (a) Distribution of peds. height                                                                  (b) Distance vs height
distortion because the reflection ratios of the visible band
                                                                                Figure 5. We define evaluation conditions with respect to the scale.
from the beam splitter are uneven depending on the incident                     Considering the general driving speed and the braking distances,
light directions (shown as Fig. 3). To handle this problem,                     we set 45 pixel and 115 pixel to the criteria of scale conditions.
we capture a reference which is an image of a white plane                       More than 75 % of pedestrians belong to medium scale. It means
but showing the color distortion. As our color camera has                       the detection algorithms try to focus on this condition.
a linear camera response function, the reference image is                                                                                                                   5
                                                                                                                                                                           10

equivalent to the per-pixel reflection coefficient of the vis-                  50
                                                                                                                                                                            4
                                                                                100                                                                                        10
ible band. Therefore, we alleviate the color distortion by

                                                                                                                                              # images (Log−scale)
                                                                                150

dividing the intensity level of captured images with these                      200
                                                                                                                                                                            3
                                                                                                                                                                           10

                                                                                250
reflection coefficients.                                                        300
                                                                                                                                                                            2
                                                                                                                                                                           10

                                                                                350

2.2. Data Collection and Ground truth                                           400
                                                                                                                                                                            1
                                                                                                                                                                           10

                                                                                450
                                                                                                                                                                            0
                                                                                                                                                                           10
Data capture. The hardware is mounted on the roof of a                          500
                                                                                              100         200    300     400    500    600
                                                                                                                                                                                         1−2      3−4    5−6      7−8     9−10 11−12 13−14
                                                                                                                                                                                                        # peds. in an image

car, and used for capturing ego-centric images of the traf-                       (a) Distribution of peds. centers                                                    (b) Number of peds. per frame
fic scenes. In particular, we captured various scenes at day
and night time to consider changes in light conditions. An                      Figure 6. (a) Due to the right-handed traffic condition, most pedes-
example of proposed dataset is shown in Fig. 4.                                 trians appear at the right side of the image. (b) The proposed
                                                                                dataset contains a lot of crowded scenes.
Ground truth annotation. Among the grabbed frames,
95,328 color-thermal pairs2 were manually annotated for
the total of 103,128 dense annotations and 1,182 unique                         Train and Test sets. To divide annotated color-thermal im-
pedestrians. To annotate the ground truth, we used Piotr’s                      age pairs into train and test datasets, we used the follow-
Computer Vision Toolbox[8], but it was modified to display                      ing criterion. First, the numbers of pedestrians appearing
color and thermal images simultaneously. The modifica-                          in the two sets were similar. Second, the frame numbers of
tion helps with annotation because a distant pedestrian at                      day/night images in the two sets were similar. Third, the
nighttime is rarely observable in the color channel. We also                    two sets were not overlapped. Compared to random divi-
modified the toolbox to give occlusion tags instead of oc-                      sion, this scheme helps to avoid data bias and over-fitting
clusion regions for each bounding box. Similar to Dollár et                    on a certain scene.
al. [10], the object has one of four labels. Obviously an
individual pedestrian was labeled as a person. Not distin-                      2.3. Properties of Dataset
guishable individuals were labeled as people. People rid-
                                                                                Scale. Since the key application of pedestrian detection
ing a two-wheeled vehicle were labeled as cyclist. In a
                                                                                is accident avoidance, we classified the size of annotated
highly cluttered scene, even human annotators sometimes
                                                                                bounding boxes based on the braking distance of the vehi-
cannot clearly determine whether a human shaped object
                                                                                cles. In urban areas where pedestrians usually appear, we
is a pedestrian or not. This object is labeled as person?
                                                                                regarded the general driving speed as 30 ∼ 55 km/h. The
and it is ignored in the evaluation3 . After the annotation,
                                                                                expected braking distances under this driving condition are
the bounding boxes also have temporal correspondences in-
                                                                                11 ∼ 28 m (including braking delay due to the reaction of
dicating the person index over the frames. In our dataset,
                                                                                drivers) [7]. That corresponds to 45 ∼ 115 pixels of height
a person appears 74.80 frames on average (corresponds to
                                                                                in our aligned image domain if the height of the pedestri-
3.74 seconds).
                                                                                ans is around 1.7m. We classified the annotations within
    2 Note that the frame number was not enlarged by horizontal mirroring.      these sizes as medium. As shown in Fig. 5(a), near and far,
However, in the training stage of the baseline algorithm, we mirrored the       which are smaller or larger than medium, were also deter-
positive samples to make more general examples.
    3 In our dataset, the number of person? is only 1,434 (1.66%) compared      mined. Figure 5(b) shows the relation between the pedes-
to a total of 86,152 person annotations. Therefore, it does not significantly   trian’s height in pixel units and its corresponding distance
affect the reliability of the evaluation result.                                in meters.
                           Examples                                                      Training                      Testing                                    Properties

                                                                                                                                                                aligned channels
                                                                                                                                                                temporal corr.
                                                                                                                                               # total frames
                                                                                         # pedestrians

                                                                                                                    # pedestrians

                                                                                                                                                                moving cam.
                                                              Color

                                                                                                                                                                publication
                                                                                                                                                                video seqs.
                                                                                                                                                                occ. labels
                                                                                                         # images

                                                                                                                                    # images

                                                                                                                                                                thermal
                                                                                                                                                                color
 Day

                                                              Thermal
                                                                        INRIA [4]     1.2k 1.2k 566 741 2.5k       X           ‘05
                                                                        ETHZ [14]     2.4k 499 12k 1.8k            X     X     ‘08
                                                                        Daimler [13] 15.6k 6.7k 56.4k 21.8k 28.5k X X X        ‘09
                                                                        Caltech [10] 192k 128k 155k 121k 250k X X X X X ‘09
                                                                        KITTI [15]    12k 1.6k     –     –   80k X X X X       ‘12

                                                              Color
                                                                        OSU-T [5]     984 1.9k     –     –   0.2k    X X       ‘05
                                                                        LSI [21]     10.2k 6.2k 5.9k 9.1k 15.2k      XXX       ‘13
 Night

                                                                        ASL-TID [24] – 5.6k        – 1.3k 4.3k       X X       ‘14
                                                                        TIV [28]        –    –     –     –   63k     X X       ‘14

                                                              Thermal
                                                                        OSU-CT [6]      –    –     –     –   17k   X X X X ‘07
                                                                        LITIV [27]      –    – 16.1k 5.4k 4.3k     X X X X ‘12
                                                                        Ours         41.5k 50.2k 44.7k 45.1k 95k X X X X X X X ‘15

Figure 7. Examples of annotated pedestrians with no occlusion tag.      Table 1. Comparison of several pedestrian datasets. The horizon-
It shows color and thermal image pairs at day and night times.          tal lines divide the image types of the dataset (color, thermal, and
                                                                        color-thermal) based on the image types. The first four columns
                                                                        indicate number of pedestrian and images in the training and test-
Occlusion. If a pedestrian is suddenly occluded by other                ing dataset (k = 103 ). Properties column summarizes additional
pedestrians or objects in the scene, we annotated it with one           characteristics of the datasets. Note that our dataset is largest
of the three occlusion tags. Pedestrians who were never oc-             color-thermal dataset providing occlusion labels and temporal cor-
                                                                        respondences captured in a non-static traffic scene.
cluded were tagged as no occlusion; those occluded to some
extent up to one half were tagged as partial occlusion; and
those whose contour was mostly occluded were tagged as                  better performance by using the strong points of the color
heavy occlusion. Among the total annotations, over 75%                  and the thermal images throughout the day.
of pedestrians were tagged not occluded (78.6%), and the
remainder were partial occlusion (12.6%) and heavy occlu-               2.4. Comparison to Existing Datasets
sion (8.8%).                                                                Table 1 provides a summary of existing pedestrian
Position. Figure 6 (a) shows the center of annotated pedes-             datasets. According to the image type, the datasets are clas-
trians represented as the distribution of a Gaussian mixture            sified into: color, thermal, and color-thermal.
model. Our hardware was set up to cover the view of a gen-                  Most of the existing color datasets [4, 10, 13, 14, 15] pro-
eral driver. This setup constrains the appearance of pedes-             vide color image sequences captured in daytime under fine
trians in certain regions. Therefore, pedestrians were dis-             weather conditions. Caltech [10] and KITTI [15] in partic-
tributed in a narrow band across the center of the image.               ular are the most widely used datasets having various real
Pedestrians mostly appear at the right side of the image, be-           driving scenarios. Caltech [10] has the largest number of
cause the car drives under the right-handed traffic condition.          frames in the video format. They also have temporal corre-
We also show the number of pedestrians per frame in log-                spondences of the bounding boxes, which give an identifi-
normalized scale in Fig. 6 (b).                                         cation index over the frame in the same target. KITTI [15]
                                                                        is used for validating various computer vision applications
Appearance change. Figure 7 shows several examples of                   such as stereo vision, optical flow, visual SLAM, and object
pedestrians in the day and night time. The color image in               detection using color images only.
daytime shows a distinct human shape due to the strong                      Thermal datasets [5, 21, 24, 28] are usually designed
sunlight. On the other hand, the shape in the color image               for object detection and tracking. The OSU-T dataset [5]
at nighttime is not distinguishable due to the dark environ-            is made for benchmarking tracking algorithms, and some
ment. However, the thermal image shows a distinct shape                 datasets provide a trajectory instead of a bounding box [24,
at nighttime, because the temperature difference is greater             28]. Olmeda et al. [21] provides a pedestrian detection
when the air temperature is cooler, so the pedestrians hav-             dataset captured by thermal camera on a moving vehicle.
ing a fixed temperature, can be clearly captured in the night-          Notable benchmark, referred to as TIV [28], provides multi-
time. In the daytime, the strong sun radiation causes back-             view or multi-resolution image sequences, and have anno-
ground clutters. For these reasons, we can expect to obtain             tated labels such as person, bat, runner, bicycle, motorcycle,
and car. In addition, TIV [28] provides a high resolution
thermal image (up to 1024×1024) and provides the largest
number of frames among the thermal datasets.
    Our approach is classified as color-thermal dataset as
it provides aligned color and thermal images. Compared
to [6, 27], our dataset has an ego-centric moving view of
the traffic scene, and provides a much larger number of an-
notated frames. In addition, our approach provides tempo-
ral correspondences and occlusion labels, which are use-                      (a) ACF                 (b) Multispectral ACF
ful information for pedestrian detection, identification, and    Figure 8. Linear discriminant analysis (LDA) on the ACF and mul-
tracking. Our setup is also related to the pedestrian detec-     tispectral ACF features. The high dimensional features are pro-
tion system [18] which consists of a pair of color cameras       jected into 2D domain using LDA. In the above two figures, red
and a infrared camera. However, compared to our system, it       and blue dots indicate positive and negative samples respectively.
requires additional stereo matching of the color images and      By adding thermal channels, the positive and negative samples be-
aligns color-thermal image pairs using a trifocal tensor.        come more distinctive.

3. Baseline Approaches
                                                                 ACF is the aforementioned feature defined for the color
    To handle the color and thermal channels effectively, our    channel. T, T+TM+TO, and T+THOG indicates the addi-
baseline algorithm is built upon the aggregated channel fea-     tional channel features augmented from the thermal chan-
tures (ACF) pedestrian detector [9]. This is natural choice      nel. The individual explanations follow.
because the algorithm can accommodate multiple channels
                                                                 T. This channel feature uses the thermal intensity directly.
showing different modalities. For instance, it uses chro-
                                                                 To improve the detection performance, we enhanced the
matic and gradient channels augmented from a single color
                                                                 contrast of the image using histogram equalization.
image. In this manner, the thermal channel can be regarded
as another augmented channel in this algorithm. Here, we         T+TM+TO. This extension consists of three channels: T,
benefit from our capturing hardware because the alignment        TM and TO. T is the aforementioned thermal channel, TM
problem between color and thermal channels is removed. In        is the normalized gradient magnitude of the thermal images,
addition, the ACF pedestrian detector [9] is widely used as      TO is the histogram of oriented gradients of the thermal im-
a basis algorithm for the concurrent state-of-the-art pedes-     ages. The TM and TO are acquired from the same method
trian detectors [20, 22, 29].                                    as standard ACF.
    With this idea, we first review standard ACF designed        T+THOG. This extension uses the T and HOG feature [4]
for color images and introduce our extension to additionally     of the thermal image (denoted as THOG). Compared to TO
handle the thermal channel.                                      which computes 6 directions of histograms, THOG com-
3.1. Standard ACF                                                putes more gradient orientations and has additional normal-
                                                                 ization steps on the local histograms.
    For color image input, the standard ACF [9] have 10 aug-
mented channels (LUV+M+O): LUV denotes 3 channels                   Note that the three extensions utilize the intensity and
of CIELUV color space, M denotes 1 channel of gradient           gradient information of the thermal channel. We were mo-
magnitude, and O denotes 6 channels of gradient histogram        tivated by recent work [26] which utilized gradients of a
which is a simplified version of histogram of oriented gra-      thermal image as an important cue. We self-evaluated these
dients (HOG) [4]. In ACF [9], they utilize the bootstrap-        extensions on various conditions: different scales, occlu-
ping procedure which is to mine hard negatives among a           sion tags, and capturing time (day or night). The result in
tremendous number of negatives, and re-train the AdaBoost        Fig. 10 indicates that the three extensions outperforms ACF,
classifier [1] several times. Finally, they apply an efficient   and ACF+T+THOG shows the best performance. This is
rejection method called soft cascade to boost detection time.    because ACF+T+THOG has most elaborate representation
In this manner, a powerful pedestrian detection framework        of the human shape. Based on this observation, we selected
is constructed.                                                  ACF+T+THOG as a desirable combination for the channel
                                                                 feature, and we name it multispectral ACF for the ramain-
3.2. Multispectral ACF                                           der of this paper.
   We utilized the ACF pedestrian detector [9] as our base-
                                                                 3.3. Analysis of Multispectral ACF
line and extended it to encode the thermal intensity channel.
For the extension, we suggest three baselines as follows:           We compared the multispectral ACF to standard ACF to
(1) ACF+T (2) ACF+T+TM+TO (3) ACF+T+THOG. Here,                  observe the benefits that resulted from the thermal channel.
                                                70               70

                                                65               65
                                                                      the voting map of the multispectral ACF, shown in Fig. 9
                                                60               60
                                                                      (d), displays gathered votes in the upper part of the human
                                                55               55
                                                                      shape. This visualization implies that the multispectral ACF
                                                50               50
                                                                      can build a more spatially concentrated feature set.
                                                45               45

                                                40               40
                                                                      4. Experimental Results
                                                35               35

                                                30               30      To measure the effectiveness of the thermal channel in
 (a) Avg. using (b) Avg. using (c) Voting map     (d) Voting map      various conditions, we evaluated the ACF and its extended
  color images thermal images       (ACF)       (multispectral ACF)   candidates as described in Sec. 3.2. For all these experi-
Figure 9. Average images of annotated pedestrians using (a) color     ments, the detectors were trained and tested on the proposed
channel and (b) thermal channel. (c, d) voting maps indicating        dataset using the public ACF implementation[8]. Since our
frequently used feature grid. The voting map of multispectral ACF     focus was on evaluating the effect of the thermal channel,
is more concentrated around the upper part of human body.             the parameters were fixed in all experiments. We plotted
                                                                      the miss rate using a per-image evaluation scheme (FPPI)
                                                                      and summarized the performance with a single value by us-
Distinctiveness of multispectral ACF. For the qualitative             ing log-average miss rate over the range of [10−2 , 100 ] as
analysis, we trained the AdaBoost classifier [1] using ACF            suggested by Dollar et al.[10] Figure 10 shows the evalua-
and multispectral ACF, respectively. After the training, each         tion results for the various subsets of the test set described
classifier had two groups of features belonging to either             below.
the hard negative class or the positive class. Here, we ap-
plied linear discriminant analysis (LDA) [11] to the two              Day and night. For this experiment, we used a sub-
groups of features to visualize their distribution. LDA finds         set named reasonable which is a representative subset of
an optimal projection vector which minimizes a variance               the proposed dataset. The reasonable subset consists of
of the same class and maximizes a variance of the differ-             not/partially occluded pedestrians which are larger than 55
ent classes. In this manner, features are projected into 2D           pixels. The dataset is divided into reasonable day and rea-
spaces, and one of the results are shown in Fig. 8.                   sonable night based on the capturing time. In Fig. 10 (a), all
                                                                      three extensions using a color-thermal channel performed
   For the quantitative analysis, we introduce the following
                                                                      better than ACF using only the color channel. This is valid
steps to measure the distance between positive and negative
                                                                      regardless of daytime or nighttime as shown in Fig. 10 (b),
features. The analysis was separately applied to the two
                                                                      (c). Apparently, in case of the nighttime when the pedes-
feature groups obtained from ACF and multispectral ACF.
                                                                      trian is hardly distinguishable in the color image, the ther-
First, for each of the feature groups, we applied k-means
                                                                      mal channel seems to be dominant at detecting pedestrians.
clustering [12]. Second, we made histograms of positive
and negative features by binning the corresponding cluster            Scale. In this experiment, we examined trained detectors
labels. Third, we measured the distance between the posi-             using three subsets of the dataset which were defined based
tive and negative histograms. As a result, the Bhattacharyya          on the size of the bounding box. As shown in Fig. 6, these
distance [2] using multispectral ACF was found to be larger           were classified into near (∼28 m, 115 pixels∼), medium
(0.65) than the distance using the ACF (0.43). This implies           (11∼28 m, 45∼115 pixels) and far (28 m∼, ∼45 pixels).
that the multispectral ACF shows more distinctiveness than            These subsets contain non-occluded pedestrians captured
the ACF.                                                              in daytime and nighttime. As shown in Fig. 10 (d)-(f),
                                                                      the multispectral ACF generally outperforms ACF on the
Frequently used local features. Figure 9 (a-b) show the
                                                                      three scales. In general, as the height of a pedestrian gets
average images of the positive samples. In our baseline al-
                                                                      smaller, the miss rate gets larger. Our detector also fol-
gorithm [9], weak classifiers select few cells in the regular
                                                                      lows this tendency (near: 50.09%, medium: 70.67% and
grid of the bounding box and classify positive and negative
                                                                      far: 91.42%). Interestingly, the performance gap between
samples using the most discriminant cell. Based on the av-
                                                                      ACF and multispectral ACF gets larger if the scale increases
erage image, the classifier can be regarded as well-trained if
                                                                      (near: 17.63%, medium: 13.41% and far: 5.67%). We be-
the features around the human shape regions are frequently
                                                                      lieve this is due to the low-resolution of the thermal camera,
used. To observe locations of frequently used features, we
                                                                      which can capture a human shape better if the pedestrian is
made voting maps in the regular grid as shown in Fig. 9
                                                                      not too distant.
(c-d). In Fig. 9 (c), a learned model with color images (us-
ing ACF) has many features located outside of the human               Occlusion. For this experiment, we made three subsets
shape. This is caused by the significant background clut-             based on the occlusion tags: no-occlusion, partial-occlusion
ter, which is common in color images. On the other hand,              (∼50% of area occluded) and heavy occlusion (50%∼ of
                                   1                                                         1                                                          1

                                  .80                                                       .80                                                        .80
Day & night subsets

                                  .64                                                       .64                                                        .64
                      miss rate

                                                                                miss rate

                                                                                                                                           miss rate
                                  .50                                                       .50                                                        .50

                                  .40                                                       .40                                                        .40

                                  .30    79.26%, ACF                                        .30    81.09%, ACF                                         .30    90.17%, ACF
                                         72.46%, ACF+T                                             76.48%, ACF+T                                              74.54%, ACF+T
                                         68.11%, ACF+T+TM+TO                                       70.02%, ACF+T+TM+TO                                        64.92%, ACF+T+TM+TO
                                         64.76%, ACF+T+THOG                                        64.17%, ACF+T+THOG                                         63.99%, ACF+T+THOG
                                  .20    −2          −1           0         1
                                                                                            .20    −2           −1           0         1
                                                                                                                                                       .20    −2           −1           0         1
                                        10         10           10         10                     10          10           10         10                     10          10           10         10
                                               False positives per image                                  False positives per image                                  False positives per image

                                              (a) Reasonable all                                        (b) Reasonable day                                        (c) Reasonable night
                                   1                                                         1                                                          1

                                  .80                                                       .80                                                        .80

                                  .64                                                       .64                                                        .64
                      miss rate

                                                                                miss rate

                                                                                                                                           miss rate
                                  .50                                                       .50                                                        .50
  Scale

                                  .40                                                       .40                                                        .40

                                  .30    67.72%, ACF                                        .30    84.08%, ACF                                         .30    97.09%, ACF
                                         61.24%, ACF+T                                             77.40%, ACF+T                                              93.60%, ACF+T
                                         54.63%, ACF+T+TM+TO                                       73.72%, ACF+T+TM+TO                                        93.32%, ACF+T+TM+TO
                                         50.09%, ACF+T+THOG                                        70.67%, ACF+T+THOG                                         91.42%, ACF+T+THOG
                                  .20    −2          −1           0         1
                                                                                            .20    −2           −1           0         1
                                                                                                                                                       .20    −2           −1           0         1
                                        10         10           10         10                     10          10           10         10                     10          10           10         10
                                               False positives per image                                  False positives per image                                  False positives per image

                                                (d) Near scale                                          (e) Medium scale                                              (f) Far scale
                                   1                                                         1                                                          1

                                  .80                                                       .80                                                        .80

                                  .64                                                       .64                                                        .64
  Occlusion
                      miss rate

                                                                                miss rate

                                  .50                                                       .50                                            miss rate   .50

                                  .40                                                       .40                                                        .40

                                  .30    76.26%, ACF                                        .30    91.59%, ACF                                         .30    93.46%, ACF
                                         69.16%, ACF+T                                             85.82%, ACF+T                                              89.70%, ACF+T
                                         64.50%, ACF+T+TM+TO                                       80.69%, ACF+T+TM+TO                                        88.50%, ACF+T+THOG
                                         60.69%, ACF+T+THOG                                        78.96%, ACF+T+THOG                                         87.75%, ACF+T+TM+TO
                                  .20    −2          −1           0         1
                                                                                            .20    −2           −1           0         1
                                                                                                                                                       .20    −2           −1           0         1
                                        10         10           10         10                     10          10           10         10                     10          10           10         10
                                               False positives per image                                  False positives per image                                  False positives per image

                                              (g) No occlusion                                         (h) Partial occlusion                                       (i) Heavy occlusion

Figure 10. False positive per image (FPPI) versus miss rate in various conditions. Our multispectral ACF is denoted as ACF+T+THOG.

the area occluded). The dataset contains daytime and night-                                                          5. Conclusion
time images with various scales. The evaluation results are
shown in Fig. 10 (g)-(i). The performance of our multi-                                                                 We introduced an multispectral pedestrian dataset of real
spectral ACF acceptably degrades as the occlusion level in-                                                          traffic scenes. The proposed dataset has rich information
creases. However, the performance of stadard ACF drops                                                               involving thermal images, various real traffic scenes, lots of
significantly even under partial occlusion. This implies that                                                        annotations with occlusion tags, and temporal correlations
the additional thermal channel is helpful in case of partial                                                         of the annotations. In addition, we thoughtfully defined the
occlusion as well.                                                                                                   subsets of the dataset in terms of day/nighttime, braking dis-
                                                                                                                     tances, and occlusion levels.
                                                                                                                        We analyzed the effects of the thermal channel with re-
Summary. Through our experiments, we validated the ef-                                                               gard to the distinctiveness of channel features. We also veri-
fectiveness of the joint use of color-thermal images. Our                                                            fied our extension of ACF, called multispectral ACF, in var-
trained detectors showed consistent improvements for all                                                             ious conditions. Through the experiments, we determined
conditions compared to the color image based detector. The                                                           that the aligned multispectral images are very helpful for
thermal image was helpful even when visual information                                                               resolving pedestrian detection problems in various condi-
was lacking, in far scale (Fig. 10 (f)) or occluded cases                                                            tions. We expect that the proposed dataset can encourage
(Fig. 10 (h), (i)).                                                                                                  the development of better pedestrian detection methods.
Day 1
Day 2
Night 1
Night 2

            (a) Detection using ACF [9]                                      (b) Detection using our multispectral ACF
              (trained by color images)                               (trained by both color (left) and thermal (right) images)

Figure 11. Examples of detection results at FPPI 1. (a) Detection results of ACF [9] trained by color images only. (b, c) Detection results of
the multispectral ACF (described in Sec. 3.2) trained by both color and thermal images. The ACF misses some pedestrians which are hard
to distinguish from background and produce some false positives. On the contrary, the multispectral ACF can detect pedestrian correctly
even in the challenging nighttime images. Images are cropped for better visualization.

Acknowledgement: We thank anonymous reviewers giv-                           [2] A. Bhattacharyya. On a measure of divergence between two
ing constructive comments to our work. We also appreciate                        statistical populations defined by their probability distribu-
KAIST-RCV labmates who help to finish the tedious anno-                          tions. Bulletin of the Calcutta Mathematical Society, 1943.
tation task. This work was supported by the Development                      [3] L. Bienkowski, C. Homma, K. Eisler, and C. Boller. Hy-
of Autonomous Emergency Braking System for Pedestrian                            brid camera and real-view thermography for nondestructive
Protection project funded by the Ministry of Trade, Industry                     evaluation. Quantitativ InfraRed Thermography, 254, 2012.
and Energy of Korea. (MOTIE)(No.10044775)                                    [4] N. Dalal and B. Triggs. Histograms of oriented gradients
                                                                                 for human detection. In Proceedings of IEEE Conference on
                                                                                 Computer Vision and Pattern Recognition (CVPR), 2005.
References                                                                   [5] J. Davis and M. Keck. A two-stage approach to person de-
   [1] R. Appel, T. Fuchs, P. Dollar, and P. Perona. Quickly boost-              tection in thermal imagery. In Proceeding of Workshop on
       ing decision trees – pruning underachieving features early.               Applications of Computer Vision (WACV), 2005.
       In International Conference on Machine Learning (ICML),               [6] J. Davis and V. Sharma. Background-subtraction using
       2013.                                                                     contour-based fusion of thermal and visible imagery. Com-
     puter Vision and Image Understanding, 106(2–3):162–182,          [23] J. Philbin, O. Chum, M. Isard, J. Sivic, and A. Zisser-
     2007.                                                                 man. Object retrieval with large vocabularies and fast spatial
 [7] Department for Transport (DfT) Driver and Vehicle Stan-               matching. In Proceedings of IEEE Conference on Computer
     dards Agency (DVSA). The Official Highway Code. TSO                   Vision and Pattern Recognition (CVPR), 2007.
     (The Stationery Office), United Kingdom, 2007.                   [24] J. Portmann, S. Lynen, M. Chli, and R. Siegwart. People
 [8] P. Dollár.     Piotr’s Computer Vision Matlab Toolbox                detection and tracking from aerial thermal views. In Pro-
     (PMT).        http://vision.ucsd.edu/˜pdollar/                        ceeding of IEEE International Conference on Robotics and
     toolbox/doc/index.html.                                               Automation (ICRA), 2014.
 [9] P. Dollár, R. Appel, S. Belongie, and P. Perona. Fast feature   [25] L. St-Laurent, X. Maldague, and D. Prévost. Combination of
     pyramids for object detection. IEEE Transactions on Pat-              colour and thermal sensors for enhanced object detection. In
     tern Analysis and Machine Intelligence (PAMI), 36(8):1532–            Information Fusion, 2007 10th International Conference on,
     1545, 2014.                                                           pages 1–8. IEEE, 2007.
[10] P. Dollár, C. Wojek, B. Schiele, and P. Perona. Pedestrian      [26] M. Teutsch, T. Mller, M. Huber, and J. Beyerer. Low resolu-
     detection: A benchmark. In Proceedings of IEEE Conference             tion person detection with a moving thermal infrared camera
     on Computer Vision and Pattern Recognition (CVPR), 2009.              by hot spot classification. In Proceedings of IEEE Interna-
[11] R. O. Duda, P. E. Hart, and D. H. Stork. Pattern Classifica-          tional Conference of Computer Vision and Pattern Recogni-
     tion (2nd ed.). Wiley Interscience, 2000.                             tion Workshops (CVPRW), 2014.
[12] C. Elkan. Using the triangle inequality to accelerate k-         [27] A. Torabi, G. Mass, and G.-A. Bilodeau. An iterative in-
     means. In International Conference on Machine Learning                tegrated framework for thermal-visible image registration,
     (ICML), 2003.                                                         sensor fusion, and people tracking for video surveillance
[13] M. Enzweiler and D. M. Gavrila.             Monocular pedes-          applications. Computer Vision and Image Understanding,
     trian detection: Survey and experiments. IEEE Transac-                116:210–221, 2012.
     tions on Pattern Analysis and Machine Intelligence (PAMI),       [28] Z. Wu, N. Fuller, D. Theriault, and M. Betke. A thermal
     31(12):2179–2195, 2009.                                               infrared video benchmark for visual analysis. In Proceed-
[14] A. Ess, B. Leibe, K. Schindler, and L. van Gool. A mobile             ing of 10th IEEE Workshop on Perception Beyond the Visible
     vision system for robust multi-person tracking. In Proceed-           Spectrum (PBVS), 2014.
     ings of IEEE Conference on Computer Vision and Pattern           [29] S. Zhang, C. Bauckhage, and A. B. Cremers. Informed haar-
     Recognition (CVPR), 2008.                                             like features improve pedestrian detection. In Proceedings of
[15] A. Geiger, P. Lenz, and R. Urtasun. Are we ready for au-              IEEE Conference on Computer Vision and Pattern Recogni-
     tonomous driving? the kitti vision benchmark suite. In Pro-           tion (CVPR), 2014.
     ceedings of IEEE Conference on Computer Vision and Pat-
     tern Recognition (CVPR), 2012.
[16] J. Jung, Y. Jeong, J. Park, H. Ha, J. D. Kim, and I.-S. Kweon.
     A novel 2.5d pattern for extrinsic calibration of tof and cam-
     era fusion system. In IEEE/RSJ International Conference on
     Intelligent Robots and Systems (IROS), 2011.
[17] J. Jung, J.-Y. Lee, Y. Jeong, and I. S. Kweon. Time-of-flight
     sensor calibration for a color and depth camera pair. IEEE
     Transactions on Pattern Analysis and Machine Intelligence,
     Accepted.
[18] S. J. Krotosky and M. M. Trivedi. On color-, infrared-, and
     multimodal-stereo approaches to pedestrian detection. IEEE
     Transactions on Intelligent Transportation Systems, 8:619–
     629, 2007.
[19] F.-F. Li, R. Fergus, and P. Perona. One-shot learning of ob-
     ject categories. IEEE Transactions on Pattern Analysis and
     Machine Intelligence (PAMI), 28:594–611, 2006.
[20] W. Nam, P. Dollár, , and J. H. Han. Local decorrelation
     for improved pedestrian detection. In Annual Conference on
     Neural Information Processing Systems (NIPS), 2014.
[21] D. Olmeda, C. Premebida, U. Nunes, J. Armingol, and
     A. de la Escalera. Pedestrian classification and detection in
     far infrared images. Integrated Computer-Aided Engineer-
     ing, 20:347–360, 2013.
[22] S. Paisitkriangkrai, C. Shen, and A. van den Hengel.
     Strengthening the effectiveness of pedestrian detection with
     spatially pooled features. In Proceedings of European Con-
     ference on Computer Vision (ECCV), 2014.
