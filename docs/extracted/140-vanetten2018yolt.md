---
source_id: 140
bibtex_key: vanetten2018yolt
title: You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery
year: 2018
domain_theme: Remote Sensing
verified_pdf: 140_YOLT (Satellite Imagery).pdf
char_count: 52578
---

You Only Look Twice: Rapid Multi-Scale Object Detection In
                                                                 Satellite Imagery
                                                                                                       Adam Van Etten
                                                                                                    CosmiQ Works, In-Q-Tel
                                                                                                      avanetten@iqt.org

                                         ABSTRACT                                                                     The application of deep learning methods to traditional object
                                         Detection of small objects in large swaths of imagery is one of           detection pipelines is non-trivial for a variety of reasons. The unique
                                         the primary problems in satellite imagery analytics. While object         aspects of satellite imagery necessitate algorithmic contributions to
arXiv:1805.09512v1 [cs.CV] 24 May 2018

                                         detection in ground-based imagery has benefited from research             address challenges related to the spatial extent of foreground target
                                         into new deep learning approaches, transitioning such technology          objects, complete rotation invariance, and a large scale search space.
                                         to overhead imagery is nontrivial. Among the challenges is the            Excluding implementation details, algorithms must adjust for:
                                         sheer number of pixels and geographic extent per image: a single
                                                                                                                         Small spatial extent In satellite imagery objects of interest
                                         DigitalGlobe satellite image encompasses > 64 km2 and over 250
                                                                                                                            are often very small and densely clustered, rather than
                                         million pixels. Another challenge is that objects of interest are
                                                                                                                            the large and prominent subjects typical in ImageNet data.
                                         minuscule (often only ∼ 10 pixels in extent), which complicates
                                                                                                                            In the satellite domain, resolution is typically defined as
                                         traditional computer vision techniques. To address these issues, we
                                                                                                                            the ground sample distance (GSD), which describes the
                                         propose a pipeline (You Only Look Twice, or YOLT) that evaluates
                                                                                                                            physical size of one image pixel. Commercially available
                                         satellite images of arbitrary size at a rate of ≥ 0.5 km2 /s. The
                                                                                                                            imagery varies from 30 cm GSD for the sharpest Digital-
                                         proposed approach can rapidly detect objects of vastly different
                                                                                                                            Globe imagery, to 3 − 4 meter GSD for Planet imagery. This
                                         scales with relatively little training data over multiple sensors. We
                                                                                                                            means that for small objects such as cars each object will
                                         evaluate large test images at native resolution, and yield scores of
                                                                                                                            be only ∼ 15 pixels in extent even at the highest resolution.
                                         F 1 > 0.8 for vehicle localization. We further explore resolution and
                                                                                                                         Complete rotation invariance Objects viewed from over-
                                         object size requirements by systematically testing the pipeline at
                                                                                                                            head can have any orientation (e.g. ships can have any
                                         decreasing resolution, and conclude that objects only ∼ 5 pixels in
                                                                                                                            heading between 0 and 360 degrees, whereas trees in Ima-
                                         size can still be localized with high confidence. Code is available at
                                                                                                                            geNet data are reliably vertical).
                                         https://github.com/CosmiQ/yolt
                                                                                                                         Training example frequency There is a relative dearth of
                                                                                                                            training data (though efforts such as SpaceNet1 are attempt-
                                         KEYWORDS                                                                           ing to ameliorate this issue)
                                         Computer Vision, Satellite Imagery, Object Detection                            Ultra high resolution Input images are enormous (often
                                                                                                                            hundreds of megapixels), so simply downsampling to the
                                                                                                                            input size required by most algorithms (a few hundred
                                                                                                                            pixels) is not an option (see Figure 1).
                                         1   INTRODUCTION
                                         Computer vision techniques have made great strides in the past few           The contribution in this work specifically addresses each of these
                                         years since the introduction of convolutional neural networks [5]         issues separately, while leveraging the relatively constant distance
                                         in the ImageNet [13] competition. The availability of large, high-        from sensor to object, which is well known and is typically ∼ 400
                                         quality labelled datasets such as ImageNet [13], PASCAL VOC [2]           km. This coupled with the nadir facing sensor results in consistent
                                         and MS COCO [6] have helped spur a number of impressive ad-               pixel size of objects.
                                         vances in rapid object detection that run in near real-time; three of        Section 2 details in further depth the challenges faced by standard
                                         the best are: Faster R-CNN [12], SSD [7], and YOLO [10] [11]. Faster      algorithms when applied to satellite imagery. The remainder of
                                         R-CNN typically ingests 1000 × 600 pixel images, whereas SSD uses         this work is broken up to describe the proposed contributions as
                                         300 × 300 or 512 × 512 pixel input images, and YOLO runs on either        follows. To address small, dense clusters, Section 3.1 describes
                                         416 × 416 or 544 × 544 pixel inputs. While the performance of all         a new, finer-grained network architecture. Sections 3.2 and 3.3
                                         these frameworks is impressive, none can come remotely close to in-       detail our method for splitting, evaluating, and recombining large
                                         gesting the ∼ 16, 000×16, 000 input sizes typical of satellite imagery.   test images of arbitrary size at native resolution. With regard to
                                         Of these three frameworks, YOLO has demonstrated the greatest             rotation invariance and small labelled training dataset sizes, Section
                                         inference speed and highest score on the PASCAL VOC dataset. The          4 describes data augmentation and size requirements. Finally, the
                                         authors also showed that this framework is highly transferrable           performance of the algorithm is discussed in detail in Section 6.
                                         to new domains by demonstrating superior performance to other
                                         frameworks (i.e., SSD and Faster R-CNN) on the Picasso Dataset
                                         [3] and the People-Art Dataset [1]. Due to the speed, accuracy,
                                         and flexibility of YOLO, we accordingly leverage this system as the
                                         inspiration for our satellite imagery object detection framework.         1 https://aws.amazon.com/public-datasets/spacenet/
                                                                             Figure 2: Challenges of the standard object detection net-
                                                                             work architecture when applied to overhead vehicle detec-
                                                                             tion. Each image uses the same standard YOLO architecture
                                                                             model trained on 416 × 416 pixel cutouts of cars from the
                                                                             COWC dataset. Left: Model applied to a large 4000 × 4000
                                                                             pixel test image downsampled to a size of 416 × 416; none of
