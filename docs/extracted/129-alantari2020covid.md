---
source_id: 129
bibtex_key: alantari2020covid
title: Fast Deep Learning Computer-Aided Diagnosis of COVID-19 Based on Digital Chest X-Ray Images
year: 2021
domain_theme: Medis
verified_pdf: 129_COVID-19 CAD dari X-Ray (Al-Antari dkk.).pdf
char_count: 157958
---

Applied Intelligence (2021) 51:2890–2907
https://doi.org/10.1007/s10489-020-02076-6

“Fast deep learning computer-aided diagnosis of COVID-19 based
on digital chest x-ray images”
Mugahed A. Al-antari 1,2           & Cam-Hao Hua
                                                       1
                                                            & Jaehun Bang
                                                                             1
                                                                                 & Sungyoung Lee
                                                                                                      1

Accepted: 9 November 2020 / Published online: 28 November 2020
# Springer Science+Business Media, LLC, part of Springer Nature 2020

Abstract
Coronavirus disease 2019 (COVID-19) is a novel harmful respiratory disease that has rapidly spread worldwide. At the end of 2019,
COVID-19 emerged as a previously unknown respiratory disease in Wuhan, Hubei Province, China. The world health organization
(WHO) declared the coronavirus outbreak a pandemic in the second week of March 2020. Simultaneous deep learning detection and
classification of COVID-19 based on the full resolution of digital X-ray images is the key to efficiently assisting patients by enabling
physicians to reach a fast and accurate diagnosis decision. In this paper, a simultaneous deep learning computer-aided diagnosis (CAD)
system based on the YOLO predictor is proposed that can detect and diagnose COVID-19, differentiating it from eight other respiratory
diseases: atelectasis, infiltration, pneumothorax, masses, effusion, pneumonia, cardiomegaly, and nodules. The proposed CAD system
was assessed via five-fold tests for the multi-class prediction problem using two different databases of chest X-ray images: COVID-19
and ChestX-ray8. The proposed CAD system was trained with an annotated training set of 50,490 chest X-ray images. The regions on
the entire X-ray images with lesions suspected of being due to COVID-19 were simultaneously detected and classified end-to-end via
the proposed CAD predictor, achieving overall detection and classification accuracies of 96.31% and 97.40%, respectively. Most test
images from patients with confirmed COVID-19 and other respiratory diseases were correctly predicted, achieving average intersection
over union (IoU) greater than 90%. Applying deep learning regularizers of data balancing and augmentation improved the COVID-19
diagnostic performance by 6.64% and 12.17% in terms of the overall accuracy and the F1-score, respectively. It is feasible to achieve a
diagnosis based on individual chest X-ray images with the proposed CAD system within 0.0093 s. Thus, the CAD system presented in
this paper can make a prediction at the rate of 108 frames/s (FPS), which is close to real-time. The proposed deep learning CAD system
can reliably differentiate COVID-19 from other respiratory diseases. The proposed deep learning model seems to be a reliable tool that
can be used to practically assist health care systems, patients, and physicians.

Highlights of the Article
A fast deep learning computer-aided diagnosis (CAD) based on the
YOLO predictor is proposed to simultaneously detect and diagnose
COVID-19 respiratory disease from the entire chest X-ray (CXR) images.
The COVID-19 respiratory disease is automatically detected and classi-
fied end-to-end with overall detection and classification accuracies of
96.31% and 97.40%, respectively.
The proposed deep learning CAD system is able to detect and classify
COVID-19 or other respiratory diseases in a single X-ray image within
0.0093 seconds.
The presented CAD system is able to predict at least 108 frames/sec at the
real-time of prediction.

* Mugahed A. Al-antari                                                       1
                                                                                 Department of Computer Science and Engineering, College of
  en.mualshz@oslab.khu.ac.kr                                                     Software, Kyung Hee University, 1732, Deogyeong-daero,
                                                                                 Giheung-gu, Yongin-si, Gyeonggi-do 17104, Republic of Korea
* Jaehun Bang
  jhb@oslab.khu.ac.kr
                                                                             2
                                                                                 Department of Biomedical Engineering, Sana’a Community College,
* Sungyoung Lee
                                                                                 Sana’a, Republic of Yemen
  sylee@oslab.khu.ac.kr
    Cam-Hao Hua
    hao.hua@oslab.khu.ac.kr
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                          2891

Keywords COVID-19 . Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) . Respiratory diseases . Artificial
intelligence (AI), Deep learning . Diagnosis

1 Introduction                                                              CT scans or X-rays should be routinely obtained in addition to
                                                                            RT-PCR results to improve the accuracy of the diagnosis of
Coronavirus disease 2019 (COVID-19) has recently become                     COVID-19 [8]. However, the large number of patients who
an unprecedented public health crisis worldwide [1]. At the                 test positive for SARS-CoV-2 makes the use of regular
end of December 2019, patients with a previously unknown                    screening on a daily basis challenging for physicians. Thus,
respiratory disease were identified in Wuhan, Hubei Province,               on March 16, 2020,the United States administration encour-
China [2]. By January 25, 2020, the diagnosis of COVID-19                   aged experts and researchers to employ artificial intelligence
had been confirmed in at least 1975 more patients since the                 (AI) techniques to combat the COVID-19 pandemic [1].
first patient was hospitalized on December 12, 2019. COVID-                 Currently, experts have started to use machine learning and
19 caused by a new coronavirus named severe acute respira-                  deep learning technologies to develop CAD systems to assist
tory syndrome coronavirus 2 (SARS-CoV-2) [2, 3]. The typ-                   physicians in increasing the accuracy of the diagnosis of
ical symptoms of COVID-19 include fever, shortness of                       COVID-19 [1, 8]. In the last few years, the use of deep learn-
breath, dizziness, cough, headache, sore throat, fatigue, and               ing methods as adjunct screening tools for physicians has
muscle pain [2–4]. After the first case of COVID-19 was                     attracted a great deal of interest. Deep learning CAD systems
discovered in Wuhan, the virus has rapidly spread to 216                    have been shown to be capable and reliable, and promising
countries worldwide, largely due to human-to-human trans-                   diagnostic performance has been achieved using the entire
mission of the virus early in the clinical course [1]. The                  image without user intervention [9, 10]. The use of a deep
COVID-19 pandemic has imposed substantial demands on                        learning CAD system could assist physicians and improve
the public health systems, health infrastructure, and econo-                the accuracy of the diagnosis of COVID-19 [1]. Deep learning
mies of most countries worldwide [5]. Because the total num-                CAD systems have been successfully applied to predict dif-
ber of people infected by SARS-CoV-2 has increased rapidly,                 ferent medical problems, such as breast cancer [9, 10], skin
the capacity of healthcare systems (i.e., beds, ventilators, care           cancer [11, 12], and respiratory disease, using digital X-ray
providers, masks, etc.) is insufficient to meet the demand. Due             images [8]. The rapid spread of the COVID-19 pandemic and
to the rapid transmission of SARS-CoV-2 from person to per-                 the consequent death of humans worldwide makes it neces-
son, millions of people have been infected, more than four                  sary to apply deep learning technologies to develop CAD
billion people have been instructed to remain at home, and                  systems that can improve the diagnostic performance. This
many people have lost their jobs [1, 2, 5]. Severe COVID-                   need was the motivation for developing a deep learning
19 has caused deaths worldwide [6]. As reported by the world                CAD system to diagnose COVID-19 based on entire digital
health organization (WHO) on November 17, 2020 [6], the                     X-ray images.
numbers of patients with confirmed cases of COVID-19, re-                       In this paper, our contributions to the diagnosis of COVID-
covered COVID-19 patients, and non-surviving COVID-19                       19 based on digital X-ray images are as follows. First, a si-
patients were 55.4M, 38.6M, and 1.3M, respectively.                         multaneous deep learning CAD system that uses the YOLO
Moreover, education systems have been negatively affected                   predictor was adopted to detect and diagnose COVID-19 di-
by the COVID-19 pandemic, and schools and universities                      rectly from entire chest X-ray images. Second, COVID-19 is
have switch to remote learning.                                             differentiated from eight other respiratory diseases in a
    To date, the most widely used screening tool for the detec-             multiclass recognition problem. Third, deep learning
tion and diagnosis of COVID-19 has been real-time reverse-                  regularizations of data balancing, augmentation, and transfer
transcription polymerase chain reaction (RT-PCR) [7].                       learning were also applied to improve the overall diagnostic
Radiological imaging techniques such as chest digital X-ray                 performance for COVID-19. Finally, our proposed CAD sys-
(CXR) and computed tomography (CT) are the standard                         tem was trained and optimized with five-fold tests using data
screening tools used to detect and diagnose chest respiratory               from two different digital X-ray datasets, COVID-19 [13, 14]
diseases early in the clinical course, including COVID-19 [1,               and ChestX-ray8 [15]. The outcomes of this study can be used
8]. Due to the low sensitivity of RT-PCR, radiological images               to guide other researchers when developing novel deep learn-
are also used for diagnostic purposes in patients with symp-                ing CAD frameworks to accurately diagnose COVID-19.
toms of respiratory diseases. Although the CT is the gold                       The objective of this work was to provide a practical and
standard, primary chest digital X-ray systems are still useful              feasible CAD system based on AI that can help physicians,
because they are faster, deliver a lower dose of radiation, are             patients, healthcare systems, and hospitals by facilitating the
less expensive, and are more widely available [4, 8]. Indeed,               faster and more accurate diagnosis of COVID-19.
2892                                                                                                           M. A. Al-antari et al.

   The rest of this paper is organized as follows. A review of     Net outperformed VGG-16 and ResNet-50, with positive
the relevant literature is presented in Section 2. The technical   predictive values (PPVs) of 90.50%, 91.30%, and 98.9%
aspects of the deep learning CAD-based YOLO system are             for healthy, pneumonia, and COVID-19, respectively.
detailed in Section 3. The results of the experiment with          Hamdan et al. [19] presented a deep learning COVIDX-
COVID-19 are reported and discussed in Sections 4 and 5.           Net model that can be used to distinguish between
Finally, the most important findings of this work are summa-       COVID-19 patients and healthy individuals based on 50
rized in Section 6.                                                digital chest X-ray images. They used seven well-
                                                                   established deep networks as feature extractors and com-
                                                                   pared their classification results. Compared with other deep
2 Related works                                                    learning models, VGG-19 and DensNet201 had the highest
                                                                   diagnostic performance value of 90%. Apostolopoulos
