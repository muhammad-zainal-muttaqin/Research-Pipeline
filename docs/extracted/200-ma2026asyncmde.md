---
source_id: 200
bibtex_key: ma2026asyncmde
title: AsyncMDE: Real-Time Monocular Depth Estimation via Asynchronous Spatial Memory
year: 2026
domain_theme: Estimasi Kedalaman
verified_pdf: 200_AsyncMDE Kedalaman Monokular Real-Time Memori Spasial.pdf
char_count: 69979
---

AsyncMDE: Real-Time Monocular Depth Estimation
                                                                   via Asynchronous Spatial Memory
                                                      Lianjie Ma1 , Yuquan Li1 , Bingzheng Jiang1 , Ziming Zhong3 , Han Ding2 , and Lijun Zhu1,†

                                            Abstract— Foundation-model-based monocular depth estima-
                                         tion offers a viable alternative to active sensors for robot
                                         perception, yet its computational cost often prohibits deployment
                                         on edge platforms. Existing methods perform independent
                                         per-frame inference, wasting the substantial computational
                                         redundancy between adjacent viewpoints in continuous robot
arXiv:2603.10438v2 [cs.RO] 28 Jun 2026

                                         operation. This paper presents AsyncMDE, an asynchronous
                                         depth perception system consisting of a frozen foundation model
                                         and a lightweight fast path that amortizes the foundation model’s
                                         computational cost over time. The foundation model periodically
                                         produces high-quality spatial features in the background,
                                         while the lightweight fast path runs asynchronously in the
                                         foreground, fusing cached memory with current observations
                                         through complementary fusion, outputting depth estimates, and
                                         autoregressively updating memory. This enables cross-frame
                                         feature reuse with bounded accuracy degradation. With 3.83M
                                         trainable fast-path parameters and a 97.5M frozen slow path,
                                         AsyncMDE’s fast path operates at 237 FPS on an RTX 4090,
                                         recovering 77% of the accuracy gap to the foundation model.                  Fig. 1.     Overview of AsyncMDE. Top: the Slow Path (DAv2-ViTB)
                                                                                                                      periodically refreshes spatial memory; the Fast Path fuses cached memory
                                         Across indoor static, dynamic, and synthetic extreme-motion                  with each frame at high frequency, with depth maps at increasing lag
                                         benchmarks, AsyncMDE degrades predictably and reaches                        showing bounded degradation. Bottom: efficiency–accuracy trade-off (three-
                                         161 FPS fast-path inference on a TensorRT-optimized Jetson                   benchmark average δ1 ); AsyncMDE (3.83 M trainable fast path, 237 FPS
                                         AGX Orin, supporting real-time edge deployment.                              fast-path throughput) recovers 77% of the δ1 gap between the lightweight
                                                                                                                      baseline and the foundation model.
                                                              I. INTRODUCTION
                                            Depth perception is a fundamental capability for embod-                   to meet the real-time perception demands of robots operating
                                         ied intelligent systems, playing a key role in autonomous                    in highly dynamic environments.
                                         navigation [1]–[4], perceptual control [5]–[7], and vision-                     Beyond single-frame depth estimation, the MDE field
                                         language-action decision making [8]. Mainstream approaches                   continues to advance along two directions. Video depth
                                         use LiDAR or RGB-D cameras, but these active sensors                         methods [14]–[18] improve temporal consistency through
                                         are costly and constrained by lighting conditions, sensing                   cross-frame modeling, while Depth Anything V3 [19] and
                                         range, and environmental structure, making it difficult to                   VGGT [20] unify monocular and multi-view geometric con-
                                         maintain stable performance across diverse deployment                        straints toward general-purpose visual geometry foundation
                                         scenarios. Monocular depth estimation (MDE) requires only                    models. However, embodied intelligence requires not just peak
                                         a single RGB camera to produce dense, structured depth                       single-frame accuracy, but reliable depth estimation under
                                         maps, offering low cost, minimal calibration, and broad                      strict latency and resource constraints—all these methods
                                         adaptability across environments, which makes it an attractive               depend on heavy backbone networks, and real-time edge
                                         alternative for robot perception [9]. Recently, depth foundation             deployment remains out of reach. Knowledge distillation and
                                         models [10]–[13] have demonstrated strong zero-shot general-                 lightweight architecture design [21], [22] attempt to bridge the
                                         ization through large-scale pretraining and Vision Transformer               efficiency gap by compressing model size, but cross-domain
                                         (ViT) architectures. However, their large parameter counts                   generalization and accuracy both drop significantly once the
                                         lead to excessive inference latency on edge platforms, failing               parameter count is reduced to a few million.
                                                                                                                         The accuracy–efficiency tension extends to the decision-
                                            This work was supported by the Fundamental and Interdisciplinary
                                         Disciplines Breakthrough Plan of the Ministry of Education of China under
                                                                                                                      making layer. VLA models such as OpenVLA [8] incur
                                         Grant JYB2025XDXM208, and the National Natural Science Foundation of         hundreds of milliseconds per inference, far too slow for
                                         China under Grant U25A6013.                                                  50–100 Hz robotic control loops. Inspired by dual-process
                                            † Corresponding author.
                                            1 School of Artificial Intelligence and Automation, Huazhong University   theory [23], fast–slow architectures [5]–[7], [24] decouple a
                                         of Science and Technology, Wuhan, China. {yingyi1048596, yuquanli,           slow, large-model system for semantic reasoning from a fast
                                         bzjiang, ljzhu}@hust.edu.cn                                                  system for high-frequency action execution. This paradigm
                                            2 School of Mechanical Science and Engineering, Huazhong University
                                                                                                                      suggests that a similar fast–slow separation can be applied
                                         of Science and Technology, Wuhan, China. dinghan@hust.edu.cn
                                            3 Yichang Testing Technology Research Institute, Yichang, China.          at the perception level, rather than solely compressing the
                                         zhongziminghaha@outlook.com                                                  model itself.
                                                                                              TABLE I
   In continuous robot operation, adjacent viewpoints share
                                                                                           N OMENCLATURE
substantial 3D structure, enabling a decomposition into two
subproblems of vastly different complexity: scene representa-            Symbol           Description
tion—recovering 3D-aware features from a single 2D image—             xt∈ R3×H×W          Input RGB frame at time t
demands large capacity and strong priors; temporal adapta-            ŷt ∈ R1×H×W        Predicted depth map at time t
tion—incrementally updating cached features for the current               N ∈ Z+          Refresh interval in frames (for training/evaluation)
viewpoint—is far simpler, as physical continuity bounds inter-               fθ           Lightweight inference network with parameters θ
                                                                              (ℓ)
