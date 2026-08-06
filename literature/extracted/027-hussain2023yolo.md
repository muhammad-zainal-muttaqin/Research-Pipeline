---
source_id: 027
bibtex_key: hussain2023yolo
title: YOLO-v1 to YOLO-v8, the Rise of YOLO and Its Complementary Nature toward Digital Manufacturing and Industrial Defect Detection
year: 2023
domain_theme: Survei YOLO
verified_pdf: 27_Review_YOLO_Manufaktur_Hussain.pdf
char_count: 333288
---

machines
Review
YOLO-v1 to YOLO-v8, the Rise of YOLO and Its
Complementary Nature toward Digital Manufacturing and
Industrial Defect Detection
Muhammad Hussain

                                         Department of Computer Science, School of Computing and Engineering, University of Huddersfield,
                                         Queensgate, Huddersfield HD1 3DH, UK; m.hussain@hud.ac.uk

                                         Abstract: Since its inception in 2015, the YOLO (You Only Look Once) variant of object detectors has
                                         rapidly grown, with the latest release of YOLO-v8 in January 2023. YOLO variants are underpinned
                                         by the principle of real-time and high-classification performance, based on limited but efficient
                                         computational parameters. This principle has been found within the DNA of all YOLO variants
                                         with increasing intensity, as the variants evolve addressing the requirements of automated quality
                                         inspection within the industrial surface defect detection domain, such as the need for fast detection,
                                         high accuracy, and deployment onto constrained edge devices. This paper is the first to provide an
                                         in-depth review of the YOLO evolution from the original YOLO to the recent release (YOLO-v8) from
                                         the perspective of industrial manufacturing. The review explores the key architectural advancements
                                         proposed at each iteration, followed by examples of industrial deployment for surface defect detection
                                         endorsing its compatibility with industrial requirements.

                                         Keywords: industrial defect detection; object detection; smart manufacturing; quality inspection

                                         1. Introduction
                                              Humans via the visual cortex, a primary cortical region of the brain responsible for
Citation: Hussain, M. YOLO-v1 to         processing visual information [1], are able to observe, recognize [2], and differentiate
YOLO-v8, the Rise of YOLO and Its        between objects instantaneously [3]. Studying the inner workings of the visual cortex and
Complementary Nature toward              the brain in general has paved the way for artificial neural networks (ANNs) [4] along
Digital Manufacturing and Industrial     with a myriad of computational architectures residing under the deep learning umbrella.
Defect Detection. Machines 2023, 11,     In the last decade, owing to rapid and revolutionary advancements in the field of deep
677. https://doi.org/10.3390/            learning [5], researchers have exerted their efforts on providing efficient simulation of the
machines11070677                         human visual system to computers, i.e., enabling computers to detect objects of interest
Academic Editor: Sang Do Noh
                                         within static images and video [6], a field known as computer vision (CV) [7]. CV is
                                         a prevalent research area for deep learning researchers and practitioners in the present
Received: 30 May 2023                    decade. It is composed of subfields consisting of image classification [8], object detection [9],
Revised: 15 June 2023                    and object segmentation [10]. All three fields share a common architectural theme, namely,
Accepted: 21 June 2023
                                         manipulation of convolutional neural networks (CNNs) [11]. CNNs are accepted as the de
Published: 23 June 2023
                                         facto when dealing with image data. In comparison with conventional image processing
                                         and artificial defection methods, CNNs utilize multiple convolutional layers coupled with
                                         aggregation, i.e., pooling structures aiming to unearth deep semantic features hidden away
Copyright:   © 2023 by the author.
                                         within the pixels of the image [12].
Licensee MDPI, Basel, Switzerland.
                                              Artificial intelligence (AI) has found opportunities in industries across the spectrum
This article is an open access article   from renewable energy [13,14] and security to healthcare [15] and the education sector.
distributed under the terms and          However, one industry that is poised for significant automation through CV is the manu-
conditions of the Creative Commons       facturing industry. Quality inspection (QI) is an integral part of any manufacturing domain
Attribution (CC BY) license (https://    providing integrity and confidence to the clients on the quality of the manufactured prod-
creativecommons.org/licenses/by/         ucts [16]. Manufacturing has wide scope for automation; however, when dealing with
4.0/).                                   surface inspection [17], defects can take sophisticated forms [18], making human-based

Machines 2023, 11, 677. https://doi.org/10.3390/machines11070677                                        https://www.mdpi.com/journal/machines
Machines 2023, 11, 677                                                                                            2 of 25

                         quality inspection a cumbersome task with manifold inefficiencies linked to human bias,
                         fatigue, cost, and downtime [19]. These inefficiencies provide an opportunity for CV-based
                         solutions to present automated quality inspection that can be integrated within existing
                         surface defect inspection processes, increasing efficiency whilst overcoming bottlenecks
                         presented via conventional inspection methodologies [20].
                              However, for success, CV-based architectures must conform to a stringent set of
                         deployment requirements that can vary from one manufacturing sector to another [21]. In
                         the majority of applications, the focus is not only on the determination of the defect, but also
                         on multiple defects along with the locality details of each [22]. Therefore, object detection
                         is preferred over image classification since the latter only focuses on determination of
                         object within the image without providing any locality information. Architectures within
                         the object detection domain can be classified into single-stage or two-stage detectors [23].
                         Two-stage detectors split the detection process into two stages: Feature extraction/proposal
                         followed by regression and classification for acquiring the output [24]. Although this can
                         provide high accuracy, it comes with a high computational demand making it inefficient for
                         real-time deployment onto constrained edge devices. Single-stage detectors, on the other
                         hand, merge the two processes into one, enabling the classification and regression via a
                         single pass, significantly reduce the computational demand, and provide a more compelling
                         case for production-based deployment [25]. Although many single-stage detectors have
                         been introduced, such as single shot detector (SSD) [26], deconvolutional single shot
                         detector (D-SSD) [27], and RetinaNet [28], the YOLO (You Only Look Once) [29] family of
                         architectures seems to be gaining high traction due to its high compatibility with industrial
                         requirements, such as accuracy, lightweight, and edge-friendly deployment conditions.
                         The last half-a-decade has been dominated by the introduction of YOLO variants, with the
                         most recent variant introduced in 2022 as YOLO-v8.
                              To the best of our knowledge, there is no cohesive review of the advancing YOLO
                         variants, benchmarking technical advancements, and their implications on industrial
                         deployment. This paper reviews the YOLO variants released to the present date, focusing
                         on presenting the key technical contributions of each YOLO iteration and its impact on key
                         industrial metrics required for deployment, such as accuracy, speed, and computational
                         efficacy. As a result, the aim is to provide researchers and practitioners with a better
                         understanding of the inner workings of each variant, enabling them to select the most
                         relevant architecture based on their industrial requirements. Additionally, literature on
                         the deployment of YOLO architectures for various industrial surface defect detection
                         applications is presented.
                              The subsequent structure of the review is as follows. The first section provides an
                         introduction to single- and two-stage detectors and the anatomy for single-stage object
                         detectors. Next, the evolution of YOLO variants is presented, detailing the key contributions
                         from YOLO-v1 to YOLO-v8, followed by a review of the literature focused on YOLO-based
                         implementation of industrial surface defect detection. Finally, the discussion section
                         focuses on summarizing the reviewed literature, followed by extracted conclusions, future
                         directions, and challenges are presented.

                         Object Detection
                              CNNs can be categorized as convolution-based feed forward neural networks for
                         classification purposes [30]. The input layer is followed by multiple convolutional layers
                         to acquire an increased set of smaller-scale feature maps. These feature maps post further
                         manipulation are transformed into one-dimensional feature vectors before being used as
                         input to the fully connected layer(s). The process of feature extraction and feature map
                         manipulation is vital to the overall accuracy of the network; therefore, this can involve the
                         stacking of multiple convolutional and pooling layers for richer feature maps. Popular
                         architectures for feature extraction include AlexNet [31], VGGNet [32], GoogleNet [33], and
                         ResNet [34]. AlexNet is proposed in 2012 and consists of five convolutional, three pooling,
                         and three fully connected layers primarily utilized for image classification tasks. VGGNet
Machines 2023, 11, x FOR PEER REVIEW                                                                                                          3 of 26

 Machines 2023, 11, 677         and ResNet [34]. AlexNet is proposed in 2012 and consists of five convolutional,                           3 of 25three
                                pooling, and three fully connected layers primarily utilized for image classification tasks.
                                VGGNet focused on performance enhancement by increasing the internal depth of the
                                architecture, introducing several variants with increased layers, VGG-16/19. GoogleNet
                                focused on performance enhancement by increasing the internal depth of the architecture,
                                introduced several
                                introducing     the cascading
                                                          variantsconcept     by cascading
                                                                    with increased      layers, multiple
                                                                                                 VGG-16/19.   ‘inception’
                                                                                                                   GoogleNetmodules,     whilst
                                                                                                                                introduced    theRes-
                                cascading concept by cascading multiple ‘inception’ modules, whilst ResNet introduced it
                                Net   introduced      the  concept   of  skip-connections       for   preserving     information      and  making
                                available
                                the  concept from   the earlier to thefor
                                                of skip-connections        later  layers ofinformation
                                                                              preserving      the architecture.
                                                                                                              and making it available from
                                       The motive
                                the earlier            for an
                                              to the later      object
                                                             layers of detector    is to infer whether the object(s) of interest are resid-
                                                                       the architecture.
                                ing inThethemotive
                                              image foror present   thedetector
                                                            an object     frame ofisato  video.
                                                                                           inferIfwhether
                                                                                                     the object(s)    of interest
                                                                                                                the object(s)   of are  present,
                                                                                                                                    interest  are the
                                detector in
                                residing    returns    the respective
                                                the image      or present class
                                                                             the and
                                                                                  framelocality,   i.e., location
                                                                                           of a video.      If the dimensions       of the object(s).
                                                                                                                    object(s) of interest     are
                                present,   the detector
                                Object detection       can returns    the divided
                                                             be further     respectiveintoclass
                                                                                            twoand      locality, i.e., Two-stage
                                                                                                   sub-categories:      location dimensions
                                                                                                                                       methods and
                                of the object(s).
                                one-stage     methods Object    detection
                                                           as shown         can be 1.
                                                                        in Figure    further    dividedinitiates
                                                                                         The former         into two thesub-categories:
                                                                                                                          first stage with  Two-
                                                                                                                                               the se-
                                stage   methods     and    one-stage   methods      as  shown     in  Figure    1.  The
                                lection of numerous proposals, then in the second stage, performs prediction on the pro- former    initiates  the
                                first
                                posed stage   with the
                                         regions.         selection
                                                     Examples     of of  numerous
                                                                     two-stage         proposals,
                                                                                    detectors         then the
                                                                                                 include     in the  second
                                                                                                                  famous      stage, performs
                                                                                                                            R-CNN      [35] variants,
                                prediction
                                such as Fast R-CNN [36] and Faster R-CNN [37], boasting high accuraciesthe
                                               on the  proposed    regions.    Examples     of two-stage      detectors   include     butfamous
                                                                                                                                           low com-
                                R-CNN [35] variants, such as Fast R-CNN [36] and Faster R-CNN [37], boasting high
                                putational eﬃciency. The latter transforms the task into a regression problem, eliminating
                                accuracies but low computational efficiency. The latter transforms the task into a regression
                                the need for an initial stage dedicated to selecting candidate regions; therefore, the candi-
                                problem, eliminating the need for an initial stage dedicated to selecting candidate regions;
                                date selection and prediction is achieved in a single pass. As a result, architectures falling
                                therefore, the candidate selection and prediction is achieved in a single pass. As a result,
                                into this category
                                architectures     fallingare  computationally
                                                           into  this category are  less  demanding, generating
                                                                                        computationally                    higher FPS
                                                                                                               less demanding,            and detec-
                                                                                                                                     generating
                                higher FPS and detection speed, but in general the accuracy tends to be inferior with respect de-
                                tion   speed,   but  in  general   the   accuracy    tends    to  be  inferior    with  respect   to  two-stage
                                tectors.
                                to two-stage detectors.

                                Figure 1. Object
                                Figure 1. Objectdetector
                                                 detectoranatomy.
                                                          anatomy.

                                2. Original YOLO Algorithm
                                2. Original YOLO Algorithm
                                      YOLO was introduced to the computer vision community via a paper release in 2015 by
                                      YOLO was introduced to the computer vision community via a paper release in 2015
                                Joseph Redmon et al. [29] titled ‘You Only Look Once: Unified, Real-Time Object Detection’.
                                by  Joseph    Redmon et
                                The paper reframed           al. [29]
                                                          object      titled ‘You
                                                                  detection,        Only Look
                                                                              presenting          Once: Unified,
                                                                                           it essentially           Real-Time
                                                                                                           as a single           Object De-
                                                                                                                        pass regression
                                tection’. The
                                problem,          paperwith
                                            initiating   reframed
                                                              image object    detection,
                                                                      pixels and  movingpresenting
                                                                                            to bounding it essentially
                                                                                                           box and classas probabilities.
                                                                                                                           a single pass re-
                                The proposed approach based on the ‘unified’ concept enabled the simultaneous box
                                gression    problem,     initiating   with  image    pixels  and   moving    to  bounding          and class
                                                                                                                             prediction
                                probabilities.     The  proposed    approach     based  on  the  ‘unified’  concept
                                of multiple bounding boxes and class probabilities, improving both speed and accuracy.enabled   the  simulta-
                                neous    prediction
                                      Since             of multiple
                                             its inception              bounding
                                                            in 2016 until            boxes
                                                                           the present  yearand    class
                                                                                              (2023), the probabilities,
                                                                                                          YOLO family has  improving
                                                                                                                              continuedboth
                                speed
                                to      and
                                   evolve   at accuracy.
                                                a rapid pace. Although the initial author (Joseph Redmon) halted further work
                                within   the computer
                                      Since                vision
                                               its inception       domain
                                                               in 2016  untilatthe
                                                                                YOLO-v3
                                                                                   present[38],
                                                                                             yearthe   effectiveness
                                                                                                   (2023),  the YOLO   and  potential
                                                                                                                         family        of
                                                                                                                                 has contin-
                                the core  ‘unified’   concept   have  been  further  developed     by several  authors,
                                ued to evolve at a rapid pace. Although the initial author (Joseph Redmon) halted furtherwith  the latest
                                addition
                                work withinto thetheYOLO   familyvision
                                                      computer     coming    in the form
                                                                           domain         of YOLO-v8.
                                                                                     at YOLO-v3     [38], Figure  2 presents the
                                                                                                          the eﬀectiveness    andYOLO
                                                                                                                                    potential
                                evolution
                                of the core  timeline.
                                                 ‘unified’ concept have been further developed by several authors, with the
                                latest addition to the YOLO family coming in the form of YOLO-v8. Figure 2 presents the
                                2.1. Original YOLO
                                YOLO evolution timeline.
                                     The core principle proposed by YOLO-v1 was the imposing of a grid cell with dimen-
                                sions of s×s onto the image. In the case of the center of the object of interest falling into one
                                of the grid cells, that particular grid cell would be responsible for the detection of that object.
                                This permitted other cells to disregard that object in the case of multiple appearances.
Machines
 Machines2023,
           2023,11,
                 11,x677
                      FOR PEER REVIEW                                                                                             4 of 25 4 of 26

                                 Figure2.2.YOLO
                                 Figure     YOLOevolution
                                                 evolution  timeline.
                                                          timeline.

                                      For implementation
                                 2.1. Original YOLO       of object detection, each grid cell would predict B bounding boxes
                                 along with the dimensions and confidence scores. The confidence score was indicative of
                                      The core
                                 the absence     principleofproposed
                                             or presence                by YOLO-v1
                                                             an object within           was the
                                                                               the bounding    box.imposing   ofthe
                                                                                                     Therefore,  a grid  cell with di-
                                                                                                                    confidence
                                 mensions   of s×s onto  the  image.  In
                                 score can be expressed as Equation (1):  the  case of the  center   of the object  of interest falling
                                     into one of the grid cells, that particular grid cell would be responsible for the detection
                                                                                                       truth
                                                                con f idence
                                     of that object. This permitted          score
                                                                         other     = pto
                                                                                cells  (object ) ∗ IoUthat
                                                                                         disregard     pred object in the case of (1)
                                                                                                                                   multiple
                                     appearances.
                                     where p(object) signified the probability of the object being present, with a range of 0–1 with
                                          For implementation of object detection, each grid cell would predict B bounding
                                     0 indicating that the object is not present and IoU truth    represented the intersection-over-
                                                                                            pred scores.
                                     boxes along with the dimensions and confidence                       The confidence score was indic-
                                     union with the predicted bounding box with respect to the ground truth bounding box.
                                     ativeEach
    Machines 2023, 11, x FOR PEER REVIEW   of the  absence  or presence    of an object  within    the bounding
                                                bounding box consisted of five components (x, y, w, h, and the    box. Therefore,
                                                                                                                           5 of 26 the con-
                                                                                                                     confidence score)
                                     fidence
                                     with the score   cancomponents
                                              first four  be expressed    as Equationto(1):
                                                                       corresponding     center coordinates (x, y, width, and height)
                                 of the respective bounding box𝑐𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒
                                                                as shown in Figure
                                                                          𝑠𝑐𝑜𝑟𝑒    3.
                                                                                = 𝑝(𝑜𝑏𝑗𝑒𝑐𝑡) ∗ 𝐼𝑜𝑈                                            (1)
                                  where 𝑝(𝑜𝑏𝑗𝑒𝑐𝑡) signified the probability of the object being present, with a range of 0–1
                                  with 0 indicating that the object is not present and 𝐼𝑜𝑈     represented the intersection-
                                  over-union with the predicted bounding box with respect to the ground truth bounding
                                  box.
                                       Each bounding box consisted of five components (x, y, w, h, and the confidence score)
                                  with the first four components corresponding to center coordinates (x, y, width, and height)
                                  of the respective bounding box as shown in Figure 3.
                                  Figure 3.
                                 Figure  3. YOLO-v1
                                            YOLO-v1 preliminary
                                                    preliminaryarchitecture.
                                                                architecture.

                                       As alluded to earlier, the input image is split into s × s grid cells (default = 7 × 7), with
                                  each cell predicting B bounding boxes, each containing five parameters and sharing pre-
                                  diction probabilities of classes (C). Therefore, the parameter output would take the fol-
                                  lowing form, expressed in (2):

                                                                           𝑠 × 𝑠 × (5 ∗ 𝐵 + 𝐶)                                   (2)
                        Considering
               As alluded                   the example
                                    to earlier,    the inputof        YOLO
                                                                    image         network
                                                                               is split    into with      eachcells
                                                                                                  s × s grid   cell (default
                                                                                                                    bounding   = 7box
                                                                                                                                    × 7),p
     eachset   celltopredicting
                         2 and evaluating B bounding the benchmark
                                                              boxes, eachCOCO     containingdataset      consisting
                                                                                                      five parametersof 80 classes,
                                                                                                                         and   sharing th
Figure 3. YOLO-v1 preliminary architecture.
     diction  eterprobabilities
                      output would         ofbe    given(C).
                                              classes       as expressed
                                                                   Therefore,inthe      (3):parameter output would take the
     lowing
     As  alluded
     Machines       form,
              2023,to
                    11,earlier,
                        677     expressed
                                the input imagein   (2):into s × s grid cells (default = 7 × 7), with
                                                is split                                                                    5 of 25
each cell predicting B bounding boxes, each containing five parameters       7 ×and
                                                                                  7 ×sharing
                                                                                        (5 ∗ 2pre-+ 80)
diction probabilities of classes (C). Therefore, the parameter output would take the fol-
                                                                     𝑠 × 𝑠 × (5 ∗ 𝐵 + 𝐶 )
