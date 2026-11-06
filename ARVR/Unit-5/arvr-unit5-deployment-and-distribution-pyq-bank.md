# ARVR Unit 5: Deployment and Distribution — Exam PYQ Bank & Model Answers

This comprehensive, exam-oriented Previous Year Question (PYQ) bank covers **Unit 5: Deployment and Distribution** as prescribed in the SVKM's NMIMS MPSTME curriculum (**Course Code: 702COI002 / 702MH0I004**). It compiles every actual examination question extracted from university examination papers (2023–2026), mapped directly against the official Term End Exam (TEE) Answer Key, syllabus requirements, lecture slide decks, and authoritative reference textbooks (*Creating Augmented and Virtual Realities* by Erin Pangilinan, Steve Lukas, & Vasanth Mohan; *Complete Virtual Reality and Augmented Reality Development with Unity* by Jesse Glover & Jonathan Linowes).

> [!IMPORTANT]
> **Theory & Architecture Focus**: In strict adherence to exam evaluation guidelines, all answers are presented purely conceptually and theoretically. Head-Related Transfer Function acoustics, forward vs. deferred rendering paths, Android compilation targets, and OVR Metrics profiling HUDs are illustrated via structured comparison tables, engineering schemas, and ASCII box-and-arrow diagrams without source code.

---

## Course Policy & Learning Objective Alignment

* **Course Outcome (CO):** **CO2, CO3** — Design, optimize, profile, and deploy basic AR/VR standalone applications across target platforms, adhering to runtime performance budgets and user comfort protocols.
* **Bloom's Taxonomy Level:** **K2 (Understand), K3 (Apply)** — Formulating spatial audio acoustic pipelines, configuring platform build targets, analyzing GPU/CPU profiling metrics, and enforcing physiological user safety standards.
* **Examination Weightage & Structure:**
  * **Structured Descriptive / Technical Essays (Q3):** 10 Marks each (Lighting techniques, PBR shaders, materials, and mobile performance trade-offs).
  * **Master Deployment Pipeline Scenario (Q7):** 20 Marks (Comprehensive Meta Quest deployment evaluated across build configuration [6M], device profiling [6M], and user comfort guidelines [8M]).
  * **Applied Acoustic & Store Distribution Blueprints:** 10 Marks each (HRTF spatial acoustics, App Lab vs. Quest Store submission requirements).

---

## Part 1: Verified University Examination Questions & Model Answers

### Topic 1: Visual Realism, Lighting & Shader Performance Trade-offs

#### Question Group 1.1: Contribution of Lighting, Shaders & Materials to VR Realism
* **Original PYQs:**
  1. *"Explain how Lighting, Shaders, and Materials contribute to realism in VR. Discuss performance trade-offs."* (SVKMs NMIMS MPSTME, Final Exam, Acad. Year 2024–2025, Semester V, Date: 10 Dec 2025, Q3-b, **Marks: 10**, CO-2, CO-3; BL-3) [Answer Key Synoptics Q3-b; Glover & Linowes, Ch. 11; Pangilinan et al., Ch. 8]
* **Official Answer Key Mark Split (10 Marks Total):**
  * **Lighting Techniques (Real-Time vs. Baked Lightmaps & Probes):** **4 Marks**
  * **Shader & Material Roles (Physically Based Rendering / PBR):** **3 Marks**
  * **Performance Trade-offs & Mobile VR Hardware Bottlenecks:** **3 Marks**
* **Priority Level:** 🔥 **Very Important** (Official 10-Mark Answer Key Question)
* **Diagram Required:** YES | Type: Rendering Pipeline Matrix | Exam Sketch Target: Real-Time vs Baked Illumination

##### Model Answer (10 Marks):

