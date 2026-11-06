# Unit 8: Fundamentals of Digital Video and Its Compression — Solved Numericals & Exam Guide

## 1. Overview of Unit 8 Numerical Types & Formula Cheat Sheet

Unit 8 numerical problems in Image and Video Processing (IVP) evaluate macroblock-based motion estimation, error metrics, search algorithm computational complexity, motion vector determination, and video data rate / storage requirements.

---

### 1.1 Summary Formula Cheat Sheet

#### 1. Macroblock Error Metrics (for $N \times N$ Macroblocks)

* **Sum of Absolute Differences (SAD):**

```math

\text{SAD}(dx, dy) = \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i+dx, j+dy) \rvert

```

* **Mean Absolute Difference (MAD):**

```math

\text{MAD}(dx, dy) = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \lvert C(i,j) - R(i+dx, j+dy) \rvert = \frac{\text{SAD}(dx, dy)}{N^2}

```

* **Mean Squared Error (MSE):**

```math

\text{MSE}(dx, dy) = \frac{1}{N^2} \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} \left[ C(i,j) - R(i+dx, j+dy) \right]^2

```

* **Peak Signal-to-Noise Ratio (PSNR):**

```math

\text{PSNR} = 10 \log_{10} \left( \frac{\text{Peak}^2}{\text{MSE}} \right) = 10 \log_{10} \left( \frac{255^2}{\text{MSE}} \right) \quad \text{dB}

```

#### 2. Search Point Complexity & Speedup

* **Exhaustive Search (Full Search / ESBMA) Candidate Points:**

```math

N_{\text{ESBMA}} = (2p + 1)^2

```

*(Where $p$ is the maximum search displacement parameter)*
* **Three-Step Search (TSS) Candidate Points:**

```math

N_{\text{TSS}} = 9 + 8 + 8 = 25 \quad \text{search points (for } p = 7\text{)}

```

* **Computational Speedup Factor:**

```math

\text{Speedup} = \frac{N_{\text{ESBMA}}}{N_{\text{TSS}}} = \frac{(2p+1)^2}{25}

```

#### 3. Video Data Storage & Bit-Rate

* **Uncompressed Frame Size (Bits):**

```math

\text{Bits per Frame} = M \times N \times b

```

*(Where $M \times N$ is frame resolution and $b$ is bit depth per pixel)*
* **Total Video File Size (Bits & Megabytes):**

```math

\text{Total Bits} = T \times R \times M \times N \times b

```

```math

\text{Total Storage (MB)} = \frac{\text{Total Bits}}{8 \times 1024 \times 1024} = \frac{\text{Total Bits}}{8,388,608}

```

---

## 2. Numerical Type 1: Macroblock Error Metric Evaluation (SAD, MAD, MSE, PSNR)

### Exam Context

* **Marks:** 8 Marks / 10 Marks
* **Repeated In:** Mid-Sem 2025–2026, Re-Exam 2023–2024, Textbook Problem 8.25.

---

### Problem Statement

A $3 \times 3$ macroblock $C$ in the current frame $f_t$ and two candidate reference blocks $R_A$ and $R_B$ in the reference frame $f_{t-1}$ are given below:

```math

C = \begin{bmatrix}
10 & 12 & 15 \\
14 & 15 & 18 \\
12 & 14 & 16
\end{bmatrix}

```

```math

R_A = \begin{bmatrix}
12 & 10 & 10 \\
11 & 10 & 14 \\
7 & 11 & 12
\end{bmatrix}, \quad
R_B = \begin{bmatrix}
9 & 11 & 13 \\
12 & 12 & 17 \\
10 & 13 & 14
\end{bmatrix}

```

1. Compute the **Sum of Absolute Differences (SAD)** for candidate blocks $R_A$ and $R_B$.
2. Compute the **Mean Absolute Difference (MAD)** for candidate blocks $R_A$ and $R_B$.
3. Compute the **Mean Squared Error (MSE)** for candidate blocks $R_A$ and $R_B$.
4. Determine which candidate block is selected as the optimal motion prediction block.
5. Compute the **Peak Signal-to-Noise Ratio (PSNR)** of the selected optimal block assuming an 8-bit image peak value of $255$.

---

### Step-by-Step Solution

#### Part 1: Evaluation of Candidate Block $R_A$

##### Step 1.1: Calculate Absolute Difference Matrix $\lvert C - R_A \rvert$