lowing form, expressed
                    Theinfundamental
                            (2):                 motive
                                          As alluded          of YOLO
                                                        to earlier,             and object
                                                                    the input image                detection
                                                                                        is split into             in general
                                                                                                      s × s grid cells (default = 7is  the obje
                                                                                                                                    × 7),
                                    with each cell predicting B bounding boxes, each containing five parameters and sharing
             tion   and localization            (5 ∗ 𝐵bounding
                                          × 𝑠 ×via                      boxes.      Therefore,    (2) twocellsets   of bounding
              Considering         the                                                                                                thebox   ve
                                        𝑠example       +of𝐶) YOLO         network         with
                                    prediction   probabilities   of classes   (C). Therefore,   theeach
                                                                                                     parameter   bounding
                                                                                                                output            box
                                                                                                                         would take      predi
      set torequired,
               2 and
      Considering           i.e.,ofvector
                         evaluating
                   the example      following
                                   YOLO    theyform,
                                                 is   the
                                                 benchmark
                                           network     with representative
                                                        expressed   in (2):
                                                            each cell  COCO
                                                                        bounding box  ofprediction
                                                                                           ground
                                                                                     dataset            truth and
                                                                                                  consisting      of 80  vector
                                                                                                                           classes, 𝑦̇ is
                                                                                                                                        thethe
                                                                                                                                             pap
set to 2 and evaluating the benchmark COCO dataset consisting of 80 classes, the param-
eter output  vector.
      eter would
             output      To asaddress
                        would
                    be given        be given
                                 expressed  inmultiple        bounding
                                               (3): as expressed                ×boxes
                                                                                   s × (5 ∗ Bcontaining
                                                                            ins (3):         + C)               no object or the      (2) sam
               YOLO opts for non-maximum            7×Considering
                                                         7 × (5 ∗ 2 + 80)   the example    suppression
                                                                                                   of YOLO network           (NMS).
                                                                                                                                  with              By defining a threshold v
                                                                                                                                        (3)each cell bounding box prediction
                                                                                            7   ×     7   ×   (5     ∗  2   +    80)
               NMS, all overlapping
      The fundamental motive of YOLO
                                              set to 2 andpredicted
                                                       and
                                                                  evaluating the bounding
                                                               object
                                                                                          benchmark COCO            boxes dataset  with consisting an IoU              lower
                                                                                                                                                            of 80 classes,      thethan
                                                                                                                                                                                    parameter the defin
                                              output       would       bedetection
                                                                           given as in         general is
                                                                                          expressed         inthe(3):object detec-
               value
tion and localization       are
                The fundamental    eliminated.
                            via bounding        boxes.     Therefore,
                                                      motive             oftwo YOLOsets of boundingand object     box vectors          are
                                                                                                                               detection                  in general is the object d
required, i.e., vector y is the representative of ground truth and vector7 ×                                 𝑦̇ 7is×the     ∗ 2 + 80)
                                                                                                                       (5 predicted                                                            (3)
vector.tion              The
               and localization
          To address
                                  originalvia
                          multiple bounding
                                                     YOLO   bounding
                                                         boxes
                                                                       based on
                                                                    containingboxes.
                                                                                                the or    Darknet
                                                                                        no objectTherefore,    the same object,
                                                                                                                                framework
                                                                                                                                   two sets ofconsisted            boundingofbox             two      sub-
                                                                                                                                                                                                  vector
          opts The
YOLOrequired,           first
                          i.e.,architecture
                for non-maximum    vector   suppression
                                                  y   is    thecomprised
                                                      The fundamental
                                                                 (NMS).        Bymotive
                                                                      representative       ofof24
                                                                                    defining         YOLO convolutional
                                                                                                               and object
                                                                                                      a threshold
                                                                                                           of     ground    valuedetection
                                                                                                                                       for
                                                                                                                                        truth   layers
                                                                                                                                                    in general
                                                                                                                                                        and        with
                                                                                                                                                                    vector     the𝑦̇ final
                                                                                                                                                                      is the object   detection
                                                                                                                                                                                        is the   layer
                                                                                                                                                                                                     predp
NMS, all overlapping predicted bounding       and localization
                                                            boxes with     viaanbounding
                                                                                  IoU lowerboxes.     than the    Therefore,
                                                                                                                     defined NMS    two sets of bounding box vectors are
valuevector.
               a connection
        are eliminated.To address         into       the first
                                                 multiple
                                              required,                  of the
                                                                        bounding
                                                               i.e., vector     y is the two         fully connected
                                                                                                     boxes
                                                                                               representative        containing
                                                                                                                         of ground truth       layers.no           Whereas
                                                                                                                                                                object
                                                                                                                                                        and vector
                                                                                                                                                                           .
                                                                                                                                                                           y isor     the ‘Fast
                                                                                                                                                                                     the
                                                                                                                                                                                 the predictedsameYO    ob
      The
       YOLO    iantopts
            original    consisted
                       YOLO              onof  theonly
                                              vector.
                                 basednon-maximum
                                for                       To
                                                     Darknet    nine
                                                                address
                                                                   frameworkconvolutional
                                                                             multiple       bounding
                                                                                        consisted of two
                                                                               suppression                       layers
                                                                                                             boxes      containing
                                                                                                                     sub-variants.
                                                                                                                  (NMS).          hosting    no   object
                                                                                                                                        By defining      fewer filters
                                                                                                                                                               or  the   same         each. Inspir
                                                                                                                                                                                 object,
                                                                                                                                                                           a threshold    YOLO
                                                                                                                                                                                                     valu
The first architecture comprised ofopts               for non-maximum
                                                24 convolutional             layerssuppression
                                                                                        with the final(NMS).                By defining a threshold value for NMS, all
                                                                                                                 layer providing
       NMS,into
a connection
               inception            module
                    alltheoverlapping
                            first of the two  overlapping
                                                  fully
                                                         in
                                                     predicted  GoogleNet,
                                                          connected predicted bounding
                                                                            layers. bounding    a
                                                                                        Whereas boxes
                                                                                                     sequence
                                                                                                          boxes
                                                                                                         the  ‘Fastwith  with  of
                                                                                                                            an IoU
                                                                                                                        YOLO’       var-
                                                                                                                                        1
                                                                                                                                       an    ×
                                                                                                                                           lower   1
                                                                                                                                               IoUthan    convolutional
                                                                                                                                                            lower          thanNMS
                                                                                                                                                                 the defined               layers
                                                                                                                                                                                     thevaluedefined   waN
iant consisted
       value   mented
                  of
                   areonly      for
                             nine       reducing
                                              are eliminated.
                                   convolutional
                          eliminated.                          thehosting
                                                          layers        resultantfewer filters   feature             spacebyfrom
                                                                                                        each. Inspired                 the             the preceding layers. The
inception module in GoogleNet, a sequence             The original of 1 ×YOLO           based on the
                                                                              1 convolutional                  Darknet
                                                                                                           layers       wasframework
                                                                                                                                imple-                consisted of two sub-variants.
               nary
mented for reducing
                          architecture
                The originalthe resultant  YOLO
                                              The    for
                                                feature
                                                              YOLO-v1
                                                     first based
                                                              architecture
                                                             space     from onthe   the is presented
                                                                                 comprised     Darknet
                                                                                       preceding      of layers.         in Figure
                                                                                                                     framework
                                                                                                          24 convolutional
                                                                                                                      The prelimi-       layers3.      consisted
                                                                                                                                                      with      the final layer of two
                                                                                                                                                                                    providing sub-vari
                         To    address        a   connection
                                                  the       issue     into   the   first
                                                                         of 3.multiple      of   the    two     fully
                                                                                                        bounding boxes    connected           layers.         Whereas
                                                                                                                                                      for thethe             the  ‘Fast
                                                                                                                                                                        same object      YOLO’
nary architecture
       The firstforarchitecture
                            YOLO-v1       is presented
                                                    comprised
                                              variant
                                                               in Figure
                                                            consisted of of     only   24nine  convolutional
                                                                                                    convolutional layers           layershostingwith     fewer filters final            layerorprovi
                                                                                                                                                                               each. Inspired
                                                                                                                                                                                                      with
      To address the issue of multiple bounding boxes for the same object or with a confi-
denceascore
               dence
          connection        score
               of zero, i.e., nointo
                                        ofthe
                                   object,
                                             zero,  the i.e.,
                                              by first
                                             the authors       of
                                                           inceptionnotheobject,
                                                                 decided      two
                                                                            module
                                                                              to greatly
                                                                                           inthe
                                                                                         fully         authors
                                                                                                       connected
                                                                                                GoogleNet,
                                                                                                penalize
                                                                                                                            decided
                                                                                                               predictionslayers.
                                                                                                                     a sequence
                                                                                                                                  from
                                                                                                                                            of 1to       1greatly
                                                                                                                                                     ×Whereasconvolutional   penalize
                                                                                                                                                                               thelayers
                                                                                                                                                                                     ‘Fastwas  predicti
                                                                                                                                                                                                YOLO’
                                              implemented for reducing the resultant feature space from the preceding layers. The
bounding       bounding
              boxes   containing
       iant consisted of only       boxes
                                     objects    (𝛾 containing
                                                   𝑐𝑜𝑜𝑟𝑑
                                              preliminary
                                                            =   5)  and
                                                     nine convolutional    theobjects
                                                                                lowest
                                                                   architecture for YOLO-v1
                                                                                                  (𝛾
                                                                                              penalization
                                                                                                      layers
                                                                                                       𝑐𝑜𝑜𝑟𝑑        =
                                                                                                                    for   5)    and
                                                                                                                          prediction
                                                                                                                       hosting
                                                                                                               is presented
                                                                                                                                             the
                                                                                                                                             fewer
                                                                                                                                     in Figure
                                                                                                                                                        lowest            penalization
                                                                                                                                                        3. filters each. Inspired b
                                                                                                                                                                                                     for p
containing no object (𝛾𝑛𝑜𝑜𝑏𝑗 = 0.5). The authors calculated the loss function by taking the
               containing
       inception                      no object               (𝛾𝑛𝑜𝑜𝑏𝑗    the =     a0.5).         The        authors              calculated
                                                                                                                            1 boxes
                                                                                                                                ×prob- 1 for                      the     loss     function           byim
                                                                                                                                                                                                         ta
          all bounding module                 in (x,GoogleNet,                           sequence                   ofclass                   convolutional                        layers        was
                                                      To address               issue     of   multiple        bounding                             the same         object    or with    a confi-
sum of                      box parameters              y, width,      height, confidence              score, and
                                              dence score of zero, i.e., no object, the authors decided to greatly penalize predictions from
ability).  As asum
       mented    result, of
                        fortheall
                                firstbounding
                               reducingpart of the  the       box
                                                              resultant
                                                        equation        parameters
                                                                        computes         the loss(x,
                                                                                     feature            ofspace
                                                                                                            they,bounding
                                                                                                                     width,frombox    height,
                                                                                                                                          the preceding   confidence                score,The
                                                                                                                                                                                layers.           andprecl
                                              bounding          boxes containing             objects (γ      coord = 5) and the lowest penalization for prediction
prediction with respect to the ground truth bounding box based on the coordinates
               ability). As a for          result,
                                              containing    thenofirst objectis part
                                                                                 (γnoobj of          the The
                                                                                               = 0.5).        equation
                                                                                                                     authors calculated computes          the loss   the      lossbyoftaking
                                                                                                                                                                        function            the boun
𝑥𝑐𝑒𝑛𝑡𝑒𝑟nary
        , 𝑦𝑐𝑒𝑛𝑡𝑒𝑟architecture                      YOLO-v1                       presented       within in          Figure             3.
                         𝑜𝑏𝑗
                  . 𝕝 is set as 1 in the      the  case
                                                     sum    ofofthe
                                                                  all  object
                                                                       bounding residing box     parameters
                                                                                                               𝑡ℎ
                                                                                                             𝑗 bounding
                                                                                                                      (x,  y,   width,box   height,       confidence         score,  and
                                                                                                                                                                                         onclass
                         𝑖𝑗
prediction in  prediction
                To𝑖 𝑡ℎ address
                       cell; otherwise,with      is respect
                                        theitprobability).
                                                 issue
                                                    set as of  0. The
                                                                   As
                                                                        to
                                                                      multiple the ground
                                                                        aselected,
                                                                           result, thei.e., bounding
                                                                                             firstpredicted
                                                                                                     part of the
                                                                                                                 truth  boxes
                                                                                                                    bounding
                                                                                                                       equation
                                                                                                                                bounding
                                                                                                                                      boxfor thethesame
                                                                                                                                       computes
                                                                                                                                                                box        based
                                                                                                                                                                           object
                                                                                                                                                                 loss of the    boundingor      the acoo
                                                                                                                                                                                              with
                                                                                                                                                                                              box        c
would be tasked with predicting an                 𝑜𝑏𝑗 with the greatest IoU, as expressed in (4):
                                                  object
       dence   𝑥𝑐𝑒𝑛𝑡𝑒𝑟
                    score, of  𝑦𝑐𝑒𝑛𝑡𝑒𝑟
                                    zero,. i.e., 𝕝𝑖𝑗 no
                                              prediction   is
                                                           obj
                                                                 set as 1the
                                                                 with
                                                                 object,respect      in authors
                                                                                     to   thethe casedecided
                                                                                                 ground       truth of the object
                                                                                                                        bounding           box
                                                                                                                                       to greatly based residing
                                                                                                                                                               on   the       within
                                                                                                                                                                          coordinates
                                                                                                                                                                   penalize               x    𝑡ℎ
                                                                                                                                                                                             𝑗 boun
                                                                                                                                                                                     predictions
                                                                                                                                                                                            center ,
                                                    2
                                              ycenter      𝑜𝑏𝑗 is set as 21 in the case
                                                   ∑𝐵𝑗=0. 𝕝ij                                   2 of the object residing within j th bounding box prediction in
                                   𝛾𝑐𝑜𝑜𝑟𝑑 ∑𝑆𝑖=0
                                              𝑡ℎ                [(𝑥   −  𝑥
                                                                         ̂  )  +  (𝑦    −   𝑦
                                                                                            ̂)    ]                                     (4)
       boundingprediction                   𝑖 th cell;
                            boxesincontaining              𝑖𝑗 otherwise,
                                                                   objects
                                                                    𝑖     𝑖
                                                                                      (𝛾𝑐𝑜𝑜𝑟𝑑
                                                                                      𝑖
                                                                                             it
                                                                                             𝑖
                                                                                                    is set
                                                                                                         = 5)asand       0. The  the lowest selected,                i.e., predicted
                                                                                                                                                                penalization               for predi boun
                                              i cell; otherwise, it is set as                 0. The selected, i.e., predicted bounding box would be tasked
      The next    component
               would          beoftasked
                                      the loss function
                                                    with         computes the prediction
                                                                 predicting                 anthe    objecterror in widththe         and greatest IoU, as expressed in
       containing             no    object    with (𝛾 predicting     =an0.5). objectThe  with           greatestwith
                                                                                                   authors              calculated
                                                                                                                       IoU,    as expressed           the
                                                                                                                                                        in (4): loss function by takin
height of the bounding box, similar to 𝑛𝑜𝑜𝑏𝑗           the preceding component. However, the scale of
error sum       of all
       in the large    boxesbounding
                               has lesser impact   boxcomparedparameters   to the small     (x,  2S y, 𝐵
                                                                                               𝑆boxes.
                                                                                                   2      width,
                                                                                                           The obj
                                                                                                           B
                                                                                                                       h height, confidence
                                                                                                                    normalization
                                                                                                                   𝑜𝑏𝑗
                                                                                                                                                                 i          score, and(4)class p
of width and height between the range 0 and 1 indicates                     𝛾 𝑐𝑜𝑜𝑟𝑑γ coord ∑ ∑
                                                                                     that their𝑖=0    ∑ ∑ 𝑗=0
                                                                                                           j=0 ij
                                                                                                  i =0 square     𝕝𝑖𝑗
                                                                                                                         ([x(i 𝑥
                                                                                                                               −𝑖
                                                                                                                    roots increase −
                                                                                                                                  x̂ i ) 2
                                                                                                                                          𝑥̂+𝑖 )(2y − ŷ( )2
                                                                                                                                                    i +      𝑦
                                                                                                                                                             i  𝑖 −𝑦    ̂𝑖 )2 ]
       ability). As a result, the first part of the equation computes the loss of the bounding
                                                      The next component of the loss function computes the prediction error in width and
       prediction        The  withnextrespect
                                            component         to the
                                              height of the bounding     of ground
                                                                               thebox,   loss         truth
                                                                                                      function
                                                                                                similar
                                                                                                                     bounding
                                                                                                            to the preceding computes              box
                                                                                                                                            component.    thebased  prediction   on the
                                                                                                                                                                    However, the scale    error coordin
                                                                                                                                                                                                of in w
                                         𝑜𝑏𝑗
       𝑥𝑐𝑒𝑛𝑡𝑒𝑟      , 𝑦𝑐𝑒𝑛𝑡𝑒𝑟
               height              . 𝕝𝑖𝑗bounding
                              of the             is set
                                              error    in theas       box,
                                                                  large1 inboxes similar
                                                                                 thehas caselesserto     ofthe
                                                                                                       impact  the     preceding
                                                                                                                          objectto residing
                                                                                                                    compared                the small component.
                                                                                                                                                               boxes.within         𝑗𝑡ℎ bounding
                                                                                                                                                                                    However,
                                                                                                                                                                         The normalization             the
                                     𝑡ℎ       of   width      and     height    between          the    range      0 and     1  indicates          that     their    square     roots  increase
               error ininthe
       prediction                  𝑖 large    the boxes
                                           cell;      otherwise,
                                                     differences   has  for lesser
                                                                                 it is values
                                                                              smaller         impact
                                                                                              set asto 0.     a compared
                                                                                                                    Thedegree
                                                                                                                  higher        selected,     to the
                                                                                                                                            compared       i.e.,smallpredicted
                                                                                                                                                                 to that      boxes.
                                                                                                                                                                             of            The
                                                                                                                                                                                           bounding
                                                                                                                                                                                larger values,       norm
       would   of width
                      be tasked   andwith   height            between
                                                      predicting
                                              expressed         as (5):         an theobject  rangewith       0 and     the1greatest
                                                                                                                                  indicates              IoU,  thatastheir           squareinroots
                                                                                                                                                                             expressed                (4):
                                                                                                           "                                q 2 #
                                                                                                               √        p 2
                                                                                                                                    p
                                                                                 𝑆 2S2         𝐵B   𝑜𝑏𝑗
                                                                     𝛾   γ coord
                                                                       𝑐𝑜𝑜𝑟𝑑 𝑖=0  ∑∑ ∑∑
                                                                                    i =0       𝑗=0
                                                                                                    obj
                                                                                                j=0 ij
                                                                                                    𝑖𝑗 𝕝       [(𝑥w𝑖 i −
                                                                                                                       −𝑥̂𝑖ŵ)i2 ++(𝑦𝑖 −  𝑦̂𝑖 )2ĥ]i
                                                                                                                                       hi −                                           (5)

             The next component   Next,ofthethe
                                             loss loss
                                                  of the function     computes
                                                         confidence score   is computedthe   prediction
                                                                                          based              error
                                                                                                 on whether the       inis width
                                                                                                                  object
                             present or absent with respect to the bounding box. Penalization of the object confidence
        height of the bounding
                             error is box,   similar
                                      only executed      toloss
                                                    by the   the   preceding
                                                                function             component.
                                                                         if that predictor             However,
                                                                                           was responsible for the groundthe sca
        error in the large boxes has lesser impact compared to the small boxes. The normaliza
        of width and height between the range 0 and 1 indicates that their square roots incr
                                                  nary architecture for YOLO-v1                                                       is presented               2           in Figure               3.
ontaining
m ofability).
                  no As object
                           a   result, (𝛾
                                        containing
                                          𝑛𝑜𝑜𝑏𝑗
                                           the      = part
                                                 first    0.5). noy,ofThe
                                                                        object
                                                                           the        authors
                                                                                            𝛾(𝛾
                                                                                       equation
                                                                                                         ∑𝑆𝑖=0calculated
                                                                                                     𝑛𝑜𝑜𝑏𝑗              =𝕝𝑜𝑏𝑗
                                                                                                                        2
                                                                                                                    ∑𝐵𝑗=0
                                                                                                                    computes   0.5). [(√𝑤The   𝑖 − the
                                                                                                                                                 the   √𝑤  ̂) 𝑖authors
                                                                                                                                                             loss  loss
                                                                                                                                                                     + (√ℎ𝑖function
                                                                                                                                                                            of       − √calculated
                                                                                                                                                                                   the      ℎ̂𝑖 ) ]
                                                                                                                                                                                              bounding      by taking    the loss  (5)thefunc
                                                                                                                                                                                                               thebox
                                                                                                𝑐𝑜𝑜𝑟𝑑
        all bounding             box    parameters
                      To address the issue                   (x,
                                                            To address   width,
                                                                   of multiple              height,
                                                                                         the issue               confidence
                                                                                                          bounding
                                                                                                                               𝑖𝑗
                                                                                                                      of multiple                score,
                                                                                                                                             boxes      bounding      and
                                                                                                                                                                   for theboxes    class    same prob-forobject          sameor with  objectaorc
um    of
 lity).   Asalla bounding
        predictionresult, with         box
                                        sum
                               the respect
                                      first    parameters
                                             partoftoofall
                                                         the
                                                           thebounding
                                                                  ground
                                                                   equation (x,        y,truth  box
                                                                                                 width,
                                                                                                computes    parameters
                                                                                                           bounding   height, the           confidence
                                                                                                                                           box
                                                                                                                                        loss           (x,
                                                                                                                                                       of based
                                                                                                                                                              they,        width,
                                                                                                                                                                              on
                                                                                                                                                                           bounding score,
                                                                                                                                                                                         the  height, and
                                                                                                                                                                                                   coordinates
                                                                                                                                                                                                     box         confidence
                                                                                                                                                                                                                   class         prob-      scor
             dence score 𝑜𝑏𝑗          of zero,dence i.e.,
                                                        Next,  score
                                                              no   the      of zero,
                                                                      object,
                                                                          loss        of thethei.e.,          no object,
                                                                                                         authors
                                                                                                     confidence                     decided
                                                                                                                                score       the
                                                                                                                                            is computedauthors   to greatly    decided
                                                                                                                                                                             based                   to greatly
                                                                                                                                                                                                 penalize
                                                                                                                                                                                          on whether                        penalize
                                                                                                                                                                                                                          predictions
                                                                                                                                                                                                                  the object         is      pre
bility).
ediction     As
        𝑥𝑐𝑒𝑛𝑡𝑒𝑟  , a𝑦𝑐𝑒𝑛𝑡𝑒𝑟
               with   result,
                        respect  . 𝕝𝑖𝑗the
                                        ability).
                                       to    first
                                          isthe       part
                                                        As
                                                   ground
                                              setpresent
                                                    as
                                                  bounding1   in aof result,
                                                                     truth
                                                                    the
                                                              or absent   the
                                                                        boxes case     equation
                                                                                            the
                                                                                       bounding
                                                                                            of
                                                                                 withcontaining      the  firstobject
                                                                                            respect to theobjects       computes
                                                                                                                        boxpart          of
                                                                                                                                     based
                                                                                                                                   residing
                                                                                                                              bounding(𝛾box.      the    onthe
                                                                                                                                                       𝑐𝑜𝑜𝑟𝑑
                                                                                                                                                                equation
                                                                                                                                                              withinthe   loss          of
                                                                                                                                                                                       𝑡ℎ
                                                                                                                                                                                coordinates
                                                                                                                                                                       = 5) andofthe
                                                                                                                                                                Penalization         𝑗          the
                                                                                                                                                                                                computes
                                                                                                                                                                                             bounding     bounding
                                                                                                                                                                                                         lowest
                                                                                                                                                                                                 the object            box  the
                                                                                                                                                                                                                          penalization
                                                                                                                                                                                                                    confidence        box
                                                                                                                                                                                                                                      loss    of f
             bounding  𝑜𝑏𝑗         boxes
                                  𝑡ℎ          containing                 objects                   (𝛾   𝑐𝑜𝑜𝑟𝑑               =     5)      and              the         lowest                  penalization                      for     predi