Figure 1: DigitalGlobe 8 × 8 km (∼ 16, 000 × 16, 000 pixels)                 the 1142 cars in this image are detected. Right: Model ap-
image at 50 cm GSD near the Panama Canal. One 416 × 416                      plied to a small 416 × 416 pixel cutout; the excessive false
pixel sliding window cutout is shown in red. For an image                    negative rate is due to the high density of cars that cannot
this size, there are ∼ 1500 unique cutouts.                                  be differentiated by the 13 × 13 grid.

2   RELATED WORK                                                                We also note that the large sizes satellite images preclude simple
Deep learning approaches have proven effective for ground-based              approaches to some of the problems noted above. For example,
object detection, though current techniques are often still subopti-         upsampling the image to ensure that objects of interest are large
mal for overhead imagery applications. For example, small objects            and dispersed enough for standard architectures is infeasible, since
in groups, such as flocks of birds present a challenge [10], caused          this approach would also increase runtime many-fold. Similarly,
in part by the multiple downsampling layers of all three convolu-            running a sliding window classifier across the image to search for
tional network approaches listed above (YOLO, SDD, Faster-RCNN).             objects of interest quickly becomes computationally intractable,
Further, these multiple downsampling layers result in relatively             since multiple window sizes will be required for each object size.
course features for object differentiation; this poses a problem if          For perspective, one must evaluate over one million sliding window
objects of interest are only a few pixels in extent. For example,            cutouts if the target is a 10 meter boat in a DigitalGlobe image. Our
consider the default YOLO network architecture, which downsam-               response is to leverage rapid object detection algorithms to evaluate
ples by a factor of 32 and returns a 13 × 13 prediction grid; this           satellite imagery with a combination of local image interpolation
means that object differentiation is problematic if object centroids         on reasonably sized image chips (∼ 200 meters) and a multi-scale
are separated by less than 32 pixels. Accordingly we implement               ensemble of detectors.
a unique network architecture with a denser final prediction grid.              To demonstrate the challenges of satellite imagery analysis, we
This improves performance by yielding finer grained features to              train a YOLO model with the standard network architecture (13×13
help differentiate between classes. This finer prediction grid also          grid) to recognize cars in 416 × 416 pixel cutouts of the COWC
permits classification of smaller objects and denser clusters.               overhead imagery dataset [8] (see Section 4 for further details on
    Another reason object detection algorithms struggle with satel-          this dataset). Naively evaluating a large test image (see Figure
lite imagery is that they have difficulty generalizing objects in new        2) with this network yields a ∼ 100% false positive rate, due to
or unusual aspect ratios or configurations [10]. Since objects can           the 100× downsampling of the test image. Even appropriately
have arbitrary heading, this limited range of invariance to rotation         sized image chips are problematic (again, see Figure 2), as the
is troublesome. Our approach remedies this complication with ro-             standard YOLO network architecture cannot differentiate objects
tations and augmentation of data. Specifically, we rotate training           with centroids separated by less than 32 pixels. Therefore even if
images about the unit circle to ensure that the classifier is agnos-         one restricts attention to a small cutout, performance is often poor
tic to object heading, and also randomly scale the images in HSV             in high density regions with the standard architecture.
(hue-saturation-value) to increase the robustness of the classifier to
varying sensors, atmospheric conditions, and lighting conditions.            3   YOU ONLY LOOK TWICE
    In advanced object detection techniques the network sees the             In order to address the limitations discussed in Section 2, we im-
