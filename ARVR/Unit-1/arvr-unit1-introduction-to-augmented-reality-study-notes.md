# Comprehensive Study Notes — Unit 1: Introduction to Augmented Reality
**Course Code:** NMIMS ARVR (702COI002 / 702MH0I004)  
**Target Assessment:** Final Examination Synoptics & Core Theory

---

## Section 1: Definitions, Scope, and the XR Umbrella

### 1. Fundamental Definitions
* **Azuma's Definition (1997):** Augmented Reality (AR) is defined as a system 
that satisfies three core characteristics:
  1. **Combines real and virtual content** in a real-world environment.
  2. Is **interactive in real time**.
  3. Is **registered in 3D** space aligned with physical surroundings.
* **Milgram & Kishino's Definition (1994):** Mixed Reality (MR) is 
conceptualized along the **Virtuality Continuum**. It spans from a 
completely physical **Real Environment** to a completely computer-generated 
**Virtual Environment**. MR acts as an umbrella for any environment where 
real and virtual objects are merged:
  * **Augmented Reality (AR):** Primarily real-world dominated, overlaid with 
synthetic 3D elements.
  * **Augmented Virtuality (AV):** Primarily virtual-world dominated, 
incorporating real-time real-world feeds (e.g., live video textures on virtual 
avatars).
* **Origin of Terms:**
  * **Virtual Reality (VR):** Term coined by **Jaron Lanier**. VR isolates 
the user entirely from physical reality into a computer-simulated realm.
  * **Augmented Reality (AR):** Term coined in 1990 by Boeing researchers **Tom
Caudell and David Mizell** to describe digital head-mounted displays used in 
aircraft wire bundle assembly.

```
                     MILGRAM'S VIRTUALITY CONTINUUM
|<------------------------------------------------------------------------->|
|                                                                           |
|   Real Environment      Augmented Reality    Augmented Virtuality   Virtual 
Environment  |
|     (Physical)               (AR)                   (AV)                  
(VR)           |
|____________________|________________________|___________________|____________
________|
                     |                                            |
                     |<----------- MIXED REALITY (MR) ----------->|
```

### 2. Scope & The XR Umbrella
* **Extended Reality (XR):** Serves as the overarching umbrella term 
encompassing **AR, VR, and MR**.
* **Core Technological Pillars Behind XR:**
  * **Artificial Intelligence (AI):** Object recognition, computer vision, 
gesture tracking, and scene perception.
  * **Embedded Systems:** Compact sensors (IMUs, depth cameras, LIDAR), 
specialized mobile SOCs, and power-efficient microprocessors.
  * **Human-Computer Interaction (HCI):** Spatial UIs, natural user interfaces 
(spatial gestures, eye tracking, voice commands).
* **Primary Development Platforms:**
  * **Unity:** C# scripting (industry standard for AR Foundation and 
cross-platform deployment).
  * **Unreal Engine:** C++ and Blueprint visual scripting for high-fidelity 
graphics.
  * **Native SDKs:** Android Studio (Kotlin / Java + ARCore native) and Xcode 
(Swift + ARKit native).

---

## Section 2: Historical Milestones (1968 – 2017)

The evolution of Augmented Reality spans key academic, military, and commercial
breakthroughs:

```
+------------------------------------------------------------------------------
-----+
| 1968 | Ivan Sutherland builds 'The Sword of Damocles' (First Optical HMD)    
|
| 1974 | Myron Krueger creates 'Videoplace' (Artificial Reality Lab)           
|
| 1990 | Caudell & Mizell (Boeing) coin the term 'Augmented Reality'           
|
| 1992 | Louis Rosenberg builds 'Virtual Fixtures' at USAF Armstrong Labs      
|
| 1993 | Steve Feiner et al. introduce KARMA (First Knowledge-Based AR)        
|
| 1994 | Milgram & Kishino publish the 'Virtuality Continuum' Taxonomy         
|
| 1998 | Sportvision launches 'NFL 1st & Ten' yellow yard-line overlay         
|
| 1999 | Hirokazu Kato creates ARToolKit (First Open-Source AR Tracking 
Library)   |
| 2014 | Google Glass commercializes consumer wearable AR                      
|
| 2016 | Microsoft HoloLens (Spatial Computing) & Niantic's Pokémon GO released
|
| 2017 | Apple launches ARKit, Google launches ARCore & IKEA releases 'IKEA 
Place'   |
+------------------------------------------------------------------------------
-----+
```