```
📊 Diagram Required: YES | Type: Architecture Flow | Exam Sketch Target: Baked vs Real-Time Illumination

  OFFLINE PRE-COMPUTATION (Unity Editor)       RUNTIME EXECUTION (Meta Quest Standalone)
  ═════════════════════════════════════       ═════════════════════════════════════════
  [ High-Poly Static Architecture ]
  [ Complex Area / Spotlight Rigs ]
                 │
                 ▼
  [ Global Illumination Raytracer ] ────────► [ 2D Baked Lightmap Textures ]
  (Bakes Radiosity, Ambient Occlusion)        (Zero runtime lighting math on GPU)
                 │                                        │
                 ▼                                        ▼
  [ Light Probe Tetrahedral Grid ]  ────────► [ Sampled by Dynamic VR Objects ]
  (Captures directional photon cache)         (Beakers / Characters lit accurately)
```

---

#### Section A: Lighting Techniques in VR (4 Marks)

1. **The Dual Stereoscopic Challenge:**
   * In traditional gaming, lighting calculations execute once per pixel per frame. In VR, the engine must compute lighting for two separate eye viewports at high refresh rates ($72\text{ to } 90\text{ Hz}$), making dynamic real-time global illumination mathematically prohibitive on mobile chipsets.

2. **Baked Lightmapping (Static Global Illumination):**
   * **Mechanism:** In the editor, an offline progressive GPU raytracer simulates physical photon bouncing (radiosity, soft area shadows, color bleeding, and ambient occlusion). These complex mathematical calculations are baked directly into 2D **Lightmap Texture Atlases** wrapped around static room surfaces.
   * **Realism Impact:** Delivers photorealistic cinematic lighting with soft contact shadows and ambient bounces with **absolute zero runtime lighting calculation cost** on the mobile GPU.

3. **Light Probes & Reflection Probes (Dynamic Integration):**
   * **Light Probes:** An invisible 3D tetrahedral grid of spatial probes placed throughout the room samples baked photon intensity and color. When dynamic objects (moving hands, test tubes) traverse the space, they interpolate lighting from adjacent probes, appearing naturally illuminated without casting expensive real-time shadows.
   * **Reflection Probes:** Pre-render $360^\circ$ environment cubemaps, providing physically accurate metallic and glossy specular reflections on glassware and shiny surfaces.

---

#### Section B: Shaders & Materials in VR (Physically Based Rendering) (3 Marks)

1. **Physically Based Rendering (PBR) Materials:**
   * Modern XR engines replace artificial Phong shading with **PBR Shaders** governed by physical optical laws (conservation of energy):
     * *Albedo (Base Color):* Pure surface diffuse color devoid of directional shadows.
     * *Metallic:* Scalar determining whether the material behaves as a conductor (metal) or dielectric (plastic, wood, glass).
     * *Smoothness / Roughness:* Microfacet distribution governing whether light reflects as a sharp mirror highlight or a broad diffuse blur.
     * *Normal Mapping:* Simulates micro-geometric surface details (brick crevices, bolt threads, leather grains) without adding high-poly vertex geometry.

2. **Universal Render Pipeline (URP) Custom XR Shaders:**
   * Uses streamlined shader graphs:
     * *Complex Lit:* Full PBR shading with normal maps and specular reflections for key focus objects held in the user's hands.
     * *Simple Lit (Blinn-Phong):* Lightweight specular shading for secondary background props.
     * *Unlit:* Pure texture sampling with zero lighting calculation, reserved for spatial UI panels and distant backdrops.

---

#### Section C: Performance Trade-offs & Mobile Hardware Bottlenecks (3 Marks)