entire image at train and test time. While this greatly improves             plement an object detection framework optimized for overhead
background differentiation since the network encodes contextual              imagery: You Only Look Twice (YOLT). We extend the Darknet
(background) information for each object, the memory footprint               neural network framework [9] and update a number of the C li-
on typical hardware (NVIDIA Titan X GPUs with 12GB RAM) is                   braries to enable analysis of geospatial imagery and integrate with
infeasible for a 256 megapixel image.                                        external python libraries. We opt to leverage the flexibility and large
                                                                         2
                                                                                              Table 1: YOLT Network Architecture

                                                                                      Layer       Type         Filters   Size/Stride    Output Size
                                                                                      0       Convolutional      32        3×3 / 1      416×416×32
                                                                                      1         Maxpool                    2×2 / 2      208×208×32
                                                                                      2       Convolutional      64        3×3 / 1     208×208× 64
                                                                                      3         Maxpool                    2×2 / 2     104×104× 64
                                                                                      4       Convolutional     128        3×3 / 1     104×104×128
                                                                                      5       Convolutional     64         1×1 / 1      104×104×64
                                                                                      6       Convolutional     128        3×3 / 1     104×104×128
                                                                                      7         Maxpool                    2×2 / 2       52×52×64
                                                                                      8       Convolutional     256        3×3 / 1      52× 52×256
                                                                                      9       Convolutional     128        1×1 / 1      52× 52×128
                                                                                      10      Convolutional     256        3×3 / 1      52× 52×256
Figure 3: Limitations of the YOLO framework (left column,                             11        Maxpool                    2×2 / 2      26× 26×256
quotes from [10]), along with YOLT contributions to address                           12      Convolutional      512       3×3 / 1      26× 26×512
these limitations (right column).                                                     13      Convolutional      256       1×1 / 1      26× 26×256
                                                                                      14      Convolutional      512       3×3 / 1      26× 26×512
                                                                                      15      Convolutional      256       1×1 / 1      26× 26×256
                                                                                      16      Convolutional      512       3×3 / 1      26× 26×512
                                                                                      17      Convolutional     1024       3×3 / 1     26× 26×1024
                                                                                      18      Convolutional     1024       3×3 / 1     26× 26×1024
user community of python for pre- and post-processing. Between
                                                                                      19       Passthrough                10 → 20      26× 26×1024
the updates to the C code and the pre and post-processing code
                                                                                      20      Convolutional     1024       3×3 / 1      26×26×1024
written in python, interested parties need not have any knowledge                     21      Convolutional      Nf        1×1 / 1       26×26×N f
of C to train, test, or deploy YOLT models.

3.1    Network Architecture
To reduce model coarseness and accurately detect dense objects
(such as cars or buildings), we implement a network architecture
that uses 22 layers and downsamples by a factor of 16 Thus, a
416 × 416 pixel input image yields a 26 × 26 prediction grid. Our
architecture is inspired by the 30-layer YOLO network, though this
new architecture is optimized for small, densely packed objects.
The dense grid is unnecessary for diffuse objects such as airports,
but crucial for high density scenes such as parking lots (see Fig-
ure 2). To improve the fidelity of small objects, we also include a
passthrough layer (described in [11], and similar to identity map-
pings in ResNet [4]) that concatenates the final 52 × 52 layer onto
the last convolutional layer, allowing the detector access to finer
grained features of this expanded feature map.
    Each convolutional layer save the last is batch normalized with
