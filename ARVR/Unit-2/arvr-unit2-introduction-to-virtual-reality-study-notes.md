# Comprehensive Study Notes — Unit 2: Introduction to Virtual Reality (VR)

**Course Code**: NMIMS ARVR (702COI002 / 702MH0I004)  
**Program**: B. Tech / MBA Tech (Computer Engineering, AI & ML, Data Science)  
**Department**: Mukesh Patel School of Technology Management & Engineering  

---

## 1. Definition, Scope, and the 3 I's of Virtual Reality

### 1.1 Academic Definition & Historical Genesis
The term **Virtual Reality (VR)** was formally coined in **1987 by Jaron 
Lanier**, founder of VPL Research, who pioneered early commercial HMDs 
(DataGlove and EyePhone).

In academic and engineering literature, Virtual Reality is defined as a 
computer-generated, interactive, 3D stereoscopic environment that completely 
surrounds and isolates the user from the physical world. By feeding 
synchronized sensory stimuli (visual, auditory, and haptic) in real time, the 
system replaces physical sensory inputs with synthetic ones, creating the 
perception of digitally teleporting the user into an artificial realm.

```
+-----------------------------------------------------------------------+
|                       PHYSICAL REALITY ISOLATION                      |
|                                                                       |
|  +------------------+     Display/Audio     +----------------------+  |
|  |   Human User     | <------------------- |  Computing Engine    |  |
|  | (Sensory Organs) | -------------------> | (Unity / Render GPU) |  |
|  +------------------+   Tracking / Input   +----------------------+  |
+-----------------------------------------------------------------------+
```

### 1.2 Engineering Scope & Applications
Virtual Reality extends beyond entertainment into critical engineering, 
medical, and enterprise domains:
*   **Aerospace & Flight Simulation**: High-fidelity flight simulators and 
pilot training systems where real-world risks or financial costs are 
prohibitive.
*   **Medical & Tele-Surgery**: Pre-operative surgical planning, organ 
simulation, and remote robotic tele-surgery training without patient risk.
*   **Automotive & Industrial Design**: Collaborative 3D digital twin 
prototyping and factory assembly line simulation (e.g., Mercedes-Benz 
production layout optimization).
*   **Architecture & Civil Engineering**: Spatial walk-throughs of structural 
models (BIM integration) prior to physical construction.

### 1.3 The 3 I's Framework of Virtual Reality (Burdea & Coiffet)
Virtual Reality is functionally modeled around the **3 I's Framework**, defined
by Grigore Burdea and Philippe Coiffet:

```
                      [ IMMERSION ]
                     /             \
                    /               \
                   /                 \
                  /                   \
        [ INTERACTION ] ----------- [ IMAGINATION ]
```

1.  **Immersion (Sensory Component)**: The technological capability of the 
hardware system to isolate the user's natural senses and replace them with 
high-fidelity computer-generated inputs (stereoscopic visual displays, spatial 
audio, and haptic feedback).
2.  **Interaction (Control Component)**: The real-time bidirectional 
responsiveness between the user and the virtual world. When a user turns their 
head, moves their hands, or manipulates a virtual tool, the system updates the 
rendered viewpoint and physics states deterministically without perceptible 
delay.
3.  **Imagination (Cognitive Component)**: The human mind's capacity to 
perceive the synthetic environment as a living reality, conceptualize 
non-existent worlds, and form emotional, intuitive connections with the virtual
simulation.

---

## 2. Taxonomy & Types of Virtual Reality

Virtual Reality environments are categorized based on their level of sensory 
isolation, interaction models, and delivery platforms.

```
+------------------------------------------------------------------------------
-----+
|                                  TYPES OF VR                                 
|
+-------------------+--------------------+-------------------+-----------------
-----+
|  Non-Immersive    |   Semi-Immersive   |  Fully Immersive  | Cinematic / 
WebVR    |
|  - Monitor / PC   |   - Flight Sim     |  - HMD / CAVE     | - 360 Video 
(3DoF)   |
|  - Mouse / Key    |   - Curved Screen  |  - 6DoF Motion    | - WebXR Browser 
|
+-------------------+--------------------+-------------------+-----------------
-----+
```