rediction
 𝑛𝑡𝑒𝑟 , prediction
         𝑦𝑐𝑒𝑛𝑡𝑒𝑟      𝕝𝑖𝑗in11,isrespect
                   with
                   . 2023,
            Machines            𝑖 setcell;
                                677              error
                                        prediction
                                               to    the
                                        as 1otherwise,
                                                in   the  is case
                                                  containing only   itexecuted
                                                               ground
                                                                 with    is
                                                                        ofnothe  respect
                                                                                 setobjectby
                                                                                         truth
                                                                                          as
                                                                                           object
                                                                                          𝑜𝑏𝑗
                                                                                                  the
                                                                                                   0.(𝛾   loss
                                                                                                            to
                                                                                                          The       function
                                                                                                             bounding
                                                                                                             residing
                                                                                                            𝑛𝑜𝑜𝑏𝑗       the
                                                                                                                        selected,
                                                                                                                             = 0.5).   ifwithin
                                                                                                                                           thati.e.,
                                                                                                                                      ground      box
                                                                                                                                                The    predictor𝑗𝑡ℎtruth
                                                                                                                                                                    based
                                                                                                                                                                predicted
                                                                                                                                                               authors        was responsible
                                                                                                                                                                           bounding     bounding
                                                                                                                                                                                           on        boxforcoordinates
                                                                                                                                                                                                     the
                                                                                                                                                                                              bounding
                                                                                                                                                                                        calculated                  the
                                                                                                                                                                                                                  the  box
                                                                                                                                                                                                                       box ground
                                                                                                                                                                                                                          loss     based
                                                                                                                                                                                                                                6 offunction
                                                                                                                                                                                                                                      25       o
        wouldcontaining
                    𝑡ℎ
              in 𝑖be tasked   𝑜𝑏𝑗   no    object truth
                                     with predicting   (𝛾 bounding
                                                            𝑛𝑜𝑜𝑏𝑗  an     =  box.
                                                                           object 0.5).
                                                                                 𝑜𝑏𝑗     𝕝         The
                                                                                                withis   set
                                                                                                            the toauthors
                                                                                                                       1    when
                                                                                                                         greatest       the  calculated
                                                                                                                                                 object
                                                                                                                                                IoU,    (x, as
                                                                                                                                                                 is   present
                                                                                                                                                                          expressedthe   in    loss
                                                                                                                                                                                              the   cell; function
                                                                                                                                                                                                             otherwise,         it byis  takin
ediction                 cell; otherwise,
 𝑒𝑛𝑡𝑒𝑟 , 𝑦𝑐𝑒𝑛𝑡𝑒𝑟 . 𝕝𝑖𝑗 is𝑥set
                                                     it𝑦isinofset     as      0. The
                                                                             𝕝noobj                selected,              1 i.e.,        predicted                         bounding              𝑗𝑡ℎin
                                                                                                                                                                                                     box   (4):
                                                                                          𝑖𝑗
                                                  sum             all   .bounding                      box           parameters                                  y, of    width,          height,          confidence
                                                                                                                                                                                                              residing score,                  an
                                         𝑐𝑒𝑛𝑡𝑒𝑟  set, 1
                                                as    as 𝑐𝑒𝑛𝑡𝑒𝑟  the
                                                           0, whilst       𝕝case 𝑖𝑗 works  isof     setthe     asobject
                                                                                                          in the                in the
                                                                                                                         opposite        residing
                                                                                                                                            way,case     as shown          within
                                                                                                                                                                                the
                                                                                                                                                                               in     (6): object         bounding                    box
                                                                                                                                                                                                                                       within
             sum ofwith
 uld be tasked             all     bounding
                                   predicting        anbox
                                                  ability).object parameters
                                                                         with
                                                                   As𝑖is𝑡ℎ
                                                                              ij
                                                                           a∑box.result, the             (x,
                                                                                                    greatest
                                                                                                      the            y,      width,
                                                                                                                              IoU,
                                                                                                                 first)selected,
                                                                                                                             2part
                                                                                                                                           as    height,
                                                                                                                                                  expressed                confidence
                                                                                                                                                                                   in     (4):              score,           and        of the bp
                                                                                                                                                                                                                                        class
