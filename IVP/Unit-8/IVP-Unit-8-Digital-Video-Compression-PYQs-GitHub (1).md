# Unit 8: Digital Video Compression — Past Year Questions (PYQs) & Exam Solutions

---

## 1. Overview of Unit 8 Syllabus and Exam Weightage

Unit 8 covers the Fundamentals of Digital Video and Its Compression. Topics include video representation, temporal correlation, frame classifications (I, P, and B frames), bitstream reordering, motion estimation metrics (SAD, MAD, MSE), block matching algorithms (Exhaustive Search, Three-Step Search, 2D-Logarithmic Search), and video encoder/decoder architectures.

* **Course Outcome Mapping:** CO5 — Explain video representation concepts and motion estimation techniques used in digital video compression.
* **Exam Distribution & Weightage:** Unit 8 carries approximately 15–20% of the total marks in Continuous Assessments (CA) and Semester Term-End Examinations (TEE). Questions consist of theoretical comparisons (I vs P vs B frames), algorithm step-by-step breakdowns, block diagrams, and numerical calculations.

---

## 2. PYQ 1: Exhaustive Search Block Matching Algorithm (ESBMA / Full Search)

### Exam Context

* **Marks:** 10 Marks / 8 Marks
* **Repeated In:** Semester V Final Exam 2025–2026 Q7(a), Batch 2024–2025 Final Exam Q4(a), Re-Exam 2024–2025 Q4(a), Special Re-Exam 2022–2023 Q5(b).

### Question Statement

Explain the Exhaustive Search Block Matching Algorithm (ESBMA) for motion estimation in video processing. Discuss its operational steps, mathematical formulation, search window bounds, and evaluate its advantages and disadvantages.

---

### Step-by-Step Solution

#### 1. Concept and Principle

The Exhaustive Search Block Matching Algorithm (also known as Full Search) is the most straightforward motion estimation technique. It compares a candidate macroblock of size $N imes N$ (typically $16 imes 16$) in the current frame $`f_t`$ against **every possible overlapping candidate location** within a predefined search area $S$ in the reference frame $`f_{t-1}`$.

```text
Reference Frame (f_{t-1})                 Current Frame (f_t)
+-------------------------+               +-------------------------+
|                         |               |                         |
|     +---------------+   |               |     +-------+           |
|     | Search Area   |   |               |     | Current           |
|     | (2p+1)x(2p+1) |   |               |     | Macroblock        |
|     |   +---+       |   |               |     |  NxN  |           |
|     |   |NxN|       |   |               |     +-------+           |
|     |   +---+       |   |               |                         |
|     +---------------+   |               |                         |
+-------------------------+               +-------------------------+
```

#### 2. Mathematical Formulation

For a maximum allowable displacement search parameter $p$, the displacement offsets $(dx, dy)$ are tested over the range:

```math
-p \le dx \le +p, \quad -p \le dy \le +p
```

The matching error is evaluated using the Sum of Absolute Differences (SAD):

```math
ext{SAD}(dx, dy) = \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert f_t(x+i, y+j) - f_{t-1}(x+dx+i, y+dy+j)\vert
```

The optimal motion vector $`(dx^*, dy^*)`$ corresponds to the displacement that minimizes the cost function:

```math
(dx^*, dy^*) = \arg\min_{-p \le dx, dy \le +p} ext{SAD}(dx, dy)
```

#### 3. Operational Steps for Exam Answer

1. **Macroblock Partitioning:** Divide the current frame $`f_t`$ into non-overlapping macroblocks of size $N imes N$ (usually $16 imes 16$).
2. **Define Search Window:** For a macroblock centered at $(x,y)$ in $`f_t`$, define a search region of size $(2p+N) imes (2p+N)$ centered at $(x,y)$ in reference frame $`f_{t-1}`$.
3. **Exhaustive Evaluation:** Compute SAD for all $`(2p+1)^2`$ possible candidate displacement vectors $(dx, dy)$.
4. **Motion Vector Selection:** Select the displacement $`(dx^*, dy^*)`$ that yields the minimum SAD value.
5. **Residual Computation:** Compute the prediction error residual matrix $`e(i,j) = f_t(x+i, y+j) - f_{t-1}(x+dx^*+i, y+dy^*+j)`$ for transform coding.

#### 4. Total Search Candidate Calculation (For $p = 7$)