| Visual Feature | High Realism Option (PCVR / High-End) | Performance-Optimized VR Option (Standalone Quest) | Technical Trade-off |
| :--- | :--- | :--- | :--- |
| **Shadows** | Real-Time Cascaded Shadow Maps (CSM) | Hard Baked Shadows + Light Probes | Real-time shadows cause severe GPU fragment fill-rate exhaustion and frame drops. |
| **Rendering Path** | **Deferred Shading** (Calculates lighting in screen G-Buffers) | **Forward Single-Pass Stereo** (Calculates lighting per-vertex/per-object) | Deferred shading requires massive memory bandwidth ($>100\text{ GB/s}$), causing thermal throttling on mobile mobile chips; Forward Rendering allows hardware MSAA anti-aliasing. |
| **Material Shaders** | Parallax Occlusion Mapping, Subsurface Scattering | Standard PBR with Normal Maps or Baked Albedo | Subsurface skin/marble scattering requires multiple render passes, exceeding the $11.1\text{ ms}$ VR frame budget. |
| **Transparency** | Depth-Sorted Multi-Layer Alpha Blending | Opaque Meshes or Alpha-Testing (Cutout) | Transparent overlapping surfaces (smoke, glass beakers) cause severe **Overdraw**, forcing the GPU to re-render the same pixel multiple times. |

---

### Topic 2: Master VR Deployment Scenario (20-Mark Question Paper Staple)

#### Question Group 2.1: End-to-End VR Deployment Process to Meta Quest
* **Original PYQs:**
  1. *"Describe the deployment process of a VR application using Unity and Meta Quest. Explain build targets, device profiling, testing, and user safety optimization."* (SVKMs NMIMS MPSTME, Final Exam, Acad. Year 2024–2025, Semester V, Date: 10 Dec 2025, Q7, **Marks: 20**, CO-2, CO-3; BL-3) [Answer Key Synoptics Q7; Glover & Linowes, Ch. 12; Pangilinan et al., Ch. 11]
* **Official Answer Key Mark Split (20 Marks Total):**
  * **Component 1: Build target configuration and Android export:** **6 Marks**
  * **Component 2: Profiling, device testing, and performance analysis:** **6 Marks**
  * **Component 3: User comfort, safety guidelines, and VR hygiene:** **8 Marks**
* **Priority Level:** 🔥 **Very Important** (Official 20-Mark Term-End Exam Scenario)
* **Diagram Required:** YES | Type: Deployment Pipeline Sequence | Exam Sketch Target: Build to Deployment Architecture

##### Model Answer (20 Marks):

```
📊 Diagram Required: YES | Type: Deployment Pipeline | Exam Sketch Target: VR Build & Profiling Workflow

  +────────────────────────────────────────────────────────────────────────────+
  |              VR STANDALONE DEPLOYMENT & PROFILING PIPELINE                 |
  +────────────────────────────────────────────────────────────────────────────+

  ┌────────────────────────────────────────────────────────────────────────────┐
  | 1. BUILD TARGET CONFIGURATION & ANDROID EXPORT                             |
  | • Platform Switch: Android | Architecture: ARM64                           |
  | • Compiler Backend: IL2CPP (Ahead-of-Time C++ Compilation)                |
  | • Graphics API: Vulkan | Texture Compression: ASTC                         |
  | • OpenXR Loader: Meta Quest Feature Group Active                           |
  └─────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
  ┌────────────────────────────────────────────────────────────────────────────┐
  | 2. DEVICE PROFILING & RUNTIME PERFORMANCE TESTING                          |
  | • On-Device HUD: OVR Metrics Tool (Real-time FPS, CPU/GPU utilization)    |
  | • Frame Analysis: Unity Frame Debugger (Draw call breakdown <150 calls)    |
  | • Memory & Threading: Unity Profiler (Garbage collection spikes = 0 ms)    |
  └─────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
  ┌────────────────────────────────────────────────────────────────────────────┐
  | 3. USER COMFORT, SAFETY OPTIMIZATION & STORE COMPLIANCE                    |
  | • Visual Comfort: Fixed Foveated Rendering & Chromatic Aberration Corr.    |
  | • Locomotion Ergonomics: Snap Turning (30 deg) & Dynamic FOV Vignetting    |
  | • Physical Guardian Safety: Real-world boundary integration                |
  | • Comfort Rating Certification: Comfortable / Moderate / Intense           |
  └────────────────────────────────────────────────────────────────────────────┘
```