rediction in 𝑖 𝑡ℎ cell;prediction        otherwise,   𝛾𝑐𝑜𝑜𝑟𝑑
                                                   truth        init
                                                                  ∑𝑆𝑖=0
                                                            bounding
                                                                       2
                                                                               set
                                                                                 𝐵cell;
                                                                                 𝑗=0 𝕝ij
                                                                                           as
                                                                                            𝑜𝑏𝑗otherwise,
                                                                                            obj
                                                                                                   is0.
                                                                                            𝑖𝑗 [(𝑥𝑖 − 𝑥
                                                                                                        setTheto 1̂𝑖when         + (𝑦 theit𝑖of− isthe
                                                                                                                                              object 𝑦̂) set
                                                                                                                                                        𝑖 is
                                                                                                                                                            2 equation
                                                                                                                                                            i.e.,    aspredicted
                                                                                                                                                               ] present      0. inThe       computes
                                                                                                                                                                                          the cell;selected,
                                                                                                                                                                                                          bounding
                                                                                                                                                                                                          otherwise,
                                                                                                                                                                                                                     the i.e.,
                                                                                                                                                                                                                             lossbox
                                                                                                                                                                                                                         (4)it is set   predic
             ability). As a result,                   the
                                                  prediction
                                                        2       firstnoobj  part
                                                                          with
                                                                        𝑜𝑏𝑗                  of
                                                                                           respect    the equation   to       theway,    ground   computes         truth                the2 loss of
                                                                                                                                                                                     bounding                  box     the basedbounding on the
 ould be tasked withwould                predicting
                                         𝛾𝑐𝑜𝑜𝑟𝑑 as ∑be𝑆0,
                                                            ∑tasked
                                                               𝐵
                                                           whilstan
                                                      𝑖=0 𝑗=0 𝑖𝑗i=0   𝕝∑
                                                                       ijobject
                                                                          S with
                                                                               [(𝑥∑   B
                                                                                  works𝑖
                                                                                      j=0 − 𝕝
                                                                                           𝑜𝑏𝑗 ij
                                                                                                 with
                                                                                                    predicting
                                                                                               objin 2
                                                                                               2
                                                                                                  𝑥
                                                                                                  ̂ (c
                                                                                                    𝑖 ) the
                                                                                                        i  −+  c the
                                                                                                                  (𝑦  2 −greatest
                                                                                                                opposite
                                                                                                               ̂) i     𝑖 +   γ  𝑦
                                                                                                                                 ̂)𝑖
                                                                                                                                 noobj
                                                                                                                                       2an
                                                                                                                                         ] ∑  Sas
                                                                                                                                              i=0object
                                                                                                                                                   2      BIoU,
                                                                                                                                                       shown
                                                                                                                                                       ∑  j=0    𝕝
                                                                                                                                                                  noobj
                                                                                                                                                                  ij
                                                                                                                                                                           with
                                                                                                                                                                          in as
                                                                                                                                                                              (6):
                                                                                                                                                                             (x  i  −expressed
                                                                                                                                                                                         xthe
                                                                                                                                                                                          ̂i )   +  greatest
                                                                                                                                                                                                    (c (4)
                                                                                                                                                                                                        i −   c
                                                                                                                                                                                                              ̂)i  in
                                                                                                                                                                                                                   2      (4):
                                                                                                                                                                                                                            IoU,   (6) as exp
             prediction
               The next component    with respect 𝑥of    the, loss
                                                    𝑐𝑒𝑛𝑡𝑒𝑟        to
                                                                  𝑦𝑐𝑒𝑛𝑡𝑒𝑟 the
                                                                            function. 𝕝ground
                                                                                           𝑖𝑗        iscomputes
                                                                                                           set as     truth    1 in  the  bounding
                                                                                                                                           the prediction
                                                                                                                                                        case of the             box
                                                                                                                                                                                error     objectbased
                                                                                                                                                                                                in width residing on   and  the
                                                                                                                                                                                                                              within   coordi
                                                                                                                                                                                                                                            𝑗𝑡ℎ b
                                              𝑜𝑏𝑗                  𝑆 2S in        𝑖Bj=𝑡ℎ                                                     2S
                                                                                           2                                                       2
        height     of the                                                                    𝑜𝑏𝑗                                                                       𝑜𝑏𝑗
                         , 𝑦bounding             box,is similar             1to
                                                                              ∑𝐵𝑗=0   the         preceding                      component.
                                                                                                                                  2 ∑𝑆it                  𝐵error
                                                                                                                                                                    𝕝)However,                   2 the 2 scale            of predicted
                                                                                                                                                             B
    The    next    component
             𝑥𝑐𝑒𝑛𝑡𝑒𝑟                    of the    prediction
                                𝑐𝑒𝑛𝑡𝑒𝑟 . 𝕝𝑖𝑗 𝛾𝑐𝑜𝑜𝑟𝑑
                                                  loss     set  ∑∑
                                                            functionasi=0∑
                                                                   𝑖=0
                                                                                  computes
                                                                                  in   0 𝕝the
                                                                                             cell;
                                                                                             obj
                                                                                             ij𝑖𝑗 (c[i (
                                                                                                           otherwise,
                                                                                                          −𝑥
                                                                                                         casec𝑖ˆthe 𝛾2𝑐𝑜𝑜𝑟𝑑
                                                                                                                 i )−    +𝑥of 𝑖 )noobj
                                                                                                                              γ    the+∑
                                                                                                                            ̂prediction   𝑖=0  𝑦=is0𝑖∑∑
                                                                                                                                             (iobject   − set
                                                                                                                                                          𝑗=0j=𝑦̂0𝑖as  2 0.
                                                                                                                                                                       noobj
                                                                                                                                                                            ]in[((xThe
                                                                                                                                                                       residing
                                                                                                                                                                       ij𝑖𝑗
                                                                                                                                                                                     width
                                                                                                                                                                                     𝑥i −𝑖 − x̂iselected,
                                                                                                                                                                                                )𝑥   and
                                                                                                                                                                                                    𝑖 ) (ci+
                                                                                                                                                                                                  ̂within
                                                                                                                                                                                                   +         − (cˆ𝑦 i )i.e.,
                                                                                                                                                                                                                        2 𝑡ℎ
                                                                                                                                                                                                                        𝑖𝑗− 𝑦
                                                                                                                                                                                                                                      2
                                                                                                                                                                                                                                 𝑖 )(6)](4)
                                                                                                                                                                                                                               ̂bounding        b
 ght error
        of the  inbounding
                     the large boxes
             prediction             inbox,      has
                                                  would
                                         𝑖 𝑡ℎsimilar
                                                cell;  lesser    be
                                                            tolast  impact
                                                                  the
                                                           otherwise,  tasked
                                                                           preceding     compared
                                                                                            with
                                                                                            it ofisofthepredicting
                                                                                                            component.
                                                                                                           set          asto     the small
                                                                                                                                 0.        ansimilar
                                                                                                                                         The         object
                                                                                                                                                However,     boxes.
                                                                                                                                                         selected,        with  The
                                                                                                                                                                                the     the   normalization
                                                                                                                                                                                                 greatest
                                                                                                                                                                                             scale       of IoU,                as    expresse
                                                        TheThe    lastcomponent
                                                                          component                         thelossloss    function,
                                                                                                                                 function,              similar  to the         the i.e.,
                                                                                                                                                                            to normal     normal    predicted
                                                                                                                                                                                                classification
                                                                                                                                                                                                         classification  loss, bounding
                                                                                                                                                                                                                                 cal-
                                                                                                                                                                                                                                  loss,
 or in  ofthe
      The   width
               largeand
              next     component
                        boxes   height      between
                                     has lesser of
                                                 The thenext
                                                     impact
                                                 culates    theloss
                                                             the     range
                                                                       component
                                                                          function
                                                                     compared
                                                                   class               0 andto1computes
                                                                              (c) probability                indicates
                                                                                                           the ofloss,   the
                                                                                                                       small except  loss that
                                                                                                                                            the
                                                                                                                                        boxes.
                                                                                                                                           for    the
                                                                                                                                             𝑆 2 for
                                                                                                                                                         their
                                                                                                                                                  function
                                                                                                                                                         prediction
                                                                                                                                                            The 𝑜𝑏𝑗
                                                                                                                                                              𝕝𝑖𝑗 obj 𝑜𝑏𝑗  square  computes
                                                                                                                                                                           normalization
                                                                                                                                                                          part,      expressedroots
                                                                                                                                                                                              errorinincreasein
                                                                                                                                                                                                             (7):thewidth  prediction and e
             would be tasked with                          predicting
                                                   calculates      the class (c)an                    object
                                                                                               probability                   with
                                                                                                                          𝛾𝑐𝑜𝑜𝑟𝑑
                                                                                                                         loss,     except∑the𝑖=0 ∑greatest
                                                                                                                                                           𝐵
                                                                                                                                                           𝑗=0 𝕝ij
                                                                                                                                                           the
                                                                                                                                                                      𝑖𝑗      [(𝑥𝑖 IoU,
                                                                                                                                                                             part,       − 𝑥̂𝑖 )2as
                                                                                                                                                                                         expressed    + (𝑦   expressed
                                                                                                                                                                                                            in     − 𝑦̂)
                                                                                                                                                                                                                𝑖(7):     𝑖 ]
                                                                                                                                                                                                                             2          in (4):
width of
eight      andthe height
                       bounding between height the range
                                             box,     of     the0 bounding
                                                       similar         and to 1the       indicates        box,that
                                                                                                   preceding                similar their
                                                                                                                                       component. square
                                                                                                                                                     to the roots            preceding
                                                                                                                                                                                  However, increasecomponent.    the scale ofHow
                                                                                                𝑆2          𝐵𝑆S of         𝑜𝑏𝑗 loss function
                                                                                                                            2
                                                                                                                            2
 ror in the large boxes                 error
                                            has in lesser
                                                        the The      next
                                                                 large
                                                                  impact
                                                                      𝛾𝑐𝑜𝑜𝑟𝑑      component
                                                                                  boxes  ∑
                                                                                         compared
                                                                                                𝑖=0 has ∑∑  ∑
                                                                                                            𝑗=0i =0lesser
                                                                                                               𝑖=0
                                                                                                                          obj
                                                                                                                         𝑜𝑏𝑗
                                                                                                                               ∑
                                                                                                                       𝕝𝕝𝑖𝑗ij the
                                                                                                                           𝑖𝑗 to    c(∈
                                                                                                                                      theimpact
                                                                                                                                          .𝑖 −small
                                                                                                                                ∑[𝑐∈𝑐𝑙𝑎𝑠𝑠𝑒𝑠
                                                                                                                                       𝑥classes   (𝑝  (𝑥    (c2)−
                                                                                                                                                           i)
                                                                                                                                                       ̂p𝑖𝑖(𝑐)            ̂
                                                                                                                                                                   compared
                                                                                                                                                                   +𝑝boxes.
                                                                                                                                                                   −          𝑦computes
                                                                                                                                                                           𝑖((𝑐)𝑖)− 𝑦
                                                                                                                                                                                     2
                                                                                                                                                                                                )2 ]tonormalization
                                                                                                                                                                                            ̂𝑖The          the
                                                                                                                                                                                                            theprediction
                                                                                                                                                                                                                       small(7)(7)        errorT
                                                                                                                                                                                                                                      boxes.
                                                                                                                                               .

  width and height between              of width  height the
                                                           and   ofrange
                                                                       the bounding
                                                                      height           0 and    between     1 box, indicates  thesimilar range    that to the   0theirand   preceding square
                                                                                                                                                                                      1layers)
                                                                                                                                                                                            indicates  component.
                                                                                                                                                                                                          roots        that
                                                                                                                                                                                                                          increase   Howeve
                                                                                                                                                                                                                                  their      squ
                      The next component                   Performance
                                                  error in the      of the largeloss  wise, boxes  the     simple
                                                                                                       function
                                                                                                              has lesser     YOLO          (24
                                                                                                                                      computes    convolutional
                                                                                                                                            impact compared                the prediction           when
                                                                                                                                                                                                 to the small  trained
                                                                                                                                                                                                                     error    on
                                                                                                                                                                                                                             boxes. the
                                                                                                                                                                                                                                    in width
                                                                                                                                                                                                                                          The n
                                                   PASCAL VOC dataset (2007 and 2012) [39,40] achieved a mean average precision (referring
             height of the bounding               of   width    box,
                                                        Performance
                                                   to cross-class    and          height
                                                                              similar
                                                                                  wise,
                                                                          performance)           the between
                                                                                                        to
                                                                                                        simple
                                                                                                           (mAP)  theYOLO         the(24range
                                                                                                                             ofpreceding
                                                                                                                                  63.4%        atconvolutional
                                                                                                                                                       45 FPS,  0 component.
                                                                                                                                                                      and whilst   1layers)
                                                                                                                                                                                        indicates
                                                                                                                                                                                        Fast      whenHowever,
                                                                                                                                                                                                 YOLO          that their
                                                                                                                                                                                                             trained
                                                                                                                                                                                                             achieved            thesquare
                                                                                                                                                                                                                            on52.7%    the scar
                                                 PASCAL          VOC       dataset           (2007         and       2012)        [39,40]
                                                   mAP at an impressive 155 FPS. Although the performance was better than real-time               achieved                 a  mean         average        precision         (refer-
             error in the large boxes            ring
                                                   detectors,
                                                              has
                                                         to cross-class lesser
                                                                   such as DPM-v5
                                                                                            impact
                                                                                    performance)       [41] (33%
                                                                                                                      compared
                                                                                                                     (mAP)    mAP),  of 63.4%
                                                                                                                                            it was at
                                                                                                                                                           to
                                                                                                                                                            lower45the    FPS, small
                                                                                                                                                                           thanwhilst
                                                                                                                                                                                                  boxes.
                                                                                                                                                                                                 Fast
                                                                                                                                                                                      the state-of-the-artYOLOThe               normaliz
                                                                                                                                                                                                                         achieved
                                                                                                                                                                                                                         (SOTA) at
             of width and height                   thebetween
                                                 52.7%     mAPi.e.,
                                                        time,       at anFaster  theR-CNN
                                                                                impressive   range        155
                                                                                                           (71%     0 mAP).
                                                                                                                   FPS.   and Although  1 indicates  the performance           thatwas         their
                                                                                                                                                                                                   bettersquare
                                                                                                                                                                                                              than real-time    roots inc
                                                                  detectors,
                                                                          Theresuch
                                                                                  were as DPM-v5
                                                                                          some clear  [41]loopholes
                                                                                                             (33% mAP), thatitrequired
                                                                                                                                was lower      than the such
                                                                                                                                            attention,     state-of-the-art    (SOTA)
                                                                                                                                                                  as the architecture
                                                                  athaving
                                                                      the time,  i.e., Faster   R-CNN      (71%   mAP).
                                                                             comparatively low recall and higher localization error compared to Faster R-CNN.
                                                                         There were
                                                                    Additionally,    thesome   clear loopholes
                                                                                          architecture   struggled  that
                                                                                                                       torequired     attention,
                                                                                                                           detect close    proximitysuchobjects
                                                                                                                                                           as the due
                                                                                                                                                                   architecture
                                                                                                                                                                        to the facthav-
                                                                                                                                                                                     that
                                                                  ing   comparatively       low  recall  and     higher   localization     error   compared
                                                                    each grid cell was capped to two bounding box proposals. The loopholes attributed to the     to  Faster   R-CNN.
                                                                  Additionally,
                                                                    original YOLO   theprovided
                                                                                          architecture     struggled
                                                                                                    inspiration     for to
                                                                                                                        thedetect   closevariants
                                                                                                                              following      proximity      objects due to the fact
                                                                                                                                                        of YOLO.
                                                                  that each grid cell was capped to two bounding box proposals. The loopholes attributed
                                                                  to2.2.
                                                                      theYOLO-v2/9000
                                                                          original YOLO provided inspiration for the following variants of YOLO.
                                                                          YOLO-v2/9000 was introduced by Joseph Redmon in 2016 [42]. The motive was
                                                                  2.2.  YOLO-v2/9000
                                                                    to remove     or at least mitigate the inefficiencies observed with the original YOLO while
                                                                    maintaining     the impressive
                                                                         YOLO-v2/9000                    speed factor.
                                                                                             was introduced        by Joseph Several
                                                                                                                                 Redmon enhancements
                                                                                                                                              in 2016 [42].  were
                                                                                                                                                                Theclaimed
                                                                                                                                                                       motive through
                                                                                                                                                                                 was to
                                                                    the implementation
                                                                  remove                      of various
                                                                            or at least mitigate             techniques. observed
                                                                                                     the inefficiencies      Batch normalization         [43] was
                                                                                                                                         with the original      YOLO introduced
                                                                                                                                                                         while main-with
                                                                    the internal
                                                                  taining          architecture
                                                                            the impressive          to improve
                                                                                                speed                modelenhancements
                                                                                                        factor. Several       convergence, leading          to faster
                                                                                                                                                 were claimed           training.
                                                                                                                                                                    through          This
                                                                                                                                                                                the im-
                                                                    introduction of
                                                                  plementation      eliminated     the need forBatch
                                                                                        various techniques.         othernormalization
                                                                                                                            regularization[43]  techniques,     such as with
                                                                                                                                                    was introduced        dropout    [44]
                                                                                                                                                                                 the in-
                                                                    aimedarchitecture
                                                                  ternal    at reducingto    overfitting
                                                                                               improve model[45]. Itsconvergence,
                                                                                                                      effectivenessleading
                                                                                                                                        can be gauged
                                                                                                                                                   to fasterby   the fact This
                                                                                                                                                               training.    that simply
                                                                                                                                                                                  intro-
                                                                    introducing
                                                                  duction          batch normalization
                                                                             eliminated      the need for improved          the mAP by techniques,
                                                                                                               other regularization         2% compared        to the
                                                                                                                                                             such   as original
                                                                                                                                                                        dropoutYOLO.[44]
                                                                  aimed at reducing overfitting [45]. Its effectiveness can be gauged by the factpixels
                                                                          The   original    YOLO     worked       with  an   input   image     size  of  224   ×   224            during
                                                                                                                                                                          that simply
                                                                    the trainingbatch
                                                                  introducing       stage,normalization
                                                                                              whilst for theimproved
                                                                                                                  detection thephase,
                                                                                                                                   mAP   input
                                                                                                                                            by 2% images     could to
                                                                                                                                                       compared       be the
                                                                                                                                                                          scaled   up to
                                                                                                                                                                               original
                                                                    448 × 448 pixels, enforcing the architecture to adjust to the varying image resolution,
                                                                  YOLO.
                                                                    whichTheinoriginal
                                                                               turn decrease
                                                                                          YOLO theworkedmAP.withTo address
                                                                                                                     an inputthis,    the size
                                                                                                                                  image    authors
                                                                                                                                                 of 224trained
                                                                                                                                                          × 224the     architecture
                                                                                                                                                                   pixels  during the  on
                                                                    448  ×  448  pixel   images   for  10  epochs    on  the  ImageNet      [46]  dataset,
                                                                  training stage, whilst for the detection phase, input images could be scaled up to 448 × 448providing    the  architec-
                                                                    ture with
                                                                  pixels,       the capacity
                                                                           enforcing             to adjust to
                                                                                         the architecture      theadjust
                                                                                                                    internal   filters
                                                                                                                           to the       whenimage
                                                                                                                                   varying       dealing    with higher
                                                                                                                                                        resolution,    which resolution
                                                                                                                                                                                in turn
                                                                    images,   resulting    in an increased      mAP    of 4%.   Whilst    architectures,
                                                                  decrease the mAP. To address this, the authors trained the architecture on 448 × 448 pixel such   as Fast  and   Faster
                                                                    R-CNN     predict    coordinates    directly    from    the convolutional        network,
                                                                  images for 10 epochs on the ImageNet [46] dataset, providing the architecture with the          the  original   YOLO
                                                                    utilized to
                                                                  capacity    fully connected
                                                                                 adjust           layersfilters
                                                                                          the internal      to serve  this dealing
                                                                                                                   when     purpose.withYOLO-v2
                                                                                                                                             higherreplaced
                                                                                                                                                       resolution theimages,
                                                                                                                                                                       fully connected
                                                                                                                                                                                 result-
                                                                    layer
                                                                  ing      responsible
                                                                       in an  increased for mAP predicting
                                                                                                   of 4%. Whilstbounding      boxes bysuch
                                                                                                                      architectures,       adding     anchor
                                                                                                                                                as Fast         boxes for
                                                                                                                                                          and Faster     R-CNNbounding
                                                                                                                                                                                    pre-
                                                                    boxcoordinates
                                                                  dict   predictions.directly
                                                                                          Anchorfromboxesthe[47]   are essentially
                                                                                                               convolutional           a list of
                                                                                                                                  network,     thepredefined
                                                                                                                                                    original YOLOdimensions
                                                                                                                                                                        utilized(boxes)
                                                                                                                                                                                   fully
                                                                    aimed at best matching the objects of interest. Rather than manual determination of best-fit
                                                                    anchor boxes, the authors utilized k-means clustering [48] on the training set bounding
                                                                    boxes, inclusive of the ground truth bounding boxes, grouping similar shapes and plotting
                                                                    average IoU with respect to the closest centroid as shown in Figure 4. YOLO-v2 was trained
                                                                    on different architectures, namely, VGG-16 and GoogleNet, in addition to the authors
                                                                    proposing the Darknet-19 [49] architecture due to characteristics, such as reduced process-
                                                                    ing requirements, i.e., 5.58 FLOPs compared to 30.69 FLOPs and 8.52 FLOPs on VGG-16
                                                                    and GoogleNet, respectively. In terms of performance, YOLO-v2 provided 76.8 mAP at
                                                                    67 FPS and 78.6 mAP at 40 FPS. The results demonstrated the architectures’ superiority
                                                                    over SOTA architectures of that time, such as SSD and Faster R-CNN. YOLO-9000 utilized
                                   trained on diﬀerent architectures, namely, VGG-16 and GoogleNet, in addition to the
                                   thors proposing the Darknet-19 [49] architecture due to characteristics, such as redu
                                   processing requirements, i.e., 5.58 FLOPs compared to 30.69 FLOPs and 8.52 FLOP
                                   VGG-16 and GoogleNet, respectively. In terms of performance, YOLO-v2 provided
    Machines 2023, 11, 677                                                                                          7 of 25
                                   mAP at 67 FPS and 78.6 mAP at 40 FPS. The results demonstrated the architectures’ su
                                   riority over SOTA architectures of that time, such as SSD and Faster R-CNN. YOLO-
                                   utilized YOLO-v2 architecture, aimed at real-time detection of more than 9000 diﬀe
                                   YOLO-v2 architecture, aimed at real-time detection of more than 9000 different objects;
                                   objects;
                                   however,however,     at a significantly
                                            at a significantly reduced mAPreduced
                                                                           of 19.7%. mAP of 19.7%.

                                   Figure
                                   Figure 4.4.Dimension
                                               Dimension   clusters
                                                        clusters     vs. mAP.
                                                                 vs. mAP.

                                   2.3. YOLO-v3
                                   2.3. YOLO-v3
                                       Architectures, such as VGG, focused their development work around the concept that
                                  deeperArchitectures,    suchinternal
                                         networks, i.e., more     as VGG,     focused
                                                                          layers, equatedtheir    development
                                                                                            to higher              work around
                                                                                                       accuracy. YOLO-v2    also hadthe con
                                  that deeper
                                  higher number networks,     i.e., more
                                                  of convolutional         internal
                                                                      layers compared layers,
                                                                                          to itsequated    to higher accuracy. YOLO-v2
                                                                                                 predecessor.
                                  had However,
                                       higher number      of convolutional
                                                 as the image                     layersthe
                                                                 progressed through        compared      to its
                                                                                              network, the      predecessor.
                                                                                                             progressive down sam-
                                  pling However,
                                        resulted in as
                                                     thethe
                                                         lossimage
                                                               of fine-grained
                                                                      progressed  features;
                                                                                      throughtherefore,  YOLO-v2
                                                                                                  the network,      often
                                                                                                                  the     struggled down s
                                                                                                                      progressive
                                  with
Machines 2023, 11, x FOR PEER REVIEW   detecting smaller   objects.  At  the time   research   was  active  in
                                  pling resulted in the loss of fine-grained features; therefore, YOLO-v2 oftenaddressing this issue,
                                                                                                                                 struggled8 w
                                  as evident by the deployment of skip connections [50] embedded within the proposed
                                  detecting smaller objects. At the time research was active in addressing this issue, as
                                  ResNet architecture, the focus was on addressing the vanishing gradient issue by facilitating
                                  dent  by thepropagation
                                  information   deployment    via of skip
                                                                  skip      connections
                                                                        connection,         [50] embedded
                                                                                      as presented   in Figure 5.within the proposed Res
                                   architecture, the focus was on addressing the vanishing gradient issue by facilitating
                                   formation propagation via skip connection, as presented in Figure 5.

                                   Figure5.5.Skip-connection
                                   Figure     Skip-connection    configuration.
                                                             configuration.

                                        YOLO-v3 proposed a hybrid architecture factoring in aspects of YOLO-v2, Dark
                                   53 [51], and the ResNet concept of residual networks. This enabled the preservatio
                                   fine-grained features by allowing for the gradient flow from shallow layers to deeper
                                   ers.
                                        On top of the existing 53 layers of Darknet-53 for feature extraction, a stack o
  Machines 2023, 11, 677                                                                                                   8 of 25

                                      YOLO-v3 proposed a hybrid architecture factoring in aspects of YOLO-v2, Darknet-
                                 53 [51], and the ResNet concept of residual networks. This enabled the preservation of
                                 fine-grained features by allowing for the gradient flow from shallow layers to deeper layers.
                                      On top of the existing 53 layers of Darknet-53 for feature extraction, a stack of 53 addi-
                                 tional layers was added for the detection head, totaling 106 convolutional layers for the
                                 YOLO-v3. Additionally, YOLO-v3 facilitated multi-scale detection, namely, the architecture
                                 made predictions at three different scales of granularity for outputting better performance,
                                 increasing the probability of small object detection.

                                 2.4. YOLO-v4
                                      YOLO-v4 was the first variant of the YOLO family after the original author discon-
                                 tinued further work that was introduced to the computer vision community in April 2020
                                 by Alexey Bochkovsky et al. [52]. YOLO-v4 was essentially the distillation of a large suite
                                 of object detection techniques, tested and enhanced for providing a real-time, lightweight
                                 object detector.
                                      The backbone of an object detector has a critical role in the quality of features extracted.
                                 In-line with the experimental spirit, the authors experimented with three different back-
                                 bones: CSPResNext-50, CSPDarknet-53, and EfficientNet-B3 [53]. The first was based on
                                 DenseNet [54] aimed at alleviating the vanishing gradient problem and bolstering feature
                                 propagation and reuse, resulting in reduced number of network parameters. EfficientNet
                                 was proposed by Google Brain. The paper posits that an optima selection for parameters
                                 when scaling CNNs can be ascertained through a search mechanism. After experimenting
                                 with the above feature extractors, the authors based on their intuition and backed by their
                                 experimental results selected CSPDarknet-53 as the official backbone for YOLO-v4.
                                      For feature aggregation, the authors experimented with several techniques for integra-
                                 tion at the neck level including feature pyramid network (FPN) [55] and path aggregation
                                 network (PANet) [56]. Ultimately, the authors opted for PANet as the feature aggregator.
                                 The modified PANet, as shown in Figure 6, utilized the concatenation mechanism. PANet
                                 can be seen as an advanced version of FPN, namely, PANet proposed a bottom-up augmen-
                                 tation path along with the top-down path (FPN), adding a ‘shortcut’ connection for linking
                                 fine-grained features from high- and low-level layers. Additionally, the authors introduced
Machines 2023, 11, x FOR PEER REVIEW                                                                                                 9 of 2
                                 a SPP [57] block post CSPDarknet-53 aimed at increasing the receptive field and separation
                                 of the important features arriving from the backbone.

                                  Figure6. 6.
                                 Figure       Path
                                           Path    aggregation.
                                                 aggregation.     (a) Original
                                                              (a) Original PAN,PAN,  (b) modified
                                                                                (b) modified PAN. PAN.

                                        The authors also introduced a bag-of-freebies, presented in Figure 7, primarily con
                                  sisting of augmentations, such as Mosaic aimed at improving performance without intro
                                  ducing additional baggage onto the inference time. CIoU loss [58] was also introduced a
                                  a freebie, focused on the overlap of the predicted and ground truth bounding box. In th
                                  case of no overlap, the idea was to observe the closeness of the two boxes and encourag
                                  overlap if in close proximity.
                                        In addition to the bag-of-freebies, the authors introduced ‘bag-of-specials’, with th
                               The authors also introduced a bag-of-freebies, presented in Figure 7, primarily con-
                         sisting of augmentations, such as Mosaic aimed at improving performance without intro-
                         ducing additional baggage onto the inference time. CIoU loss [58] was also introduced as
                         a freebie, focused on the overlap of the predicted and ground truth bounding box. In the
                         case of no overlap, the idea was to observe the closeness of the two boxes and encourage
Machines 2023, 11, 677   overlap if in close proximity.                                                                    9 of 25

                               In addition to the bag-of-freebies, the authors introduced ‘bag-of-specials’, with the
                         authors claiming that although this set of optimization techniques presented in Figure 7
                         wouldThemarginally   impact
                                    authors also       the inference
                                                 introduced           time, they would
                                                              a bag-of-freebies,  presentedsignificantly
                                                                                               in Figure improve     the consist-
                                                                                                           7, primarily  overall
                         performance.
                         ing             One of such
                             of augmentations,   the components      within
                                                        as Mosaic aimed      the ‘bag-of-specials’
                                                                          at improving    performance  waswithout
                                                                                                            the Mish   [59] acti-
                                                                                                                   introducing
                         additional  baggage
                         vation function       ontoatthe
                                           aimed         inference
                                                      moving        time.
                                                               feature    CIoU loss
                                                                        creations      [58] was
                                                                                   toward    theiralso introduced
                                                                                                   respective       as a freebie,
                                                                                                                optimal  points.
                         focused   on the overlap
                         Cross mini-batch           of the predicted
                                             normalization            andalso
                                                               [60] was    ground    truth bounding
                                                                               presented    facilitatingbox.
                                                                                                          the In the case
                                                                                                               running   onofany
                                                                                                                               no
                         overlap,
                         GPU as themanyidea was normalization
                                          batch  to observe the closeness
                                                                  techniques of involve
                                                                                the two boxes    andGPUs
                                                                                          multiple     encourage   overlap
                                                                                                              operating   in if in
                                                                                                                             tan-
                         close
                         dem.   proximity.

                         Figure 7.7. State-of-the-art
                         Figure       State-of-the-artoptimization
                                                       optimizationmethodologies
                                                                    methodologies  experimented
                                                                                 experimented    in YOLO-v4
                                                                                              in YOLO-v4     via bag-of-spe-
                                                                                                         via bag-of-specials.
                         cials.
                              In addition to the bag-of-freebies, the authors introduced ‘bag-of-specials’, with the
                         2.5. YOLO-v5
                         authors  claiming that although this set of optimization techniques presented in Figure 7
                         would  marginally
                               The          impactin
                                   YOLO network     the inference
                                                      essence     time,of
                                                              consists  they would
                                                                          three     significantly
                                                                                key pillars,      improve
                                                                                             namely,       the for
                                                                                                     backbone  overall
                                                                                                                   fea-
                         performance.   One  of the components   within  the ‘bag-of-specials’ was  the Mish [59]
                         ture extraction, neck focused on feature aggregation, and the head for consuming output   acti-
                         vation function aimed at moving feature creations toward their respective optimal points.
                         Cross mini-batch normalization [60] was also presented facilitating the running on any
                         GPU as many batch normalization techniques involve multiple GPUs operating in tandem.

                         2.5. YOLO-v5
                              The YOLO network in essence consists of three key pillars, namely, backbone for
                         feature extraction, neck focused on feature aggregation, and the head for consuming
                         output features from the neck as input and generating detections. YOLO-v5 [61] similar to
                         YOLO-v4, with respect to contributions, focus on the conglomeration and refinement of
                         various computer vision techniques for enhancing performance. In addition, in less than
                         2 months after the release of YOLO-v4, Glenn Jocher open-sourced an implementation of
                         YOLO-v5 [61].
                              A notable mention is that YOLO-v5 was the first native release of architectures be-
                         longing to the YOLO clan, to be written in PyTorch [62] rather than Darknet. Although
                         Darknet is considered as a flexible low-level research framework, it was not purpose built
                         for production environments with a significantly smaller number of subscribers due to
                         configurability challenges. PyTorch, on the other hand, provided an established eco-system,
                         with a wider subscription base among the computer vision community and provided the
                         supporting infrastructure for facilitating mobile device deployment.
                         [61].
                              A notable mention is that YOLO-v5 was the first native release of architectures be-
                         longing to the YOLO clan, to be written in PyTorch [62] rather than Darknet. Although
                         Darknet is considered as a flexible low-level research framework, it was not purpose built
                         for production environments with a significantly smaller number of subscribers due to
Machines 2023, 11, 677                                                                                                   10 of 25
                         configurability challenges. PyTorch, on the other hand, provided an established eco-sys-
                         tem, with a wider subscription base among the computer vision community and provided
                         the supporting infrastructure for facilitating mobile device deployment.
                               Inaddition,
                              In  addition, another
                                             another notable
                                                     notableproposal
                                                               proposalwas
                                                                         wasthe the‘automated
                                                                                     ‘automated anchor
                                                                                                  anchorbox learning’
                                                                                                          box          concept.
                                                                                                               learning’  con-
                          In YOLO-v2,    the anchor  box  mechanism    was    introduced    based  on selecting
                         cept. In YOLO-v2, the anchor box mechanism was introduced based on selecting anchor     anchor  boxes
                          that closely
                         boxes          resemble
                                that closely       the dimensions
                                              resemble               of the
                                                         the dimensions     of ground   truthtruth
                                                                               the ground      boxes  in the
                                                                                                    boxes     training
                                                                                                          in the        set set
                                                                                                                  training   via
                          k-means.  The   authors select the five close-fit anchor    boxes based  on the COCO
                         via k-means. The authors select the five close-fit anchor boxes based on the COCO dataset dataset  [63]
                          and implement them as default boxes. However, the application of this methodology to a
                         [63] and implement them as default boxes. However, the application of this methodology
                          unique dataset with significant object differentials compared to those present in the COCO
                         to a unique dataset with significant object diﬀerentials compared to those present in the
                          dataset can quickly expose the inability of the predefined boxes to adapt quickly to the
                         COCO dataset can quickly expose the inability of the predefined boxes to adapt quickly
                          unique dataset. Therefore, authors in YOLO-v5 integrated the anchor box selection process
                         to the unique dataset. Therefore, authors in YOLO-v5 integrated the anchor box selection
                          into the YOLO-v5 pipeline. As a result, the network would automatically learn the best-fit
                         process into the YOLO-v5 pipeline. As a result, the network would automatically learn
                          anchor boxes for the particular dataset and utilize them during training to accelerate the
                         the best-fit anchor boxes for the particular dataset and utilize them during training to ac-
                          process. YOLO-v5 comes in several variants with respect to the computational parameters
                         celerate the process. YOLO-v5 comes in several variants with respect to the computational
                          as presented in Table 1.
                         parameters as presented in Table 1.
                         Table 1. YOLO-v5 internal variant comparison.
                         Table 1. YOLO-v5 internal variant comparison.
             Model
            Model            AveragePrecision
                            Average  Precision (@50)
                                               (@50)                  Parameters
                                                                     Parameters                            FLOPs
                                                                                                          FLOPs
           YOLO-v5s
          YOLO-v5s                   55.8%
                                    55.8%                                7.5M
                                                                        7.5  M                              13.2B
                                                                                                           13.2B
           YOLO-v5m
          YOLO-v5m                   62.4%
                                    62.4%                               21.8
                                                                       21.8 MM                              39.4B
                                                                                                           39.4B
           YOLO-v5l                  65.4%                              47.8 M                              88.1B
          YOLO-v5l
           YOLO-v5x
                                    65.4%
                                     66.9%
                                                                       47.8  M
                                                                        86.7 M
                                                                                                           88.1B
                                                                                                           205.7B
          YOLO-v5x                  66.9%                              86.7 M                             205.7B

                             YOLO-v5comprised
                             YOLO-v5   comprised of
                                                 ofaaweight
                                                       weightfile
                                                              fileequating
                                                                   equatingto
                                                                            to27
                                                                               27MB
                                                                                 MBcompared
                                                                                     comparedto toYOLO-v5l
                                                                                                   YOLO-v5lat
                                                                                                            at192
                                                                                                               192
                         MB.Figure
                         MB. Figure88demonstrates
                                     demonstrates the
                                                    the superiority
                                                        superiority of
                                                                     of YOLO-v5
                                                                        YOLO-v5 over
                                                                                 over EﬃcientDet
                                                                                      EfficientDet [64].
                                                                                                   [64].

                         Figure
                          Figure8.8.YOLO-v5
                                     YOLO-v5variant
                                             variantcomparison
                                                     comparisonvs.
                                                                vs.EﬃcientDet
                                                                    EfficientDet[61].
                                                                                 [61].

                         2.6. YOLO-v6
                               The initial codebase for YOLO-v6 [65] was released in June 2022 by the Meituan
                         Technical Team based in China. The authors focused their design strategy on producing an
                         industry-orientated object detector.
                               To meet industrial application requirements, the architecture would need to be highly
                         performant on a range of hardware options, maintaining high speed and accuracy. To
                         conform with the diverse set of industrial applications, YOLO-v6 comes in several variants
                         starting with YOLO-v6-nano as the fastest with the least number of parameters and reaching
                         YOLO-v6-large with high accuracy at the expense of speed, as shown in Table 2.
                          industry-orientated object detector.
                               To meet industrial application requirements, the architecture would need to be
                          highly performant on a range of hardware options, maintaining high speed and accuracy.
                          To conform with the diverse set of industrial applications, YOLO-v6 comes in several var-
                          iants starting with YOLO-v6-nano as the fastest with the least number of parameters and
Machines 2023, 11, 677                                                                                     11 of 252.
                          reaching YOLO-v6-large with high accuracy at the expense of speed, as shown in Table

                          Table 2. YOLO-v6 variant comparison.
                         Table 2. YOLO-v6 variant comparison.
                                                               mAP 0.5:0.95
                                  Variant                                                FPS Tesla T4 Parameters (Million)
                                                          mAP(COCO-val)
                                                                0.5:0.95
                                  Variant                                           FPS Tesla T4           Parameters (Million)
                              YOLO-v6-N                      35.9 (300 epochs)
                                                          (COCO-val)                          802                    4.3
                              YOLO-v6-T
                              YOLO-v6-N                 35.9 40.3 (300 epochs)
                                                             (300 epochs)                 802 449                    15.0
                                                                                                                     4.3
                            YOLO-v6-RepOpt
                              YOLO-v6-T                 40.3 43.3 (300 epochs)
                                                             (300 epochs)                 449 596                    17.2
                                                                                                                    15.0
                            YOLO-v6-RepOpt
                               YOLO-v6-S                43.3 43.5
                                                             (300 epochs)
                                                                  (300 epochs)            596 495                   17.2
                                                                                                                     17.2
                              YOLO-v6-S                 43.5 (300 epochs)                 495                       17.2
                              YOLO-v6-M                             49.7                      233                    34.3
                              YOLO-v6-M                        49.7                       233                       34.3
                            YOLO-v6-L-ReLU
                            YOLO-v6-L-ReLU                     51.7 51.7                  149 149                    58.5
                                                                                                                    58.5

                                The impressive performance presented in Table 2 is a result of several innovations
                              The impressive performance presented in Table 2 is a result of several innovations
                          integrated into the YOLO-v6 architecture. The key contributions can be summed into four
                         integrated into the YOLO-v6 architecture. The key contributions can be summed into four
                          points. First, in contrast to its predecessors, YOLO-v6 opts for an anchor-free approach,
                         points. First, in contrast to its predecessors, YOLO-v6 opts for an anchor-free approach,
                          making it 51% faster when compared to anchor-based approaches.
                         making it 51% faster when compared to anchor-based approaches.
                                Second, the authors introduced a revised reparametrized backbone and neck, pro-
                              Second, the authors introduced a revised reparametrized backbone and neck, proposed
                          posed as EﬃcientRep backbone and Rep-PAN neck [66], namely, up to and including
                         as EfficientRep backbone and Rep-PAN neck [66], namely, up to and including YOLO-v5,
                          YOLO-v5, the regression and classification heads shared the same features. Breaking the
                         the regression and classification heads shared the same features. Breaking the convention,
                          convention, YOLO-v6 implements the decoupled head as shown in Figure 9. As a result,
                         YOLO-v6 implements the decoupled head as shown in Figure 9. As a result, the architecture
                          the architecture has additional layers separating features from the final head, as empiri-
                         has additional layers separating features from the final head, as empirically shown to
                          cally shown
                         improve         to improve theThird,
                                    the performance.       performance.
                                                                 YOLO-v6Third,       YOLO-v6
                                                                               mandates          mandates
                                                                                           a two-loss         a two-loss
                                                                                                        function.          function.
                                                                                                                    Varifocal  loss
                         (VFL) [67] is used as the classification loss and distribution focal loss (DFL) [68], along (DFL)
                          Varifocal  loss  (VFL)  [67] is used  as  the  classification  loss and   distribution   focal loss  with
                          [68], along with
                         SIoU/GIoU            SIoU/GIoU
                                        [69] as  regression[69]  as VFL
                                                              loss.  regression
                                                                             being loss. VFL being
                                                                                   a derivative        a derivative
                                                                                                   of focal           of focal
                                                                                                             loss, treats       loss,
                                                                                                                           positive
                          treats positive   and negative   samples     at varying   degrees  of importance,     helping
                         and negative samples at varying degrees of importance, helping in balancing the learning         in balanc-
                          ing thefrom
                         signals   learning
                                        both signals
                                              sample from
                                                       types.both
                                                               DFLsample       types.for
                                                                      is deployed      DFL
                                                                                         boxisregression
                                                                                                deployedin  for  box regression
                                                                                                              YOLO-v6      medium  in
                          YOLO-v6     medium     and  large  variants,    treating the  continuous    distribution
                         and large variants, treating the continuous distribution of the box locations as discretizedof the  box  lo-
                          cations as discretized
                         probability   distribution,probability  distribution,
                                                     which is shown                which is shown
                                                                           to be particularly         to when
                                                                                               efficient be particularly
                                                                                                                 the ground eﬃcient
                                                                                                                              truth
                          when   the  ground   truth
                         box boundaries are blurred. box   boundaries      are blurred.

                         Figure 9. YOLO-v6 model base architecture.

                               Additional improvements focused on industrial applications include the use of knowl-
                         edge distillation [70], involving a teacher model used for training a student model, where
                         the predictions of the teacher are used as soft labels along with the ground truth for training
                         the student. This comes without fueling the computational cost as essentially the aim is
                         to train a smaller (student) model to replicate the high performance of the larger (teacher)
                         model. Comparing the performance of YOLO-v6 with its predecessors, including YOLO-v5
                         on the benchmark COCO dataset in Figure 10, it is clear that YOLO-v6 achieves a higher
                         mAP at various FPS.
                                  where the predictions of the teacher are used as soft labels along with the ground truth
                                  for training the student. This comes without fueling the computational cost as essentially
                                  the aim is to train a smaller (student) model to replicate the high performance of the larger
                                  (teacher) model. Comparing the performance of YOLO-v6 with its predecessors, includ-
Machines 2023, 11, 677            ing YOLO-v5 on the benchmark COCO dataset in Figure 10, it is clear that YOLO-v6      12 of 25
                                  achieves a higher mAP at various FPS.

                                  Figure 10.
                                  Figure 10. Relative evaluation of YOLO-v6 vs. YOLO-v5 [71].

                                  2.7.
                                  2.7. YOLO-v7
                                        YOLO-v7
                                        The
                                         The following
                                              following month
                                                          month after
                                                                   after the
                                                                         the release
                                                                              release of
                                                                                       of YOLO-v6,
                                                                                          YOLO-v6, the
                                                                                                     the YOLO-v7
                                                                                                          YOLO-v7 was was released
                                                                                                                           released [72].
                                                                                                                                     [72].
                                  Although    other   variants have  been  released   in between, including   YOLO-X
                                  Although other variants have been released in between, including YOLO-X [73] and      [73] and   YOLO-
                                  R [74], these
                                  YOLO-R         focused
                                              [74],        more on more
                                                     these focused   GPU speed
                                                                            on GPU enhancements    with respect
                                                                                      speed enhancements         to respect
                                                                                                              with  inferencing.   YOLO-
                                                                                                                             to inferenc-
                                  v7
                                  ing. YOLO-v7 proposes several architectural reforms for improving the accuracy high
                                      proposes   several  architectural  reforms   for improving   the accuracy  and  maintaining     and
                                  detection
                                  maintaining  speeds.   The proposed
                                                  high detection   speeds.reforms    can be split
                                                                             The proposed         intocan
                                                                                             reforms    twobecategories:   Architectural
                                                                                                              split into two  categories:
                                  reforms   and Trainable
                                  Architectural     reforms BoF   (bag-of-freebies).
                                                              and Trainable            Architectural reforms
                                                                              BoF (bag-of-freebies).           included
                                                                                                       Architectural      the implemen-
                                                                                                                      reforms   included
                                  tation  of the  E-ELAN     (extended   efficient layer  aggregation  network)   [75]
                                  the implementation of the E-ELAN (extended eﬃcient layer aggregation network) [75] inin  the YOLO-v7
                                  backbone, taking inspiration from research advancements in network efficiency. The design
                                  the YOLO-v7 backbone, taking inspiration from research advancements in network eﬃ-
                                  of the E-ELAN was guided by the analysis of factors that impact accuracy and speed, such
                                  ciency. The design of the E-ELAN was guided by the analysis of factors that impact accu-
                                  as memory access cost, input/output channel ratio, and gradient path.
                                  racy and speed, such as memory access cost, input/output channel ratio, and gradient
                                        The second architectural reform was presented as compound model scaling, as shown
                                  path.
                                  in Figure 11. The aim was to cater for a wider scope of application requirements, i.e., certain
                                         The second architectural reform was presented as compound model scaling, as
                                  applications require accuracy to be prioritized, whilst others may prioritize speed. Although
                                  shown in Figure 11. The aim was to cater for a wider scope of application requirements,
                                  NAS (network architecture search) [76] can be used for parameter-specific scaling to find
                                  i.e., certain applications require accuracy to be prioritized, whilst others may prioritize
                                  the best factors, the scaling factors are independent [77]. Whereas the compound-scaling
Machines 2023, 11, x FOR PEER REVIEW                                                                                              13 of 26
                                  speed. Although NAS (network architecture search) [76] can be used for parameter-spe-
                                  mechanism allows for the width and depth to be scaled in coherence for concatenation-
                                  cific scaling to find the best factors, the scaling factors are independent [77]. Whereas the
                                  based networks, maintaining optimal network architecture while scaling for different sizes.
                                  compound-scaling mechanism allows for the width and depth to be scaled in coherence
                                  for concatenation-based networks, maintaining optimal network architecture while scal-
                                  ing for diﬀerent sizes.

                                  Figure 11. YOLO-v7 compound scaling.

                                        Re-parameterization planning is based on averaging a set of model weights to obtain
                                  a more robust network [78,79]. Expanding further, module level re-parameterization ena-
                                  bles segments of the network to regulate their own parameterization strategies. YOLO-v7
                                  utilizes gradient flow propagation paths with the aim to observe which internal network
Machines 2023, 11, 677                                                                                                           13 of 25
                         Figure 11. YOLO-v7 compound scaling.

                                Re-parameterization planning is based on averaging a set of model weights to obtain
                         a more Re-parameterization       planning
                                    robust network [78,79].         is basedfurther,
                                                                Expanding       on averaging
                                                                                          modulea set  of model
                                                                                                   level           weights to obtain
                                                                                                          re-parameterization        ena-a
                         moresegments
                         bles    robust network      [78,79]. Expanding
                                             of the network   to regulate further,
                                                                             their own module   level re-parameterization
                                                                                          parameterization                       enables
                                                                                                               strategies. YOLO-v7
                         segments
                         utilizes       of the flow
                                    gradient     network   to regulate
                                                      propagation   pathstheir
                                                                             with own
                                                                                    the parameterization
                                                                                         aim to observe which strategies.
                                                                                                                     internalYOLO-v7
                                                                                                                                network
                         utilizes    gradient   flow  propagation   paths
                         modules should deploy re-parameterization strategies.with  the  aim  to observe    which    internal network
                         modules       should deploy
                                The auxiliary     head re-parameterization
                                                         coarse-to-fine concept   strategies.
                                                                                      is proposed on the premise that the net-
                                The   auxiliary   head  coarse-to-fine  concept
                         work head is quite far downstream; therefore, the         is proposed
                                                                                        auxiliaryon   theispremise
                                                                                                   head     deployed  thatatthe
                                                                                                                             thenetwork
                                                                                                                                 middle
                         head    is quite  far downstream;    therefore,   the  auxiliary   head  is deployed
                         layers to assist in the training process. However, this would not train as eﬃciently as  at the middle    layers
                                                                                                                                      the
                         to  assist   in the  training  process.  However,       this  would   not
                         lead head, due to the former not having access to the complete network.    train  as efficiently    as the  lead
                         head,Figure
                                  due to12the   formeranot
                                             presents       having access
                                                         performance           to the complete
                                                                         comparison               network.
                                                                                          of YOLO-v7     with the preceding YOLO
                                Figure    12 presents  a  performance    comparison
                         variants on the MS COCO dataset. It is clear from Figure 12 that of YOLO-v7     withallthe  preceding
                                                                                                                   YOLO-v7        YOLO
                                                                                                                                variants
                         variants     on  the  MS   COCO    dataset.  It  is  clear  from   Figure   12 that  all
                         surpassed the compared object detectors in accuracy and speed in the range of 5–160 FPS.  YOLO-v7      variants
                         surpassed the compared object detectors in accuracy and speed in the range of 5–160 FPS.
                         It is, however, important to note, as mentioned by the authors of YOLO-v7, that none of
                         It is, however, important to note, as mentioned by the authors of YOLO-v7, that none of
                         the YOLO-v7 variants are designed for CPU-based mobile device deployment. YOLO-v7-
                         the YOLO-v7 variants are designed for CPU-based mobile device deployment. YOLO-
                         tiny/v7/W6 variants are designed for edge GPU, consumer GPU, and cloud GPU, respec-
                         v7-tiny/v7/W6 variants are designed for edge GPU, consumer GPU, and cloud GPU,
                         tively. Whilst YOLO-v7-E6/D6/E6E are designed for high-end cloud GPUs only.
                         respectively. Whilst YOLO-v7-E6/D6/E6E are designed for high-end cloud GPUs only.

                                    YOLO-v7 comparison
                         Figure 12. YOLO-v7
                         Figure             comparison vs. other
                                                           other object
                                                                 object detectors
                                                                        detectors [72].
                                                                                  [72].

                              Internal variant comparison of YOLO-v7 is presented in Table 3. As evident, there is a
                         significant performance gap with respect to mAP when comparing YOLO-v7-tiny with the
                         computationally demanding YOLO-v7-D6. However, the latter would not be suitable for
                         edge deployment onto a computationally constrained device.

                         Table 3. Variant comparison of YOLO-v7.

                                Model              Size (Pixels)           mAP (@50)             Parameters               FLOPs
                            YOLO-v7-tiny                 640                  52.8%                 6.2 M                  5.8G
                              YOLO-v7                   640                   69.7%                36.9 M                 104.7G
                             YOLO-v7-X                  640                   71.1%                71.3 M                 189.9G
                            YOLO-v7-E6                  1280                  73.5%                97.2 M                 515.2G
                            YOLO-v7-D6                  1280                  73.8%                154.7 M                806.8G
Machines 2023, 11, 677                                                                                                         14 of 25

                               2.8. YOLO-v8
                                       The latest addition to the family of YOLO was confirmed in January 2023 with the
                                  release of YOLO-v8 [80] by Ultralytics (also released YOLO-v5). Although a paper release
                                  is impending and many features are yet to be added to the YOLO-v8 repository, initial
                                  comparisons of the newcomer against its predecessors demonstrate its superiority as the
                                  new YOLO state-of-the-art.
                                       Figure 13 demonstrates that when comparing YOLO-v8 against YOLO-v5 and YOLO-
                                  v6 trained on 640 image resolution, all YOLO-v8 variants output better throughput with a
                                  similar number of parameters, indicating toward hardware-efficient, architectural reforms.
                                  The fact that YOLO-v8 and YOLO-v5 are presented by Ultralytics with YOLO-v5 providing
                                  impressive real-time performance and based on the initial benchmarking results released
 Machines 2023, 11, x FOR PEER REVIEW                                                                                 15 of 26
                                  by Ultralytics, it is strongly assumed that the YOLO-v8 will be focusing on constrained
                                  edge device deployment at high-inference speed.

                                Figure13.
                               Figure  13.YOLO-v8
                                           YOLO-v8comparison
                                                   comparisonwith
                                                             withpredecessors
                                                                  predecessors[80].
                                                                               [80].

                               3.3.Industrial
                                    IndustrialDefect
                                                DefectDetection
                                                        Detectionvia
                                                                   ViaYOLO
                                                                        YOLO
                                      The
                                       The previous section demonstratesthe
                                           previous  section  demonstrates    therapid
                                                                                  rapidevolution
                                                                                         evolutionof ofthetheYOLO
                                                                                                              YOLO‘clan’
                                                                                                                       ‘clan’ofofobject
                                                                                                                                  object
                               detectors    amongst   the computer    vision community.     This   section   of the
                                detectors amongst the computer vision community. This section of the review focuses  review    focuseson
                               on
                                thethe  implementation
                                      implementation    of of YOLO
                                                           YOLO       variants
                                                                  variants  forfor
                                                                                thethe detection
                                                                                    detection    of of  surface
                                                                                                    surface      defects
                                                                                                              defects      within
                                                                                                                        within   thethe
                                                                                                                                     in-
                               industrial   setting.The
                                dustrial setting.    Theselection
                                                          selection
                                                                  ofof ‘industrial
                                                                     ‘industrial   setting’
                                                                                 setting’ is is
                                                                                             duedue
                                                                                                  to to
                                                                                                      itsits varying
                                                                                                          varying   andand   stringent
                                                                                                                          stringent  re-
                               requirements
                                quirements alternating between accuracy and speed, a theme which is foundthrough
                                                alternating  between   accuracy  and  speed,   a theme     which  is found     through
                               DNA
                                DNAof   ofthe
                                           theYOLO
                                               YOLOvariants.
                                                       variants.

                                3.1. Industrial Fabric Defect Detection
                                      Rui Jin et al. [81] in their premise state the ineﬃciencies of manual inspection in the
                                textile manufacturing domain as high cost of labor, human-related fatigue, and reduced
                                detection speed (less than 20 m/min). The authors aim to address these ineﬃciencies by
Machines 2023, 11, 677                                                                                                         15 of 25

                                 3.1. Industrial Fabric Defect Detection
                                        Rui Jin et al. [81] in their premise state the inefficiencies of manual inspection in the
                                  textile manufacturing domain as high cost of labor, human-related fatigue, and reduced
                                  detection speed (less than 20 m/min). The authors aim to address these inefficiencies by
                                  proposing a YOLO-v5-based architecture, coupled with a spatial attention mechanism
                                  for accentuation of smaller defective regions. The proposed approach involved a teacher
                                  network trained on the fabric dataset. Post training of the teacher network, the learned
                                  weights were distilled to the student network, which was compatible for deployment onto
                                  a Jetson TX2 [82] via TensorRT [83]. The results presented by the authors show, as expected,
Machines 2023, 11, x FOR PEER REVIEW
                                  that the teacher network reported higher performance with an AUC of 98.1% compared          16 of to
                                                                                                                                    26
                                  95.2% (student network). However, as the student network was computationally smaller,
                                  the inference time was significantly less at 16 ms for the student network in contrast to the
                                  teacher network
                                  authors   claim thatat the
                                                          35 ms on the Jetson
                                                             proposed          TX2.
                                                                        solution     Based on
                                                                                  provides     theaccuracy
                                                                                            high   performance,    the authors
                                                                                                             and real-time      claim
                                                                                                                            inference
                                  that the  proposed   solution  provides   high accuracy  and real-time
                                  speed, making it compatible for deployment via the edge device.         inference speed,  making   it
                                  compatible     for deployment   via the  edge  device.
                                        Sifundvoleshile Dlamini et al. [84] propose a production environment fabric defect
                                        Sifundvoleshile
                                  detection   framework Dlamini      et al.
                                                            focused on      [84] propose
                                                                        real-time         a production
                                                                                   detection and accurateenvironment    fabric
                                                                                                            classification     defect
                                                                                                                           on-site, as
                                  detection    framework     focused  on  real-time detection  and   accurate  classification
                                  shown in Figure 14. The authors embed conventional image processing at the onset of         on-site,
                                  as shown in Figure 14. The authors embed conventional image processing at the onset
                                  their data enhancement strategy, i.e., filtering to denoise feature enhancement. Post aug-
                                  of their data enhancement strategy, i.e., filtering to denoise feature enhancement. Post
                                  mentations and data scaling, the authors train the YOLO-v4 architecture based on pre-
                                  augmentations and data scaling, the authors train the YOLO-v4 architecture based on
                                  trained weights. The reported performance was respectable with an F1-score of 93.6%, at
                                  pretrained weights. The reported performance was respectable with an F1-score of 93.6%,
                                  an impressive detection speed of 34 fps and prediction speed of 21.4 ms. The authors claim
                                  at an impressive detection speed of 34 fps and prediction speed of 21.4 ms. The authors
                                  that the performance is evident to the eﬀectiveness of the selected architecture for the
                                  claim that the performance is evident to the effectiveness of the selected architecture for the
                                  given domain.
                                  given domain.

                                 Figure 14.
                                 Figure     Inspection machine
                                        14. Inspection machine integration
                                                               integration [84].
                                                                           [84].

                                       Restricted by the available computing resources for edge deployment, Guijuan Lin et al. [85]
                                       Restricted by the available computing resources for edge deployment, Guijuan Lin et
                                 state problems with quality inspection in the fabric production domain, including minute
                                 al. [85] state problems with quality inspection in the fabric production domain, including
                                 scale of defects, extreme unbalance with the aspect ratio of certain defects, and slow defect
                                 minute scale of defects, extreme unbalance with the aspect ratio of certain defects, and
                                 detection speeds. To address these issues, the authors proposed a sliding-window, self-
                                 slow defect detection speeds. To address these issues, the authors proposed a sliding-win-
                                 attention (multihead) mechanism calibrated for small defect targets. Additionally, the Swin
                                 dow, self-attention (multihead) mechanism calibrated for small defect targets. Addition-
                                 Transformer [86] module as depicted in Figure 15 was integrated into the original YOLO-v5
                                 ally, the Swin Transformer [86] module as depicted in Figure 15 was integrated into the
                                 architecture for the extraction of hierarchical features. Furthermore, the generalized focal
                                 original YOLO-v5 architecture for the extraction of hierarchical features. Furthermore, the
                                 loss is implemented with the architecture aimed at improving the learning process for
                                 generalized
                                 positive targetfocal loss is implemented
                                                   instances,               with
                                                               whilst lowering    the
                                                                                the   architecture
                                                                                    rate of missed aimed   at improving
                                                                                                   detections.          the report
                                                                                                                The authors learn-
                                 ing  process  for positive  target instances, whilst lowering  the rate of missed detections.
                                 the accuracy of the proposed solution on a real-world fabric dataset, reaching 76.5% mAP      The
                                 authors report the accuracy of the proposed solution on a real-world fabric dataset, reach-
                                 ing 76.5% mAP at 58.8 FPS, making it compatible with the real-time detection require-
                                 ments for detection via embedded devices.
  Machines 2023, 11, 677                                                                                                               16 of 25

Machines 2023, 11, x FOR PEER REVIEW                                                                                                              17 of 26
                                at 58.8 FPS, making it compatible with the real-time detection requirements for detection
                                via embedded devices.

                                Figure15.
                                Figure 15.Backbone
                                           Backboneforfor Swin
                                                       Swin    Transformer
                                                            Transformer     network
                                                                        network [85]. [85].

                                3.2. Solar Cell Surface Defect Detection
                                3.2. Solar Cell Surface Defect Detection
                                      Setting their premise, the authors [87] state that human-led Photovoltaic (PV) inspec-
                                       Setting
                                tion has  manytheir     premise,
                                                  drawbacks          the authors
                                                                 including            [87] stateof
                                                                              the requirement       that   human-led
                                                                                                       operation           Photovoltaic
                                                                                                                    and maintenance          (PV) inspec
                                                                                                                                          (O&M)
                                tion has many
                                engineers,             drawbacks
                                              cell-by-cell   inspection, including      the requirement
                                                                             high workload,        and reduced    ofefficiency.
                                                                                                                      operationThe  and     maintenance
                                                                                                                                        authors
                                (O&M) an
                                propose   engineers,
                                              improvedcell-by-cell
                                                            architectureinspection,        high workload,
                                                                            based on YOLO-v5                      and reduced eﬃciency.
                                                                                                      for the characterization      of complex The au
                                thorscell
                                solar   propose
                                           surfacean     improved
                                                      textures            architecture
                                                                 and defective     regions.based     on YOLO-v5
                                                                                               The proposal      is basedforonthe
                                                                                                                               thecharacterization
                                                                                                                                   integration           o
                                of deformable
                                complex      solarconvolution
                                                     cell surface  within   the CSP
                                                                       textures   andmodule
                                                                                         defectivewithregions.
                                                                                                         the aim ofThe achieving  an adaptive
                                                                                                                           proposal     is based on the
                                learning  scale.
                                integration     ofAdditionally,
                                                    deformablean         attention mechanism
                                                                     convolution       within the   is incorporated
                                                                                                        CSP modulefor        enhanced
                                                                                                                           with the aim   feature
                                                                                                                                             of achieving
                                extraction. Moreover, the authors optimize the original YOLO-v5 architecture further via
                                an adaptive learning scale. Additionally, an attention mechanism is incorporated for en
                                K-means++ clustering for anchor box determination algorithm. Based on the presented
                                hanced feature extraction. Moreover, the authors optimize the original YOLO-v5 architec
                                results, the improved architecture achieved a respectable mAP of 89.64% on an EL-based
                                ture further
                                solar cell image via   K-means++
                                                    dataset,            clustering
                                                               7.85% higher           for anchor
                                                                                compared      to mAPbox  for determination       algorithm.
                                                                                                             the original architecture,      withBased on
                                the presented
                                detection   speedresults,
                                                    reachingthe     improved
                                                                36.24   FPS, whicharchitecture       achieved
                                                                                       can be translated      as aa more
                                                                                                                    respectable
                                                                                                                            accuratemAP     of 89.64% on
                                                                                                                                      detection
                                an EL-based
                                while  remaining  solar  cell image
                                                     compatible      withdataset,    7.85%
                                                                           the real-time       higher compared to mAP for the original ar
                                                                                            requirements.
                                chitecture,
                                      Amran with       detection
                                                Binomairah            speed
                                                                 et al.        reachingtwo
                                                                         [88] highlight     36.24     FPS, which
                                                                                                  frequent    defectscan     be translated
                                                                                                                        encountered      during as a more
                                the manufacturing
                                accurate    detectionprocess
                                                          while of    crystallinecompatible
                                                                   remaining        solar cells as    darkthe
                                                                                                    with     spot/region
                                                                                                                real-time and     microcracks.
                                                                                                                              requirements.
                                The latter
                                       Amran canBinomairah
                                                   have a detrimental        impact
                                                                   et al. [88]         on thetwo
                                                                                 highlight       performance       of the module,
                                                                                                     frequent defects                  whichduring
                                                                                                                             encountered        is      the
                                a major cause for PV module failures. The authors subscribe to the YOLO architecture,
                                manufacturing process of crystalline solar cells as dark spot/region and microcracks. The
                                comparing the performance of their methodology on YOLO-v4 and an improved YOLO-v4-
                                latter can have a detrimental impact on the performance of the module, which is a major
                                tiny integrated with a spatial pyramid pooling mechanism. Based on the presented results,
                                cause forachieved
                                YOLO-v4      PV module  98.8% failures.
                                                                 mAP atThe 62.9 authors
                                                                                ms, whilst subscribe      to theYOLO-v4-tiny
                                                                                               the improved        YOLO architecture,
                                                                                                                                  lagged with  comparing
                                the performance
                                91%  mAP at 28.2 ms.    ofThe
                                                           their   methodology
                                                                authors    claim thaton    YOLO-v4
                                                                                        although          and an
                                                                                                    the latter       improved
                                                                                                                is less accurate,YOLO-v4-tiny
                                                                                                                                   it is notably      inte
                                grated   with   a  spatial
                                faster than the former.      pyramid       pooling   mechanism.         Based     on  the  presented     results,  YOLO
                                v4 achieved
                                      Tianyi Sun 98.8%
                                                    et al. mAP     at 62.9
                                                           [89] focus        ms, whilsthot-spot
                                                                         on automated        the improved
                                                                                                        detection YOLO-v4-tiny
                                                                                                                     within PV cells  lagged
                                                                                                                                         based with
                                                                                                                                                 a     91%
                                modified
                                mAP at 28.2 version
                                                  ms.ofThe
                                                         the YOLO-v5
                                                               authors claimarchitecture.    The first the
                                                                                   that although         improvement
                                                                                                              latter is lesscomes  in the form
                                                                                                                               accurate,     it is notably
                                of enhanced
                                faster  than theanchors
                                                    former.and detection heads for the respective architecture. To improve the
                                detection precision at varying scales, k-means clustering [48] is deployed for clustering the
                                       Tianyi Sun et al. [89] focus on automated hot-spot detection within PV cells based a
                                length–width ratio with respect to the data annotation frame. Additionally, a set of the
                                modified version of the YOLO-v5 architecture. The first improvement comes in the form
                                anchors consisting of smaller values were added to cater for the detection of small defects
                                of optimizing
                                by enhanced anchors
                                                  the clusterand     detection
                                                                number.           heads for
                                                                            The reported         the respective
                                                                                             performance       of the architecture.     To improve the
                                                                                                                       improved architecture
                                detection     precision     at  varying     scales,  k-means        clustering     [48]
                                was reported as 87.8% mAP, with the average recall rate of 89.0% and F1-score reaching    is deployed      for clustering
                                the length–width ratio with respect to the data annotation frame. Additionally, a set of the
                                anchors consisting of smaller values were added to cater for the detection of small defects
                                by optimizing the cluster number. The reported performance of the improved architecture
                                was reported as 87.8% mAP, with the average recall rate of 89.0% and F1-score reaching
 Machines 2023, 11, 677                                                                                                                 17 of 25

                                  88.9%. The reported FPS was impressive reaching 98.6 FPS, with the authors claiming
                                  that the proposed solution would provide intelligent monitoring at PV power stations.
Machines 2023, 11, x FOR PEER REVIEW                                                                                  18 of 26
                                  Inferencing output presented in Figure 16 shows the proposed AP-YOLO-v5 architecture,
                                  providing inferences at a higher confidence level compared to the original YOLO-v5.

                               Figure 16.Inference/confidence
                               Figure16.  inference/confidencecomparison [89].
                                                                comparison  [89].
                               3.3. Steel Surface Defect Detection
                               3.3. Steel Surface Defect Detection
                                     Dinming Yang et al. [90] set the premise of their research by stating the importance
                                      Dinming
                               of steel            Yanginspection,
                                         pipe quality      et al. [90] citing
                                                                        set thethepremise
                                                                                      growing   ofdemand
                                                                                                    their research       by stating
                                                                                                               in countries,     such astheChina.
                                                                                                                                             importance
                                of steel  pipe   quality    inspection,     citing   the   growing        demand      in
                               Although X-ray testing is utilized as one of the key methods for industrial nondestructive countries,     such   as China.
                                Although
                               testing       X-ray
                                        (NDT),   the testing
                                                      authorsis    utilized
                                                                state that itas  one
                                                                              still    of thehuman
                                                                                    requires      key methods
                                                                                                           assistanceforfor
                                                                                                                          industrial    nondestructive
                                                                                                                             the determination,
                                testing (NDT),
                               classification,  and the  authors state
                                                      localization    of thethat  it stillThe
                                                                              defects.      requires
                                                                                               authorshumanproposeassistance        for the determina-
                                                                                                                       the implementation        of
                               YOLO-v5     for  production-based        weld   steel  defect    detection    based    on
                                tion, classification, and localization of the defects. The authors propose the implementa- X-ray  images    of the
                               weld   pipe.
                                tion of      The authors
                                         YOLO-v5             claim that the trained
                                                       for production-based             YOLO-v5
                                                                                     weld               reached
                                                                                              steel defect         a mAP of
                                                                                                               detection        98.7%on
                                                                                                                              based     (IoU-0.5),
                                                                                                                                           X-ray images
                               whilst  meeting    the  real-time   detection   requirements        of steel
                                of the weld pipe. The authors claim that the trained YOLO-v5 reached a mAP   pipe   production     with   a single
                                                                                                                                                 of 98.7%
                               image detection rate of 0.12 s.
                                (IoU-0.5), whilst meeting the real-time detection requirements of steel pipe production
                                     Zhuxi MA et al. [91] address the issue of large-scale computation and specific hard-
                                with a single image detection rate of 0.12 s.
                               ware requirements for automated defect detection in aluminum strips. The authors select
                               YOLO-v4Zhuxi as MA    et al. [91] address
                                               the architecture,     whilst the
                                                                              the issue
                                                                                    backboneof large-scale
                                                                                                   is constructedcomputation
                                                                                                                       to make use  andofspecific
                                                                                                                                           depth- hard-
                               wise separable convolutions along with a parallel dual attention mechanism for feature select
                                ware   requirements       for  automated      defect   detection       in  aluminum        strips.  The   authors
                                YOLO-v4 as the
                               enhancement,            architecture,
                                                  as shown     in Figurewhilst
                                                                           17. Thetheproposed
                                                                                        backbone         is constructed
                                                                                                     network     is tested on to real
                                                                                                                                 make     use
                                                                                                                                       data     of depth-
                                                                                                                                             from
                               awise  separable
                                  cold-rolling       convolutions
                                                workshop,              along
                                                                providing       with a parallel
                                                                             impressive      results on dualrealattention     mechanism
                                                                                                                 data achieving       an mAP  foroffeature
                                enhancement,
                               96.28%.   Compared  as shown      in Figure
                                                        to the original       17. Thethe
                                                                          YOLO-v4,        proposed
                                                                                              authors network
                                                                                                          claim thatisthe tested   on real
                                                                                                                            proposed         data from a
                                                                                                                                         architec-
                               ture  volume isworkshop,
                                cold-rolling      reduced byproviding
                                                                  83.38%, whilst     the inference
                                                                               impressive        results  speed   is increased
                                                                                                            on real               by a factor
                                                                                                                        data achieving       anofmAP of
                               three.  The  increase   in performance     was   partly  due    to  the  custom    anchor
                                96.28%. Compared to the original YOLO-v4, the authors claim that the proposed architec-     approach,    whereby
                               due
                                turetovolume
                                        the maximum       aspectbyratio
                                                 is reduced              of thewhilst
                                                                     83.38%,     customthe  dataset,    the defect
                                                                                                 inference     speed  wasis set to 1:20 which
                                                                                                                            increased            is
                                                                                                                                          by a factor   of
                               in-line with the defect characteristics, such as scratch marks.
                               three. The increase in performance was partly due to the custom anchor approach,
                               whereby due to the maximum aspect ratio of the custom dataset, the defect was set to 1:20
                               which is in-line with the defect characteristics, such as scratch marks.
Machines 2023,
  Machines 2023,11,
                 11,x677
                      FOR PEER REVIEW                                                                                            18 of 25 19 of 2

                                 Figure17.
                                 Figure 17.Proposed
                                            Proposed  parallel
                                                    parallel    network
                                                             network     structure
                                                                     structure [91]. [91].

                                       Jianting
                                        Jianting Shi et et
                                                   Shi  al.al.
                                                           [92]  citecite
                                                               [92]   the the
                                                                          manufacturing
                                                                               manufacturing process of steelofproduction
                                                                                                  process                  as the reason
                                                                                                                steel production    as the reason
                                 for various    defects originating    on  the steel surface,  such as rolling  scale and
                                  for various defects originating on the steel surface, such as rolling scale and patches. patches.  The      Th
                                 authors state that the small dimensions of the defects as well as the stringent detection
                                  authors state that the small dimensions of the defects as well as the stringent detection
                                 requirements make the quality inspection process a challenging task. Therefore, the authors
                                  requirements make the quality inspection process a challenging task. Therefore, the au
                                 present an improved version of YOLO-v5 by incorporating an attention mechanism for
                                  thors present
                                 facilitating       an improved
                                               the transmission    of version   of YOLO-v5
                                                                      shallow features           by incorporating
                                                                                          from the  backbone to thean     attention
                                                                                                                       neck,         mechanism
                                                                                                                             preserving
                                  for defective
                                 the  facilitating    the transmission
                                                  regions,  in addition toof     shallow
                                                                              k-means       featuresoffrom
                                                                                         clustering     anchortheboxes
                                                                                                                   backbone    to the neck, pre
                                                                                                                         for addressing
                                  serving   the   defective    regions,    in addition    to  k-means    clustering    of
                                 the extreme aspect ratios of defective targets within the dataset. The authors state thatanchor   boxes
                                                                                                                                     the for ad
                                  dressing the
                                 improved          extremeachieved
                                              architecture    aspect ratios
                                                                        86.35% ofmAP
                                                                                  defective   targets
                                                                                        reaching       within
                                                                                                  45 FPS         the dataset.
                                                                                                           detection           The authors
                                                                                                                      speed, whilst  the     stat
                                 original
                                  that thearchitecture
                                             improvedachieved         81.78%
                                                           architecture        mAP at 52
                                                                             achieved       FPS. mAP reaching 45 FPS detection speed
                                                                                         86.35%
                                 whilst the original architecture achieved 81.78% mAP at 52 FPS.
                                 3.4. Pallet Racking Defect Inspection

                                 3.4. A promising application with significant deployment scope in the warehousing
                                      Pallet Racking Defect Inspection
                                 and general industrial storage centers is automated pallet racking inspection. Ware-
                                 houses Aand
                                           promising     application
                                              distribution              witha significant
                                                               centers host                    deployment
                                                                                critical infrastructure        scope
                                                                                                           known        in the warehousing
                                                                                                                    as racking    for stock     and
                                  general industrial
                                 storage.   Unnoticed storage
                                                          damagecenters
                                                                    to palletis racking
                                                                                 automated  can pallet
                                                                                                pave theracking   inspection.
                                                                                                            way for   significant Warehouses
                                                                                                                                     losses     and
                                  distribution
                                 initiated        centers
                                            by racking      host a leading
                                                          collapse  critical to
                                                                              infrastructure
                                                                                  wasted/damaged  known     as racking
                                                                                                         stock, financialfor    stock storage. Un
                                                                                                                             implications,
                                 operational
                                  noticed damagelosses,toinjured   employees,
                                                           pallet racking   can andpaveworst-case,
                                                                                           the way forloss   of lives [93].
                                                                                                          significant    losses Due  to the by rack
                                                                                                                                 initiated
                                 inefficiencies   of the  conventional    racking    inspection    mechanisms,      such
                                  ing collapse leading to wasted/damaged stock, financial implications, operational losses  as human-led
                                 annual inspection resulting in labor costs, bias, fatigue, and mechanical products, such
                                  injured employees, and worst-case, loss of lives [93]. Due to the ineﬃciencies of the con
                                 as rackguards [94] lacking classification intelligence, CNN-based automated detection
                                  ventional racking inspection mechanisms, such as human-led annual inspection resulting
                                 seems to be a promising alternative.
                                  in labor  costs,the
                                       Realizing    bias,  fatigue,
                                                       potential,   and mechanical
                                                                  Hussain                   products, such
                                                                            et al. [95] inaugurated           as rackguards
                                                                                                        research  into automated  [94]pallet
                                                                                                                                       lacking clas
                                 racking detection via computer vision. After presenting their initial research based on the alterna
                                  sification intelligence,     CNN-based        automated      detection    seems    to  be  a  promising
                                  tive.
                                 MobileNet-V2      architecture, the authors recently proposed the implementation of YOLO-
                                 v7 forRealizing
                                         automated   the potential,
                                                       pallet  rackingHussain
                                                                        inspectionet al.[96].
                                                                                          [95] The
                                                                                               inaugurated     research
                                                                                                    selection of            into automated
                                                                                                                  the architecture     was palle
                                 in-line with  the  stringent   requirements     of production    floor  deployment,     i.e.,
                                  racking detection via computer vision. After presenting their initial research based on th   edge device
                                 deployment,
                                  MobileNet-V2   placed  onto an operating
                                                     architecture,             forklift,
                                                                     the authors          requiring
                                                                                      recently       real-timethe
                                                                                                 proposed       detection    as the forklift
                                                                                                                    implementation        of YOLO
                                 v7 for automated pallet racking inspection [96]. The selection of the architecture was in
                                 line with the stringent requirements of production floor deployment, i.e., edge device de
                                 ployment, placed onto an operating forklift, requiring real-time detection as the forklif
                                 approaches the racking. Evaluating the performance of the proposed solution on a rea
                                 dataset, the authors claimed an impressive performance of 91.1% mAP running at 19 FPS
Machines 2023, 11, 677                                                                                            19 of 25

                         approaches the racking. Evaluating the performance of the proposed solution on a real
                         dataset, the authors claimed an impressive performance of 91.1% mAP running at 19 FPS.
                              Table 4 presents a comparison of the present research in this emerging field. Although
                         mask R-CNN presents the highest accuracy, which is a derivative of the segmentation
                         family of architectures with significant computational load, this makes it an infeasible
                         option for deployment. Whereas the proposed approach utilizing YOLO-v7 achieved
                         similar accuracy compared to MobileNet-V2, whilst requiring significantly less training
                         data along with inferencing at 19 FPS.

                         Table 4. Racking domain research comparison.

                              Research         Architecture      Dataset Size        Accuracy             FPS
                                [95]          MobileNet-V2          19,717             92.7%              -----
                                [96]           YOLO-v7               2095              91.1%               19
                                [97]          Mask-RCNN               75              93.45%              -----

                         4. Discussion
                               The YOLO family of object detectors has had a significant impact on improving the
                         potential of computer vision applications. Right from the onset, i.e., the release of the
                         YOLO-v1 in 2015, significant breakthroughs were introduced. YOLO-v1 became the first
                         architecture combining the two conventionally separate tasks of bounding box prediction
                         and classification into one. YOLO-v2 was released in the following year, introducing archi-
                         tectural improvements and iterative improvements, such as batch normalization, higher
                         resolution, and anchor boxes. In 2018, YOLO-v3 was released, an extension of previous
                         variants with enhancements including the introduction of objectness scores for bounding
                         box predictions added connections for the backbone layers and the ability to generate
                         predictions at three different levels of granularity, leading to improved performance on
                         smaller object targets.
                               After a short delay, YOLO-v4 was released in April 2020, becoming the first variant of
                         the YOLO family not to be authored by the original author Joseph Redmon. Enhancements
                         included improved feature aggregation, gifting of the ‘bag of freebies’, and the mish
                         activation. In a matter of months, YOLO-v5 entered the computer vision territory, becoming
                         the first variant to be released without being accompanied by a paper release. YOLO-v5
                         based on PyTorch, with an active GitHub repo further delineated the implementation
                         process, make it accessible to a wider audience. Focused on internal architectural reforms,
                         YOLO-v6 authors redesigned the backbone (EfficientRep) and neck (Rep-PAN) modules,
                         with an inclination toward hardware efficiency. Additionally, anchor-free and the concept
                         of decoupled head was introduced, implying additional layers for feature separation from
                         the final head, which is empirically shown to improve the overall performance. The authors
                         of YOLO-v7 also focused on architectural reforms, considering the amount of memory
                         required to keep layers within memory and the distance required for gradients to back-
                         propagate, i.e., shorter gradients, resulting in enhanced learning capacity. For the ultimate
                         layer aggregation, the authors implemented E-ELAN, which is an extension of the ELAN
                         computational block. The advent of 2023 introduced the latest version of the YOLO family,
                         YOLO-v8, which was released by Ultralytics. With an impending paper release, initial
                         comparisons of the latest version against predecessors have shown promising performance
                         with respect to throughput when compared to similar computational parameters.

                         4.1. Reason for Rising Popularity
                             Table 5 presents a summary of the reviewed YOLO variants based on the underlying
                         framework, backbone, average-precision (AP), and key contributions. It can be observed
                         from Table 3 that as the variants evolved there was a shift from the conservative Darknet
                         framework to a more accessible one, i.e., PyTorch. The AP presented here is based on
                         COCO-2017 [63] with the exception of YOLO-v1/v2, which are based on VOC-2017 [39].
Machines 2023, 11, 677                                                                                                         20 of 25

                               COCO-2017 [63] consists of over 80 objects designed to represent a vast array of regularly
                               seen object. It contains 121,408 images resulting in 883,331 object annotations with median
                               image ratio of 640 × 480 pixels. It is important to note that the overall accuracy along with
                               inference capacity depends on the deployed design/training strategies, as demonstrated in
                               the industrial surface detection section.

                               Table 5. Abstract variant comparison.

    Variant        Framework      Backbone            AP (%)                                    Comments
       V1            Darknet     Darknet-24             63.4             Only detect a maximum of two objects in the same grid.
                                                                       Introduced batch norm, k-means clustering for anchor boxes.
       V2            Darknet     Darknet-24             63.4
                                                                                  Capable of detecting > 9000 categories.
                                                                       Utilized multi-scale predictions and spatial pyramid pooling
       V3            Darknet     Darknet-53             36.2
                                                                                      leading to larger receptive field.
       V4            Darknet   CSPDarknet-53            43.5             Presented bag-of-freebies including the use of CIoU loss.
                                                                       First variant based in PyTorch, making it available to a wider
       V5            PyTorch   Modified CSPv7           55.8            audience. Incorporated the anchor selection processes into
                                                                                           the YOLO-v5 pipeline.
                                                                         Focused on industrial settings, presented an anchor-free
       V6            PyTorch     EfficientRep           52.5             pipeline. Presented new loss determination mechanisms
                                                                                        (VFL, DFL, and SIoU/GIoU).
                                                                         Architectural introductions included E-ELAN for faster
       V7            PyTorch     RepConvN               56.8                convergence along with a bag-of-freebies including
                                                                               RepConvN and reparameterization-planning.
                                                                       Anchor-free reducing the number of prediction boxes whilst
       V8            PyTorch      YOLO-v8               53.9           speeding up non-maximum suppression. Pending paper for
                                                                                        further architectural insights.

                                    The AP metric consists of precision-recall (PR) metrics, defining of a positive prediction
                               using Intersection over Union, and the handling of multiple object categories. AP provides
                               a balanced overview of PR based on the area under the PR curve. IoU facilitates the
                               quantification of similarity between predicted k p and ground truth k g bounding boxes as
                               expressed in (8):                                         
                                                                          area k p ∩ k g
                                                                   IoU =                                                   (8)
                                                                          area k p ∪ k g
                                    The rise of YOLO can be attributed to two factors. First, the fact that the architectural
                               composition of YOLO variants is compatible for one-stage detection and classification
                               makes it computationally lightweight with respect to other detectors. However, we feel
                               that efficient architectural composition by itself did not drive the popularity of the YOLO
                               variants, as other single-stage detectors, such as MobileNets, also serve a similar purpose.
                                    The second reason is the accessibility factor, which was introduced as the YOLO
                               variants progressed, with YOLO-v5 being the turning point. Expanding further on this
                               point, the first two variants were based on the Darknet framework. Although this pro-
                               vided a degree of flexibility, accessibility was limited to a smaller user base due to the
                               required expertise. Ultralytics, introduced YOLO-v5 based on the PyTorch framework,
                               making the architecture available for a wider audience and increasing the potential domain
                               of applications.
                                    As evident from Table 6, the migration to a more accessible framework coupled with
                               architectural reforms for improved real-time performance sky-rocketed. At present, YOLO-
                               v5 has 34.7 k stars, a significant lead compared to its predecessors. From implementation,
                               YOLO-v5 only required the installation of lightweight python libraries. The architectural
                               reforms indicated that the model training time was reduced, which in turn reduced the ex-
                               perimentation cost attributed to the training process, i.e., GPU utilization. For deployment
                               and testing purposes, researchers have several routes, such as individual/batch images,
                               video/webcam feeds, in addition to simple weight conversion to ONXX weights for edge
                               device deployment.
Machines 2023, 11, 677                                                                                            21 of 25

                         Table 6. GitHub popularity comparison.

                                          YOLO Variant                                       Stars (K)
                                               V3                                               9.3
                                               V4                                              20.2
                                               V5                                              34.7
                                               V6                                               4.6
                                               V7                                               8.4
                                               V8                                               2.9

                         4.2. YOLO and Industrial Defect Detection
                               Manifestations of the fourth industrial revolution can be observed at present in an
                         ad-hoc manner, spanning across various industries. With respect to the manufacturing
                         industry, this revolution can be targeted at the quality inspection processes, which are
                         vital for assuring efficiency and retaining client satisfaction. When focusing on surface
                         defect detection, as alluded to earlier, the inspection requirements can be more stringent
                         as compared to other applications. This is due to many factors, such as the fact that the
                         defects may be extremely small, requiring external spectral imaging to expose defects prior
                         to classification and due to the fact that the operational setting of the production line may
                         only provide a small-time window within which inference must be carried out.
                               Considering the stringent requirements outlined above and benchmarking against the
                         principles of YOLO family of variants, forms the conclusion that the YOLO variants have the
                         potential to address both real-time, constrained deployment and small-scale defect detec-
                         tion requirements of industrial-based surface defect detection. YOLO variants have proven
                         real-time compliance in several industrial environments as shown in [81,84,85,90,95]. An
                         interesting observation arising from the industrial literature reviewed is the ability for users
                         to modify the internal modules of YOLO variants in order to take care of their specific ap-
                         plication needs without compromising on real-time compliance, for example [81,87,91,92],
                         introducing attention-mechanisms for accentuation of defective regions.
                               An additional factor, found within the later YOLO variants is sub-variants for each
                         base architecture, i.e., for YOLO-v5 variants including YOLO-v5-S/M/L, this corresponds
                         to different computational loads with respect to the number of parameters. This flexibility
                         enables researchers to consider a more flexible approach with the architecture selection
                         criteria based on the industrial requirements, i.e., if real-time inference is required with less
                         emphasis on optimal mAP, a lightweight variant can be selected, such as YOLO-v5-small
                         rather than YOLO-v5-large.

                         5. Conclusions
                              In conclusion, this work is the first of its type focused on documenting and reviewing
                         the evolution of the most prevalent single-stage object detector within the computer vision
                         domain. The review presents the key advancements of each variant, followed by imple-
                         mentation of YOLO architectures within various industrial settings focused on surface
                         automated real-time surface defect detection.
                              From the review, it is clear as the YOLO variants have progressed, latter versions in
                         particular, YOLO-v5 has focused on constrained edge deployment, a key requirement for
                         many manufacturing applications. Due to the fact that there is no copyright and patent
                         restrictions, research anchored around the YOLO architecture, i.e., real-time, lightweight,
                         accurate detection, can be conducted by any individual or research organization, which has
                         also contributed to the prevalence of this variant.
                              With YOLO-v8 released in January 2023, showing promising performance with respect
                         to throughput and computational load requirements, it is envisioned that 2023 will see
                         more variants released by previous or new authors focused on improving the deployment
                         capacity of the architectures with respect to constrained deployment environments.
                              With research organizations, such as Ultralytics and Meituan Technical Team taking
                         a keen interest in the development of YOLO architectures with a focus on edge-friendly
Machines 2023, 11, 677                                                                                                         22 of 25

                                  deployment, we anticipate further technological advancements in the architectural footprint
                                  of YOLO. To cater for constrained deployment, these advancements will need to focus on
                                  energy conservation whilst maintaining high inference rates. Furthermore, we envision
                                  the proliferation of YOLO architectures into production facilities to help with quality
                                  inspection pipelines as well as providing stimulus for innovative products as demonstrated
                                  by [96] with an automated pallet racking inspection solution. Along with integration
                                  into a diverse set of hardware and IoT devices, YOLO has the potential to tap into new
                                  domains where computer vision can assist in enhancing existing processes whilst requiring
                                  limited resources.

                                  Funding: This research received no external funding.
                                  Data Availability Statement: Not applicable.
                                  Conflicts of Interest: The authors declare no conflict of interest.

References
1.    Zhang, B.; Quan, C.; Ren, F. Study on CNN in the recognition of emotion in audio and images. In Proceedings of the 2016
      IEEE/ACIS 15th International Conference on Computer and Information Science (ICIS), Okayama, Japan, 26–29 June 2016.
      [CrossRef]
2.    Pollen, D.A. Explicit neural representations, recursive neural networks and conscious visual perception. Cereb. Cortex 2003, 13,
      807–814. [CrossRef] [PubMed]
3.    Using artificial neural networks to understand the human brain. Res. Featur. 2022. [CrossRef]
4.    Improvement of Neural Networks Artificial Output. Int. J. Sci. Res. (IJSR) 2017, 6, 352–361. [CrossRef]
5.    Dodia, S.; Annappa, B.; Mahesh, P.A. Recent advancements in deep learning based lung cancer detection: A systematic review.
      Eng. Appl. Artif. Intell. 2022, 116, 105490. [CrossRef]
6.    Ojo, M.O.; Zahid, A. Deep Learning in Controlled Environment Agriculture: A Review of Recent Advancements, Challenges and
      Prospects. Sensors 2022, 22, 7965. [CrossRef] [PubMed]
7.    Jarvis, R.A. A Perspective on Range Finding Techniques for Computer Vision. IEEE Trans. Pattern Anal. Mach. Intell. 1983, PAMI-5,
      122–139. [CrossRef]
8.    Hussain, M.; Bird, J.; Faria, D.R. A Study on CNN Transfer Learning for Image Classification. 11 August 2018. Available online:
      https://research.aston.ac.uk/en/publications/a-study-on-cnn-transfer-learning-for-image-classification (accessed on 1 January
      2023).
9.    Yang, R.; Yu, Y. Artificial Convolutional Neural Network in Object Detection and Semantic Segmentation for Medical Imaging
      Analysis. Front. Oncol. 2021, 11, 638182. [CrossRef]
10.   Haupt, J.; Nowak, R. Compressive Sampling vs. Conventional Imaging. In Proceedings of the 2006 International Conference on
      Image Processing, Las Vegas, NV, USA, 26–29 June 2006; pp. 1269–1272. [CrossRef]
11.   Gu, J.; Wang, Z.; Kuen, J.; Ma, L.; Shahroudy, A.; Shuai, B.; Liu, T.; Wang, X.; Wang, G.; Cai, J.; et al. Recent advances in
      convolutional neural networks. Pattern Recognit. 2018, 77, 354–377. [CrossRef]
12.   Perez, H.; Tah, J.H.M.; Mosavi, A. Deep Learning for Detecting Building Defects Using Convolutional Neural Networks. Sensors
      2019, 19, 3556. [CrossRef]
13.   Hussain, M.; Al-Aqrabi, H.; Hill, R. PV-CrackNet Architecture for Filter Induced Augmentation and Micro-Cracks Detection
      within a Photovoltaic Manufacturing Facility. Energies 2022, 15, 8667. [CrossRef]
14.   Hussain, M.; Dhimish, M.; Holmes, V.; Mather, P. Deployment of AI-based RBF network for photovoltaics fault detection
      procedure. AIMS Electron. Electr. Eng. 2020, 4, 1–18. [CrossRef]
15.   Hussain, M.; Al-Aqrabi, H.; Munawar, M.; Hill, R.; Parkinson, S. Exudate Regeneration for Automated Exudate Detection in
      Retinal Fundus Images. IEEE Access 2022. [CrossRef]
16.   Hussain, M.; Al-Aqrabi, H.; Hill, R. Statistical Analysis and Development of an Ensemble-Based Machine Learning Model for
      Photovoltaic Fault Detection. Energies 2022, 15, 5492. [CrossRef]
17.   Singh, S.A.; Desai, K.A. Automated surface defect detection framework using machine vision and convolutional neural networks.
      J. Intell. Manuf. 2022, 34, 1995–2011. [CrossRef]
18.   Weichert, D.; Link, P.; Stoll, A.; Rüping, S.; Ihlenfeldt, S.; Wrobel, S. A review of machine learning for the optimization of
      production processes. Int. J. Adv. Manuf. Technol. 2019, 104, 1889–1902. [CrossRef]
19.   Wang, J.; Ma, Y.; Zhang, L.; Gao, R.X.; Wu, D. Deep learning for smart manufacturing: Methods and applications. J. Manuf. Syst.
      2018, 48, 144–156. [CrossRef]
20.   Weimer, D.; Scholz-Reiter, B.; Shpitalni, M. Design of deep convolutional neural network architectures for automated feature
      extraction in industrial inspection. CIRP Ann. 2016, 65, 417–420. [CrossRef]
21.   Kusiak, A. Smart manufacturing. Int. J. Prod. Res. 2017, 56, 508–517. [CrossRef]
Machines 2023, 11, 677                                                                                                                23 of 25

22.   Yang, J.; Li, S.; Wang, Z.; Dong, H.; Wang, J.; Tang, S. Using Deep Learning to Detect Defects in Manufacturing: A Comprehensive
      Survey and Current Challenges. Materials 2020, 13, 5755. [CrossRef]
23.   Soviany, P.; Ionescu, R.T. Optimizing the Trade-Off between Single-Stage and Two-Stage Deep Object Detectors using Image
      Difficulty Prediction. In Proceedings of the 2018 20th International Symposium on Symbolic and Numeric Algorithms for
      Scientific Computing (SYNASC), Timisoara, Romania, 20–23 September 2018. [CrossRef]
24.   Du, L.; Zhang, R.; Wang, X. Overview of two-stage object detection algorithms. J. Phys. Conf. Ser. 2020, 1544, 012033. [CrossRef]
25.   Sultana, F.; Sufian, A.; Dutta, P. A Review of Object Detection Models Based on Convolutional Neural Network. In Advances in
      Intelligent Systems and Computing; Springer: Singapore, 2020; pp. 1–16. [CrossRef]
26.   Liu, W.; Anguelov, D.; Erhan, D.; Szegedy, C.; Reed, S.; Fu, C.Y.; Berg, A.C. SSD: Single shot multibox detector. In Proceedings of
      the Computer Vision—ECCV 2016, Amsterdam, The Netherlands, 11–14 October 2016; pp. 21–37. [CrossRef]
27.   Fu, C.Y.; Liu, W.; Ranga, A.; Tyagi, A.; Berg, A.C. DSSD: Deconvolutional Single Shot Detector. arXiv 2017, arXiv:1701.06659.
28.   Cheng, X.; Yu, J. RetinaNet with Difference Channel Attention and Adaptively Spatial Feature Fusion for Steel Surface Defect
      Detection. IEEE Trans. Instrum. Meas. 2020, 70, 2503911. [CrossRef]
29.   Redmon, J.; Divvala, S.; Girshick, R.; Farhadi, A. You Only Look Once: Unified, Real-Time Object Detection. In Proceedings of the
      2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 27–30 June 2016; pp. 779–788.
      [CrossRef]
30.   Wang, Z.J.; Turko, R.; Shaikh, O.; Park, H.; Das, N.; Hohman, F.; Kahng, M.; Chau, D.H.P. CNN Explainer: Learning Convolutional
      Neural Networks with Interactive Visualization. IEEE Trans. Vis. Comput. Graph. 2020, 27, 1396–1406. [CrossRef] [PubMed]
31.   Krizhevsky, A.; Sutskever, I.; Hinton, G.E. Imagenet classification with deep convolutional neural networks. Commun. ACM 2017,
      60, 84–90. [CrossRef]
32.   Simonyan, K.; Zisserman, A. Very Deep Convolutional Networks for Large-Scale Image Recognition. arXiv 2014, arXiv:1409.1556.
33.   Szegedy, C.; Liu, W.; Jia, Y.; Sermanet, P.; Reed, S.; Anguelov, D.; Rabinovich, A. Going deeper with convolutions. In Proceedings
      of the Conference on Computer Vision and Pattern Recognition, Boston, MA, USA, 12 June 2015.
34.   He, K.; Zhang, X.; Ren, S.; Sun, J. Deep residual learning for image recognition. In Proceedings of the Conference on Computer
      Vision and Pattern Recognition, Las Vegas, NV, USA, 30 June 2016.
35.   Girshick, R.; Donahue, J.; Darrell, T.; Malik, J. Region-Based Convolutional Networks for Accurate Object Detection and
      Segmentation. IEEE Trans. Pattern Anal. Mach. Intell. 2015, 38, 142–158. [CrossRef]
36.   Girshick, R. Fast R-CNN. In Proceedings of the International Conference on Computer Vision, Santiago, Chile, 7–13 December
      2015.
37.   Ren, S.; He, K.; Girshick, R.; Sun, J. Faster R-CNN: Towards real-time object detection with region proposal networks. Trans.
      Pattern Anal. Mach. Intell. 2017, 39, 1137–1149. [CrossRef]
38.   Vidyavani, A.; Dheeraj, K.; Reddy, M.R.M.; Kumar, K.N. Object Detection Method Based on YOLOv3 using Deep Learning
      Networks. Int. J. Innov. Technol. Explor. Eng. 2019, 9, 1414–1417. [CrossRef]
39.   Everingham, M.; Van Gool, L.; Williams, C.K.I.; Winn, J.; Zisserman, A. The Pascal Visual Object Classes (VOC) Challenge. Int. J.
      Comput. Vis. 2009, 88, 303–338. [CrossRef]
40.   Shetty, S. Application of Convolutional Neural Network for Image Classification on Pascal VOC Challenge 2012 dataset.
      arXiv 2016, arXiv:1607.03785.
41.   Felzenszwalb, P.F.; Girshick, R.B.; McAllester, D.; Ramanan, D. Object Detection with Discriminatively Trained Part-Based Models.
      IEEE Trans. Pattern Anal. Mach. Intell. 2009, 32, 1627–1645. [CrossRef] [PubMed]
42.   Chang, Y.-L.; Anagaw, A.; Chang, L.; Wang, Y.C.; Hsiao, C.-Y.; Lee, W.-H. Ship Detection Based on YOLOv2 for SAR Imagery.
      Remote Sens. 2019, 11, 786. [CrossRef]
43.   Liao, Z.; Carneiro, G. On the importance of normalisation layers in deep learning with piecewise linear activation units. In
      Proceedings of the 2016 IEEE Winter Conference on Applications of Computer Vision (WACV), New York, NY, USA, 7–10 March
      2016. [CrossRef]
44.   Garbin, C.; Zhu, X.; Marques, O. Dropout vs. batch normalization: An empirical study of their impact to deep learning. Multimed.
      Tools Appl. 2020, 79, 12777–12815. [CrossRef]
45.   Li, G.; Jian, X.; Wen, Z.; AlSultan, J. Algorithm of overfitting avoidance in CNN based on maximum pooled and weight decay.
      Appl. Math. Nonlinear Sci. 2022, 7, 965–974. [CrossRef]
46.   Deng, J.; Dong, W.; Socher, R.; Li, L.J.; Li, K.; Fei-Fei, L. Imagenet: A large-scale hierarchical image database. In Proceedings of the
      2009 IEEE Conference on Computer Vision and Pattern Recognition, Miami, FL, USA, 20–25 June 2009.
47.   Xue, J.; Cheng, F.; Li, Y.; Song, Y.; Mao, T. Detection of Farmland Obstacles Based on an Improved YOLOv5s Algorithm by Using
      CIoU and Anchor Box Scale Clustering. Sensors 2022, 22, 1790. [CrossRef]
48.   Ahmed, M.; Seraj, R.; Islam, S.M.S. The k-means Algorithm: A Comprehensive Survey and Performance Evaluation. Electronics
      2020, 9, 1295. [CrossRef]
49.   Redmon, J. Darknet: Open Source Neural Networks in C. 2013. Available online: https://pjreddie.com/darknet (accessed on
      1 January 2023).