Starting in 2020, after the discovery of COVID-19, some            et al. [20] tested the ability of five well-established deep
artificial intelligence (AI) systems based on deep learning        learning networks to detect COVID-19 on digital X-ray
have been employed to detect COVID-19 on digital X-ray             images. They used three classifications, namely, normal,
and CT images. In [16], Oh et al. presented a patch-based          pneumonia, and COVID-19, and they achieved the best
deep learning CAD system consisting of segmentation and            overall classification accuracy of 93.48% with VGG-19.
classification stages that could identify COVID-19 based           Additionally, they tested all five deep learning models with
on CXR images. With regard to segmentation, FC-                    regard to the binary classification problem (i.e., COVID-19
DenseNet103 was used to segment and extract the full lung          against non-COVID-19), and they achieved the highest ac-
regions from the entire CXR images. With regard to classi-         curacy of 98.75% with VGG-19. Sakshy et al. [21] pro-
fication, multiple random patches (i.e., regions of interest)      posed a three-phase deep learning detection model to detect
were extracted from the segmented lung regions for use as          COVID-19 on CT images with a binary classification task.
the input for the classification DL model. They used CXR           They used data augmentation, transfer learning, and abnor-
images from multiple patients who were healthy and pa-             mality localization with different backend deep learning
tients who were diagnosed with bacterial pneumonia, tuber-         networks: ResNet18, ResNet50, ResNet101, and
culosis, and viral pneumonia associated with COVID-19.             SqueezeNet. They concluded that the pre-trained
Diagnostic accuracies of 84.40% and 88.9% were achieved            ResNet18 using the transfer learning strategy achieved the
for the F1-score and overall accuracy, respectively. Ozturk        best diagnostic results of 99.82%, 97.32%, and 99.40% in
et al. [8] proposed the deep learning DarkCovidNet that can        the training, validation, and test sets, respectively. Khan
automatically detect COVID-19 based on digital chest X-            et al. [22] proposed a deep learning convolutional neural
ray images. They developed their model using 17                    network (i.e., CoroNet) that could be used to diagnose
convolutional layers with the aim of achieving binary clas-        COVID-19 as a multiclass problem based on whole chest
sification (i.e., COVID-19 and no finding) and multinomial         X-ray images. They achieved an overall accuracy of 89.6%
classification (i.e., COVID-19, no finding, and pneumonia)         for the identification of COVID-19 from among bacterial
diagnoses. They achieved overall classification accuracies         pneumonia, viral pneumonia, and normal images. Narin
of 98.08% and 87.02% for the binary and multinomial clas-          et al. [23] compared the classification performances of three
sifications, respectively. Fan et al. [17] proposed a deep         different deep learning convolutional neural networks (i.e.,
learning model called Inf-Net that can be used to identify         ResNet-50, InceptionV3, and InceptionResNetV2) using
or segment suspicious regions indicative of COVID-19 on            chest X-ray images. They evaluated the ability of those
chest CT images. They used a parallel partial decoder to           three models to differentiate patients with COVID-19 from
generate the global representation of the final segmented          individuals without COVID-19, and they achieved the best
maps. After that, they used implicit reverse attention and         classification accuracy of 98% using ResNet-50. Ardakani
explicit edge attention to enhance the segmented bound-            et al. [24] evaluated ten different well-established DL
aries. They achieved segmentation accuracies of 73.90%             models to diagnose COVID-19 on CT scans in routine clin-
and 89.40% with regard to Dice and the enhanced-                   ical practice. They differentiated between COVID-19 and
alignment index, respectively. In May 2020, Wang et al.            non-COVID-19 with a binary classification task, and they
[18] proposed COVID-Net, which was based on a deep                 achieved the best diagnostic result using the ResNet-101
learning model and could differentiate patients with               and Xception DL networks, with an overall accuracy of
COVID-19 from healthy individuals and those with pneu-             99.40%. Pereira et al. [7] presented a classification scheme
monia based on digital X-ray images. The classification            based on well-known texture descriptors and a
performance of their model was compared with the those             convolutional neural network (CNN). They used a resam-
of VGG-19 and ResNet-50 using the same database of dig-            pling algorithm to balance the training dataset for a
ital X-ray images [18]. The authors concluded that COVID-          multiclass classification problem. Their model achieved
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                        2893

an average F1 score of 65%. Moreover, comprehensive sur-                    structure; the system has been validated and can simultaneous-
vey studies on deep learning applications pertaining to                     ly detect and classify COVID-19. Figure 1 is a conceptual
COVID-19 are presented in [25, 26]. Such deep learning                      diagram of the proposed CAD system.
methods have been employed to diagnose COVID-19 on
entire X-ray images. This is due to the lack of X-ray images                3.1 Digital X-ray images dataset
with annotated regions of suspected lesions. However, it is
not practical to use the entire X-ray image to achieve a                    We used two different digital chest X-ray databases, namely,
reliable diagnosis of COVID-19 [27]. Thus, the detection                    COVID-19 [13, 14] and ChestX-ray8 [15]. The data distribu-
of suspicious regions specific to individual respiratory dis-               tions for the two datasets are shown in Fig. 2.
eases is critical for achieving a more accurate diagnosis
because it could be used to derive more representative deep
                                                                            3.1.1 COVID-19 dataset
features of the abnormalities. To our knowledge, this is the
regional convolutional deep learning CAD system devel-
                                                                            The COVID-19 dataset used in this study was collected
oped to simultaneously detect COVID-19 and differentiate
                                                                            from two different publicly available sources. First, we
it from among other respiratory diseases based on chest X-
                                                                            used the digital X-ray images from patients with
ray images. The automatic detection of COVID-19 is a ma-
                                                                            COVID-19 collected by Cohen et al. [13] from different
jor challenge for researchers. Our previous promising diag-
                                                                            public sources, hospitals and radiologists. These images
nostic results from the breast cancer diagnosis CAD system
                                                                            are publicly available to help expert researchers develop
using the YOLO predictor [9, 10] have encouraged us to
                                                                            AI based on deep learning approaches to improve the
employ a similar system to detect and classify COVID-19,
                                                                            diagnosis and understanding of COVID-19. Researchers
with the aim of enhancing the diagnosis of COVID-19.
                                                                            from different countries try to constantly update these
                                                                            datasets and add more X-ray images. In this study, we
                                                                            used the available X-ray images acquired from 125 pa-
3 Material and methods                                                      tients with COVID-19 (82 males and 43 females).
                                                                            Unfortunately, complete metadata were not yet available
Deep learning computer-aided diagnosis (CAD) based on the                   for all these patients. Age was provided for only 26 pa-
YOLO predictor was used to simultaneously detect COVID-                     tients; the average age was 55 years. Second, we used
19 and differentiate it from eight other respiratory diseases:              digital X-ray images from patients with COVID-19 col-
atelectasis, infiltration, pneumothorax, masses, effusion,                  lected by a research team from Qatar University [14]. All
pneumonia, cardiomegaly, and nodules. The CAD system                        these images are publicly available in portable network
presented in this paper has a unique deep learning framework                graphic (png) file format with a size of 1024 × 1024
                                                                                     Potential Detected
                                                                                     Suspicious regions

          Input Digital X-ray                                                                                     The final
                image                                                                                         Prediction Results
                                          Deep Learning CAD System

                                                                                    Map of Conditional
                                                                                    Class Probabilities

                                        Deep feature Fully   Confidence
                                         Extraction Connected Model
                                         via CNN     Layers   Output

Fig. 1 Schematic diagram of the proposed deep learning CAD system based on the YOLO predictor
2894                                                                                                                                             M. A. Al-antari et al.

                                          240
                                                              Training (70%)                Testing (20%)             Validation (10%)

                 Number of X-ray images
                                          180

                                          120

                                          60

                                           0
                                                                             Pneumothor                                   Cardiomega
                                                Atelectasis   Infiltration                Mass     Effusion   Pneumonia                Nodule   COVID_19
                                                                                 ax                                           ly
            Training (70%)                         126            86             69        60        107         84          102         55       228
            Testing (20%)                           36            25            20         17         31         24          29          16        65
            Validation (10%)                        18            12            10         9          15         12          15          8         33

Fig. 2 Data distribution over all nine classes of respiratory diseases. The datasets for each classes were randomly split into 70%, 20%, and 10% for the
training, testing, and validation sets, respectively

pixels. This dataset is publicly provided for researchers to                                     3.1.2 ChestX-ray8
develop useful and impactful AI models with the aim of
addressing the COVID-19 crisis. The metadata were not                                            The ChestX-ray8 [15] dataset is the most frequently used and
yet available for all patients with COVID-19. In this                                            widely accessible medical imaging examination dataset avail-
study, we used all available digital X-ray images from                                           able for eight different respiratory diseases: atelectasis, infil-
201 patients with COVID-19. Thus, a total of 326 CXR                                             tration, pneumothorax, masses, effusion, pneumonia,
images were collected and used to develop the proposed                                           cardiomegaly, and nodules. In this study, we used all CXR
CAD system. The classification labels for these images                                           images with ground truth (GT) information involving the dis-
are publicly available, but the information regarding the                                        ease class label and the disease localization information as a
GT localization (i.e., bounding box) is not yet available                                        labeled bounding box. The information pertaining to the GT
for either COVID-19 dataset. This is because the CXR                                             bounding box (i.e., the starting point of the box (x,y), width
images are rapidly collected in the context of the pandem-                                       (w), and height (h)) for each image is publicly available in the
ic. To locate the abnormalities, we asked two expert radi-                                       XML file [15]. As shown in Fig. 2, a total of 984 frontal views
ologists to annotate the abnormalities (i.e., lesions associ-                                    of CXR images were used, which were representative of eight
ated with COVID-19) localizations in a parallel manner.                                          different respiratory diseases. These images were accurately
Since some CXR images were provided by the authors                                               converted from DICOM format into ‘.png’ file format with a
with some small white/black arrows, as shown in                                                  size of 1024 × 1024 pixels. Figure. 4 shows an example of an
Figure 3a-c, showing the localization of the COVID-19                                            X-ray image for each disease class with the associated GT
lesions, we compared the experts’ opinion with the                                               information.
existing annotations and marked the suspected lesions
with a rectangle. Each bounding box GT was determined                                            3.2 Data preparation: Training, validation, and testing
by the coordinates corresponding to the width (w), height
(h), and center (x, y) of the abnormality. Figure. 3 shows                                       To fine-tune and evaluate the proposed CAD system, the
some examples of COVID-19 lesions with the associated                                            COVID-19 [13, 14] and ChestX-ray8 [15] datasets were
GT information.                                                                                  used. As shown in Fig. 2, the chest X-ray images for