### 2.1 Non-Immersive VR
*   **Architecture**: Renders a 3D environment on a standard 2D desktop monitor
or television display.
*   **Control Mechanism**: Uses conventional desktop peripherals (keyboard, 
mouse, or gamepad joystick).
*   **Sensory Isolation**: Zero physical isolation; the user remains fully 
aware of their physical surroundings.
*   **Examples**: PC flight simulators, CAD architectural 3D walk-throughs, and
3D video games.

### 2.2 Semi-Immersive VR
*   **Architecture**: Combines high-end 3D graphics with large-scale physical 
displays, such as concave projection screens, dome displays, or multi-monitor 
setups.
*   **Control Mechanism**: Dedicated physical control rigs (such as replica 
flight control sticks, pedals, and physical cockpit seats).
*   **Sensory Isolation**: Partial visual immersion; surrounds the user's 
forward field of view while allowing peripheral vision of real-world physical 
controls without requiring a head-mounted display.
*   **Examples**: Commercial aviation flight simulators and IMAX 3D theaters.

### 2.3 Fully Immersive VR
*   **Architecture**: Achieves complete sensory replacement using closed 
Head-Mounted Displays (HMDs), noise-isolating spatial audio headphones, and 
spatial tracking sensors, or CAVE (Cave Automatic Virtual Environment) system 
rooms with stereoscopic rear-projection walls and floor.
*   **Control Mechanism**: 6DoF motion-tracked controllers, data gloves, or 
optical hand-tracking pipelines.
*   **Sensory Isolation**: Complete visual and auditory isolation from the 
physical environment.
*   **Examples**: Meta Quest 3, HTC Vive Pro, and multi-projection CAVE 
laboratories.

### 2.4 Cinematic VR: POV vs. 360-Degree Spherical Media
Cinematic VR captures real-world video using omnidirectional camera rigs:
*   **Point-of-View (POV) Cinematic VR**: Places the camera rig at the eye 
level of a specific actor or driver, capturing a fixed perspective (typically 
180-degree FOV) to simulate living through an individual's personal vantage 
point.
*   **360-Degree Spherical Media**: Uses a multi-lens camera array located at 
the center of a scene to stitch a full 360-degree by 180-degree spherical video
projection. The user can look in any direction (3DoF rotational tracking), but 
cannot translate physically in space (0DoF positional movement).

### 2.5 Interactive VR
Interactive VR provides true user agency. Unlike passive cinematic media, the 
user can navigate freely, trigger physical events, pick up virtual objects via 
collision detection and rigidbodies, and influence the narrative or simulation 
state.

### 2.6 WebVR / WebXR Frameworks
WebVR (now standardized as **WebXR Device API**) enables immersive 3D 
experiences delivered directly through web browsers without requiring 
application installation via app stores.
*   **A-Frame**: An open-source, declarative HTML Entity-Component-System (ECS)
framework built on top of Three.js and WebGL.
*   **Technical Advantage**: Cross-platform portability across mobile devices, 
desktop browsers, and standalone HMDs.

```
+────────────────────────────────────────────────────────────────────────────+
|                    WEBXR SCENE ENTITY-COMPONENT ARCHITECTURE               |
+────────────────────────────────────────────────────────────────────────────+

  [ <a-scene> Root Engine Context ]
         │
         ├─► [ Camera Rig Node ]: Positional Tracking + Stereoscopic Eye Sinks
         ├─► [ Light Entities ]: Directional Photon Emitter + Ambient Illumination
         ├─► [ Spatial Entities ]:
         │     • 3D Geometric Primitives: Mesh Geometry (Box, Sphere, Cylinder)
         │     • PBR Material Components: Diffuse Color, Roughness, Normal Mapping
         │     • World Transform Matrices: Cartesian Position (X,Y,Z), Rotation (Roll,Pitch,Yaw)
         └─► [ Environment Skybox ]: 360-degree Equirectangular Panoramic Backdrop
```

---