50.   Furusho, Y.; Ikeda, K. Theoretical analysis of skip connections and batch normalization from generalization and optimization
      perspectives. APSIPA Trans. Signal Inf. Process. 2020, 9, e9. [CrossRef]
Machines 2023, 11, 677                                                                                                              24 of 25

51.   Machine-Learning System Tackles Speech and Object Recognition. Available online: https://news.mit.edu/machine-learning-
      image-object-recognition-918 (accessed on 1 January 2023).
52.   Bochkovskiy, A.; Wang, C.Y.; Liao HY, M. YOLOv4: Optimal Speed and Accuracy of Object Detection. arXiv 2020,
      arXiv:2004.10934.
53.   Tan, M.; Le, Q. EfficientNet: Rethinking model scaling for convolutional neural networks. In Proceedings of the International
      Conference on Machine Learning (ICML), Long Beach, CA, USA, 9–15 June 2019.
54.   Huang, G.; Liu, Z.; Van Der Maaten, L.; Weinberger, K.Q. Densely connected convolutional networks. In Proceedings of the IEEE
      Conference on Computer Vision and Pattern Recognition (CVPR), Honolulu, HI, USA, 21–26 July 2017; pp. 4700–4708.
55.   Lin, T.Y.; Dollár, P.; Girshick, R.; He, K.; Hariharan, B.; Belongie, S. Feature pyramid networks for object detection. In Proceedings
      of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Honolulu, HI, USA, 21–26 July 2017; pp. 2117–2125.