Fig. 3 Example cases of COVID-19 in different patients. The ground-truth (GT) information of the bounding box (i.e., green) for each case is
superimposed on the original chest X-ray (CXR) image. The GT information was determined by expert physicians
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                 2895

Fig. 4 Example cases of eight common respiratory diseases in different         nodule. The ground-truth (GT) information of the bounding box (i.e.,
patients from the ChestX-ray8 dataset [15]: a atelectasis, b infiltration, c   green) for each case is superimposed on the original image
pneumothorax, d mass, e effusion, f pneumonia, g cardiomegaly, and h

each disease class were randomly divided as follows:                           3.2.1 Balancing and augmentation strategies for the training
70% in the training dataset, 20% in the evaluation                             dataset
dataset, and 10% in the validation dataset [9, 10]. The
hypertrainable parameters of the proposed deep learning                        Data balancing and augmentation strategies were applied to
system were selected via the training process using the                        enlarge the size of the training dataset, avoid overfitting, and
training and validation datasets. After that, the final per-                   accelerate the learning process [9, 10]. These practical solu-
formance of the proposed CAD system was assessed                               tions were successfully applied to address the challenge of
using the evaluation set. Meanwhile, our proposed                              small datasets of annotated medical images [9, 10]. During
CAD system was assessed using five-fold tests in the                           training, each mini-batch included an almost equal number
training, validation, and evaluation datasets. These sets                      of digital X-ray images for each disease class [29, 30]. This
were generated by stratified partitioning to ensure equal                      was to avoid overfitting and prevent the performance of the
testing of each X-ray image and to avoid system bias                           deep learning model from being biased towards the disease
error. It is important to use k-fold cross-validation to                       class with the largest number of images (i.e., COVID-19). To
develop a robust, reliable, and efficient CAD system,                          balance the training sets and avoid having a majority of im-
especially given the small sizes of medical datasets                           ages related to COVID-19, the training images from the eight
[9–11]. In addition, to prevent the development of bias                        disease classes in the ChestX-ray8 dataset were flipped twice
in the proposed prediction model during the learning                           (i.e., left-right and up-down), generating 1378 chest X-ray
process due to an unbalanced training set, we used the                         images. Thus, the total number of images in all disease classes
following techniques. First, the training set for each                         in the training set after balancing was 2295 (i.e., 917 original
mini-batch was automatically shuffled. Second, a weight-                       images from all disease classes including COVID-19 and
ed cross-entropy was used as a loss function to optimize                       1378 balanced images from eight disease classes from the
the deep learning trainable parameters [28].                                   ChestX-ray8 dataset).
2896                                                                                                                       M. A. Al-antari et al.

   After data balancing, an augmentation strategy was applied         YOLO-based confidence that the predicted box contains a
for all nine disease classes as follows. First, the original chest    lesion and how accurate it expects the representation of the
X-ray images were randomly scaled and translated ten times.           final output prediction by that box to be.
Second, the X-ray images for each class were rotated around              During the training process, the predicted confidence in
the origin center by 0°, 45°, 90°, 135°, 180°, 225°, 270°, and        each anchor is calculated by the multiplying the probability
315°. Finally, the rotated X-ray images for each class with θ =       of the existing respiratory disease (i.e., lesion) by the value of
0° and 270° were flipped left-right and up-down. This ensured         the intersections over union (IoU) as follows:
that each X-ray image for each balanced class was augmented
22 times. Thus, a total of 50,490 X-ray images were generated         Confidence ðPrconf : Þ ¼ ProbðObject Þ  IoUGT
                                                                                                                  Pred: :                   ð1Þ
and used to train our proposed CAD system. For each k-fold
                                                                         If the grid cell does not contain any respiratory dis-
test, the same data balancing and augmentation strategy was
                                                                      ease lesion, the confidence of all bounding boxes of
utilized. In addition, transfer learning was applied to initialize
                                                                      that cell should be zero. In contrast, if any suspected
the trainable parameters using ImageNet [9, 10]. Then, the
                                                                      disease lesion falls in that grid cell, Prob(Object )
deep learning CAD system was fine-tuned using our training
                                                                      should be greater than zero. Thus, the confidence of
set of chest X-ray images [31].
                                                                      all bounding boxes of that cell should also be greater
                                                                      than zero. However, the network has been optimized to
3.3 The concept of the deep learning CAD system
                                                                      achieve the highest object probability and the highest
                                                                      object confidence. Based on both object probability and
To simultaneously predict (detect and classify) COVID-
                                                                       IOUGT
                                                                           Pred: , the coordinates of all bounding boxes are si-
19 from among the other respiratory diseases, a deep
                                                                      multaneously optimized and adjusted to fit the object
learning CAD system based on the YOLO predictor
                                                                      that is falling in the specific grid cell. During the train-
was adopted and used. With regard to object detection,
                                                                      ing process, each grid cell predicts the conditional class
previous studies have employed conventional image pro-
                                                                      probabilities Prob(Classi| Object ) for all nine disease
cessing algorithms, machine learning classifiers, or com-
                                                                      classes (i.e., COVID-19 and other respiratory diseases).
plex deep learning pipelines [9, 10]. In contrast, our pro-
                                                                      During training, the confidence score for a detected
posed CAD system is a regressor model that can simul-
                                                                      bounding box is determined based on the conditional
taneously detect the localization of potential disease le-
                                                                      class probabilities as follows:
sions and predict the probabilities of those lesions be-
longing to specific disease classes [10]. It has a robust             Confidence Score ¼ ProbðClassi jObject Þ                              ð2Þ
ability to simultaneously learn the characteristics of the
entire input X-ray image and the background. Thus, it                                      Confidence i ¼ 1; 2; 3; …; and 9
can locate regions with lesions indicative of respiratory
                                                                      where
diseases with fewer background errors than other existing
methods [30]. In addition, it has a unique deep learning                                          ProbðClassi Þ
                                                                      ProbðClassi jObject Þ ¼                   :                           ð3Þ
structure allowing it to simultaneously optimize trainable                                        ProbðObjectÞ
parameters end-to-end to tune the training weights for
the detection and classification tasks. Unlike the Faster                Then,
R-CNN [32] and sliding window [33] methods, YOLO                                           ProbðClassi Þ
inspects the regions suspected of containing disease le-              Confidence Score ¼                  ProbðObject Þ                    ð4Þ
                                                                                           ProbðObjectÞ
sions directly in the context of the entire chest X-ray
                                                                                      IoUGT
                                                                                          Pred: ¼ ProbðClassi Þ  IoUPred:
                                                                                                                     GT
images. The conceptual diagram of the CAD-based
YOLO predictor is shown in Fig. 1.
   In fact, the YOLO predictor starts by dividing the input X-           During testing, to obtain the confidence score when
ray image into N × N grid cells, as shown in Fig. 1. If the           there is no GT, the conditional class probability is mul-
lesion (i.e., the lesion associated with COVID-19 or any other        tiplied by the individual box confidence value. The de-
respiratory diseases) center falls into any grid cell, that cell is   tected bounding boxes with the highest confidence
responsible for predicting that disease. For each grid cell, five     values indicate that COVID-19 or another respiratory
anchors (i.e., bounding boxes) are assigned and used to predict       disease is present, which should be considered the final
the disease class to which the lesion belongs (i.e., COVID-19,        prediction output. However, the confidence score proba-
pneumonia, etc.). For each anchor, YOLO predicts the disease          bility for each detected bounding box encodes the prob-
class of the lesions based on five prediction parameters: center      ability for each disease class and how well each box fits
location (x,y), width (w), height (h), and confidence score           the classes of respiratory diseases. The confidence score
probability (Prconf.). The confidence score interprets the            for each box is computed as follows:
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                                        2897

Confidence ScoreBoxi ¼                                                        ð5Þ             are used for each convolutional layer. Moreover, convolution
                                                                          
argmax ðPrconf :i  Prðclassi jObjectÞÞ; Prconf :iþ1  Prðclassiþ1 jObjectÞ ; …etc            reduction layers with a kernel size of 1 × 1 are added and
                  i ¼ 1; 2; 3; …; and 9:                                                      utilized, followed by 3 × 3 convolutional layers, as shown in
                                                                                              Fig. 5. This structure is used to reduce the size and compress
   For each bounding box, only one disease class is predicted                                 the derived feature representations [9, 10]. In addition, batch
and assigned (i.e., COVID-19, pneumonia, mass, etc.). As                                      normalization (BN) layer is used after each convolutional lay-
long as all bounding boxes are assigned to the same grid cell,                                er to reduce overfitting, accelerate convergence, and stabilize
the disease class for these boxes should be the same, but they                                the training of the deep network [9, 10]. Down-sampling using
can have different confidence values and conditional proba-                                   max-pooling (MP) with a size of 2 × 2 is applied five times
bilities. Finally, the detected box that has the maximum con-                                 after the convolutional layers to minimize the dimensionality
fidence probability should be used to determine the final pre-                                of the derived deep-feature maps and select the most appro-
dicted output of the proposed CAD system. Moreover, all                                       priate deep features. The aggregated deep-feature maps from
other detected bounding boxes have IoUGT       Pred: < 45% with                               the last convolutional layer are concatenated and flattened
lower confidence scores are suppressed using the algorithm                                    using global average pooling (GAP) to feed directly into the
of non-max suppression (NMS).                                                                 fully connected layers. The numbers of nodes or neurons for
                                                                                              the first and second dense layers are modified to 512 and
3.3.1 Deep learning structure of the CAD system                                               4096, respectively. The final output of the proposed model
                                                                                              is called a tensor of prediction (ToP), which contains all de-