For a standard search displacement parameter $p = 7$:

```math
N_{ext{candidates}} = (2p + 1)^2 = (2(7) + 1)^2 = 15^2 = 225 ext{ positions}
```

#### 5. Advantages and Disadvantages

| Feature Dimension | Exhaustive Search (Full Search) |
| :--- | :--- |
| **Optimality** | Guaranteed to find the global minimum error prediction block within the search window. |
| **Accuracy** | Highest achievable motion compensation accuracy and lowest residual energy. |
| **Implementation** | Extremely simple, highly regular memory access pattern; suitable for VLSI hardware design. |
| **Computational Overhead** | Extremely high complexity; requires $`(2p+1)^2`$ SAD evaluations per macroblock. |
| **Real-time Viability** | Computationally prohibitive for high-resolution software video encoders without specialized hardware acceleration. |

---

## 3. PYQ 2: Three-Step Search Algorithm (TSS / 3SS)

### Exam Context

* **Marks:** 10 Marks / 8 Marks
* **Repeated In:** Semester V Final Exam 2025–2026 Q4(c), Batch 2024–2025 Final Exam Q7(a), Re-Exam 2022–2023 Q2(b).

### Question Statement

Discuss the Three-Step Search (TSS) algorithm for motion estimation. Explain step-by-step how it operates, provide an ASCII search pattern diagram for search parameter $p = 7$, and explain how it balances accuracy and computational efficiency in video compression.

---

### Step-by-Step Solution

#### 1. Concept and Principle

The Three-Step Search (TSS) algorithm is a fast coarse-to-fine block matching algorithm. Instead of testing every position inside the $(2p+1) imes (2p+1)$ search window, TSS evaluates a sparse $3 imes 3$ grid of 9 candidate locations around the search center. At each step, the step size $S$ is halved, progressively narrowing down the search around the best match found in the previous step.

#### 2. Algorithm Step Breakdown (For $p = 7$)

* **Initial Parameter Setup:** Initial step size is set to $S = \lceil p/2 
ceil = 4$.

```text
TSS Algorithm Search Pattern (p = 7, Initial S = 4):

Step 1 (S = 4):
         O . . . O . . . O    (9 locations evaluated around origin (0,0))
         . . . . . . . . .
         . . . . . . . . .
         . . . . . . . . .
         O . . . C . . . O
         . . . . . . . . .
         . . . . . . . . .
         . . . . . . . . .
         O . . . O . . . O

Step 2 (S = 2):
         Move center to best match of Step 1.
         Test 8 surrounding locations at distance S = 2.

Step 3 (S = 1):
         Move center to best match of Step 2.
         Test 8 surrounding locations at distance S = 1.
         The location with minimum SAD yields final Motion Vector.
```

#### 3. Step-by-Step Execution Rules

1. **Step 1 ($S = 4$):** Set search origin at $(0,0)$. Evaluate SAD at the center $(0,0)$ and 8 surrounding locations at distance $`\pm S = \pm 4`$ along horizontal, \vertical, and diagonal axes (total 9 candidate blocks). Pick the location with minimum SAD as the new center.
2. **Step 2 ($S = 2$):** Set step size to $S = S / 2 = 2$. Evaluate SAD at 8 surrounding locations at distance $`\pm 2`$ around the new center. Pick the location with minimum SAD as the updated center.
3. **Step 3 ($S = 1$):** Set step size to $S = S / 2 = 1$. Evaluate SAD at 8 surrounding locations at distance $`\pm 1`$ around the updated center.
4. **Final Motion Vector Selection:** The location with the minimum SAD in Step 3 specifies the final motion vector $`(dx^*, dy^*)`$.

#### 4. Computational Efficiency Comparison (TSS vs. Full Search)

For search parameter $p = 7$:
* **Exhaustive Search Points:**

```math
N_{ext{ESBMA}} = (2(7) + 1)^2 = 225 ext{ points}
```

* **Three-Step Search Points:**
  * Step 1 ($S = 4$): $`1 ext{ (center)} + 8 = 9 ext{ points}`$
  * Step 2 ($S = 2$): $`8 ext{ points}`$
  * Step 3 ($S = 1$): $`8 ext{ points}`$

```math
N_{ext{TSS}} = 9 + 8 + 8 = 25 ext{ points}
```

