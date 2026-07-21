---
source_id: 142
bibtex_key: song2015sunrgbd
title: SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite
year: 2015
domain_theme: Dataset
verified_pdf: 142_SUN RGB-D.pdf
char_count: 74076
---

SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite

                            Shuran Song        Samuel P. Lichtenberg Jianxiong Xiao
                                                  Princeton University
                                              http://rgbd.cs.princeton.edu

                        Abstract

    Although RGB-D sensors have enabled major break-
throughs for several vision tasks, such as 3D reconstruc-
tion, we have not attained the same level of success in high-
level scene understanding. Perhaps one of the main rea-
sons is the lack of a large-scale benchmark with 3D anno-
                                                                          (a) NYU Depth v2           (b) UW Object Dataset
tations and 3D evaluation metrics. In this paper, we intro-
duce an RGB-D benchmark suite for the goal of advancing
the state-of-the-arts in all major scene understanding tasks.
Our dataset is captured by four different sensors and con-
tains 10,335 RGB-D images, at a similar scale as PASCAL
VOC. The whole dataset is densely annotated and includes
146,617 2D polygons and 64,595 3D bounding boxes with
accurate object orientations, as well as a 3D room layout
and scene category for each image. This dataset enables                      (c) SUN3D                      (d) Ours
us to train data-hungry algorithms for scene-understanding          Figure 1. Comparison of RGB-D recognition benchmarks.
tasks, evaluate them using meaningful 3D metrics, avoid             Apart from 2D annotation, our benchmark provided high quality
overfitting to a small testing set, and study cross-sensor          3D annotation for both objects and room layout.
bias.
                                                                    small datasets successfully bootstrapped initial progress in
                                                                    RGB-D scene understanding in the past few years, the size
1. Introduction                                                     limit is now becoming the critical common bottleneck in
    Scene understanding is one of the most fundamen-                advancing research to the next level. Besides causing over-
tal problems in computer vision. Although remarkable                fitting of the algorithm during evaluation, they cannot sup-
progress has been achieved in the past decades, general-            port training data-hungry algorithms that are currently the
purpose scene understanding is still considered to be very          state-of-the-arts in color-based recognition (e.g. [15, 36]).
challenging. Meanwhile, the recent arrival of affordable            If a large-scale RGB-D dataset were available, we could
depth sensors in consumer markets enables us to acquire             borrow the same success to the RGB-D domain as well.
reliable depth maps at a very low cost, stimulating break-          (Table 1 shows the performance improvement for a RGB-
throughs in several vision tasks, such as body pose recog-          D deep learning algorithm [20] when a bigger training set
nition [56, 58], intrinsic image estimation [4], 3D modeling        is used.) Furthermore, although the RGB-D images in these
[27] and SfM reconstruction [72].                                   datasets contain depth maps, the annotation and evaluation
    RGB-D sensors have also enabled rapid progress for              metrics are mostly in 2D image domain, but not directly in
scene understanding (e.g. [20, 19, 53, 38, 30, 17, 32, 49]).        3D (Figure 1). Scene understanding is much more useful in
However, while we can crawl color images from the Inter-            the real 3D space for most applications. We desire to reason
net easily, it is not possible to obtain large-scale RGB-D          about scenes and evaluate algorithms in 3D.
data online. Consequently, the existing RGB-D recogni-                 To this end, we introduce SUN RGB-D, a dataset con-
tion benchmarks, such as NYU Depth v2 [49], are an order-           taining 10,335 RGB-D images with dense annotations in
of-magnitude smaller than modern recognition datasets for           both 2D and 3D, for both objects and rooms. Based on
color images (e.g. PASCAL VOC [9]). Although these                  this dataset, we focus on six important recognition tasks

                                                                1
            Training Set
                         NYU (795 images) SUN RGB-D (5,285 images)
Testing Set                                                                                 Intel Realsense   Asus Xtion   Kinect v1         Kinect v2
         NYU                  32.50               34.33

                                                                           color
      SUN RGB-D               15.78               33.20
Table 1. Performance improves as the size of training data in-
creases. We trained the Depth-RCNN [20] for 2D object detection

                                                                           raw depth
using RGB-D images, and evaluated the mean average precision.
Bigger training set produces better result. Especially for the first
row using NYU as the testing set, the performance is still better

                                                                           refined depth
using the bigger SUN RGB-D that is a superset of NYU, despite
the domain gap due to dataset bias.
                  RealSense    Xtion   Kinect v1   Kinect v2
weight (pound)      0.077       0.5       4           4.5

                                                                           raw points
  size (inch) 5.2×0.25×0.75 7.1×1.4×2 11×2.3×2.7 9.8×2.7×2.7
     power       2.5W USB 2.5W USB 12.96W           115W
depth resolution  628×468    640×480 640×480       512×424
color resolution 1920×1080   640×480 640×480 1920×1080

                                                                           refined points
Table 2. Specification of sensors. RealSense is very light, while
Kinect v2 is heavier and has much higher power consumption.

towards total scene understanding, which recognizes ob-                           Figure 2. Comparison of the four RGB-D sensors. The raw
jects, room layouts and scene categories. For each task,                          depth map from Intel RealSense is noisier and has more missing
we propose metrics in 3D and evaluate baseline algorithms                         values. Asus Xtion and Kinect v1’s depth map have observable
derived from the state-of-the-arts. Since there are several                       quantization effect. Kinect v2 is more accurate to measure the de-
popular RGB-D sensors available, each with different size                         tails in depth, but it is more sensitive to reflection and dark color.
                                                                                  Across different sensors our depth improvement algorithm man-
and power consumption, we construct our dataset using four
                                                                                  ages to robustly improve the depth map quality.
different kinds of sensors to study how well the algorithms
generalize across sensors. By constructing a PASCAL-scale
                                                                                  notation by ourselves. Although this dataset is very good,
dataset and defining a benchmark with 3D evaluation met-
                                                                                  the size is still small compared to other modern recognition
rics, we hope to lay the foundation for advancing RGB-D
                                                                                  datasets, such as PASCAL VOC [9] or ImageNet [7]. B3DO
scene understanding in the coming years.
                                                                                  [28] is another dataset with 2D bounding box annotations
1.1. Related work                                                                 on the RGB-D images. But its size is smaller than NYU
                                                                                  and it has many images with an unrealistic scene layouts
   There are many interesting works on RGB-D scene un-                            (e.g. snapshot of a computer mouse on the floor). The Cor-