The structure of the proposed CAD system involves                                             tected predictors of the five anchors: coordinates (x, y, w,
convolutional layers (Conv.), fully connected (FC) layers,                                    and h), confidence scores (Prconf.), and the conditional class
and tensor of prediction (ToP), as shown in Fig. 5. Deep                                      probabilities of all nine disease classes (Pr COVID − 19 ,
high-level features are extracted with 23 sequential                                          PrPneumonia, …etc). These predictors are encoded in the 3D
convolutional layers, while the coordinates of the detected                                   matrix of the ToP with the size of N × N × (5 × B + C), where
bounding boxes and the output probabilities are predicted with                                N, B, and C represent the number of grid cells, number of
two FC layers. The total number of derived deep-feature maps                                  anchors, and number of classes, respectively [27]. As men-
depends mainly on the number of convolutional kernels that                                    tioned above, the input X-ray image is divided into 7 × 7

                            Conv.1:3×3×32         Conv.2: 3×3×64 Conv.3: 1×1×128               Conv.7: 1×1×128         Conv./14/16/18: 3×3×1024        Conv.21: 1×1×64
                            MP: 2×2-s-2           MP: 2×2-s-2    Conv.4: 1×1×64                Conv.8: 3×3×256         Conv./15/17/: 1×1×512           Conv.22: 3×3×1024
            Input X-ray                                          Conv.5: 3×3×128               MP: 2×2-s-2             Conv./19/20/: 3×3×1024          Conv.23: 1×1×70
              Image                                              MP: 2×2-s-2                   Conv./10/12/: 1×1×256 Conv.22: 3×3×1024
                                                                 Conv.6: 3×3×256               Conv./9/11/13/: 3×3×512                                        FC2
                                                                                               MP: 2×2-s-2                                             FC1
                                      224
448

                                                      112

                                                                    56

                                                                                     28

                                                                                                       14

                                                                                                                                        7
                                                                                                                      7

                                     224                             56              28                                7
                                                 32   112                                               14                                  7
                                                               64            256                 512          1024               1024           1024
                                                                                                                                                        512
                                                                                                                                                              4096
                448
                                                                             Tensor of Prediction (ToP)
         Final prediction
                                                             1st Detected      5th Detected        Conditional Probability
              result                                        Bounding Box      Bounding Box             of nine Class
                                                                         .
                                                                         .
                                                                         .

                                            Cell
                                             1                                                                               7
448

                                            Cell 2
                                             .                                            .                                      Box1
                                             .                                            .                                             Box2 Pri
                                             .                                            .
                                                                                                                                 7
                                              . 49
                                            Cell                                          .                                              34
                448
Fig. 5 Deep learning structure of the proposed CAD System
2898                                                                                                                                                                                      M. A. Al-antari et al.

                                                                                                                         Pr. = 27%           Pr. = 17%               Pr. = 27%

                                         (a)                                  (b)                                                    (c)                                         (d)
Fig. 6 Effect of the confidence score (i.e., Prconf) threshold on the number of detected bounding boxes. The potential regions including suspected lesions
(i.e., detected bounding boxes) caused by COVID-19 were detected using confidence score thresholds of a 0.005, b 0.02, c 0.10, and d 0.20

nonoverlapping grid cells, and each grid cell should detect any                                  transformation of the input θi with a nonzero slope for the
lesion (caused by COVID-19 or the other respiratory diseases)                                    negative part of the activation function as follows:
in that cell. The size of 7 × 7 was chosen to achieve the best                                            
                                                                                                             θi ;            if θi > 0
performance, as shown in our previous studies. Meanwhile,                                        ϕðθi Þ ¼                                                ð6Þ
five anchors or bounding boxes (i.e., B = 5) are used to detect                                             0:1  θi ;        otherwise:
the object in each grid cell. The proposed CAD system was
built to detect and recognize nine classes of respiratory dis-
eases (i.e., C = 9). Thus, the final output represents a 3D ToP
with a size of 7 × 7 × 34. This means that the actual output
                                                                                                 3.4 Experimental setting
layer of the fully connected layer has 7 × 7 × 34 or 1666 neu-
rons. Each set of 34 neurons in the output FC layer is respon-
                                                                                                 The input digital CXR images were scaled using bilinear in-
sible for predicting all parameters of the five bounding boxes
                                                                                                 terpolation to a size of 448 × 448 pixels [9, 10]. In addition,
for each grid cell in the original chest X-ray image. Here, the
                                                                                                 the intensity of all CXR images was linearly normalized to a
key is that each grid cell can only make local predictions for its
                                                                                                 range of [0 ~ 1] as in [9, 10]. A multiscale training strategy
region of the input X-ray image. The proposed prediction
                                                                                                 was used to learn predictions across different resolutions of
model has the capability to detect and classify respiratory
                                                                                                 the input X-ray images [34]. Since the proposed network
diseases faster than other recent detection methodologies.
                                                                                                 downsamples the derived deep-feature maps five times, the
Moreover, the leaky rectified linear activation function is uti-
                                                                                                 network randomly chose a new image dimension size for ev-
lized in all the convolutional and fully connected layers, while
                                                                                                 ery 10 batches in multiplies of 32 (i.e., 320, 352, …, 608).
the ReLU activation function, ϕ(x) = max (0, x), is only uti-
                                                                                                 Thus, the smallest input resolution was 320 × 320, and the
lized in the final dense layer [27]. The leaky rectified linear
                                                                                                 largest input resolution was 608 × 608. Moreover, a mini-
activation function ϕ(θ i ) is expressed as the linear

                        180                                                                                              60
No. of testing images

                                                                                           143
                                                                                                 No. of testing images

                        150                                                                                                                                                                         46

                        120                                                                                              40                                                                   34           34
                                                                                                                                                  28
                        90                                                                                                                                                              24
                                                                                                                                           19            20             21        19
                                                                                                                                                               18
                        60                                                                                               20
                                                                                     34
                        30                                  18          20     15
                              4          5     6     5            10
                                   3
                         0                                                                                                 0
                              0    0.1   0.2   0.3   0.4    0.5   0.6   0.7    0.8   0.9    1                                        0     0.1    0.2    0.3   0.4     0.5        0.6   0.7   0.8   0.9    1

                                  Intersection over Union (IoU)                                                                                          Confidence Score
                                                           (a)                                                                                                        (b)