Subtract $R_A$ element-by-element from $C$ and take absolute values:

* Row 1:
  * $\lvert 10 - 12 \rvert = \lvert -2 \rvert = 2.0000$
  * $\lvert 12 - 10 \rvert = \lvert 2 \rvert = 2.0000$
  * $\lvert 15 - 10 \rvert = \lvert 5 \rvert = 5.0000$
* Row 2:
  * $\lvert 14 - 11 \rvert = \lvert 3 \rvert = 3.0000$
  * $\lvert 15 - 10 \rvert = \lvert 5 \rvert = 5.0000$
  * $\lvert 18 - 14 \rvert = \lvert 4 \rvert = 4.0000$
* Row 3:
  * $\lvert 12 - 7 \rvert = \lvert 5 \rvert = 5.0000$
  * $\lvert 14 - 11 \rvert = \lvert 3 \rvert = 3.0000$
  * $\lvert 16 - 12 \rvert = \lvert 4 \rvert = 4.0000$

```math

\lvert C - R_A \rvert = \begin{bmatrix}
2 & 2 & 5 \\
3 & 5 & 4 \\
5 & 3 & 4
\end{bmatrix}

```

##### Step 1.2: Compute $\text{SAD}(R_A)$

Sum all elements of $\lvert C - R_A \rvert$:

```math

\text{SAD}(R_A) = (2 + 2 + 5) + (3 + 5 + 4) + (5 + 3 + 4) = 9.0000 + 12.0000 + 12.0000 = \mathbf{33.0000}

```

##### Step 1.3: Compute $\text{MAD}(R_A)$

Divide $\text{SAD}(R_A)$ by total macroblock pixel count $N^2 = 3 \times 3 = 9$:

```math

\text{MAD}(R_A) = \frac{\text{SAD}(R_A)}{9} = \frac{33.0000}{9} = \mathbf{3.6667}

```

##### Step 1.4: Compute Squared Difference Matrix $(C - R_A)^2$ and $\text{MSE}(R_A)$

Square each element of $(C - R_A)$:

```math

(C - R_A)^2 = \begin{bmatrix}
2^2 & 2^2 & 5^2 \\
3^2 & 5^2 & 4^2 \\
5^2 & 3^2 & 4^2
\end{bmatrix} = \begin{bmatrix}
4 & 4 & 25 \\
9 & 25 & 16 \\
25 & 9 & 16
\end{bmatrix}

```

```math

\text{Sum of Squared Differences} = (4 + 4 + 25) + (9 + 25 + 16) + (25 + 9 + 16) = 33.0000 + 50.0000 + 50.0000 = 133.0000

```

```math

\text{MSE}(R_A) = \frac{133.0000}{9} = \mathbf{14.7778}

```

---

#### Part 2: Evaluation of Candidate Block $R_B$

##### Step 2.1: Calculate Absolute Difference Matrix $\lvert C - R_B \rvert$

Subtract $R_B$ element-by-element from $C$ and take absolute values:

* Row 1:
  * $\lvert 10 - 9 \rvert = 1.0000$
  * $\lvert 12 - 11 \rvert = 1.0000$
  * $\lvert 15 - 13 \rvert = 2.0000$
* Row 2:
  * $\lvert 14 - 12 \rvert = 2.0000$
  * $\lvert 15 - 12 \rvert = 3.0000$
  * $\lvert 18 - 17 \rvert = 1.0000$
* Row 3:
  * $\lvert 12 - 10 \rvert = 2.0000$
  * $\lvert 14 - 13 \rvert = 1.0000$
  * $\lvert 16 - 14 \rvert = 2.0000$

```math

\lvert C - R_B \rvert = \begin{bmatrix}
1 & 1 & 2 \\
2 & 3 & 1 \\
2 & 1 & 2
\end{bmatrix}

```

##### Step 2.2: Compute $\text{SAD}(R_B)$

Sum all elements of $\lvert C - R_B \rvert$:

```math

\text{SAD}(R_B) = (1 + 1 + 2) + (2 + 3 + 1) + (2 + 1 + 2) = 4.0000 + 6.0000 + 5.0000 = \mathbf{13.0000}

```

##### Step 2.3: Compute $\text{MAD}(R_B)$

Divide $\text{SAD}(R_B)$ by total macroblock pixel count $N^2 = 9$:

```math

\text{MAD}(R_B) = \frac{13.0000}{9} = \mathbf{1.4444}

```