derstanding, including semantic segmentation [53, 49, 19]                         nell RGBD dataset [2, 34] contains 52 indoors scenes with
object classification [69], object detection [59, 20, 62], con-                   per-point annotations on the stitched point clouds. SUN3D
text reasoning [38], mid-level recognition [32, 31], and sur-                     [72] contains 415 RGB-D video sequence with 2D polygon
face orientation and room layout estimation [13, 14, 74].                         annotation on some key frames. Although they stitched the
Having a solid benchmark suite to evaluate these tasks will                       point cloud in 3D, the annotation is still purely in the 2D
be very helpful in further advancing the field.                                   image domain, and there are only 8 annotated sequences.
   There are many existing RGB-D datasets available [54,
47, 1, 25, 44, 60, 49, 45, 29, 66, 57, 52, 46, 16, 21, 73, 35,                    2. Dataset construction
67, 3, 41, 10, 63, 42, 64, 65, 48, 12, 33, 8, 50, 26, 6]. Fig-
ure 1 shows some of them. Here we will briefly describe                              The goal of our dataset construction is to obtain an im-
several most relevant ones1 . There are datasets [61, 37] that                    age dataset captured by various RGB-D sensors at a similar
capture objects on a turntable instead of real-world scenes.                      scale as the PASCAL VOC object detection benchmark. To
For natural indoor scene datasets, NYU Depth v2 [49] is                           improve the depth map quality, we take short videos and
probably the most popular one. They labeled 1,449 selected                        use multiple frames to obtain a refined depth map. For each
frames from short RGB-D videos using 2D semantic seg-                             image, we annotate the objects with both 2D polygons and
mentation on the image domain. [18] annotates each object                         3D bounding boxes and the room layout with 3D polygons.
by aligning a CAD model with the 3D point cloud. How-
ever, the 3D annotation is quite noisy, and in our bench-                         2.1. Sensors
mark we reuse the 2D segmentation but recreate the 3D an-                            Since there are several popular sensors available, with
   1 A full list with brief descriptions is available at http://www0.cs.          different size and power consumption, we construct our
ucl.ac.uk/staff/M.Firman/RGBDdatasets/.                                           dataset using four kinds – Intel RealSense 3D Camera for
                            2D segmentation    3D annotaion                             2D segmentation               3D annotaion

                                                                          dining room
 bedroom
conference room classroom

                                                                          bathroom
                                                                          office
home office

                                                                          kitchen
                                              Figure 3. Example images with annotation from our dataset.

      tablets, Asus Xtion LIVE PRO for laptops, and Microsoft                       driver and decoded the raw depth in GPU (Kinect v2 re-
      Kinect versions 1 and 2 for desktop. Table 2 shows each                       quires software depth decoding) to capture real-time video
      sensor’s specification. Figure 2 shows the example color                      without depth cutoffs or additional filtering.
      and depth images captured.
                                                                                    2.2. Sensor calibration
      Intel RealSense is a lightweight, low power consuming
      depth sensor designed for tablets. It will soon reach con-                        For RGB-D sensors, we must calibrate the camera in-
      sumers; we obtained two pre-release samples from Intel. It                    trinsic parameters and the transformation between the depth
      projects an IR pattern to the environment and uses stereo                     and color cameras. For Intel RealSense, we use the default
      matching to obtain the depth map. For outdoor environ-                        factory parameters. For Asus Xtion, we rely on the default
      ments, it can switch automatically to stereo matching with-                   parameters returned by OpenNI library without modeling
      out IR pattern; however, we visually inspect the 3D point                     radial distortion. For Kinect v2, the radial distortion is very
      cloud and believe the depth map quality is too low for use in                 strong. So we calibrate all cameras with standard calibra-
      accurate object recognition for outdoors. We thus only use                    tion toolbox [5]. We calibrate the depth cameras by comput-
      this sensor to capture indoor scenes. Figure 2 shows its raw                  ing the parameters with the IR image which is the same with
      depth is worse than that of other RGB-D sensors, and the                      the depth camera. To see the checkerboard without overex-
      effective range for reliable depth is shorter (depth gets very                posure on IR, we cover the emitter with a piece of paper.
      noisy around 3.5 meters). But this type of lightweight sen-                   We use the stereo calibration function to calibrate the trans-
      sor can be embedded in portable devices and be deployed at                    formation between the depth (IR) and the color cameras.
      a massive scale in consumer markets, so it is important to
      study algorithm performance with it.                                          2.3. Depth map improvement
                                                                                       The depth maps from these cameras are not perfect, due
      Asus Xtion and Kinect v1 use a near-IR light pattern. Asus
                                                                                    to measurement noise, view angle to the regularly reflec-
      Xtion is much lighter and powered by USB only, with worse
                                                                                    tive surface, and occlusion boundary. Because all the RGB-
      color image quality than Kinect v1’s. However, Kinect v1
                                                                                    D sensors operate as a video camera, we can use nearby
      requires an extra power source. The raw depth maps from
                                                                                    frames to improve the depth map, providing redundant data
      both sensors have an observable quantization effect.
                                                                                    to denoise and fill in missing depth.
      Kinect v2 is based on time-of-flight and also consumes sig-                      We propose a robust algorithm for depth map integration
      nificant power. The raw depth map captured is more accu-                      from multiple RGB-D frames. For each nearby frame in a
      rate, with high fidelity to measure the detailed depth differ-                time window, we project the points to 3D, get the triangu-
      ence, but fails more frequently for black objects and slightly                lated mesh from nearby points, and estimate the 3D rotation
      reflective surfaces. The hardware supports long distance                      and translation between this frame and the target frame for
      depth range, but the official Kinect for Windows SDK cuts                     depth improvement. Using this estimated transformation,
      the depth off at 4.5 meters and applies some filtering that                   we render the depth map of the mesh from the target frame
      tends to lose object details. Therefore, we wrote our own                     camera. After we obtain aligned and warped depth maps,
          19959                         (a) object distribution                                                     (b) scene distribution
5000
                                                                                                                        rest space(6.3%)
                                Kinect v2              SUN3D (ASUS Xtion)      NYUv2 (Kinect v1)                                       living room(6.0%)
                                                                                                      bathroom(6.4%)
3750                                                                                                                                        kitchen(5.6%)
                                                                                                    others(8.0%)
                                                                                                                                            corridor(3.8%)
                                Intel RealSense        B3DO (Kinect v1)                                                                          lab(3.0%)
2500                                                                                               classroom                                conference room(2.6%)
                                                                                                   (9.3%)                                        dining area(2.4%)
                                                                                                                                                 dining room(2.3%)