* **1968 — Sutherland's Sword of Damocles:** Ivan Sutherland completed the 
first head-mounted display (HMD) system with see-through optics and mechanical 
head tracking.
* **1974 — Videoplace:** Myron Krueger established an interactive room 
laboratory at the University of Connecticut enabling unencumbered gesture 
interaction.
* **1990 — Boeing Wire Assembly:** Tom Caudell and David Mizell designed a 
see-through HMD to guide workers through aircraft wiring harness schematics, 
coining "Augmented Reality".
* **1992 — Virtual Fixtures:** Louis Rosenberg created an early functional AR 
system for the US Air Force, overlaying sensory guidance on telerobotics.
* **1993 — KARMA (Knowledge-based AR for Maintenance Assistance):** Developed 
at Columbia University by Feiner et al. to guide laser printer repair via 3D 
graphics.
* **1994 — Milgram's Virtuality Continuum:** Formally defined MR and AR 
taxonomies in spatial computing.
* **1998 — NFL 1st & Ten Line:** First mainstream broadcasting AR application, 
superimposing a green/yellow line on live football fields.
* **1999/2000 — ARToolKit:** Hirokazu Kato released open-source computer vision
tracking using planar fiducial square markers.
* **2014 – 2017 — Modern Mobile & Spatial Era:** Evolution from **Google 
Glass** (2014) to untethered spatial computing headsets like **Microsoft 
HoloLens** (2016), mobile markerless SLAM tracking via **ARKit/ARCore**
(2017), and retail adoption via **IKEA Place** (2017).

---

## Section 3: Display Technologies

AR displays merge synthetic graphics with physical light using three primary 
architectural methods:

```
                              AR DISPLAY PARADIGMS
                                       |
    +----------------------------------+----------------------------------+
    |                                  |                                  |
  Optical See-Through (OST)         Video See-Through (VST)           Spatial 
AR (SAR) /
 (Direct Optical Combiners)        (Camera Video Feed Composite)      
Projection Mapping
  e.g., HoloLens, Glass    e.g., Mobile Phones, Quest    e.g., 
Projectors, SRD
```

### 1. Optical See-Through (OST) vs. Video See-Through (VST)

| Feature / Metric | Optical See-Through (OST) | Video See-Through (VST) |
| :--- | :--- | :--- |
| **Operating Principle** | Uses semi-transparent optical combiners (beam splitters, waveguides, prisms) to reflect computer visuals directly into the user's eye while allowing direct sunlight/ambient light to pass through. | Uses external cameras to capture real-world video, composites digital graphics over video frames in software, and outputs the composite image to an opaque display. |
| **View of Reality** | **Direct, unmediated optical sight.** Zero optical delay or latency for physical scene viewing. | **Mediated video feed.** Subject to camera exposure, sensor noise, resolution caps, and processing lag. |
| **Latency Impact** | Zero latency on real-world view. Dynamic latency only affects virtual overlays, which may "swim" or lag during fast head movements . | Video feed delay must match graphic rendering latency. High latency (>20–30 ms) risks severe motion sickness. |
| **Brightness & Contrast** | High ambient light (e.g., direct sunlight) washes out virtual overlays. Requires physical LCD shutter masks. | Brightness and contrast of real and virtual feeds can be software-matched perfectly in any lighting. |
| **Occlusion & Alignment** | Hard to achieve true black or full occlusion; virtual objects appear translucent. | **Exact pixel-level occlusion.** Virtual objects can completely block out physical backgrounds. |
| **Safety in Failure** | Safe. If power fails or software crashes, the user still sees the physical world. | Danger of total darkness/blindness if cameras or software fail while navigating. |
| **Representative Hardware** | Microsoft HoloLens, Google Glass, Sony Glasstron. | Apple Vision Pro, Meta Quest 3 pass-through, Smartphone/Tablet AR. |

