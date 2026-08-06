---
source_id: 174
bibtex_key: girdhar2022omnivore
title: Omnivore: A Single Model for Many Visual Modalities
year: 2022
domain_theme: Segmentasi RGB-D
verified_pdf: 174_Omnivore.pdf
char_count: 97502
---

O MNIVORE: A Single Model for Many Visual Modalities

    Rohit Girdhar∗           Mannat Singh∗            Nikhila Ravi∗    Laurens van der Maaten             Armand Joulin             Ishan Misra∗
                                                                      Meta AI
                                                 https://facebookresearch.github.io/omnivore

 Image (RGB)                          Depth map (D)                      Single-view 3D (RGBD)                       Video (RGBT)

Figure 1. O MNIVORE is a single vision model for many different visual modalities. It learns to construct representations that are aligned
across visual modalities, without requiring training data that specifies correspondences between those modalities. Using O MNIVORE’s
shared visual representation, we successfully identify nearest neighbors of left: an image (ImageNet-1K validation set) in vision datasets that
contain right: depth maps (ImageNet-1K training set), single-view 3D images (ImageNet-1K training set), and videos (Kinetics-400 validation set).

                              Abstract                                     1. Introduction
    Prior work has studied different visual modalities in iso-                 Computer vision research spans multiple modalities re-
lation and developed separate architectures for recogni-                   lated to our perception of the visual world, such as images,
tion of images, videos, and 3D data. Instead, in this pa-                  videos, and depth. In general, we study each of these modal-
per, we propose a single model which excels at classifying                 ities in isolation, and tailor our computer vision models to
images, videos, and single-view 3D data using exactly the                  learn the best features from their specificities. While these
same model parameters. Our ‘O MNIVORE’ model lever-                        modality-specific models achieve impressive performance,
ages the flexibility of transformer-based architectures and is             sometimes even surpassing humans on their specific tasks,
trained jointly on classification tasks from different modal-              they do not possess the flexibility that a human-like vision
ities. O MNIVORE is simple to train, uses off-the-shelf stan-              system does—the ability to work across modalities. We ar-
dard datasets, and performs at-par or better than modality-                gue that the first step towards a truly all-purpose vision sys-
specific models of the same size. A single O MNIVORE model                 tem is to build models that work seamlessly across modali-
obtains 86.0% on ImageNet, 84.1% on Kinetics, and 67.1%                    ties, instead of being over-optimized for each modality.
on SUN RGB-D. After finetuning, our models outperform
prior work on a variety of vision tasks and generalize across                  Beyond their flexibility, such modality-agnostic models
modalities. O MNIVORE’s shared visual representation nat-                  have several advantages over their traditional, modality-
urally enables cross-modal recognition without access to                   specific counterparts. First, a modality-agnostic model can
correspondences between modalities. We hope our results                    perform cross-modal generalization: it can use what it has
motivate researchers to model visual modalities together.                  learned from one modality to perform recognition in other
                                                                           modalities. For example, it can recognize pumpkins in 3D
                                                                           images even if it has only seen labeled videos of pumpkins.
    ∗ Equal technical contribution.                                        In turn, this allows existing labeled datasets to be used more
effectively: it becomes possible to train models on the union        Input            Patches              Omnivore Model
of vision datasets with different input modalities. Second,
it saves the research and engineering effort spent on opti-
                                                                                                      Linear
mizing models for a specific modality. For example, image
and video models have followed a similar trajectory of evo-
lution, from hand-crafted descriptors [47, 55] to convolu-            Image
tional networks [34, 91] and, eventually, vision transform-

                                                                                                                                Transformer
ers [5, 21]; however, each had to be developed and tuned
                                                                                                      Linear
individually. A common architecture would make scientific
progress readily available to users of any visual modality.
Finally, a model that operates on many visual modalities              Video
is naturally multi-modal and can easily leverage new visual                                           Linear
sensors as they becomes available. For instance, a modality-
agnostic recognition model running on a robot can readily                                                      +
exploit a new depth sensor when it is installed on that robot.
                                                                                                      Linear
Despite such clear advantages, modality-agnostic models
                                                                   Single-view 3D                                  Embeddings
have rarely been studied and their performance compared
to their modality-specific counterparts has been disappoint-
ing. There are many reasons that explain this situation, such    Figure 2. Multiple visual modalities in the O MNIVORE model.
                                                                 We convert image, video, and single-view 3D modalities into em-
as the need for a flexible architecture with enough capacity
                                                                 beddings that are fed into a Transformer model. The images are
to learn modality-specific cues from the different modali-
                                                                 converted into patches, videos into spatio-temporal tubes, and the
ties; and enough compute to train it on video, images, and       single-view 3D images are converted into RGB patches and depth
single-view 3D simultaneously.                                   patches. The patches are projected into embeddings using linear
   This paper develops a modality-agnostic vision model          layers. We use the same linear layer for (image or video) RGB
that leverages recent advances in vision architectures [21,      patches and a separate one for depth patches.
51]. The model we develop is “omnivorous” in that it
works on three different visual modalities: images, videos,
and single-view 3D. Our O MNIVORE model does not use             at par with recent large transformers on ImageNet-1K, sets
a custom architecture for each visual modality. It per-          a new state-of-the-art on action recognition benchmarks
forms recognition on all three modalities using the same,        such as EPIC-Kitchens-100, Something Something-v2, and
shared model parameters. It works by converting each in-         on single-view 3D classification and segmentation bench-
put modality into embeddings of spatio-temporal patches,         marks. We believe our work presents a compelling argu-
which are processed by exactly the same Transformer [92]         ment for shifting towards the development of vision models
to produce a representation of the input. We train O MNI -       that can operate on any visual modality.
VORE on a collection of standard, off-the-shelf classifica-
tion datasets that have different input modalities. Unlike       2. Related Work
prior work [33, 77], our training does not use explicit corre-       We build on prior work in ConvNet architectures, Trans-
spondences between different input modalities.                   formers, multi-modal learning, and multi-task learning.
    Our experiments demonstrate the advantages of our O M -      ConvNet architectures in vision. ConvNet architec-
NIVORE models.       Surprisingly, we find that O MNIVORE        tures [26, 48] have been popular for many computer vi-
representations generalize well across visual modalities         sion tasks in images, video, and 3D recognition. 2D con-
(see Figure 1) even though O MNIVORE was not explicitly          volutions are the main building block in ConvNets for im-
trained to model cross-modal correspondences. These ca-          ages [34, 46, 77, 84], whereas 3D convolutions are used on
pabilities emerge without explicit cross-modal supervision       3D data [18, 32] or are combined with 2D convolutions for
simply due to the parameter sharing between models for           recognition of videos [13, 90, 91]. I3D [13] introduced a
different modalities. On standard image, video, and single-      way to “inflate” 2D image convolutions into 3D convolu-
view 3D benchmarks, O MNIVORE performs at par with or            tions, which allows 3D ConvNets for videos and 3D data
better than modality-specific vision models with the same        to leverage image data indirectly via initialization from pre-
number of parameters. The same O MNIVORE model ob-               trained image models. Since video and 3D datasets are rela-
tains 85.6% top-1 accuracy on ImageNet-1K, 83.4% top-1           tively small, they benefit from inflated pretrained image net-
on Kinetics-400, and 67.4% top-1 accuracy on SUN RGB-            works. However, while the inflation technique is applicable
D. O MNIVORE’s strong generalization capabilities also ex-       only to model finetuning, O MNIVORE models are pretrained
tend to transfer learning experiments. O MNIVORE performs        jointly on images, videos, and single-view 3D data.
Transformers in vision. The Transformer architecture [92]       challenge in designing the model. To overcome this chal-
originally proposed for NLP tasks has been successfully ap-     lenge, we adopt the Transformer [92] architecture because
plied in computer vision on images [11, 21, 70, 88, 93, 94],    the self-attention mechanism gracefully handles variable-
video [5, 8, 28, 29, 52, 66], and 3D data [60, 68, 103].        sized inputs. Figure 2 presents an overview of our approach.
Models such as ViT [21], Swin [51], and MViT [24] per-
form competitively on benchmark tasks such as image clas-       3.1. The O MNIVORE Model
sification, detection, and video recognition. For example,          We convert all visual modalities into a common format
Swin [51, 52] and MViT [24] require minimal changes to be       by representing them via embeddings. Our model then uses
used in image or video recognition tasks. Similarly, the Per-   a series of spatio-temporal attention operations to construct
ceiver [38] can model image, point cloud, audio, and video      a unified representation of the different visual modalities.
inputs. However, all these studies train separate models for
                                                                Input patches. We represent the different types of visual
each visual modality. Instead, we train a single model on
                                                                input as a 4D tensor X ∈ RT ×H×W ×C , where T is the size
multiple input modalities simultaneously, which equips our
                                                                of the temporal dimension, H and W of the spatial dimen-
model with cross-modal generalization capabilities.
                                                                sions, and C of the channel dimension. Thus, RGB images
Multi-modal learning. Our work uses multiple visual
                                                                I ∈ R1×H×W ×3 have T = 1 frame with C = 3 channels,
modalities to train the model. Multi-modal learning archi-
                                                                RGB videos V ∈ RT ×H×W ×3 have T > 1 frames, and