1250                                                                                               office                                    discussion area(2.0%)
                                                                                                   (11.0%)                                       home office(1.9%)
                                                                                                                                                 study space(1.9%)
                                                                                                                                                       library(1.4%)
   0                                                                                                  furniture store                         lecture theatre(1.2%)
                                                                                                      (11.3%)

                           b
          g s wn r
                  ta tv
                                                                                                                                             computer room(1.0%)
               m lam x

                 bo pu

       co frid up
                      c g

                    o ay
                      bod

                           k
               cae_b a

                           k
                  pu r
                drcha lf
                  pi esk

                  bi ol

                 be ven
                    ta air

          n res ilet

                  in nt

                       ar l
                    d le

                  on p

                    o k

              pa pla el
                        ge

      pu in rin le
           tra me
         rb llow

         bo t s ab r

                      tr d
            l c p or

        ca cl ous s
                  chnch
              r a r

                ab top

             rto oth e
            te c n
                  frawer

                    o o

                  n es

                pohon n
                    thait
                      be t

                  bi er
               fa he r

                  mting

                  boow
        ni ide ap n

          co dard

      he d to er
              ok ta le
                   a ir

                bartr e
           ke bhelf

              le h x
               m oo

                        tu
                   s nd

            u mo ble
                  boble
                         d
          gh t e
                   bi in

          te g t te

                    b et
                       ne

                sh sin
          so sito
                         f

                      ba
                yb oo

                cu ract

                m air
                   tonet
         hi rtai

                 p e
    ng nkn nit
                       b

                       w
          s p ca

             ca to
             ag so

    m in p tt

          te kitcbo
                     ne

                      ar

        ee la irr
              ca s
                    ch

                       t

                     in
                                                                                                                          bedroom(12.6%)

                e
           ffe

       in
      ga

       w

 co d

     st
    tc
  ki

 ha
                                        Figure 4. Statistics of semantic annotation in our dataset.

                                                                          2.4. Data acquisition
                                                                              To construct a dataset at the PASCAL VOC scale, we
                                                                          capture a significant amount of new data by ourselves and
                                                                          combine some existing RGB-D datasets. We capture 3,784
                                                                          images using Kinect v2 and 1,159 images using Intel Re-
            (a)                   (b)                     (c)             alSense. We included the 1,449 images from the NYU
Figure 5. Data Capturing Process. (a) RealSense attached to lap-          Depth V2 [49], and also manually selected 554 realistic
top, (b) Kinect v2 with battery, (c) Capturing setup for Kinect v2.       scene images from the Berkeley B3DO Dataset [28], both
                                                                          captured by Kinect v1. We manually selected 3,389 dis-
                                                                          tinguished frames without significant motion blur from the
we integrate them to get a robust estimation. For each pixel              SUN3D videos [72] captured by Asus Xtion. In total, we
location, we compute the median depth and 25% and 75%                     obtain 10,335 RGB-D images.
percentiles. If the raw target depth is missing or outside                    As shown in Figure 5, we attach an Intel RealSense to
the 25% − 75% range and the median is computed from                       a laptop and carry it around to capture data. For Kinect v2
at least 10 warped depth maps, we use the median depth                    we use a mobile laptop harness and camera stabilizer. Be-
value. Otherwise, we keep the original value to avoid over-               cause Kinect v2 consumes a significant amount of power,
smoothing. Examples are shown in Figure 2. Our depth                      we use a 12V car battery and a 5V smartphone battery to
map improvement algorithm, compared to [72] which uses                    power the sensor and the adaptor circuit. The RGB-D sen-
a 3D voxel-based TSDF representation, requires much less                  sors only work well for indoors. And we focus on univer-
memory and runs faster at equal resolution, enabling much                 sities, houses, and furniture stores in North America and
high-resolution integration.                                              Asia. Some example images are shown in Figure 3.
    Robust estimation of an accurate 3D transformation be-                2.5. Ground truth annotation
tween a nearby frame and target frame is critical for this
algorithm. To do this, we first use SIFT to obtain point-to-                 For each RGB-D image, we obtain LabelMe-style 2D
point correspondences between the two color images, ob-                   polygon annotations, 3D bounding box annotations for ob-
tain the 3D coordinates for the SIFT keypoints from the                   jects, and 3D polygon annotations for room layouts. To en-
raw depth map, and then estimate the rigid 3D rotation and                sure annotation quality and consistency, we obtain our own
translation between these two sparse 3D SIFT clouds us-                   ground truth labels for images from other datasets; the only
ing RANSAC with three points. To obtain a more accurate                   exception is NYU, whose 2D segmentation we use.
estimation, we would like to use the full depth map to do                    For 2D polygon annotation, we developed a LabelMe-
dense alignment with ICP, but depending on the 3D struc-                  style [55] tool for Amazon Mechanical Turk. To ensure
ture, ICP can have severe drifting. Therefore, we first use               high label quality, we add automatic evaluation in the tool.
the estimation from SIFT+RANSAC to initialize the trans-                  To finish the HIT, each image must have at least 6 objects
formation for ICP, and calculate the percentage of points                 labeled; the union of all object polygons must cover at least
for ICP matching. Using the initialization and percentage                 80% of the total image. To prevent workers from cheat-
threshold, we run point-plane ICP until convergence, then                 ing by covering everything with big polygons, the union
check the 3D distances with the original SIFT keypoint in-                of the small polygons (area < 30% of the image) must
liers from RANSAC. If the distances significantly increase,               cover at least 30% of the total image area. Finally, the au-
it means ICP makes the result drift away from the truth; we               thors visually inspect the labeling result and manually cor-
will use the original RANSAC estimation without ICP. Oth-                 rect the layer ordering when necessary. Low quality label-
erwise, we use the ICP result.                                            ings are sent back for relabeling. We paid $0.10 per image;
                       RGB (19.7)     D (20.1)   RGB-D (23.0)   RGB (35.6)    D (25.5)     RGB-D (37.2)     RGB (38.1)     D (27.7)   RGB-D (39.0)
        bathroom
         bedroom
        classroom
 computer room