frame changes. This gap motivates pairing a heavyweight                     FB,t          Foundation model layer-ℓ feature at time t
                                                                            (ℓ)
model that runs infrequently with a lightweight model at high               FS            Encoder layer-ℓ output feature
frame rates. We thus propose AsyncMDE, an asynchronous                      Φ(ℓ)          Layer-ℓ feature projector (Conv1×1 +Interp)
                                                                         (ℓ)
depth perception system that amortizes the foundation model’s         Tt ∈ (0, 1)         Layer-ℓ raw spatial modulation factor
                                                                        ′(ℓ)
cost over time. The foundation model [10] solves scene                Tt     ∈ (0, 1)     Smoothed modulation factor used for fusion
                                                                    (ℓ)
                                                                   Mt ∈ R128×Hℓ ×Wℓ       Layer-ℓ spatial memory (ℓ = 1, . . . , 4)
representation in the background, writing high-quality features
into spatial memory; the lightweight network solves temporal
adaptation in the foreground, detecting changes and selectively       Video depth methods [14]–[18] improve temporal con-
updating memory through complementary fusion. The two              sistency through cross-frame modeling. DepthCrafter [15]
paths run concurrently on separate CUDA streams; since the         generates long-sequence consistent depth via video diffusion,
lightweight network only injects changes rather than infers        and Video Depth Anything [16] introduces temporal attention
from scratch, it far outperforms distilled models of comparable    heads on top of a single-frame foundation model for inter-
size. The main contributions are:                                  frame alignment. These methods improve cross-frame depth
                                                                   quality but still rely on heavy backbones or diffusion sampling
   • We propose the asynchronous depth perception paradigm,
                                                                   processes, making real-time deployment costly. For persistent
     which exploits the complexity gap between scene rep-
                                                                   3D perception, Spann3R [27] and CUT3R [28] use external
      resentation and temporal adaptation to amortize the
                                                                   spatial memory for streaming 3D reconstruction. Their
      foundation model’s cost over time. The resulting rate-
                                                                   “persistent-state-driven inference” paradigm is conceptually
      controlled perception system’s accuracy is governed by
                                                                   close to ours, but they target general geometry estimation and
      the hardware-determined refresh rate and scales smoothly
                                                                   depend on heavy ViT architectures, making them unsuitable
     with platform capability without retraining.
                                                                   for lightweight real-time depth inference.
   • We design SpatialMemoryUnit, which uses comple-
      mentary fusion and autoregressive memory updates to          B. Efficient Depth Perception and Dual-System Architectures
      leverage foundation model features, maintaining bounded         For depth model compression, knowledge distillation [21],
      accuracy degradation within refresh intervals.               [22] transfers depth knowledge from large models to
   • The deployed system retains a 97.5M frozen slow path          lightweight networks via the teacher–student paradigm. How-
      for periodic refresh, while its 3.83M trainable fast path    ever, conventional distillation applies supervision only at the
      runs at 237 FPS on an RTX 4090 and 161 FPS on                final output level, and the compressed model struggles to in-
      a TensorRT-optimized Jetson AGX Orin. We validate            herit the foundation model’s rich intermediate representations.
     AsyncMDE on indoor static, dynamic, and synthetic             In practice, accuracy degradation remains significant when
      extreme-motion benchmarks.                                   the parameter count is reduced to a few million, indicating
                                                                   that reducing capacity alone cannot preserve both perception
                   II. RELATED WORK                                quality and real-time performance.
A. Advances in Monocular Depth Estimation                             For dual-system architectures, Kahneman’s dual-process
                                                                   theory [23] provides a cognitive science foundation for
   Single-frame depth estimation foundation models, including      fast–slow system separation. Dual MLLM [5], GR00T [6],
Depth Anything V2 [10], Metric3D [11], UniDepthV2 [12],            OpenHelix [7], and FiS-VLA [24] have validated the effec-
and Depth Pro [13], have achieved breakthroughs in cross-          tiveness of this paradigm for robotic decision-making and
domain zero-shot generalization through large-scale pretrain-      manipulation. A related systems pattern also appears in visual
ing and ViT architectures [9]. More recently, Depth Any-           SLAM, where a fast front end tracks incoming frames while
thing V3 [19] and VGGT [20] further unify monocular and            slower back-end optimization refines the global state. This
multi-view geometric constraints within a single framework,        work extends the idea to dense depth perception, using the
moving toward general-purpose visual geometry foundation           foundation model as a low-frequency quality source, the
models. While these efforts continue to raise the accuracy         lightweight network as a high-frequency executor, and spatial
ceiling, they all rely on heavy backbones and high-resolution      memory as the bridge enabling feature reuse between them.
inference, limiting real-time edge deployment.
   A related direction is prior-assisted depth estimation, which                      III. METHODOLOGY
fuses RGB with sparse depth or camera parameters [25],                This section describes AsyncMDE. Section III-A outlines
[26]. Although such methods improve metric accuracy, their         the two-phase procedure; III-B describes network components;
additional priors introduce non-negligible overhead and do         III-C details spatial memory fusion; and III-D presents the
not address inference efficiency on edge platforms.                loss. Table I summarizes the nomenclature.
Fig. 2. AsyncMDE system overview. DAv2-ViTB runs asynchronously in the background (slow path, ∼60 Hz), writing results to spatial memory when
available; the lightweight network continuously predicts depth for the current viewpoint (fast path, ∼240 Hz), combining cached memory with current
observations through complementary fusion and autoregressively updating memory. During training, DAv2 also provides pseudo-label depth for supervision.

A. Asynchronous Perception Framework                                         Head; the encoder extracts lightweight multi-scale observa-
   As shown in Fig. 2, the system maintains a set of                         tions; the projector aligns dimensions and SpatialMemoryUnit
                                  (ℓ)
multi-scale spatial memories {Mt }4ℓ=1 , where ℓ denotes                     fuses memory with current features. Structural minimalism—
the feature level, to cache high-quality features from the                   no optical flow, depth warping, or attention modules are
foundation model and update them autoregressively across                     introduced; all cross-frame information transfer uses per-
frames. The system operates in two phases.                                   pixel gated fusion, with only 3.83M trainable parameters
                                                                             (decoder 2.52M, encoder 0.93M, SMU 0.38M). External state
   Initialization and refresh phase: The frozen foundation
                                                                             memory—the update can be interpreted as a gated, spatially
model (DAv2-ViTB [10]) initializes memory at t = 0 and
                                                                             varying EMA over explicit memory, but unlike learned