tectures may involve training separate encoders for each
                                                                single-view 3D images D ∈ R1×H×W ×4 have T = 1 frame
type of input modality. For example, a range of tasks re-
                                                                with three RGB channels and one depth channel.
quire training separate encoders for images and text [15,
                                                                    We follow [21, 51, 52] and split the input into a col-
30, 41, 57, 59], for video and audio [3, 4, 62, 63, 67, 71],
                                                                lection of patches. We illustrate this process in Figure 2.
or for video and optical flow [77]. Recently, Transform-
                                                                Specifically, we convert the visual input X into a set of
ers have been used to fuse multiple modalities: Transform-
                                                                4D sub-tensors x of size t × h × w × c. Images I are
ers have been used to fuse features in vision-and-language
                                                                split into a set of non-overlapping image patches of size
tasks [2, 17, 37, 40, 49, 56, 83, 86] and video-and-audio
                                                                1×h×w ×3. Similarly, videos V are split into a set of non-
tasks [64], video-and-image tasks [7], and even tasks that
                                                                overlapping spatio-temporal patches of shape t × h × w × 3.
involve video, audio, and text [1]. Unlike our work, most
                                                                For single-view 3D images D, the image (RGB) and depth
prior work assumes that all input modalities are in cor-
                                                                (D) channels are converted separately into patches of size
respondence and available simultaneously, which restricts
                                                                1 × h × w × 3 and 1 × h × w × 1, respectively.
them to using only multi-modal datasets. In our work, we
                                                                Model architecture. Our model f maps the resulting
train a single model on different visual modalities without
                                                                spatio-temporal visual patches into a shared representation
assuming simultaneous access to all modalities. This allows
                                                                Φ for images, videos, and single-view 3D. We design the
us to leverage standard off-the-shelf single-modality vision
                                                                model to enable maximal parameter sharing across visual
datasets and we show that using a single shared encoder
                                                                modalities. The input layer of the model processes each
naturally leads to cross-modal generalization.
                                                                patch x independently, and projects the patches into an em-
Multi-task learning. Our work is also related to stud-
                                                                bedding e using a linear layer followed by a LayerNorm [6]
ies on multi-task learning [14], which develop models
                                                                (linear+LN). Each patch x of shape t × h × w × c is con-
that output predictions for multiple tasks on the same in-
                                                                verted into an embedding of size d. We use the same layers
put [23, 27, 44, 58, 61, 102]. Such multi-task learners are
                                                                to embed all the three-channel RGB patches, i.e., for image
known to work well when the target tasks exhibit strong
                                                                patches, video patches, and patches of the first three chan-
similarities [61, 99]. They differ from O MNIVORE in that
                                                                nels of a single-view 3D image. We zero-pad the single-
they operate on a single input modality but are trained to
                                                                frame patches on one side to ensure all patches have the
perform multiple tasks. By contrast, our models are trained
                                                                same shape, t × h × w × 3. We use a separate linear+LN
to perform a single task (i.e., classification) on a variety
                                                                layer to embed the depth-channel patches and add its output
of input modalities. Other multi-task learners operate on
                                                                to the embedding of the corresponding RGB patch.
multi-modal inputs [39], but they use hand-designed model
components for each modality.                                       We use the same model (parameters) to process all the re-
                                                                sulting embeddings. While O MNIVORE can use any vision
3. Approach                                                     transformer architecture [21, 24] to process the patch em-
                                                                beddings, we use the Swin transformer architecture [51] as
   Our goal is to learn a single model that can operate on      our base model given its strong performance on image and
three major visual modalities: images, videos, and single-      video tasks. We rely on the self-attention [92] operation for
view 3D. Because the model’s input modalities have dif-         spatio-temporal modeling across the patch embeddings, e.
ferent sizes and layouts—videos have a temporal axis and        Akin to [51], the self-attention involves patch embeddings
single-view 3D has an extra depth channel—this poses a          from spatially and temporally nearby patches. We also use
two sets of relative positional encodings: one for the spatial     Dataset                                 Task         #cls #train #val
                                                                   iNaturalist-2018 (iNat18) [36]     Fine-grained cls. 8142 437K 24K
dimension and the other for the temporal dimension.                Oxford-IIIT Pets (Pets) [69]       Fine-grained cls. 37 3.6K 3.6K
                                                                   Places-365 (P365) [105]               Scene cls.     365 1.8M 36K
3.2. Training the O MNIVORE Model                                  Something Something-v2 (SSv2) [31]    Action cls.     174 169K 25K
                                                                   EPIC-Kitchens-100 (EK100) [20]        Action cls.    3806 67K 10K
    The O MNIVORE model f creates a single embedding               NYU-v2 (NYU) [65]                     Scene cls.      10 794 653
f (X) = Φ for multiple types of visual inputs. We train            NYU-v2-seg (NYU-seg) [65]           Segmentation      40 794 653
our model using a collection of classification tasks that pro-
vide inputs {(Xi , yi )} with a visual input, Xi , and a label,   Table 1. Transfer datasets used to evaluate O MNIVORE on im-
                                                                  age, video and single-view 3D modalities. The table reports the