conference room
          corridor
       dining area
     dining room
  discussion area
   furniture store
     home office
           kitchen
                 lab
  lecture theatre
            library
      living room
              office
        rest space
      study space

                           (a) GIST[51] + RBF kernel SVM           (b) Places-CNN[75] + Linear SVM            (c) Places-CNN[75] + RBF kernel SVM
  Figure 6. Confusion matrices for various scene recognition algorithms. Each combination of features and classifiers is run on RGB, D
  and RGB-D. The numbers inside the parentheses are the average accuracy for classification.

  some images required multiple labeling iterations to meet
  our quality standards.
                                                                                   Effective free space
      For 3D annotation, the point clouds are first rotated to
                                                                                   Outside the room
  align with the gravity direction using an automatic algo-                        Inside some objects
  rithm. We estimate the normal direction for each 3D point                        Beyond cutoff distance
  with the 25 closest 3D points. Then we accumulate a his-
  togram on a 3D half-sphere and pick the maximal count
                                                                                Figure 7. Free space evaluation. The free space is the gray area
  from it to obtain the first axis. For the second axis, we pick                inside the room, outside any object bounding boxes, and within
  the maximal count from the directions orthogonal to the first                 the effective minimal and maximal range [0.5m-5.5m]. For evalu-
  axis. In this way, we obtain the rotation matrix to rotate the                ation, we use IoU between the gray areas of the ground truth and
  point cloud to align with the gravity direction. We manually                  the prediction as the criteria.
  adjust the rotation when the algorithm fails.
      We design a web-based annotation tool and hire oDesk                      given an RGB-D image, classify the image into one of the
  workers to annotate objects and room layouts in 3D. For ob-                   predefined scene categories, and use the standard average
  jects, the tool requires drawing a rectangle on the top view                  categorization accuracy for evaluation.
  with an orientation arrow, and adjusting the top and bottom
  to inflate it to 3D. For room layouts, the tool allows arbitrary              Semantic Segmentation Semantic segmentation in the
  polygon on the top view to describe the complex structure                     2D image domain is currently the most popular task for
  of the room (Figure 3). Our tool also shows the projec-                       RGB-D scene understanding. In this task, the algorithm
  tion of the 3D boxes to the image in real time, to provide                    outputs a semantic label for each pixel in the RGB-D im-
  intuitive feedback during annotation. We hired 18 oDesk                       age. We use the standard average accuracy across object
  workers and trained them over Skype. The average hourly                       categories for evaluation.
  rate is $3.90, and they spent 2,051 hours in total. Finally,                  Object Detection Object detection is another important
  all labeling results are thoroughly checked and corrected by                  step for scene understanding. We evaluate both 2D and 3D
  the authors. For scene categories, we manually classify the                   approaches by extending the standard evaluation criteria for
  images into basic-level scene categories.                                     2D object detection to 3D. Assuming the box aligns with
                                                                                the gravity direction, we use the 3D intersection over union
  2.6. Label statistics
                                                                                of the predicted and ground truth boxes for 3D evaluation.
     For the 10,335 RGB-D images, we have 146,617 2D
                                                                                Object Orientation Besides predicting the object loca-
  polygons and 64,595 3D bounding boxes (with accurate ori-
                                                                                tion and category, another important vision task is to es-
  entations for objects) annotated. Therefore, there are 14.2
                                                                                timate its pose. For example, knowing the orientation of a
  objects in each image on average. In total, there are 47
                                                                                chair is critical to sit on it properly. Because we assume that
  scene categories and about 800 object categories. Figure 4
                                                                                an object bounding box is aligned with gravity, there is only
  shows the statistics for the semantic annotation of the major
                                                                                one degree of freedom in estimating the yaw angle for ori-
  object and scene categories.
                                                                                entation. We evaluate the prediction by the angle difference
                                                                                between the prediction and the ground truth.
  3. Benchmark design
                                                                                Room Layout Estimation The spatial layout of the entire
     To evaluate the whole scene understanding pipeline, we
                                                                                space of the scene allows more precise reasoning about free
  select six tasks, including both popular existing tasks and
                                                                                space (e.g., where can I walk?) and improved object rea-
  new but important tasks, both single-object based tasks and
                                                                                soning. It is a popular but challenging task for color-based
  scene tasks, as well as a final total scene understanding task
                                                                                scene understanding (e.g. [22, 23, 24]). With the extra depth
  that integrates everything.
                                                                                information in the RGB-D image, this task is considered to
  Scene Categorization Scene categorization is a very pop-                      be much more feasible [74]. We evaluate the room layout
  ular task for scene understanding [70]. In this task, we are                  estimation in 3D by calculating the Intersection over Union
                                                                         Angle: 3.54 IoU: 0.66 Angle: 8.6 IoU: 0.7                                       Angle: 1.6 IoU: 0.6               Angle: 2.4 IoU: 0.7

                                                           mean
 RGB NN 45.03 27.89 16.89 18.51 21.77 1.06 4.07        0 8.32
 Depth NN 42.6 9.65 21.51 12.47 6.44 2.55 0.6 0.3 5.32
RGB-D NN 45.78 35.75 19.86 19.29 23.3 1.66 6.09 0.7 8.97
 RGB [40] 47.22 39.14 17.21 20.43 21.53 1.49 5.94      0 9.33
Depth [40] 43.83 13.9 22.31 12.88 6.3 1.49 0.45 0.25 5.98                Angle: 12.6 IoU: 0.7                        Angle: 49.5 IoU: 0.6                 Angle: 87.4 IoU: 0.4           Angle: 31.4 IoU: 0.24
RGB-D [40] 48.25 49.18 20.8 20.92 23.61 1.83 8.73 0.77 10.05
RGB-D [53] 78.64 84.51 33.15 34.25 42.52 25.01 35.74 35.71 36.33

Table 3. Semantic segmentation. We evaluate performance for 40
object categories. Here shows 8 selected ones: floor, ceiling, chair,
table, bed, nightstand, books, and person. The mean accuracy is
for all the 40 categories. A full table is in the supp. material.
                                                                         Figure 8. Example results for 3D object detection and orienta-
                                                                         tion prediction. We show the angle difference and IoU between
                                                               mAP       predicted boxes (blue) and ground truth (red).
 Sliding Shapes [62]   33.42   25.78   42.09   61.86   23.28   37.29                                                     chair                                                          bed
                                                                            3000                                                                          200
                  Table 4. 3D object detection.                             2000
                                                                                                                           Sliding Shapes 150

                                                                        count
                                                                                                                           Examplar SVM 100
                                                                            1000
                                                                                                                                                           50

(IoU) between the free space from the ground truth and the                        0
                                                                                      9        27        45    63    81     99   117   135   153   171
                                                                                                                                                            0
                                                                                                                                                             0   20   40      60    80    100   120   140   160   180
                                                                                                         angle difference in degree                                        angle difference in degree
free space predicted by the algorithm output.                                                                        sofa                                                            toilet
    As shown in Figure 7, the free space is defined as the                      300
                                                                                                                                                           40

                                                                        count
                                                                                200
space that satisfies four conditions: 1) within camera field                    100
                                                                                                                                                           20

of view, 2) within effective range, 3) within the room, and                      0
                                                                                  0       20        40        60    80     100   120   140   160    180
                                                                                                                                                            0
                                                                                                                                                             0   20   40      60   80    100    120   140   160   180
                                                                                                     angle difference in degree                                        angle difference in degree
4) outside any object bounding box (for room layout esti-
                                                                         Figure 9. Object orientation estimation. Here we show the dis-
mation, we assume empty rooms without objects). In terms                 tribution of the orientation errors for all true positive detections.
of implementation, we define a voxel grid of 0.1 × 0.1 × 0.1
meter3 over the space and choose the voxels that are inside              dicted boxes and ground truth boxes, and we sort the IoU
the field of view of the camera and fall between 0.5 and 5.5             scores in a descending order. We choose each available pair
meters from the camera, which is an effective range for most             with the largest IoU and mark the two boxes as unavail-
RGB-D sensors. For each of these effective voxels, given a               able. We repeat this process until the IoU is lower than
room layout 3D polygon, we check whether the voxel is in-                a threshold τ (τ = 0.25 in this case). For each matched
side. In this way, we can compute the intersection and the               pair between ground truth and prediction, we compare their
union by counting 3D voxels.                                             object label in order to know whether it is a correct predic-
    This evaluation metric directly measures the free space              tion or not. Let |G| be the number of ground truth boxes,