* **Computational Speedup Factor:**

```math
ext{Speedup Factor} = \frac{N_{ext{ESBMA}}}{N_{ext{TSS}}} = \frac{225}{25} = 9imes ext{ reduction in SAD calculations}
```

#### 5. Accuracy vs. Efficiency Trade-off Analysis

* **Computational Savings:** Reduces candidate evaluations by $`88.89\%`$, significantly cutting encoder processing latency and memory bandwidth requirements.
* **Limitation (Local Minima Trap):** TSS assumes that error increases monotonically away from the global minimum. In fast, complex, or non-rigid motion, TSS can become trapped in a local minimum during Step 1, producing a suboptimal motion vector.

---

## 4. PYQ 3: Comparative Analysis of I, P, and B Video Frames

### Exam Context

* **Marks:** 10 Marks / 5 Marks / 4 Marks
* **Repeated In:** Batch 2024–2025 Final Exam Q3(b), Re-Exam 2022–2023 Q1(d), Special Re-Exam 2022–2023 Q5(a), Re-Exam 2023–2024 Q5(a).

### Question Statement

Explain the key differences between I-frames, P-frames, and B-frames. Why are I-frames required in video compression? Justify why P-frames provide higher compression than I-frames but lower than B-frames, and explain why B-frames are the least reliable.

---

### Step-by-Step Solution

#### 1. Definitions and Frame Types

```text
Inter-Frame Prediction & Dependency Structure:

       I1 --------------> P4 --------------> P7 --------------> I10
        \                /  \                /  \                /
         +---> B2 <-----+    +---> B5 <-----+    +---> B8 <-----+
         |              |    |              |    |              |
         +---> B3 <-----+    +---> B6 <-----+    +---> B9 <-----+

  Key:
  ---> Denotes Motion Compensated Prediction Dependency
```

* **I-Frames (Intra-Coded Frames):** Self-contained images coded using only intra-frame spatial compression (like JPEG). They do not reference any other video frames.
* **P-Frames (Predictive-Coded Frames):** Coded using forward inter-frame prediction from a previous reference frame (which can be an I-frame or a P-frame).
* **B-Frames (Bidirectionally Predictive-Coded Frames):** Coded using bidirectional temporal interpolation from both a past reference frame and a future reference frame.

#### 2. Comprehensive Comparison Matrix

| Property / Parameter | I-Frame (Intra) | P-Frame (Predictive) | B-Frame (Bidirectional) |
| :--- | :--- | :--- | :--- |
| **Reference Dependency** | None (Self-contained) | Past reference frame (I or P) | Past AND future reference frames |
| **Compression Ratio** | Lowest ($1imes$ baseline, e.g., $10:1$ to $20:1$) | Moderate ($3imes$ to $5imes$ higher than I-frame) | Highest ($10imes$ to $20imes$ higher than I-frame) |
| **Relative File Size** | Largest | Medium | Smallest |
| **Random Access Point** | Yes (Entry point for seeking) | No | No |
| **Error Propagation** | Stops error propagation completely | Propagates errors to dependent P/B frames | No error propagation (never used as reference) |
| **Decoding Complexity** | Low | Medium | High (Requires frame reordering memory buffer) |

#### 3. Answers to Specific Justification Questions

##### Why are I-Frames Required?

1. **Random Access & Seeking:** Allows users to jump/seek to specific timestamps in a video stream without decoding from the very beginning.
2. **Channel Switching & Streaming:** Enables rapid tuning in digital TV broadcasts and network video streaming.
3. **Error Recovery / Refresh:** Erases accumulated transmission errors or drift caused by lossy wireless networks, resetting the reference frame buffer.

##### Why P-Frames Provide More Compression than I-Frames but Less than B-Frames?

* **P vs. I:** P-frames exploit temporal redundancy by transmitting only residual error matrices and motion vectors rather than full pixel grids, making them significantly smaller than self-contained I-frames.
* **P vs. B:** P-frames use only unidirectional (past) prediction. B-frames use bidirectional prediction, averaging past and future reference blocks, which yields smaller prediction residual energy and uses fewer bits.

##### Why B-Frames are Least Reliable?

B-frames depend on **two** distinct reference frames (one past, one future). If *either* reference frame suffers packet loss or corruption during network transmission, the B-frame cannot be correctly reconstructed. Furthermore, because B-frames require future reference frames to be decoded first, they introduce encoding/decoding frame delay.

