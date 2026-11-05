# Comprehensive Study Notes — Unit 5: Deployment and Distribution

This study guide provides a rigorous, exam-focused synthesis of **Unit 5: 
Deployment and Distribution** for the NMIMS B.Tech/MBA Tech Extended Reality 
curriculum (*Course Code: 702COI002*). It covers spatial sound physics, 
real-time rendering pipelines, platform architecture, submission standards, 
profiling tools, human factors, and model answers for official semester 
examination questions.

---

## 1. Spatial Audio in AR/VR

Spatial audio delivers depth, directionality, and environmental realism by 
recreating three-dimensional acoustic propagation as perceived by the human 
auditory system. In immersive environments, directional audio cues are as vital
as visual feedback for user orientation and spatial presence.

### Head-Related Transfer Functions (HRTF)
A Head-Related Transfer Function ($\text{HRTF}$) is a complex mathematical 
response function that models how a sound wave arriving from a specific point 
in 3D space $(r, \theta, \phi)$ is acoustically filtered by human 
anatomical structures—specifically the pinna (outer ear), head geometry, neck, 
and shoulders—before entering the ear canal.

$$
\text{HRTF}_L(f, r, \theta, \phi) = \frac{P_L(f, r, \theta, \phi)}{P_0(f)}
$$

Where $P_L$ represents the sound pressure at the left eardrum and $P_0$
is the free-field sound pressure at the center of the head. HRTFs alter the 
frequency spectrum of the sound, providing high-frequency spectral cues that 
allow the brain to distinguish vertical elevation $(\phi)$ and front-back 
orientation.

### Interaural Spatial Cues: ITD and ILD
Duplex theory governs horizontal azimuth $(\theta)$ sound localization 
through two primary interaural cues:

1. **Interaural Time Difference (ITD)**:
   * **Mechanism**: The physical distance difference between the two ears 
creates a time delay when sound arrives from an off-center source.
   * **Frequency Range**: Dominant for low-frequency acoustic waves ($< 
1500\text{ Hz}$), where the acoustic wavelength is larger than the human head
diameter.
   * **Delay Calculation**: For a head radius $a$ and sound velocity 
$c$, the time delay $\Delta t$ is approximated by:

$$
\Delta t = \frac{a}{c} (\theta + \sin\theta)
$$