---

#### Component 1: Build Target Configuration & Android Export (6 Marks)

The Meta Quest operates on a modified Android operating system (Android Open Source Project / AOSP) running atop Qualcomm Snapdragon XR2 silicon. Exporting a standalone `.apk` or `.aab` package requires specific architectural configurations:

**1. Platform & Compilation Settings:**
* **Platform Switch:** The active build target is switched from Desktop to **Android** within the Unity Build Settings window.
* **Scripting Backend (IL2CPP):** The default Mono JIT (Just-In-Time) compilation is replaced with **IL2CPP (Intermediate Language to C++)**. IL2CPP translates C# code directly into highly optimized native C++ machine code prior to packaging, slashing CPU execution time and unlocking 64-bit performance.
* **Target Architecture:** Configured strictly for **ARM64**. 32-bit ARMv7 architectures are completely deprecated and rejected by the Meta Quest Store.

**2. Graphics API & Stereo Pipelines:**
* **Graphics API:** **Vulkan** is selected as the primary graphics API, bypassing legacy OpenGL ES. Vulkan provides direct low-level GPU hardware control, multi-threaded command buffer generation, and drastically reduced CPU driver overhead.
* **Stereo Rendering Mode:** Configured to **Single Pass Instanced**. The GPU draws geometry into both eye viewports using a single vertex stream, cutting CPU draw call preparation by almost $50\%$.
* **Texture Compression:** Set to **ASTC (Adaptive Scalable Texture Compression)**, maximizing texture detail while minimizing memory bus saturation.

**3. Project Manifest & OpenXR Integration:**
* **XR Plugin Management:** The **OpenXR** backend is initialized, enabling the **Meta Quest Support Feature Group** (handling boundary guardians, controller models, hand tracking, and system overlays).
* **Package Manifest (`AndroidManifest.xml`):**
  * Configures `minSdkVersion = 29` (Android 10+) and `targetSdkVersion = 32+`.
  * Injects mandatory VR hardware flags:
    `<uses-feature android:name="android.hardware.vr.headtracking" android:required="true" android:version="1" />`
  * Defines Quest device form factor compatibility (Quest 2, Quest 3, Quest Pro).

---

#### Component 2: Device Profiling & Runtime Performance Testing (6 Marks)

Rigorous testing directly on the physical Quest headset is required to verify that the application satisfies the non-negotiable **Meta VRCs (Virtual Reality Checks)**: locked target frame rate ($72, 90, \text{ or } 120\text{ FPS}$), zero dropped frames, and thermal stability.

**1. OVR Metrics Tool (On-Device Profiling HUD):**
* The **OVR Metrics Tool** is sideloaded directly onto the Quest hardware. It renders a floating heads-up display overlay atop the live running application, providing continuous, non-intrusive runtime telemetry:
  * **FPS & Stale Frame Counter:** Monitors instantaneous frame rate. Detects "Stale Frames" (frames where the GPU failed to render in time, forcing the display compositor to reproject the previous frame via Asynchronous Spacewarp / ASW).
  * **CPU / GPU Clock Level Utilization:** Tracks hardware performance states (Levels $0 - 5$). If GPU utilization constantly hovers at Level 5 with $100\%$ utilization, the app will trigger thermal throttling within $15$ minutes, forcing the OS to aggressively downclock the chipset.
  * **Thermal Throttle Warning:** Verifies whether device temperature remains within safe handheld/headset limits ($<42^\circ\text{C}$).

**2. Unity Profiler Analysis:**
* The headset is connected to the development workstation via USB-C or Wi-Fi with **Autoconnect Profiler** enabled:
  * **CPU Usage Profiler:** Identifies CPU execution spikes. Verifies that `GC.Alloc` (Garbage Collection Allocation) is exactly **$0\text{ bytes}$ per frame** during active gameplay, ensuring no Garbage Collector pauses interrupt the rendering loop.
  * **GPU Profiler:** Traces per-pass rendering times. Confirms total GPU frame time stays strictly beneath the $11.1\text{ ms}$ threshold ($90\text{ FPS}$).