overwrites it whenever a slow-path refresh completes. Let R
                                                                             recurrent cells, the memory is an externally refreshable spatial
denote refresh frames; the memory available to the fast path
                                                                             cache: M0 is injected by the foundation model, each refresh
is
                                                                             overwrites memory, and any frame can perform independent
                     (
                         (ℓ)
                 (ℓ)   FB,t , t = 0 or t ∈ R,
              Mt =       (ℓ)                             (1)                 inference given memory.
                       Ot−1 , t ∈/ R.                                           1) Encoder: The encoder employs MobileNetV3-
   Continuous inference phase (t > 0): The lightweight net-                  Small [29] (0.93M parameters), producing multi-scale
                                                                                          (ℓ)
work runs frame by frame, performing continuous inference                    features {FS }4ℓ=1 at 4×–32× downsampling. Its role is to
through spatial memory fusion:                                               provide current-frame observations to SpatialMemoryUnit,
                                                                             not to perform depth estimation independently. Ablation
                      (ŷt , Ot ) = fθ (xt , Mt )                    (2)     experiments (Section IV-D) compare multiple encoder
                                                                             architectures, showing that spatial memory compensates for
where fθ consists of an encoder, SpatialMemoryUnit, and
                                                                             limited encoder capacity.
decoder; Ot becomes the next memory unless a new slow-
                                                                                2) Feature Projector: The projector applies a 1 × 1 convo-
path refresh overwrites it. During training, sequence slices
                                                                             lution for channel alignment followed by bilinear interpolation
with a fixed refresh interval N are used; the foundation
                                                                             for spatial alignment to each feature level, making encoder
model generates pseudo-label depth and refreshes memory,
                                                                             outputs dimensionally consistent with the memory features:
and its parameters are not updated. The foundation model
sets the representation quality ceiling, while the lightweight                                  (ℓ)                      (ℓ)
                                                                                        Φ(ℓ) (FS ) = Interp Conv1×1 (FS ), sℓ
                                                                                                                                 
                                                                                                                                          (3)
network learns to preserve and adapt it. Implementation and
deployment details are provided in Section IV-B.                             where sℓ is the spatial size of the layer-ℓ memory. After
                                                                             projection, all levels are unified to 128 channels.
B. Network Architecture                                                        3) Decoder: The decoder directly inherits the RefineNet
   The overall architecture follows three design principles.                 architecture and pretrained weights from the DPT Head. It
Maximize reuse—the decoder inherits the RefineNet architec-                  progressively fuses the four feature levels from deepest to
ture and pretrained weights from the foundation model’s DPT                  shallowest, performs cross-scale aggregation through residual
convolutional units, and outputs a depth map at the same          TL1 , while semantically changing regions switch to TeL4 to
resolution as the input: ŷt ∈ R1×H×W , omitting the batch        drive global refresh. The modulation factor for each level is
dimension as in Table I.                                          obtained by interpolating Tfinal :
                                                                                     (ℓ)
C. Spatial Memory Fusion                                                         Tt        = Interp(Tfinal , sℓ ),     ℓ = 1, . . . , 4          (8)
   SpatialMemoryUnit is the core component of the system.                                                       (1)
                                                                  where sℓ is the spatial size of layer ℓ, and Tt = Tfinal .
Viewing the memory update as a discrete-time dynamical               Additionally, the system applies temporal smoothing
system, the fusion form must satisfy boundedness and               ′(ℓ)       (ℓ)              ′(ℓ)
                                                                  Tt    = βTt + (1 − β)Tt−1 with β = 0.5, suppressing
controllable decay. The per-pixel convex combination O =          frame-to-frame jitter in the T values.
T · M + (1 − T ) · F (T ∈ (0, 1)) keeps fused features between       2) Complementary Fusion and Memory Update: Given the
memory and current observations, preventing long-sequence                                              ′(ℓ)
                                                                  smoothed spatial modulation factor Tt , SpatialMemoryUnit
divergence. When combined with the autoregressive update          mixes memory and current observations per pixel through
Mt+1 = Q    Ot , the contribution weight of M0 to frame t         complementary fusion:
              t
becomes s=1 Ts , which decays at a rate determined by                      (ℓ)             ′(ℓ)      (ℓ)             ′(ℓ)                 (ℓ)
scene dynamics. This gives a predictable refresh-interval                 Ot     = Tt             ⊙ Mt     + (1 − Tt        ) ⊙ Φ(ℓ) (FS,t )     (9)
trade-off, verified in Section IV-C.                              The fused result is written back as an autoregressive memory
   Justification for feature-space fusion. Fusion operates in     update, sustaining foundation-model feature quality within
the 8×–32× downsampled feature space, where each vector’s         the refresh interval:
receptive field spans hundreds of pixels and encodes semantic
                                                                                                         (ℓ)     (ℓ)
and structural information robust to pixel-level displacements.                                      Mt+1 = Ot                                  (10)
When motion exceeds the receptive field tolerance, T → 0                       (ℓ)
                                                                  where Mt ∈ RB×128×Hℓ ×Wℓ is the layer-ℓ spatial memory
injects new observations without requiring pose estimation
                                                                  at time t, and Φ(ℓ) is the feature projector.
or feature warping, trading a predictable degradation rate for
robustness against the known failure modes of optical flow,       D. Loss Function
such as occlusion boundaries and dynamic object interference.        The training objective consists of three loss terms that con-
   Based on the above, the fusion procedure has two steps.        strain depth accuracy, edge structure, and memory utilization,
A semantic gated modulation factor assesses regional change       respectively.
(Section III-C-1), and complementary fusion selectively              Scale-Shift Invariant Loss eliminates global scale and shift
updates memory (Section III-C-2).                                 differences between the predicted depth P and the pseudo-
   1) Semantic Gated Modulation Factor: The spatial modula-       label G:
              (ℓ)
tion factor Tt ∈ (0, 1) governs the per-pixel trust balance be-                             
                                                                                              P − µP G − µG
                                                                                                                   
tween memory and the current observation. When T → 1 the                        LSSI = MSE              ,                     (11)
                                                                                                 σP         σG
system retains memory (static region); when T → 0 it injects
the current frame (changed region). Shallow features (Layer 1)    where µ and σ denote the spatial mean and standard deviation,
capture fine-grained texture changes but miss semantic shifts,    respectively.
whereas deep features (Layer 4) capture semantic changes but         Multi-Scale Gradient Loss enforces edge sharpness on
lack spatial precision. The SemanticGatedModulator fuses          the normalized depth maps:
both scales through a learnable gating mechanism.                              4
                                                                               X 1                                              
   Given the projected features at Layer 1 and 4 from the          Lgrad =                   |∇x Ps − ∇x Gs | + |∇y Ps − ∇y Gs | (12)