---

## 5. PYQ 4: 2D-Logarithmic Search Method (2D-Log Search)

### Exam Context

* **Marks:** 10 Marks / 8 Marks
* **Repeated In:** Semester V Final Exam 2022–2023 Q3(a), Re-Exam 2023–2024 Q5(b), Batch 2023–2024 Re-Exam Q5(b).

### Question Statement

Illustrate the 2D-Logarithmic Search algorithm for motion estimation. Explain its working steps, step-size reduction rules, and search pattern layout.

---

### Step-by-Step Solution

#### 1. Concept and Principle

The 2D-Logarithmic Search algorithm is a fast block matching technique that tracks motion along the horizontal and \vertical axes using a cross-shaped 5-point search pattern. It relies on logarithmic step-size reduction ($S = S / 2$) whenever the center point yields the minimum error, or moves the pattern center to the best matching location.

#### 2. Search Pattern Layout

```text
2D-Log Search Cross-Pattern Layout:

                 . . . O . . .        (Top: (0, +S))
                 . . . . . . .
                 . . . . . . .
         O . . . C . . . O            (Left: (-S, 0), Center: (0,0), Right: (+S, 0))
                 . . . . . . .
                 . . . . . . .
                 . . . O . . .        (Bottom: (0, -S))
```

#### 3. Algorithmic Workflow Steps

1. **Initialization:** Choose initial step size $`S = 2^{k-1}`$ for maximum displacement $p$ (e.g., $S = 4$ for $p = 7$). Set initial search center at $(0,0)$.
2. **5-Point Evaluation:** Evaluate SAD at 5 locations forming a cross centered at current origin $`(x_c, y_c)`$:

```math
\{(x_c, y_c), (x_c \pm S, y_c), (x_c, y_c \pm S)\}
```

3. **Center Update / Step Reduction Rules:**
   * **Rule A (Off-Center Match):** If one of the 4 outer points yields the minimum SAD, move the search origin $`(x_c, y_c)`$ to that location. Keep step size $S$ unchanged and repeat 5-point evaluation around the new center.
   * **Rule B (Center Match):** If the center point $`(x_c, y_c)`$ yields the minimum SAD, reduce step size by half: $S = S / 2$.
4. **Final Refinement ($S = 1$):** When step size reaches $S = 1$, evaluate all 8 surrounding locations around the current center (9 points total). The location with the absolute minimum SAD gives the final motion vector $`(dx^*, dy^*)`$.

#### 4. Comparison of Search Patterns (TSS vs. 2D-Log Search)

| Feature Parameter | Three-Step Search (TSS) | 2D-Logarithmic Search |
| :--- | :--- | :--- |
| **Grid Pattern Shape** | $3 imes 3$ square box pattern (9 points per step) | Cross-shaped pattern (5 points per step) |
| **Step-Size Reduction** | Fixed 3-step execution ($S=4 o 2 o 1$) | Dynamic step reduction ($S = S/2$ only when center wins) |
| **Total Evaluations** | Fixed 25 search locations | Variable (typically 13 to 21 locations) |
| **Performance in Directional Motion** | Rigid grid search | More adaptive along principal horizontal/\vertical motion axes |

---

## 6. PYQ 5: Bitstream Reordering & GOP Frame Display Order vs. Encoding Order

### Exam Context

* **Marks:** 4 Marks / 8 Marks
* **Repeated In:** Re-Exam 2023–2024 / 22–23 Q5(a), Video Processing Course Module.

### Question Statement

For a video signal, consider the following sequence of 13 frames in **display order**:

```text
I1  B2  B3  P4  B5  B6  P7  B8  B9  P10  B11  B12  I13
 1   2   3   4   5   6   7   8   9   10   11   12   13
```

Reorder the sequence to show the **bitstream transmission / encoding order** required to achieve motion compensation decoding. Explain why frame reordering is mandatory.

---

### Step-by-Step Solution

#### 1. Why Bitstream Reordering is Mandatory

B-frames require bidirectional temporal prediction from both a **past** reference frame and a **future** reference frame. A decoder cannot decode a B-frame until both of its reference frames are already decoded and present in memory. 