##### Step 2.4: Compute Squared Difference Matrix $(C - R_B)^2$ and $\text{MSE}(R_B)$

Square each element of $(C - R_B)$:

```math

(C - R_B)^2 = \begin{bmatrix}
1^2 & 1^2 & 2^2 \\
2^2 & 3^2 & 1^2 \\
2^2 & 1^2 & 2^2
\end{bmatrix} = \begin{bmatrix}
1 & 1 & 4 \\
4 & 9 & 1 \\
4 & 1 & 4
\end{bmatrix}

```

```math

\text{Sum of Squared Differences} = (1 + 1 + 4) + (4 + 9 + 1) + (4 + 1 + 4) = 6.0000 + 14.0000 + 9.0000 = 29.0000

```

```math

\text{MSE}(R_B) = \frac{29.0000}{9} = \mathbf{3.2222}

```

---

#### Part 3: Selection of Optimal Candidate Block & PSNR Calculation

##### Step 3.1: Optimal Block Decision

Comparing error metrics between $R_A$ and $R_B$:
* $\text{SAD}(R_B) = 13.0000 < \text{SAD}(R_A) = 33.0000$
* $\text{MAD}(R_B) = 1.4444 < \text{MAD}(R_A) = 3.6667$
* $\text{MSE}(R_B) = 3.2222 < \text{MSE}(R_A) = 14.7778$

Candidate Block $R_B$ has significantly lower error across all metrics. Therefore, **Candidate Block $R_B$ is selected as the optimal matching block**.

##### Step 3.2: Compute PSNR for Optimal Block $R_B$

Using peak intensity $\text{Peak} = 255$ and $\text{MSE}(R_B) = 3.2222$:

```math

\text{Peak}^2 = 255^2 = 65,025.0000

```

```math

\frac{\text{Peak}^2}{\text{MSE}(R_B)} = \frac{65,025.0000}{3.2222} = 20,179.9193

```

```math

\text{PSNR} = 10 \log_{10}(20,179.9193) = 10 \times 4.3049 = \mathbf{43.0492 \quad \text{dB}}

```

---

### Final Answer

* $\text{SAD}(R_A) = \mathbf{33.0000}$, $\text{MAD}(R_A) = \mathbf{3.6667}$, $\text{MSE}(R_A) = \mathbf{14.7778}$
* $\text{SAD}(R_B) = \mathbf{13.0000}$, $\text{MAD}(R_B) = \mathbf{1.4444}$, $\text{MSE}(R_B) = \mathbf{3.2222}$
* **Optimal Selected Block:** $R_B$
* **Reconstructed Block PSNR:** $43.0492 	ext{ dB}$

---

## 3. Numerical Type 2: Block Matching Complexity & Speedup (Full Search vs TSS)

### Exam Context

* **Marks:** 6 Marks / 8 Marks
* **Repeated In:** Final Exam 2024–2025 Q7(a), Re-Exam 2022–2023 Q7(a).

---

### Problem Statement

A video encoder uses macroblocks of size $16 \times 16$ pixels with a search window displacement range of $p = \pm 7$ pixels in both horizontal and vertical directions.

1. Compute the total number of candidate blocks evaluated by the **Exhaustive Search Block Matching Algorithm (ESBMA / Full Search)** for a single macroblock.
2. Compute the total number of candidate blocks evaluated by the **Three-Step Search (TSS)** algorithm for a single macroblock.
3. Calculate the **computational speedup factor** of TSS relative to ESBMA.
4. Calculate the percentage reduction in candidate block evaluations achieved by TSS.
5. If sub-pixel precision of $\frac{1}{4}$-pixel is used for Full Search, how many candidate positions must be evaluated?

---

### Step-by-Step Solution

#### Step 1: Calculate Candidate Block Evaluations for Full Search (ESBMA)

The search window displacement range $p = 7$ allows candidate displacements $dx \in [-7, +7]$ and $dy \in [-7, +7]$.

The total number of candidate search locations per axis is $2p + 1 = 2(7) + 1 = 15$.

```math

N_{\text{ESBMA}} = (2p + 1)^2 = 15 \times 15 = \mathbf{225 \quad \text{candidate locations}}

```

---

#### Step 2: Calculate Candidate Block Evaluations for Three-Step Search (TSS)

TSS evaluates search candidates over three fixed step sizes:

1. **Step 1 ($S_1 = 4$):** Evaluates $1$ center origin point plus $8$ surrounding perimeter points at offset $\pm 4$:

```math

N_{\text{Step 1}} = 1 + 8 = 9 \quad \text{search points}

```

2. **Step 2 ($S_2 = 2$):** Re-centers around the minimum SAD location from Step 1 and evaluates $8$ new surrounding perimeter points at offset $\pm 2$:

```math

N_{\text{Step 2}} = 8 \quad \text{search points}

```

3. **Step 3 ($S_3 = 1$):** Re-centers around the minimum SAD location from Step 2 and evaluates $8$ new surrounding perimeter points at offset $\pm 1$:

```math

N_{\text{Step 3}} = 8 \quad \text{search points}

```

```math

N_{\text{TSS}} = 9 + 8 + 8 = \mathbf{25 \quad \text{candidate locations}}

```

---

#### Step 3: Compute Computational Speedup Factor

Dividing Full Search candidates by TSS candidates:

```math

\text{Speedup Factor} = \frac{N_{\text{ESBMA}}}{N_{\text{TSS}}} = \frac{225}{25} = \mathbf{9.0000\times \quad (9\times \text{ speedup})}

```

---

#### Step 4: Compute Percentage Complexity Reduction

Calculate percentage savings in evaluations:

```math

\text{Percentage Reduction} = \left( 1 - \frac{N_{\text{TSS}}}{N_{\text{ESBMA}}} \right) \times 100\% = \left( 1 - \frac{25}{225} \right) \times 100\%

```

```math

\text{Percentage Reduction} = \left( 1 - 0.1111 \right) \times 100\% = \mathbf{88.8889\%}

```

---

#### Step 5: Calculate Evaluations for $\frac{1}{4}$-Pixel Sub-Pixel Precision Full Search

For $\frac{1}{4}$-pixel precision, the search grid density increases by a factor of $4$ along each spatial dimension ($16\times$ total density):

```math

N_{\text{subpixel}} = [4 \times (2p) + 1]^2 = [4 \times 14 + 1]^2 = [56 + 1]^2 = 57^2 = \mathbf{3,249 \quad \text{candidate locations}}

```

---

### Final Answer

* **Full Search Evaluations ($N_{\text{ESBMA}}$):** $225	ext{ positions}$
* **Three-Step Search Evaluations ($N_{\text{TSS}}$):** $25	ext{ positions}$
* **TSS Computational Speedup:** $9.0000	imes$
* **Percentage Evaluation Savings:** $88.8889\%$
* $\frac{1}{4}$-Pixel Sub-Pixel Full Search Evaluations:** $3,249	ext{ positions}$

---

## 4. Numerical Type 3: Step-by-Step 2D-Logarithmic Search Vector Tracking

### Exam Context

* **Marks:** 8 Marks
* **Repeated In:** IVP Unit-8 Sample Numerical PPT, Re-Exam 2023–2024 Q5(b).

---

### Problem Statement

A $1 \times 1$ pixel macroblock in the current video frame has an intensity value of $C = 65$. We perform a **Two-Dimensional Logarithmic Search (2D-Log Search)** to locate its best match in the reference frame starting with an initial step size $S = 8$.

The reference frame intensity grid surrounding coordinates $(0,0)$ is given as follows:
* Center origin $(0,0) = 55$
* Offset $(0, +8) = 100$, Offset $(0, -8) = 251$, Offset $(-8, 0) = 10$, Offset $(+8, 0) = 227$

Track the step-by-step search progression, compute the SAD at each candidate point, update search centers and step sizes, and determine the final optimal motion vector $(dx^*, dy^*)$.

---

### Step-by-Step Solution

#### Iteration 1: Initial Step Size $S = 8$, Center $(0,0)$

Target intensity $C = 65$. Search $5$ points: center $(0,0)$ and $4$ cross-pattern points at distance $S = 8$:

1. Center $(0,0)$ with intensity $55$:

```math

\text{SAD}(0,0) = \lvert 65 - 55 \rvert = 10.0000

```

2. Top $(0,+8)$ with intensity $100$:

```math

\text{SAD}(0,+8) = \lvert 65 - 100 \rvert = 35.0000

```

3. Bottom $(0,-8)$ with intensity $251$:

```math

\text{SAD}(0,-8) = \lvert 65 - 251 \rvert = 186.0000

```

4. Left $(-8,0)$ with intensity $10$:

```math

\text{SAD}(-8,0) = \lvert 65 - 10 \rvert = 55.0000

```