previous and current frames, the T values at both scales are:                  s=1
                                                                                       s2
                                                                  where s indicates the downsampling scale; gradients are
                  TL1 = σ h(1) ([pL1 ; cL1 ])
                                             
                                                            (4)
                                                                  computed at multiple scales to capture both fine and coarse
                  TL4 = σ h(4) ([pL4 ; cL4 ])                     edge structure.
                                             
                                                            (5)
                                                                     Memory Regularization Loss prevents the network from
where pLi and cLi are the projected features of the previous      ignoring the memory and relying solely on the current frame
and current frames at Layer i (i ∈ {1, 4}), [·; ·] denotes        during early training by introducing a soft lower bound on
channel-wise concatenation, and h(1) and h(4) denote inde-        the T values:
pendently parameterized lightweight convolutional networks.                          Lmem = ReLU(τ − T̄ )                 (13)
The T values from the two scales are non-linearly combined
via semantic gating:                                              where T̄ is the spatial mean of the Layer 1 T values and
                                                                 τ = 0.4 is the lower-bound threshold. This constraint activates
                  g = σ k · (TeL4 − 0.5)                  (6)     only when T̄ falls below the threshold, without interfering
                                                                  with the network’s freedom to assign low T values to local
              Tfinal = g ⊙ TL1 + (1 − g) ⊙ TeL4            (7)    dynamic regions.
where TeL4 = Interp(TL4 , s1 ) is TL4 upsampled to Layer 1          The total loss is:
resolution, and k = 4.0 is a temperature parameter. The gate                    L = 1.0 · LSSI + 0.5 · Lgrad + 0.1 · Lmem                       (14)
g causes semantically stable regions to adopt the fine-grained
                                                                         TABLE II
                                                              ACCURACY–E FFICIENCY C OMPARISON

                                                                       ScanNet                               Bonn                                Sintel
   Method                       Params           FPS       AbsRel↓       RMSE↓         δ1 ↑     AbsRel↓       RMSE↓         δ1 ↑     AbsRel↓       RMSE↓         δ1 ↑
   DAv2-ViTL [10]               335.3M           21.1        0.037        0.133       0.984       0.049        0.174       0.979       0.224        4.985       0.735
   DAv2-ViTB                     97.5M           60.1        0.040        0.137       0.983       0.050        0.177       0.979       0.222        4.867       0.733
   DAv2-ViTS                     24.8M           132.1       0.044        0.146       0.980       0.052        0.178       0.979       0.235        4.993       0.717
   VDA-Base [16]                114.4M            42.4       0.041        0.144       0.982       0.042        0.170       0.985       0.212        4.922       0.758
   VDA-Small                     29.0M            75.9       0.047        0.154       0.979       0.044        0.160       0.986       0.233        5.040       0.716
   CUT3R [28]                   748.4M            14.4       0.107        0.390       0.888       0.112        0.377       0.877       0.448        6.185       0.425
   LiteMono [22]                3.07M             238        0.168        0.431       0.727       0.158        0.455       0.759       0.416        5.956       0.443
   LiteMono†                    3.07M             238        0.120        0.306       0.851       0.123        0.365       0.854       0.383        5.664       0.502
   AsyncMDE (ours)         3.83M(+97.5M)          237        0.057        0.181       0.968       0.058        0.196       0.969       0.287        5.377       0.640
All baselines perform independent per-frame inference; AsyncMDE reports lag 0–9 cycle averages. For AsyncMDE, Params denote trainable fast path plus frozen slow path, and
FPS denotes fast-path throughput. † Fine-tuned on our training data using the same frozen-foundation pseudo-label supervision as AsyncMDE. LiteMono input 640×192,
CUT3R input 224×224; all others are resized so that the shorter side equals 518 px (divisible by 14).

                         IV. EXPERIMENTS                                               B. Main Results: Accuracy–Efficiency Comparison
A. Experimental Setup                                                                     Accuracy comparison with baselines. As shown in
                                                                                       Table II, AsyncMDE achieves δ1 =96.8% and 96.9% on
   1) Training Setup: Training mixes three datasets:
                                                                                       ScanNet and Bonn, respectively, using a 3.83M-parameter
NYUv2 [30] (indoor static, ∼155K frames), TartanAir [31]
                                                                                       trainable fast path together with a 97.5M frozen slow path,
(synthetic, ∼112K frames), and BridgeData V2 [32] (robotic
                                                                                       keeping the gap within 2 percentage points of DAv2-ViTB
interaction, ∼387K frames), totaling ∼654K frames. The
                                                                                       (98.3%/97.9%). This comparison highlights the value of
supervision signal is pseudo-labeled inverse depth generated
                                                                                       spatial memory from three perspectives. (1) vs. standalone
by the frozen foundation model. Training uses video clips
                                                                                       lightweight models. Compared with LiteMono† at a similar
of length 10 with stride 5; each image is resized so that its
                                                                                       trainable fast-path scale, AbsRel is 52% lower, demonstrat-
short edge measures 518 pixels, aligned to multiples of 14.
                                                                                       ing that feature amortization is far superior to standalone
We use AdamW (lr=10−4 , weight decay 0.01), batch size
                                                                                       lightweight models of comparable size. (2) vs. general-
4, 30 epochs, and cosine learning rate scheduling. AMP is
                                                                                       purpose memory architectures. CUT3R also uses external
enabled with gradient clipping at 1.0.
                                                                                       memory but targets general 3D reconstruction, achieving only
   2) Evaluation Setup: Evaluation is conducted on three
                                                                                       88.8% δ1 with 748M parameters, still inferior to AsyncMDE,
benchmarks covering different scene characteristics. Scan-
                                                                                       confirming that task-specific design is essential for efficient
Net [33] contains 100 indoor scenes (43,600 frames,
                                                                                       amortization. (3) vs. extreme scenarios. On Sintel, the cycle-
structured-light depth GT). Bonn [34] contains 14 dynamic
                                                                                       average AbsRel of 0.287 reflects the inherent limitation of
indoor scenes (2,850 frames). Sintel [35] contains 23 synthetic
                                                                                       the temporal continuity prior under severe scene dynamics;
sequences (1,064 frames) with large motion and extreme
                                                                                       however, the degradation is strictly lower-bounded by the
dynamics. The evaluation refresh interval is N =10. Depth
                                                                                       standalone encoder capacity (AbsRel=0.386), confirming that