### 2. Spatial AR (SAR) & Projection Mapping
* **Projection-Based AR / Spatial AR:** Projects synthetic light directly onto 
physical 3D objects or surfaces (e.g., buildings, industrial machinery, or 
physical models) using high-output projectors.
* **Spatial Reality Displays (SRD):** Reproduce spatial 3D visuals using 
micro-optical lenses and eye tracking, allowing viewing without 3D glasses or 
HMDs.

### 3. Multimodal AR Interfaces
* Integrates visual overlays with **3D spatial audio** (distance/directional 
cues), **haptic feedback** (vibrations/force-feedback controllers), and 
**natural user interfaces** (MediaPipe vision-based gesture tracking and voice 
commands) to maximize presence and immersion.

---

## Section 4: Strong AR vs. Weak AR

In spatial computing engineering and NMIMS examination synoptics, AR systems 
are categorized by their level of spatial awareness and scene perception:

```
+------------------------------------------------------------------------------
------+
|                                 STRONG AR vs. WEAK AR                        
|
+------------------------------------+-----------------------------------------
------+
| Feature                            | Strong AR (Spatial / Context-Aware)  |
+------------------------------------+-----------------------------------------
------+
| Spatial Tracking                   | 6DOF SLAM (Simultaneous Localization & 
Mapping)|
| Environmental Integration          | 3D Mesh, Plane Detection, Occlusion, 
Physics  |
| Primary Examples                   | IKEA Place, HoloLens, AR Maintenance 
  |
+------------------------------------+-----------------------------------------
------+
| Feature                            | Weak AR (2D / Non-Contextual)  
|
+------------------------------------+-----------------------------------------
------+
| Spatial Tracking                   | 3DOF / Sensor HUD / 2D Pattern / GPS    
|
| Environmental Integration          | Floating 2D Overlay, No Surface Geometry
|
| Primary Examples                   | Snapchat 2D Filters, Yelp Monocle HUD 
|
+------------------------------------+-----------------------------------------
------+
```

* **Strong AR (Context-Aware / Spatial AR):**
  * **Definition:** Utilizes **6DOF (Degrees of Freedom) tracking** combined 
with **3D spatial mapping / SLAM** (Simultaneous Localization and Mapping). The system understands environmental geometry, surface boundaries, 
light estimation, and real-time collision/occlusion.
  * **Behavior:** Virtual 3D assets remain anchored to physical surfaces 
(floors, tables), cast shadows, and are hidden behind physical objects when 
blocked.
  * **Examples:** **IKEA Place** placing true-to-scale furniture on detected 
room floors, **Microsoft HoloLens** spatial applications, and **AR 
Foundation vehicle maintenance repair assistants**.
* **Weak AR (2D Overlay / Non-Contextual AR):**
  * **Definition:** Relies on basic 2D pattern matching, 3DOF orientation 
sensors (gyroscope/compass), or GPS coordinates. It lacks 3D 
spatial mapping or physical scene awareness.
  * **Behavior:** Digital content is presented as a static 2D layer or floating
heads-up display (HUD) over the screen, regardless of room contours or physical
depth.
  * **Examples:** **Snapchat 2D face stickers**, **Yelp Monocle** GPS 
compass overlays, or simple screen-space navigation arrows.

---

## Section 5: Engineering & Industry Applications

```
                       ENGINEERING APPLICATIONS OF AR
                                     |
       +-----------------------------+-----------------------------+
       |                             |                             |
    Aviation                      Medicine                   Maintenance &
  (HUDs, Flight Telemetry,      (CamC X-Ray Overlays,      Industrial 
Operations
   Boeing Wire Harness) Surgical Navigation) (KARMA, Step-by-Step 
Guides)
```