**3. Unity Frame Debugger (Draw Call Clamping):**
* Freezes a single rendered frame to inspect every individual draw call sequentially:
  * Validates that static meshes are successfully merging via **Static Batching**.
  * Confirms repetitive assets (test tubes, foliage, particles) are rendering via **GPU Instancing**.
  * Ensures total draw calls remain clamped below the safe mobile VR ceiling: **$<150$ draw calls per frame**.

---

#### Component 3: User Comfort, Safety Guidelines & VR Hygiene (8 Marks)

Because VR directly stimulates the human vestibular, ocular, and nervous systems, applications must strictly follow physiological comfort guidelines to prevent nausea, eye fatigue, and physical collision injuries.

```
+────────────────────────────────────────────────────────────────────────────+
|                    USER COMFORT & SAFETY RUBRIC MATRIX                     |
+────────────────────────────────────────────────────────────────────────────+

  1. VESTIBULAR HARMONY     2. OCULAR COMFORT        3. PHYSICAL SAFETY
  • Motion-to-Photon <20ms  • No text < 0.75m        • Meta Guardian bounds
  • No forced camera roll   • Interpupillary range   • Floor height zeroing
  • Snap turning (30-45 deg)• VAC fatigue mitigation • Roomscale clearance
```

**1. Vestibular System & Motion Sickness Mitigation:**
* **Visual-Vestibular Conflict Prevention:** The inner ear's vestibular semicircular canals sense physical rotational and linear acceleration. If the virtual camera moves or rotates without corresponding physical body acceleration, sensory conflict triggers nausea.
* **Camera Autonomy Prohibition:** The virtual camera transform must be driven **100% by the user's physical head movements**. Developers must *never* introduce artificial head-bobbing, camera shaking, or involuntary camera rotations during cutscenes.
* **Comfort Locomotion Standards:**
  * Implement **Teleportation** as the default locomotion system.
  * If continuous joystick motion is enabled, force **Snap Turning** ($30^\circ \text{ or } 45^\circ$ instant steps) to eliminate the severe nausea caused by smooth horizontal panning.
  * Deploy a **Dynamic FOV Vignette** (tunneling mask) that contracts peripheral vision during fast forward translation.

**2. Ocular Comfort & Optical Ergonomics:**
* **Vergence-Accommodation Conflict (VAC):** Human eyes naturally converge on an object while simultaneously adjusting the lens focal length (accommodation). In modern fixed-focal-plane VR headsets (focal distance $\approx 1.5 - 2.0\text{ meters}$), virtual objects placed extremely close to the eyes ($<0.5\text{ meters}$) force eyes to converge sharply while accommodating at distance, inducing severe eye strain and double vision.
* **Spatial UI Placement Rule:** All text, UI menus, and interactive targets must be positioned within the **Comfortable Vergence Zone**: between **$1.0\text{ meter}$ and $3.0\text{ meters}$** from the user's eyes, with text font size scaled to maintain an angular visual resolution of at least $1.2^\circ$ per character.

**3. Physical Environment Guardian Safety & Store Ratings:**
* **Meta Guardian Boundary Integration:** The application must immediately pause, mute audio, and fade to passthrough video if the user steps outside their calibrated physical safe zone or approaches a physical wall.
* **Floor Height Zeroing:** The tracking origin must correctly calibrate floor level to prevent the user from reaching through physical flooring when picking up dropped virtual items.
* **Meta Comfort Rating Certification:** Applications submitted to the Meta Quest Store undergo mandatory human comfort testing and receive an official public comfort certification tag:
  * **Comfortable:** Zero camera acceleration; teleportation only.
  * **Moderate:** Mild translational motion with comfort vignetting.
  * **Intense:** Full 6DoF flight simulators, roller coasters, or rapid acrobatic maneuvers.