56.   Liu, S.; Qi, L.; Qin, H.; Shi, J.; Jia, J. Path aggregation network for instance segmentation. In Proceedings of the IEEE Conference
      on Computer Vision and Pattern Recognition (CVPR), Salt Lake City, UT, USA, 18–23 June 2018; pp. 8759–8768.
57.   He, K.; Zhang, X.; Ren, S.; Sun, J. Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition. IEEE Trans.
      Pattern Anal. Mach. Intell. 2015, 37, 1904–1916. [CrossRef]
58.   Zheng, Z.; Wang, P.; Liu, W.; Li, J.; Ye, R.; Ren, D. Distance-IoU Loss: Faster and better learning for bounding box regression. In
      Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), New York, NY, USA, 7–12 February 2020.
59.   Misra, D. Mish: A self regularized nonmonotonic neural activation function. arXiv 2019, arXiv:1908.08681.
60.   Yao, Z.; Cao, Y.; Zheng, S.; Huang, G.; Lin, S. Cross-Iteration Batch Normalization. arXiv 2020, arXiv:2002.05712.
61.   Ultralytics. YOLOv5 2020. Available online: https://github.com/ultralytics/yolov5 (accessed on 1 January 2023).
62.   Jocher, G.; Stoken, A.; Borovec, J.; Christopher, S.T.A.N.; Laughing, L.C. Ultralytics/yolov5: v4.0-nn.SiLU() Activations, Weights
      & Biases Logging, PyTorch Hub Integration. Zenodo 2021. Available online: https://zenodo.org/record/4418161 (accessed on
      5 January 2023).
