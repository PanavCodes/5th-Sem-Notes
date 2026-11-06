# Unit 8: Fundamentals of Digital Video and Its Compression — Comprehensive Study Notes & Exam Guide

## 1. Introduction to Digital Video and Temporal Correlation

A digital video signal is fundamentally a time-varying sequence of two-dimensional (2D) image matrices (frames) acquired at constant temporal intervals. While a static digital image $`f(x,y)`$ represents a spatial distribution of light intensities across spatial coordinates $(x,y)$, a video signal $`f(x,y,t)`$ incorporates a continuous temporal parameter $`t`$, capturing motion and scene evolution over time.

### 1.1 Temporal Redundancy and Inter-Frame Correlation

In standard video sequences sampled at typical rates of 25 to 60 frames per second (fps), consecutive frames exhibit extremely high spatial and temporal similarities. Except for fast-moving objects or sudden camera cuts, large portions of the background and stationary objects remain virtually identical across successive frames.

```text
Temporal Sequence of Video Frames:

+-----------------+       +-----------------+       +-----------------+
| Frame (t - 1)   | ----> | Frame (t)       | ----> | Frame (t + 1)   |
| [Previous]      |       | [Current]       |       | [Next]          |
+-----------------+       +-----------------+       +-----------------+
        |                          |                         |
        +--- High Correlation -----+--- High Correlation ----+
             (Temporal Redundancy: > 90% Unchanged Pixels)
```

#### Key Concepts of Video Redundancy
* **Spatial Redundancy (Intra-Frame):** Correlation existing among neighboring pixels within the same single image frame (exploited by spatial transforms like DCT).
* **Temporal Redundancy (Inter-Frame):** Correlation existing among corresponding spatial pixels across successive time frames. Exploiting temporal redundancy is the single most important mechanism for achieving high video compression ratios ($`> 50:1`$).

#### Mathematical Formulation of Inter-Frame Correlation
The temporal correlation coefficient $`\rho`$ between two consecutive grayscale video frames $`f_k(x,y)`$ and $`f_{k-1}(x,y)`$ of size $`M \times N`$ is defined using the 2D correlation coefficient $`\text{corr2}`$:

```math
\rho = \frac{\sum_{x=0}^{M-1} \sum_{y=0}^{N-1} (f_k(x,y) - \bar{f}_k)(f_{k-1}(x,y) - \bar{f}_{k-1})}{\sqrt{\left[ \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} (f_k(x,y) - \bar{f}_k)^2 \right] \left[ \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} (f_{k-1}(x,y) - \bar{f}_{k-1})^2 \right]}}
```

Where $`\bar{f}_k`$ and $`\bar{f}_{k-1}`$ are the mean intensity values of frames $`k`$ and $`k-1`$, respectively. For typical video sequences, $`\rho > 0.95`$, indicating that over $`95\%`$ of pixel data can be temporally predicted rather than retransmitted.

---

### 1.2 Video Parameters and Bitrate Calculations

Digital video standards are governed by fundamental temporal and spatial parameters:

1. **Frame Rate ($`f_s`$):** Number of complete frames displayed per second (measured in fps or Hz). Standard broadcast video uses 25 fps (PAL) or 29.97/30 fps (NTSC).
2. **Frame Time / Temporal Sampling Interval ($`T_s`$):** Time duration between two consecutive frames, defined as $`T_s = \frac{1}{f_s}`$.
3. **Line Rate ($`f_L`$):** Number of horizontal scan lines displayed per second: $`f_L = N_{\text{lines}} \times f_s`$.
4. **Uncompressed Bit Rate ($`R`$):** Transmission bandwidth required for raw video streams without compression:

```math
R = M \times N \times B \times f_s \quad \text{(bits per second)}
```

Where $`M \times N`$ is frame spatial resolution, $`B`$ is bit depth per pixel (e.g., 24 bits for 4:4:4 RGB or 12 bits for 4:2:0 YUV), and $`f_s`$ is frame rate.

---

## 2. Video Frame Classifications (I, P, and B Frames)

To achieve high compression efficiency while maintaining random access, error resilience, and fast seeking, digital video compression standards (such as MPEG-1, MPEG-2, MPEG-4, H.264/AVC, and H.265/HEVC) organize video sequences into a Group of Pictures (GOP) consisting of three distinct frame types: **I-Frames**, **P-Frames**, and **B-Frames**.