## 3. Immersion vs. Presence (Mel Slater's Dual-Illusion Theory)

Understanding the distinction between technical system capabilities and human 
psychological perception is essential for VR engineering.

### 3.1 Technical Distinction Matrix

| Feature | Immersion (System Property) | Presence (Psychological Property) |
| :--- | :--- | :--- |
| **Definition** | Objective measurement of sensory fidelity supplied by hardware. | Subjective mental sensation of "being physically present" in the virtual space. |
| **Domain** | Hardware, rendering engine, display physics, sensor latency. | Cognitive psychology, perceptual neuroscience, human factors. |
| **Quantification** | Measurable metrics (e.g., 2160x2160 per eye, 90 Hz, <20ms latency, 110° FOV). | Evaluated via qualitative questionnaires (e.g., Witmer-Singer scale) or biometrics. |
| **Modifiability** | Upgrading hardware components directly increases immersion. | Cannot be guaranteed solely by hardware; depends on narrative and interaction design. |

### 3.2 Mel Slater's Dual Illusion Theory (2009)
Professor Mel Slater established that **Presence** in Virtual Reality is 
composed of two independent mental illusions:

```
                                +---------------------------+
                                |  PSYCHOLOGICAL PRESENCE   |
                                +-------------+-------------+
                                              |
                      +-----------------------+-----------------------+
                      |                                               |
        +-------------v-------------+                   
+-------------v-------------+
        |   PLACE ILLUSION (PI)     |                   | PLAUSIBILITY ILLUSION
(Psi)|
        | Sensorimotor Contingencies|                   |  Coherence & Realism 
|
        |  "I am physically here"   |                   |  "This is actually 
happening"
        +---------------------------+                   
+---------------------------+
```

1.  **Place Illusion (PI)**:
    *   **Concept**: The visceral, subconscious sensation of being in the 
virtual room/space, despite consciously knowing you are wearing a headset in a 
physical room.
    *   **Enabling Factor**: Driven by **Sensorimotor Contingencies (SC)**—the 
motor actions used to perceive the world (turning the head, leaning forward, 
looking under objects) produce immediate, accurate updates to visual and 
auditory displays.
2.  **Plausibility Illusion (Psi)**:
    *   **Concept**: The cognitive belief that the events, interactions, and 
situations occurring in the virtual world are actually taking place.
    *   **Enabling Factor**: Driven by **Environmental Coherence**—the virtual 
world responds logically and dynamically to user actions, virtual characters 
exhibit believable social reactions, and physical laws (gravity, collision) 
behave consistently.

---

## 4. Key VR Hardware Architecture & Tracking Subsystems

```
+------------------------------------------------------------------------------
-----+
|                             VR HARDWARE ARCHITECTURE                         
|
+-----------------------+-----------------------+------------------------------
-----+
|     Display Engine    |   Tracking Subsystem  |       Input / Haptic Engine  
|
|  - OLED / LCD Panels  |  - 3DoF vs 6DoF IMU   |  - 6DoF Controllers 
(Triggers)    |
|  - Fresnel / Pancake  |  - Inside-Out / Out-In|  - Capacitive Touch / LRAs   
|
+-----------------------+-----------------------+------------------------------
-----+
```

### 4.1 Displays and Optical Enclosures
*   **OLED (Organic Light Emitting Diode)**: Emits light per subpixel, 
providing true black levels, infinite contrast ratios, and low-persistence 
emission that eliminates motion blur.
*   **LCD (Liquid Crystal Display)**: Employs fast-switch panels with high 
subpixel density (RGB stripe matrix) to minimize the **Screen-Door Effect 
(SDE)**—the visible black grid between pixels.
*   **Optical Lens Systems**:
    *   **Fresnel Lenses**: Uses concentric optical ridges to bend light, 
reducing lens thickness and weight. Prone to optical glare ("god rays") in 
high-contrast scenes.
    *   **Pancake Optics**: Uses folded optical paths with polarizers and 
beam-splitters. Drastically reduces the distance required between the display 
panel and the lens, yielding thin, light headsets with edge-to-edge optical 
clarity.