yi . For example, we train most O MNIVORE models jointly
                                                                  task, number of classes (#cls), number of training samples (#train),
on the ImageNet-1K dataset for image classification, the          and number of validation samples (#val) for each dataset.
Kinetics-400 dataset for action recognition, and the SUN
RGB-D dataset for single-view 3D scene classification.
    This approach is similar to multi-task learning [14] and
cross-modal alignment [15], but there important differ-           long, and are labeled into one of 400 action classes.
ences. In particular, we neither assume that the input ob-        Single-view 3D. The SUN RGB-D dataset has ∼5K train
servations are aligned (i.e., we do not assume access to cor-     and ∼5K val RGBD images with 19 scene classes. Follow-
respondences between images, videos, and 3D data) nor do          ing [74], we convert the depth maps into disparity maps.
we assume that these datasets share the same label space.
To achieve this, we employ dataset-specific linear classifi-      Implementation details. We use the Swin transformer [51,
cation layers on top of the final representation, Φ, produced     52] architecture as the backbone for O MNIVORE, and attach
by the model. The training loss of a sample is computed           linear heads for each target dataset. At training time, we use
based solely on the output of the classification layer that       a resolution of 224×224 and train using standard image aug-
corresponds to that sample’s source dataset.                      mentations [88] on ImageNet. For Kinetics, we sample 32
Loss and optimization. We train O MNIVORE to minimize             frames at stride 2. SUN RGB-D is processed similarly to
the cross-entropy loss on the training datasets using mini-       ImageNet but we randomly drop the RGB channels with a
batch SGD. We experiment with two different mini-batch            probability of 0.5 in order to encourage the model to use the
construction strategies for SGD. In our first strategy, we        depth channel for recognition as well. We provide complete
construct mini-batches from each dataset (modality) sepa-         implementation details in Appendix A. Our models are op-
rately. This strategy is easy to implement but alternating        timized using AdamW [53] for 500 epochs where a single
between datasets may potentially lead to training instabili-      epoch consists of one epoch each for ImageNet-1K and Ki-
ties. Hence, we experiment with a second strategy that con-       netics, and 10 epochs for SUN RGB-D.
structs mini-batches that mix samples from all datasets. We       Transfer datasets and metrics. We evaluate O MNIVORE
evaluate both mini-batch construction strategies in § 4.3.        in transfer learning experiments on a diverse set of image,
                                                                  video, and single-view 3D tasks; see Table 1 for a summary.
4. Experiments                                                    We present details on the experimental setup in Appendix B.
    We perform a series of experiments to assess the effec-       Images. We evaluate O MNIVORE on fine-grained object
tiveness of O MNIVORE. Specifically, we compare O MNI -           recognition on the iNaturalist-2018 dataset [36], fine-
VORE models to their modality-specific counterparts and to        grained classification on the Oxford-IIIT Pets dataset [69],
state-of-the-art models on a variety of recognition tasks. We     and in scene classification on the Places-365 dataset [105].
also ablate several design choices we made in O MNIVORE.
                                                                  Videos. We use the Something Something-v2 dataset, which
Pre-training datasets. We train O MNIVORE on images
                                                                  has a special emphasis on temporal modeling for action
from the ImageNet-1K dataset [75], videos from the Kinet-
                                                                  recognition. We also use the EPIC-Kitchens-100 dataset,
ics dataset [42], and single-view 3D images from the SUN
                                                                  which has 100 hours of unscripted egocentric video. Each
RGB-D dataset [79]. We measure the top-1 and top-5 clas-
                                                                  clip is labeled with a verb and a noun that together form an
sification accuracy of our models on the respective valida-
                                                                  action. Our model is trained to recognize all 3,806 actions,
tion sets. We note that the three datasets have negligible
                                                                  i.e., verb-noun pairs in the dataset. We marginalize over
overlap in their visual concepts: ImageNet-1K focuses on
                                                                  verbs to obtain noun predictions and vice versa.
object-centric classes, Kinetics-400 on action classes, and
SUN RGB-D on indoor scene classes.                                Single-view 3D. We use the NYU-v2 dataset for single-view
Images. The ImageNet-1K (IN1K) dataset has ∼1.2M train-           3D scene classification and segmentation. We follow the
ing and 50K validation images that comprise 1,000 classes.        setup from [33] for scene classification and [10, 33] for seg-
Videos. The Kinetics-400 (K400) dataset consists of ∼240K         mentation. For segmentation, we follow [51] and use the
training and 20K validation video clips that are 10 seconds       UPerNet [95] head with the Swin trunk.
                     6
                                                                                                  P365       iNat18        Pets       SSv2       EK100     NYU NYU-seg
                                                                       Model    Method
F1 on Kinetics-400

                     5                                                                         top-1 top-5 top-1 top-5 top-1 top-5 top-1 top-5 top-1 top-5 top-1 mIoU
                     4
                     3                                                        Specific         57.9   87.3   69.7   87.6   93.7   99.6   62.2   88.7   41.8   62.8   72.5   47.9
                                                                       Swin-T
                     2                                                        O MNIVORE        58.2   87.4   69.0   87.7   94.2   99.7   64.4   89.7   42.7   63.1   77.3   49.7
                     1
                     0                                                        Specific         58.7   88.1   72.9   90.2   94.4   99.6   66.8   91.1   42.5   63.4   76.7   51.3
                                                                       Swin-S
                                 martial arts
                                    dancing
                         racquet + bat sports
                            touching person
                                     heights
                                 gymnastics
                           eating + drinking
                                       hands
                              playing games
                            mobility - water
                           auto maintenance
                                    athletics
                               body motions
                               head + mouth
                                         golf
                                                                              O MNIVORE        58.8   88.0   73.6   90.8   95.2   99.7   68.2   91.8   44.9   64.8   76.9   52.7
                                                                              Specific         58.9   88.3   73.2   90.9   94.2   99.7   65.8   90.6   42.8   64.0   76.4   51.1
                                                                       Swin-B
                                                                              O MNIVORE        59.2   88.3   74.4   91.1   95.1   99.8   68.3   92.1   47.4   67.7   79.4   54.0

                                                                      Table 3. Comparing O MNIVORE with modality-specific models after finetuning the models
Figure 3. Comparing O MNIVORE                                         on seven downstream tasks. Results are presented for three different model sizes: T, S, and B.
with VideoSwin on K400. O MNIVORE                                     Our image specific model is pretrained on IN1K. The video specific and single-view 3D specific
improves over VideoSwin on F1 score                                   models are both initialized using inflation from the pretrained image-specific model and fine-
on all 38 class groups defined in [42]                                tuned on K400 and SUN RGB-D respectively. O MNIVORE models are at par with or outperform
(top 15 shown here for brevity).                                      modality-specific models on nearly all downstream tasks.

                                                   ImageNet-1K         Kinetics-400    SUN              NIVORE to modality-specific models on the pretraining
                     Method
                                                   top-1 top-5         top-1 top-5     top-1
                                                                                                        datasets. The results in the table show that across model
                     ImageSwin-T [51]               81.2     95.5       ✗        ✗      ✗               sizes, O MNIVORE models match or exceed the performance
                     VideoSwin-T [52]                ✗        ✗        78.8     93.6    ✗               of their modality-specific counterparts. This observation
                     DepthSwin-T                     ✗        ✗         ✗        ✗     63.1
                     O MNIVORE (Swin-T)             80.9     95.5      78.9     93.8   62.3
                                                                                                        supports our hypothesis that it is possible to learn a sin-
                     ImageSwin-S [51]               83.2     96.2       ✗        ✗      ✗               gle visual representation that works across visual modal-
                     VideoSwin-S [52]                ✗        ✗        80.6     94.5    ✗               ities. O MNIVORE learns representations that are as good
                     DepthSwin-S                     ✗        ✗         ✗        ✗     64.9             as modality-specific representations using the same train-
                     O MNIVORE (Swin-S)             83.4     96.6      82.2     95.4   64.6             ing data, same model parameters and same model capacity.
                     ImageSwin-B [51]               83.5     96.5       ✗        ✗      ✗               This implies that O MNIVORE provides a viable alternative
                     VideoSwin-B [52]                ✗        ✗        80.6     94.6    ✗
                     DepthSwin-B                     ✗        ✗         ✗        ✗     64.8
                                                                                                        to the pretrain-then-finetune paradigm commonly used to
                     O MNIVORE (Swin-B)             84.0     96.8      83.3     95.8   65.4             deploy modality-specific models: it can deliver the same or
                                                                                                        better recognition accuracy with a third of the parameters.
Table 2. O MNIVORE vs. modality-specific models that have                                                  From our results, we also observe that higher-capacity
the same model architecture and number of parameters. O MNI -
                                                                                                        models benefit more from omnivorous training. O MNI -
VORE is a single model trained from scratch jointly on the IN1K,
                                                                                                        VORE models using the larger Swin-B architecture improve
K400 and SUN datasets whereas the modality-specific models are
trained specifically for each dataset (modality). The ImageSwin                                         over their modality-specific counterparts on both IN1K and
model is trained from scratch while the VideoSwin and Depth-                                            K400, whereas the smallest Swin-T model does not.
Swin models are finetuned from the ImageSwin model. O MNI -                                                 Figure 3 presents a detailed analysis of the improve-
VORE performs at-par or outperforms modality-specific models.                                           ments of O MNIVORE over the VideoSwin baseline (both
                                                                                                        using the Swin-B architecture) on the K400 dataset. Here
                                                                                                        VideoSwin is pre-trained on IN1K and finetuned on K400,
4.1. Comparison with Modality-Specific Models                                                           whereas O MNIVORE is trained jointly on IN1K, K400, and
    We compare O MNIVORE to models trained on a spe-                                                    SUN RGB-D. Both models use the the Swin-B architecture.
cific visual modality. We train O MNIVORE from scratch                                                  O MNIVORE particularly improves the recognition of classes
jointly on the IN1K, K400, and SUN datasets. Our                                                        that require reasoning about parts of the human body such
modality-specific baseline models use the same Swin trans-                                              as the hands, arms, head, mouth, hair etc. We surmise this is
former architecture as O MNIVORE; we refer to them as Im-                                               because joint training on images helps O MNIVORE to learn
ageSwin, VideoSwin, and DepthSwin. Excluding the patch-                                                 a better model of the spatial configuration of parts.
embedding linear layers, these models have the same num-                                                Transfer learning performance. We compare O MNIVORE
ber of parameters as O MNIVORE. Following standard prac-                                                to modality-specific models by finetuning on various down-
tice [51, 52], the ImageSwin model is trained on IN1K,                                                  stream tasks. Table 3 presents the results of these exper-
whereas VideoSwin and DepthSwin models are finetuned                                                    iments. We observe that O MNIVORE transfers better than
by inflating the ImageSwin model. We experiment with                                                    modality-specific models on nearly all downstream tasks. In
three model sizes: viz., Swin-T, Swin-S, and Swin-B.1                                                   particular, O MNIVORE provides significant gains on video-
Pretraining performance. In Table 2, we compare O M -                                                   recognition tasks, even though it does not get any additional
                                                                                                        video supervision during pre-training compared to the base-
                         1 We refer to [51] for details on these model sizes.                           line. We reiterate that O MNIVORE has the same model ca-
                           ImageNet-1K       Kinetics-400     SUN                   Method                     P365   iNat18   Pets
  Method
                           top-1 top-5       top-1 top-5      top-1                 EfficientNet B6 [78, 96]   58.5    79.1    95.4
  MViT-B-24 [24]            83.1      -        ✗       ✗        ✗                   EfficientNet B7 [78, 96]   58.7    80.6     –
  ViT-L/16 [21]             85.3      -        ✗       ✗        ✗                   EfficientNet B8 [78, 96]   58.6    81.3     –
  ImageSwin-B [51]          85.2     97.5      ✗       ✗        ✗                   DeiT-B [88] ↑               –      79.5     –
  ImageSwin-L [51]          86.3     97.9      ✗       ✗        ✗                   ViT-B/16 [21, 78] ↑        58.2    79.8     –
  ViT-B-VTN [66]             ✗        ✗       79.8    94.2      ✗                   ViT-L/16 [21, 78] ↑        59.0    81.7     –
  TimeSformer-L [8]          ✗        ✗       80.7    94.7      ✗                   O MNIVORE (Swin-B)         59.3    76.3    95.5
  ViViT-L/16x2 320 [5]       ✗        ✗       81.3    94.7      ✗                   O MNIVORE (Swin-B ↑)       59.6    82.6    95.9
                                                                                    O MNIVORE (Swin-L)         59.4    78.0    95.7
  MViT-B 64×3 [24]           ✗        ✗       81.2    95.1      ✗
                                                                                    O MNIVORE (Swin-L ↑)       59.9    84.1    96.1
  VideoSwin-B [52]           ✗        ✗       82.7    95.5      ✗
  VideoSwin-L [52]           ✗        ✗       83.1    95.9      ✗
                                                                          Table 5. Comparing O MNIVORE with state-of-the-art models
  DF2 Net [50]               ✗        ✗        ✗       ✗       54.6
  G-L-SOOR [80]              ✗        ✗        ✗       ✗       55.5       in image classification finetuning experiments on three datasets.
  TRecgNet [22]              ✗        ✗        ✗       ✗       56.7       O MNIVORE representations generalize well to scene classification
  CNN-RNN [9]                ✗        ✗        ✗       ✗       60.7       (P365) and fine-grained classification (iNat18, Pets). ↑ indicates
  Depth Swin-B               ✗        ✗        ✗       ✗       69.1       finetuning on a higher resolution image (384×384px; see [89]).
  Depth Swin-L               ✗        ✗        ✗       ✗       68.7
  O MNIVORE (Swin-B)        85.3     97.5     84.0    96.2     67.2
  O MNIVORE (Swin-L)        86.0     97.7     84.1    96.3     67.1       Transfer learning performance. We compare O MNIVORE
                                                                          models to modality-specific models by finetuning on down-
Table 4. Comparing O MNIVORE with state-of-the-art models                 stream tasks. In Table 5, we report results on image classi-
on the image, video, and single-view 3D classification datasets
                                                                          fication. O MNIVORE models outperform prior state-of-the-
used to pre-train O MNIVORE. O MNIVORE performs on par with
                                                                          art in scene classification on Places-365, and in fine-grained
or better than state-of-the-art models on all three pre-training tasks,
including modality-specific models of similar size.                       classification on iNaturalist-2018 and Oxford-IIIT Pets.
                                                                              We finetune O MNIVORE on video-classification and re-
                                                                          port the results in Table 6. On the EPIC-Kitchens-100
pacity as the modality-specific baselines. This observation               dataset, the O MNIVORE Swin-B model achieves the ab-
underscores one of the key benefits of multi-modal training:              solute best performance across verb, noun, and verb-noun
because O MNIVORE was pretrained jointly on more diverse                  pair (action) classification. Similarly, on the SSv2 dataset,
training data, it generalizes better out-of-distribution. As              which requires temporal reasoning, O MNIVORE outper-
before, Table 3 also shows that higher-capacity models ben-               forms all prior work. This suggests that O MNIVORE repre-
efit the most from omnivorous training.                                   sentations transfer well to temporal-reasoning tasks – O M -
                                                                          NIVORE sets a new state-of-the-art while outperforming ar-
4.2. Comparison with the state-of-the-art                                 chitectures specialized for these video tasks.
   Next, we perform experiments comparing O MNIVORE to                        Finally, in Table 7, we report finetuning results for
existing state-of-the-art models. In these experiments, like              RGBD scene classification and segmentation. While prior
many state-of-the-art modality-specific methods, we use the               work relies on specialized 3D operators [10], fusion tech-
ImageNet-21K (IN21K) dataset during pretraining. The                      niques [97], or depth encoding schemes [33], O MNIVORE
O MNIVORE Swin-B and Swin-L models are trained from                       uses a generic architecture and operates directly on dispar-
scratch on IN21K, IN1K, K400, and SUN, where a sin-                       ity. O MNIVORE achieves state-of-the-art performance on
gle epoch consists of one epoch each of IN1K and K400,                    both the scene classification and segmentation tasks.
10 epochs of SUN, and 0.1 epochs of ImageNet-21K. Ta-
                                                                          4.3. Ablation Study
ble 4 compares the performance of the O MNIVORE models
to state-of-the-art models on each of the three benchmarks.                  We ablate some of O MNIVORE’s key design choices
O MNIVORE performs at par with or exceeds modality-                       in Table 8. Together, the results suggest O MNIVORE’s per-
specific methods despite using a model architecture that is               formance is relatively stable under different design choices.
not tailored towards any specific modality. Even when com-                For a faster turnaround time in the ablations, we train the
pared to modality-specific models with a similar number of                model for 300 epochs.
parameters, O MNIVORE models match the state-of-the-art                   Training from scratch or finetuning. We compare train-
on IN1K, and outperform the previous state-of-the-art on                  ing O MNIVORE models from scratch on different modalities
K400 by achieving 84.1% accuracy – a gain of 1% which                     (top row) with initializing the model via image classifica-
was previously only possible by using additional large video              tion followed by finetuning on all modalities (second row).
datasets. This demonstrates the strong performance of us-                 For the finetuning result, we initialize O MNIVORE (Swin-B)
ing the same O MNIVORE model across image, video and                      using a pretrained ImageNet-21K model followed by joint
single-view 3D benchmarks.                                                finetuning on IN1K, K400, and SUN for 100 epochs. The
                                  EK100                 SSv2          (which alternates between datasets during training) does not
  Method                   verb   noun action       top-1 top-5       lead to instabilities during training. Additionally, since it is
  RGB-only methods
                                                                      easier to implement, we use it to train O MNIVORE.
  SlowFast [25]            65.6    50.0    38.5     63.0     88.5
  TimeSformer [8]           –       –       –       62.4      –       Patch embedding model for depth channel. O MNIVORE
  MViT-B-24 [24]            –       –       –       68.7     91.5     uses a separate linear+LN layer for the depth channel in
  TAR [76]                 66.0    53.4    45.3      –        –       RGBD images. We compare this to using a four-channel
  VIMPAC [87]               –       –       –       68.1      –       convolutional model to embed depth patches instead, and
  ViViT-L [5]              66.4    56.8    44.0     65.9     89.9     find that the separate layer leads to better performance on
  MFormer-L [72]           67.1    57.6    44.1     68.1     91.2     SUN. We also observed that using the separate layer helps
  ORViT [35]               68.4    58.7    45.7     69.5     91.5
                                                                      O MNIVORE transfer better to downstream RGBD tasks.
  C OV E R [100]            –       –       –       70.9      –
  VideoSwin-B [52]         67.8    57.0    46.1     69.6     92.7
  O MNIVORE (Swin-B)       69.5    61.7    49.9     71.4     93.5     5. Cross-Modal Generalization
  Multi-modal methods
  MML [45]                  –       –       –       69.1     92.1         A key advantage of O MNIVORE over modality-specific
  MTCN [43]                70.7    62.1    49.6      –        –       models is that it can generalize across visual modalities.
                                                                      This generalization emerges naturally because we use the
Table 6. Comparing O MNIVORE with state-of-the-art models             same model for all modalities. Our model is neither trained
in video classification finetuning experiments on two datasets.       with corresponding data across modalities nor with any
We highlighted columns that show the two primary classification       cross-modal consistency losses.
metrics used in prior work. O MNIVORE models obtain state-of-         Retrieval across images and depth. We use the O MNI -
the-art results on both datasets, even outperforming some multi-
                                                                      VORE representation to retrieve depth maps given an RGB
modal methods.
                                                                      image. To create a database of depth maps, we run a
                                                                      monocular depth-prediction model [74] on the ImageNet-
  Method                       Classification     Segmentation
                                                                      1K train set. We note that O MNIVORE was not trained on
     2
  DF Net [50]                       65.4               ✗              ImageNet-1K depth maps nor on predicted depth. We use
  TRecgNet [22]                     69.2               ✗              the ImageNet-1K val set (RGB) images as queries. Fig-
  ShapeConv [10]                     ✗                51.3            ure 4 shows five examples of retrieved maps. These results
  BCMFP + SA-Gate [16]               ✗                52.4            illustrate that O MNIVORE constructs good depth-map rep-
  TCD [97]                           ✗                53.1
                                                                      resentations, even though it had not previously observed
  O MNIVORE (Swin-B)                80.0              55.1
                                                                      ImageNet-1K depth maps during training. We emphasize
  O MNIVORE (Swin-L)                80.3              56.8
                                                                      that this cross-modal generalization ability is not the re-
Table 7. Comparing O MNIVORE with state-of-the-art models             sult of explicitly learning correspondences between visual
in RGBD finetuning experiments on the NYU-v2 dataset. The             modalities [33, 77]. Instead, it emerges due to the use of an
left column shows the scene classification accuracy while the right   almost entirely shared encoder for those modalities.
column shows the mean intersection-over-union of semantic seg-
mentation. O MNIVORE outperforms prior art in RGBD classifica-
tion and segmentation.                                                                                            IN1K     K400    SUN
                                                                        Baseline                                  85.2     83.2    65.5
                                                                        Finetuned                                 –0.7     –0.9    +0.9
model trained from scratch performs better in both image                Data ratio                0.1:1:1:1       –0.1     +0.3    –0.7
                                                                        IN21K:IN1K:K400:SUN       0.1:1:1:10       +0      +0.1    +0.6
and video classification.
                                                                                                  0.1:1:1:20       +0      +0.2    +0.6
Data ratio. Since the IN1K and K400 datasets are much                                             0.1:1:1:100     –0.1     –0.1    –2.1
larger than SUN, we replicate SUN when training O MNI -                                           0.3:1:1:50      +0.1     –1.3    +1.5
VORE . Although replication helps, a higher replication fac-                                      0.6:1:1:50      –0.2     –3.1    +1.0
tor hurts the model performance on SUN (which hints at                                            1.0:1:1:50      –0.1     –4.5    +2.0
overfitting), whereas the performance on IN1K and K400 is               Batching                  Mixed           –0.2     –0.1    –0.4
                                                                        Patch embedding           RGBD Conv.      –0.1     +0.1    –2.2
unchanged. Based on the same logic, we undersample the
IN21K dataset to have a similar size as IN1K. Increasing              Table 8. Ablation study of design choices made when training
the proportion of IN21K has no effect on IN1K, decreases              O MNIVORE. Our baseline settings use a data ratio of 0.1:1:1:50,
performance on K400, and improves performance on SUN.                 the separate batching strategy, linear layers for embedding RGB
Hence, we use the 0.1:1:1:10 setting for our final model.             and depth channels, and 300 epoch training. O MNIVORE’s per-
Batching strategy. We evaluate the two different batching             formance is robust under different decisions. O MNIVORE trained
strategies described in § 3, and observe that they perform            from scratch (top row) performs slightly better than a jointly fine-
similarly. We also find that the separate batching strategy           tuned model (second row).
Query Retrieved depth maps −−−−−−−−−−→

                                                                         Top-1 accuracy
                                                                                          80
                                                                                          70
                                                                                          60                         VideoSwin-B
                                                                                                                      O MNIVORE
                                                                                          50
                                                                                               1         2      4     8      16     32
                                                                                                   Clip length (number of frames)
                                                                  Figure 5. Accuracy as a function of clip length on the K400
                                                                  dataset. Models are trained on 32-frame clips but evaluated on
                                                                  clips of different length (with the same fps used for frame sam-
                                                                  pling). The performance of O MNIVORE degrades more gracefully
                                                                  than that of the VideoSwin-B model, and is still effective when
Figure 4. Retrieving depth maps given RGB images on the           doing frame-level inference (i.e., when the clip length is 1).
ImageNet-1K dataset. We show retrieved depth maps from the
IN1K training set (right) for RGB image queries from the IN1K
validation set (left). Although O MNIVORE was not trained on      full 10 second video at inference time. In this experiment,
IN1K depth maps, the shared visual representation enables it to   we vary the clip length from 1 to 32, increasing the number
retrieve depth maps that are semantically similar to the query.   of clips proportionally to still cover the full video in each
                                                                  case. The results show that O MNIVORE’s performance de-
Classifying based on different modalities.                        grades more gracefully as the video length decreases. No-
                                                                  tably, O MNIVORE outperforms the baseline by 18.5% at a
        Method             RGB D RGBD                             clip length of 1 frame (frame-level inference). This suggests
        O MNIVORE (Swin-B) 84.3 63.1 83.7                         that joint training on images and videos enables the model
                                                                  to use both temporal and spatial cues effectively.
To quantitatively measure O MNIVORE’s generalization per-
formance across different modalities, we perform k-nearest        6. Discussion and Limitations
neighbor (k-NN, k = 20) classification experiments on the
ImageNet-1K dataset using the predicted depth maps. We                Although O MNIVORE presents an advance over tra-
extract O MNIVORE representations from the RGB images             ditional modality-specific models, it has several limita-
on the val set and measure the model’s ability to retrieve        tions. Current implementation of O MNIVORE only works
images, RGBD images, and depth-only images from the               on single-view 3D images and does not generalize to other
train set. We observe that O MNIVORE produces a rep-              3D representations such as voxels, point clouds, etc. A sim-
resentation that allows for successful k-NN classification,       ple approach to deal with such inputs may be to render mul-
which demonstrates its strong generalization performance.         tiple single-view 3D images from such inputs and average
Surprisingly, we observe a high accuracy is attained even         our predictions over those images, but such an approach
when retrieving depth-images, which provide less informa-         would not effectively leverage multi-view information. An-
tion about the object class than RGB images.                      other caveat is that depth inputs are not scale-invariant; we
Retrieval across all modalities. We further probe the             used normalizations to alleviate this issue [74]. Also, O M -
O MNIVORE visual representations in retrieval experiments         NIVORE focuses only on visual modalities, so co-occurring
across images, videos, and depth maps. We use the RGB             modalities such as audio are not used. O MNIVORE was pre-
images from the ImageNet-1K val set as queries and use            trained using only classification; using structured prediction
them to retrieve similar depth maps from ImageNet-1K              tasks such as segmentation might yield richer representa-
(predicted depth) and videos from Kinetics-400. Figure 1          tions. We leave such extensions to future work.
shows examples of the resulting retrievals. The results illus-    Ethical Considerations. Our study focuses on technical in-
trate how O MNIVORE supports retrieval of visual concepts         novations in training models for visual recognition. These
across images (RGB), single-view 3D (RGBD), and videos            innovations themselves appear to be neutral from an ethics
(RGBT) using its shared representation space.                     point-of-view. However, all ethical considerations that ap-
Bridging frame-based and clip-based video models.                 ply to other visual-recognition models apply equally to O M -
O MNIVORE’s cross-modality generalization capabilities            NIVORE . Any real-world deployment of a model like O M -
also make it more robust to changes in lengths of videos          NIVORE is best preceded by a careful analysis of that model
to be classified. We demonstrate this in in Figure 5, where       for ethical problems, including but not limited to: perfor-
we classify videos using different length clips at inference      mance disparities between different user groups, associa-
time. The model is trained with 32 frames at stride 2, and by     tions that may be harmful to some users, and predictions
default uses 4 clips of the same length and stride to cover the   that may propagate stereotypes.
References                                                               Uniter: Universal image-text representation learning. In
                                                                         ECCV, 2020.
 [1] Hassan Akbari, Linagzhe Yuan, Rui Qian, Wei-Hong               [18] Christopher Choy, JunYoung Gwak, and Silvio Savarese.
     Chuang, Shih-Fu Chang, Yin Cui, and Boqing Gong.                    4d spatio-temporal convnets: Minkowski convolutional
     Vatt: Transformers for multimodal self-supervised learn-            neural networks. In CVPR, 2019.
     ing from raw video, audio and text. arXiv preprint             [19] Ekin D Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V
     arXiv:2104.11178, 2021.                                             Le. Randaugment: Practical automated data augmentation
 [2] Jean-Baptiste Alayrac, Adria Recasens, Rosalia Schneider,           with a reduced search space. In CVPR, 2020.
     Relja Arandjelovic, Jason Ramapuram, Jeffrey De Fauw,          [20] Dima Damen, Hazel Doughty, Giovanni Maria Farinella,
     Lucas Smaira, Sander Dieleman, and Andrew Zisserman.                Antonino Furnari, Evangelos Kazakos, Jian Ma, Davide
     Self-supervised multimodal versatile networks. NeurIPS,             Moltisanti, Jonathan Munro, Toby Perrett, Will Price, et al.
     2020.                                                               Rescaling egocentric vision. IJCV, 2021.
 [3] Relja Arandjelovic and Andrew Zisserman. Look, listen          [21] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
     and learn. In ICCV, 2017.                                           Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
 [4] Relja Arandjelovic and Andrew Zisserman. Objects that               Mostafa Dehghani, Matthias Minderer, Georg Heigold,
     sound. In ECCV, 2018.                                               Sylvain Gelly, et al. An image is worth 16x16 words: Trans-
 [5] Anurag Arnab, Mostafa Dehghani, Georg Heigold, Chen                 formers for image recognition at scale. In ICLR, 2021.
     Sun, Mario Lucic, and Cordelia Schmid. ViViT: A video          [22] Dapeng Du, Limin Wang, Huiling Wang, Kai Zhao, and
     vision transformer. In ICCV, 2021.                                  Gangshan Wu. Translate-to-recognize networks for rgb-d
 [6] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton.              scene recognition. In CVPR, 2019.
     Layer normalization. arXiv preprint arXiv:1607.06450,          [23] David Eigen and Rob Fergus. Predicting depth, surface nor-
     2016.                                                               mals and semantic labels with a common multi-scale con-
 [7] Max Bain, Arsha Nagrani, Gül Varol, and Andrew Zisser-             volutional architecture. In ICCV, 2015.
     man. Frozen in time: A joint video and image encoder           [24] Haoqi Fan, Bo Xiong, Karttikeya Mangalam, Yanghao Li,
     for end-to-end retrieval. arXiv preprint arXiv:2104.00650,          Zhicheng Yan, Jitendra Malik, and Christoph Feichten-
     2021.                                                               hofer. Multiscale vision transformers. In ICCV, 2021.
 [8] Gedas Bertasius, Heng Wang, and Lorenzo Torresani. Is          [25] Christoph Feichtenhofer, Haoqi Fan, Jitendra Malik, and
     space-time attention all you need for video understanding?          Kaiming He. Slowfast networks for video recognition. In
     In ICML, 2021.                                                      ICCV, 2019.
 [9] Ali Caglayan, Nevrez Imamoglu, Ahmet Burak Can, and            [26] Kunihiko Fukushima. A self-organizing neural network
     Ryosuke Nakamura. When cnns meet random rnns: To-                   model for a mechanism of pattern recognition unaffected
     wards multi-level analysis for rgb-d object and scene recog-        by shift in position. Biol. Cybern., 1980.
     nition. arXiv preprint arXiv:2004.12349, 2020.                 [27] Golnaz Ghiasi, Barret Zoph, Ekin D Cubuk, Quoc V Le,
[10] Jinming Cao, Hanchao Leng, Dani Lischinski, Danny                   and Tsung-Yi Lin. Multi-task self-training for learning gen-
     Cohen-Or, Changhe Tu, and Yangyan Li. Shapeconv:                    eral representations. In ICCV, 2021.
     Shape-aware convolutional layer for indoor rgb-d semantic      [28] Rohit Girdhar, João Carreira, Carl Doersch, and Andrew
     segmentation. In ICCV, 2021.                                        Zisserman. Video action transformer network. In CVPR,
[11] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nico-            2019.
     las Usunier, Alexander Kirillov, and Sergey Zagoruyko.         [29] Rohit Girdhar and Kristen Grauman. Anticipative Video
     End-to-end object detection with transformers. In ECCV,             Transformer. In ICCV, 2021.
     2020.                                                          [30] Yunchao Gong, Liwei Wang, Micah Hodosh, Julia Hocken-
[12] Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou,           maier, and Svetlana Lazebnik. Improving image-sentence
     Julien Mairal, Piotr Bojanowski, and Armand Joulin.                 embeddings using large weakly annotated photo collec-
     Emerging properties in self-supervised vision transformers.         tions. In ECCV, 2014.
     In ICCV, 2021.                                                 [31] Raghav Goyal, Samira Ebrahimi Kahou, Vincent Michal-
[13] João Carreira and Andrew Zisserman. Quo vadis, action              ski, Joanna Materzynska, Susanne Westphal, Heuna Kim,
     recognition? a new model and the kinetics dataset. In               Valentin Haenel, Ingo Fruend, Peter Yianilos, Moritz
     CVPR, 2017.                                                         Mueller-Freitag, Florian Hoppe, Christian Thurau, Ingo
[14] Rich Caruana. Multitask learning. Machine Learning,                 Bax, and Roland Memisevic. The “something something”
     1997.                                                               video database for learning and evaluating visual common
[15] Lluis Castrejon, Yusuf Aytar, Carl Vondrick, Hamed Pirsi-           sense. In ICCV, 2017.
     avash, and Antonio Torralba. Learning aligned cross-modal      [32] Benjamin Graham, Martin Engelcke, and Laurens van der
     representations from weakly aligned data. In CVPR, 2016.            Maaten. 3d semantic segmentation with submanifold sparse
[16] Xiaokang Chen, Kwan-Yee Lin, Jingbo Wang, Wayne Wu,                 convolutional networks. In CVPR, 2018.
     Chen Qian, Hongsheng Li, and Gang Zeng. Bi-directional         [33] Saurabh Gupta, Pablo Arbelaez, and Jitendra Malik. Per-
     cross-modality feature propagation with separation-and-             ceptual organization and recognition of indoor scenes from
     aggregation gate for rgb-d semantic segmentation. In                rgb-d images. In CVPR, 2013.
     ECCV, 2020.                                                    [34] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
[17] Yen-Chun Chen, Linjie Li, Licheng Yu, Ahmed El Kholy,               Deep residual learning for image recognition. In CVPR,
     Faisal Ahmed, Zhe Gan, Yu Cheng, and Jingjing Liu.
     2016.                                                                        Zhang, Stephen Lin, and Baining Guo. Swin transformer:
[35] Roei Herzig, Elad Ben-Avraham, Karttikeya Mangalam,                          Hierarchical vision transformer using shifted windows. In
     Amir Bar, Gal Chechik, Anna Rohrbach, Trevor Darrell,                        ICCV, 2021.
     and Amir Globerson. Object-region video transformers.                   [52] Ze Liu, Jia Ning, Yue Cao, Yixuan Wei, Zheng Zhang,
     arXiv preprint arXiv:2110.06915, 2021.                                       Stephen Lin, and Han Hu. Video swin transformer. arXiv
[36] Grant Van Horn, Oisin Mac Aodha, Yang Song, Yin Cui,                         preprint arXiv:2106.13230, 2021.
     Chen Sun, Alex Shepard, Hartwig Adam, Pietro Perona,                    [53] Ilya Loshchilov and Frank Hutter. Decoupled weight decay
     and Serge Belongie. The inaturalist species classification                   regularization. arXiv preprint arXiv:1711.05101, 2017.
     and detection dataset. In CVPR, 2018.                                   [54] Ilya Loshchilov and Frank Hutter. Sgdr: Stochastic gradient
[37] Ronghang Hu and Amanpreet Singh. Unit: Multimodal                            descent with warm restarts. In ICLR, 2017.
     multitask learning with a unified transformer. In ICCV,                 [55] David G Lowe. Distinctive image features from scale-
     2021.                                                                        invariant keypoints. IJCV, 2004.
[38] Andrew Jaegle, Felix Gimeno, Andrew Brock, Andrew Zis-                  [56] Jiasen Lu, Dhruv Batra, Devi Parikh, and Stefan Lee.
     serman, Oriol Vinyals, and Joao Carreira. Perceiver: Gen-                    Vilbert: Pretraining task-agnostic visiolinguistic repre-
     eral perception with iterative attention. ICML, 2021.                        sentations for vision-and-language tasks. arXiv preprint
[39] Lukasz Kaiser, Aidan N Gomez, Noam Shazeer, Ashish                           arXiv:1908.02265, 2019.
     Vaswani, Niki Parmar, Llion Jones, and Jakob Uszko-                     [57] Jiasen Lu, Vedanuj Goswami, Marcus Rohrbach, Devi
     reit. One model to learn them all. arXiv preprint                            Parikh, and Stefan Lee. 12-in-1: Multi-task vision and lan-
     arXiv:1706.05137, 2017.                                                      guage representation learning. In CVPR, 2020.
[40] Aishwarya Kamath, Mannat Singh, Yann LeCun, Gabriel                     [58] Kevis-Kokitsi Maninis, Ilija Radosavovic, and Iasonas
     Synnaeve, Ishan Misra, and Nicolas Carion. Mdetr-                            Kokkinos. Attentive single-tasking of multiple tasks. In
     modulated detection for end-to-end multi-modal under-                        CVPR, 2019.
     standing. In ICCV, 2021.                                                [59] Antoine Miech, Jean-Baptiste Alayrac, Lucas Smaira, Ivan
[41] Andrej Karpathy and Li Fei-Fei. Deep visual-semantic                         Laptev, Josef Sivic, and Andrew Zisserman. End-to-end
     alignments for generating image descriptions. In CVPR,                       learning of visual representations from uncurated instruc-
     2015.                                                                        tional videos. In CVPR, 2020.
[42] Will Kay, Joao Carreira, Karen Simonyan, Brian Zhang,                   [60] Ishan Misra, Rohit Girdhar, and Armand Joulin. An End-to-
     Chloe Hillier, Sudheendra Vijayanarasimhan, Fabio Vi-                        End Transformer Model for 3D Object Detection. In ICCV,
     ola, Tim Green, Trevor Back, Paul Natsev, et al. The                         2021.
     kinetics human action video dataset.                  arXiv preprint    [61] Ishan Misra, Abhinav Shrivastava, Abhinav Gupta, and
     arXiv:1705.06950, 2017.                                                      Martial Hebert. Cross-stitch networks for multi-task learn-
[43] Evangelos Kazakos, Jaesung Huh, Arsha Nagrani, Andrew                        ing. In CVPR, 2016.
     Zisserman, and Dima Damen. With a little help from my                   [62] Pedro Morgado, Ishan Misra, and Nuno Vasconcelos. Ro-
     temporal context: Multimodal egocentric action recogni-                      bust audio-visual instance discrimination. In CVPR, 2021.
     tion. In BMVC, 2021.                                                    [63] Pedro Morgado, Nuno Vasconcelos, and Ishan Misra.
[44] Iasonas Kokkinos. UberNet: Training a universal convolu-                     Audio-visual instance discrimination with cross-modal
     tional neural network for low-, mid-, and high-level vision                  agreement. In CVPR, 2021.
     using diverse datasets and limited memory. In CVPR, 2017.               [64] Arsha Nagrani, Shan Yang, Anurag Arnab, Aren Jansen,
[45] Stepan Komkov, Maksim Dzabraev, and Aleksandr                                Cordelia Schmid, and Chen Sun. Attention bottlenecks for
     Petiushko. Mutual modality learning for video action clas-                   multimodal fusion. In NeurIPS, 2021.
     sification. arXiv preprint arXiv:2011.02543, 2020.                      [65] Pushmeet Kohli Nathan Silberman, Derek Hoiem and Rob
[46] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.                      Fergus. Indoor segmentation and support inference from
     Imagenet classification with deep convolutional neural net-                  rgbd images. In ECCV, 2012.
     works. NeurIPS, 2012.                                                   [66] Daniel Neimark, Omri Bar, Maya Zohar, and Dotan As-
[47] Ivan Laptev and Tony Lindeberg. Space-time interest                          selmann. Video transformer network. arXiv preprint
     points. In ICCV, 2003.                                                       arXiv:2102.00719, 2021.
[48] Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick                    [67] Andrew Owens and Alexei A Efros. Audio-visual scene
     Haffner. Gradient-based learning applied to document                         analysis with self-supervised multisensory features. In
     recognition. Proceedings of the IEEE, 1998.                                  ECCV, 2018.
[49] Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xi-                    [68] Xuran Pan, Zhuofan Xia, Shiji Song, Li Erran Li, and Gao
     aowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu, Li Dong,                       Huang. 3d object detection with pointformer. In CVPR,
     Furu Wei, Yejin Choi, and Jianfeng Gao. Oscar: Object-                       2021.
     semantics aligned pre-training for vision-language tasks. In            [69] Omkar M Parkhi, Andrea Vedaldi, Andrew Zisserman, and
     ECCV, 2020.                                                                  CV Jawahar. Cats and dogs. In CVPR, 2012.
[50] Yabei Li, Junge Zhang, Yanhua Cheng, Kaiqi Huang, and                   [70] Niki Parmar, Ashish Vaswani, Jakob Uszkoreit, Lukasz
                                                                                  Kaiser, Noam Shazeer, Alexander Ku, and Dustin Tran. Im-
     Tieniu Tan. Df{}^{\mbox {2}} net: Discriminative feature learning and
                                                                                  age transformer. In ICML, 2018.
     fusion network for RGB-D indoor scene classification. In
                                                                             [71] Mandela Patrick, Yuki M Asano, Ruth Fong, João F Hen-
     AAAI, 2018.
                                                                                  riques, Geoffrey Zweig, and Andrea Vedaldi. Multi-
[51] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng
                                                                                  modal self-supervision from generalized data transforma-
     tions. arXiv preprint arXiv:2003.04298, 2020.                        contrastive learning. arXiv preprint arXiv:2106.11250,
[72] Mandela Patrick, Dylan Campbell, Yuki M Asano, Is-                   2021.
     han Misra Florian Metze, Christoph Feichtenhofer, Andrea        [88] Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco
     Vedaldi, and João Henriques. Keeping your eye on the ball:          Massa, Alexandre Sablayrolles, and Hervé Jégou. Train-
     Trajectory attention in video transformers. In NeurIPS,              ing data-efficient image transformers & distillation through
     2021.                                                                attention. In ICML, 2021.
[73] Boris T Polyak and Anatoli B Juditsky. Acceleration of          [89] Hugo Touvron, Andrea Vedaldi, Matthijs Douze, and Hervé
     stochastic approximation by averaging. SIAM journal on               Jégou. Fixing the train-test resolution discrepancy. In
     control and optimization, 1992.                                      NeurIPS, 2019.
[74] René Ranftl, Katrin Lasinger, David Hafner, Konrad             [90] Du Tran, Lubomir Bourdev, Rob Fergus, Lorenzo Torre-
     Schindler, and Vladlen Koltun. Towards robust monocu-                sani, and Manohar Paluri. Learning spatiotemporal features
     lar depth estimation: Mixing datasets for zero-shot cross-           with 3d convolutional networks. In CVPR, 2015.
     dataset transfer. TPAMI, 2020.                                  [91] Du Tran, Heng Wang, Lorenzo Torresani, Jamie Ray, Yann
[75] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause,                 LeCun, and Manohar Paluri. A closer look at spatiotempo-
     Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej                     ral convolutions for action recognition. In CVPR, 2018.
     Karpathy, Aditya Khosla, Michael Bernstein, Alexander C.        [92] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
     Berg, and Li Fei-Fei. ImageNet Large Scale Visual Recog-             Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser,
     nition Challenge. IJCV, 2015.                                        and Illia Polosukhin. Attention is all you need. In NeurIPS,
[76] Fadime Sener, Dibyadip Chatterjee, and Angela Yao. Tech-             2017.
     nical report: Temporal aggregate representations. arXiv         [93] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao
     preprint arXiv:2106.03152, 2021.                                     Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao.
[77] Karen Simonyan and Andrew Zisserman. Two-stream con-                 Pyramid vision transformer: A versatile backbone for dense
     volutional networks for action recognition in videos. In             prediction without convolutions. In ICCV, 2021.
     NeurIPS, 2014.                                                  [94] Xiaolong Wang, Ross Girshick, Abhinav Gupta, and Kaim-
[78] Mannat Singh, Laura Gustafson, Aaron Adcock, Vinicius                ing He. Non-local neural networks. In CVPR, 2018.
     de Freitas Reis, Bugra Gedik, Raj Prateek Kosaraju, Dhruv       [95] Tete Xiao, Yingcheng Liu, Bolei Zhou, Yuning Jiang, and
     Mahajan, Ross Girshick, Piotr Dollár, and Laurens van der           Jian Sun. Unified perceptual parsing for scene understand-
     Maaten. Revisiting weakly supervised pre-training of visual          ing. In ECCV, 2018.
     perception models. In CVPR, 2022.                               [96] Cihang Xie, Mingxing Tan, Boqing Gong, Jiang Wang,
[79] Shuran Song, Samuel P Lichtenberg, and Jianxiong Xiao.               Alan L Yuille, and Quoc V Le. Adversarial examples im-
     Sun rgb-d: A rgb-d scene understanding benchmark suite.              prove image recognition. In CVPR, 2020.
     In CVPR, 2015.                                                  [97] Yuchun Yue, Wujie Zhou, Jingsheng Lei, and Lu Yu. Two-
[80] Xinhang Song, Shuqiang Jiang, Bohan Wang, Chengpeng                  stage cascaded decoder for semantic segmentation of rgb-d
     Chen, and Gongwei Chen. Image representations with spa-              images. IEEE Signal Processing Letters, 2021.
     tial object-to-object relations for rgb-d scene recognition.    [98] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk
     TIP, 2020.                                                           Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regu-
[81] Khurram Soomro, Amir Roshan Zamir, and Mubarak Shah.                 larization strategy to train strong classifiers with localizable
     UCF101: A dataset of 101 human action classes from                   features. In ICCV, 2019.
     videos in the wild. CRCV-TR-12-01, 2012.                        [99] Amir Roshan Zamir, Alexander Sax, William B. Shen,
[82] Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya            Leonidas J. Guibas, Jitendra Malik, and Silvio Savarese.
     Sutskever, and Ruslan Salakhutdinov. Dropout: a simple               Taskonomy: Disentangling task transfer learning. In CVPR,
     way to prevent neural networks from overfitting. JMLR,               2018.
     2014.                                                          [100] Bowen Zhang, Jiahui Yu, Christopher Fifty, Wei Han, An-
[83] Weijie Su, Xizhou Zhu, Yue Cao, Bin Li, Lewei Lu,                    drew M. Dai, Ruoming Pang, and Fei Sha. Co-training
     Furu Wei, and Jifeng Dai. Vl-bert: Pre-training of                   transformer with videos and images improves action recog-
     generic visual-linguistic representations. arXiv preprint            nition. arXiv preprint arXiv:2112.07175, 2021.
     arXiv:1908.08530, 2019.                                        [101] Hongyi Zhang, Moustapha Cisse, Yann N Dauphin, and
[84] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet,           David Lopez-Paz. mixup: Beyond empirical risk minimiza-
     Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent                tion. In ICLR, 2018.
     Vanhoucke, and Andrew Rabinovich. Going deeper with            [102] Zhanpeng Zhang, Ping Luo, Chen Change Loy, and Xiaou
     convolutions. In CVPR, 2015.                                         Tang. Facial landmark detection by deep multi-task learn-
[85] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon              ing. In ECCV, 2014.
     Shlens, and Zbigniew Wojna. Rethinking the inception ar-       [103] Hengshuang Zhao, Li Jiang, Jiaya Jia, Philip Torr, and
     chitecture for computer vision. In CVPR, 2016.                       Vladlen Koltun. Point transformer. In ICCV, 2021.
[86] Hao Tan and Mohit Bansal. Lxmert: Learning cross-              [104] Zhun Zhong, Liang Zheng, Guoliang Kang, Shaozi Li, and
     modality encoder representations from transformers. arXiv            Yi Yang. Random erasing data augmentation. In AAAI,
     preprint arXiv:1908.07490, 2019.                                     2020.
[87] Hao Tan, Jie Lei, Thomas Wolf, and Mohit Bansal. VIM-          [105] Bolei Zhou, Agata Lapedriza, Aditya Khosla, Aude Oliva,
     PAC: Video pre-training via masked token prediction and              and Antonio Torralba. Places: A 10 million image database
                                                                          for scene recognition. TPAMI, 2017.
A. Implementation details for Pretraining                                             6

                                                                 F1 on Kinetics-400
                                                                                      5
   We train using AdamW with a batch size of 4096 for
each dataset, and use a cosine learning rate (LR) schedule                            4
with linear warm up and cool down phases for the first and                            3
last 10% of training, respectively. We train for 500 epochs                           2
with a peak LR of 2 · 10−3 and a weight decay of 5 · 10−2 .                           1
Swin-T, Swin-S and Swin-L use a window size of 8×7×7,

                                                                                                mobility - land
                                                                                                    swimming

                                                                                                    electronics

                                                                                              mobility - water

                                                                                           athletics - jumping
                                                                                               communication
                                                                                           interact w. animals
                                                                                            auto maintenance
                                                                                                       athletics

                                                                                                       juggling
                                                                                                  water sports
                                                                                               garden + plants

                                                                                                          cloths
                                                                                                miscellaneous
                                                                                                    snow + ice
                                                                                                          music
                                                                                                       cooking
                                                                                                   gymnastics
                                                                                                    using tools
                                                                                                          paper

                                                                                                arts and crafts
                                                                                          racquet + bat sports
                                                                                                       cleaning
                                                                                                   martial arts
                                                                                                     ball sports
                                                                                                        dancing
                                                                                                         heights
                                                                                                        makeup
                                                                                                playing games
                                                                                                 body motions

                                                                                             eating + drinking
                                                                                             personal hygiene
                                                                                                          hands
                                                                                              touching person
                                                                                                            hair
                                                                                                        waxing
                                                                                                            golf
                                                                                                 head + mouth
whereas Swin-B uses a window size of 16×7×7. The models
are trained with stochastic depth with a drop rate of 0.1 for
Swin-T, 0.2 for Swin-S, and 0.3 for Swin-B, and Swin-L.
We use exponential moving average (EMA) [73] with a de-
cay of 10−4 and report the best results during training since
EMA results peak before the end of training.                     Figure 6. Gain of O MNIVORE over baseline on Action recog-
   For IN1K and IN21K we use RandAugment [19],                   nition (per group). We plot the gain in per-class F1-score on the
                                                                 K400 dataset for all the action groups defined in [13]. The base-
mixup [101], CutMix [98], label smoothing [85], and Ran-
                                                                 line model is first pretrained on ImageNet-1K and then fine-tuned
dom Erasing [104] with the same settings as used in [88],
                                                                 on K400 whereas O MNIVORE is trained jointly on ImageNet-1K,
and color jittering of 0.4. For SUN RGB-D we clamp               K400 and the single-view 3D SUN RGB-D dataset. O MNIVORE
and normalize the disparity channel, drop the RGB chan-          improves the performance for all the 38 groups.
nels with a probability of 0.5, and we also apply 0.5
Dropout [82] before the linear head when pre-training with
ImageNet-21K. For Kinetics-400 we use mixup, CutMix              Throughout we use a weight decay of 0.05. We use a batch
and label smoothing, and Dropout of 0.5 before the linear        size of 4× 64 distributed over 64 32GB GPUs. For EPIC-
head.                                                            Kitchens-100, we use similar hyperparamters with only dif-
                                                                 ference being that we use a peak learning rate of 2 · 10−3
B. Details on the Transfer Tasks                                 and we train for 150 epochs. These settings provided better
B.1. Image Classification                                        performance for the modality-specific baseline, and we use
                                                                 it for finetuning both the baseline and O MNIVORE models.
   We finetune all models on the downstream tasks for 100            In terms of preprocessing, at train time we sample a 32
epochs and optimize the models with mini-batch SGD. We           frame video clip at stride 2 from the full video using tem-
use a half-wave cosine learning rate [54] and set the weight     poral segment sampling as in [52]. We scale the short side
decay to zero. For all models, including the modality-           of the video to 256px, take a 224px random resized crop,
specific models, we perform a grid search for the best learn-    followed by RandAugment and Random Erasing. At test
ing rate in the range [5e-3, 1e-2, 2e-2, 4e-2, 8e-2, 1e-1, 2e-   time, we again sample a 32 frame clip with stride 2, scale
1, 3e-1, 4e-1, 5e-1, 6e-1] and drop path in [0.1, 0.3]. We       the short side to 224px and take 3 spatial crops along the
use the strong augmentations from [88] for finetuning. For       longer axis to get 224 × 224 crops. The final predictions are
the evaluations in Tables 3 and 5, we follow [78] and resize     averaged over these crops.
the images to shortest side of 224px and evaluate the mod-
                                                                     For comparison to the state-of-the-art in Table 6, when
els on the center crop of 224 × 224. For higher resolution
                                                                 finetuning O MNIVORE models trained with IN21K, we
(384px) evaluations in Table 5, we similarly resize the im-
                                                                 found slightly different hyperparameters to perform better.
ages to shortest side of 384px and evaluate the models on
                                                                 For Something Something-v2, we used peak learning rate
the center crop of 384 × 384. We also increase the spatial
                                                                 of 1.2 · 10−3 over 150 epochs. For EPIC-Kitchens-100, we
window size for all the Swin models from 7 to 12.
                                                                 used weight decay of 0.004, over 100 epochs, peak learning
B.2. Video Classification                                        rate of 4 · 10−4 , with the same learning rate schedule for
                                                                 backbone and head. We also used cutmix augmentation and
   In Table 3, we finetune video models using hyperparam-
                                                                 label smoothing. All other hyperparameters in both cases
eters as described in [52]. For Something Something-v2, we
                                                                 were as described earlier. We also use EMA with similar
finetune for 60 epochs with AdamW optimizer. We use half-
                                                                 settings as used during pretraining.
wave cosine learning rate with warmup. We start the learn-
ing rate from 10−6 and linearly warmup to a peak learning        B.3. Single-view 3D Tasks
rate of 6 ·10−3 over 5% of the training, and rest 95% we use
half-wave cosine schedule to decay the learning rate back        NYU Scene classification. We follow the setup from [33]
to 10−6 . We train the classification head with this learning    for scene classification and use 10 classes derived from the
rate, and the backbone with 0.1× the above learning rate.        original 19 classes. In Table 7 (classification) the best Swin
                     15
F1 on Kinetics-400

                     10
                      5
                      0
                      5
                                               playing clarinet

                                            playing basketball

                                          dribbling basketball

                                              getting a haircut
                                                         busking
                                             making sandwich

                                           dancing charleston
                                                         tickling
                                                sweeping floor
                                                            yoga

                                               massaging legs
                                              filling eyebrows
                                           eating watermelon
                                                  eating carrots

                                           playing harmonica
                                                          texting
                                                  making pizza
                                          juggling soccer ball

                                                      auctioning
                                                 doing laundry
                                           playing saxophone

                                                  eating hotdog

                                                  folding paper
                                                 riding scooter
                                                  building shed

                                                    training dog
                                            playing accordion
                                           playing xylophone
                          skiing (not slalom or crosscountry)
                                                  bending back
                                                   catching fish
                                                     tap dancing

                                                       whistling
                                              playing cymbals
                                                    egg hunting
                                           reading newspaper
                                                   washing hair

                                                    waxing legs
                                                  breakdancing

                                                 snowboarding
Figure 7. Gain of O MNIVORE over baseline on Action Recognition (per class). We plot the gain in per-class F1-score on the K400
dataset for the top twenty and bottom twenty classes. The baseline model is first pretrained on ImageNet-1K and then fine-tuned on K400
whereas O MNIVORE is trained jointly on ImageNet-1K, K400 and the single-view 3D SUN RGB-D dataset. O MNIVORE improves the F1
score on 308 out of the 400 total classes.

B and Swin L models were trained for 200 epochs with                                       VideoSwin-B O MNIVORE (Swin-B)
starting learning rate of 5 × 10−3 , weight decay of 0 for              3-split accuracy       96.9           98.2
Swin B and 1 × 10−4 for Swin L. All other hyperparame-
ters were as described earlier.                                       Table 9. UCF-101. As in Table 3, the VideoSwin model is in-
                                                                      flated from IN1K and pre-trained on K400. O MNIVORE is pre-
NYU RGBD Segmentation. We follow the training and
                                                                      trained with IN1K, K400 and SUN RGB-D. Both models are then
evaluation setup from [10]. We follow the Swin segmen-                finetuned and evaluated on UCF-101 for each split separately. Per-
tation architecture which uses an UperNet [95] head with              formance reported is averaged over the standard 3 splits.
the Swin trunk. All models are finetuned with AdamW [53]
with a weight decay of 0.01. The learning rate follows a
Polynomial Decay (power 1) schedule and starts at 0.00006.            each match we create a one-hot vector using its ground truth
We warmup the learning rate for 1500 iterations and train             label, and scale it by es/τ , where s is the dot product be-
the model with a batchsize of 32. All the depth maps in               tween the feature of the matched image the query image,
NYU are converted into disparity maps by using the camera             and τ is a temperature hyperparameter (set to 0.07). We
baseline and focal length of the Kinect sensor.                       compute an effective prediction for the query by summing
B.4. k-NN experiments                                                 the top-k one-hot vectors. Similar processing is used for the
                                                                      visualizations in Figure 1 and Figure 4.
Extracting depth on ImageNet-1K. We ran a monocular
depth-prediction model [74] on the IN1K train set. We used
                                                                      C. Other Results
the pretrained dpt large model and followed the input im-
age preprocessing steps as provided in [74].                          Results on UCF-101. We also evaluate O MNIVORE on an-
                                                                      other popular (albeit smaller) video recognition benchmark,
Classifying ImageNet-1K using different modalities.                   UCF-101 [81]. As shown in Table 9, O MNIVORE pre-
For the experiments involving classification using different          training is effective for sports action recognition in UCF-
modalities, we extract features from the IN1K train set us-           101 as well. Note that the results shown are with RGB
ing the RGB, RGBD or just Depth (D) modalities, and on                modality only; the state-of-the-art on these datasets often
IN1K validation set using the RGB modality. We follow                 leverages additional features such as optical flow, dense tra-
the k-NN protocol from [12] for evaluation and briefly de-            jectories (IDT) etc.
scribe it next. We extract the stage 3 [51] features and L2           Low-data regime fine-tuning. We analyzed low-shot
normalize them. For each validation feature as the query,             versions of the Places-365 benchmark (models from Ta-
we retrieve the nearest neighbors from the train set using            ble 3). As shown in Table 10, O MNIVORE outperforms the
euclidean distance, and take the top-k closest matches. For           modality-specific baseline in the low-shot regime too.
          Method              Places-365
                         1% 2% 5% 10%
          O MNIVORE      46.2 49.0 51.5 53.9
          Image-specific 44.8 47.9 50.9 53.4

Table 10. Low-shot finetuning. Performance of finetuning O M -
NIVORE on low-shot versions of the Places-365 dataset.

Per-class gains. We present the gain of O MNIVORE over
the VideoSwin baseline (§ 4.1 of the main paper) in Figs. 6
and 7.