prediction accuracy. However, we care only about the space               |P| be the number of prediction boxes, |M| be the num-
within a 5.5 meter range; if a room is too big, all effective            ber of matched pairs with IoU> τ , and |C| be the number
voxels will be in the ground truth room. If an algorithm pre-            of matched pairs with a correct label. We evaluate the al-
dicts a huge room beyond 5.5 meters, then the IoU will be                gorithms by computing three numbers: Rr = |C| / |G| to
equal to one, which introduces bias: algorithms will favor               measure the recall of recognition for both semantics and ge-
a huge room. To address this issue, we only evaluate algo-               ometry, Rg = |M|/|G| to measure the geometric prediction
rithms on the rooms with reasonable size (not too big), since            recall, and Pg = |M|/|P| to measure the geometric predic-
none of the RGB-D sensors can see very far either. If the                tion precision. We also evaluate the free space by using a
percentage of effective 3D voxels in the ground truth room               similar scheme as for room layout: counting the visible 3D
is bigger than 95%, we discard the room in our evaluation.               voxels for the free space, i.e. inside the room polygon but
                                                                         outside any object bounding box. Again, we compute the
Total Scene Understanding The final task for our scene                   IoU between the free space of ground truth and prediction.
understanding benchmark is to estimate the whole scene in-
cluding objects and room layout in 3D [38]. This task is also
                                                                         4. Experimental evaluation
referred to “Basic Level Scene Understanding” in [71]. We
propose this benchmark task as the final goal to integrate                  We choose some state-of-the-art algorithms to evaluate
both object detection and room layout estimation to obtain               each task. For the tasks without existing algorithm or imple-
a total scene understanding, recognizing and localizing all              mentation, we adapt popular algorithms from other tasks.
the objects and the room structure.                                      For each task, whenever possible, we try to evaluate al-
   We evaluate the result by comparing the ground truth ob-              gorithms using color, depth, as well as RGB-D images to
jects and the predicted objects. To match the prediction with            study the relative importance of color and depth, and gauge
ground truth, we compute the IoU between all pairs of pre-               to what extent the information from both is complementary.
                                                                                                                            mAP
 RGB-D ESVM 7.38 12.95 7.44 0.09 12.47 0.02 0.86 0.57 1.87 6.01 6.12 0.41 6.00 1.61 6.19 14.02 11.89 0.75 14.79 5.86
  RGB-D DPM    34.23 54.74 14.40 0.45 29.30 0.87 4.75 0.43 1.82 13.25 23.38 11.99 23.39 9.36 15.59 21.62 24.04 8.73 23.79 16.64
RGB-D RCNN[20] 49.56 75.97 34.99 5.78 41.22 8.08 16.55 4.17 31.38 46.83 21.98 10.77 37.17 16.5 41.92 42.2 43.02 32.92 69.84 35.20
Table 5. Evaluation of 2D object detection. We evaluate on 19 popular object categories using Average Precision (AP): bathtub, bed,
bookshelf, box, chair, counter, desk, door, dresser, garbage bin, lamp, monitor, night stand, pillow, sink, sofa, table, tv and toilet.
  Ground Truth    Manhattan Box (0.99)    Convex Hull (0.90)   Geometric Context (0.27)                  RGB-D RCNN                   Sliding Shapes
                                                                                                   (1)     (2)   (3)     (4)    (1)     (2)     (3)     (4)
                                                                                            Pg    21.5    21.7 21..4    22.3   33.2    37.7    33.2    37.8
  Ground Truth    Manhattan Box (0.811)   Convex Hull (0.85)   Geometric Context (0.57)    Rg     38.2    39.4  40.8    39.0   32.5    32.4    32.5    32.3
                                                                                            Rr    21.5    32.6  20.4    21.4   23.7    23.7    23.7    23.7
                                                                                           IoU    59.5    60.5  59.5    59.8   65.1    65.8    65.2    66.0
   Ground Truth   Manhattan Box (0.72)    Convex Hull (0.43)   Geometric Context (0.61)   Table 6. Evaluation of total scene understanding. With the ob-
                                                                                          jects detection result from Sliding Shape and RCNN and Man-
                                                                                          hattan Box for room layout estimation, we evaluate four ways to
                                                                                          integrate object detection and room layout: (1) directly combine
Figure 10. Example visualization to compare the three 3D room
                                                                                          (2) constrain the object using room. (3) adjust room base on the
layout estimation algorithms.
                                                                                          objects (4) adjust the room and objects together.
Various evaluation results show that we can apply standard
                                                                                          report the result on Table 3. Since our dataset is quite large,
techniques designed for color (e.g. hand craft features, deep
                                                                                          we expect non-parametric label transfer to work well. We
learning features, detector, sift flow label transfer) to depth
                                                                                          first use Places-CNN features [75] to find the nearest neigh-
domain and it can achieve comparable performance for var-
                                                                                          bor and directly copy its segmentation as the result. We sur-
ious tasks. In most of cases, when we combining these two
                                                                                          prisingly found that this simple method performs quite well,
source of information, the performance get improved.
                                                                                          especially for big objects (e.g. floor, bed). We then adapt
    For evaluation, we carefully split the data into training
                                                                                          the SIFT-flow algorithm [40, 39], on both color and depth to
and testing set, ensuring each sensor has around half for
                                                                                          estimation flow. But it only slightly improves performance.
training and half for testing, Since some images are cap-
tured from the same building or house with similar furni-                                 Object Detection We evaluate four state-of-the-art algo-
ture styles, to ensure fairness, we carefully split the training                          rithms for object detection: DPM [11], Exemplar SVM
and testing sets by making sure that those images from the                                [43], RGB-D RCNN [20], and Sliding Shapes [62]. For
same building either all go into the training set or the testing                          DPM and Exemplar SVM, we use the depth as another
set and do not spread across both sets. For data from NYU                                 image channel and concatenate HOG computed from that
Depth v2 [49], we use the original split.                                                 and from color images. To evaluate the first three 2D al-
                                                                                          gorithms, we use 2D IoU with a threshold of 0.5 and the
Scene Categorization For this task, we use the 19 scene
                                                                                          results are reported in Table 5. The 2D ground truth box is
categories with more than 80 images. We choose GIST [51]
                                                                                          obtained by projecting the points inside the 3D ground truth
with a RBF kernel one-vs-all SVM as the baseline. We also
                                                                                          box back to 2D and finding a tight box that encompasses
choose the state-of-the-art Places-CNN [75] scene feature,
                                                                                          these 2D points. For 3D detection, we evaluate the state-
which achieves the best performance in color-based scene
                                                                                          of-the-art Sliding Shapes algorithm, using the CAD models
classification on the SUN database [70]. This feature is
                                                                                          originally used in [62], and evaluate the algorithm for their