63.   Lin, T.Y.; Maire, M.; Belongie, S.; Hays, J.; Perona, P.; Ramanan, D.; Zitnick, C.L. Microsoft coco: Common objects in context. In
      Proceedings of the European Conference on Computer Vision, Zurich, Switzerland, 6–12 September 2014.
64.   Tan, M.; Pang, R.; Le, Q.V. EfficientDet: Scalable and Efficient Object Detection. In Proceedings of the IEEE/CVF Conference on
      Computer Vision and Pattern Recognition, Seattle, WA, USA, 13–19 June 2020.
65.   Li, C.; Li, L.; Jiang, H.; Weng, K.; Geng, Y.; Li, L.; Wei, X. YOLOv6: A Single-Stage Object Detection Framework for Industrial
      Applications. arXiv 2022, arXiv:2209.02976.
66.   Ding, X.; Zhang, X.; Ma, N.; Han, J.; Ding, G.; Sun, J. Repvgg: Making vgg-style convnets great again. In Proceedings of the
      IEEE/CVF Conference on Computer Vision and Pattern Recognition, Nashville, TN, USA, 20–25 June 2021; pp. 13733–13742.
67.   Zhang, H.; Wang, Y.; Dayoub, F.; Sunderhauf, N. Varifocalnet: An iou-aware dense object detector. In Proceedings of the
      IEEE/CVF Conference on Computer Vision and Pattern Recognition, Nashville, TN, USA, 20–25 June 2021; pp. 8514–8523.