1. **Aviation & Aerospace:**
   * **In-Flight Telemetry:** Heads-Up Displays (HUDs) and Helmet-Mounted 
Displays project critical airspeed, horizon, altitude, and targeting reticles 
directly into pilot line-of-sight.
   * **Manufacturing Assembly:** Boeing wire bundle assembly systems overlay 
wiring schematics onto physical boards to eliminate manual paper blueprints.
2. **Medicine & Healthcare:**
   * **Surgical Navigation:** Systems like the **CamC mobile C-arm** merge live
optical video with real-time X-ray feeds, allowing surgeons to visualize 
internal bone structures, vascular networks, or shrapnel without looking away 
from the patient.
   * **Anatomical Training:** Interactive 3D holographic overlays on medical 
mannequins accelerate clinical skill acquisition.
3. **Industrial Maintenance & Repair:**
   * **Step-by-Step Spatial Guidance:** Knowledge-based systems (e.g., Columbia
KARMA) overlay animated 3D tools and directional arrows directly on equipment 
(valves, engines, coffee brewing units) to guide technicians through assembly 
and disassembly.

---

## Section 6: Technical & Usability Challenges

```
                           TECHNICAL & USABILITY CHALLENGES
                                          |
   +--------------------+-----------------+--------------------+---------------
----+
   |                    |                 |                    |               
|
Latency & Lag        Tracking &        Field of View        Physical Safety    
Privacy & Legal
(End-to-End <20ms)   Registration      (Clipping / Window)  (Distraction/Risks)
(Unregulated Feed)

```

1. **Latency & Dynamic Delay:**
   * **End-to-End Delay:** Sum of sensor sample time, camera frame capture, 
SLAM pose calculation, GPU rendering, and display pipeline sync.
   * **Impact:** Delays exceeding **20–30 ms** cause spatial lag ("swimming") 
between virtual assets and physical targets, leading to **simulator sickness** 
.
2. **Tracking & Registration Accuracy:**
   * **Spatial Errors:** Jitter, drift, and misregistration occur when feature 
points are lost (e.g., featureless white walls, reflections, or fast camera 
panning).
   * **Requirement:** Requires robust Visual-Inertial Odometry (VIO) and 
continuous tracking reinitialization.
3. **Field of View (FOV) Restrictions:**
   * **Window Effect:** Most Optical See-Through displays feature limited 
diagonal FOVs (30°–50°), causing virtual objects to be abruptly clipped at 
peripheral boundaries.
4. **Physical Safety, Ethics, and Privacy:**
   * **Physical Hazards:** User immersion and screen distraction create 
real-world collision/injury risks in industrial zones or street navigation 
(e.g., **Pokémon GO accidents**).
   * **Privacy & Regulation:** Continuous background camera feeds capture 
bystanders without consent in public spaces; clear regulatory standards for AR 
spatial data processing remain lacking.

---

## Section 7: NMIMS Exam Scaffolding & Answer Scenarios

---

### [5 Marks] Exam Question 1(a)
**Prompt:** Define Augmented Reality and Virtual Reality. Mention one 
engineering application of each.

```
+-------------------------------------------------------------------+
|                     MARKING SCHEME SPLIT                      |
+-------------------------------------------------------------------+
| AR Definition                                         | 1.0 Mark  |
| AR Engineering Application + Brief Detail             | 1.5 Marks |
| VR Definition                                         | 1.0 Mark  |
| VR Engineering Application + Brief Detail             | 1.5 Marks |
| TOTAL                                                 | 5.0 Marks |
+-------------------------------------------------------------------+
```

#### Answer Template:
1. **Augmented Reality (AR) Definition:**
   AR is an interactive technology that overlays computer-generated digital 
graphics, 3D models, or perceptual data onto the physical real-world 
environment in real time, maintaining precise 3D spatial alignment without 
isolating the user.
2. **AR Engineering Application — Aircraft Wiring Assembly (Boeing):**
   Boeing technicians use see-through AR head-mounted displays during aircraft 