learned using a Deep Convolutional Neural Net (AlexNet
                                                                                          five categories. We use 3D boxes for evaluation with 0.25
[36]) with 2.5 million scene images [75]. We use both linear
                                                                                          for the IoU as in [62], results are reported in Table 4.
SVM and RBF kernel SVM with this CNN feature. Also,
empirical experiments [20] suggest that both traditional im-                              Object Orientation We evaluate two exemplar-based ap-
age features and deep learning features for color image can                               proaches: Exemplar SVM [43] and Sliding Shapes [62]. We
be used to extract powerful features for depth maps as well.                              transfer the orientations from the training exemplars to the
Therefore, we also compute the GIST and Places-CNN on                                     predicted bounding boxes. Some categories (e.g. round ta-
the depth images. We also evaluate the concatenation of                                   ble) do not have well-defined orientations and are not in-
depth and color features. The depth image is encoded as                                   cluded for evaluation. Figure 8 shows example results, and
HHA image as in [20] before extract the feature. Figure 6                                 Figure 9 shows the distribution of prediction error.
reports the accuracy for these experiments. We can see that
                                                                                          Room Layout Estimation Although there exists an algo-
the deep learning features indeed perform much better, and
                                                                                          rithm for this task [74], we could not find an open source
the combination of color and depth features also helps.
                                                                                          implementation. Therefore, we design three baselines: the
Semantic Segmentation We run the state-of-the-art algo-                                   simplest baseline (named Convex Hull) computes the floor
rithm for semantic segmentation [53] on our benchmark and                                 and ceiling heights by taking the 0.1 and 99.9 percentiles
             bathtub     bed      bookshelf        box     chair     counter      desk        door     dresser      garbage bin               lamp    monitor      night stand        pillow   sink     sofa      table      tv      toilet
Ground truth

                 IoU 72.9 Rr: 0.333 Rg: 0.667 Pg: 0.667    IoU: 77.0 Rr: 0.25 Rg: 0.25 Pg: 0.5        IoU 63.9 Rr: 0.333 Rg: 0.667 Pg:1               IoU: 53.1 Rr: 0.111 Rg : 0.111 Pg: 0.5     IoU:60 Rr: 0.50 Rg : 0.0.50 Pg: 0.5
Sliding Shapes

                 IoU: 53.1 Rr: 0.333 Rg: 0.333 Pg: 0.125      IoU: 78.8 Rr: 1 Rg: 1 Pg: 0.5          IoU: 57.3 Rr :0.33 Rg: 0.667 Pg:0.125           IoU 50.7 Rr: 0.333 Rg: 0.333 Pg : 0.375    IoU: 54.6 Rr : 0.333 Rg : 0.333 Pg: 0.125
3D RCNN

                                                                   Figure 11. Visualization of total scene understanding results.

  of the 3D points along the gravity direction, and computes                                                                                   Train     Kinect v2          Xtion         Percent drop (%)
                                                                                                                                          Test       rgb    d     rgbd rgb    d   rgbd rgb       d     rgbd
  the convex hull of the point projection onto the floor plane
                                                                                                                            table chair

                                                                                                                                          Kinect v2 18.07 22.15 24.46 18.93 22.28 24.77 -4.76 -0.60 -1.28
  to estimate the walls. Our stronger baseline (named Man-                                                                                  Xtion 12.28 16.80 15.31 15.86 13.71 23.76 29.22 -18.39 55.23
  hattan Box) uses plane fitting to estimate a 3D rectangular                                                                             Kinect v2 15.45 30.54 29.53 16.34 8.74 18.69 -5.78 71.38 36.70
  room box. We first estimate the three principal directions of                                                                             Xtion    8.13 24.39 28.38 14.95 18.33 24.30 45.64 -33.05 -16.79
  the point cloud based on the histogram of normal directions                                                                                                 Table 7. Cross-sensor bias.
  (see Section 2.5). We then segment the point cloud based on                                                              outside the estimated room layout; (3) adjust room to en-
  the normal orientation and look for the planes with furthest                                                             compass 90 % the objects; (4) adjust the room according
  distance from center to form a box for the room layout. To                                                               to majority of objects and remove the out-of-room objects.
  compare with the color-based approach, we run Geometric                                                                  Figure 11 and Table 6 show the results.
  Context [22] on the color image to estimate the room layout
  in 2D. We then use the camera tilt angle from gravity direc-                                                             Cross sensor Because real data likely come from differ-
  tion estimation and the focal length from the sensor to re-                                                              ent sensors, it is important that an algorithm can generalize
  construct the layout in 3D with single-view geometry, using                                                              across them. Similar to dataset bias [68], we study sensor
  the estimated floor height to scale the 3D layout properly.                                                              bias for different RGB-D sensors. We conduct an experi-
  Figure 10 shows examples of the results of these algorithms.                                                             ment to train a DPM object detector using data captured by
  Average IoU for Geometric Context is 0.442, Convex Hull                                                                  one sensor and test on data captured by another to evaluate
  is 0.713, and Manhattan Box is 0.734 performs best.                                                                      the cross-sensor generality. To separate out the dataset bi-
                                                                                                                           ases, we do this experiment on a subset of our data, where
  Total Scene Understanding We use RGB-D RCNN and
                                                                                                                           a Xtion and a Kinect v2 are mounted on a rig with large
  Sliding Shapes for object detection and combine them with
                                                                                                                           overlapping views of the same places. From the result in
  Manhattan Box for room layout estimation. We do non-
                                                                                                                           Table 7, we can see that sensor bias does exist. Both color
  maximum suppression across object categories. For RGB-
                                                                                                                           and depth based algorithms exhibit some performance drop.
  D RCNN, we estimate the 3D bounding boxes of objects
                                                                                                                           We hope this benchmark can stimulate the development of
  from the 2D detection results. To get the 3D box we first
                                                                                                                           RGB-D algorithms with better sensor generalization ability.
  project the points inside the 2D window to 3D. Along each
  major direction of the room we build a histogram of the
  point count. Starting from the median of the histogram, we                                                               5. Conclusions
  set the box boundary at the first discontinuous location. We                                                                We introduce a RGB-D benchmark suite at PASCAL
  also set a threshold of detection confidence and maximum                                                                 VOC scale with annotation in both 2D and 3D. We pro-
  number of objects in a room to further reduce the number                                                                 pose 3D metrics and evaluate algorithms for all major tasks
  of detections. With the objects and room layout in hand                                                                  towards total scene understanding. We hope that our bench-
  we propose four simple ways to integrate them: (1) directly                                                              marks will enable significant progress for RGB-D scene un-
  combines them; (2) remove the object detections that fall                                                                derstanding in the coming years.