Fig. 7 Prediction measurements in terms of a the intersection over union (IoU) and b the confidence score for the final predicted bounding box for all test
sets for the nine disease classes
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                                                                                                                                   2899

                                                                                                                                                           10.65%

                                                                                                                                                           10.27%

                                                                                                                                                           10.27%

                                                                                                                                                                                   8.75%

                                                                                                                                                                                   6.71%
                                                                                                                                                                                                     batch size of 24 and number of epochs of 120 were utilized to

                                                                                                                                                   False

                                                                                                                                                                                   9.33
                                                                                                                           Total Classes

                                                                                                                                                           28

                                                                                                                                                           27

                                                                                                                                                           27

                                                                                                                                                                                   23

                                                                                                                                                                                   19
                                                                                                                                                                                                     train and validate the proposed CAD system.

                                                                                                                                                           89.35%

                                                                                                                                                           89.73%

                                                                                                                                                           89.73%

                                                                                                                                                                                   91.25%

                                                                                                                                                                                   93.29%
                                                                                                                                                                                   90.67
                                                                                                                                                   True

                                                                                                                                                           235

                                                                                                                                                           236

                                                                                                                                                           236

                                                                                                                                                                                   240

                                                                                                                                                                                   264
                                                                                                                                                                                                     3.5 Implementation environment

                                                                                                                                                           4.62%

                                                                                                                                                           6.15%

                                                                                                                                                           3.08%

                                                                                                                                                                                   3.08%

                                                                                                                                                                                   1.54%
                                                                                                                                                   False

                                                                                                                                                                                   3.69
                                                                                                                                                                                                     To execute the experimental study, a PC with the following
                                                                                                                           COVID-19

                                                                                                                                                           3

                                                                                                                                                           4

                                                                                                                                                           2

                                                                                                                                                                                   2

                                                                                                                                                                                   1
                                                                                                                                                           95.38%                                    specifications was used. Intel® Core(TM) i7-6850K proces-

                                                                                                                                                           93.85%

                                                                                                                                                           96.92%

                                                                                                                                                                                   96.92%

                                                                                                                                                                                   98.46%
                                                                                                                                                                                                     sor, RAM of 16.0 GB, 3.36 GHz, and four GPUs NVIDIA

                                                                                                                                                                                   96.31
                                                                                                                                                   True

                                                                                                                                                                                                     GeForce GTX1080.
                                                                                                                                                           62

                                                                                                                                                           61

                                                                                                                                                           63

                                                                                                                                                                                   63

                                                                                                                                                                                   64
                                                                                                                                                           18.75%

                                                                                                                                                                                   12.50%
                                                                                                                                                           25.0%

                                                                                                                                                           25.0%

                                                                                                                                                                                   25.0%
                                                                                                                                                                                   21.25
                                                                                                                                                   False

                                                                                                                                                                                                     3.6 Evaluation strategy
                                                                                                                                                           4

                                                                                                                                                           3

                                                                                                                                                           4

                                                                                                                                                                                   2

                                                                                                                                                                                   4
                                                                                                                                                           81.25%

                                                                                                                                                           75.00%

                                                                                                                                                                                   87.50%

                                                                                                                                                                                   75.00%
                                                                                                                           Nodule

                                                                                                                                                           75.0%

                                                                                                                                                                                                     Our evaluation strategy used two conditions to deter-

                                                                                                                                                                                   78.75
                                                                                                                                                   True

                                                                                                                                                           12

                                                                                                                                                           13

                                                                                                                                                           12

                                                                                                                                                                                   14

                                                                                                                                                                                   12                mine whether the detected bounding boxes constituted
                                                                                                                                                                                                     a final true detection. First, the overlapping ratio (i.e.,
                                                                                                                                                           3.45%

                                                                                                                                                           6.90%

                                                                                                                                                                                   3.45%
                                                                                                                                                   False

                                                                                                                                                           0.0%

                                                                                                                                                                                   0.0%
                                                                                                                                                                                   2.76
                                                                                                                           Cardiomegaly

                                                                                                                                                                                                     IoUGTPred: ) between the detected bounding box and its
                                                                                                                                                           0

                                                                                                                                                           1

                                                                                                                                                           2

                                                                                                                                                                                   1

                                                                                                                                                                                   0

                                                                                                                                                                                                     corresponding GT boxes had to be equal to or greater
                                                                                                                                                           96.55%

                                                                                                                                                           93.10%

                                                                                                                                                                                   96.55%
                                                                                                                                                           100%

                                                                                                                                                                                   100%
                                                                                                                                                                                   97.24

                                                                                                                                                                                                     than an appropriate practical threshold. Second, the con-
                                                                                                                                                   True

                                                                                                                                                           29

                                                                                                                                                           28

                                                                                                                                                           27

                                                                                                                                                                                   28

                                                                                                                                                                                   29

                                                                                                                                                                                                     fidence score (i.e., Prconf) of the final detected box had
                                                                                                                                                                                   12.50%
                                                                                                                                                           16.67%

                                                                                                                                                                                   16.67%

                                                                                                                                                                                                     to be equal to or greater than an appropriate threshold
    Detection evaluation results for COVID-19 and eight other respiratory diseases over the 5-fold tests in the test set

                                                                                                                                                           12.5%

                                                                                                                                                           8.33%

                                                                                                                                                                                   13.33
                                                                                                                                                   False

                                                                                                                                                                                                     [27, 35]. Specifically, we always use the maximum con-
                                                                                                                           Pneumonia

                                                                                                                                                           3

                                                                                                                                                           4

                                                                                                                                                           2

                                                                                                                                                                                   4

                                                                                                                                                                                   3

                                                                                                                                                                                                     fidence score to evaluate truly detected boxes [9, 10]. A
                                                                                                                                                                                   87.50%
                                                                                                                                                           83.33%

                                                                                                                                                           91.67%

                                                                                                                                                                                   83.33%
                                                                                                                                                           87.5%

                                                                                                                                                                                                     high confidence score reflects a highly accurate predic-
                                                                                                                                                                                   86.67
                                                                                                                                                   True

                                                                                                                                                           21

                                                                                                                                                           20

                                                                                                                                                           22

                                                                                                                                                                                   20

                                                                                                                                                                                   21

                                                                                                                                                                                                     tion that the lesion exists in the detected bounding box
                                                                                                                                                                                                     [9, 10].
                                                                                                                                                           12.90%
                                                                                                                                                           9.68%

                                                                                                                                                           6.45%

                                                                                                                                                                                   3.23%
                                                                                                                                                                                   9.68%
                                                                                                                                                   False

                                                                                                                                                                                   8.39

                                                                                                                                                                                                        For the quantitative evaluation with each fold test, we
                                                                                                                                                           3

                                                                                                                                                           2

                                                                                                                                                           4

                                                                                                                                                                                   3

                                                                                                                                                                                   1

                                                                                                                                                                                                     used weighted objective metrics, including sensitivity
                                                                                                                           Effusion

                                                                                                                                                           90.32%

                                                                                                                                                           93.55%

                                                                                                                                                           87.10%

                                                                                                                                                                                   96.77%
                                                                                                                                                                                   90.32%

                                                                                                                                                                                                     (Sens.), specificity (Spec.), overall accuracy (Acc.), the
                                                                                                                                                                                   91.61
                                                                                                                                                   True

                                                                                                                                                                                                     F1-score or Dice, the Matthews correlation coefficient
                                                                                                                                                           28

                                                                                                                                                           29

                                                                                                                                                           27

                                                                                                                                                                                   28

                                                                                                                                                                                   30

                                                                                                                                                                                                     (Mcc.), the positive predictive value (PPV), and the nega-
                                                                                                                                                           11.76%

                                                                                                                                                                                   17.65%
                                                                                                                                                           5.88%

                                                                                                                                                           5.88%

                                                                                                                                                                                   5.88%
                                                                                                                                                   False

                                                                                                                                                                                                     tive predictive value (NPV) [9, 10]. To avoid having test
                                                                                                                                                                                   9.41
                                                                                                                                                           2

                                                                                                                                                           1

                                                                                                                                                           1

                                                                                                                                                                                   3

                                                                                                                                                                                   1

                                                                                                                                                                                                     sets that were unbalanced with regard to the nine disease
                                                                                                                                                           88.24%

                                                                                                                                                           94.12%

                                                                                                                                                                                   94.12%
                                                                                                                                                           94.12%

                                                                                                                                                                                   82.35%

                                                                                                                                                                                                     classes, we used the weighted class strategy [27]. The
                                                                                                                                                                                   90.59
                                                                                                                           Mass

                                                                                                                                                   True

                                                                                                                                                                                                     weighted ratios for atelectasis, infiltration, pneumothorax,
                                                                                                                                                           15

                                                                                                                                                           16

                                                                                                                                                           16

                                                                                                                                                                                   14

                                                                                                                                                                                   16

                                                                                                                                                                                                     masses, effusion, pneumonia, cardiomegaly, nodules, and
                                                                                                                                                                                   12.50%
                                                                                                                                                           40.0%

                                                                                                                                                           30.0%

                                                                                                                                                           35.0%

                                                                                                                                                                                   25.0%
                                                                                                                           Pneumothorax

                                                                                                                                                                                                     COVID-19 were 0.14, 0.10, 0.08, 0.06, 0.12, 0.09, 0.11,
                                                                                                                                                                                   28.50
                                                                                                                                                   False

                                                                                                                                                                                                     0.06, and 0.25, respectively. All evaluation indices were
                                                                                                                                                           8

                                                                                                                                                           6

                                                                                                                                                           7

                                                                                                                                                                                   5

                                                                                                                                                                                   5

                                                                                                                                                                                                     computed using multiclass confusion matrices for each fold
                                                                                                                                                           60.0%

                                                                                                                                                           70.0%

                                                                                                                                                                                   75.0%
                                                                                                                                                           65.0%

                                                                                                                                                                                   75.0%

                                                                                                                                                                                   71.50
                                                                                                                                                   True

                                                                                                                                                                                                     test [9, 10].
                                                                                                                                                           12

                                                                                                                                                           14

                                                                                                                                                           13

                                                                                                                                                                                   15

                                                                                                                                                                                   15
                                                                                                                                                                                   4.00%
                                                                                                                                                   False

                                                                                                                                                           4.0%

                                                                                                                                                           4.0%

                                                                                                                                                           0.0%

                                                                                                                                                                                   0.0%

                                                                                                                                                                                   2.40
                                                                                                                                                           1

                                                                                                                                                           1

                                                                                                                                                           0

                                                                                                                                                                                   0

                                                                                                                                                                                   1
                                                                                                                           Infiltration

                                                                                                                                                                                                     4 Experimental results
                                                                                                                                                                                   96.00%
                                                                                                                                                           96.0%

                                                                                                                                                           96.0%

                                                                                                                                                           100%

                                                                                                                                                                                   100%

                                                                                                                                                                                   97.60
                                                                                                                                                   True

                                                                                                                                                           24

                                                                                                                                                           24

                                                                                                                                                           25

                                                                                                                                                                                   25

                                                                                                                                                                                   24

                                                                                                                                                                                                     4.1 Detection results
                                                                                                                                                           11.11%

                                                                                                                                                           13.89%

                                                                                                                                                           13.89%

                                                                                                                                                                                   8.33%

                                                                                                                                                                                   8.33%
                                                                                                                                                                                   11.11
                                                                                                                                                   False

                                                                                                                                                                                                     4.1.1 The prober threshold of the IoU and confidence score
                                                                                                                                                           4

                                                                                                                                                           5

                                                                                                                                                           5

                                                                                                                                                                                   3

                                                                                                                                                                                   3
                                                                                                                           Fold Test Atelectasis

                                                                                                                                                           88.89%

                                                                                                                                                           86.11%

                                                                                                                                                           86.11%

                                                                                                                                                                                            91.67%

                                                                                                                                                                                            91.67%

                                                                                                                                                                                                     The presented CAD system is able to predict five anchors (i.e.,
                                                                                                                                                                                   Avg. (%) 88.89
                                                                                                                                                   True

                                                                                                                                                           32

                                                                                                                                                           31

                                                                                                                                                           31

                                                                                                                                                                                            33

                                                                                                                                                                                            33

                                                                                                                                                                                                     bounding boxes) for each grid cell in entire X-ray images. To
                                                                                                                                                                                                     suppress undesirable detected boxes with very small confidence
    Table 1

                                                                                                                                                                                                     scores, the non-max suppression (NMS) technique was used [9,
                                                                                                                                                           Fold1

                                                                                                                                                                   Fold2

                                                                                                                                                                           Fold3

                                                                                                                                                                                   Fold4

                                                                                                                                                                                   Fold5

                                                                                                                                                                                                     34]. This algorithm required three consecutive stages during the
2900                                                                                                                                M. A. Al-antari et al.

        GT: Atelectasis               GT: Infiltration           GT: Pneumothorax                  GT: Mass                      GT: Effusion
        Predicted: Atelectasis        Predicted: Infiltration    Predicted: Pneumothorax           Predicted: Mass               Predicted: Effusion

IoU = 85.59%                     IoU = 98.31%                   IoU = 72.29%                IoU = 100%                     IoU = 100%
Pr. = 27.40%                     Pr. = 96.79%                   Pr. = 84.89%                Pr. = 90.30%                   Pr. = 92.74%

               (a)                          (b)                           (c)                              (d)                         (e)
       GT: Pneumonia                GT: Cardiomegaly                  GT: Nodule                  GT: COVID-19                  GT: COVID-19
       Predicted: Pneumonia         Predicted: Cardiomegaly           Predicted: Nodule           Predicted: COVID-19           Predicted: COVID-19

                                 IoU = 100%                     IoU = 84.21%                 IoU = 100%                    IoU = 99.31%
IoU = 100%
                                 Pr. = 60.70%                   Pr. = 81.79%                 Pr. = 85.79%                  Pr. = 32.69%
Pr. = 90.30%

             (f)                         (g)                              (h)                              (i)                         (j)
Fig. 8 Examples of correctly predicted cases of COVID-19 and other              (green), detected bounding box (red), IoU, and probability or confidence
respiratory diseases from chest X-ray (CXR) images: a atelectasis, b            score (Pr.) for each case are superimposed on the original chest X-ray
infiltration, c pneumothorax, d mass, e effusion, f pneumonia, g                images
cardiomegaly, h nodule, and i & j COVID-19. The GT information

testing phase. First, detected bounding boxes with confidence                   This was for the detection of at least one suspected lesion in
scores less than 0.005 were directly discarded. Second, among                   each test image for diagnostic purposes.
any remaining boxes, the box with the highest confidence score
(i.e., Prconf.) was selected to represent the final predicted                   4.1.2 Detection results after 5-fold cross-validation
bounding box. Finally, any remaining boxes with IoUnms ≥
50% with respect to the predicted box representing the final                    The presented deep learning CAD system can efficiently au-
output identified in the second step were also discarded.                       tomatically predict suspected COVID-19 lesions and other
Figure 6a shows the potential predicted boxes after applying                    respiratory disease lesions from entire X-ray images. Table 1
NMS. During the evaluation phase, the overlapping ratio of the                  shows the overall detection performance according to 5-fold
IoU between the final predicted box and its GT had to be greater                validation using the test images from all nine disease classes.
than an appropriate threshold to ensure that the confidence that                For each k-fold test, the same deep learning structure, training,
the predicted box includes the lesion is high. Experimentally,                  and testing parameters of the presented CAD system were
we found that the appropriate threshold for IoUGTPred: was greater              applied. The detected regions of interest (ROIs) that involved
than 45%, as shown in Fig. 7a. The majority of the final detect-                COVID-19 or other respiratory diseases were considered to be
                                                                                                                      Pred: ≥45% with Prconf. ≥
                                                                                correctly detected if and only if IoUGT