For example, $`B_2`$ and $`B_3`$ depend on past frame $`I_1`$ and future frame $`P_4`$. Therefore, future frame $`P_4`$ **must be transmitted and decoded before** $`B_2`$ and $`B_3`$ can be processed.

#### 2. Frame Dependency Analysis

* $`I_1`$: Decoded independently.
* $`P_4`$: Predicted forward from $`I_1`$. Must be decoded 2nd so it can act as future reference for $`B_2, B_3`$.
* $`B_2, B_3`$: Predicted bidirectionally from $`I_1`$ and $`P_4`$. Decoded 3rd and 4th.
* $`P_7`$: Predicted forward from $`P_4`$. Must be decoded 5th so it can act as future reference for $`B_5, B_6`$.
* $`B_5, B_6`$: Predicted bidirectionally from $`P_4`$ and $`P_7`$. Decoded 6th and 7th.
* $`P_{10}`$: Predicted forward from $`P_7`$. Decoded 8th.
* $`B_8, B_9`$: Predicted bidirectionally from $`P_7`$ and $`P_{10}`$. Decoded 9th and 10th.
* $`I_{13}`$: Decoded 11th (acts as future reference for $`B_{11}, B_{12}`$).
* $`B_{11}, B_{12}`$: Decoded 12th and 13th.

#### 3. Display Order vs. Bitstream Order Table

```text
Display Order (Order of presentation to viewer):
Index:    1    2    3    4    5    6    7    8    9   10   11   12   13
Type:    I1   B2   B3   P4   B5   B6   P7   B8   B9  P10  B11  B12  I13

Bitstream / Transmission Order (Order sent over network & decoded):
Index:    1    4    2    3    7    5    6   10    8    9   13   11   12
Type:    I1   P4   B2   B3   P7   B5   B6  P10   B8   B9  I13  B11  B12
```

---

## 7. PYQ 6: Motion Vectors & Error Evaluation Metrics (SAD, MAD, MSE, PSNR)

### Exam Context

* **Marks:** 10 Marks
* **Repeated In:** Semester V Final Exam 2022–2023 Q2(a), Batch 2024–2025 Final Exam Q4(a).

### Question Statement

Explain the concept of motion vectors in video block matching. Define the mathematical formulas for Sum of Absolute Differences (SAD), Mean Absolute Difference (MAD), Mean Squared Error (MSE), and Peak Signal-to-Noise Ratio (PSNR). Given a target macroblock and two candidate reference blocks, calculate SAD and MAD to select the optimal motion vector.

---

### Step-by-Step Solution

#### 1. Mathematical Definitions of Matching Error Metrics

For a target macroblock $C(i,j)$ of size $N imes N$ and a candidate reference block $R(i,j)$:

1. **Sum of Absolute Differences (SAD):**

```math
ext{SAD} = \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i,j)\vert
```

2. **Mean Absolute Difference (MAD):**

```math
ext{MAD} = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i,j)\vert = \frac{ext{SAD}}{N^2}
```

3. **Mean Squared Error (MSE):**

```math
ext{MSE} = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} [C(i,j) - R(i,j)]^2
```

4. **Peak Signal-to-Noise Ratio (PSNR):**

```math
ext{PSNR} = 10 \log_{10} \left( \frac{ext{Peak}^2}{ext{MSE}}\right) = 10 \log_{10} \left( \frac{255^2}{ext{MSE}}\right) \quad ext{dB}
```

---

#### 2. Worked Numerical Example

##### Problem Statement

A $3 imes 3$ current macroblock $C$ is given below:

```math
C = \begin{bmatrix}
10 & 12 & 15 \\
14 & 15 & 18 \\
12 & 14 & 16 \end{bmatrix}
```

Two candidate reference macroblocks $`R_A`$ and $`R_B`$ in the previous frame are:

```math
R_A = \begin{bmatrix}
12 & 10 & 10 \\
11 & 10 & 14 \\
7 & 11 & 12 \end{bmatrix}, \quad
R_B = \begin{bmatrix}
9 & 11 & 13 \\
12 & 12 & 17 \\
10 & 13 & 14 \end{bmatrix}
```

Determine which candidate block provides the best motion vector match using SAD and MAD criteria.

---

##### Step-by-Step Calculation

###### Candidate Block $`R_A`$ Evaluation:

* Absolute Difference Matrix $`\lvert C - R_A \vert`$:

```math
\lvert C - R_A\vert = \begin{bmatrix}
\lvert 10-12\vert & \lvert 12-10\vert & \lvert 15-10\vert \\
\lvert 14-11\vert & \lvert 15-10\vert & \lvert 18-14\vert \\
\lvert 12-7\vert & \lvert 14-11\vert & \lvert 16-12\vert \end{bmatrix} = \begin{bmatrix}
2 & 2 & 5 \\
3 & 5 & 4 \\
5 & 3 & 4 \end{bmatrix}
```

* **Compute $`ext{SAD}(R_A)`$:**

```math
ext{SAD}(R_A) = (2 + 2 + 5) + (3 + 5 + 4) + (5 + 3 + 4) = 9 + 12 + 12 = \mathbf{33.0000}
```

* **Compute $`ext{MAD}(R_A)`$:** (where $`N^2 = 9`$)

```math
ext{MAD}(R_A) = \frac{33}{9} = \mathbf{3.6667}
```

---

###### Candidate Block $`R_B`$ Evaluation:

* Absolute Difference Matrix $`\lvert C - R_B \vert`$:

```math
\lvert C - R_B\vert = \begin{bmatrix}
\lvert 10-9\vert & \lvert 12-11\vert & \lvert 15-13\vert \\
\lvert 14-12\vert & \lvert 15-12\vert & \lvert 18-17\vert \\
\lvert 12-10\vert & \lvert 14-13\vert & \lvert 16-14\vert \end{bmatrix} = \begin{bmatrix}
1 & 1 & 2 \\
2 & 3 & 1 \\
2 & 1 & 2 \end{bmatrix}
```

* **Compute $`ext{SAD}(R_B)`$:**

```math
ext{SAD}(R_B) = (1 + 1 + 2) + (2 + 3 + 1) + (2 + 1 + 2) = 4 + 6 + 5 = \mathbf{13.0000}
```

* **Compute $`ext{MAD}(R_B)`$:**

```math
ext{MAD}(R_B) = \frac{13}{9} = \mathbf{1.4444}
```

---

##### Final Decision

Since $`ext{SAD}(R_B) = 13.0000 < ext{SAD}(R_A) = 33.0000`$ (and $`ext{MAD}(R_B) = 1.4444 < ext{MAD}(R_A) = 3.6667`$), **Candidate Block $`R_B`$ is selected as the optimal matching block**.

---

## 8. PYQ 7: Motion-Compensated Video Encoder & Decoder Architecture

### Exam Context

* **Marks:** 8 Marks / 4 Marks
* **Repeated In:** Re-Exam 2023–2024 / 22–23 Q6(a), Textbook Problem 8.27.

### Question Statement

Draw and explain the block diagram of a typical motion-compensated video encoder and its companion video decoder.

---

### Step-by-Step Solution

#### 1. Motion-Compensated Video Encoder Block Diagram

```text
Motion-Compensated Video Encoder Architecture:

Current Frame f_t
     |
     v      +---+ Prediction Error e_t
 ----(+)--->|DCT|------------->[Quantizer]----->[Entropy Coding]----> Bitstream
      ^     +---+                  |                    |
      |                            v                    v
  Prediction                  [Inverse Quant]     [Rate Control]
  Macroblock                       |
      |                            v
      |                       [Inverse DCT]
      |                            |
      |                            v
      |                         [ + ] <--- Reconstruction
      |                            |
      |                            v
      |                     [Frame Store / Memory]
      |                            |
      +--- [Motion Estimator] <----+ (Reference Frame f_{t-1})
                 ^
                 | (Motion Vectors)
                 +-------------------------------------> (To Bitstream)
```

#### 2. Key Components of Encoder

1. **Motion Estimator & Compensator:** Compares current macroblock with reference frame stored in memory to compute motion vectors $(dx, dy)$ and form prediction block $`\hat{f}_t`$.
2. **Difference Junction (+/-):** Subtracts predicted macroblock $`\hat{f}_t`$ from current macroblock $`f_t`$ to create prediction residual $`e_t`$.
3. **DCT Mapper & Quantizer:** Transforms spatial residual block to frequency domain and quantizes high-frequency coefficients to achieve compression.
4. **Decoder Reconstruction Loop (Inverse Quant/DCT):** Reconstructs reference frame locally inside encoder to prevent drift between encoder and decoder reference buffers.