5. Right $(+8,0)$ with intensity $227$:

```math

\text{SAD}(+8,0) = \lvert 65 - 227 \rvert = 162.0000

```

* **Evaluation:** Minimum SAD occurs at center origin $(0,0)$ with $\text{SAD} = 10.0000$.
* **Decision:** Since the center point wins, keep origin at $(0,0)$ and halve the step size: $S = 8 / 2 = 4$.
---

#### Iteration 2: Step Size $S = 4$, Center $(0,0)$

Search $4$ new cross-pattern points at distance $S = 4$ around origin $(0,0)$:
1. Top $(0,+4)$ with intensity $90$:

```math

\text{SAD}(0,+4) = \lvert 65 - 90 \rvert = 25.0000

```

2. Bottom $(0,-4)$ with intensity $190$:

```math

\text{SAD}(0,-4) = \lvert 65 - 190 \rvert = 125.0000

```

3. Left $(-4,0)$ with intensity $50$:

```math

\text{SAD}(-4,0) = \lvert 65 - 50 \rvert = 15.0000

```

4. Previous Center $(0,0)$ with intensity $55$:

```math

\text{SAD}(0,0) = 10.0000

```

* **Evaluation:** Minimum SAD remains at center origin $(0,0)$ with $\text{SAD} = 10.0000$.
* **Decision:** Center wins again. Keep origin at $(0,0)$ and halve the step size: $S = 4 / 2 = 2$.
---

#### Iteration 3: Step Size $S = 2$, Center $(0,0)$

Search $4$ new cross-pattern points at distance $S = 2$ around origin $(0,0)$:
1. Top $(0,+2)$ with intensity $90$:

```math

\text{SAD}(0,+2) = \lvert 65 - 90 \rvert = 25.0000

```

2. Bottom $(0,-2)$ with intensity $210$:

```math

\text{SAD}(0,-2) = \lvert 65 - 210 \rvert = 145.0000

```

3. Left $(-2,0)$ with intensity $20$:

```math

\text{SAD}(-2,0) = \lvert 65 - 20 \rvert = 45.0000

```

4. Right $(+2,0)$ with intensity $51$:

```math

\text{SAD}(+2,0) = \lvert 65 - 51 \rvert = 14.0000

```

* **Evaluation:** Minimum SAD remains at center origin $(0,0)$ with $\text{SAD} = 10.0000$.
* **Decision:** Center wins again. Keep origin at $(0,0)$ and halve the step size: $S = 2 / 2 = 1$.
---

#### Iteration 4: Final Step Size $S = 1$, Full $3 \times 3$ Neighborhood Search

When $S = 1$, evaluate all $8$ surrounding neighbors around center $(0,0)$:
* Offset $(0,+1) = 61 \implies \text{SAD} = \lvert 65 - 61 \rvert = \mathbf{4.0000}$
* Offset $(+1,0) = 57 \implies \text{SAD} = \lvert 65 - 57 \rvert = 8.0000$
* Offset $(-1,0) = 40 \implies \text{SAD} = \lvert 65 - 40 \rvert = 25.0000$
* Offset $(0,-1) = 150 \implies \text{SAD} = \lvert 65 - 150 \rvert = 85.0000$
* Offset $(+1,+1) = 100 \implies \text{SAD} = \lvert 65 - 100 \rvert = 35.0000$
* Offset $(-1,+1) = 90 \implies \text{SAD} = \lvert 65 - 90 \rvert = 25.0000$
* Offset $(+1,-1) = 145 \implies \text{SAD} = \lvert 65 - 145 \rvert = 80.0000$
* Offset $(-1,-1) = 167 \implies \text{SAD} = \lvert 65 - 167 \rvert = 102.0000$
---

### Final Answer

* **Minimum SAD Value:** $4.0000$ (at location intensity $61$)
* **Optimal Motion Vector:** $(dx^*, dy^*) = (0, +1)$
---

## 5. Numerical Type 4: Uncompressed Video File Size and Memory Savings Calculation

### Exam Context

* **Marks:** 8 Marks / 10 Marks
* **Repeated In:** Textbook Problem 8.30, Unit 7/Unit 8 Notes PPT.
---

### Problem Statement