ed bounding boxes for the X-ray images in the test set had in
IoU accuracy greater than 90%. The final detected boxes with                    10%. Otherwise, they were considered to be false detection
IoUGTPred: < 45% were considered to be false detections. In ad-                 cases even if.Prconf. ≥ 10%. Indeed, the most correct final de-
dition to controlling the IoU, we also adjusted the appropriate                 tected bounding boxes had the maximum IoU and confidence
threshold for the confidence score to ignore the undesirable                    scores as well. Based on the average of the 5-fold tests, the
detected boxes. Figure 6b-d show the detected bounding boxes                    CAD-based YOLO was shown to be a reliable and feasible
stratified by different probability thresholds of the confidence                method of detecting COVID-19, with an overall detection
score. Experimentally, we found that the appropriate confi-                     accuracy of 96.31%. It failed to detect only 3.69% of
dence threshold was greater than 10%, as shown in Fig. 7b.                      COVID-19 cases in all the images. More generally, the
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                            2901

      GT: Atelectasis               GT: Infiltration              GT: Pneumothorax                  GT: Mass                          GT: Effusion
      Predicted: Atelectasis        Predicted: Infiltration       Predicted: Pneumonia              Predicted: Cardiomegaly            Predicted: Effusion

 IoU = 0.0%                    IoU = 0.0%                     IoU = 0.0%                         IoU = 0.0%                    IoU = 12.12%
 Pr. = 23.77%                  Pr. = 3.07%                    Pr. = 21.04%                       Pr. = 96.08%                   Pr. = 87.25%

                (a)                           (b)                             (c)                            (d)                           (e)
        GT: Pneumonia                 GT: Nodule                  GT: COVID-19                       GT: COVID-19                     GT: COVID-19
        Predicted: Nodule             Predicted: Nodule           Predicted: COVID-19                Predicted: COVID-19              Predicted: COVID-19

   IoU = 0.0%                  IoU = 0.0%                     IoU = 0.0%                                                       IoU = 0.0%
                                                                                                 IoU = 0.0%
  Pr. = 32.53%                 Pr. = 60.75%                    Pr. = 55.0%                                                      Pr. = 75.39%
                                                                                                  Pr. = 59.02%

            (f)                         (g)                             (h)                                (i)                             (j)
Fig. 9 Examples of the incorrectly predicted cases of COVID-19 and                  (h, i, & j) COVID-19. The GT information (green), detected bounding
other respiratory diseases from chest X-ray images: a atelectasis, b infil-         box (red), IoU, and probability or confidence score (Pr.)for each case are
tration, c pneumothorax, d mass, e effusion, f pneumonia, g nodule, and             superimposed on the original chest X-ray images

presented CAD system has the capability to correctly detect                         classifies them at the same time. In fact, this is the key char-
respiratory diseases, with an overall detection accuracy of                         acteristic that makes the YOLO predictor faster and more
90.67% for all nine disease classes. The true and false detec-                      accurate than other techniques, such as Faster R-CNN [10,
tion cases for the individual classes for the 5-fold validation                     27, 34]. All final detected bounding boxes are classified even
are presented in Table 1.                                                           if they have been incorrectly detected. With regard to classi-
    With regard to the qualitative evaluation, Fig. 8 shows                         fication, it is important to know the final diagnosis status of
examples of correctly detected suspicious lesions indicative                        each X-ray image (i.e., COVID-19 or another disease) since
of COVID-19 and all other disease classes. The overlapping                          its GT label is available. The classification evaluation results
ratios (i.e., IoU) for the resulting bounding boxes beside their                    are derived based on the multiclass confusion matrices for all
corresponding confidence scores from each case are also pre-                        nine classes over each fold test. Figure 10 shows an example
sented. The detected boxes of these cases have acceptable IoU                       of the confusion matrices for all disease classes from the 3-
ratios and high confidence scores, indicating that the lesions                      fold and 5-fold tests. Indeed, most of the COVID-19 cases
have been accurately detected. Figure. 9 shows some exam-                           were correctly distinguished from other respiratory diseases.
ples of falsely detected cases of all nine disease classes. The                     Due to the high degree of similarity between COVID-19 and
final detected boxes of these cases have undesirable overlap-                       other respiratory diseases, some cases of COVID-19 were
ping ratios with their GTs. Therefore, they were considered                         misclassified as pneumonia and vice versa. The weighted rec-
incorrect detection cases even if they satisfied the confidence                     ognition evaluation metrics obtained via the five-fold test for
score condition.                                                                    all classes are reported in Table 2. Specifically, the classifica-
                                                                                    tion evaluation results for each individual disease class as an
4.2 Classification results                                                          average of the tests are shown in Fig. 11. It is clear that the
                                                                                    proposed CAD system achieved an average overall accuracy
The presented CAD-based YOLO predictor has the capability                           of classification between 94.60% for pneumonia and 97.40%
to simultaneously detect ad classify end-to-end the detected                        for COVID-19. The sensitivity was 91.69%, the specificity
ROIs as COVID-19 or other respiratory diseases. As shown in                         was 98.79%, and the Mcc. was 91.96% for differentiating
Figs. 8 and 9, the presented CAD system detects the final                           COVID-19 from the other respiratory diseases. The classifi-
regions with suspected lesions of respiratory diseases and                          cation performance of the system for COVID-19 as
2902                                                                                                          M. A. Al-antari et al.

Fig. 10 The derived multiclass
confusion matrices of COVID-19
against other lung diseases from
the test sets over a 3-fold and b 5-
fold tests

                                               Actual Class

                                                                                 Predicted Class
                                                                                        (a)
                                               Actual Class

                                                                                  Predicted Class
                                                                                       (b)

represented by the F1-score was 93.86%. We can conclude          tuned over 5-fold tests using the original, balanced, and aug-
that the CAD system achieved satisfactory and promising          mented datasets in three separate scenarios. In each scenario,
classification performance with regard to the problem of the     the same deep learning structure and learning settings were
multiclass recognition of respiratory diseases.                  used. Figure 12 shows the weighted classification perfor-
                                                                 mance as an average of the 5-fold tests for each scenario.
4.3 Effects of the regularization strategies                     The balancing strategy improved the diagnostic performance
                                                                 by 3.43%, 1.47%, 2.79%, 3.35%, 3.86%, 3.28%, and 1.43%
To improve the diagnostic performance for COVID-19 and           in terms of the sens., spec., Acc., F1-score, Mcc., PPV, and
the differentiation of COVID-19 from other respiratory dis-      NPV, respectively. The major improvement was achieved
eases, data balancing and augmentation strategies were used.     through data augmentation after balancing. After applying
In this regard, the presented CAD system was trained and fine-   the augmentation strategy, the classification performance
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                                          2903

Table 2 Weighted classification measurements (%) for COVID-19                                               5 Discussion
among the other lung diseases as an average over the 5-fold tests in the
test set
                                                                                                            Recently, researchers have been encouraged to apply artificial
Fold Test                                  Sens. Spec.      Acc.    F1-         Mcc. PPV          NPV       intelligence (AI) methodologies to help physicians in hospi-
                                                                    score                                   tals diagnose COVID-19. Indeed, deep learning based on
Fold1                                      88.25   99.16    97.59   85.47       83.60   86.0      98.90
                                                                                                            CNN has been shown to achieve promising classification re-
Fold2                                      84.47   99.09    97.37   84.75       82.75   85.33     98.72
                                                                                                            sults with different applications. To date, a few studies based
                                                                                                            on machine learning and deep learning models have been
Fold3                                      83.33   98.78    97.08   83.63       81.50   84.40     98.68
                                                                                                            designed and presented. Such studies employed deep learning
Fold4                                      85.25   99.16    97.59   85.47       83.60   86.0      98.90
                                                                                                            models to classify entire input X-ray images. However, it is
Fold5                                      84.47   99.09    97.37   84.75       82.75   85.33     98.72
                                                                                                            neither efficient nor accurate to base a diagnosis on an entire
Average (%)                                85.15   99.056   97.40   84.81       82.84   85.412    98.784
                                                                                                            X-ray image [12, 27]. Thus, the detection by the CAD system
                                                                                                            of regions containing suspected lesions related to a respiratory
                                                                                                            disease (i.e., COVID-19 or another disease) represents a cru-
was improved by 12.91%, 4.49%, 6.64%, 12.17%, 12.99%,                                                       cial prerequisite for achieving a more accurate diagnosis.
11.72%, and 3.56% in terms of the sens., spec., Acc., F1-                                                   Table 3 compares the prediction compression performance
score, Mcc., PPV, and NPV, respectively.                                                                    of our proposed CAD system with the performance of the
                                                                                                            latest deep learning models. Ozturk et al. [8] presented the
                                                                                                            deep learning model of DarkCovidNet that can be used to
4.4 The cost of the prediction time                                                                         differentiate COVID-19 cases from pneumonia and normal
                                                                                                            cases. They achieved an overall diagnostic performance of