#### 3. Motion-Compensated Video Decoder Block Diagram

```text
Motion-Compensated Video Decoder Architecture:

Compressed
Bitstream ---->[Entropy Decoder]----+---> Quantized Coefficients --->[Inverse Quant/DCT]----+
                                    |                                                        |
                                    v                                                        v
                             [Motion Vectors]                                             [ + ] ---> Reconstructed
                                    |                                                        ^       Video Frame
                                    v                                                        |
                         [Motion Compensator] -----------------------------------------------+
                                    ^
                                    |
                           [Frame Store Memory]
```

---

## 9. PYQ 8: Solved Numerical on Video Memory & Storage Computation

### Exam Context

* **Marks:** 5 Marks / 8 Marks
* **Repeated In:** Special Re-Exam 2022–2023 Q6(c).

### Question Statement

Compute the memory (in bits and megabytes) required to store an uncompressed video signal of 30 seconds duration, running at a frame rate of 30 frames per second. Each frame of the video is an 8-bit monochrome image of resolution $256 imes 256$ pixels. If each frame of the video is subsequently con\verted to a 4-bit image, calculate the total storage space saved.

---

### Step-by-Step Solution

#### Step 1: Calculate Total Number of Frames

* Video Duration $`T = 30 ext{ seconds}`$
* Frame Rate $`R = 30 ext{ frames/second}`$

```math
ext{Total Frames } (N_{ext{frames}}) = T imes R = 30 imes 30 = \mathbf{900 ext{ frames}}
```

#### Step 2: Compute Storage for 8-Bit Video

* Frame Resolution = $`256 imes 256 ext{ pixels}`$
* Bits per Pixel (bpp) = $`8 ext{ bits}`$

```math
ext{Bits per Frame} = 256 imes 256 imes 8 = 524,288 ext{ bits}
```

```math
ext{Total Bits (8-bit)} = 900 imes 524,288 = \mathbf{471,859,200 ext{ bits}}
```

* Con\vert to Megabytes (MB): (Dividing by $8 imes 1024 imes 1024$)

```math
ext{Total Storage (8-bit)} = \frac{471,859,200}{8 imes 1024 imes 1024} = \frac{471,859,200}{8,388,608} = \mathbf{56.2500 ext{ MB}}
```

#### Step 3: Compute Storage for 4-Bit Video

* Bits per Pixel (bpp) = $`4 ext{ bits}`$

```math
ext{Bits per Frame} = 256 imes 256 imes 4 = 262,144 ext{ bits}
```

```math
ext{Total Bits (4-bit)} = 900 imes 262,144 = \mathbf{235,929,600 ext{ bits}}
```

```math
ext{Total Storage (4-bit)} = \frac{235,929,600}{8,388,608} = \mathbf{28.1250 ext{ MB}}
```

#### Step 4: Calculate Storage Space Saved

* Storage Saved in Bits:

```math
ext{Bits Saved} = 471,859,200 - 235,929,600 = \mathbf{235,929,600 ext{ bits}}
```

* Storage Saved in Megabytes:

```math
ext{MB Saved} = 56.2500 - 28.1250 = \mathbf{28.1250 ext{ MB}} \quad (50.0000\% ext{ reduction})
```

---

## 10. Summary Cheat Sheet for Unit 8 PYQ Preparation

| Topic / Concept | Essential Formula / Key Rule | Quick Exam Tip |
| :--- | :--- | :--- |
| **Search Window Size** | Area $= (2p+1) imes (2p+1)$ | For $p=7$, area is $15 imes 15 = 225$ blocks. |
| **ESBMA Complexity** | $`N_{ext{eval}} = (2p+1)^2`$ | Gives global minimum error, but takes 225 evaluations. |
| **TSS Complexity** | $`N_{ext{eval}} = 9 + 8 + 8 = 25`$` | `$9imes$ computational speedup over Full Search. |
| **SAD Formula** | $`\sum \lvert C(i,j) - R(i,j) \vert`$ | No multiplications needed; faster than MSE. |
| **MAD Formula** | $`\frac{1}{N^2} ext{SAD}`$` | Divide SAD by macroblock pixel count `$`N^2`$. |
| **Bitstream Order** | Decodes $I$ & $P$ before dependent $B$ frames | Display: `I1 B2 B3 P4` $o$ Bitstream: `I1 P4 B2 B3`. |