manufacturing. The AR system overlays 3D wiring harness schematics and 
connection points directly onto physical assembly boards, reducing assembly 
time and human error.
3. **Virtual Reality (VR) Definition:**
   VR is a fully immersive technology that uses opaque displays and motion 
tracking to replace the user's physical surroundings with a 100% 
computer-generated 3D virtual environment, completely isolating the user from 
the real world.
4. **VR Engineering Application — Automotive Flight / Factory Simulation:**
   Automotive manufacturers (e.g., Mercedes-Benz) use fully immersive VR 
headsets to simulate factory assembly lines and crash safety ergonomics, 
allowing engineers to test vehicle maintenance and spatial clearance before 
physical prototypes are built.

---

### [5 Marks] Exam Question 1(c)
**Prompt:** Differentiate between Strong AR and Weak AR. Provide an example of 
each.

```
+-------------------------------------------------------------------+
|                     MARKING SCHEME SPLIT                      |
+-------------------------------------------------------------------+
| Strong AR Definition & Technical Characteristics     | 1.5 Marks |
| Strong AR Industry Example                            | 1.0 Mark  |
| Weak AR Definition & Technical Characteristics       | 1.5 Marks |
| Weak AR Industry Example                              | 1.0 Mark  |
| TOTAL                                                 | 5.0 Marks |
+-------------------------------------------------------------------+
```

#### Answer Template:
1. **Strong AR:**
   * **Definition:** Strong AR relies on **6DOF spatial tracking** and 
real-time **3D environmental mapping (SLAM)**. It dynamically 
extracts surface planes, ambient lighting, and depth geometry so virtual 
objects anchor naturally to physical surfaces and interact with real-world 
occlusion/physics.
   * **Example:** **IKEA Place / AR Maintenance Assistant** — 3D furniture or 
engine overlays detect floor/machinery geometry and remain spatially locked in 
place even when the user walks around the object.
2. **Weak AR:**
   * **Definition:** Weak AR utilizes basic 2D pattern matching, 3DOF 
orientation sensors (gyroscope/compass), or GPS coordinates without 
understanding 3D room geometry or physical spatial depth. Content 
is displayed as a flat overlay on top of the camera view.
   * **Example:** **Snapchat 2D Face Filters / Yelp Monocle** — Floating 2D 
stickers or heads-up compass pointers superimposed over camera video without 
physical depth interaction.

---

### [10 Marks] Exam Question 4(a)
**Prompt:** Compare AR, VR, and Mixed Reality (MR) environments with reference 
to user interaction and tracking needs.

```
+-------------------------------------------------------------------+
|                     MARKING SCHEME SPLIT                      |
+-------------------------------------------------------------------+
| Comparison of Immersion & Environmental Synthesis     | 3.0 Marks |
| Comparison of Interaction Paradigm & UIs             | 3.0 Marks |
| Comparison of Tracking Needs & Hardware Architecture  | 4.0 Marks |
| TOTAL                                                 | 10.0 Marks|
+-------------------------------------------------------------------+
```

#### Comprehensive 3-Way Comparison Matrix:

| Feature / Dimension | Augmented Reality (AR) | Virtual Reality (VR) | Mixed Reality (MR) |
| :--- | :--- | :--- | :--- |
| **1. Environmental Synthesis** | Overlays 2D/3D digital graphics onto the physical world. Physical world remains dominant. | Replaces physical world entirely with a 100% computer-generated environment. | Blends real and virtual worlds where physical and digital objects coexist and interact in real time. |
| **2. Immersion Level [3 Marks]** | **Partial / Non-occluding Immersion.** User remains aware of physical surroundings. | **Total Immersion.** User is completely cut off from physical sight and surroundings. | **Hybrid / High Spatial Immersion.** Seamless visual integration via depth sensing and spatial lighting. |
| **3. Interaction Model [3 Marks]** | Touchscreen gestures (mobile), raycasting, spatial tap, and 2D UI widgets. | 6DOF handheld motion controllers, teleportation, continuous joystick locomotion, haptic gloves. | Direct spatial manipulation, mid-air hand gesture tracking, gaze tracking, and physical surface mapping. |
| **4. Tracking Needs [4 Marks]** | 6DOF SLAM, Visual-Inertial Odometry (VIO), surface plane detection, camera feature tracking. | 6DOF Head & Controller tracking, IMU sensor fusion, inside-out camera / outside-in lighthouse tracking. | **High-Precision Spatial Mapping.** Mesh reconstruction, depth sensing (ToF/LIDAR), semantic object recognition. |
| **5. Hardware Displays** | Smart glasses (HoloLens), mobile phones (ARKit/ARCore), heads-up displays. | Closed opaque HMDs (Meta Quest, HTC Vive, Oculus Rift). | Advanced OST/VST Headsets with integrated depth sensors and spatial mapping chips. |

---

### [20 Marks] Exam Question 5: Complete AR Development Scenario
**Prompt:** Design an AR-based vehicle maintenance assistant using Unity + AR 
Foundation. Describe scene setup, overlay logic, control, and deployment 
strategy.

```
+-------------------------------------------------------------------+
|                     MARKING SCHEME SPLIT                      |
+-------------------------------------------------------------------+
| Component 1: Scene setup with physical alignment & tracking | 6.0 Marks|
| Component 2: Overlay logic: Object recognition & instructions| 8.0 Marks|
| Component 3: Controls & deployment strategy                  | 6.0 Marks|
| TOTAL                                                        | 20.0 Marks|
+-------------------------------------------------------------------+
```

#### Component 1: Scene Setup, Physical Alignment & Tracking [6 Marks]
1. **Unity Project & Package Setup:**
   * Create a 3D Unity project. Navigate to `Package Manager` and install **AR 
Foundation**, **ARCore XR Plugin** (Android), and **ARKit XR Plugin** (iOS) 
.
   * Set Scripting Backend to **IL2CPP** and Target API to Android 7.0 (API 
Level 24+) or higher.
2. **Scene Hierarchy Construction:**
   * Delete the default Main Camera.
   * Add **AR Session** GameObject (manages AR lifecycle, system state, and 
camera tracking drivers).
   * Add **XR Origin / AR Session Origin** GameObject:
     * Houses the **AR Camera** (tagged as `MainCamera`, tagged with `AR Camera
Manager` and `AR Camera Background` components to render live camera video 
feed).
     * Attach **AR Plane Manager** (Detection Mode: Horizontal & Vertical) to 
perform real-time surface plane detection.
     * Attach **AR Raycast Manager** to perform screen-to-world spatial 
raycasts against physical geometry.
     * Attach **AR Tracked Image Manager** or **AR Object Manager** to store 
the reference image/mesh library of the vehicle engine bay for physical anchor 
alignment.

```
+------------------------------------------------------------------------------
-----+
|                        UNITY AR FOUNDATION SCENE HIERARCHY                   
|
+------------------------------------------------------------------------------
-----+
| [Scene Root]                                                                 
|
|  ├── AR Session (Manages tracking lifecycle & system state)                  
|
|  └── XR Origin (AR Session Origin)                                           
|
|       ├── AR Camera (Renders live camera feed & tracks 6DOF pose)            
|
|       ├── AR Plane Manager (Detects floor/engine flat planes)                
|
|       ├── AR Raycast Manager (Executes spatial raycasts against mesh)        
|
|       └── AR Tracked Image Manager (Tracks physical engine target marker)    
|
+------------------------------------------------------------------------------
-----+
```

---

#### Component 2: Overlay Logic, Object Recognition & Scripting [8 Marks]
1. **Tracking & Physical Alignment Logic:**
   * An **Image Marker / QR Anchor** is placed on the physical vehicle engine 
block.
   * When `ARTrackedImageManager` detects the engine marker, it instantiates 