accuracy metrics are AbsRel, RMSE, and δ1 (the fraction
                                                                                       the system retains a guaranteed performance floor.
of pixels satisfying max(d∗ /d, d/d∗ ) < 1.25); efficiency
                                                                                          Accuracy–latency coupling and deployment architec-
metrics report fast-path FPS and distinguish trainable fast-path
                                                                                       ture. Unlike conventional models with deterministic accuracy,
parameters from frozen slow-path parameters for AsyncMDE.
                                                                                       AsyncMDE’s accuracy is governed by the rate ratio of the
   Metric reporting convention. The accuracy of AsyncMDE
                                                                                       fast and slow paths. At deployment, the two paths occupy
varies with lag (the number of frames since the last refresh).
                                                                                       separate CUDA streams and exchange data through a lock-free
All values reported in tables are averages over one complete re-
                                                                                       shared feature cache. The slow path writes updated multi-
fresh cycle (lag ∈ [0, N −1]), referred to as the cycle average;
                                                                                       scale features into the cache whenever a new foundation-
per-lag degradation behavior is presented in Section IV-C.
                                                                                       model inference completes, and the fast path reads the latest
   3) Baselines: DAv2-ViTB (97.5M) serves as the primary                               cached features at each frame without blocking. The fast-path
baseline and is also the frozen foundation model used for the                          latency is tfast =4.2 ms; the slow-path latency tslow =16.6 ms is
slow path; DAv2-ViTS/ViTL serve as same-family references.                             entirely hidden by the pipeline, yielding an effective refresh
The baselines also include LiteMono [22] (3.07M, as a                                  interval Neff ≈ 237/60 ≈ 4 frames on an RTX 4090. As
lightweight representative), Video Depth Anything [16] (as                             platform compute capability varies, Neff adjusts accordingly
a video depth representative), and CUT3R [28] (streaming                               and accuracy traces the degradation curve smoothly (Fig. 3).
3D reconstruction with external spatial memory). Because                               Section IV-C quantifies this property.
LiteMono performed poorly with its original weights due
to limited training data, we fine-tuned it on our dataset                              C. System Behavior Analysis: Degradation and Deployment
using the same frozen-foundation pseudo-label supervision                                1) Accuracy Degradation Characteristics: Fig. 3 shows
as AsyncMDE, denoted LiteMono† .                                                       the relationship between lag and accuracy, with N set to
             AbsRel ↓                         δ1 ↑             DAv2-ViTB AbsRel                              DAv2-ViTB δ1                                             TABLE IV
                                                                                                                                                 E NCODER A BLATION ON S CAN N ET, N=10 C YCLE AVERAGE
                  0.983                        0.975                0.979                                                           0.76
                                                                                       0.980      0.733
     0.105                                       0.085                                   0.33
                                                                                                                                            Encoder    Type     Params   FPS↑   AbsRel↓     δ1 ↑   FastPath%
AbsRel ↓

                                               0.930                                   0.955                                        0.68

                                                                                                                                     δ1 ↑
     0.075                                       0.067                                   0.27                                               MNv3-S     CNN      3.83M    237     0.057     0.968     11.3
                                               0.885                                   0.930
                                                                                                                         0.222
                                                                                                                                    0.60    MNv3-L      CNN     5.93M    198     0.060     0.962     12.7
     0.045       0.040                           0.049              0.050                0.21                                               EViT-B0    Linear   3.53M    207     0.065     0.955     23.4
           0 –3 –5 10
            1 4 6–            –1
                                 5
                                       –2
                                          0            0 –3 –5 10
                                                        1 4 6–         –1
                                                                          5
                                                                                –2
                                                                                   0           0 –3 –5 10
                                                                                                1 4 6–          –1
                                                                                                                     5
                                                                                                                           –2
                                                                                                                                0           EViT-B1    Linear   7.52M    147     0.064     0.958     37.6
                         11          16                              11       16                              11         16
                Lag (frames)                                Lag (frames)                            Lag (frames)                            MViT-XS    Hybrid   4.82M    112     0.070     0.945     39.7
                                                                                                                                            MViT-S     Hybrid   7.87M    110     0.065     0.956     33.7
                (a) ScanNet                                   (b) Bonn                                    (c) Sintel

Fig. 3. Lag–accuracy degradation curves. The evaluation interval N =20
exceeds the training setting (N =10) to test out-of-distribution generalization.                                                            resource contention; TRT deployment or a dual-GPU setup
ScanNet and Bonn degrade predictably within the training interval (lag≤10)                                                                  can mitigate this bottleneck.
and more steeply beyond; Sintel AbsRel saturates beyond lag=10 at ∼0.34,
exhibiting bounded degradation.

                                                                                                                                            D. Ablation Studies
20 at evaluation to test generalization beyond the training
distribution. At lag=0, ScanNet AbsRel is 0.041, nearly                                                                                        1) Encoder Selection Ablation: Table IV fixes SpatialMem-
identical to DAv2-ViTB (0.040). As lag increases, degradation                                                                               oryUnit and the decoder, varying the encoder across pure CNN
exhibits two key properties. (1) Predictable and bounded.                                                                                   (MobileNetV3 [29]), hybrid architectures (MobileViT [36]),
ScanNet and Bonn degrade gradually within the training                                                                                      and linear attention (EfficientViT [37]).
interval (lag≤10), consistent with the theory in Section III-C;
                                                                                                                                               The results show a counterintuitive trend: larger encoder
Sintel saturates for lag>10 at ∼0.34, with the lower bound
                                                                                                                                            capacity leads to lower system accuracy. MNv3-S achieves
being the encoder’s standalone inference capability (FastPath
                                                                                                                                            the best overall performance; EViT-B1 worsens AbsRel
Only AbsRel=0.386). (2) Scene-dependent. Bonn has a small
                                                                                                                                            by +12% and reduces FPS by 38%. This is explained
fraction of dynamic objects, with AbsRel increasing only
                                                                                                                                            by FastPath% (the fraction of encoder-dominated regions):
38% relative to lag=0 at lag 6–10; ScanNet increases by 82%
                                                                                                                                            MNv3-S has only 11.3% encoder-dominated regions, with
due to global camera scanning; Sintel exhibits the steepest
                                                                                                                                            88.7% retaining high-quality memory; EViT-B1 (37.6%) and
rise (AbsRel reaches 0.337) yet saturates beyond lag>10,
                                                                                                                                            MViT-XS (39.7%) excessively overwrite memory with lower-
indicating bounded degradation even under extreme dynamics.
                                                                                                                                            quality observations. This indicates that the optimal role of
   2) Amortization Efficiency and Deployment Trade-offs:                                                                                    the encoder is as a change detector and observation injector—