68.   Li, X.; Wang, W.; Wu, L.; Chen, S.; Hu, X.; Li, J.; Yang, J. Generalized focal loss: Learning qualified and distributed bounding
      boxes for dense object detection. Adv. Neural Inf. Process. Syst. 2020, 33, 21002–21012.
69.   Gevorgyan, Z. Siou loss: More powerful learning for bounding box regression. arXiv 2022, arXiv:2205.12740.
70.   Shu, C.; Liu, Y.; Gao, J.; Yan, Z.; Shen, C. Channel-wise knowledge distillation for dense prediction. In Proceedings of the
      IEEE/CVF International Conference on Computer Vision, Montreal, BC, Canada, 11–17 October 20221; pp. 5311–5320.
71.   Solawetz, J.; Nelson, J. What’s New in YOLOv6? 4 July 2022. Available online: https://blog.roboflow.com/yolov6/ (accessed on
      1 January 2023).
72.   Wang, C.Y.; Bochkovskiy, A.; Liao HY, M. YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors.
      arXiv 2022, arXiv:2207.02696.
73.   Ge, Z.; Liu, S.; Wang, F.; Li, Z.; Sun, J. YOLOX: Exceeding YOLO series in 2021. arXiv 2021, arXiv:2107.08430.
74.   Wang, C.-Y.; Yeh, I.-H.; Liao, H.-Y.M. You only learn one representation: Unified network for multiple tasks. arXiv 2021,
      arXiv:2105.04206.
75.   Wu, W.; Zhao, Y.; Xu, Y.; Tan, X.; He, D.; Zou, Z.; Ye, J.; Li, Y.; Yao, M.; Dong, Z.; et al. DSANet: Dynamic Segment AggrDSANet:
      Dynamic Segment Aggregation Network for Video-Level Representation Learning. In Proceedings of the MM ’21—29th ACM
      International Conference on Multimedia, Virtual, 20–24 October 2021. [CrossRef]
76.   Li, C.; Tang, T.; Wang, G.; Peng, J.; Wang, B.; Liang, X.; Chang, X. BossNAS: Exploring Hybrid CNN-transformers with Block-
      wisely Self-supervised Neural Architecture Search. In Proceedings of the IEEE/CVF International Conference on Computer
      Vision, Online, 11–17 October 2021. [CrossRef]
77.   Dollar, P.; Singh, M.; Girshick, R. Fast and accurate model scaling. In Proceedings of the IEEE/CVF Conference on Computer
      Vision and Pattern Recognition (CVPR), Nashville, TN, USA, 20–25 June 2021; pp. 924–932.
78.   Guo, S.; Alvarez, J.M.; Salzmann, M. ExpandNets: Linear over-parameterization to train compact convolutional networks. Adv.
      Neural Inf. Process. Syst. (NeurIPS) 2020, 33, 1298–1310.
79.   Ding, X.; Zhang, X.; Zhou, Y.; Han, J.; Ding, G.; Sun, J. Scaling up your kernels to 31 × 31: Revisiting large kernel design in CNNs.
      In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), New Orleans, LA, USA, 18–24
      June 2022.
80.   Jocher, G.; Chaurasia, A.; Qiu, J. YOLO by Ultralytics. GitHub. 1 January 2023. Available online: https://github.com/ultralytics/
      ultralytics (accessed on 12 January 2023).
Machines 2023, 11, 677                                                                                                              25 of 25

81.   Jin, R.; Niu, Q. Automatic Fabric Defect Detection Based on an Improved YOLOv5. Math. Probl. Eng. 2021, 2021, 1–13. [CrossRef]
82.   NVIDIA Jetson TX2: High Performance AI at the Edge, NVIDIA. Available online: https://www.nvidia.com/en-gb/autonomous-
      machines/embedded-systems/jetson-tx2/ (accessed on 30 January 2023).
83.   NVIDIA TensorRT. NVIDIA Developer. 18 July 2019. Available online: https://developer.nvidia.com/tensorrt (accessed on
      5 January 2023).
84.   Dlamini, S.; Kao, C.-Y.; Su, S.-L.; Kuo, C.-F.J. Development of a real-time machine vision system for functional textile fabric defect
      detection using a deep YOLOv4 model. Text. Res. J. 2021, 92, 675–690. [CrossRef]
85.   Lin, G.; Liu, K.; Xia, X.; Yan, R. An Efficient and Intelligent Detection Method for Fabric Defects based on Improved YOLOv5.
      Sensors 2022, 23, 97. [CrossRef] [PubMed]
86.   Liu, Z.; Tan, Y.; He, Q.; Xiao, Y. SwinNet: Swin Transformer Drives Edge-Aware RGB-D and RGB-T Salient Object Detection. IEEE
      Trans. Circuits Syst. Video Technol. 2021, 32, 4486–4497. [CrossRef]
87.   Zhang, M.; Yin, L. Solar Cell Surface Defect Detection Based on Improved YOLO v5. IEEE Access 2022, 10, 80804–80815. [CrossRef]
88.   Binomairah, A.; Abdullah, A.; Khoo, B.E.; Mahdavipour, Z.; Teo, T.W.; Noor, N.S.M.; Abdullah, M.Z. Detection of microcracks
      and dark spots in monocrystalline PERC cells using photoluminescene imaging and YOLO-based CNN with spatial pyramid
      pooling. EPJ Photovolt. 2022, 13, 27. [CrossRef]
89.   Sun, T.; Xing, H.; Cao, S.; Zhang, Y.; Fan, S.; Liu, P. A novel detection method for hot spots of photovoltaic (PV) panels using
      improved anchors and prediction heads of YOLOv5 network. Energy Rep. 2022, 8, 1219–1229. [CrossRef]
90.   Yang, D.; Cui, Y.; Yu, Z.; Yuan, H. Deep Learning Based Steel Pipe Weld Defect Detection. Appl. Artif. Intell. 2021, 35, 1237–1249.
      [CrossRef]
91.   Ma, Z.; Li, Y.; Huang, M.; Huang, Q.; Cheng, J.; Tang, S. A lightweight detector based on attention mechanism for aluminum strip
      surface defect detection. Comput. Ind. 2021, 136, 103585. [CrossRef]
92.   Shi, J.; Yang, J.; Zhang, Y. Research on Steel Surface Defect Detection Based on YOLOv5 with Attention Mechanism. Electronics
      2022, 11, 3735. [CrossRef]
93.   CEP, F.A. 5 Insightful Statistics Related to Warehouse Safety. Available online: www.damotech.com (accessed on 11 January 2023).
94.   Armour, R. The Rack Group. Available online: https://therackgroup.com/product/rack-armour/ (accessed on 12 January 2023).
95.   Hussain, M.; Chen, T.; Hill, R. Moving toward Smart Manufacturing with an Autonomous Pallet Racking Inspection System
      Based on MobileNetV2. J. Manuf. Mater. Process. 2022, 6, 75. [CrossRef]
96.   Hussain, M.; Al-Aqrabi, H.; Munawar, M.; Hill, R.; Alsboui, T. Domain Feature Mapping with YOLOv7 for Automated Edge-Based
      Pallet Racking Inspections. Sensors 2022, 22, 6927. [CrossRef] [PubMed]
97.   Farahnakian, F.; Koivunen, L.; Makila, T.; Heikkonen, J. Towards Autonomous Industrial Warehouse Inspection. In Proceedings of
      the 2021 26th International Conference on Automation and Computing (ICAC), Portsmouth, UK, 2–4 September 2021. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