2. **Interaural Level Difference (ILD)**:
   * **Mechanism**: The physical head acts as an acoustic barrier ("head 
shadow"), attenuating high-frequency sound waves arriving at the far ear.
   * **Frequency Range**: Dominant for high-frequency acoustic waves ($> 
1500\text{ Hz}$), where wavelengths are shorter than head dimensions, 
creating significant amplitude drop-off.

```
       [ Sound Source ] (High & Low Frequencies)
            /        \
           /          \ (Direct Path)
          /            \
    (Near Ear)      [ Head ] (Acoustic Shadow Blocks High Freq)
    Direct sound       |
    Arrives First     (Far Ear) Attenuated Sound Arrives Later
    (Higher dB)       (Lower dB + Time Delay \Delta t)
```

### 3D Sound Positioning and Attenuation in Engines
In engine architectures such as Unity, 3D spatial sound placement requires 
binding an `AudioSource` component to a 3D spatial transform while an 
`AudioListener` component is attached to the player's main camera rig 
(representing the user's ears).

* **Spatial Blend**: Scalar parameter set to `1.0` for full 3D spatialization 
(0.0 represents 2D monaural/stereophonic playback).
* **Distance Attenuation**: Defines volume decay over physical distance 
$d$:
  * **Logarithmic Roll-off**: $V(d) = \frac{\text{Min Distance}}{d}$, 
matching real-world inverse-square energy dissipation.
  * **Linear Roll-off**: $V(d) = 1 - \frac{d - \text{Min Distance}}{\text{Max
Distance} - \text{Min Distance}}$, used for predictable game balance.
* **Min/Max Distance**: `Min Distance` establishes the threshold within which 
volume remains at $100\%$. Beyond `Max Distance`, volume attenuates to 
zero.

### Acoustic Occlusion vs. Obstruction
Environmental objects degrade direct acoustic waves based on physical geometry:

| Acoustic Feature | Physical Definition | Direct Sound Path | Reverberant / Diffuse Path | Signal Modification |
| :--- | :--- | :--- | :--- | :--- |
| **Obstruction** | An obstacle blocks the direct line-of-sight between source and listener, but secondary openings allow reflected sound to pass. | Fully Blocked | Unaffected / Open | Low-pass filtered direct signal; ambient room reverb remains normal. |
| **Occlusion** | Source and listener are in separate enclosed spaces divided by solid geometry (e.g., a closed wall). | Fully Blocked | Fully Blocked | Severe attenuation across all frequencies; low-frequency muffle dominates. |

### Reverb Zones and Doppler Effect
* **Reverb Zones (`AudioReverbZone`)**: Spherical environmental triggers that 
modify global acoustics. Parameters include `Decay Time`, `Reflection Level`, 
and reverb presets (`PaddedCell`, `Cave`, `Hallway`) to simulate room volume 
and surface absorbency.
* **Doppler Effect**: Pitch modification resulting from relative velocity 
between the source ($\vec{v}_s$) and listener ($\vec{v}_l$). The 
observed frequency $f$ is given by:

\

Where $c$ is the speed of sound and $\hat{r}$ is the unit vector along 
the source-listener axis. In VR, excessive Doppler scaling can induce 
disorientation and is typically clamped.

---

## 2. Visual Realism: Lighting, Shaders, and Materials

Achieving high visual fidelity under strict real-time frame budgets requires a 
detailed understanding of rendering pipelines, shading models, and lighting 
precomputations.

### Forward Rendering vs. Deferred Rendering in XR

```
FORWARD RENDERING PIPELINE (XR Gold Standard):
[ Geometry Pass ] ---> [ Shader & Light Calculations Per Object ] ---> [ 
Framebuffer + MSAA ]
(Memory Efficient, Single-Pass Instanced, Low VRAM Bandwidth)

DEFERRED RENDERING PIPELINE (High Desktop PCVR Cost):
[ Geometry Pass ] ---> [ Write to G-Buffer (Normals, Albedo, Depth) ] ---> [ 
Lighting Compute Pass ] ---> [ Final Composition ]
(Extreme VRAM Bandwidth, No Native MSAA, High Tile Memory Penalty on Mobile 
GPUs)
```

1. **Forward Rendering**:
   * **Mechanism**: Each object geometry is rendered, and light calculations 
are executed per-light for every visible fragment.
   * **XR Performance Advantages**: Compatible with hardware Multi-Sample 
Anti-Aliasing (MSAA), which is essential for eliminating sub-pixel aliasing and
specular shimmer in VR HMD lenses. Highly efficient on mobile Tile-Based 
Deferred Rendering (TBDR) GPUs (e.g., Adreno on Meta Quest) as fragment 
operations stay within fast on-chip SRAM.
   * **Single Pass Instanced Rendering**: Renders left and right eye views 
simultaneously in a single draw call by instancing draw calls and propagating 
eye indices to the render target array, cutting CPU draw call overhead by 
$50\%$.

2. **Deferred Rendering**:
   * **Mechanism**: Decouples geometry rendering from lighting. Surface 
attributes (albedo, world normals, roughness, depth) are rendered into a 
massive multi-target buffer (G-Buffer). Lighting is calculated in a second 
screen-space pass.
   * **XR Drawbacks**: High VRAM memory bandwidth requirements caused by 
writing/reading multi-target G-Buffers. Incompatible with native MSAA (requires
expensive spatial anti-aliasing like FXAA/TAA, which introduces blurriness in 
HMDs).

### Universal Render Pipeline (URP) Configurations for XR
Unity's URP is optimized specifically for cross-platform XR development:
* **Single Pass Instanced**: Mandatory pipeline setting ensuring left/right eye
stereo buffers are submitted in a single pass.
* **Render Scale**: Scales internal rendering resolution independently of 
physical display panel resolution (e.g., $0.8\times$ to reduce GPU load, 
$1.2\times$ for supersampling sharpness).
* **Fixed Foveated Rendering (FFR)**: Utilizes Vulkan/OpenGL extensions to 
shade the peripheral regions of the display at lower fragment density than the 
focal center, saving up to $20\%$ GPU fill-rate.

### Shader Complexity: Unlit vs. Simple Lit vs. Complex Lit (PBR)

```
SHADER COMPUTATIONAL SPECTRUM:
+------------------------------------------------------------------------------
-+
|  UNLIT SHADER          |  SIMPLE LIT (Blinn-Phong)   |  COMPLEX LIT (PBR)    
|
|  - Raw Texture Sampling|  - Per-Vertex/Pixel Diffuse  |  - 
Metallic/Smoothness |
|  - Zero Lighting ALU   |  - Empirical Specular Highlight| - Cook-Torrance 
BRDF  |
|  - Fast (UI/Particle)  |  - Low Mobile ALU Cost      |  - High Texture/ALU 
Cost|
+------------------------------------------------------------------------------
-+
```

* **Unlit Shaders**: Ignores light sources entirely; samples color or texture 
maps directly. Lowest possible ALU cost. Used for UI, skyboxes, and particle 
cards.
* **Simple Lit Shaders**: Calculates empirical Blinn-Phong diffuse and specular
highlights ($\mathbf{N} \cdot \mathbf{L}$ and $\mathbf{N} \cdot 
\mathbf{H}$). Approximates lighting at low mathematical cost, ideal for 
mobile AR assets.
* **Complex Lit (PBR - Physically Based Rendering)**: Implements 
energy-conserving Bidirectional Reflectance Distribution Functions (BRDF), such
as Cook-Torrance:

\

Where $D$ is microfacet distribution (GGX), $F$ is Fresnel reflection, 
and $G$ is geometric shadowing. Requires texture maps for Albedo, 
Metallic/Smoothness, Normal, and Ambient Occlusion. High ALU and memory 
bandwidth consumption requires strict ASTC texture compression.

### Lighting Techniques for XR
1. **Realtime Lights**: Calculates per-pixel lighting every frame. Extremely 
resource-intensive; dynamic shadow maps require additional rendering passes per
light source. Mobile XR projects typically limit realtime lighting to a single 
directional light without dynamic shadows.
2. **Baked Lightmaps**: Precomputes direct lighting, indirect bounce, and soft 
ambient occlusion into high-dynamic-range (HDR) lightmap textures during editor
offline baking. Runtime cost is reduced to a single texture lookup, enabling 
realistic global illumination on mobile hardware.
3. **Light Probes**: A 3D grid of sampling points storing precomputed ambient 
and bounced irradiance as Spherical Harmonics (SH) polynomials. Dynamic objects
sample nearby light probes to receive ambient light matching static baked 
environments without runtime shadow passes.
4. **Reflection Probes**: Captures a $360^\circ$ cubemap of surrounding 
static geometry to generate radiance maps for specular PBR reflections on shiny
or metallic surfaces.

### Hardware Performance Trade-offs
* **GPU Fill-Rate Bottlenecks**: Caused by rendering dual high-resolution 
buffers ($2\text{K} \times 2\text{K}$ per eye at $90\text{ FPS}$) 
combined with overdraw from transparent alpha-blended objects.
* **Draw Call Overhead**: Submitting draw calls places heavy CPU overhead on 
the main thread. Mitigated via Static Batching, GPU Instancing, and SRP 
Batcher.
* **Battery and Thermal Throttling**: System on Chip (SoC) platforms operate 
under tight passive thermal limits. High CPU/GPU utilization triggers automatic
frequency downclocking, leading to dropped frames, visual stuttering, and 
severe motion sickness.

---

## 3. Platform Considerations & Standalone Applications

Architecture choices dictate target performance constraints, build outputs, and
hardware feature access.

### Standalone Mobile VR vs. PCVR Tethered

```
+------------------------------------------------------------------------------
-----------+
| CHARACTERISTIC          | STANDALONE MOBILE VR (Meta Quest) | PCVR TETHERED 
(Rift/Vive) |
+-------------------------+-----------------------------------+----------------
-----------+
| Operating System        | Android (Linux Kernel, ARM64)     | Windows 
(x86_64)          |
| Build Output            | Android Package (`.apk` / `.aab`)  | Windows 
Executable (`.exe`)|
| Compute & Power Limits  | Passive Mobile SoC (Snapdragon)   | Dedicated 
Active Desktop  |
| Target Frame Rate       | 72 / 90 / 120 FPS (Strict)        | 90 / 120 / 144 
FPS        |
| Draw Call Budget        | < 100 - 150 per frame             | > 1000 - 2000 
per frame   |
| Polygon Count Budget    | 500,000 - 1,000,000 tris          | 3,000,000+ tris
|
| Memory Architecture     | Unified LPDDR (Shared CPU/GPU)    | Discrete VRAM 
(GDDR6)     |
+------------------------------------------------------------------------------
-----------+
```

### Mobile AR: Android (ARCore) vs. iOS (ARKit)
* **Android AR (ARCore APK)**: Deployed across fragmented third-party hardware.
Uses Visual-Inertial Odometry (VIO), feature point detection, plane 
identification, and ambient light estimation. Requires Android API Level 24+ 
and Google Play Services for AR.
* **iOS AR (ARKit IPA)**: Deployed via Xcode to uniform Apple hardware. 
Integrates deeply with A-series/M-series Apple Silicon and hardware LiDAR 
sensors, enabling instant scene mesh generation, precise occlusion, and 
sub-millimeter tracking stability.

---

## 4. App Store Submission & Distribution

Distributing commercial XR applications requires adherence to strict platform 
technical checks (VRCs), policy guidelines, and user safety standards.

### Meta Quest Store vs. App Lab Requirements
* **Meta Quest Store**: Highly curated commercial storefront requiring 
conceptual approval via a formal proposal before developer onboarding.
* **App Lab**: Direct-distribution portal with no conceptual curation, but 
enforcing identical **Virtual Reality Checks (VRCs)**:
  * **VRC-QUEST-PERF-1**: Application must maintain a stable target frame rate 
($72\text{ FPS}$, $90\text{ FPS}$, or $120\text{ FPS}$) with 
$0\%$ persistent frame drops or stuttering.
  * **VRC-QUEST-TRACKING-1**: Full $6\text{DoF}$ tracking support; 
application must handle tracking loss gracefully without freezing the visual 
display.
  * **VRC-QUEST-PAUSE-2**: Application must respond immediately to system 
overlay triggers (e.g., Meta menu button) by pausing audio and gameplay.
  * **VRC-QUEST-GUARDIAN-1**: Must integrate with Guardian boundary alerts and 
suppress visual rendering if the user steps outside the safe boundary.

### Google Play Console AR Requirements
* **AR Required**: App manifest flags `<uses-feature 
android:name="com.google.ar.core" android:required="true" />`. App is hidden in
Google Play Store for non-ARCore certified devices.
* **AR Optional**: Feature flag set to `false`. Non-AR devices can download the
app, but AR modes are conditionally disabled at runtime.

### Comfort Rating Classifications
Platforms categorize applications based on motion characteristics to inform 
users of potential cybersickness risks:

```
+------------------------------------------------------------------------------
------+
| COMFORT RATING | LOCOMOTION & MOTION CHARACTERISTICS                         
|
+----------------+-------------------------------------------------------------
------+
| Comfortable    | Static camera position; instant teleportation; no camera 
movement. |
| Moderate       | Slow continuous glide; snap turns; restricted FOV 
vignetting.     |
| Intense        | Rapid artificial movement; smooth turns; flight or 
acceleration.  |
+----------------+-------------------------------------------------------------
------+
```

---

## 5. Profiling and Performance Testing

Systematic performance profiling is mandatory for maintaining the high frame 
rates required in spatial computing.

### OVR Metrics Tool (On-Device HUD Display)
An on-device diagnostic application for Meta Quest headsets that renders a 
real-time performance overlay over running VR applications:
* **FPS / Frame Time**: Real-time frame rate display and frame completion time 
in milliseconds ($\le 13.88\text{ ms}$ for $72\text{ FPS}$).
* **CPU / GPU Utilization & Clocks**: Shows current processor frequency levels 
($0$ to $4$) and capacity usage percentages.
* **Stale / Tear Count**: Tracks dropped frames where the GPU failed to 
complete rendering before the display scan-out, triggering Asynchronous 
TimeWarp (ATW).
* **Thermal Level**: Reports SoC junction temperature and thermal throttling 
states.

### Unity Profiler Analysis
Connects remotely to a development build running on the target device via ADB 
(Android Debug Bridge):
* **CPU Usage Module**: Distinguishes between `Main Thread` execution (game 
logic, physics, script updates) and `Render Thread` queue preparation.
* **GC Alloc (Garbage Collection Allocation)**: Identifies per-frame heap 
allocation spikes (`GC.Alloc`). Any value above $0\text{ Bytes/frame}$ 
during gameplay causes periodic runtime Garbage Collection stalls, creating 
severe visual drops.

```
FRAME BUDGET TIMELINE (72 FPS Target = 13.88 ms Total):
|--- Main Thread (Scripts/Physics): ~5 ms ---|--- Render Thread (Commands): ~4 
ms ---|
                                             |--- GPU Rasterization/Shading: < 
13.88 ms ---|
```

### Frame Debugger and Draw Calls
* **Frame Debugger**: Pauses rendering on a specific frame and allows 
developers to step through individual draw calls sequentially.
* **Draw Call Breakdown**: Reveals state changes, material swaps, unbatched 
meshes, and redundant shadow passes. Helps optimize Static Batching, Dynamic 
Batching, GPU Instancing, and SRP Batcher efficiency.
* **Memory Bandwidth**: Monitored by inspecting texture resolution, mipmap 
enablement, and ASTC compression blocks ($4\times4$ or $6\times6$) to 
prevent bus saturation.

---

## 6. User Comfort and Safety Guidelines

Designing for spatial technology requires understanding human perceptual 
physiology to minimize physical discomfort.

### Cybersickness and Vection Mitigation
* **Cybersickness**: Motion sickness induced by spatial computing applications.
Caused by **Vestibular-Ocular Mismatch**—a sensory conflict where the visual 
system perceives self-motion while the vestibular system (inner ear) detects a 
stationary body.
* **Vection**: The illusion of self-motion induced by moving visual fields in 
peripheral vision.
* **Mitigation Strategies**:
  1. Eliminate artificial acceleration curves; move at constant velocities.
  2. Maintain fixed visual reference frames (e.g., virtual cockpits, static UI 
dashboards).
  3. Avoid forced camera rotations, head bobbing, or camera shaking.

### Field-of-View (FOV) Vignetting (Tunneling)
Dynamically constrains the visual peripheral field during artificial locomotion
or rotation by applying a dark circular mask around the camera view. This 
suppresses peripheral optic flow, mitigating vection while preserving central 
focal awareness.

```
FOV VIGNETTING / TUNNELING DURING MOTION:
+---------------------------------------+
|  ///// DARK VIGNETTE MASK /////       |
|  /////// +-----------------+ //////// |
|  //////  | Visible Central |  /////// |
|  //////  |   Focal View    |  /////// |
|  /////// +-----------------+ //////// |
|  ///// DARK VIGNETTE MASK /////       |
+---------------------------------------+
```

### Snap Turning vs. Smooth Turning
* **Snap Turning**: Rotates the camera instantly in discrete angular jumps 
(e.g., $30^\circ$, $45^\circ$, or $90^\circ$). Because the rotation
occurs instantly within a single frame, visual optic flow across the retina is 
eliminated, preventing vestibular conflict.
* **Smooth Turning**: Rotates the camera continuously over time. Generates 
continuous rotational optic flow, making FOV vignetting mandatory to prevent 
motion sickness.

### Guardian Boundaries and Ergonomic Pacing
* **Guardian Boundary Integration**: Interfacing with the Meta XR SDK boundary 
system (`OVRBoundary`) allows applications to query the physical room-scale 
bounds. Applications must pause or fade to passthrough when the user nears 
physical obstacles.
* **Ergonomic Session Pacing**: Designing interaction loops suited for 
$15\text{--}30$ minute play sessions. Virtual UIs must be positioned at 
comfortable focal depths ($1.5\text{--}2.0\text{ meters}$) to prevent 
Vergence-Accommodation Conflict (VAC).

---

## 7. Exam Questions & Model Answers

### Question 3(b) [10 Marks]
**Explain how Lighting, Shaders, and Materials contribute to realism in VR. 
Discuss performance trade-offs.**

#### Model Answer:

##### 1. Lighting Techniques [4 Marks]
Lighting establishes depth cues, volumetric structure, and spatial immersion in
VR environments:
* **Baked Lightmaps**: High-dynamic-range global illumination (direct light, 
indirect bounces, and soft ambient occlusion) is precalculated during offline 
development and stored in lightmap textures. At runtime, static geometry 
samples these lightmaps with zero lighting calculation overhead, enabling 
photorealistic static scenes on mobile VR hardware.
* **Light Probes**: Dynamic assets cannot utilize static lightmaps. A 3D grid 
of Light Probes samples the baked ambient light environment using Spherical 
Harmonics (SH) coefficients. Moving objects interpolate lighting from adjacent 
probes, receiving realistic directional ambient light without computing 
real-time shadows.
* **Reflection Probes**: Captures environment cubemaps to supply radiance data 
for metallic and reflective surfaces. Essential for accurate specular 
highlights on materials like glass and metal.

##### 2. Shader and Material Roles [3 Marks]
* **Physically Based Rendering (PBR)**: Materials utilize energy-conserving 
BRDF equations, relying on Albedo, Metallic, Smoothness, and Normal maps. PBR 
ensures materials react predictably under varying light conditions.
* **URP Shaders**: Unity’s Universal Render Pipeline offers optimized shader 
variants: *Unlit* (zero lighting cost for UI/particles), *Simple Lit* (low-cost
Blinn-Phong diffuse/specular), and *Complex Lit* (full PBR). In VR, choosing 
the lowest acceptable shader complexity directly preserves frame headroom.
* **Texture Compression**: Mobile VR GPUs consume significant memory bandwidth 
reading high-resolution PBR textures. Applying **ASTC (Adaptive Scalable 
Texture Compression)** reduces texture VRAM footprint, preventing bus 
saturation without visible quality loss.

##### 3. Performance Trade-offs [3 Marks]
* **GPU Fill-Rate Limits**: VR requires rendering dual high-resolution displays
($90\text{+ FPS}$). Complex pixel shaders and alpha overdraw saturate the 
GPU fill-rate, leading to dropped frames.
* **Draw Call Overhead**: Each material and light pass submits CPU draw calls. 
Excessive draw calls bottleneck the Main Thread, requiring Static Batching, GPU
Instancing, and SRP Batcher.
* **Thermal Constraints**: Untethered mobile SoCs (e.g., Snapdragon XR2) 
operate under passive cooling limits. Unoptimized lighting and shaders cause 
thermal throttling, forcing the system to drop CPU/GPU clock frequencies and 
triggering severe frame drops.

---

### Question 7 [20 Marks]
**Describe the deployment process of a VR application using Unity and Meta 
Quest. Explain build targets, device profiling, testing, and user safety 
optimization.**

#### Model Answer:

##### Component 1: Build Target Configuration and Android Export [6 Marks]
Deploying a VR application to Meta Quest requires configuring Unity's build 
system for the target Android ARM64 architecture:

1. **Unity Build Settings**:
   * Open `File | Build Settings`, select **Android** as the target platform, 
and click **Switch Platform**.
   * Set **Texture Compression** to **ASTC**.
2. **Player Settings Identification & Configuration**:
   * **Minimum API Level**: Set to `Android 10.0 (API Level 29)` or higher.
   * **Scripting Backend**: Switch from Mono to **IL2CPP** (Intermediate 
Language to C++). IL2CPP converts C# byte code into native C++ prior to 
compilation, increasing execution speed.
   * **Target Architectures**: Enable **ARM64** exclusively; disable ARMv7 
(32-bit is unsupported on modern Quest runtimes).
3. **Graphics API Configuration**:
   * In Graphics APIs, remove OpenGL ES3 and add **Vulkan**. Vulkan reduces CPU
driver overhead and provides better multi-threading for draw calls.
4. **XR Plugin Management & Meta XR SDK**:
   * Install `XR Plugin Management` via the Package Manager. Under the Android 
tab, check **Meta Quest** / **OpenXR**.
   * Set **Stereo Rendering Mode** to **Single Pass Instanced**. This packs 
left and right eye rendering into a single draw call pass, reducing CPU draw 
call overhead by $50\%$.

##### Component 2: Device Profiling and Performance Testing [6 Marks]
Ensuring the application maintains a stable $72\text{ / }90\text{ FPS}$ 
target budget ($\le 13.88\text{ ms}$ or $11.11\text{ ms}$ per frame) 
requires on-device profiling:

1. **OVR Metrics Tool**:
   * Install and launch the OVR Metrics Tool on the Quest headset to enable an 
on-screen performance HUD overlay during gameplay.
   * Monitor real-time **FPS**, **App Frame Time**, **GPU Utilization %**, 
**CPU Utilization %**, **Stale Frame Count**, and **Thermal Level**.
   * Identify frame drops caused by GPU saturation or CPU spikes.
2. **Unity Profiler Integration**:
   * Connect the Quest headset via USB/ADB, enable `Development Build` and 
`Autoconnect Profiler` in Unity Build Settings, and execute the app.
   * Analyze the **CPU Usage Module** to ensure `Main Thread` execution remains
under budget.
   * Inspect **GC Alloc (Garbage Collection Allocation)** per frame. Developers
must enforce $0\text{ Bytes/frame}$ of dynamic heap allocation during 
gameplay loops (e.g., pre-allocating memory, using Object Pools) to prevent 
Garbage Collection stalls.
3. **Thermal Throttling Analysis**:
   * Observe CPU/GPU clock levels ($0\text{--}4$). If clock levels drop 
automatically during runtime due to rising junction temperatures, developers 
must reduce draw calls, lower shader complexity, or adjust Fixed Foveated 
Rendering (FFR) levels.

##### Component 3: User Comfort and Safety Guidelines [8 Marks]
Spatial computing safety requires physiological comfort optimizations to 
prevent cybersickness and physical injury:

1. **FOV Vignetting (Tunneling) During Motion**:
   * Implement FOV vignetting during continuous locomotion or smooth turns. 
Darkening the peripheral vision during movement reduces peripheral optic flow, 
mitigating vection and preventing vestibular-ocular conflict.
2. **Guardian Boundary Integration**:
   * Integrate the Meta XR Boundary API (`OVRBoundary`). Query physical 
boundary distance during room-scale gameplay.
   * Automatically pause gameplay, mute spatial audio, or fade the display to 
the Passthrough camera feed if the user approaches or crosses physical safe 
limits.
3. **Ergonomic Session Pacing & Focal Distance**:
   * Design interaction sequences around $15\text{--}30$ minute play 
sessions to prevent visual fatigue.
   * Position spatial UI elements at comfortable focal distances 
($1.5\text{--}2.0\text{ meters}$) with zero stereoscopic parallax conflict 
to avoid Vergence-Accommodation Conflict (VAC).
4. **Safety Disclaimers & Health Warnings**:
   * Display a clear boot screen prompting the user to clear their physical 
environment, confirm their Guardian bounds, and take immediate breaks if 
experiencing disorientation or nausea.