When N increases to 20, the ScanNet cycle-average AbsRel                                                                                    injecting new observations only where memory has become
rises from 0.057 to 0.081 (+42%), and δ1 drops from 96.8%                                                                                   invalid, rather than performing independent depth inference.
to 92.6%; the degradation magnitude can be estimated from
                                                                                                                                               2) Core Architecture Ablation: Table V progressively
Fig. 3. On edge platforms, the slow-path rate decreases and
                                                                                                                                            introduces core components to quantify each design choice.
Neff increases, but the fast-path frame rate is unaffected. To
verify edge feasibility, we conduct inference benchmarks on                                                                                    Using FastPath Only (no memory) as an anchor, initializing
a Jetson AGX Orin (64 GB, 50 W mode).                                                                                                       memory with encoder features (Enc. Mem.) actually increases
   Table III presents the Orin edge deployment characteristics.                                                                             ScanNet AbsRel by +7%, as low-quality features introduce
Under PyTorch, the fast path runs at 27.8 FPS, a 6.8× speedup                                                                               drift through autoregressive accumulation. Switching to DAv2
over DAv2-ViTB (higher than the 3.9× on RTX 4090), as                                                                                       initialization reduces AbsRel by 57% and improves δ1 by
depthwise separable convolutions exhibit a more pronounced                                                                                  14.3 pp, establishing the value of high-quality memory. DAv2
efficiency advantage on edge devices; the SMU module                                                                                        L4 Only (semantic gating only) closely matches Full SMU
accounts for only 14% of latency (5.0 ms), confirming that                                                                                  (ScanNet AbsRel 0.057 vs. 0.057), while DAv2 w/o SGM
memory fusion overhead is minimal. TRT FP16 further boosts                                                                                  (texture gating only) degrades to 0.061 (+7%), indicating
the fast path to 161.1 FPS (13.1×), at which point Neff ≈                                                                                   semantic features are the primary gating contributor. Dual-
161/12 ≈ 13 frames, still within the bounded degradation                                                                                    scale fusion (Full SMU) still holds a slight δ1 edge, as texture
region of Fig. 3. Note that under single-GPU concurrency,                                                                                   information contributes to depth details.
the fast path drops to 13.5 FPS (2.16× slowdown) due to                                                                                                                TABLE V
                                  TABLE III                                                                                                       C ORE A RCHITECTURE A BLATION , N=10 C YCLE AVERAGE
             J ETSON AGX O RIN E DGE D EPLOYMENT, I NPUT 518×518
                                                                                                                                                                           ScanNet        Bonn      Sintel
                                                     PyTorch FP32                                  TRT FP16                                 Config.        M Init SGM AR↓ δ1 ↑ AR↓ δ1 ↑ AR↓ δ1 ↑
                                              FastPath ViTS ViTB FastPath ViTS ViTB                                                         FastPath Only ✗  –    – 0.132 0.825 0.114 0.873 0.386 0.492
                                                                                                                                            Enc. Mem.     ✓ Enc. Full 0.141 0.801 0.112 0.879 0.432 0.444
     FPS↑                                        27.8         10.1 4.1                         161.1          25.3            12.3
                                                                                                                                            DAv2 w/o SGM ✓ DAv2 L1 0.061 0.960 0.062 0.965 0.297 0.637
     Latency (ms)                                36.0         99.3 244.0                        6.2           39.5            81.0
                                                                                                                                            DAv2 L4 Only ✓ DAv2 L4 0.057 0.966 0.056 0.970 0.287 0.637
     Speedup (vs ViTB)                                      6.8×                                       13.1×                                Full SMU      ✓ DAv2 Full 0.057 0.968 0.058 0.969 0.287 0.640
        Input              GT Depth             DAv2-ViTB              CUT3R                VDA-ViTS              LiteMono†             AsyncMDE

Fig. 4. Qualitative depth comparison (least-squares aligned). The three rows correspond to ScanNet (indoor static), Bonn (indoor dynamic), and Sintel
(synthetic extreme). AsyncMDE produces depth quality comparable to DAv2-ViTB at low lag.

    Input (lag=0)      T -value (lag=1)     Depth (lag=1)       T -value (lag=5)     Depth (lag=5)       T -value (lag=10)     Depth (lag=10)
                                                                                                                                                  Retain

                                                                                                                                                       T value
                                                                                                                                                  Update

Fig. 5. T -value visualization. Each row shows, from left to right, the refresh-frame RGB, T -value masks and depth estimates at lag=1 and lag=N . Top:
indoor robotic manipulation; bottom: outdoor dynamic scene. Warm colors (T → 1) indicate static regions; cool colors (T → 0) indicate moving regions.
Degradation primarily affects moving objects, while static structures maintain stable estimates even at high lag.

E. Qualitative Results                                                        standalone compressed model. The fast path achieves 237 FPS
   Fig. 4 presents a qualitative depth comparison. In ScanNet                 (RTX 4090) / 161 FPS (Orin TRT) with 3.83M trainable
scenes, AsyncMDE’s edge sharpness and low-texture smooth-                     parameters, while the deployed system retains a 97.5M frozen
ness are close to those of DAv2-ViTB and far superior to                      slow path for periodic refresh. The system maintains bounded
LiteMono; in Bonn dynamic scenes, moving object contours                      degradation within refresh intervals, and the asynchronous
are well preserved; in Sintel, distant details show some                      amortization paradigm generalizes to dense perception tasks
degradation, consistent with the quantitative findings.                       that rely on spatiotemporal continuity.
   Fig. 5 visualizes the spatial evolution of T values across                    Limitations and future work. We identify two limitations
lag. In the indoor robotic scene (top row), T ≈ 1 everywhere                  that also suggest future research directions. Extreme motion
at lag=1 except at the robot arm’s end effector; by lag=N ,                   degradation—when scene motion causes large-scale memory
the low-T region expands along the motion trajectory with                     invalidation (an excessive fraction of T → 0), the system
local depth blurring, while static structures retain high T . In              falls back to standalone encoder inference, reaching the
the outdoor scene (bottom row), the parkour figure triggers                   inherent lower bound of the temporal continuity prior. Motion-
low T even at lag=1 and the affected area grows markedly                      adaptive memory reset or region-specific memory update
by lag=N , whereas the building background stays at T → 1                     strategies could address this. Scale consistency—the current
throughout. Two patterns emerge: (1) T values distinguish                     system outputs relative depth without inter-frame metric scale
static from dynamic regions, preserving estimate quality for                  constraints. For applications that require absolute depth, such
static structures even at high lag; (2) degradation primarily                 as robot navigation, incorporating a temporal scale alignment
affects moving objects, consistent with Section IV-C.                         module or integrating with metric depth foundation models
                                                                              would be necessary.
                       V. CONCLUSIONS
                                                                                                           R EFERENCES
   This paper presents AsyncMDE, which bridges the gap