```text
Group of Pictures (GOP) Dependency Structure:

        +----------------------- Forward Prediction ----------------------+
        |                                                                 |
        v                                                                 v
    +-------+        +-------+        +-------+        +-------+      +-------+
    | I_1   | <====> | B_2   | <====> | B_3   | =====> | P_4   | ===> | P_7   |
    +-------+        +-------+        +-------+        +-------+      +-------+
       |                 ^                ^                |
       +--- Bidirectional Prediction ----+----------------+
```

---

### 2.1 Intra-Coded Frames (I-Frames)

* **Definition:** Self-contained reference frames encoded purely using spatial (intra-frame) compression techniques, completely independent of past or future frames.
* **Coding Mechanism:** The frame is divided into $`8 \times 8`$ or $`16 \times 16`$ blocks, transformed via Discrete Cosine Transform (DCT), quantized, and variable-length coded (identical to JPEG still image compression).
* **Role in Compression:**
  * Serves as the primary anchor point for a Group of Pictures (GOP).
  * Enables random access, channel tuning, and fast-forward/rewind seeking.
  * Stops temporal error propagation (resets transmission errors).
* **Compression Ratio:** Lowest compression ratio among all frame types (typically $`5:1`$ to $`10:1`$).

---

### 2.2 Predictive-Coded Frames (P-Frames)

* **Definition:** Inter-frame predicted frames encoded using forward motion estimation and compensation based on a single previously decoded reference frame (either an I-frame or a prior P-frame).
* **Coding Mechanism:**
  * For each macroblock in the current P-frame, a matching block is searched in the preceding reference frame.
  * Only the resulting **Motion Vector** $`\mathbf{v} = (dx, dy)`$ and the **Displaced Frame Difference (DFD)** residual matrix are transmitted.
* **Role in Compression:** Achieves significantly higher compression than I-frames (typically $`20:1`$ to $`30:1`$) by eliminating temporal redundancy.
* **Error Propagation:** If a reference frame suffers transmission loss, subsequent P-frames will propagate the reconstruction error until the next I-frame.

---

### 2.3 Bidirectionally Predictive-Coded Frames (B-Frames)

* **Definition:** Inter-frame interpolated frames encoded using motion compensation from **two reference frames**: one past reference frame and one future reference frame (I or P frames).
* **Prediction Modes:** A macroblock in a B-frame can use one of four prediction modes:
  1. **Forward Prediction:** Predicted from a past reference frame.
  2. **Backward Prediction:** Predicted from a future reference frame.
  3. **Bidirectional Interpolation:** Average of past and future matching blocks.
  4. **Intra Coding:** Encoded directly without prediction if motion is highly non-linear or obscured.
* **Role in Compression:**
  * Provides the highest compression ratio (typically $`50:1`$ to $`80:1`$).
  * Highly effective against object occlusions and background unveilings.
  * B-frames are non-reference frames (in standard MPEG), meaning errors in B-frames do **not** propagate to any other frame.

---

### 2.4 Display Order vs. Bitstream (Transmission / Processing) Reordering

Because B-frames require a **future reference frame** for decoding, the transmission order (bitstream order) in the encoder and decoder must differ from the chronological display order.

#### Example GOP Sequence
Consider a display sequence of 13 frames:

```text
Display Order:
Frame #:    1     2     3     4     5     6     7     8     9    10    11    12    13
Frame Type: I_1   B_2   B_3   P_4   B_5   B_6   P_7   B_8   B_9   P_10  B_11  B_12  I_13
```

To decode B-frame $`B_2`$ and B-frame $`B_3`$, the decoder requires both past frame $`I_1`$ and future frame $`P_4`$. Therefore, frame $`P_4`$ **must be transmitted and decoded before** $`B_2`$ and $`B_3`$.

#### Reordered Transmission / Bitstream Order

```text
Bitstream Order:
Position:   1     2     3     4     5     6     7     8     9    10    11    12    13
Frame Type: I_1   P_4   B_2   B_3   P_7   B_5   B_6   P_10  B_8   B_9   I_13  B_11  B_12
```

---

### 2.5 Comprehensive Comparison Matrix of I, P, and B Frames