---

### Topic 3: Spatial Audio in AR/VR: HRTF & Acoustic Mechanics

#### Question Group 3.1: Head-Related Transfer Functions (HRTF), ITD, ILD & Acoustic Occlusion
* **Original PYQs:**
  1. *"Explain the implementation and physics of Spatial Audio in AR/VR. How do Head-Related Transfer Functions (HRTF), ITD, and ILD enable 3D auditory localization?"* (Model Question / TEE Syllabus Unit 5, **Marks: 10**, CO-1, CO-2; BL-2) [Slide 2–8; Pangilinan et al., Ch. 7]
* **Priority Level:** ⭐ **Important** (Core acoustic realism topic)
* **Diagram Required:** YES | Type: Acoustic Physics Diagram | Exam Sketch Target: ITD and ILD Spatial Geometry

##### Model Answer (10 Marks):

```
📊 Diagram Required: YES | Type: Acoustic Geometry | Exam Sketch Target: ITD and ILD Sound Paths

                               [ 3D Audio Source ]
                                  /            \
                                 /              \
             Path 1 (Shorter)   /                \   Path 2 (Longer; around skull)
                               ▼                  ▼
                         [ Near Ear ]        [ Far Ear ]
                         
  1. ITD (Time Difference): Sound reaches Near Ear first (Delta t = d / c)
  2. ILD (Level Difference): Head casts an "Acoustic Shadow", dampening high frequencies at Far Ear
```

**1. Foundational Physics of Human Spatial Localization (4 Marks):**
Humans perceive the precise 3D direction and distance of a sound using binaural auditory cues processed by the brain:

* **Interaural Time Difference (ITD):**
  * **Physics:** The speed of sound in air is finite ($c \approx 343\text{ m/s}$). If an audio emitter is located to the right of the listener, the sound wave reaches the right ear slightly before it reaches the left ear.
  * The time disparity $\Delta t$ ranges from $0\text{ ms}$ (sound directly in front) to $\approx 0.65\text{ ms}$ (sound directly at $90^\circ$ azimuth):
    $$\Delta t = \frac{r}{c} (\theta + \sin\theta)$$
  * **Frequency Range:** Governs low-frequency sound localization ($<1500\text{ Hz}$).

* **Interaural Level Difference (ILD):**
  * **Physics:** The human head acts as a solid physical obstacle (an **Acoustic Shadow**). High-frequency sound waves have wavelengths smaller than the diameter of the human skull ($\approx 20\text{ cm}$). When sound originates from the side, the near ear receives full sound pressure, while the far ear receives attenuated, muffled sound.
  * **Frequency Range:** Governs high-frequency sound localization ($>1500\text{ Hz}$), producing an intensity disparity of up to $20\text{ dB}$.

**2. Head-Related Transfer Functions (HRTF) (3 Marks):**
* **The Spectral Pinna Cue:** ITD and ILD cannot distinguish between a sound placed directly in front versus directly behind (the *Cone of Confusion*).
* **HRTF Mechanism:** The complex, asymmetrical cartilaginous convolutions of the human outer ear (pinna), ear canal, head, and shoulders act as an anatomical acoustic filter. As sound waves strike these contours from different vertical elevations and azimuths, specific frequencies undergo microscopic phase cancellations and resonances.
* **Digital Implementation:** An **HRTF** is a pair of complex mathematical impulse response filters (measured in anechoic chambers) applied via real-time convolution to raw mono audio signals. When convolved with the user's current 6DoF head orientation, it fools the brain into perceiving sounds originating above, below, behind, or at exact metric distances in 3D space.