```
FRESNEL LENS (Ridge Bending)               PANCAKE OPTICS (Folded Light Path)
  \  |  /  (Concentric Ridges)               Display Panel
   \ | /                                        ||
  [=======]  Thick Profile                      ||  Polarizer
   / | \                                        |/  Beam Splitter / Folded Path
  /  |  \                                       ||  Compact Profile
```

### 4.2 Tracking Paradigms: 3DoF vs. 6DoF
*   **3DoF (Three Degrees of Freedom)**: Measures **rotational motion only** 
along three orthogonal axes:
    *   *Pitch* (Rotation around X-axis / looking up and down).
    *   *Yaw* (Rotation around Y-axis / looking left and right).
    *   *Roll* (Rotation around Z-axis / tilting head side to side).
*   **6DoF (Six Degrees of Freedom)**: Measures **rotational motion (Pitch, 
Yaw, Roll)** PLUS **translational motion** along three positional axes:
    *   *X-axis (Sway)*: Moving left and right.
    *   *Y-axis (Heave)*: Moving up and down (crouching/jumping).
    *   *Z-axis (Surge)*: Moving forward and backward.

```
                 Y (Yaw / Heave)
                   ^
                   |  
                   |   / Z (Roll / Surge)
                   |  /
                   | /
  X (Pitch / Sway) +---------------->
```

### 4.3 Inertial Measurement Units (IMUs)
An **IMU** is an integrated micro-electro-mechanical system (MEMS) chip 
combining:
1.  **Tri-axial Accelerometer**: Measures linear acceleration along X, Y, Z 
axes.
2.  **Tri-axial Gyroscope**: Measures angular velocity along X, Y, Z axes.
3.  **Tri-axial Magnetometer**: Measures magnetic north to correct heading 
drift.

*IMU Limitation*: Integrating raw acceleration twice to compute position causes
exponential integration drift. Therefore, IMUs must be combined with optical 
tracking.

### 4.4 Inside-Out vs. Outside-In Positional Tracking

```
INSIDE-OUT TRACKING                        OUTSIDE-IN TRACKING
+--------------------+                     +--------------------+
| Headset Cameras    | ----> Sees Room     | External Sensors   | ----> Tracks
| (VIO / SLAM)       |       Landmarks     | (Lighthouse/Lighth)|       Headset
LEDs
+--------------------+                     +--------------------+
  - No External Hardware                     - Sub-millimeter Accuracy
  - Self-Contained Space                     - Occlusion Vulnerable
```

*   **Inside-Out Tracking**: Cameras mounted directly on the HMD observe the 
physical environment. Algorithms run **Visual Inertial Odometry (VIO)** and 
**SLAM (Simultaneous Localization and Mapping)** to identify spatial feature 
points and compute headset pose without external room hardware (e.g., Meta 
Quest 3).
*   **Outside-In Tracking**: External stationary sensors or laser emitters 
placed around the room track passive or active markers mounted on the headset 
and controllers (e.g., SteamVR Lighthouse laser sweep emitters, Oculus Rift CV1
infrared cameras).

### 4.5 6DoF Motion Controllers
Modern VR controllers utilize capacitive finger sensors (detecting thumb, 
index, and middle finger resting states), analog thumbsticks, dual-stage index 
triggers, grip triggers, and Linear Resonant Actuators (LRA) for localized 
haptic force feedback.

---

## 5. Real-Time VR Performance Challenges & System Limitations

Operating a real-time VR system demands strict hardware and software 
performance bounds.

```
+------------------------------------------------------------------------------
-----+
|                            REAL-TIME VR CHALLENGES                           
|
+------------------+------------------+------------------+---------------------
-----+
| Motion-to-Photon | Frame Rate Target| Cybersickness    | Rendering Load      
|
| Latency (< 20ms) | (72 / 90 / 120Hz)| Visuomotor Mismatch| Dual Stereo Draw 
Calls   |
+------------------+------------------+------------------+---------------------
-----+
```