| Parameter / Feature | I-Frame (Intra) | P-Frame (Predictive) | B-Frame (Bidirectional) |
| :--- | :--- | :--- | :--- |
| **Reference Dependence** | None (Self-contained) | 1 Past Reference (I or P) | 2 References (Past & Future I/P) |
| **Compression Ratio** | Low ($`5:1 - 10:1`$) | Medium ($`20:1 - 30:1`$) | Highest ($`50:1 - 80:1`$) |
| **Relative File Size** | Largest ($`100\%`$) | Medium ($`30\% - 40\%`$ of I) | Smallest ($`10\% - 20\%`$ of I) |
| **Error Propagation** | None (Resets errors) | Propagates to subsequent P/B | None (Non-reference frame) |
| **Computational Complexity**| Low (Spatial DCT only) | Moderate (Forward Search) | High (Dual Forward/Backward Search) |
| **Encoding/Decoding Latency**| Zero latency | Low latency | High latency (Frame reordering buffer) |
| **Random Access Capability** | Yes (Entry point) | No | No |

---

## 3. Fundamentals of Motion Estimation and Motion Compensation

Motion Estimation (ME) is the process of analyzing consecutive video frames to determine the movement vectors of objects. Motion Compensation (MC) uses these motion vectors to predict the current frame from reference frames, transmitting only the residual prediction error.

```text
Motion Estimation & Compensation Architecture:

Current Frame (t)                Reference Frame (t-1)
+-----------------------+        +-----------------------+
|  +-----+              |        |         +-----+       |
|  | MB  |              |        |         |Ref  |       |
|  +-----+              |        |         +-----+       |
+-----|-----------------+        +------------|----------+
      |                                       |
      +------------ Motion Estimation --------+
                           |
                           v
                  Motion Vector (dx, dy)
                           +
              Displaced Frame Difference (DFD)
```

---

### 3.1 Macroblock Partitioning and Search Window

1. **Macroblock (MB):** Video frames are partitioned into non-overlapping square blocks of $`M \times M`$ pixels (typically $`16 \times 16`$ pixels for luminance).
2. **Search Parameter ($`p`$):** The maximum allowable spatial displacement in pixels along horizontal and vertical directions ($`\pm p`$ pixels).
3. **Search Window Size:** For a search parameter $`p`$, the search window in the reference frame surrounding the current macroblock position has dimensions of $`(M + 2p) \times (M + 2p)`$ pixels, containing a total of $`(2p + 1) \times (2p + 1)`$ candidate displacement locations.

---

### 3.2 Block Distortion & Matching Cost Metrics

To select the best-matching candidate macroblock in the reference frame, a mathematical matching metric is evaluated across candidate displacement vectors $`(dx, dy)`$:

Let $`C(i,j)`$ be the pixel intensity at position $(i,j)$ in the current frame macroblock of size $`N \times N`$, and $`R(i+dx, j+dy)`$ be the pixel intensity in the reference frame candidate block shifted by displacement $`(dx, dy)`$.

#### 1. Sum of Absolute Differences (SAD)
SAD is the most widely used metric in hardware implementations because it avoids division and multiplication:

```math
\text{SAD}(dx, dy) = \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i+dx, j+dy) \rvert
```

#### 2. Mean Absolute Difference (MAD)
MAD normalizes SAD by the total number of pixels $`N^2`$:

```math
\text{MAD}(dx, dy) = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i+dx, j+dy) \rvert
```

#### 3. Mean Squared Error (MSE)
MSE computes the average squared intensity difference, penalizing large pixel errors more heavily:

```math
\text{MSE}(dx, dy) = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \left( C(i,j) - R(i+dx, j+dy) \right)^2
```

#### 4. Peak Signal-to-Noise Ratio (PSNR)
Reconstruction quality of motion-compensated frames is measured in decibels (dB):

```math
\text{PSNR} = 10 \log_{10} \left( \frac{\text{Peak}^2}{\text{MSE}} \right) = 10 \log_{10} \left( \frac{255^2}{\text{MSE}} \right)
```

Where $`\text{Peak} = 255`$ for 8-bit grayscale images.

---

### 3.3 Motion Vector Formulation

The optimal motion vector $`\mathbf{v}^* = (dx^*, dy^*)`$ is the displacement pair that minimizes the matching cost function over the search window $`[-p, +p]`$:

```math
(dx^*, dy^*) = \arg\min_{-p \le dx, dy \le +p} \text{SAD}(dx, dy)
```

The resulting motion vector represents the relative spatial shift:

```math
\mathbf{v} = (dx^*, dy^*) = (x_{\text{ref}} - x_{\text{curr}}, y_{\text{ref}} - y_{\text{curr}})
```

---

## 4. Motion Estimation Algorithms (Block Matching)

### 4.1 Exhaustive Search Block Matching Algorithm (ESBMA / Full Search)

The Exhaustive Search Block Matching Algorithm (also known as Full Search) evaluates the matching cost metric at **every single possible candidate location** within the search window $`[-p, +p]`$.

```text
Exhaustive Search Grid (Search Parameter p = 2, 5x5 = 25 Candidates):

   x  x  x  x  x
   x  x  x  x  x
   x  x (0,0) x  x
   x  x  x  x  x
   x  x  x  x  x

(Every candidate pixel position is tested systematically)
```

#### Algorithmic Steps
1. Position the current $`N \times N`$ macroblock over the same spatial location in the reference frame $(0,0)$.
2. Step through every integer displacement $(dx, dy)$ where $`-p \le dx \le +p`$ and $`-p \le dy \le +p`$.
3. Compute $`\text{SAD}(dx, dy)`$ for each of the $`(2p+1)^2`$ candidate positions.
4. Select displacement $(dx^*, dy^*)$ that yields the minimum SAD value as the final Motion Vector.

#### Performance Analysis
* **Total Candidate Search Locations per Macroblock:**

```math
N_{\text{pts}} = (2p + 1)^2
```

For a typical search parameter $`p = 7`$, $`N_{\text{pts}} = (2(7) + 1)^2 = 15^2 = 225`$ candidate blocks per macroblock.
* **Advantages:** Guarantees finding the globally optimal motion vector (lowest possible prediction residual).
* **Disadvantages:** Extremely high computational complexity; impractical for real-time video encoding without specialized hardware.

---

### 4.2 Three-Step Search Method (TSS / 3SS)

The Three-Step Search algorithm is a fast coarse-to-fine block matching algorithm that reduces computational complexity by searching a small subset of candidate points across three successive steps with decreasing step sizes.

```text
Three-Step Search Pattern Progression (Search Parameter p = 7):

Step 1 (S = 4):                 Step 2 (S = 2):                 Step 3 (S = 1):
o . . . o . . . o               . . . . . . . . .               . . . . . . . . .
. . . . . . . . .               . o . o . o . . .               . . . . . . . . .
. . . . . . . . .               . . . . . . . . .               . . o o o . . . .
. . . . . . . . .               . o . C . o . . .               . . o C o . . . .
o . . . C . . . o  =====>       . . . . . . . . .  =====>       . . o o o . . . .
. . . . . . . . .               . o . o . o . . .               . . . . . . . . .
. . . . . . . . .               . . . . . . . . .               . . . . . . . . .
. . . . . . . . .               . . . . . . . . .               . . . . . . . . .
o . . . o . . . o               . . . . . . . . .               . . . . . . . . .
```

#### Algorithmic Steps (for Search Parameter $`p = 7`$)
1. **Initialization:** Set initial search origin at center $(0,0)$ and initial step size $`S = \lfloor \frac{p+1}{2} \rfloor = 4`$.
2. **Step 1:**
   * Evaluate SAD at the center $(0,0)$ and 8 surrounding locations at distance $`\pm S`$: $`(0,0), (\pm 4, 0), (0, \pm 4), (\pm 4, \pm 4)`$ (Total 9 search points).
   * Find candidate point $`(dx_1, dy_1)`$ that yields minimum SAD. Set this point as the new search origin.
3. **Step 2:**
   * Halve the step size: $`S = \lfloor \frac{S}{2} \rfloor = 2`$.
   * Evaluate SAD at 8 surrounding locations at distance $`\pm 2`$ around the new origin $`(dx_1, dy_1)`$ (Total 8 new search points).
   * Find candidate point $`(dx_2, dy_2)`$ with minimum SAD. Set as new search origin.
4. **Step 3:**
   * Halve the step size: $`S = \lfloor \frac{S}{2} \rfloor = 1`$.
   * Evaluate SAD at 8 surrounding locations at distance $`\pm 1`$ around origin $`(dx_2, dy_2)`$ (Total 8 new search points).
   * The location with minimum SAD is the final Motion Vector $`\mathbf{v}^*`$.