The training time depends on the deep learning structure,                                                   87.02%. Wand et al. developed the COVID-Net deep learning
training settings (i.e., number of epochs and mini-batch                                                    model to differentiate COVID-19 cases from normal and
size), number of training sets, and specifications of the                                                   pneumonia cases. They achieved an overall diagnotic perfor-
PC. For each fold test, the presented CAD system re-                                                        mance of 92.40%. Meanwhile, Khan et al. [22] presented the
quired almost 18 h for training. To make predictions                                                        deep learning model of CoroNet, which can be used to differ-
for all test images, the proposed CAD system required                                                       entiate COVID-19 cases from bacterial pneumonia, viral
2.44 s. Since we had 263 test images across all disease                                                     pneumonia, and normal cases. A diagnostic performance of
classes, the predication time for an individual X-ray im-                                                   89.60% was achieved for the multiclass recognition problem.
age was 0.0093 s. Our CAD system can make reliable                                                             In this study, the proposed CAD system could effectively
preditctions in real time by 108 FPS. The rapid global                                                      differentiate COVID-19 from eight other respiratory diseases.
spread of COVID-19 is challenging for physicians. The                                                       The detection accuracies for all nine disease classes ranged
accurate and fast detection of COVID-19 based on entire                                                     from 71.50% for pneumothorax to 97.60% for infiltration.
chest X-ray image can help physicians, patients, and                                                        The overall performance for the correct detection of regions
health care systems.                                                                                        with suspicious lesions was 90.67%. With regard to the

                                           100
            Classiﬁcaon Performance (%)

                                           95
                                           90
                                           85
                                           80
                                           75
                                           70
                                           65
                                           60
                                                      Sens.             Spec.              Acc.            F1-score        Mcc.           PPV            NPV
                                                   Atelectasis              Inﬁltraon              Pneumothorax        Mass                Eﬀusion
                                                   Pneumonia                Cardiomegaly            Nodule              COVID-19

                                                                                                    Evaluaon Metrics
Fig. 11 Classification evaluation measurements (%) for each individual class of lung diseases as an average over the 5-fold tests in the test set
2904                                                                                                                                             M. A. Al-antari et al.

            Classification Performance (%)
                                             95

                                             85

                                             75

                                             65
                                                  Sens.       Spec.              Acc.         F1-score           Mcc.          PPV            NPV
                                                                                        Evaluation Metrics

                                                                      Original          Balancing        Balancing and Augmentation
Fig. 12 Effect of enlarging the training set sizes using different deep learning regularization strategies on the overall classification performance of the
proposed CAD system. The evaluation results are presented as the average of the 5-fold tests in the test sets for all disease classes

detection of COVID-19, an overall detection accuracy of                                          results are logical and acceptable because COVID-19 and oth-
96.31% was achieved. The results of the evaluation of the                                        er respiratory diseases can affect both lungs in the same pa-
detection capability of the model for each individual disease                                    tient. Meanwhile, it is important to consider the final detected
class are reported in Table 1. The proposed CAD system could                                     regions with suspicious lesions for classification even if they
simultaneously predict the diagnosis (i.e., COVID-19 or not)                                     have been incorrectly detected. As shown in Fig. 9, most
for each detected ROI to determine the final diagnosis of the                                    falsely detected cases were correctly classified. Additionally,
input X-ray image. As shown in Table 2, a promising classi-                                      it may help physicians focus on regions with suspicious le-
fication accuracy of 97.40% was achieved over 5-fold tests.                                      sions other than those with GTs. Figure 9h-j show the incor-
The simultaneous detection and classification of COVID-19                                        rectly detected ROIs according to the annotated position of the
or other respiratory diseases in a single assessment of an entire                                GT, but the final diagnosis was accurate. Meanwhile, deep
X-ray image is helpful for physicians, especially when the                                       learning regularizations for data balancing and augmentation
number of patients is large. This will directly help support                                     were applied to improve the final diagnostic performance of
health care systems in hospitals as well. By controlling the                                     the proposed CAD system. As shown in Fig. 12, these
confidence score threshold for the detected bounding boxes,                                      regularizers obviously improved the diagnostic performance
we can select the desired number of boxes that should be used                                    as reflected in all evaluation indices. The average of the five-
for the final real-time diagnosis. As shown in Fig. 6c, after                                    fold tests for the overlap class problem showed that the clas-
adjusting the confidence threshold to be greater than 10%, two                                   sification performance increased from 90.76% to 97.40% and
detected boxes were finally assigned two different regions                                       from 72.64% to 84.81% with regard to the Acc. and F1-score,
with lesions suspected of being related to COVID-19. These                                       respectively. Generally, CAD systems could support physi-

Table 3     Prediction performance comparison against the latest deep learning models for the diagnosis of COVID-19 based on chest x-ray images

Reference                                          Method                                Prediction Classes: No. of images                   Diagnosis Accuracy
                                                                                                                                             (%)

Ozturk et al. [8]          DarkCovidNet                                                  COVID-19: 125, Pneumonia: 500, and Normal: 500      87.02
Wang et al. [18]           COVID-Net                                                     COVID-19: 53, Pneumonia: 5526, and Normal: 8066     92.40
Apostolopoulos et al. [20] VGG19, Mobile Net, Inception,                                 COVID-19: 224, Pneumonia: 700, and Normal: 504      93.48 ➔ for VGG19
                             Xception,
                             and InceptionResNet v2
Khan et al. [22]           CoroNet                                                       COVID-19: 284, Pneumonia bacterial: 330, Pneumonia 89.60
                                                                                          viral: 327, and Normal: 310
The Presented CAD                                  CAD-based YOLO Predictor              COVID-19: 326 and the number of images from other Detection: 90.67
  system                                                                                  eight                                             Classification: 97.40
                                                                                          classes are shown in Fig. 2.
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                    2905

cians by providing a second opinion that could be used when                 Research Center) support program(IITP-2017-0-01629) supervised by
                                                                            the IITP(Institute for Information & communications Technology
making the final decision regarding the diagnosis. The fast
                                                                            Promotion)”, by Institute for Information & communications
and accurate diagnosis of COVID-19 based on entire X-ray                    Technology P romoti on(IITP) grant funded by the Korea
images is key to helping physicians, patients, and health care              government(MSIT) (No.2017–0-00655), by the MSIT(Ministry of
systems.                                                                    Science and ICT), Korea, under the Grand Information Technology
                                                                            Research Center support program(IITP-2020-0-01489) supervised by
   The proposed CAD system has some advantages. First, the
                                                                            the IITP(Institute for Information & communications Technology
model has promising predictive accuracy for differentiating                 Planning & Evaluation) NRF-2016K1A3A7A03951968 and NRF-
COVID-19 from other respiratory diseases is achieved.                       2019R1A2C2090504.
Second, the model can rapidly predict the presence of
COVID-19 and other respiratory diseases based on entire X-                  Compliance with ethical standards
ray images. Finally, user interventions are not required to de-
tect and classify COVID-19 because the proposed CAD sys-                    Conflict of interest None.
tem has a unique end-to-end deep learning structure.
                                                                            Declarations Not applicable.
   Despite the encouraging and rapid diagnostic performance
for COVID-19, some drawbacks and limitations need to be
addressed. Annotated digital X-ray images from COVID-19
patients are still unavailable. Considerable time and effort on
                                                                            References
the part of physicians is needed to label and localize the exact
                                                                             1.   Alimadadi A, Aryal S, Manandhar I, Munroe PB, Joe B, Cheng X
regions containing lesions associated with COVID-19.                              (2020) Artificial intelligence and machine learning to fight COVID-
   In the future, when the annotated chest X-ray images be-                       19. American Physiological Society Bethesda, MD
come available, we plan to validate the presented CAD sys-                   2.   Wu F, Zhao S, Yu B, Chen Y-M, Wang W, Song Z-G, Hu Y, Tao
                                                                                  Z-W, Tian J-H, Pei Y-Y (2020) A new coronavirus associated with
tem. For increase the reliability of the diagnosis, we will ex-
                                                                                  human respiratory disease in China. Nature 579(7798):265–269
pand our proposed CAD system to diagnose COVID-19 based                      3.   Chinazzi M, Davis JT, Ajelli M, Gioannini C, Litvinova M, Merler
on digital CT images. Additionally, we plan to locally collect                    S, y Piontti AP, Mu K, Rossi L, Sun K (2020) The effect of travel
digital X-ray and CT images for further validation. To achieve                    restrictions on the spread of the 2019 novel coronavirus (COVID-
more accurate pre-training of deep learning models, a gener-                      19) outbreak. Science 368 (6489):395–400
                                                                             4.   Robson B (2020) Computers and viral diseases. Preliminary bioin-
ative adversarial network (GAN) could be used to synthesize                       formatics studies on the design of a synthetic vaccine and a preven-
images [27].                                                                      tative peptidomimetic antagonist against the SARS-CoV-2 (2019-
                                                                                  nCoV, COVID-19) coronavirus. Comput Biol Med 119:103670
                                                                             5.   Zhao S, Lin Q, Ran J, Musa SS, Yang G, Wang W, Lou Y, Gao D,
                                                                                  Yang L, He D (2020) Preliminary estimation of the basic reproduc-
6 Conclusion                                                                      tion number of novel coronavirus (2019-nCoV) in China, from
                                                                                  2019 to 2020: a data-driven analysis in the early phase of the out-
                                                                                  break. Int J Infect Dis 92:214–217
In this work, a deep learning CAD system is proposed that can
                                                                             6.    Coronavirus disease (COVID-19) (2020) World Health
simultaneously detect and diagnose COVID-19 based on                               Organization. https://www.who.int/emergencies/diseases/novel-
chest X-ray images. Our presented deep learning system was                         coronavirus-2019. Accessed November 2020
built in a unique deep learning structure and can rapidly pre-               7.   Pereira RM, Bertolini D, Teixeira LO, Silla CN Jr, Costa YM
dict the regions containing suspicious lesions likely associated                  (2020) COVID-19 identification in chest X-ray images on flat and
                                                                                  hierarchical classification scenarios. Comput Methods Prog
with COVID-19 on entire X-ray images. The proposed CAD                            Biomed 194:105532
system was validated with regard to the multiclass recognition               8.   Ozturk T, Talo M, Yildirim EA, Baloglu UB, Yildirim O, Acharya
problem, achieving a promising diagnostic accuracy of                             UR (2020) Automated detection of COVID-19 cases using deep
97.40% over 5-fold tests. Highly accurate and rapid informa-                      neural networks with X-ray images. Comput Biol Med 121:103792
                                                                             9.   Al-Antari MA, Al-Masni MA, Choi MT, Han SM, Kim TS (2018)
tion extraction from entire CXR images is a key for develop-                      A fully integrated computer-aided diagnosis system for digital X-
ing a comprehensive and useful patient triage system in hos-                      ray mammograms via deep learning detection, segmentation, and
pitals and healthcare systems. The promising diagnostic per-                      classification. Int J Med Inform 117:44–54. https://doi.org/10.1016/
formance and the rapid prediction time make this proposed                         j.ijmedinf.2018.06.003
                                                                            10.   Al-Masni MA, Al-Antari MA, Park JM, Gi G, Kim TY, Rivera P,
CAD system practical and reliable as a means of assisting
                                                                                  Valarezo E, Choi MT, Han SM, Kim TS (2018) Simultaneous