Acknowledgement. This work is supported by gift funds                 [20] S. Gupta, R. Girshick, P. Arbelaez, and J. Malik. Learning
from Intel Corporation. We thank Thomas Funkhouser, Ji-                    rich features from RGB-D images for object detection and
tendra Malik, Alexi A. Efros and Szymon Rusinkiewicz for                   segmentation. In ECCV, 2014. 1, 2, 7
valuable discussion. We also thank Linguang Zhang, Fisher             [21] A. Handa, T. Whelan, J. McDonald, and A. Davison. A
Yu, Yinda Zhang, Luna Song, Zhirong Wu, Pingmei Xu,                        benchmark for RGB-D visual odometry, 3D reconstruction
                                                                           and SLAM. In ICRA, 2014. 2
Guoxuan Zhang and others for data capturing and labeling.
                                                                      [22] V. Hedau, D. Hoiem, and D. Forsyth. Recovering the spatial
                                                                           layout of cluttered rooms. In ICCV, 2009. 5, 8
References
                                                                      [23] V. Hedau, D. Hoiem, and D. Forsyth. Thinking inside the
 [1] A. Aldoma, F. Tombari, L. Di Stefano, and M. Vincze. A                box: Using appearance models and context based on room
     global hypotheses verification method for 3d object recogni-          geometry. In ECCV. 2010. 5
     tion. In ECCV. 2012. 2                                           [24] V. Hedau, D. Hoiem, and D. Forsyth. Recovering free space
 [2] A. Anand, H. S. Koppula, T. Joachims, and A. Saxena.                  of indoor scenes from a single image. In CVPR, 2012. 5
     Contextually guided semantic labeling and search for three-      [25] S. Hinterstoisser, V. Lepetit, S. Ilic, S. Holzer, G. Bradski,
     dimensional point clouds. IJRR, 2012. 2                               K. Konolige, and N. Navab. Model based training, detec-
 [3] B. I. Barbosa, M. Cristani, A. Del Bue, L. Bazzani, and               tion and pose estimation of texture-less 3d objects in heavily
     V. Murino. Re-identification with rgb-d sensors. In First             cluttered scenes. In ACCV. 2013. 2
     International Workshop on Re-Identification, 2012. 2             [26] C. Ionescu, D. Papava, V. Olaru, and C. Sminchisescu. Hu-
 [4] J. T. Barron and J. Malik. Intrinsic scene properties from a          man3.6m: Large scale datasets and predictive methods for
     single rgb-d image. CVPR, 2013. 1                                     3d human sensing in natural environments. PAMI, 2014. 2
 [5] J.-Y. Bouguet. Camera calibration toolbox for matlab. 2004.      [27] S. Izadi, D. Kim, O. Hilliges, D. Molyneaux, R. Newcombe,
     3                                                                     P. Kohli, J. Shotton, S. Hodges, D. Freeman, A. Davison, and
 [6] C. S. Catalin Ionescu, Fuxin Li. Latent structured models for         A. Fitzgibbon. Kinectfusion: Real-time 3d reconstruction
     human pose estimation. In ICCV, 2011. 2                               and interaction using a moving depth camera. In UIST, 2011.
 [7] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-             1
     Fei. Imagenet: A large-scale hierarchical image database. In     [28] A. Janoch, S. Karayev, Y. Jia, J. T. Barron, M. Fritz,
     CVPR, 2009. 2                                                         K. Saenko, and T. Darrell. A category-level 3-d object
 [8] N. Erdogmus and S. Marcel. Spoofing in 2d face recognition            dataset: Putting the kinect to work. In ICCV Workshop on
     with 3d masks and anti-spoofing with kinect. In BTAS, 2013.           Consumer Depth Cameras for Computer Vision, 2011. 2, 4
     2                                                                [29] A. Janoch, S. Karayev, Y. Jia, J. T. Barron, M. Fritz,
 [9] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn,               K. Saenko, and T. Darrell. A category-level 3d object dataset:
     and A. Zisserman. The pascal visual object classes (voc)              Putting the kinect to work. 2013. 2
     challenge. IJCV, 2010. 1, 2                                      [30] Z. Jia, A. Gallagher, A. Saxena, and T. Chen. 3d-based rea-
[10] G. Fanelli, M. Dantone, J. Gall, A. Fossati, and L. Van Gool.         soning with blocks, support, and stability. In CVPR, 2013.
     Random forests for real time 3d face analysis. IJCV, 2013. 2          1
[11] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ra-    [31] H. Jiang. Finding approximate convex shapes in rgbd im-
     manan. Object detection with discriminatively trained part            ages. In ECCV. 2014. 2
     based models. PAMI, 2010. 7                                      [32] H. Jiang and J. Xiao. A linear approach to matching cuboids
[12] S. Fothergill, H. M. Mentis, P. Kohli, and S. Nowozin. In-            in RGBD images. In CVPR, 2013. 1, 2
     structing people for training gestural interactive systems. In   [33] M. Kepski and B. Kwolek. Fall detection using ceiling-
     CHI, 2012. 2                                                          mounted 3d depth camera. 2
[13] D. F. Fouhey, A. Gupta, and M. Hebert. Data-driven 3d prim-      [34] H. S. Koppula, A. Anand, T. Joachims, and A. Saxena. Se-
     itives for single image understanding. In ICCV, 2013. 2               mantic labeling of 3d point clouds for indoor scenes. In
[14] D. F. Fouhey, A. Gupta, and M. Hebert. Unfolding an indoor            NIPS, 2011. 2
     origami world. In ECCV. 2014. 2                                  [35] H. S. Koppula, R. Gupta, and A. Saxena. Learning human
[15] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich fea-          activities and object affordances from rgb-d videos. IJRR,
     ture hierarchies for accurate object detection and semantic           2013. 2
     segmentation. In CVPR, 2014. 1                                   [36] A. Krizhevsky, I. Sutskever, and G. E. Hinton. Imagenet
[16] D. Gossow, D. Weikersdorfer, and M. Beetz. Distinctive tex-           classification with deep convolutional neural networks. In
     ture features from perspective-invariant keypoints. In ICPR,          NIPS, 2012. 1, 7
     2012. 2                                                          [37] K. Lai, L. Bo, X. Ren, and D. Fox. A large-scale hierarchical
[17] R. Guo and D. Hoiem. Support surface prediction in indoor             multi-view rgb-d object dataset. In ICRA, 2011. 2
     scenes. In ICCV, 2013. 1                                         [38] D. Lin, S. Fidler, and R. Urtasun. Holistic scene understand-
[18] R. Guo and D. Hoiem. Support surface prediction in indoor             ing for 3d object detection with RGBD cameras. In ICCV,
     scenes. In ICCV, 2013. 2                                              2013. 1, 2, 6
[19] S. Gupta, P. Arbelaez, and J. Malik. Perceptual organization     [39] C. Liu, J. Yuen, and A. Torralba. Nonparametric scene pars-
     and recognition of indoor scenes from RGB-D images. In                ing: Label transfer via dense scene alignment. In CVPR,
     CVPR, 2013. 1, 2                                                      2009. 7