### 5.1 Motion-to-Photon Latency
**Motion-to-Photon Latency** is the total time elapsed between the user 
physically moving their head/body and the updated visual image being drawn on 
the HMD screen.
*   **Critical Threshold**: Must be strictly **less than 20 milliseconds (< 
20ms)** (Carmack Limit).
*   **Latency Breakdown**: Total time includes sensor sampling delay, 
transmission time, game logic loop, GPU rendering pipeline, and display 
scanout.
*   **Impact of High Latency**: Causes visual lag, "image swimming," 
misregistration, and severe simulator sickness.

### 5.2 Frame Rate Requirements
To maintain visual stability and prevent motion sickness, VR systems target 
steady frame rates:
*   **Minimum Target**: 72 FPS / 72 Hz (Meta Quest entry baseline).
*   **Standard Target**: 90 FPS / 90 Hz (PC VR / High-end standalone baseline).
*   **High Performance Target**: 120 FPS / 120 Hz.
*   *Constraint*: Dropping below target frame rates introduces judder 
(stuttering frames), breaking immersion instantly.

### 5.3 Cybersickness (Simulator Sickness)
Cybersickness occurs due to **Sensory Conflict Theory**: a mismatch between the
visual system (which perceives movement in the virtual environment) and the 
vestibular system in the inner ear (which senses that the physical body is 
stationary).
*   *Symptoms*: Nausea, disorientation, dizziness, eyestrain, and cold 
sweating.
*   *Mitigation*: Maintain high frame rates, eliminate uncommanded camera 
acceleration, use teleportation locomotion, and apply dynamic Field of View 
(FOV) vignetting during motion.

### 5.4 Tracking Accuracy and Spatial Drift
Cumulative sensor error in IMU integration causes **positional drift**. Without
optical calibration from SLAM/VIO cameras, the virtual world slowly drifts or 
rotates away from physical reality.

### 5.5 Rendering Load and Draw Call Bottlenecks
Stereoscopic rendering requires drawing the scene twice every frame—once for 
the left eye camera and once for the right eye camera:
*   **Double Draw Calls**: Traditional rendering pipelines issue duplicate draw
calls to the GPU, creating CPU performance bottlenecks.
*   **Resolution Load**: Rendering dual high-resolution displays (e.g., 2064 x 
2208 pixels per eye) at 90 FPS requires processing over 800 million pixels per 
second.

---

## 6. Exam Questions & Model Answers (NMIMS Exam Pattern)

---

### Question 1(a) [5 Marks]
**Prompt**: Define Virtual Reality and explain one engineering application of 
Virtual Reality.  
*(Marking Scheme: VR Definition = 1 Mark; Engineering Application = 1.5 Marks; 
AR Definition = 1 Mark; AR Application = 1.5 Marks)*

#### Model Answer:

**Virtual Reality (VR) Definition**:
Virtual Reality is a computer-generated 3D environment that completely 
surrounds, isolates, and immerses the user from physical reality. Utilizing a 
stereoscopic Head-Mounted Display (HMD), spatial audio, and motion tracking, VR
replaces physical sensory inputs with synthetic stimuli in real time, enabling 
interactive exploration of artificial worlds.

**Engineering Application of VR (Industrial Manufacturing & Digital Twins)**:
Automotive enterprises like Mercedes-Benz use VR to construct full-scale 3D 
digital twins of vehicle assembly lines. Automotive engineers wear 6DoF HMDs to
evaluate human ergonomics, assembly clearance, and robotic arm pathing prior to
building physical manufacturing plant infrastructure. This eliminates physical 
prototyping costs and accelerates design iterations.

**Augmented Reality (AR) Definition**:
Augmented Reality is an interactive experience that overlays computer-generated
3D graphics, text, or perceptual data directly onto the user's real-world 
physical environment in real time, maintaining a continuous visual connection 
to physical reality.

**Engineering Application of AR (Aerospace Maintenance Assistance)**:
Boeing utilizes AR headsets (e.g., Microsoft HoloLens) in aircraft wiring 
assembly. Interactive 3D schematic overlays are projected directly onto real 
aircraft frames, guiding technicians through complex wiring harnesses 
hands-free, reducing assembly errors and installation times.