A digital video sequence runs for a duration of $T = 30\text{ seconds}$ at a frame rate of $R = 30\text{ frames/second}$.
Each frame is an 8-bit monochrome image with a resolution of $256 \times 256$ pixels.
1. Compute the total number of frames in the video sequence.
2. Compute the uncompressed video file size in bits and Megabytes (MB).
3. If each pixel in the video is quantised down to a 4-bit representation, compute the new video storage size in MB.
4. Calculate the total memory storage saved in MB and the percentage memory savings.
---

### Step-by-Step Solution

#### Step 1: Compute Total Number of Frames ($N_{\text{frames}}$)

Multiply duration $T$ by frame rate $R$:

```math

N_{\text{frames}} = T \times R = 30 \text{ seconds} \times 30 \text{ frames/second} = \mathbf{900 \quad \text{frames}}

```

---

#### Step 2: Compute 8-Bit Uncompressed Video Storage

##### Step 2.1: Bits per Single Frame

Multiply row pixels, column pixels, and bit depth per pixel:

```math

\text{Bits per Frame} = 256 \times 256 \times 8 = 65,536 \times 8 = \mathbf{524,288 \quad \text{bits/frame}}

```

##### Step 2.2: Total Video File Size in Bits

Multiply single frame size by total frame count:

```math

\text{Total Bits (8-bit)} = 900 \times 524,288 = \mathbf{471,859,200 \quad \text{bits}}

```

##### Step 2.3: Convert Total Bits to Megabytes (MB)

Divide total bits by $8 \times 1024 \times 1024 = 8,388,608$:

```math

\text{Total Storage (8-bit MB)} = \frac{471,859,200}{8,388,608} = \mathbf{56.2500 \quad \text{MB}}

```

---

#### Step 3: Compute 4-Bit Quantized Video Storage

##### Step 3.1: Bits per Single 4-Bit Frame

```math

\text{Bits per 4-bit Frame} = 256 \times 256 \times 4 = 65,536 \times 4 = \mathbf{262,144 \quad \text{bits/frame}}

```

##### Step 3.2: Total 4-Bit File Size in Bits and Megabytes

```math

\text{Total Bits (4-bit)} = 900 \times 262,144 = \mathbf{235,929,600 \quad \text{bits}}

```

```math

\text{Total Storage (4-bit MB)} = \frac{235,929,600}{8,388,608} = \mathbf{28.1250 \quad \text{MB}}

```

---

#### Step 4: Compute Memory Storage Saved and Percentage Savings

##### Step 4.1: Megabytes Saved

```math

\text{MB Saved} = 56.2500 \text{ MB} - 28.1250 \text{ MB} = \mathbf{28.1250 \quad \text{MB}}

```

##### Step 4.2: Percentage Memory Reduction

```math

\text{Percentage Saved} = \left( \frac{28.1250}{56.2500} \right) \times 100\% = \mathbf{50.0000\%}

```

---

### Final Answer

* **Total Frame Count:** $900	ext{ frames}$
* **8-Bit Uncompressed File Size:** $471,859,200	ext{ bits} = 56.2500	ext{ MB}$
* **4-Bit Quantized File Size:** $235,929,600	ext{ bits} = 28.1250	ext{ MB}$
* **Memory Saved:** $28.1250	ext{ MB}$ ($50.0000\%$ reduction**)

---

## 6. Exam Shortcuts, Tricks, and Pitfalls for Unit 8

### 1. Macroblock Metric Calculation Tricks

* **SAD vs MAD:** Always check if the question asks for SAD or MAD. MAD is simply $\text{SAD} / N^2$. Do not re-sum division terms manually; sum absolute differences first to find SAD, then divide by $N^2$ once at the end!
* **Fast SAD Matrix Summing:** Sum each row of the difference matrix individually before adding rows together to prevent mental addition slip-ups during exams.

### 2. Full Search vs TSS Search Point Distinctions

* **Search Window Area:** If displacement parameter $p = 7$, the search area length is $2p + 1 = 15$. The search area size is $15 \times 15 = 225$ blocks.
* **TSS Point Formula:** Remember TSS always tests $9 + 8 + 8 = 25$ points regardless of macroblock size, giving an immediate speedup factor of $225 / 25 = 9\times$.

### 3. Bit-Rate & Storage Conversion Errors

* **Byte vs Bit Division:** 1 Byte = 8 bits, 1 KB = 1024 Bytes, 1 MB = $1024 \times 1024$ Bytes $= 1,048,576$ Bytes $= 8,388,608$ bits.
* Always divide total bits by $8,388,608$ to directly convert bits to Megabytes!
