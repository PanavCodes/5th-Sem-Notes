# 📚 IVP Unit 5: Edge Detection — Previous Year Question (PYQ) Bank

---

## 📌 Document Overview & Scope Notice

> **Source-status note:** The listed paper filenames, dates, marks, and question numbers are preserved as reported in the supplied workbook. The original examination papers were not provided for comparison in this repair, so their question text and attribution are **not independently verified**. Practice questions are not PYQs.

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 5 — Edge Detection
* **Format:** GitHub Flavored Markdown (GFM) with Standalone Math Blocks
* **Target Audience:** B.Tech / M.Tech Computer Science & EXTC Engineering Students
* **Source Scope:** SVKM's NMIMS MPSTME Semester V Final & Re-Examinations (2022–2026), AKTU / University Term-End Examinations, Standard Textbooks (*Gonzalez & Woods 4th Ed.*, *Bovik's Handbook*), and Laboratory Courseware.
* **Strict Syllabus Boundary:**
  1. Gradient-based edge detection using first-order and second-order derivatives.
  2. Prewitt and Sobel operators (kernels, 1D separable properties, directional responses).
  3. Laplacian operator and Laplacian of Gaussian (LoG / Marr-Hildreth operator, zero-crossing mechanism).
  4. Canny edge detector (3 optimal criteria, 5-stage multi-stage pipeline, NMS, double thresholding, hysteresis tracking).
  5. *Supporting Topics:* Diagonal Sobel/Prewitt masks, Kirsch Compass operator, and Difference of Gaussians (DoG) are preserved where asked in papers and explicitly labeled as **(Supporting topic outside the supplied Unit 5 syllabus)**.

---

## 📊 Syllabus Coverage & Reported Source Directory

| Source Document Name | Institution / Paper Title | Session / Year | Source Status | Target Questions |
|---|---|---|---|---|
| `QP_Final-Exam_Image and Video Processing(702EX0E004)_Semester V_2025-2026.pdf` | NMIMS MPSTME Final Exam | Dec 2025 | **Reported PYQ (unverified)** | Q5(a) Prewitt Gradient Direction |
| `Image_and_Video_Processing_2025-26_Final_JXqVAbAxKK.pdf` | NMIMS MPSTME Final Exam | Dec 2025 | **Reported PYQ (unverified)** | Q3(b) Sobel Magnitude on 4x4 Matrix |
| `Image_and_Video_Processing_Batch_2024-25_Final_DQGae7s0kr.pdf` | NMIMS MPSTME Re-Exam | May 2025 | **Reported PYQ (unverified)** | Q2(b) Prewitt Horizontal, Vertical & Diagonal |
| `Image_and_Video_Processing__3rd_Year__Sem_V__Year_2022-23__Final_Exam_J8kGCoOkO4.pdf` | NMIMS MPSTME Final Exam | Nov/Dec 2022 | **Reported PYQ (unverified)** | Q5(b) Sobel Vector & Edge Comparison |
| `Image_and_Video_Processing__3rd_Year__Sem_V__Year_2022-23__Final_Exam_YTuTXsa4Ff.pdf` | NMIMS MPSTME Final Exam | Nov/Dec 2022 | **Reported PYQ (unverified)** | Q5(a) Prewitt with Zero Padding |
| `Image_and_Video_Processing__Sem-V__Batch_2023-24__Re_Exam_h7sTQW2Di6.pdf` | NMIMS MPSTME Re-Exam | May 2024 | **Reported PYQ (unverified)** | Q5(a) Sobel vs. Prewitt Performance |
| `Image_and_Video_Processing__Sem-V__Year_2022-23__Special_Re_Exam_0wQX152gD2.pdf` | NMIMS MPSTME Special Re-Exam | Jan 2023 | **Reported PYQ (unverified)** | Q5(a) Sobel & Prewitt Masks on 5x5 Matrix |
| `Image_and_Video_Processing___Re-exam_2023-24_2022-23_LL2njyPc7F.pdf` | NMIMS MPSTME Re-Exam | May 2024 | **Reported PYQ (unverified)** | Q3(a) First and Second Derivatives on 1D Scanline |
| `Digital Image Processing (DIP) - @DeveloperLibrary.pdf` | AKTU University Question Bank | 2014–2019 | **Reported PYQ (unverified)** | Kirsch Compass, Sobel LPF/HPF proof, Laplacian |

---

## 📑 Table of Contents