---

### Question 1(d) [5 Marks]
**Prompt**: List and describe any four challenges in achieving real-time 
performance in Virtual Reality applications.  
*(Marking Scheme: 1 Mark for each valid challenge clearly described)*

#### Model Answer:

1.  **Motion-to-Photon Latency Constraint (< 20ms)**:
    The system delay between physical head movement and updated pixel display 
must remain strictly under 20ms. If processing or rendering delays exceed 20ms,
visual lag causes "image swimming," spatial registration errors, and severe 
motion sickness.
2.  **High Frame Rate Maintenance (72 / 90 / 120 FPS)**:
    VR rendering engines must generate a stable minimum frame rate of 72 to 90 
frames per second. Dropping below this baseline causes visual judder (dropped 
frames), leading to eyestrain and immediate loss of user presence.
3.  **Stereoscopic Rendering Load & CPU Draw Calls**:
    VR requires rendering the 3D scene twice per frame—once from the left eye 
camera and once from the right eye camera. This doubles geometry passes and CPU
draw call overhead, creating GPU bottlenecks on mobile standalone processors.
4.  **Tracking Accuracy & Cumulative Sensor Drift**:
    Real-time pose estimation using IMUs suffers from mathematical integration 
drift over time. Suppressing positional drift requires real-time optical 
tracking (SLAM/VIO) running concurrently, consuming processing overhead.

---

### Question 2 [10 Marks]
**Prompt**: Differentiate between Immersion and Presence. Explain the key 
hardware architecture differences between 3DoF and 6DoF tracking systems.  
*(Marking Scheme: Immersion vs Presence Comparison = 5 Marks; 3DoF vs 6DoF 
Hardware Architecture = 5 Marks)*

#### Model Answer:

#### Part A: Immersion vs. Presence (5 Marks)

```
+------------------------------------+------------------------------------+
|        IMMERSION (SYSTEM)          |        PRESENCE (MENTAL)           |
| - Technical Hardware Capability    | - Subjective Psychological Feeling |
| - Quantifiable Metrics (90Hz, FOV) | - Mel Slater: Place/Plausibility   |
+------------------------------------+------------------------------------+
```

1.  **Core Definition**:
    *   *Immersion* is an objective, quantifiable property of the VR hardware 
and engine (e.g., screen resolution, refresh rate, field of view, audio 
precision).
    *   *Presence* is the subjective, psychological state of feeling physically
located inside the virtual environment ("being there").
2.  **Determinants**:
    *   *Immersion* is elevated by upgrading physical hardware (e.g., switching
from 60 Hz to 90 Hz panels, adding 6DoF haptic controllers).
    *   *Presence* is achieved when high immersion triggers Mel Slater’s 
**Place Illusion (PI)** (sensorimotor consistency) and **Plausibility Illusion 
(Psi)** (logical world coherence).
3.  **Measurement**:
    *   *Immersion* is measured via engineering benchmarks (FPS, latency in ms,
pixel density PPI).
    *   *Presence* is measured via psychological surveys (Witmer-Singer scale) 
and physiological responses (heart rate variability, galvanic skin response).

#### Part B: 3DoF vs. 6DoF Hardware Architecture (5 Marks)

```
       3DoF (Rotational Tracking Only)            6DoF (Full Spatial Tracking)
             [Pitch, Yaw, Roll]            [Pitch, Yaw, Roll + X, Y, Z 
Translation]

                 Y (Yaw)                               Y (Yaw / Heave)
                   ^                                     ^
                   |                                     |   / Z (Surge)
                   |---> Pitch                           |  /
                  /                                      | /
                 v Roll                 X (Pitch/Sway)  +---------------->
```

*   **3DoF Hardware Architecture**:
    *   *Tracking Scope*: Tracks rotational movements only around 3 axes: Pitch
(X), Yaw (Y), and Roll (Z).
    *   *Sensor Rationale*: Uses internal **IMU sensors** (accelerometer, 
gyroscope, magnetometer). It cannot track user translation—if a user crouches, 
leans forward, or steps side-to-side, the virtual camera remains static.
    *   *Device Examples*: Google Cardboard, Samsung Gear VR, Oculus Go.