the Maintenance UI Anchor at the exact 3D spatial pose.
2. **Step-by-Step C# Script Implementation (`VehicleMaintenanceManager.cs`):**

```csharp
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using TMPro;

public class VehicleMaintenanceManager : MonoBehaviour
{
    [Header("AR Foundation Components")]
    [SerializeField] private ARTrackedImageManager trackedImageManager;
    
    [Header("UI & Spatial Overlays")]
    [SerializeField] private GameObject step1EngineOilOverlay;
    [SerializeField] private GameObject step2BatteryOverlay;
    [SerializeField] private TextMeshProUGUI instructionText;

    private int currentStep = 0;

    private void OnEnable()
    {
        trackedImageManager.trackedImagesChanged += OnTrackedImagesChanged;
    }

    private void OnDisable()
    {
        trackedImageManager.trackedImagesChanged -= OnTrackedImagesChanged;
    }

    private void OnTrackedImagesChanged(ARTrackedImagesChangedEventArgs 
eventArgs)
    {
        foreach (var trackedImage in eventArgs.added)
        {
            if (trackedImage.referenceImage.name == "EngineBlockMarker")
            {
                // Align UI origin to physical engine anchor
                transform.position = trackedImage.transform.position;
                transform.rotation = trackedImage.transform.rotation;
                ShowStep(0);
            }
        }
    }

    public void AdvanceNextStep()
    {
        currentStep++;
        ShowStep(currentStep);
    }

    private void ShowStep(int stepIndex)
    {
        step1EngineOilOverlay.SetActive(stepIndex == 0);
        step2BatteryOverlay.SetActive(stepIndex == 1);

        switch (stepIndex)
        {
            case 0:
                instructionText.text = "Step 1: Unscrew Oil Cap & Check 
Dipstick Level.";
                break;
            case 1:
                instructionText.text = "Step 2: Disconnect Negative Battery 
Terminal First.";
                break;
            default:
                instructionText.text = "Maintenance Check Complete!";
                break;
        }
    }
}
```

3. **Visual Feedback & AR Guidance Overlays:**
   * **3D Animated Arrows:** Superimpose pulsing 3D directional arrows pointing
to the oil cap using transparent highlighted shaders.
   * **Spatial World-Space Canvas:** Attach a World-Space Canvas containing 
step descriptions, safety warnings, and an "Advance Step" button positioned 
directly beside the target part.

---

#### Component 3: Controls, Performance Optimization & Deployment Strategy [6 
Marks]
1. **User Interaction & Controls:**
   * **Screen Touch Raycasting:** Tapping screen elements sends a raycast via 
`ARRaycastManager` to select 3D car components.
   * **Voice / Spatial Button Controls:** Next/Previous UI buttons mounted on a
billboarding screen Canvas that always faces the operator.
2. **Performance Optimization Techniques:**
   * **Target Frame Rate:** Force `Application.targetFrameRate = 60` to ensure 
smooth tracking and prevent motion jitter.
   * **Shader & Polygon Optimization:** Use mobile-optimized 
Lightweight/Universal Render Pipeline (URP) shaders (`Unlit` or `Simple Lit`) 
to maintain high mobile performance.
   * **Texture Compression & Occlusion Culling:** Compress textures to ASTC 
format and disable plane detection once physical alignment is locked to 
conserve CPU/GPU cycles.
3. **Build Target & Deployment Pipeline (Android Export):**
   * **Build Settings:** Select **Android** platform -> Switch Platform.
   * **Player Settings:**
     * Set **Min API Level** to Android 7.0 'Nougat' (API Level 24).
     * Disable **Auto Graphics API**, remove OpenGLES2, and enforce **Vulkan / 
OpenGLES3**.
     * Set Architecture to **ARM64** (required for Google Play & ARCore native 
binaries).
     * Enable **Require AR** in XR Plug-in Management -> ARCore settings.
   * **Export & Testing:** Connect target mobile device via USB, execute `Build
and Run` to compile the standalone `.apk`, and verify spatial alignment on the 
physical vehicle.

---