1. [Module 5.1: Derivative Fundamentals & Gradient Edge Detection](#module-51-derivative-fundamentals-gradient-edge-detection)
   * [PYQ 5.1.1: First vs. Second Order Derivatives in Edge Detection (Theory)](#pyq-511-first-vs-second-order-derivatives-in-edge-detection-theory) — *[Reported PYQ (unverified)]*
   * [PYQ 5.1.2: 1D Scanline Derivative Calculation](#pyq-512-1d-scanline-derivative-calculation) — *[Reported PYQ (unverified)]*
   * [PYQ 5.1.3: 2D Gradient Vector, Magnitude, and Direction Angle Calculations](#pyq-513-2d-gradient-vector-magnitude-and-direction-angle-calculations) — *[Practice Question]*
2. [Module 5.2: First-Order Gradient Mask Operators (Prewitt, Sobel & Compass Operators)](#module-52-first-order-gradient-mask-operators-prewitt-sobel-compass-operators)
   * [PYQ 5.2.1: Prewitt Operator Gradient Direction Calculation on a 3x3 Patch](#pyq-521-prewitt-operator-gradient-direction-calculation-on-a-3x3-patch) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.2: Horizontal & Vertical Sobel Convolution with Border Replication](#pyq-522-horizontal-vertical-sobel-convolution-with-border-replication) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.3: Prewitt Horizontal, Vertical & Diagonal Edge Extraction](#pyq-523-prewitt-horizontal-vertical-diagonal-edge-extraction) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.4: Sobel Operator Comparison & Edge Strength Interpretation](#pyq-524-sobel-operator-comparison-edge-strength-interpretation) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.5: Prewitt Operator with Zero Padding Convolution](#pyq-525-prewitt-operator-with-zero-padding-convolution) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.6: Sobel vs. Prewitt Performance & Smoothing Effect Comparison](#pyq-526-sobel-vs-prewitt-performance-smoothing-effect-comparison) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.7: Sobel & Prewitt Mask Application on Step Edge Matrix](#pyq-527-sobel-prewitt-mask-application-on-step-edge-matrix) — *[Reported PYQ (unverified)]*
   * [PYQ 5.2.8: Kirsch Compass Operator 8-Directional Masks](#pyq-528-kirsch-compass-operator-8-directional-masks) — *[Reported PYQ (unverified)]*
3. [Module 5.3: Second-Order Edge Operators (Laplacian & LoG / Marr-Hildreth)](#module-53-second-order-edge-operators-laplacian-log-marr-hildreth)
   * [PYQ 5.3.1: 2D Discrete Laplacian Operator Derivation & Mask Formulation](#pyq-531-2d-discrete-laplacian-operator-derivation-mask-formulation) — *[Reported PYQ (unverified)]*
   * [PYQ 5.3.2: Laplacian Filter Convolution on Center Pixel](#pyq-532-laplacian-filter-convolution-on-center-pixel) — *[Reported PYQ (unverified)]*
   * [PYQ 5.3.3: Laplacian of Gaussian (LoG) Operator & Zero-Crossing Method](#pyq-533-laplacian-of-gaussian-log-operator-zero-crossing-method) — *[Reported PYQ (unverified)]*
4. [Module 5.4: Multi-Stage Canny Edge Detector](#module-54-multi-stage-canny-edge-detector)
   * [PYQ 5.4.1: Canny Edge Detector Optimal Criteria & 5-Stage Pipeline](#pyq-541-canny-edge-detector-optimal-criteria-5-stage-pipeline) — *[Reported PYQ (unverified)]*
   * [PYQ 5.4.2: Canny Non-Maximum Suppression (NMS) & Gradient Sector Quantization](#pyq-542-canny-non-maximum-suppression-nms-gradient-sector-quantization) — *[Practice Question]*
   * [PYQ 5.4.3: Canny Double Thresholding & Hysteresis Edge Tracking](#pyq-543-canny-double-thresholding-hysteresis-edge-tracking) — *[Practice Question]*
5. [Module 5.5: Comprehensive Operator Comparisons & Analysis](#module-55-comprehensive-operator-comparisons-analysis)
   * [PYQ 5.5.1: Comparative Analysis Matrix of Edge Detection Operators](#pyq-551-comparative-analysis-matrix-of-edge-detection-operators) — *[Reported PYQ (unverified)]*
6. [Topic-Wise Question Index & Source Status Directory](#topic-wise-question-index-source-verification-directory)
7. [Repeated & Equivalent Questions Directory](#repeated-equivalent-questions-directory)
8. [Verification Checklist & Final Audit](#verification-checklist-final-audit)

---

<a id="module-51-derivative-fundamentals-gradient-edge-detection"></a>

## Module 5.1: Derivative Fundamentals & Gradient Edge Detection

<a id="pyq-511-first-vs-second-order-derivatives-in-edge-detection-theory"></a>

### PYQ 5.1.1: First vs. Second Order Derivatives in Edge Detection (Theory)

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Re-Exam May 2024 [Q3a] — *[Reported PYQ (unverified)]*
* **Marks:** 4 Marks
* **Exact Wording:** Formulate how the derivatives are obtained in edge detection. Compute first and second order derivative of intensity of pixels along line of grayscale image: $f(x) = [1, 2, 1, 3, 5, 0, 6, 6, 0]$.

---

#### 💡 Model Answer

##### 1. Theoretical Formulation of Derivatives in Digital Images
In digital image processing, spatial derivatives are approximated using **finite differences** because image pixel coordinates are discrete integers:

1. **First-Order Derivative (Gradient):**
   Measures the rate of change of gray-level intensity. For a 1D sequence $f(x)$, the forward finite difference is defined as:

```math
\frac{\partial f}{\partial x} = f(x+1) - f(x)
```

   * **Properties:** Yields a non-zero response along intensity ramps/edges, reaching a peak at the edge slope. It produces thick edge responses.

2. **Second-Order Derivative (Laplacian):**
   Measures the rate of change of the gradient (intensity curvature). It is derived by taking central finite differences of first derivatives:

```math
\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)
```

   * **Properties:** Produces a double response (a positive peak on the dark side and a negative peak on the light side) separated by a **zero-crossing** near the edge transition; discrete sampling need not locate a unique exact midpoint.

---

##### 2. Step-by-Step Calculation for $f(x) = [1, 2, 1, 3, 5, 0, 6, 6, 0]$

* **Given Sequence:** $f(x)$ for $x = 0, 1, 2, \dots, 8$:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $f(x)$ | 1 | 2 | 1 | 3 | 5 | 0 | 6 | 6 | 0 |

---

* **Step 1: First-Order Derivative $\frac{\partial f}{\partial x} = f(x+1) - f(x)$:**
  * $x=0: f(1) - f(0) = 2 - 1 = \mathbf{+1}$
  * $x=1: f(2) - f(1) = 1 - 2 = \mathbf{-1}$
  * $x=2: f(3) - f(2) = 3 - 1 = \mathbf{+2}$
  * $x=3: f(4) - f(3) = 5 - 3 = \mathbf{+2}$
  * $x=4: f(5) - f(4) = 0 - 5 = \mathbf{-5}$
  * $x=5: f(6) - f(5) = 6 - 0 = \mathbf{+6}$
  * $x=6: f(7) - f(6) = 6 - 6 = \mathbf{0}$
  * $x=7: f(8) - f(7) = 0 - 6 = \mathbf{-6}$

```math
\frac{\partial f}{\partial x} = \begin{bmatrix}
+1 & -1 & +2 & +2 & -5 & +6 & 0 & -6
\end{bmatrix} \quad (\text{for } x=0 \dots 7)
```

---

* **Step 2: Second-Order Derivative $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$ (for interior pixels $x=1 \dots 7$):**
  * $x=1: f(2) + f(0) - 2f(1) = 1 + 1 - 2(2) = 2 - 4 = \mathbf{-2}$
  * $x=2: f(3) + f(1) - 2f(2) = 3 + 2 - 2(1) = 5 - 2 = \mathbf{+3}$
  * $x=3: f(4) + f(2) - 2f(3) = 5 + 1 - 2(3) = 6 - 6 = \mathbf{0}$
  * $x=4: f(5) + f(3) - 2f(4) = 0 + 3 - 2(5) = 3 - 10 = \mathbf{-7}$
  * $x=5: f(6) + f(4) - 2f(5) = 6 + 5 - 2(0) = 11 - 0 = \mathbf{+11}$
  * $x=6: f(7) + f(5) - 2f(6) = 6 + 0 - 2(6) = 6 - 12 = \mathbf{-6}$
  * $x=7: f(8) + f(6) - 2f(7) = 0 + 6 - 2(6) = 6 - 12 = \mathbf{-6}$

```math
\frac{\partial^2 f}{\partial x^2} = \begin{bmatrix}
-2 & +3 & 0 & -7 & +11 & -6 & -6
\end{bmatrix} \quad (\text{for } x=1 \dots 7)
```

---

##### 3. Summary Results Table

| $x$ | $f(x)$ | First Derivative $\frac{\partial f}{\partial x}$ | Second Derivative $\frac{\partial^2 f}{\partial x^2}$ | Feature Interpretation |
|---|---|---|---|---|
| 0 | 1 | +1 | — | Ramp start |
| 1 | 2 | -1 | -2 | Local peak |
| 2 | 1 | +2 | +3 | Local valley |
| 3 | 3 | +2 | 0 | Linear ramp midpoint |
| 4 | 5 | -5 | -7 | Peak before downward step |
| 5 | 0 | +6 | +11 | Zero valley / Sharp edge transition |
| 6 | 6 | 0 | -6 | Flat plateau start |
| 7 | 6 | -6 | -6 | Flat plateau end |
| 8 | 0 | — | — | Downward step end |

---

<a id="pyq-512-1d-scanline-derivative-calculation"></a>

### PYQ 5.1.2: 1D Scanline Derivative Calculation

#### ❓ Question Statement
* **Source:** Practice Question (Adapted from University Tutorial Sets) — *[Practice Question]*
* **Marks:** 5 Marks
* **Question:** Consider a 1D image scanline $f(x) = [10, 10, 10, 20, 30, 40, 40, 40]$. Compute the forward first derivative, central first derivative, and second derivative. Identify the edge boundary location.

---

#### 💡 Model Answer

##### 1. Mathematical Definitions
* **Forward First Derivative:** $\Delta_f f(x) = f(x+1) - f(x)$
* **Central First Derivative:** $\Delta_c f(x) = \frac{f(x+1) - f(x-1)}{2}$
* **Second Derivative:** $\nabla^2 f(x) = f(x+1) + f(x-1) - 2f(x)$

---

##### 2. Step-by-Step Numerical Calculations

Given scanline $f(x)$ for $x=0 \dots 7$:

```math
f(x) = \begin{bmatrix}
10 & 10 & 10 & 20 & 30 & 40 & 40 & 40
\end{bmatrix}
```

1. **Forward Derivative $\Delta_f f(x)$ ($x = 0 \dots 6$):**
   * $x=0: 10 - 10 = 0$
   * $x=1: 10 - 10 = 0$
   * $x=2: 20 - 10 = +10$
   * $x=3: 30 - 20 = +10$
   * $x=4: 40 - 30 = +10$
   * $x=5: 40 - 40 = 0$
   * $x=6: 40 - 40 = 0$

```math
\Delta_f f(x) = \begin{bmatrix}
0 & 0 & +10 & +10 & +10 & 0 & 0
\end{bmatrix}
```

2. **Central Derivative $\Delta_c f(x)$ ($x = 1 \dots 6$):**
   * $x=1: (10 - 10)/2 = 0$
   * $x=2: (20 - 10)/2 = +5$
   * $x=3: (30 - 10)/2 = +10$
   * $x=4: (40 - 20)/2 = +10$
   * $x=5: (40 - 30)/2 = +5$
   * $x=6: (40 - 40)/2 = 0$

```math
\Delta_c f(x) = \begin{bmatrix}
0 & +5 & +10 & +10 & +5 & 0
\end{bmatrix}
```

3. **Second Derivative $\nabla^2 f(x)$ ($x = 1 \dots 6$):**
   * $x=1: 10 + 10 - 20 = 0$
   * $x=2: 20 + 10 - 20 = +10$ (Positive peak on dark side of ramp)
   * $x=3: 30 + 10 - 60 = 0$ (Zero crossing at ramp midpoint $x=3$)
   * $x=4: 40 + 20 - 60 = 0 \implies 40+20-60 = 0$; indeed $f(5)+f(3)-2f(4)=40+20-2(30)=0$.
   * $x=5: f(6)+f(4)-2f(5) = 40+30-2(40) = -10$ (Negative peak on bright side of ramp)
   * $x=6: 40 + 40 - 80 = 0$

```math
\nabla^2 f(x) = \begin{bmatrix}
0 & +10 & 0 & 0 & -10 & 0
\end{bmatrix}
```

---

##### 3. Observation
The intensity transition from $10 \to 40$ represents a **ramp edge** spanning $x=2$ to $x=5$. The central derivative reaches its maximum (+10) across $x=3,4$. The second derivative produces $+10$ at $x=2$ (start of ramp) and $-10$ at $x=5$ (end of ramp), with a zero crossing at $x=3.5$, exactly locating the ramp center.

---

<a id="pyq-513-2d-gradient-vector-magnitude-and-direction-angle-calculations"></a>

### PYQ 5.1.3: 2D Gradient Vector, Magnitude, and Direction Angle Calculations

#### ❓ Question Statement
* **Source:** Practice Question — *[Practice Question]*
* **Marks:** 4 Marks
* **Question:** Suppose the horizontal gradient $G_x = +40$ and vertical gradient $G_y = -30$ at a pixel $(x,y)$. Calculate:
1. Exact Euclidean Gradient Magnitude $G$.
2. Absolute Sum Gradient Approximation $G_{\text{approx}}$.
3. Gradient Direction Angle $\theta$ using $\text{atan2}(G_y, G_x)$.
4. Physical Orientation Angle $\phi$ of the edge line.

---

#### 💡 Model Answer

##### 1. Calculations

Given $G_x = +40$, $G_y = -30$:

1. **Exact Euclidean Gradient Magnitude $G$:**

```math
G = \sqrt{G_x^2 + G_y^2} = \sqrt{40^2 + (-30)^2} = \sqrt{1600 + 900} = \sqrt{2500} = \mathbf{50.0}
```

2. **Absolute Sum ($L_1$) Gradient Magnitude Alternative $G_{\text{approx}}$:**

```math
G_{\text{approx}} = |G_x| + |G_y| = |40| + |-30| = 40 + 30 = \mathbf{70.0}
```
*(Note: $G_{\text{approx}}$ overestimates Euclidean magnitude by $(70-50)/50 = 40\%$, but avoids floating-point square root computation in hardware).*

3. **Gradient Direction Angle $\theta$:**

```math
\theta = \text{atan2}(G_y, G_x) = \text{atan2}(-30, +40) = \mathbf{-36.87^\circ} \quad (\text{or } 323.13^\circ)
```

4. **Edge Line Physical Orientation $\phi$:**
The edge boundary line runs **perpendicular** ($\pm 90^\circ$) to the gradient vector direction $\theta$:

```math
\phi = \theta + 90^\circ = -36.87^\circ + 90^\circ = \mathbf{+53.13^\circ}
```

---

<a id="module-52-first-order-gradient-mask-operators-prewitt-sobel-compass-operators"></a>

## Module 5.2: First-Order Gradient Mask Operators (Prewitt, Sobel & Compass Operators)

<a id="pyq-521-prewitt-operator-gradient-direction-calculation-on-a-3x3-patch"></a>

### PYQ 5.2.1: Prewitt Operator Gradient Direction Calculation on a 3x3 Patch

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Semester V Final Exam Dec 2025 [Q5a] — *[Reported PYQ (unverified)]*
* **Marks:** 4 Marks
* **Exact Wording:** For the given image below:

```math
\begin{bmatrix}
2 & 4 & 6 \\
1 & 5 & 7 \\
3 & 9 & 8
\end{bmatrix}
```
Compute Gradient Direction for the center pixel using Prewitt operator.

---

#### 💡 Model Answer

##### 1. Prewitt Spatial Kernels & Conventions
The standard $3 \times 3$ Prewitt operator kernels for horizontal derivative ($G_x$) and vertical derivative ($G_y$) are:

```math
P_x = \begin{bmatrix}
-1 & 0 & +1 \\
-1 & 0 & +1 \\
-1 & 0 & +1
\end{bmatrix}, \quad P_y = \begin{bmatrix}
-1 & -1 & -1 \\
0 & 0 & 0 \\
+1 & +1 & +1
\end{bmatrix}
```

* **Convention:** Cross-correlation (masks applied as printed, without a 180-degree flip) with origin at center pixel $f(1,1) = 5$. Coordinates: $x$ increases horizontally to the right, $y$ increases vertically downward.

---

##### 2. Step-by-Step Correlation at Center Pixel $f(1,1) = 5$

Given $3 \times 3$ neighborhood $I$:

```math
I = \begin{bmatrix}
2 & 4 & 6 \\
1 & 5 & 7 \\
3 & 9 & 8
\end{bmatrix}
```

* **Step 1: Compute $G_x$ (Horizontal Response):**

```math
G_x = (-1)\cdot 2 + 0\cdot 4 + (+1)\cdot 6 + (-1)\cdot 1 + 0\cdot 5 + (+1)\cdot 7 + (-1)\cdot 3 + 0\cdot 9 + (+1)\cdot 8
```

```math
G_x = (-2 + 0 + 6) + (-1 + 0 + 7) + (-3 + 0 + 8) = 4 + 6 + 5 = \mathbf{+15}
```

---

* **Step 2: Compute $G_y$ (Vertical Response):**

```math
G_y = (-1)\cdot 2 + (-1)\cdot 4 + (-1)\cdot 6 + 0\cdot 1 + 0\cdot 5 + 0\cdot 7 + (+1)\cdot 3 + (+1)\cdot 9 + (+1)\cdot 8
```

```math
G_y = (-2 - 4 - 6) + (0 + 0 + 0) + (3 + 9 + 8) = -12 + 0 + 20 = \mathbf{+8}
```
*(Note: As recorded in the official exam solution scheme, if $P_y$ has top row $+1$ and bottom row $-1$, $G_y = -8$. Using $\text{atan2}(G_y, G_x)$ with $G_y = -8, G_x = 15$ yields $\theta = -28.07^\circ$. With $G_y = +8, G_x = 15$, $\theta = +28.07^\circ$).*

---

* **Step 3: Compute Gradient Direction Angle $\theta$:**

```math
\theta = \text{atan2}(+8,+15) = \mathbf{+28.07^\circ} \quad (\text{printed }P_y\text{ mask});\qquad \text{atan2}(-8,+15)=\mathbf{-28.07^\circ}\quad(\text{reversed }P_y\text{ only})
```

---

<a id="pyq-522-horizontal-vertical-sobel-convolution-with-border-replication"></a>

### PYQ 5.2.2: Horizontal & Vertical Sobel Convolution with Border Replication

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Semester V Final Exam Dec 2025 [Q3b] — *[Reported PYQ (unverified)]*
* **Marks:** 8 Marks
* **Exact Wording:** Apply the Horizontal and Vertical Sobel operators on the image, then compute the gradient magnitude, using pixel replication at borders.

```math
\begin{bmatrix}
10 & 10 & 10 & 10 \\
10 & 10 & 10 & 10 \\
100 & 100 & 100 & 100 \\
100 & 100 & 100 & 100
\end{bmatrix}
```

---

#### 💡 Model Answer

##### 1. Sobel Kernels & Border Replication Setup

Standard $3 \times 3$ Sobel masks:

```math
S_x = \begin{bmatrix}
-1 & 0 & +1 \\
-2 & 0 & +2 \\
-1 & 0 & +1
\end{bmatrix}, \quad S_y = \begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
+1 & +2 & +1
\end{bmatrix}
```

The $4 \times 4$ input image contains a horizontal step edge transition from intensity $10$ (Rows 1–2) to $100$ (Rows 3–4):

```math
I = \begin{bmatrix}
10 & 10 & 10 & 10 \\
10 & 10 & 10 & 10 \\
100 & 100 & 100 & 100 \\
100 & 100 & 100 & 100
\end{bmatrix}
```

* **Padding Rule:** Pixel replication at borders extends Row 1 upward and Row 4 downward, Column 1 leftward and Column 4 rightward.

---

##### 2. Step-by-Step Convolution Calculations

* **Horizontal Response $G_x$:**
Because all rows in $I$ have uniform horizontal intensity ($10, 10, 10, 10$ and $100, 100, 100, 100$), every $3 \times 3$ neighborhood is horizontally symmetric. Therefore, the left column (-1, -2, -1) and right column (+1, +2, +1) products cancel out completely for all pixels:

```math
G_x = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

---

* **Vertical Response $G_y$:**
  * **Row 1 (Top Border, Replicated Row 1 above = 10):**
    Top row = 10, Middle row = 10, Bottom row = 10.
    $G_y = (-1\cdot 10 - 2\cdot 10 - 1\cdot 10) + 0 + (1\cdot 10 + 2\cdot 10 + 1\cdot 10) = -40 + 40 = \mathbf{0}$.

  * **Row 2 (Upper Side of Edge):**
    Top row = 10 (Row 1), Middle row = 10 (Row 2), Bottom row = 100 (Row 3).
    $G_y = (-1\cdot 10 - 2\cdot 10 - 1\cdot 10) + 0 + (1\cdot 100 + 2\cdot 100 + 1\cdot 100) = -40 + 400 = \mathbf{+360}$
    *(If $S_y$ has top row $+1$ and bottom row $-1$, $G_y = -360$).*

  * **Row 3 (Lower Side of Edge):**
    Top row = 10 (Row 2), Middle row = 100 (Row 3), Bottom row = 100 (Row 4).
    $G_y = (-1\cdot 10 - 2\cdot 10 - 1\cdot 10) + 0 + (1\cdot 100 + 2\cdot 100 + 1\cdot 100) = -40 + 400 = \mathbf{+360}$
    *(Or $-360$).*

  * **Row 4 (Bottom Border, Replicated Row 4 below = 100):**
    Top row = 100, Middle row = 100, Bottom row = 100.
    $G_y = -400 + 400 = \mathbf{0}$.

```math
G_y = \begin{bmatrix}
0 & 0 & 0 & 0 \\
360 & 360 & 360 & 360 \\
360 & 360 & 360 & 360 \\
0 & 0 & 0 & 0
\end{bmatrix} \quad (\text{or } -360)
```

---

* **Gradient Magnitude $M = \sqrt{G_x^2 + G_y^2} = |G_y|$:**

```math
M = \begin{bmatrix}
0 & 0 & 0 & 0 \\
360 & 360 & 360 & 360 \\
360 & 360 & 360 & 360 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

---

<a id="pyq-523-prewitt-horizontal-vertical-diagonal-edge-extraction"></a>

### PYQ 5.2.3: Prewitt Horizontal, Vertical & Diagonal Edge Extraction

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Re-Exam May 2025 [Q2b] — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Exact Wording:** Consider the given images:
  * Image 1:

```math
\begin{bmatrix}
50 & 50 & 50 & 10 \\
50 & 50 & 50 & 10 \\
50 & 50 & 50 & 10 \\
50 & 50 & 50 & 10
\end{bmatrix}
```
  * Image 2:

```math
\begin{bmatrix}
50 & 10 & 10 & 10 \\
10 & 50 & 10 & 10 \\
10 & 10 & 50 & 10 \\
10 & 10 & 10 & 50
\end{bmatrix}
```
a) Apply the Horizontal and vertical Prewitt Operator on image 1 and find the magnitude of gradient.
b) Apply forward and backward Prewitt operator to identify the diagonal edges in image 2. **(Supporting topic outside the supplied Unit 5 syllabus)**
c) Write the observations on results found in (b).

---

#### 💡 Model Answer

##### Part (a): Image 1 Horizontal & Vertical Prewitt Processing

Image 1 contains a vertical step edge transition between Column 3 ($50$) and Column 4 ($10$):

```math
\text{Image 1} = \begin{bmatrix}
50 & 50 & 50 & 10 \\
50 & 50 & 50 & 10 \\
50 & 50 & 50 & 10 \\
50 & 50 & 50 & 10
\end{bmatrix}
```

Evaluating interior pixels (Rows 2–3, Cols 2–3) using Prewitt masks:

1. **At Interior Position $(2,2)$ (Neighborhood cols 1–3 = all 50s):**
   * $G_x = (-1)(50+50+50) + (+1)(50+50+50) = -150 + 150 = \mathbf{0}$
   * $G_y = (-1)(50+50+50) + (+1)(50+50+50) = -150 + 150 = \mathbf{0}$

2. **At Interior Position $(2,3)$ (Neighborhood cols 2–4 = [50, 50, 10]):**
   * $G_x = (-1)(50+50+50) + 0 + (+1)(10+10+10) = -150 + 30 = \mathbf{-120}$
   * $G_y = (-1)(50+50+10) + 0 + (+1)(50+50+10) = -110 + 110 = \mathbf{0}$

3. **Magnitude Matrix $M = \sqrt{G_x^2 + G_y^2}$ (Interior $2 \times 2$):**

```math
M_{\text{interior}} = \begin{bmatrix}
0 & 120 \\
0 & 120
\end{bmatrix}
```

---

##### Part (b): Image 2 Forward & Backward Diagonal Prewitt Operators `*(Supporting Topic)*`

Image 2 contains a diagonal line of intensity $50$ along the main diagonal $(i,i)$:

```math
\text{Image 2} = \begin{bmatrix}
50 & 10 & 10 & 10 \\
10 & 50 & 10 & 10 \\
10 & 10 & 50 & 10 \\
10 & 10 & 10 & 50
\end{bmatrix}
```

Diagonal Prewitt Kernels:
* **Forward Diagonal Kernel $P_F$ ($+45^\circ$):** 

```math
\begin{bmatrix}
0 & +1 & +1 \\
-1 & 0 & +1 \\
-1 & -1 & 0
\end{bmatrix}
```

* **Backward Diagonal Kernel $P_B$ ($-45^\circ$):** 

```math
\begin{bmatrix}
-1 & -1 & 0 \\
-1 & 0 & +1 \\
0 & +1 & +1
\end{bmatrix}
```


Evaluating interior positions $(2,2)$ and $(2,3)$ for Image 2:
* **At Position $(2,2)$ (Center pixel = 50 on diagonal):**
  * $P_F$ response $y_F = (10+10+10) - (10+10+10) = \mathbf{0}$ (Symmetric across $+45^\circ$ axis).
  * $P_B$ response $y_B = \mathbf{0}$ for the printed symmetric diagonal patch and mask.
* **At Off-Diagonal Position $(2,3)$ (Center pixel = 10):**
  * $y_F=-80$ and $y_B=0$ for the printed masks, giving a diagonal response of magnitude $80$.

```math
y_F = \begin{bmatrix}
0 & -80 \\
80 & 0
\end{bmatrix}, \quad y_B = \begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}, \quad M_{\text{diag}} = \begin{bmatrix}
0 & 80 \\
80 & 0
\end{bmatrix}
```

---

##### Part (c): Observations
1. Standard orthogonal $P_x,P_y$ operators can also respond to diagonal edges; they do not universally give zero response. For this particular symmetric patch, evaluate their responses separately rather than assuming cancellation.
2. Diagonal Prewitt operators $P_F$ and $P_B$ effectively isolate diagonal intensity discontinuities that orthogonal operators miss.

---

<a id="pyq-524-sobel-operator-comparison-edge-strength-interpretation"></a>

### PYQ 5.2.4: Sobel Operator Comparison & Edge Strength Interpretation

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Semester V Final Exam Nov/Dec 2022 [Q5b] — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Exact Wording:** Consider two images represented by the following image matrices:
  * Image A:

```math
\begin{bmatrix}
20 & 20 & 20 & 20 \\
20 & 20 & 20 & 20 \\
60 & 60 & 60 & 60 \\
60 & 60 & 60 & 60
\end{bmatrix}
```
  * Image B:

```math
\begin{bmatrix}
10 & 10 & 100 & 100 \\
10 & 10 & 100 & 100 \\
10 & 10 & 100 & 100 \\
10 & 10 & 100 & 100
\end{bmatrix}
```
For both the images:
(i) Use Sobel operator to determine gradient vectors, $G_x$ and $G_y$.
(ii) Determine magnitude and angle of gradient vector.
(iii) Interpret the direction of edges.
(iv) Identify the image which has stronger edge?

---

#### 💡 Model Answer

##### 1. Image A Calculations (Horizontal Step Edge $20 \to 60$)

Evaluating interior $2 \times 2$ sub-image (Rows 2–3, Cols 2–3):

* **At Position $(2,2)$:**
  * $G_x = (-1\cdot 20 - 2\cdot 20 - 1\cdot 20) + (1\cdot 20 + 2\cdot 20 + 1\cdot 20) = \mathbf{0}$
  * $G_y = (-1\cdot 20 - 2\cdot 20 - 1\cdot 20) + (1\cdot 60 + 2\cdot 60 + 1\cdot 60) = -80 + 240 = \mathbf{+160}$
* **Gradient Magnitude $M_A$:**

```math
M_A = \sqrt{0^2 + 160^2} = \mathbf{160.0}
```

* **Gradient Angle $\theta_A$:**

```math
\theta_A = \text{atan2}(+160, 0) = \mathbf{+90^\circ} \quad (\text{Vertical gradient vector})
```

* **Edge Line Direction $\phi_A$:**
  The physical edge line runs at $\phi_A = 90^\circ - 90^\circ = \mathbf{0^\circ}$ (**Horizontal Edge**).

---

##### 2. Image B Calculations (Vertical Step Edge $10 \to 100$)

Evaluating interior $2 \times 2$ sub-image (Rows 2–3, Cols 2–3):

* **At Position $(2,2)$:**
  * $G_x = (-1\cdot 10 - 2\cdot 10 - 1\cdot 10) + (1\cdot 100 + 2\cdot 100 + 1\cdot 100) = -40 + 400 = \mathbf{+360}$
  * $G_y = (-1\cdot 10 - 2\cdot 10 - 1\cdot 100) + \dots = \mathbf{0}$
* **Gradient Magnitude $M_B$:**

```math
M_B = \sqrt{360^2 + 0^2} = \mathbf{360.0}
```

* **Gradient Angle $\theta_B$:**

```math
\theta_B = \text{atan2}(0, +360) = \mathbf{0^\circ} \quad (\text{Horizontal gradient vector})
```

* **Edge Line Direction $\phi_B$:**
  The physical edge line runs at $\phi_B = 0^\circ + 90^\circ = \mathbf{90^\circ}$ (**Vertical Edge**).

---

##### 3. Comparison & Conclusions
* **Edge Strengths:** $M_B = 360.0 > M_A = 160.0$.
* **Stronger Edge Identification:** **Image B has a significantly stronger edge** because its intensity transition step $\Delta I_B = 100 - 10 = 90$ is more than double the step contrast in Image A ($\Delta I_A = 60 - 20 = 40$).

---

<a id="pyq-525-prewitt-operator-with-zero-padding-convolution"></a>

### PYQ 5.2.5: Prewitt Operator with Zero Padding Convolution

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Semester V Final Exam Nov/Dec 2022 [Q5a] — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Exact Wording:** Apply Prewitt gradient operators to find horizontal and vertical edges in the given image. Also, find the magnitude of gradient vector. Show all the steps and the final image matrix. Use zero padding at the extreme edges while performing the operation.

```math
\begin{bmatrix}
5 & 10 & 10 \\
5 & 10 & 10 \\
5 & 10 & 10
\end{bmatrix}
```

---

#### 💡 Model Answer

##### 1. Zero Padding Extension Setup
Given $3 \times 3$ image $I$:

```math
I = \begin{bmatrix}
5 & 10 & 10 \\
5 & 10 & 10 \\
5 & 10 & 10
\end{bmatrix}
```

Adding a border of zeros creates a $5 \times 5$ padded matrix $I_{\text{padded}}$:

```math
I_{\text{padded}} = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 5 & 10 & 10 & 0 \\
0 & 5 & 10 & 10 & 0 \\
0 & 5 & 10 & 10 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

---

##### 2. Full $3 \times 3$ Output Convolution Calculations

* **Horizontal Prewitt Response $G_x$:**
  * **Column 1 ($r=1..3, c=1$):** Left col = 0, Center col = 5, Right col = 10 $\implies G_x = -0 + 10+10+10 = \mathbf{+30}$.
  * **Column 2 ($r=1..3, c=2$):** Left col = 5, Center col = 10, Right col = 10 $\implies G_x = (-1)(5+5+5) + (+1)(10+10+10) = -15 + 30 = \mathbf{+15}$.
  * **Column 3 ($r=1..3, c=3$):** Left col = 10, Center col = 10, Right col = 0 $\implies G_x = (-1)(10+10+10) + 0 = \mathbf{-30}$.

```math
G_x = \begin{bmatrix}
20 & 10 & -20 \\
30 & 15 & -30 \\
20 & 10 & -20
\end{bmatrix}
```

* **Vertical Prewitt Response $G_y$:**
Because all columns are vertically uniform ($5,5,5$ and $10,10,10$), $G_y = 0$ for all interior pixels, with top/bottom zero-padding effects at row boundaries. Applying the printed bottom-positive $P_y$ yields $G_y$ top row $(15,25,20)$ and bottom row $(-15,-25,-20)$; magnitude is $\sqrt{G_x^2+G_y^2}$, rounded to two decimals.

```math
G_y = \begin{bmatrix}
15 & 25 & 20 \\
0 & 0 & 0 \\
-15 & -25 & -20
\end{bmatrix}
```

* **Final Gradient Magnitude Matrix $M = \sqrt{G_x^2 + G_y^2}$:**

```math
M = \begin{bmatrix}
25.00 & 26.93 & 28.28 \\
30.00 & 15.00 & 30.00 \\
25.00 & 26.93 & 28.28
\end{bmatrix}
```

---

<a id="pyq-526-sobel-vs-prewitt-performance-smoothing-effect-comparison"></a>

### PYQ 5.2.6: Sobel vs. Prewitt Performance & Smoothing Effect Comparison

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Re-Exam May 2024 [Q5a] — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Exact Wording:** Apply appropriate masks of Sobel and Prewitt operators to detect edges in the given images (generate $4 \times 4$ output images). Compare the outputs and comment on the performance of both operators.
Image 1:

```math
\begin{bmatrix}
50 & 50 & 50 & 50 & 50 & 50 \\
50 & 50 & 50 & 50 & 50 & 50 \\
200 & 200 & 200 & 200 & 200 & 200 \\
200 & 200 & 200 & 200 & 200 & 200 \\
200 & 200 & 200 & 200 & 200 & 200 \\
200 & 200 & 200 & 200 & 200 & 200
\end{bmatrix}
```

---

#### 💡 Model Answer

##### 1. Convolution Operations on $6 \times 6$ Image 1

Image 1 contains a horizontal step edge transition between Row 2 ($50$) and Row 3 ($200$), with a step height of $\Delta I = 150$.

Evaluating $4 \times 4$ interior output matrix (Rows 2–5, Cols 2–5):

1. **Prewitt Vertical Response $G_{y,\text{Prewitt}}$:**
   * **Row 2 (Upper Side of Edge):** Top row = 50, Middle = 50, Bottom = 200.
     $G_y = (-1)(50+50+50) + 0 + (+1)(200+200+200) = -150 + 600 = \mathbf{+450}$.
   * **Row 3 (Lower Side of Edge):** Top row = 50, Middle = 200, Bottom = 200.
     $G_y = (-1)(50+50+50) + 0 + (+1)(200+200+200) = -150 + 600 = \mathbf{+450}$.
   * **Flat Rows 1, 4:** $G_y = \mathbf{0}$.

```math
M_{\text{Prewitt}} = \begin{bmatrix}
0 & 0 & 0 & 0 \\
450 & 450 & 450 & 450 \\
450 & 450 & 450 & 450 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

2. **Sobel Vertical Response $G_{y,\text{Sobel}}$:**
   * **Row 2 (Upper Side of Edge):** Top row = 50, Middle = 50, Bottom = 200.
     $G_y = (-1)(50) - 2(50) - 1(50) + (+1)(200) + 2(200) + 1(200) = -200 + 800 = \mathbf{+600}$.
   * **Row 3 (Lower Side of Edge):**
     $G_y = -200 + 800 = \mathbf{+600}$.

```math
M_{\text{Sobel}} = \begin{bmatrix}
0 & 0 & 0 & 0 \\
600 & 600 & 600 & 600 \\
600 & 600 & 600 & 600 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

---

##### 2. Operator Performance Comparison
* **Amplification Factor:** Sobel produces a peak response of **$600$** compared to Prewitt's **$450$** ($1.33\times$ higher magnitude).
* **Noise Robustness:** Sobel assigns a higher center weight ($2$) to the center row/column, providing a **weighted triangular/Gaussian smoothing effect** that suppresses high-frequency noise specks better than Prewitt's uniform box smoothing weight ($1$).

---

<a id="pyq-527-sobel-prewitt-mask-application-on-step-edge-matrix"></a>

### PYQ 5.2.7: Sobel & Prewitt Mask Application on Step Edge Matrix

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Special Re-Exam Jan 2023 [Q5a] — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Exact Wording:** Give $3 \times 3$ masks for the following edge extraction operators: 1. Sobel, 2. Prewitt. Use these masks on following image and show the resultant image, ignore the border pixel.

```math
\begin{bmatrix}
20 & 20 & 45 & 45 & 45 \\
20 & 20 & 45 & 45 & 45 \\
20 & 20 & 45 & 45 & 45 \\
20 & 20 & 45 & 45 & 45 \\
20 & 20 & 45 & 45 & 45
\end{bmatrix}
```

---

#### 💡 Model Answer

##### 1. Mask Definitions & Image Properties
The $5 \times 5$ image contains a vertical step edge transition from Column 2 ($20$) to Column 3 ($45$), step contrast $\Delta I = 25$.

Ignoring border pixels yields a $3 \times 3$ interior output matrix (Rows 2–4, Cols 2–4):

1. **Prewitt Operator Convolution ($P_x$):**
   * **Col 2 (Left Side of Edge):** Left col = 20, Center = 20, Right = 45.
     $G_x = (-1)(20+20+20) + (+1)(45+45+45) = -60 + 135 = \mathbf{+75}$.
   * **Col 3 (Right Side of Edge):** Left col = 20, Center = 45, Right = 45.
     $G_x = (-1)(20+20+20) + (+1)(45+45+45) = -60 + 135 = \mathbf{+75}$.
   * **Col 4 (Flat Region):** $G_x = \mathbf{0}$.

```math
M_{\text{Prewitt}} = \begin{bmatrix}
75 & 75 & 0 \\
75 & 75 & 0 \\
75 & 75 & 0
\end{bmatrix}
```

2. **Sobel Operator Convolution ($S_x$):**
   * **Col 2:** $G_x = (-1\cdot 20 - 2\cdot 20 - 1\cdot 20) + (1\cdot 45 + 2\cdot 45 + 1\cdot 45) = -80 + 180 = \mathbf{+100}$.
   * **Col 3:** $G_x = \mathbf{+100}$.

```math
M_{\text{Sobel}} = \begin{bmatrix}
100 & 100 & 0 \\
100 & 100 & 0 \\
100 & 100 & 0
\end{bmatrix}
```

---

<a id="pyq-528-kirsch-compass-operator-8-directional-masks"></a>

### PYQ 5.2.8: Kirsch Compass Operator 8-Directional Masks

#### ❓ Question Statement
* **Source:** AKTU University Question Bank / Question Compilations — *[Reported PYQ (unverified)]* **(Supporting topic outside the supplied Unit 5 syllabus)**
* **Marks:** 10 Marks
* **Question:** The compass gradient operators of size $3 \times 3$ are designed to measure gradients of edges oriented in eight directions: E, NE, N, NW, W, SW, S, and SE. Give the form of these eight operators using coefficients valued 0, 1, or -1 (or Kirsch 5/-3 weights). Explain how edge direction is determined.

---

#### 💡 Model Answer

##### 1. Kirsch Compass Mask Definitions
The Kirsch compass edge detector uses 8 directional $3 \times 3$ masks ($K_0 \dots K_7$) rotated in $45^\circ$ increments around the compass points:

```math
K_N = \begin{bmatrix}
+5 & +5 & +5 \\
-3 & 0 & -3 \\
-3 & -3 & -3
\end{bmatrix}, \quad K_{NE} = \begin{bmatrix}
-3 & +5 & +5 \\
-3 & 0 & +5 \\
-3 & -3 & -3
\end{bmatrix}, \quad K_E = \begin{bmatrix}
-3 & -3 & +5 \\
-3 & 0 & +5 \\
-3 & -3 & +5
\end{bmatrix}
```

---

The remaining five masks are generated by rotating the three adjacent $+5$ positions around the eight perimeter positions in $45^\circ$ steps; set the other five perimeter positions to $-3$ and the center to $0$. This defines all eight orientations without silently omitting five masks.

##### 2. Edge Detection Rule
At each pixel $(x,y)$, the image is convolved with all 8 compass masks. The final edge magnitude $E(x,y)$ and mask-response direction $\phi(x,y)$ are determined by the **maximum absolute response** (the physical edge-line direction is perpendicular to the gradient response):

```math
E(x,y) = \max_{k=0..7} \left\{ |K_k * f(x,y)| \right\}, \quad \phi(x,y) = k_{\max} \times 45^\circ
```

---

<a id="module-53-second-order-edge-operators-laplacian-log-marr-hildreth"></a>

## Module 5.3: Second-Order Edge Operators (Laplacian & LoG / Marr-Hildreth)

<a id="pyq-531-2d-discrete-laplacian-operator-derivation-mask-formulation"></a>

### PYQ 5.3.1: 2D Discrete Laplacian Operator Derivation & Mask Formulation

#### ❓ Question Statement
* **Source:** AKTU University Paper 2017–18 [Q2.26] / DIP Question Bank — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Question:** Derive the discrete 2D Laplacian operator equation from partial second-order central differences. Show how it is represented as $3 \times 3$ spatial masks for 4-neighbor and 8-neighbor configurations.

---

#### 💡 Model Answer

##### 1. Mathematical Derivation
The continuous 2D Laplacian operator $\nabla^2 f$ is defined as the sum of second partial derivatives along $x$ and $y$:

```math
\nabla^2 f(x,y) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}
```

Approximating second partial derivatives using 1D central finite differences:

```math
\frac{\partial^2 f}{\partial x^2} = f(x+1, y) + f(x-1, y) - 2f(x,y)
```

```math
\frac{\partial^2 f}{\partial y^2} = f(x, y+1) + f(x, y-1) - 2f(x,y)
```

Summing both partial derivatives yields the **4-Neighbor Discrete Laplacian**:

```math
\nabla^2_4 f(x,y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4f(x,y)
```

---

##### 2. 4-Neighbor and 8-Neighbor Mask Representations

1. **4-Neighbor Mask $L_4$ (Negative Center Weight):**

```math
L_4 = \begin{bmatrix}
0 & +1 & 0 \\
+1 & -4 & +1 \\
0 & +1 & 0
\end{bmatrix}
```

2. **8-Neighbor Mask $L_8$ (Includes Diagonal Differences):**
Adding diagonal central difference terms yields the isotropic **8-Neighbor Discrete Laplacian**:

```math
L_8 = \begin{bmatrix}
+1 & +1 & +1 \\
+1 & -8 & +1 \\
+1 & +1 & +1
\end{bmatrix}
```

---

<a id="pyq-532-laplacian-filter-convolution-on-center-pixel"></a>

### PYQ 5.3.2: Laplacian Filter Convolution on Center Pixel

#### ❓ Question Statement
* **Source:** SVKM's NMIMS MPSTME, Semester V Final Exam Dec 2025 [Q1b] — *[Reported PYQ (unverified)]*
* **Marks:** 4 Marks
* **Exact Wording:** Consider the following $3 \times 3$ grayscale image region:


```math
I = \begin{bmatrix}
10 & 20 & 30 \\
40 & 50 & 60 \\
70 & 80 & 90
\end{bmatrix}
```

Using a Laplacian filter having positive centre without diagonal elements for sharpening, compute the output value at the center pixel (50).

---

#### 💡 Model Answer

##### 1. Filter Mask Identification
* **Filter Type:** 4-neighbor Laplacian mask with **positive center weight** (without diagonal elements):

```math
L_4^+ = \begin{bmatrix}
0 & -1 & 0 \\
-1 & +4 & -1 \\
0 & -1 & 0
\end{bmatrix}
```

---

##### 2. Step-by-Step Convolution Calculation

Given $3 \times 3$ region $I$:

```math
I = \begin{bmatrix}
10 & 20 & 30 \\
40 & 50 & 60 \\
70 & 80 & 90
\end{bmatrix}
```

Overlaying mask $L_4^+$ centered at $f(1,1) = 50$:

```math
\text{Output Response } R = 0\cdot 10 + (-1)\cdot 20 + 0\cdot 30 + (-1)\cdot 40 + (+4)\cdot 50 + (-1)\cdot 60 + 0\cdot 70 + (-1)\cdot 80 + 0\cdot 90
```

```math
R = -20 - 40 + 200 - 60 - 80 = -200 + 200 = \mathbf{0}
```

---

##### 3. Physical Interpretation
The $3 \times 3$ region forms a **perfect linear intensity plane** ($f(x,y) = 10x + 30y + 10$). Because a 2D plane has zero second derivative / curvature everywhere ($\nabla^2 f = 0$), the Laplacian output evaluates to exactly **$0$**, confirming zero sharpening adjustment needed on flat/linear regions.

---

<a id="pyq-533-laplacian-of-gaussian-log-operator-zero-crossing-method"></a>

### PYQ 5.3.3: Laplacian of Gaussian (LoG) Operator & Zero-Crossing Method

#### ❓ Question Statement
* **Source:** AKTU University Paper / DIP Question Bank — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Question:** Explain the Laplacian of Gaussian (LoG) / Marr-Hildreth edge detector. Why is Gaussian smoothing required prior to applying the Laplacian? How are edges extracted using zero-crossing detection?

---

#### 💡 Model Answer

##### 1. Motivation: Gaussian Smoothing + Laplacian
The continuous 2D Laplacian operator $\nabla^2 f$ is rotationally symmetric, but its discrete masks are only approximately so, but it suffers from extreme **sensitivity to high-frequency noise**.

To overcome this limitation, the **Laplacian of Gaussian (LoG)** operator pre-smooths the image with a 2D Gaussian filter $G_\sigma(x,y)$ before taking the Laplacian:

```math
\text{LoG}(x,y) = \nabla^2 \left[ G_\sigma(x,y) * f(x,y) \right] = \left[ \nabla^2 G_\sigma(x,y) \right] * f(x,y)
```

---

##### 2. Mathematical Expression of 2D LoG Kernel
Taking second partial derivatives of the 2D Gaussian $G_\sigma(x,y) = e^{-\frac{x^2+y^2}{2\sigma^2}}$ yields the **Mexican Hat function**:

```math
\nabla^2 G_\sigma(x,y) = -\frac{1}{\pi \sigma^4} \left[ 1 - \frac{x^2 + y^2}{2\sigma^2} \right] e^{-\frac{x^2 + y^2}{2\sigma^2}}
```

---

##### 3. Zero-Crossing Edge Extraction Method
1. The LoG-filtered image produces a double-line response across edges (positive on the dark side, negative on the light side).
2. **Zero-Crossing Rule:** A pixel $P(x,y)$ is marked as an edge pixel if its LoG value changes sign across any of the 4 oppositional neighbor pairs (Left/Right, Top/Bottom, Diagonal 1, Diagonal 2) and the sign transition slope exceeds a noise threshold $T$:

```math
\text{Zero Crossing if } \left( \text{LoG}(x-1, y) \times \text{LoG}(x+1, y) < 0 \right) \text{ and } |\text{LoG}_1 - \text{LoG}_2| > T
```

---

<a id="module-54-multi-stage-canny-edge-detector"></a>

## Module 5.4: Multi-Stage Canny Edge Detector

<a id="pyq-541-canny-edge-detector-optimal-criteria-5-stage-pipeline"></a>

### PYQ 5.4.1: Canny Edge Detector Optimal Criteria & 5-Stage Pipeline

#### ❓ Question Statement
* **Source:** AKTU University Paper / DIP Question Bank — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Question:** Explain Canny's three optimal edge detection criteria. Describe the complete 5-stage Canny edge detection pipeline with neat block diagrams and equations.

---

#### 💡 Model Answer

##### 1. Canny's Three Optimal Edge Criteria
John Canny (1986) formulated edge detection as an optimal mathematical tradeoff:
1. **Low Error Rate (Good Detection):** The detector must mark real edges and avoid false edges caused by noise.
2. **Good Edge Localization:** Marked edge pixels must be as close as possible to the true physical edge center.
3. **Single Response Criterion:** The detector aims to produce one thin response to a single physical edge, suppressing multiple local maxima.

---

##### 2. Complete 5-Stage Canny Pipeline

```text
[ Input Image ] ──► [ 1. Gaussian Filter ] ──► [ 2. Sobel Gradient (M, θ) ]
                         │
                         ▼
[ Final Edges ] ◄── [ 5. Hysteresis ] ◄── [ 4. Double Threshold ] ◄── [ 3. NMS Thinning ]
```

1. **Stage 1: Gaussian Noise Reduction:**
   Convolves image $f(x,y)$ with a 2D Gaussian kernel $G_\sigma$ to suppress high-frequency noise.
2. **Stage 2: Gradient Vector & Direction Computation:**
   Applies Sobel operators to compute horizontal $G_x$ and vertical $G_y$ gradients, magnitude $M = \sqrt{G_x^2 + G_y^2}$, and direction $\theta = \text{atan2}(G_y, G_x)$.
3. **Stage 3: Non-Maximum Suppression (NMS):**
   Quantizes angle $\theta$ into 4 sector directions ($0^\circ, 45^\circ, 90^\circ, 135^\circ$). Compares magnitude $M(x,y)$ against its two immediate sector neighbors. If $M(x,y)$ is not strictly greater than both neighbors, it is thinned to $0$.
4. **Stage 4: Double Thresholding:**
   Classifies thinned magnitude pixels using two thresholds ($T_{\text{high}}$ and $T_{\text{low}}$):
   * $M \ge T_{\text{high}} \implies \text{Strong Edge Pixel (255)}$.
   * $T_{\text{low}} \le M < T_{\text{high}} \implies \text{Weak Edge Pixel (128)}$.
   * $M < T_{\text{low}} \implies \text{Rejected Non-Edge (0)}$.
5. **Stage 5: Edge Tracking by Hysteresis:**
   Promotes a Weak Edge pixel to a Strong Edge if it is connected to at least one Strong Edge pixel in its 8-neighborhood; otherwise rejects it.

---

<a id="pyq-542-canny-non-maximum-suppression-nms-gradient-sector-quantization"></a>

### PYQ 5.4.2: Canny Non-Maximum Suppression (NMS) & Gradient Sector Quantization

#### ❓ Question Statement
* **Source:** Practice Question — *[Practice Question]*
* **Marks:** 6 Marks
* **Question:** Given a thinned gradient magnitude matrix $M$ and quantized direction matrix $\Theta$, perform Non-Maximum Suppression (NMS) at center pixel $M(2,2) = 120$ with sector direction $0^\circ$ (horizontal).


```math
M = \begin{bmatrix}
40 & 50 & 30 \\
100 & 120 & 90 \\
20 & 30 & 40
\end{bmatrix}, \quad \Theta(2,2) = 0^\circ
```


---

#### 💡 Model Answer

##### 1. NMS Neighbor Selection Rule for Sector $0^\circ$
* **Sector $0^\circ$ (Horizontal Gradient Direction):** The gradient vector points horizontally across columns. Therefore, the perpendicular edge runs vertically.
* **NMS Comparison Neighbors:** Left neighbor $M(2,1) = 100$ and Right neighbor $M(2,3) = 90$.

---

##### 2. NMS Comparison Calculation
* Center pixel magnitude: $M(2,2) = \mathbf{120}$.
* Left neighbor: $M(2,1) = 100$.
* Right neighbor: $M(2,3) = 90$.

Since $M(2,2) = 120 > 100$ AND $M(2,2) = 120 > 90$, $M(2,2)$ is a **local maximum along its gradient sector**.

```math
\text{NMS Output } M_{\text{NMS}}(2,2) = \mathbf{120} \quad (\text{Preserved as a thin ridge pixel})
```

---

<a id="pyq-543-canny-double-thresholding-hysteresis-edge-tracking"></a>

### PYQ 5.4.3: Canny Double Thresholding & Hysteresis Edge Tracking

#### ❓ Question Statement
* **Source:** Practice Question — *[Practice Question]*
* **Marks:** 6 Marks
* **Question:** Given an NMS-thinned gradient magnitude matrix $M$, apply double thresholding with $T_{\text{high}} = 80$ and $T_{\text{low}} = 30$, followed by 8-connected hysteresis edge tracking:


```math
M = \begin{bmatrix}
20 & 10 & 40 & 10 & 0 \\
10 & 25 & 50 & 20 & 0 \\
0 & 90 & 85 & 45 & 10 \\
0 & 35 & 40 & 10 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
```


---

#### 💡 Model Answer

##### Step 1: Double Thresholding Classification
* $M(x,y) \ge 80 \implies \mathbf{Strong Edge (S = 255)}$.
* $30 \le M(x,y) < 80 \implies \mathbf{Weak Edge (W = 128)}$.
* $M(x,y) < 30 \implies \mathbf{Rejected Non-Edge (0)}$.

Classified Matrix $T$:

```math
T = \begin{bmatrix}
0 & 0 & W(40) & 0 & 0 \\
0 & 0 & W(50) & 0 & 0 \\
0 & S(90) & S(85) & W(45) & 0 \\
0 & W(35) & W(40) & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

---

##### Step 2: Hysteresis Edge Tracking (8-Connectivity)
1. **Strong Pixels:** $(2,1) = 90$ and $(2,2) = 85$.
2. **Weak Pixel Analysis:**
   * $(0,2) = 40$: 8-neighbors contain $W(50)$ at $(1,2)$, which is 8-connected to the strong pixel $(2,2)$; the weak chain reaches a strong pixel $\implies \mathbf{Promoted (255)}$.
   * $(1,2) = 50$: 8-neighbors contain Strong pixels $S(90)$ at $(2,1)$ and $S(85)$ at $(2,2) \implies \mathbf{Promoted (255)}$.
   * $(2,3) = 45$: 8-neighbor is Strong pixel $S(85)$ at $(2,2) \implies \mathbf{Promoted (255)}$.
   * $(3,1) = 35$: 8-neighbor is Strong pixel $S(90)$ at $(2,1) \implies \mathbf{Promoted (255)}$.
   * $(3,2) = 40$: 8-neighbors include Strong pixel $S(85)$ at $(2,2) \implies \mathbf{Promoted (255)}$.

---

##### Final Binary Edge Map $E(x,y)$:

```math
E(x,y) = \begin{bmatrix}
0 & 0 & 255 & 0 & 0 \\
0 & 0 & 255 & 0 & 0 \\
0 & 255 & 255 & 255 & 0 \\
0 & 255 & 255 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

---

<a id="module-55-comprehensive-operator-comparisons-analysis"></a>

## Module 5.5: Comprehensive Operator Comparisons & Analysis

<a id="pyq-551-comparative-analysis-matrix-of-edge-detection-operators"></a>

### PYQ 5.5.1: Comparative Analysis Matrix of Edge Detection Operators

#### ❓ Question Statement
* **Source:** AKTU University Paper / DIP Question Bank — *[Reported PYQ (unverified)]*
* **Marks:** 10 Marks
* **Question:** Compare Prewitt, Sobel, Laplacian, Laplacian of Gaussian (LoG), and Canny edge detection operators across derivative order, noise robustness, edge thickness, localization accuracy, and computational complexity.

---

#### 💡 Model Answer

##### Master Edge Operator Comparison Matrix

| Operator | Derivative Order | Mask Support | Noise Robustness | Edge Thickness | Localization Accuracy | Primary Application / Strength |
|---|---|---|---|---|---|---|
| **Prewitt** | 1st Order | $3 \times 3$ | Moderate (Box Smoothing) | Thick (Multi-pixel) | Moderate | Simple first-order gradient estimation |
| **Sobel** | 1st Order | $3 \times 3$ | Good (Weighted Smoothing) | Thick (Multi-pixel) | Moderate | Standard fast gradient edge detector |
| **Laplacian** | 2nd Order | $3 \times 3$ | Poor (Highly Noise Sensitive) | Fine Double-Lines | Poor (Ringing) | Second-derivative curvature detection |
| **LoG** | 2nd Order | Scale-dependent | Depends on smoothing scale | Zero-crossing contours (thickness depends on extraction) | High (Zero-Crossings) | Closed contour detection & scale space |
| **Canny** | 1st Order + Multi-Stage | $3 \times 3 \dots 5 \times 5$ | Parameter-dependent (Multi-Stage Pipeline) | Single-Pixel Thin | High (NMS + Hysteresis) | Multi-stage detector with localization/noise trade-offs |

---

<a id="topic-wise-question-index-source-verification-directory"></a>

## Topic-Wise Question Index & Source Status Directory

| Module | PYQ Identifier | Topic Covered | Verification Status | Source Reference |
|---|---|---|---|---|
| **5.1** | PYQ 5.1.1 | 1D First & Second Derivatives | **Reported PYQ (unverified)** | NMIMS Re-Exam May 2024 [Q3a] |
| **5.1** | PYQ 5.1.2 | 1D Scanline Derivatives | **Practice Question** | University Tutorial Sets |
| **5.1** | PYQ 5.1.3 | 2D Gradient Vector & Direction | **Practice Question** | Class Notes |
| **5.2** | PYQ 5.2.1 | Prewitt Gradient Direction Angle | **Reported PYQ (unverified)** | NMIMS Final Exam Dec 2025 [Q5a] |
| **5.2** | PYQ 5.2.2 | Sobel Convolution with Border Replication | **Reported PYQ (unverified)** | NMIMS Final Exam Dec 2025 [Q3b] |
| **5.2** | PYQ 5.2.3 | Prewitt Horizontal, Vertical & Diagonal | **Reported PYQ (unverified)** | NMIMS Re-Exam May 2025 [Q2b] |
| **5.2** | PYQ 5.2.4 | Sobel Vector & Edge Strength Comparison | **Reported PYQ (unverified)** | NMIMS Final Exam Nov/Dec 2022 [Q5b] |
| **5.2** | PYQ 5.2.5 | Prewitt Operator with Zero Padding | **Reported PYQ (unverified)** | NMIMS Final Exam Nov/Dec 2022 [Q5a] |
| **5.2** | PYQ 5.2.6 | Sobel vs. Prewitt Performance & Smoothing | **Reported PYQ (unverified)** | NMIMS Re-Exam May 2024 [Q5a] |
| **5.2** | PYQ 5.2.7 | Sobel & Prewitt Masks on Step Image | **Reported PYQ (unverified)** | NMIMS Special Re-Exam Jan 2023 [Q5a] |
| **5.2** | PYQ 5.2.8 | Kirsch Compass Operator 8 Masks | **Reported PYQ (unverified)** | AKTU Question Bank `*(Supporting)*` |
| **5.3** | PYQ 5.3.1 | 2D Laplacian Derivation & Masks | **Reported PYQ (unverified)** | AKTU Question Bank |
| **5.3** | PYQ 5.3.2 | Laplacian Filter Convolution Center Pixel | **Reported PYQ (unverified)** | NMIMS Final Exam Dec 2025 [Q1b] |
| **5.3** | PYQ 5.3.3 | LoG Operator & Zero-Crossing Method | **Reported PYQ (unverified)** | AKTU Question Bank |
| **5.4** | PYQ 5.4.1 | Canny 3 Criteria & 5-Stage Pipeline | **Reported PYQ (unverified)** | AKTU Question Bank |
| **5.4** | PYQ 5.4.2 | Canny NMS & Gradient Sectoring | **Practice Question** | Class Notes |
| **5.4** | PYQ 5.4.3 | Canny Double Thresholding & Hysteresis | **Practice Question** | Class Notes |
| **5.5** | PYQ 5.5.1 | Operator Comparative Analysis Matrix | **Reported PYQ (unverified)** | AKTU Question Bank |

---

<a id="repeated-equivalent-questions-directory"></a>

## Repeated & Equivalent Questions Directory

* **Sobel & Prewitt Mask Application on Step Edge Images:**
  * Appears in **NMIMS Dec 2025 [Q3b]**, **NMIMS May 2025 [Q2b]**, **NMIMS Nov/Dec 2022 [Q5b]**, **NMIMS May 2024 [Q5a]**, and **NMIMS Jan 2023 [Q5a]**.
  * *Note:* All 5 occurrences test first-order gradient convolution, but use different input matrices ($4 \times 4$ vs $5 \times 5$ vs $6 \times 6$) and intensity step heights.
* **1D / 2D Derivative Calculations:**
  * Appears in **NMIMS May 2024 [Q3a]** and **NMIMS Dec 2025 [Q5a]**.

---

<a id="verification-checklist-final-audit"></a>

## Verification Checklist & Final Audit

* [x] Every question entry includes a source-status label (**Reported PYQ (unverified)** or **Practice Question**); original papers must be checked before any entry is called verified.
* [x] Reported paper attributions, marks, and question numbers retained from the supplied workbook; original papers are needed to verify them.
* [x] Supporting topics (diagonal masks, Kirsch compass) are explicitly flagged as **(Supporting topic outside the supplied Unit 5 syllabus)**.
* [x] Multirow matrices and spatial masks are presented in standalone GitHub math blocks with one row per source line.
* [x] Table of contents links point to explicit section anchors.
* [x] Worked calculations have been corrected where the supplied matrices and masks permit checking; paper-source verification and any unstated operator conventions remain outstanding.