#### Performance Analysis
* **Total Candidate Search Locations per Macroblock:**

```math
N_{\text{pts\_TSS}} = 9 + 8 + 8 = 25 \quad \text{points}
```

* **Computational Speedup Factor:**

```math
\text{Speedup} = \frac{N_{\text{pts\_FullSearch}}}{N_{\text{pts\_TSS}}} = \frac{225}{25} = 9\times
```

TSS reduces search computations by **$`88.89\%`$** while maintaining high motion tracking accuracy.

---

### 4.3 Two-Dimensional Logarithmic Search Method (2D-Log Search)

The 2D-Logarithmic Search algorithm is a fast pattern-based block matching technique that evaluates a cross-shaped pattern of 5 points in each iteration, moving the search center in the direction of decreasing distortion.

```text
2D-Logarithmic Search Pattern (Cross Pattern):

               (0, +S)
                  |
    (-S, 0) ---- (0,0) ---- (+S, 0)
                  |
               (0, -S)
```

#### Algorithmic Steps
1. **Initialization:** Set initial search origin at center $(0,0)$ and step size $`S`$ (typically $`S = 4`$ or $`S = 8`$).
2. **Iteration Phase:**
   * Evaluate SAD at 5 points forming a cross pattern: center $(0,0)$ and 4 orthogonal points at distance $`S`$: $`(0,0), (\pm S, 0), (0, \pm S)`$.
   * **Case A:** If the minimum SAD point is **not** the center, move search origin to the minimum SAD point and **keep the same step size $`S`$**. Repeat cross search.
   * **Case B:** If the minimum SAD point is **the center** (or if the search origin touches the search window boundary), **halve the step size:** $`S = \lfloor \frac{S}{2} \rfloor`$.
3. **Final Stage ($`S = 1`$):**
   * When step size reduces to $`S = 1`$, search all 9 locations (center + 8 surrounding pixels at distance 1) around the current origin.
   * Select candidate point with minimum SAD as the final Motion Vector.

---

### 4.4 Comprehensive Comparison of Block Matching Algorithms

| Feature / Metric | Full Search (ESBMA) | Three-Step Search (TSS) | 2D-Logarithmic Search |
| :--- | :--- | :--- | :--- |
| **Search Strategy** | Brute-force global scan | Coarse-to-fine step reduction | Directional cross-pattern tracking |
| **Search Points ($`p=7`$)**| $`225`$ points | $`25`$ points (Fixed) | $`13 - 21`$ points (Variable) |
| **Computational Speed**| Very Slow | $`9\times`$ faster than ESBMA | $`10\times - 15\times`$ faster |
| **Optimality** | Guarantees Global Minimum | Trapped in local minima | Trapped in local minima |
| **Hardware Overhead**| High parallel memory access | Simple deterministic control | Conditional branch overhead |
| **Best Application** | Offline reference encoding | Real-time video conferencing | Low-power video encoders |

---

## 5. Solved Worked Numericals

### Numerical 1: Motion Vector Determination and SAD / MAD Computation

#### Problem Statement
Given a $`3 \times 3`$ target macroblock in the current video frame $`f_k`$:

```math
C = \begin{bmatrix}
50 & 53 & 56 \\
51 & 54 & 58 \\
53 & 57 & 59
\end{bmatrix}
```

And two candidate reference macroblocks $`R_A`$ and $`R_B`$ in the reference frame $`f_{k-1}`$:

```math
R_A = \begin{bmatrix}
52 & 55 & 61 \\
54 & 59 & 62 \\
58 & 60 & 63
\end{bmatrix}, \quad
R_B = \begin{bmatrix}
51 & 54 & 58 \\
53 & 57 & 59 \\
55 & 58 & 61
\end{bmatrix}
```

The upper-left corner of current macroblock $`C`$ is at spatial coordinate $(24, 43)$.
Candidate block $`R_A`$ is located at $(24, 43)$ and candidate block $`R_B`$ is located at $(21, 40)$.

1. Calculate the Sum of Absolute Differences (SAD) and Mean Absolute Difference (MAD) for candidate blocks $`R_A`$ and $`R_B`$.
2. Determine which candidate block is the best match.
3. Calculate the resulting Motion Vector $`\mathbf{v}`$.