a leaky rectified linear activation, save the final layer that utilizes a
linear activation. The final layer provides predictions of bounding
boxes and classes, and has size: N f = N boxes × (N classes + 5), where
N boxes is the number of boxes per grid (5 by default), and N classes
is the number of object classes [10].

3.2    Test Procedure                                                           Figure 4: Graphic of testing procedure for large image sizes,
At test time, we partition testing images of arbitrary size into man-           showing a sliding window going from left to right across Fig-
ageable cutouts and run each cutout through our trained model.                  ure 1. The overlap of the bottom right image is shown in red.
Partitioning takes place via a sliding window with user defined                 Non-maximal suppression of this overlap is necessary to re-
bin sizes and overlap (15% by default), see Figure 4. We record                 fine detections at the edge of the cutouts.
the position of each sliding window cutout by naming each cutout
according to the schema:
   ImageName|row column height width.ext                                        3.3    Post-Processing
For example:                                                                    Much of the utility of satellite (or aerial) imagery lies in its inherent
   panama50cm|1370 1180 416 416.tif                                             ability to map large areas of the globe. Thus, small image chips
                                                                            3
                                                                                     resolution of commercial satellite imagery (30 cm GSD for
                                                                                     DigitalGlobe). Accordingly, we convolve the raw imagery
                                                                                     with a Gaussian kernel and reduce the image dimensions by
                                                                                     half to create the equivalent of 30 cm GSD images. Labels
                                                                                     consist of simply a dot at the centroid of each car, and we
                                                                                     draw a 3 meter bounding box around each car for training
                                                                                     purposes. We reserve the largest geographic region (Utah)
                                                                                     for testing, leaving 13,303 labelled training cars.
                                                                                  Building Footprints The second round of SpaceNet data
                                                                                     consists of 30 cm GSD DigitalGlobe imagery and labelled
                                                                                     building footprints over four cities: Las Vegas, Paris, Shang-
                                                                                     hai, and Khartoum. The labels are precise building foot-
                                                                                     prints, which we transform into bounding boxes encom-
                                                                                     passing 90% of the extent of the footprint. Image segmen-
                                                                                     tation approaches show great promise for this challenge;
Figure 5: YOLT Training data. The top row displays imagery                           nevertheless, we explore YOLT performance on building
and labels for vehicles. The top left panel shows airplanes                          outline detection, acknowledging that since YOLT outputs
labels overlaid on DigitalGlobe imagery, while the middle                            bounding boxes it will never achieve perfect building foot-
panel displays boats overlaid on DigitalGlobe data. The top                          print detection for complex building shapes. Between the
right panel shows aerial imagery of cars from the COWC                               four cities there are 221,336 labelled buildings.
dataset [8], with the red dot denoting the COWC label and                         Airplanes We label eight DigitalGlobe images over airports
the purple box our inferred 3 meter bounding box. The lower                          for a total of 230 objects in the training set.
left panel shows an airport (orange) in 4× downsampled                            Boats We label three DigitalGlobe images taken over coastal
Planet imagery. The lower middle panel shows SpaceNet                                regions for a total of 556 boats.
building footprints in yellow, and the lower right image dis-                     Airports We label airports in 37 Planet images for training
plays inferred YOLT bounding box labels in red.                                      purposes, each with a single airport per chip. For objects
                                                                                     the size of airports, some downsampling is required, as
                                                                                     runways can exceed 1000 pixels in length even in low res-
                                                                                     olution Planet imagery; we therefore downsample Planet
are far less useful than the large field of view images produced by
                                                                                     imagery by a factor of four for training purposes.
satellite platforms. The final step in the object detection pipeline
therefore seeks to stitch together the hundreds or thousands of                 The raw training datasets for airplanes, airports, and watercraft
testing chips into one final image strip.                                    are quite small by computer vision standards, and a larger dataset
   For each cutout the bounding box position predictions returned            may improve the inference performance detailed in Section 6.
from the classifier are adjusted according to the row and column val-           We train with stochastic gradient descent and maintain many of
ues of that cutout; this provides the global position of each bounding       the hyper parameters of [11]: 5 boxes per grid, an initial learning
box prediction in the original input image. The 15% overlap ensures          rate of 10−3 , a weight decay of 0.0005, and a momentum of 0.9.
all regions will be analyzed, but also results in overlapping detec-         Training takes 2 − 3 days on a single NVIDIA Titan X GPU.
tions on the cutout boundaries. We apply non-maximal suppression
to the global matrix of bounding box predictions to alleviate such
overlapping detections.                                                      5    TEST IMAGES
                                                                             To ensure evaluation robustness, all test images are taken from