[40] C. Liu, J. Yuen, and A. Torralba. Sift flow: Dense corre-        [59] A. Shrivastava and A. Gupta. Building part-based object de-
     spondence across scenes and its applications. PAMI, 2011.             tectors via 3d geometry. In ICCV, 2013. 2
     6, 7                                                             [60] N. Silberman and R. Fergus. Indoor scene segmentation us-
[41] L. Liu and L. Shao. Learning discriminative representations           ing a structured light sensor. In Proceedings of the Inter-
     from rgb-d video data. In IJCAI, 2013. 2                              national Conference on Computer Vision - Workshop on 3D
[42] M. Luber, L. Spinello, and K. O. Arras. People tracking               Representation and Recognition, 2011. 2
     in rgb-d data with on-line boosted target models. In IROS,       [61] A. Singh, J. Sha, K. S. Narayan, T. Achim, and P. Abbeel.
     2011. 2                                                               Bigbird: A large-scale 3d database of object instances. In
[43] T. Malisiewicz, A. Gupta, and A. A. Efros. Ensemble of                ICRA, 2014. 2
     exemplar-svms for object detection and beyond. In ICCV,          [62] S. Song and J. Xiao. Sliding Shapes for 3D object detection
     2011. 7                                                               in RGB-D images. In ECCV, 2014. 2, 6, 7
[44] J. Mason, B. Marthi, and R. Parr. Object disappearance for       [63] L. Spinello and K. O. Arras. People detection in rgb-d data.
     object discovery. In IROS, 2012. 2                                    In IROS, 2011. 2
[45] O. Mattausch, D. Panozzo, C. Mura, O. Sorkine-Hornung,           [64] S. Stein and S. J. McKenna. Combining embedded ac-
     and R. Pajarola. Object detection and classification from             celerometers with computer vision for recognizing food
     large-scale cluttered indoor scans. In Computer Graphics              preparation activities. In Proceedings of the 2013 ACM inter-
     Forum, 2014. 2                                                        national joint conference on Pervasive and ubiquitous com-
[46] S. Meister, S. Izadi, P. Kohli, M. Hämmerle, C. Rother, and          puting, 2013. 2
     D. Kondermann. When can we use kinectfusion for ground           [65] S. Stein and S. J. McKenna. User-adaptive models for rec-
     truth acquisition? In Proc. Workshop on Color-Depth Cam-              ognizing food preparation activities. 2013. 2
     era Fusion in Robotics, 2012. 2                                  [66] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cre-
[47] A. Mian, M. Bennamoun, and R. Owens. On the repeatabil-               mers. A benchmark for the evaluation of rgb-d slam systems.
     ity and quality of keypoints for local feature-based 3d object        In IROS, 2012. 2
     retrieval from cluttered scenes. IJCV, 2010. 2                   [67] J. Sung, C. Ponce, B. Selman, and A. Saxena. Human ac-
[48] R. Min, N. Kose, and J.-L. Dugelay. Kinectfacedb: A kinect            tivity detection from rgbd images. Plan, Activity, and Intent
     database for face recognition. 2                                      Recognition, 2011. 2
[49] P. K. Nathan Silberman, Derek Hoiem and R. Fergus. Indoor        [68] A. Torralba and A. A. Efros. Unbiased look at dataset bias.
     segmentation and support inference from rgbd images. In               In CVPR, 2011. 8
     ECCV, 2012. 1, 2, 4, 7                                           [69] Z. Wu, S. Song, A. Khosla, X. Tang, and J. Xiao. 3D
                                                                           ShapeNets: A deep representation for volumetric shape mod-
[50] B. Ni, G. Wang, and P. Moulin. Rgbd-hudaact: A color-depth
                                                                           eling. CVPR, 2015. 2
     video database for human daily activity recognition. 2011. 2
                                                                      [70] J. Xiao, J. Hays, K. A. Ehinger, A. Oliva, and A. Torralba.
[51] A. Oliva and A. Torralba. Modeling the shape of the scene:
                                                                           SUN database: Large-scale scene recognition from abbey to
     A holistic representation of the spatial envelope. IJCV, 2001.
                                                                           zoo. In CVPR, 2010. 5, 7
     5, 7
                                                                      [71] J. Xiao, J. Hays, B. C. Russell, G. Patterson, K. Ehinger,
[52] F. Pomerleau, S. Magnenat, F. Colas, M. Liu, and R. Sieg-
                                                                           A. Torralba, and A. Oliva. Basic level scene understanding:
     wart. Tracking a depth camera: Parameter exploration for
                                                                           Categories, attributes and structures. Frontiers in Psychol-
     fast icp. In IROS, 2011. 2
                                                                           ogy, 4(506), 2013. 6
[53] X. Ren, L. Bo, and D. Fox. Rgb-(d) scene labeling: Features
                                                                      [72] J. Xiao, A. Owens, and A. Torralba. SUN3D: A database
     and algorithms. In CVPR, 2012. 1, 2, 6, 7
                                                                           of big spaces reconstructed using SfM and object labels. In
[54] A. Richtsfeld, T. Morwald, J. Prankl, M. Zillich, and                 ICCV, 2013. 1, 2, 4
     M. Vincze. Segmentation of unknown objects in indoor en-         [73] B. Zeisl, K. Koser, and M. Pollefeys. Automatic registration
     vironments. In IROS, 2012. 2                                          of rgb-d scans via salient directions. In ICCV, 2013. 2
[55] B. C. Russell, A. Torralba, K. P. Murphy, and W. T. Freeman.     [74] J. Zhang, C. Kan, A. G. Schwing, and R. Urtasun. Estimat-
     Labelme: a database and web-based tool for image annota-              ing the 3d layout of indoor scenes and its clutter from depth
     tion. IJCV, 2008. 4                                                   sensors. In ICCV, 2013. 2, 5, 7
[56] J. Shotton, R. Girshick, A. Fitzgibbon, T. Sharp, M. Cook,       [75] B. Zhou, J. Xiao, A. Lapedriza, A. Torralba, and A. Oliva.
     M. Finocchio, R. Moore, P. Kohli, A. Criminisi, A. Kipman,            Learning deep features for scene recognition using places
     et al. Efficient human pose estimation from single depth im-          database. In NIPS, 2014. 5, 7
     ages. PAMI, 2013. 1
[57] J. Shotton, B. Glocker, C. Zach, S. Izadi, A. Criminisi, and
     A. Fitzgibbon. Scene coordinate regression forests for cam-
     era relocalization in rgb-d images. In CVPR, 2013. 2
[58] J. Shotton, T. Sharp, A. Kipman, A. Fitzgibbon, M. Finoc-
     chio, A. Blake, M. Cook, and R. Moore. Real-time human
     pose recognition in parts from single depth images. Commu-
     nications of the ACM, 2013. 1