---

#### Step-by-Step Solution

##### Step 1: Compute SAD and MAD for Candidate Block $`R_A`$
Calculate absolute element-wise differences $`\lvert C(i,j) - R_A(i,j) \rvert`$:

```math
\lvert C - R_A \rvert = \begin{bmatrix}
\lvert 50-52 \rvert & \lvert 53-55 \rvert & \lvert 56-61 \rvert \\
\lvert 51-54 \rvert & \lvert 54-59 \rvert & \lvert 58-62 \rvert \\
\lvert 53-58 \rvert & \lvert 57-60 \rvert & \lvert 59-63 \rvert
\end{bmatrix} = \begin{bmatrix}
2 & 2 & 5 \\
3 & 5 & 4 \\
5 & 3 & 4
\end{bmatrix}
```

Summing all absolute difference terms:

```math
\text{SAD}(R_A) = (2 + 2 + 5) + (3 + 5 + 4) + (5 + 3 + 4) = 9 + 12 + 12 = \mathbf{33.0000}
```

Computing MAD ($`N^2 = 9`$ pixels):

```math
\text{MAD}(R_A) = \frac{33}{9} = \mathbf{3.6667}
```

---

##### Step 2: Compute SAD and MAD for Candidate Block $`R_B`$
Calculate absolute element-wise differences $`\lvert C(i,j) - R_B(i,j) \rvert`$:

```math
\lvert C - R_B \rvert = \begin{bmatrix}
\lvert 50-51 \rvert & \lvert 53-54 \rvert & \lvert 56-58 \rvert \\
\lvert 51-53 \rvert & \lvert 54-57 \rvert & \lvert 58-59 \rvert \\
\lvert 53-55 \rvert & \lvert 57-58 \rvert & \lvert 59-61 \rvert
\end{bmatrix} = \begin{bmatrix}
1 & 1 & 2 \\
2 & 3 & 1 \\
2 & 1 & 2
\end{bmatrix}
```

Summing all absolute difference terms:

```math
\text{SAD}(R_B) = (1 + 1 + 2) + (2 + 3 + 1) + (2 + 1 + 2) = 4 + 6 + 5 = \mathbf{13.0000}
```

Computing MAD ($`N^2 = 9`$ pixels):

```math
\text{MAD}(R_B) = \frac{13}{9} = \mathbf{1.4444}
```

---

##### Step 3: Select Best Matching Candidate
Comparing matching metrics:
* $\text{SAD}(R_A) = 33.0000$ vs. $\text{SAD}(R_B) = 13.0000$

Since $\text{SAD}(R_B) < \text{SAD}(R_A)$, candidate block **$`R_B`$ is the best matching block**.

---

##### Step 4: Calculate Motion Vector $`\mathbf{v}`$
The motion vector is defined as the spatial displacement from the current block origin to the reference block origin:

```math
\mathbf{v} = (dx, dy) = (x_{\text{ref}} - x_{\text{curr}}, y_{\text{ref}} - y_{\text{curr}})
```

* $x_{\text{curr}} = 24, y_{\text{curr}} = 43$
* $x_{\text{ref}} = 21, y_{\text{ref}} = 40$

```math
dx = 21 - 24 = -3, \quad dy = 40 - 43 = -3
```

#### Final Answer
* **Optimal Reference Block:** $R_B$ with $\text{SAD} = \mathbf{13.0000}$ and $\text{MAD} = \mathbf{1.4444}$.
* **Motion Vector:** $\mathbf{v} = \mathbf{(-3, -3)}$.

---

### Numerical 2: Search Point Computational Complexity Analysis

#### Problem Statement
A CIF video sequence has a spatial resolution of $`352 \times 288`$ pixels per frame operating at $`30`$ frames/sec.
The motion estimation process uses $`16 \times 16`$ macroblocks and a search displacement range of $`p = 7`$ pixels.

1. Calculate the total number of macroblocks per video frame.
2. Calculate the total number of search point evaluations required per frame using Full Search (ESBMA).
3. Calculate the total number of search point evaluations required per frame using Three-Step Search (TSS).
4. Compute the computational reduction factor achieved by TSS over ESBMA.

---

#### Step-by-Step Solution