between high-accuracy monocular depth estimation and real-                     [1] F. Yang, C. Wang, C. Cadena, and M. Hutter, “iPlanner: Imperative
                                                                                   path planning,” in Robotics: Science and Systems XIX, 2023.
time deployment by amortizing the computational cost of a                      [2] P. Roth, J. Nubert, F. Yang, M. Mittal, and M. Hutter, “ViPlanner:
foundation model over time rather than replacing it with a                         Visual semantic imperative learning for local navigation,” in 2024 IEEE
     International Conference on Robotics and Automation (ICRA), 2024,              [19] H. Lin, S. Chen, J. Liew, D. Y. Chen, Z. Li, G. Shi, J. Feng, and
     pp. 5243–5249.                                                                      B. Kang, “Depth anything 3: Recovering the visual space from any
 [3] D. Shah, A. Sridhar, N. Dashora, K. Stachowicz, K. Black, N. Hirose,                views,” arXiv preprint arXiv:2511.10647, 2025.
     and S. Levine, “ViNT: A foundation model for visual navigation,” in            [20] J. Wang, M. Chen, N. Karaev, A. Vedaldi, C. Rupprecht, and
     Proceedings of The 7th Conference on Robot Learning. PMLR, 2023,                    D. Novotny, “VGGT: Visual geometry grounded transformer,” in
     pp. 711–733, ISSN: 2640-3498.                                                       Proceedings of the IEEE/CVF Conference on Computer Vision and
 [4] A. Sridhar, D. Shah, C. Glossop, and S. Levine, “NoMaD: Goal                        Pattern Recognition, 2025, pp. 5294–5306.
     masked diffusion policies for navigation and exploration,” in 2024             [21] D. Wofk, F. Ma, T.-J. Yang, S. Karaman, and V. Sze, “FastDepth:
     IEEE International Conference on Robotics and Automation (ICRA),                    Fast monocular depth estimation on embedded systems,” in 2019
     2024, pp. 63–70.                                                                    International Conference on Robotics and Automation (ICRA), 2019,
 [5] B. Han, J. Kim, and J. Jang, “A dual process VLA: Efficient robotic                 pp. 6101–6108, ISSN: 2577-087X.
     manipulation leveraging VLM,” arXiv preprint arXiv:2410.15549, 2024.           [22] N. Zhang, F. Nex, G. Vosselman, and N. Kerle, “Lite-mono: A
 [6] NVIDIA, J. Bjorck, F. Castañeda, N. Cherniadev, X. Da, R. Ding, L. J.               lightweight CNN and transformer architecture for self-supervised
     Fan, Y. Fang, D. Fox, F. Hu, S. Huang, J. Jang, Z. Jiang, J. Kautz,                 monocular depth estimation,” in Proceedings of the IEEE/CVF Confer-
     K. Kundalia, L. Lao, Z. Li, Z. Lin, K. Lin, G. Liu, E. Llontop, L. Magne,           ence on Computer Vision and Pattern Recognition, 2023, pp. 18 537–
     A. Mandlekar, A. Narayan, S. Nasiriany, S. Reed, Y. L. Tan, G. Wang,                18 546.
     Z. Wang, J. Wang, Q. Wang, J. Xiang, Y. Xie, Y. Xu, Z. Xu, S. Ye,              [23] D. Kahneman, Thinking, Fast and Slow. Macmillan, 2011, google-
     Z. Yu, A. Zhang, H. Zhang, Y. Zhao, R. Zheng, and Y. Zhu, “GR00T                    Books-ID: SHvzzuCnuv8C.
     N1: An open foundation model for generalist humanoid robots,” arXiv            [24] H. Chen, J. Liu, C. Gu, Z. Liu, R. Zhang, X. Li, X. He, Y. Guo,
     preprint arXiv:2503.14734, 2025.                                                    C.-W. Fu, S. Zhang, and P.-A. Heng, “Fast-in-slow: A dual-system
                                                                                         foundation model unifying fast manipulation within slow reasoning,”
 [7] C. Cui, P. Ding, W. Song, S. Bai, X. Tong, Z. Ge, R. Suo, W. Zhou,
                                                                                         arXiv preprint arXiv:2506.01953, 2025.
     Y. Liu, B. Jia, H. Zhao, S. Huang, and D. Wang, “OpenHelix: A short
                                                                                    [25] H. Lin, S. Peng, J. Chen, S. Peng, J. Sun, M. Liu, H. Bao, J. Feng,
     survey, empirical analysis, and open-source dual-system VLA model
                                                                                         X. Zhou, and B. Kang, “Prompting depth anything for 4k resolution
     for robotic manipulation,” arXiv preprint arXiv:2505.03912, 2025.
                                                                                         accurate metric depth estimation,” in Proceedings of the IEEE/CVF
 [8] M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair,             Conference on Computer Vision and Pattern Recognition, 2025, pp.
     R. Rafailov, E. P. Foster, P. R. Sanketi, Q. Vuong, T. Kollar, B. Burchfiel,        17 070–17 080.
     R. Tedrake, D. Sadigh, S. Levine, P. Liang, and C. Finn, “OpenVLA:             [26] M. Liu, Z. Zhu, X. Han, P. Hu, H. Lin, X. Li, J. Chen, J. Xu, Y. Yang,
     An open-source vision-language-action model,” in Proceedings of The                 Y. Lin, X. Li, Y. Yu, W. Zhang, T. Kong, and B. Kang, “Manipulation
     8th Conference on Robot Learning. PMLR, 2025, pp. 2679–2713,                        as in simulation: Enabling accurate geometry perception in robots,”
     ISSN: 2640-3498.                                                                    arXiv preprint arXiv:2509.02530, 2025.
 [9] Z. Xu, H. Zhou, S. Peng, H. Lin, H. Guo, J. Shao, P. Yang, Q. Yang,            [27] H. Wang and L. Agapito, “3d reconstruction with spatial memory,” in
     S. Miao, X. He, Y. Wang, Y. Wang, R. Hu, Y. Liao, X. Zhou, and                      2025 International Conference on 3D Vision (3DV), 2025, pp. 78–89,
     H. Bao, “Towards depth foundation models: Recent trends in vision-                  ISSN: 2475-7888.
     based depth estimation,” Computational Visual Media, pp. 1–29, 2026.           [28] Q. Wang, Y. Zhang, A. Holynski, A. A. Efros, and A. Kanazawa,