**3. Environmental Audio Propagation: Occlusion vs. Obstruction (3 Marks):**
* **Acoustic Obstruction:** A physical obstacle (e.g., a glass window or pillar) partially blocks the direct line-of-sight sound path between emitter and listener, but sound waves wrap around the obstacle via environmental reflections (reverb remains natural, while direct high frequencies are dampened).
* **Acoustic Occlusion:** The sound source is completely enclosed in an adjacent room behind solid concrete walls. Both the direct sound path and room reverberation are heavily muffled using a low-pass cutoff filter ($<500\text{ Hz}$), simulating sound transmission through solid matter.

---

## Part 2: Analytical Appendix & University Exam Trends

### 1. Topic-Wise Frequency Table

| Topic / Exam Question Focus | Question ID Mapping | Historical Appearance | Exam Mark Weightage |
| :--- | :--- | :--- | :--- |
| **VR Master Scenario: Deployment to Meta Quest** | Q7 | Final Exam 2024–25 | **20 Marks** (Section 2 Staple) |
| **Visual Realism: Lighting, Shaders, Materials & Performance** | Q3(b) | Final Exam 2024–25 | **10 Marks** (Section 2 Staple) |
| **Spatial Audio: HRTF, ITD, ILD & Acoustic Mechanics** | Topic 3.1 Blueprint | TEE Syllabus Benchmark | **10 Marks** |
| **User Safety, Comfort Guidelines & Store VRC Protocols** | Part of Q7 | Final Exam 2024–25 | **8 Marks** |

---

### 2. Question Priority Matrix

* 🔥 **Very Important (Tier 1 - Guaranteed Exam Staples):**
  * **Q3(b) [10M]:** Lighting techniques (baked vs. real-time), PBR shaders, and mobile VR performance trade-offs.
  * **Q7 [20M]:** Meta Quest deployment workflow (Android build target [6M], profiling & OVR Metrics [6M], user comfort & safety [8M]).
* ⭐ **Important (Tier 2 - High-Yield Structural Topics):**
  * **Spatial Audio in AR/VR [10M]:** HRTF convolution, ITD vs. ILD physics, acoustic occlusion vs. obstruction.
  * **Forward vs. Deferred Rendering in XR [10M]:** Memory bandwidth constraints and MSAA compatibility.
* 🟡 **Moderate Priority (Tier 3 - Conceptual Breadth):**
  * Meta Quest Store vs. App Lab distribution channels.
  * ASTC texture compression and draw call budgeting.

---

### 3. Concept Redundancy Map & Past Rephrasings

* *Rephrasing 1:* "Why can't we use Deferred Shading on Meta Quest?" $\Longleftrightarrow$ Covered under **Question Group 1.1, Section C** (Deferred shading requires massive memory bandwidth for multiple G-Buffers, causing rapid thermal throttling on mobile GPUs).
* *Rephrasing 2:* "Explain the role of OVR Metrics Tool." $\Longleftrightarrow$ Covered under **Question Group 2.1, Component 2** (Real-time on-device HUD tracking FPS, stale frames, CPU/GPU utilization levels, and thermal throttling).
* *Rephrasing 3:* "What is the difference between ITD and ILD?" $\Longleftrightarrow$ Covered under **Question Group 3.1** (ITD = time delay for low frequencies; ILD = head-shadow intensity attenuation for high frequencies).

---

### 4. Syllabus & Slide Coverage Audit

* [x] **Implementing spatial audio in AR/VR:** Exhaustively covered in Topic 3.1 (HRTF, ITD, ILD, occlusion).
* [x] **Visual effects, shaders, and lighting techniques:** Fully detailed in Topic 1.1 (Baked Lightmaps, PBR, URP).
* [x] **Platform considerations for AR/VR deployment:** Detailed in Component 1 of Q7 (Android ARM64, Vulkan, IL2CPP).
* [x] **Building standalone applications:** Covered step-by-step in Component 1 of Q7.
* [x] **App store submission & distribution process:** Covered under Meta VRCs, Guardian rules, and Comfort ratings in Component 2 & 3.