*   **6DoF Hardware Architecture**:
    *   *Tracking Scope*: Tracks 3 rotational axes (Pitch, Yaw, Roll) PLUS 3 
translational axes: Surge (forward/back), Heave (up/down), and Sway 
(left/right).
    *   *Sensor Rationale*: Combines IMUs with **Optical SLAM/VIO Camera 
Tracking** (Inside-Out) or External Laser Beacons (Outside-In).
    *   *User Capabilities*: Users can physically walk around objects, crouch 
under obstacles, and lean into scenes with 1:1 real-to-virtual motion accuracy.
    *   *Device Examples*: Meta Quest 3, HTC Vive Pro, Apple Vision Pro.

---

### Question 3 [20 Marks]
**Prompt**: Explain the workflow of developing a VR Laboratory Simulator using 
Unity and Meta XR SDK. Cover Environment Setup, User Movement Logic, Input 
Mapping, and Frame Rate Optimization.  
*(Marking Scheme: Environment Setup = 5 Marks; User Movement Logic = 5 Marks; 
Input Mapping = 5 Marks; Frame Rate Optimization = 5 Marks)*

#### Model Answer:

```
+------------------------------------------------------------------------------
-----+
|                     VR LAB SIMULATOR DEVELOPMENT PIPELINE                    
|
+-------------------+--------------------+-------------------+-----------------
-----+
| 1. Environment    | 2. Locomotion Logic| 3. Input Mapping  | 4. Optimization 
|
|  - Unity 3D URP   |  - Teleportation   |  - OVRInput       |  - Single Pass 
Inst  |
|  - Meta XR SDK    |  - Snap Turn       |  - Action Maps    |  - FFR & ASW    
|
|  - OVRCameraRig   |  - Continuous Move |  - Trigger / Grip |  - Occlusion 
Culling |
+-------------------+--------------------+-------------------+-----------------
-----+
```

#### Component 1: Environment Setup & SDK Integration (5 Marks)
1.  **Project Creation & Render Pipeline**:
    *   Open Unity Hub and create a 3D project using the **Universal Render 
Pipeline (URP)** for optimized mobile GPU rendering.
    *   Navigate to **Project Settings > XR Plug-in Management** and enable 
**OpenXR** / **Meta Quest Support** for Android build target.
2.  **Meta XR All-In-One SDK Import**:
    *   Import the **Meta XR All-In-One SDK** from the Unity Asset Store / 
Package Manager.
3.  **Rig Construction**:
    *   Remove the default `Main Camera` from the scene.
    *   Drag the `OVRCameraRig` or `XR Origin` prefab into the scene hierarchy.
    *   Set the `OVRManager` tracking origin mode to **Floor Level** to ensure 
the virtual floor aligns with physical floor height.

#### Component 2: User Movement & Locomotion Logic (5 Marks)
Movement in a laboratory simulation requires precision and comfort to avoid 
motion sickness:
*   **Teleportation Locomotion (Comfort Mode)**:
    *   Uses a parabolic raycast line pointer. When the user holds the 
thumbstick forward and releases, a `TeleportationProvider` instantly updates 
the camera position to the target raycast intersection on a designated 
`Teleportation Area` mesh.
*   **Continuous Locomotion (Smooth Movement)**:
    *   Reads 2D thumbstick axes to translate the player rig linearly through 
space using a `CharacterController`.
*   **Snap Turn**:
    *   Rotates the camera in discrete angular steps (e.g., 30-degree or 
45-degree instant snaps) on thumbstick horizontal displacement to eliminate 
smooth rotational motion blur that triggers nausea.