[10] L. Yang, B. Kang, Z. Huang, Z. Zhao, X. Xu, J. Feng, and H. Zhao,                   “Continuous 3d perception model with persistent state,” in Proceed-
     “Depth anything v2,” in Advances in Neural Information Processing                   ings of the IEEE/CVF Conference on Computer Vision and Pattern
     Systems, A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet,                   Recognition, 2025, pp. 10 510–10 522.
     J. Tomczak, and C. Zhang, Eds., vol. 37. Curran Associates, Inc.,              [29] A. Howard, M. Sandler, G. Chu, L.-C. Chen, B. Chen, M. Tan, W. Wang,
     2024, pp. 21 875–21 911.                                                            Y. Zhu, R. Pang, V. Vasudevan, Q. V. Le, and H. Adam, “Searching
[11] M. Hu, W. Yin, C. Zhang, Z. Cai, X. Long, H. Chen, K. Wang, G. Yu,                  for MobileNetV3,” in Proceedings of the IEEE/CVF International
     C. Shen, and S. Shen, “Metric3d v2: A versatile monocular geometric                 Conference on Computer Vision (ICCV), 2019.
     foundation model for zero-shot metric depth and surface normal                 [30] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, “Indoor segmentation
     estimation,” IEEE Transactions on Pattern Analysis and Machine                      and support inference from RGBD images,” in Computer Vision – ECCV
     Intelligence, vol. 46, no. 12, pp. 10 579–10 596, 2024.                             2012, A. Fitzgibbon, S. Lazebnik, P. Perona, Y. Sato, and C. Schmid,
[12] L. Piccinelli, C. Sakaridis, Y.-H. Yang, M. Segu, S. Li, W. Abbeloos,               Eds. Springer, 2012, pp. 746–760.
     and L. Van Gool, “UniDepthV2: Universal monocular metric depth                 [31] W. Wang, D. Zhu, X. Wang, Y. Hu, Y. Qiu, C. Wang, Y. Hu, A. Kapoor,
     estimation made simpler,” IEEE Transactions on Pattern Analysis and                 and S. Scherer, “TartanAir: A dataset to push the limits of visual SLAM,”
     Machine Intelligence, vol. 48, no. 3, pp. 2354–2367, 2026.                          in 2020 IEEE/RSJ International Conference on Intelligent Robots and
[13] A. Bochkovskiy, A. Delaunoy, H. Germain, M. Santos, Y. Zhou,                        Systems (IROS), 2020, pp. 4909–4916, ISSN: 2153-0866.
     S. Richter, and V. Koltun, “Depth pro: Sharp monocular metric depth            [32] H. R. Walke, K. Black, T. Z. Zhao, Q. Vuong, C. Zheng, P. Hansen-
     in less than a second,” in The Thirteenth International Conference on               Estruch, A. W. He, V. Myers, M. J. Kim, M. Du, A. Lee, K. Fang,
     Learning Representations, 2024.                                                     C. Finn, and S. Levine, “BridgeData v2: A dataset for robot learning
[14] J. Shao, Y. Yang, H. Zhou, Y. Zhang, Y. Shen, V. Guizilini, Y. Wang,                at scale,” in Proceedings of The 7th Conference on Robot Learning.
     M. Poggi, and Y. Liao, “Learning temporally consistent video depth                  PMLR, 2023, pp. 1723–1736, ISSN: 2640-3498.
     from video diffusion priors,” in Proceedings of the IEEE/CVF Confer-           [33] A. Dai, A. X. Chang, M. Savva, M. Halber, T. Funkhouser, and
     ence on Computer Vision and Pattern Recognition, 2025, pp. 22 841–                  M. Niessner, “ScanNet: Richly-annotated 3d reconstructions of indoor
     22 852.                                                                             scenes,” in Proceedings of the IEEE Conference on Computer Vision
[15] W. Hu, X. Gao, X. Li, S. Zhao, X. Cun, Y. Zhang, L. Quan, and                       and Pattern Recognition, 2017, pp. 5828–5839.
     Y. Shan, “DepthCrafter: Generating consistent long depth sequences             [34] E. Palazzolo, J. Behley, P. Lottes, P. Giguère, and C. Stachniss,
     for open-world videos,” in Proceedings of the IEEE/CVF Conference                   “ReFusion: 3d reconstruction in dynamic environments for RGB-
     on Computer Vision and Pattern Recognition, 2025, pp. 2005–2015.                    d cameras exploiting residuals,” in 2019 IEEE/RSJ International
                                                                                         Conference on Intelligent Robots and Systems (IROS), 2019, pp. 7855–
[16] S. Chen, H. Guo, S. Zhu, F. Zhang, Z. Huang, J. Feng, and B. Kang,
                                                                                         7862, ISSN: 2153-0866.
     “Video depth anything: Consistent depth estimation for super-long
                                                                                    [35] D. J. Butler, J. Wulff, G. B. Stanley, and M. J. Black, “A naturalistic
     videos,” in Proceedings of the IEEE/CVF Conference on Computer
                                                                                         open source movie for optical flow evaluation,” in Computer Vision
     Vision and Pattern Recognition, 2025, pp. 22 831–22 840.
                                                                                         – ECCV 2012, A. Fitzgibbon, S. Lazebnik, P. Perona, Y. Sato, and
[17] G. Chou, W. Xian, G. Yang, M. Abdelfattah, B. Hariharan, N. Snavely,                C. Schmid, Eds. Springer, 2012, pp. 611–625.
     N. Yu, and P. Debevec, “FlashDepth: Real-time streaming video                  [36] S. Mehta and M. Rastegari, “MobileViT: Light-weight, general-purpose,
     depth estimation at 2k resolution,” in Proceedings of the IEEE/CVF                  and mobile-friendly vision transformer,” in International Conference
     International Conference on Computer Vision, 2025, pp. 9638–9648.                   on Learning Representations, 2021.
[18] Z. Kuang, T. Zhang, K. Zhang, H. Tan, S. Bi, Y. Hu, Z. Xu, M. Hasan,           [37] H. Cai, J. Li, M. Hu, C. Gan, and S. Han, “EfficientViT: Lightweight
     G. Wetzstein, and F. Luan, “Buffer anytime: Zero-shot video depth                   multi-scale attention for high-resolution dense prediction,” in Proceed-
     and normal from image priors,” in Proceedings of the IEEE/CVF                       ings of the IEEE/CVF International Conference on Computer Vision,
     Conference on Computer Vision and Pattern Recognition, 2025, pp.                    2023, pp. 17 302–17 313.
     17 660–17 670.