4   TRAINING DATA                                                            different geographic regions than training examples. For cars, we
Training data is collected from small chips of large images from             reserve the largest geographic region of Utah for testing, yielding
three sources: DigitalGlobe satellites, Planet satellites, and aerial        19,807 test cars. Building footprints are split 75/25 train/test, leaving
platforms. Labels are comprised of a bounding box and category               73,778 test footprints. We label four airport test images for a total of
identifier for each object. We initially focus on five categories:           74 airplanes. Four boat images are labelled, yielding 771 test boats.
airplanes, boats, building footprints, cars, and airports. For objects       Our dataset for airports is smaller, with ten Planet images used for
of very different scales (e.g. airplanes vs airports) we show in             testing. See Table 2 for the train/test split for each category.
Section 6.2 that using two different detectors at different scales is
very effective.
                                                                             6 OBJECT DETECTION RESULTS
     Cars The Cars Overhead with Context (COWC) [8] dataset
       is a large, high quality set of annotated cars from overhead
                                                                             6.1 Universal Classifier Object Detection
       imagery collected over multiple locales. Data is collected                Results
       via aerial platforms, but at a nadir view angle such that it          Initially, we attempt to train a single classifier to recognize all five
       resembles satellite imagery. The imagery has a resolution             categories listed above, both vehicles and infrastructure. We note a
       of 15 cm GSD that is approximately double the current best            number of spurious airport detections in this example (see Figure 6),
                                                                         4
                    Table 2: Train/Test Split

       Object Class    Training Examples     Test Examples
       Airport∗                37                   10
       Airplane∗              230                  74
       Boat∗                  556                  100
       Car†                  19,807              13,303
       Building†            221,336              73,778
        ∗ Internally Labelled
        † External Dataset

                                                                            Figure 7: Car detection performance on a 600 × 600 meter
                                                                            aerial image over Salt Lake City (ImageID = 21) at 30 cm
                                                                            GSD with 1389 cars present. False positives are shown in
                                                                            red, false negatives are yellow, true positives are green, and
                                                                            blue rectangles denote ground truth for all true positive de-
Figure 6: Poor results of the universal model applied to Digi-
                                                                            tections. F1 = 0.95 for this test image, and GPU processing
talGlobe imagery at two different scales (200m, 1500m). Air-
                                                                            time is < 1 second.
planes are in red. The cyan boxes mark spurious detections
of runways, caused in part by confusion from small scale
linear structures such as highways.                                         6.3     Dual Classifier Results
                                                                            For large validation images, we run the classifier at two different
                                                                            scales: 200m, and 2500m. The first scale is designed for vehicles and
                                                                            buildings, and the larger scale is optimized for large infrastructure
as down sampled runways look similar to highways at the wrong               such as airports. We break the validation image into appropriately
scale.                                                                      sized image chips and run each image chip on the appropriate clas-
                                                                            sifier. The myriad results from the many image chips and multiple
6.2    Scale Confusion Mitigation                                           classifiers are combined into one final image, and overlapping detec-
                                                                            tions are merged via non-maximal suppression. We find a detection
There are multiple ways one could address the false positive issues         probability threshold of between 0.3 and 0.4 yields the highest F1
noted in Figure 6. Recall from Section 4 that for this exploratory          score for our validation images.
work our training set consists of only a few dozen airports, far                We define a true positive as having an intersection over union
smaller than usual for deep learning models. Increasing this training       (IOU) of greater than a given threshold. An IOU of 0.5 is often used
set size might improve our model, particularly if the background            as the threshold for a correct detection, though as in Equation 5 of
is highly varied. Another option would be to use post-processing            ImageNet [13] we select a lower threshold for vehicles since we are
to remove any detections at the incorrect scale (e.g. an airport            dealing with very small objects. For SpaceNet building footprints
with a size of ∼ 50 meters). Another option is to simply build dual         and airports we use an IOU of 0.5.
classifiers, one for each relevant scale.                                       Table 3 displays object detection performance and speed over all
   We opt to utilize the scale information present in satellite im-         test images for each object category. YOLT performs relatively well