```
+────────────────────────────────────────────────────────────────────────────+
|                 VR LOCOMOTION & SNAP TURN EXECUTION PIPELINE               |
+────────────────────────────────────────────────────────────────────────────+

  [ Thumbstick Primary Axis (X, Y) ]
                  │
                  ▼
  [ Vector Projection & Direction Alignment ]
  • Extract Camera Forward Vector: V_fwd = Normalize(Camera.Forward - Y_axis)
  • Compute Translational Vector: V_move = (V_fwd * Axis.y + Camera.Right * Axis.x) * Speed * dt
                  │
                  ▼
  [ Character Controller Collision Sweep ] ──► Updates Player Metric Origin
                  │
                  ▼
  [ Secondary Thumbstick Horizontal Flick ]
  ├─► Left Flick (< -Threshold): Rotate Origin by -45 degrees around Camera Up
  └─► Right Flick (> +Threshold): Rotate Origin by +45 degrees around Camera Up
  (Instantaneous Angular Snap eliminates continuous optical motion blur & nausea)
```

#### Component 3: Input Mapping & Object Interaction (5 Marks)
In a VR lab simulator, users must pick up lab equipment (beakers, tools) using Meta Quest Touch controllers:
*   **Trigger (Index Finger)**: Mapped to secondary object actions (e.g., pouring liquid, activating a heat source).
*   **Grip Button (Middle Finger / Palm)**: Mapped to physical grabbing (`OVRGrabber` / `XR Direct Interactor`). Pressing the grip button attaches nearby colliders containing an `OVRGrabbable` / `XR Grab Interactable` component to the hand anchor transform.

```
+────────────────────────────────────────────────────────────────────────────+
|            LAB EQUIPMENT GRAB & VELOCITY TRANSFER STATE MACHINE            |
+────────────────────────────────────────────────────────────────────────────+

  [ Controller Grip Trigger Squeezed ]
                  │
                  ▼
  [ Spatial Sphere-Overlap Query ]
  • Query Physics.OverlapSphere around Hand Anchor (Radius = 0.15m)
  • Filter collisions using bitwise LayerMask: "LabEquipment"
                  │
                  ▼
  [ Object Attachment (Near Interaction) ]
  • Target Rigidbody switched to IsKinematic = True (Suppresses Gravity)
  • Child Transform parented to Hand Anchor Node
                  │
                  ▼
  [ Controller Grip Trigger Released ]
                  │
                  ▼
  [ Physical Decoupling & Momentum Transfer ]
  • Transform unparented (returns to World Root)
  • Rigidbody switched to IsKinematic = False
  • Linear & Angular Velocities sampled from IMU buffer and injected into Rigidbody:
      V_linear = OVRInput.GetLocalControllerVelocity()
      W_angular = OVRInput.GetLocalControllerAngularVelocity()
```

#### Component 4: Frame Rate Optimization Techniques for Meta Quest (5 Marks)
To achieve a stable **72 FPS / 90 FPS** target on standalone Meta Quest mobile 
hardware, developers must apply four primary optimization strategies:

1.  **Single Pass Stereo Instancing**:
    *   Combines left and right eye rendering into a single draw call pass 
using texture array indexing. Reduces CPU draw call overhead by ~50% compared 
to Multi-Pass rendering.
2.  **Fixed Foveated Rendering (FFR)**:
    *   Leverages the focal property of human vision. Renders the peripheral 
display regions at lower shading resolutions while preserving 100% full pixel 
density in the center of the display lens, reducing GPU shading workload.
3.  **Application SpaceWarp (ASW)**:
    *   Enables the app to render natively at 45 FPS while ASW uses motion 
vectors and depth buffers to synthesize every second frame, outputting a smooth
90 Hz display rate to the user.
4.  **Draw Call Batching & Occlusion Culling**:
    *   Combine static laboratory furniture meshes using **Static Batching**. 
Bake lightmaps to eliminate real-time lights and execute **Occlusion Culling** 
to prevent rendering hidden equipment behind walls.

```
SINGLE PASS STEREO INSTANCING               FIXED FOVEATED RENDERING (FFR)
+---------------------------------+         +---------------------------------+
|  Single GPU Draw Pass           |         |  [ 50% Res ] [ 100% ] [ 50% ]   |
|  [ Eye Left TXT | Eye Right TXT]|         |  Outer Periphery | Lens Center  |
+---------------------------------+         +---------------------------------+
```