##### Step 1: Calculate Total Macroblocks per Frame ($`N_{\text{MB}}`$)
* Frame width = $352$ pixels, Macroblock width = $16$ pixels $\implies \frac{352}{16} = 22$ macroblocks horizontally.
* Frame height = $288$ pixels, Macroblock height = $16$ pixels $\implies \frac{288}{16} = 18$ macroblocks vertically.

```math
N_{\text{MB}} = 22 \times 18 = \mathbf{396 \quad \text{macroblocks per frame}}
```

---

##### Step 2: Compute Total Search Points for Full Search (ESBMA)
For search parameter $`p = 7`$, search points per macroblock:

```math
N_{\text{pts\_Full}} = (2p + 1)^2 = (2(7) + 1)^2 = 15^2 = \mathbf{225 \quad \text{points/MB}}
```

Total search evaluations per frame:

```math
\text{Total Points}_{\text{Full}} = 396 \times 225 = \mathbf{89,100 \quad \text{evaluations/frame}}
```

Per second processing requirement (at 30 fps): $89,100 \times 30 = \mathbf{2,673,000 \quad \text{evaluations/sec}}$.

---

##### Step 3: Compute Total Search Points for Three-Step Search (TSS)
For $`p = 7`$, TSS evaluates $`9 + 8 + 8 = 25`$ search points per macroblock.

Total search evaluations per frame:

```math
\text{Total Points}_{\text{TSS}} = 396 \times 25 = \mathbf{9,900 \quad \text{evaluations/frame}}
```

Per second processing requirement (at 30 fps): $9,900 \times 30 = \mathbf{297,000 \quad \text{evaluations/sec}}$.

---

##### Step 4: Compute Computational Reduction Factor
Comparing total search evaluations:

```math
\text{Reduction Factor} = \frac{\text{Total Points}_{\text{Full}}}{\text{Total Points}_{\text{TSS}}} = \frac{89,100}{9,900} = \mathbf{9.0000\times}
```

#### Final Answer
* **Macroblocks per Frame:** $396$
* **ESBMA Evaluations/Frame:** $89,100$
* **TSS Evaluations/Frame:** $9,900$
* **Computational Speedup:** $\mathbf{9.0000\times}$ computational workload reduction.

---

## 6. Term-End Exam High-Yield Summary & Formula Cheat Sheet

### 6.1 Fast Block Matching Algorithm Quick Reference

| Algorithm | Search Pattern | Initial Step Size ($`p=7`$) | Formula for Search Points |
| :--- | :--- | :--- | :--- |
| **Exhaustive Search (ESBMA)**| Full rectangular grid | $`1`$ pixel step everywhere | $`N_{\text{pts}} = (2p + 1)^2`$ |
| **Three-Step Search (TSS)** | 9-point square grid | $`S = \lfloor (p+1)/2 \rfloor = 4`$ | $`N_{\text{pts}} = 1 + 8 \log_2(p + 1)`$ |
| **2D-Logarithmic Search** | 5-point cross pattern | $`S = 4`$ or $`S = 8`$ | $`N_{\text{pts}} = 2 + 3 n_{\text{steps}} + 8`$ |

---

### 6.2 Essential Formula Cheat Sheet

1. **Uncompressed Bit Rate**:

```math
R = M \times N \times B \times f_s
```

2. **Sum of Absolute Differences (SAD)**:

```math
\text{SAD}(dx, dy) = \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i+dx, j+dy) \rvert
```

3. **Mean Absolute Difference (MAD)**:

```math
\text{MAD}(dx, dy) = \frac{1}{N^2} \text{SAD}(dx, dy)
```

4. **Mean Squared Error (MSE)**:

```math
\text{MSE}(dx, dy) = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \left( C(i,j) - R(i+dx, j+dy) \right)^2
```

5. **Peak Signal-to-Noise Ratio (PSNR)**:

```math
\text{PSNR} = 10 \log_{10} \left( \frac{255^2}{\text{MSE}} \right)
```

6. **Motion Vector Calculation**:

```math
\mathbf{v} = (dx, dy) = (x_{\text{ref}} - x_{\text{curr}}, y_{\text{ref}} - y_{\text{curr}})
```

7. **ESBMA Total Search Points**:

```math
N_{\text{pts\_ESBMA}} = (2p + 1)^2
```