physicians, patients, and health care systems.                                    detection and classification of breast masses in digital mammo-
                                                                                  grams via a deep learning YOLO-based CAD system. Comput
Acknowledgement This research was supported by the MSIT(Ministry                  Methods Prog Biomed 157:85–94. https://doi.org/10.1016/j.cmpb.
of Science and ICT), Korea, under the ITRC(Information Technology                 2018.01.017
2906                                                                                                                            M. A. Al-antari et al.

11. Al-Masni MA, Al-Antari MA, Choi MT, Han SM, Kim TS (2018)                lesions in digital X-ray mammograms. Comput Methods Prog
    Skin lesion segmentation in dermoscopy images via deep full res-         Biomed 196:105584. https://doi.org/10.1016/j.cmpb.2020.105584
    olution convolutional networks. Comput Methods Prog Biomed           28. Krizhevsky A, Sutskever I, Hinton GE (2012) ImageNet classifica-
    162:221–231. https://doi.org/10.1016/j.cmpb.2018.05.027                  tion with deep convolutional neural networks. In: 25th International
12. Al-Masni MA, Kim D-H, Kim T-S (2020) Multiple skin lesions               Conference on Neural Information Processing Systems, USA, pp.
    diagnostics via integrated deep convolutional networks for segmen-       1097–1105. pp 1097–1105
    tation and classification. Comput Methods Prog Biomed 190:           29. Takahashi R, Kajikawa Y (2017) Computer-aided diagnosis: a sur-
    105351                                                                   vey with bibliometric analysis. Int J Med Inform 101:58–67. https://
13. Cohen JP, Morrison P, Dao L (2020) COVID-19 image data col-              doi.org/10.1016/j.ijmedinf.2017.02.004
    lection. https://www.githubcom/ieee8023/covid-chestxray-dataset.     30. Chougrad H, Zouaki H, Alheyane O (2018) Deep convolutional
    Accessed June [online] 2020                                              neural networks for breast cancer screening. Comput Methods
14. Chowdhury M, Rahman T, Khandakar A, Kadir R, Mahbub Z,                   Prog Biomed 157:19–30. https://doi.org/10.1016/j.cmpb.2018.01.
    Islam K, Khan M, Iqbal A, Emadi N, Reaz M (2020) Can AI help             011
    in screening Viral and COVID-19 pneumonia? https://www.              31. Celik Y, Talo M, Yildirim O, Karabatak M, Acharya UR (2020)
    kagglecom/tawsifurrahman/covid19-radiography-database. .                 Automated invasive ductal carcinoma detection based using deep
    Accessed June [online] 2020                                              transfer learning with whole-slide images. Pattern Recogn Lett 133:
15. Wang X, Peng Y, Lu L, Lu Z, Bagheri M (2017) Summers RM                  232–239
    Chestx-ray8: hospital-scale chest x-ray database and benchmarks      32. Girshick R (2015) Fast r-cnn. In: Proceedings of the IEEE interna-
    on weakly-supervised classification and localization of common           tional conference on computer vision, pp. 1440–1448
    thorax diseases. In: Proceedings of the IEEE conference on com-
                                                                         33. Felzenszwalb PF, Girshick RB, McAllester D, Ramanan D (2010)
    puter vision and pattern recognition, pp. 2097–2106
                                                                             Object detection with discriminatively trained part-based models.
16. Oh Y, Park S, Ye JC (2020) Deep learning covid-19 features on cxr
                                                                             IEEE Trans Pattern Anal Mach Intell 32(9):1627–1645
    using limited training data sets. IEEE Trans Med Imaging 39(8):
                                                                         34. Redmon J, Farhadi A (2017) YOLO9000: better, faster, stronger.
    2688–2700
                                                                             In: Proceedings of the IEEE conference on computer vision and
17. Fan D-P, Zhou T, Ji G-P, Zhou Y, Chen G, Fu H, Shen J, Shao L
                                                                             pattern recognition, pp 7263–7271
    (2020) Inf-net: automatic COVID-19 lung infection segmentation
    from CT images. IEEE Trans Med Imaging 39(8):2626–2637               35. Al-Antari MA, Al-Masni MA, Kim T-S (2020) Deep learning
                                                                             computer-aided diagnosis for breast lesion in digital mammogram.
18. Wang L, Wong A (2020) COVID-net: a tailored deep convolutional
                                                                             In: Deep Learning in Medical Image Analysis. Springer, Cham, pp
    neural network design for detection of COVID-19 cases from chest
                                                                             59–72
    radiography images. arXiv preprint arXiv:200309871
19. Hemdan EE-D, Shouman MA, Karar ME (2020) Covidx-net: a
    framework of deep learning classifiers to diagnose covid-19 in x-    Publisher’s note Springer Nature remains neutral with regard to jurisdic-
    ray images: arXiv preprint arXiv:2003.11055                          tional claims in published maps and institutional affiliations.
20. Apostolopoulos I, Mpesiana T (2020) Covid-19: automatic detec-
    tion from x-ray images utilizing transfer learning with
    convolutional neural networks. Phys Eng Sci Med 43:635–640.
                                                                                                                  Mugahed A. Al-antari received
    https://doi.org/10.1007/s13246-020-00865-4
                                                                                                                  his Ph.D. degree from th e
21. Ahuja S, Panigrahi BK, Dey N, Rajinikanth V, Gandhi TK (2020)                                                 Department of Biomed ical
    Deep transfer learning-based automated detection of COVID-19                                                  Engineering, Kyung Hee
    from lung CT scan slices. Appl Intell. https://doi.org/10.1007/                                               University, Republic of Korea, in
    s10489-020-01826-w                                                                                            2019. Now, Al-antari is a post-
22. Khan AI, Shah JL, Bhat M (2020) Coronet: a deep neural network                                                doctoral researcher in the
    for detection and diagnosis of COVID-19 from chest x-ray images.                                              Ubiquitous Computing
    Comput Methods Prog Biomed 196:105581. https://doi.org/10.                                                    Laboratory (UCLab),
    1016/j.cmpb.2020.105581                                                                                       Department of Computer Science
23. Narin A, Kaya C, Pamuk Z (2020) Automatic detection of corona-                                                and Engineering, Kyung Hee
    virus disease (covid-19) using x-ray images and deep convolutional                                            University, Republic of Korea.
    neural networks: arXiv preprint arXiv:2003.10849                                                              Al-antari is an official lecturer
24. Ardakani AA, Kanafi AR, Acharya UR, Khadem N,                                                                 since 2010 in the Department of
     Mohammadi A (2020) Application of deep learning tech-                                                        Biomedical Engineering at Sana’a
     nique to manage COVID-19 in routine clinical practice               Community College, Republic of Yemen. Al-antari has professional in-
     using CT images: results of 10 convolutional neural net-            dustrial experience (Executive Engineering Director) for more than
     works. Comput Biol Med 121:103795                                   5 years for developing mini- and whole body DXA machines using X-
25. Mohamadou Y, Halidou A, Kapen PT (2020) A review of mathe-           ray pencil and fan beams at YOZMA BMTech Group, Seoul, Republic of
    matical modeling, artificial intelligence and datasets used in the   Korea. He is a member of IEEE EMBS since 2014. His current research
    study, prediction and management of COVID-19. Appl Intell            interests include deep learning, machine learning, artificial intelligence
    50(11):3913–3925                                                     (AI), AI-based medical platforms, AI-based energy analysis, pattern rec-
26. Shoeibi A, Khodatars M, Alizadehsani R, Ghassemi N, Jafari M,        ognition, medical signal and image processing, and medical imaging of
    Moridian P, Khadem A, Sadeghi D, Hussain S, Zare A (2020)            dual-energy X-ray absorptiometry (DXA). His recent AI-based publica-
    Automated detection and forecasting of COVID-19 using deep           tions have earned a lot of attention from researchers as well as the inter-
    learning techniques: A review. arXiv preprint arXiv:2007.10785       national journal editorials and been selected to represent a cornerstone for
27. Al-Antari MA, Kim T-S (2020) Evaluation of deep learning detec-      modern medicine.
    tion and classification towards computer-aided diagnosis of breast
“Fast deep learning computer-aided diagnosis of COVID-19 based on digital chest x-ray images”                                                     2907

                                       Cam-Hao Hua received the B.S.                                                 Sungyoung Lee (M’89) received
                                       degree in Electrical and                                                      the B.S. degree from Korea
                                       Electronic Engineering from                                                   University, Seoul, Republic of
                                       Bach Khoa University, Ho Chi                                                  Korea, and the M.S. and Ph.D.
                                       Minh City, Vietnam, in 2016. He                                               degrees in computer science from
                                       is currently pursuing the Ph.D. de-                                           the Illinois Institute of
                                       gree with the Department of                                                   Technology, Chicago, IL, USA,
                                       Computer Science and                                                          in 1987 and 1991, respectively.
                                       Engineering, Kyung Hee                                                        He was an Assistant Professor
                                       University, Gyeonggi, Republic                                                with the Department of
                                       of Korea. His research interests                                              Computer Science, Governors
                                       are computer vision and deep                                                  State University, University Park,
                                       Learning.                                                                     IL, USA, from 1992 to 1993. He
                                                                                                                     has been a Professor with the
                                                                                                                     Department of Computer
                                                                             Engineering, Kyung Hee University, Republic of Korea, since 1993,
                                                                             where he has been the Director of the Neo Medical ubiquitous-Life
                                                                             Care Information Technology Research Center since 2006. He is current-
                                                                             ly the Founding Director of the Ubiquitous Computing Laboratory. His
                                       Jaehun Bang received his Ph.D.        current research interests include ubiquitous computing and applications,
                                       degree from the Department of         wireless ad hoc and sensor networks, context aware middle-ware, sensor
                                       Computer Science and                  operating systems, real-time systems and embedded systems, and activity
                                       Engineering, Kyung Hee                and emotion recognition. He is a member of ACM.
                                       University, Republic of Korea, in
                                       2019. Now, Jaehun Bang is a
                                       post-doctoral researcher in the
                                       Ubiquitous Computing
                                       Laboratory (UCLab) and
                                       Intelligent Medical Platform
                                       Research Center (IMPRC),
                                       Department of Computer Science
                                       and Engineering, Kyung Hee
                                       University, Republic of Korea.
                                       His current research interests in-
clude ubiquitous computing and applications, context awareness, signal
processing, pattern recognition, machine learning, and activity & emotion
recognition.