agery and run two different classifiers: one trained for vehicles +         on airports, airplanes, and boats, despite small training set sizes.
buildings, and the other trained only to look for airports. Running         YOLT is not optimized for building footprint extraction, though
the second airport classifier on down sampled images has a minimal          performs somewhat competitively on the SpaceNet dataset; the top
impact on runtime performance, since in a given image there are             score on the recent SpaceNet challenge achieved an F1 score of 0.692 ,
approximately 100 times more 200 meter chips than 2000 meter
chips.                                                                      2 https://spacenetchallenge.github.io/Competitions/Competition2.html

                                                                        5
                                                                             Figure 9: Top: F1 score per COWC test scene. (F 1 = 0.90±0.09).
                                                                             Bottom: Number of detections as a fraction of ground truth
                                                                             number (Fc = 0.95 ± 0.05. Dot colors correspond to the test
                                                                             scene, with the multiple red dots indicating central Salt Lake
Figure 8: YOLT classifier applied to a SpaceNet DigitalGlobe                 City cutouts. The dotted orange line denotes the weighted
50 cm GSD image containing airplanes (blue), boats (red),                    mean, with the yellow band displaying the weighted stan-
and runways (orange). In this image we note the following                    dard deviation.
F1 scores: airplanes = 0.83, boats = 0.84, airports = 1.0.

              Table 3: YOLT Performance and Speed

                Object Class            F1 Score      Run Time               6.4    Detailed Performance Analysis
                                                     (km2 /min)              The large test set of ∼ 20, 000 cars in the nine Utah images of the
                Car†                   0.90 ± 0.09       32                  COWC dataset enables detailed performance analyses. The majority
                Airplane∗              0.87 ± 0.08       32                  of the cars (> 13, 000) lie in the image over central Salt Lake City so
                Boat ∗                 0.82 ± 0.07       32                  we split this image into sixteen smaller 600 × 600 meter regions to
                Building∗              0.61 ± 0.15       32                  even out the number of cars per image. We remove one test scene
                Airport∗               0.91 ± 0.14      6000                 that has only 61 cars in the scene, leaving 23 test scenes, with mean
                 † IOU = 0.25                                                count per test image of 1130 ± 540. We apply a YOLT model trained
                 ∗ IOU = 0.5                                                 to find cars on these test scenes.
                                                                                In Figure 9 we display the F1 score for each scene, along with
                                                                             the car count accuracy. Total car count in a specified region may
while the YOLT score of 0.61 puts it in the top 3. We report inference       be a more valuable metric in the commercial realm than F1 score.
speed in terms of GPU time to run the inference step. Inference              Accordingly, we compute the number of predicted cars for each
runs rapidly on the GPU, at ∼ 50 frames per second. Currently,               scene as a fraction of ground truth number (Fc = N predicted /N truth ).
pre-processing (i.e., splitting test images into smaller cutouts) and        Like the F1 score, a value of 1.0 denotes perfect prediction for the
post-processing (i.e., stitching results back into one global image)         fractional car count metric. The COWC [8] authors sought to count
is not fully optimized and is performed on the CPU, which adds               (rather than localize) the number of cars in test images, and achieved
a factor of ≈ 2 to run time. The inference speed translates to a             an error of 0.19%. Total count error for YOLT on the COWC data is
runtime of < 6 minutes to localize all vehicles in an area of the size       0.90%.
of Washington DC, and < 2 seconds to localize airports over this                Inspection of Figure 9 reveals that the F1 score and ground truth
area. DigitalGlobe’s WorldView3 satellite3 covers a maximum of               fraction are quite high for typical urban scenes, (e.g. ImageID = 21
680,000 km2 per day, so at YOLT inference speed a 16 GPU cluster             shown in Figure 7). The worst outlier in Figure 9 is ImageID =
would provide real-time inference on satellite imagery.                      2, with an F1 score of 0.67, and 2860 cars present. This location
                                                                             corresponds to an automobile junkyard, an understandably difficult
3 http://worldview3.digitalglobe.com                                         region to analyze.
                                                                         6
                                                                                 Figure 11: Performance of the 0.3m model applied to vari-
                                                                                 ous resolutions. The 23 thin lines display the performance
                                                                                 of each individual test scene; most of these lines are tightly
                                                                                 clustered about the mean, denoted by the solid red. The red
                                                                                 band displays ±1 STD. The model peaks at F1 = 0.9 for the
                                                                                 trained resolution of 0.3m, and rapidly degrades when eval-
                                                                                 uated with lower resolution data; it also degrades somewhat
                                                                                 for higher resolution 0.15m data.

Figure 10: COWC [8] training data convolved and resized to
various resolutions from the original 15 cm resolution (top
left); bounding box labels are plotted in blue.

7    RESOLUTION PERFORMANCE STUDY
The uniformity of object sizes in the COWC [8] dataset enables
a detailed resolution study. To study the effects of resolution on               Figure 12: Object detection results on different resolutions
object detection, we convolve the raw 15 cm imagery with a Gauss-                on the same 120 × 120 meter Salt Lake City cutout of COWC
ian kernel and reduce the image dimensions to create additional                  data. The cutout on the left is at 15 cm GSD, with an F1 score
training and testing corpora at [0.30, 0.45, 0.60, 0.75, 0.90, 1.05, 1.20,       of 0.94, while the cutout on the right is at 90 cm GSD, with
1.50, 1.80, 2.10, 2.40, 3.00] meters.                                            an F1 score of 0.84.
    Initially, we test the multi-resolution test data on a single model
(trained at 0.30 meters), and in Figure 11 demonstrate that the
ability of this model to extrapolate to multiple resolutions is poor.            are rarely well suited to the object sizes or orientations present in
Subsequently, we train a separate model for each resolution, for                 satellite imagery, however, nor are they designed to handle images
thirteen models total. Creating a high quality labelled dataset at               with hundreds of megapixels.
low resolution (2.4m GSD, for example) is only possible because                      To address these limitations we implemented a fully convolu-
we downsample from already labelled high resolution 15 cm data;                  tional neural network pipeline (YOLT) to rapidly localize vehicles,
typically low resolution data is very difficult to label with high               buildings, and airports in satellite imagery. We noted poor results
accuracy.                                                                        from a combined classifier due to confusion between small and
    For objects ∼ 3 meters in size we observe from Figure 13 that                large features, such as highways and runways. Training dual clas-
object detection performance degrades from F 1 = 0.92 for objects                sifiers at different scales (one for buildings/vehicles, and one for
20 pixels in size to F 1 = 0.27 for objects 1 pixel in size, with a mean         infrastructure), yielded far better results.
error of 0.09. Interestingly, the F1 score only degrades by only                     This pipeline yields an object detection F1 score of ≈ 0.6 − 0.9,
≈ 5% as objects shrink from 20 to 5 pixels in size (0.15m to 0.60m               depending on category. While the F1 scores may not be at the
GSD). At least for cars viewed from overhead, one can conclude that              level many readers are accustomed to from ImageNet competitions,
object sizes of ≥ 5 pixels yield object detection scores of F 1 > 0.85.          object detection in satellite imagery is still a relatively nascent field
The curves of Figure 11 degrade far faster than Figures 13 and 14,               and has unique challenges. In addition, our training dataset for
illustrating that a single model fit at high resolution is inferior to a         most categories is relatively small for supervised learning methods,
series of models trained at each respective resolution.                          and the F1 scores could possibly be improved with further post-
                                                                                 processing of detections.
8    CONCLUSIONS                                                                     We also demonstrated the ability to train on one sensor (e.g. Dig-
Object detection algorithms have made great progress as of late                  italGlobe), and apply our model to a different sensor (e.g. Planet).
in localizing objects in ImageNet style datasets. Such algorithms                We show that at least for cars viewed from overhead, object sizes
                                                                             7
Figure 13: Object detection F1 score for ground sample dis-                               Figure 14: Fraction of predicted number of cars to ground
tances of 0.15 − 3.0 meters (bottom axis), corresponding to                               truth, with a unique model for each resolution (bottom axis)
car size of 20 − 1 pixel(s) (top axis). At each of the thir-                              and object pixel size (top axis). A fraction of 1.0 means that
teen resolutions we evaluate test scenes with a unique model                              the correct number of cars was predicted, while if the frac-
trained at that resolution. The 23 thin lines display the per-                            tion is below 1.0 too few cars were predicted. The thin bands
formance of the individual test scenes; most of these lines                               denote the performance of the 23 individual scenes, with the
are tightly clustered about the mean, denoted by the blue                                 dashed blue line showing the weighted mean and the red
dashed line. The red band displays ±1 STD. We fit a piecewise                             band displaying ±1 STD. We fit a piecewise linear model to
linear model to the data, shown as the dotted cyan line. Be-                              the data, shown as the dotted cyan line. Below the inflection
low the inflection point (large cyan dot) of 0.61 meters (cor-                            point (large cyan dot) of 0.86 meters the slope is essentially
responding to a car size of 5 pixels) the F1 score degrades                               flat with a slope of −0.03; between 0.87 m and 3 m GSD the
slowly with a slope of ∆F 1/∆GSD = −0.10; between 0.60 m                                  slope is steeper at −0.20. For resolutions sharper than 0.86
and 3.0 m GSD the slope is steeper at −0.26. The F1 scores at                             meters the predicted number of cars is within 4% of ground
0.15 m, 0.60 m, and 3.0 m GSD are 0.92, 0.87, and 0.27, respec-                           truth.
tively.
                                                                                           [5] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. 2012. ImageNet Classifi-
                                                                                               cation with Deep Convolutional Neural Networks. In Advances in Neural Infor-
                                                                                               mation Processing Systems 25, F. Pereira, C. J. C. Burges, L. Bottou, and K. Q. Wein-
of ≥ 5 pixels yield object detection scores of F 1 > 0.85. The de-                             berger (Eds.). Curran Associates, Inc., 1097–1105. http://papers.nips.cc/paper/
tection pipeline is able to evaluate satellite and aerial images of                            4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
                                                                                           [6] Tsung-Yi Lin, Michael Maire, Serge J. Belongie, Lubomir D. Bourdev, Ross B. Gir-
arbitrary input size at native resolution, and processes vehicles and                          shick, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C. Lawrence
buildings at a rate of ≈ 30 km2 per minute, and airports at a rate of                          Zitnick. 2014. Microsoft COCO: Common Objects in Context. CoRR abs/1405.0312
≈ 6, 000 km2 per minute. At this inference speed, a 16 GPU cluster                             (2014). http://arxiv.org/abs/1405.0312
                                                                                           [7] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott E. Reed,
could provide real-time inference on the DigitalGlobe WorldView3                               Cheng-Yang Fu, and Alexander C. Berg. 2015. SSD: Single Shot MultiBox Detector.
satellite feed.                                                                                CoRR abs/1512.02325 (2015). http://arxiv.org/abs/1512.02325
                                                                                           [8] T. Nathan Mundhenk, Goran Konjevod, Wesam A. Sakla, and Kofi Boakye. 2016.
                                                                                               A Large Contextual Dataset for Classification, Detection and Counting of Cars
                                                                                               with Deep Learning. CoRR abs/1609.04453 (2016). http://arxiv.org/abs/1609.04453
                                                                                           [9] J. Redmon. 2013-2017.         Darknet: Open source neural networks in c.
ACKNOWLEDGMENTS                                                                                http://pjreddie.com/darknet/ (2013-2017). http://pjreddie.com/darknet/
We thank Karl Ni for very helpful comments.                                               [10] Joseph Redmon, Santosh Kumar Divvala, Ross B. Girshick, and Ali Farhadi. 2015.
                                                                                               You Only Look Once: Unified, Real-Time Object Detection. CoRR abs/1506.02640
                                                                                               (2015). http://arxiv.org/abs/1506.02640
REFERENCES                                                                                [11] Joseph Redmon and Ali Farhadi. 2016. YOLO9000: Better, Faster, Stronger. CoRR
                                                                                               abs/1612.08242 (2016). http://arxiv.org/abs/1612.08242
[1] Hongping Cai, Qi Wu, Tadeo Corradi, and Peter Hall. 2015. The Cross-Depiction         [12] Shaoqing Ren, Kaiming He, Ross B. Girshick, and Jian Sun. 2015. Faster R-CNN:
    Problem: Computer Vision Algorithms for Recognising Objects in Artwork and                 Towards Real-Time Object Detection with Region Proposal Networks. CoRR
    in Photographs. CoRR abs/1505.00110 (2015). http://arxiv.org/abs/1505.00110                abs/1506.01497 (2015). http://arxiv.org/abs/1506.01497
[2] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisserman. 2010.       [13] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean
    The Pascal Visual Object Classes (VOC) Challenge. International Journal of                 Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexan-
    Computer Vision 88, 2 (June 2010), 303–338.                                                der C. Berg, and Li Fei-Fei. 2015. ImageNet Large Scale Visual Recognition
[3] Shiry Ginosar, Daniel Haas, Timothy Brown, and Jitendra Malik. 2014. Detecting             Challenge. International Journal of Computer Vision (IJCV) 115, 3 (2015), 211–252.
    People in Cubist Art. CoRR abs/1409.6235 (2014). http://arxiv.org/abs/1409.6235            https://doi.org/10.1007/s11263-015-0816-y
[4] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2015. Deep Residual
    Learning for Image Recognition. CoRR abs/1512.03385 (2015). http://arxiv.org/
    abs/1512.03385
                                                                                      8
