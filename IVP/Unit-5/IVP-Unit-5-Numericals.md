# 📚 IVP Unit 5: Edge Detection — Solved Numerical Workbook

---

## 📌 Document Overview & Syllabus Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 5 — Edge Detection (Complete Numerical Problem Bank)
* **Target Audience:** B.Tech / M.Tech Computer Engineering & EXTC Students
* **Format:** GitHub Flavored Markdown (GFM) with Standalone ```math LaTeX Blocks
* **Syllabus Scope Boundary:** This workbook is strictly limited to the prescribed Unit 5 syllabus topics:
  1. First-order and second-order derivative approximations on 1D scanlines and 2D spatial matrices.
  2. Gradient vector calculation, exact magnitude $G = \sqrt{G_x^2 + G_y^2}$, Manhattan sum approximation $|G_x| + |G_y|$, and direction angle $\theta = \text{atan2}(G_y, G_x)$.
  3. $3 \times 3$ Prewitt and Sobel spatial mask convolutions ($G_x$ horizontal, $G_y$ vertical, diagonal Sobel, and Kirsch compass operator sets).
  4. Second-order edge operators: $3 \times 3$ 4-neighbor and 8-neighbor discrete Laplacian convolution, center-weight sign rules ($g = f - \nabla^2 f$ vs. $g = f + \nabla^2 f$), and $5 \times 5$ Discrete Laplacian of Gaussian (LoG) zero-crossing detection.
  5. Canny edge detector multi-stage calculations: Gaussian smoothing, Sobel gradient sector quantization ($0^\circ, 45^\circ, 90^\circ, 135^\circ$), Non-Maximum Suppression (NMS), double thresholding ($T_{\text{high}}, T_{\text{low}}$), and 8-connected hysteresis connectivity tracking.

---

## ⚙️ Correlation vs. Convolution Convention

Every worked numerical in this workbook that writes $f * M$ for a mask $M$ actually performs **cross-correlation**: the mask is applied exactly as printed, with elementwise multiplication against the underlying image patch followed by summation — **no 180° mask flip**. This is the standard convention used in essentially all IVP exam numericals, and is what every worked calculation below actually does.

**True mathematical convolution** additionally flips the mask by $180^\circ$ (both rows and columns reversed) before the same elementwise-multiply-and-sum step. For every **antisymmetric** derivative mask used in this workbook (Prewitt $M_x, M_y$; Sobel $S_x, S_y$; diagonal Sobel $S_{\pm45^\circ}$; Kirsch masks $K_k$), flipping the mask $180^\circ$ reverses the **sign** of the computed response but leaves its **magnitude** unchanged — so $G = \sqrt{G_x^2+G_y^2}$ is identical either way, while $\theta = \text{atan2}(G_y, G_x)$ shifts by $180^\circ$. For the **symmetric** Laplacian and LoG masks used in Section 3, a $180^\circ$ flip leaves the mask (and therefore the response) completely unchanged.

**Bottom line:** treat every $f * M$ expression below as cross-correlation (masks applied as printed). If your course or textbook instead specifies true convolution, flip the sign of $G_x$/$G_y$ (add $180^\circ$ to $\theta$) for the antisymmetric masks; the Laplacian/LoG numericals in Section 3 need no change either way.

---

## 🏷️ Source Attribution & Verification Rules

In strict compliance with academic standards, every problem in this document carries an explicit source label:
* **Verified PYQ:** Checked against original paper sources with institution name, examination session, question number, and marks allocation.
* **Reported PYQ (unverified):** Sourced from reported student PYQ compilations or classroom tutorial sheets where original PDF papers were not directly available.
* **Practice Problem:** Newly constructed exam-oriented problem designed to cover crucial syllabus sub-topics, edge cases, and multi-stage pipeline algorithms.

> ⚠️ **Current verification status:** No problem in this version of the workbook has had its original question paper independently checked. The three problems previously marked *Verified PYQ* (Numericals 2.2, 3.1, and 4.3) have been downgraded to **Reported PYQ (unverified)** — their institution, session, and question numbers are preserved as reported, but should be treated as unverified attributions until the actual papers are checked. All numerical working itself (the calculations, not the source labels) has been independently recomputed and confirmed correct.

---

## 📑 Table of Contents

1. [Section 1: 1D & 2D First and Second Derivative Numericals](#section-1-1d-2d-first-and-second-derivative-numericals)
   * 1.1 [Numerical 1.1: 1D Scanline Derivatives across Step, Ramp, and Roof Edges](#numerical-11-1d-scanline-derivatives-across-step-ramp-and-roof-edges) — *[Reported PYQ (unverified)]*
   * 1.2 [Numerical 1.2: 2D Gradient Vector, Exact Magnitude, Approximation, and Direction Angle Calculation](#numerical-12-2d-gradient-vector-exact-magnitude-approximation-and-direction-angle-calculation) — *[Practice Problem]*
2. [Section 2: First-Order Gradient Mask Numericals (Prewitt & Sobel Operators)](#section-2-first-order-gradient-mask-numericals-prewitt-sobel-operators)
   * 2.1 [Numerical 2.1: 3 x 3 Prewitt Operator Convolution on a Vertical Edge Patch](#numerical-21-3-x-3-prewitt-operator-convolution-on-a-vertical-edge-patch) — *[Reported PYQ (unverified)]*
   * 2.2 [Numerical 2.2: 3 x 3 Sobel Operator Convolution on a 5 x 5 Image Matrix](#numerical-22-3-x-3-sobel-operator-convolution-on-a-5-x-5-image-matrix) — *[Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2025-26]*
   * 2.3 [Numerical 2.3: Diagonal Sobel Operator Convolution (+45° and -45° Masks)](#numerical-23-diagonal-sobel-operator-convolution-45-and-45-masks) — *[Practice Problem]*
   * 2.4 [Numerical 2.4: Kirsch Compass Operator 8-Directional Maximum Response Calculation](#numerical-24-kirsch-compass-operator-8-directional-maximum-response-calculation) — *[Practice Problem]*
3. [Section 3: Second-Order Operator Numericals (Laplacian & LoG Zero-Crossings)](#section-3-second-order-operator-numericals-laplacian-log-zero-crossings)
   * 3.1 [Numerical 3.1: 4-Neighbor vs. 8-Neighbor Laplacian Convolution on a Step Edge Image](#numerical-31-4-neighbor-vs-8-neighbor-laplacian-convolution-on-a-step-edge-image) — *[Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2022-23]*
   * 3.2 [Numerical 3.2: Laplacian Center-Weight Sign Conventions and Edge Sharpening Analysis](#numerical-32-laplacian-center-weight-sign-conventions-and-edge-sharpening-analysis) — *[Practice Problem]*
   * 3.3 [Numerical 3.3: 5 x 5 Discrete Laplacian of Gaussian (LoG) Convolution and Zero-Crossing Extraction](#numerical-33-5-x-5-discrete-laplacian-of-gaussian-log-convolution-and-zero-crossing-extraction) — *[Reported PYQ (unverified)]*
4. [Section 4: Canny Edge Detector Multi-Stage Pipeline Numericals](#section-4-canny-edge-detector-multi-stage-pipeline-numericals)
   * 4.1 [Numerical 4.1: Canny Step 2 — Gradient Magnitude and Sector Quantization (Given Pre-Computed Sobel Values)](#numerical-41-canny-step-2-gradient-magnitude-and-sector-quantization-given-pre-computed-sobel-values) — *[Practice Problem]*
   * 4.2 [Numerical 4.2: Canny Step 3 — Non-Maximum Suppression (NMS) on a 5 x 5 Gradient Matrix](#numerical-42-canny-step-3-non-maximum-suppression-nms-on-a-5-x-5-gradient-matrix) — *[Reported PYQ (unverified)]*
   * 4.3 [Numerical 4.3: Canny Step 4 & 5 — Double Thresholding and 8-Connected Hysteresis Edge Tracking](#numerical-43-canny-step-4-5-double-thresholding-and-8-connected-hysteresis-edge-tracking) — *[Reported PYQ (unverified) — SVKM's NMIMS Re-Exam 2023-24]*
   * 4.4 [Numerical 4.4: Complete End-to-End Canny Pipeline Walkthrough on a 5 x 5 Image Matrix](#numerical-44-complete-end-to-end-canny-pipeline-walkthrough-on-a-5-x-5-image-matrix) — *[Practice Problem]*
5. [Section 5: Formula Master Reference Sheet](#section-5-formula-master-reference-sheet)
6. [Section 6: Summary Answer Index Table](#section-6-summary-answer-index-table)
7. [Section 7: Common Numerical Mistakes & Pitfalls](#section-7-common-numerical-mistakes-pitfalls)
8. [Section 8: Source Status & Verification Checklist](#section-8-source-status-verification-checklist)

---

## Section 1: 1D & 2D First and Second Derivative Numericals

### Numerical 1.1: 1D Scanline Derivatives across Step, Ramp, and Roof Edges

#### ❓ Problem Statement
An image scanline $f(x)$ contains 12 spatial sample points representing various intensity edge profiles:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $f(x)$ | 5 | 5 | 5 | 5 | 15 | 25 | 35 | 35 | 35 | 10 | 35 | 35 |

1. Compute the **first forward difference** $\frac{\partial f}{\partial x}_{\text{forward}} = f(x+1) - f(x)$.
2. Compute the **first central difference** $\frac{\partial f}{\partial x}_{\text{central}} = \frac{f(x+1) - f(x-1)}{2}$.
3. Compute the **second central difference** $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$.
4. Identify the edge types present across intervals $x \in [2,7]$, $x \in [7,9]$, and $x=9$.

---

#### 💡 Step-by-Step Solution

##### 1. First Forward Difference Calculation $\frac{\partial f}{\partial x}_{\text{forward}} = f(x+1) - f(x)$:
* $x=0$: $5 - 5 = 0$
* $x=1$: $5 - 5 = 0$
* $x=2$: $5 - 5 = 0$
* $x=3$: $15 - 5 = +10$
* $x=4$: $25 - 15 = +10$
* $x=5$: $35 - 25 = +10$
* $x=6$: $35 - 35 = 0$
* $x=7$: $35 - 35 = 0$
* $x=8$: $10 - 35 = -25$
* $x=9$: $35 - 10 = +25$
* $x=10$: $35 - 35 = 0$

##### 2. First Central Difference Calculation $\frac{\partial f}{\partial x}_{\text{central}} = \frac{f(x+1) - f(x-1)}{2}$ (for interior points $x=1$ to $10$):
* $x=1$: $\frac{5 - 5}{2} = 0.0$
* $x=2$: $\frac{5 - 5}{2} = 0.0$
* $x=3$: $\frac{15 - 5}{2} = +5.0$
* $x=4$: $\frac{25 - 5}{2} = +10.0$
* $x=5$: $\frac{35 - 15}{2} = +10.0$
* $x=6$: $\frac{35 - 25}{2} = +5.0$
* $x=7$: $\frac{35 - 35}{2} = 0.0$
* $x=8$: $\frac{10 - 35}{2} = -12.5$
* $x=9$: $\frac{35 - 35}{2} = 0.0$
* $x=10$: $\frac{35 - 10}{2} = +12.5$

##### 3. Second Central Difference Calculation $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$:
* $x=1$: $5 + 5 - 2(5) = 0$
* $x=2$: $5 + 5 - 2(5) = 0$
* $x=3$: $15 + 5 - 2(5) = +10$ (Positive peak at ramp onset)
* $x=4$: $25 + 5 - 2(15) = 0$
* $x=5$: $35 + 15 - 2(25) = 0$
* $x=6$: $35 + 25 - 2(35) = -10$ (Negative peak at ramp end)
* $x=7$: $35 + 35 - 2(35) = 0$
* $x=8$: $10 + 35 - 2(35) = -25$
* $x=9$: $35 + 35 - 2(10) = +50$ (Strong positive response at roof valley)
* $x=10$: $35 + 10 - 2(35) = -25$

##### 4. Summary Table of 1D Scanline Derivatives:

| Metric / Index $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $f(x)$ | 5 | 5 | 5 | 5 | 15 | 25 | 35 | 35 | 35 | 10 | 35 | 35 |
| $\frac{\partial f}{\partial x}_{\text{fwd}}$ | 0 | 0 | 0 | +10 | +10 | +10 | 0 | 0 | -25 | +25 | 0 | — |
| $\frac{\partial f}{\partial x}_{\text{cent}}$ | — | 0 | 0 | +5 | +10 | +10 | +5 | 0 | -12.5 | 0 | +12.5 | — |
| $\frac{\partial^2 f}{\partial x^2}$ | — | 0 | 0 | **+10** | 0 | 0 | **-10** | 0 | **-25** | **+50** | **-25** | — |

##### 🧠 Observations & Edge Profile Identification:
1. **Ramp Edge ($x \in [3,6]$):** Intensity transitions linearly from $5 \to 35$. The first derivative yields a constant non-zero plateau ($+10$), producing a **thick edge line**. The second derivative yields a **double-response pair**: $+10$ at the dark side ($x=3$) and $-10$ at the light side ($x=6$). The zero-crossing point between $x=3$ and $x=6$ pinpoints the exact ramp midpoint ($x=4.5$).
2. **Line / Roof Edge / Valley ($x=9$):** Intensity dips sharply from $35 \to 10 \to 35$. The second derivative generates a strong positive impulse ($+50$) flanked by negative lobes ($-25$), demonstrating high sensitivity to fine line structures.

---

### Numerical 1.2: 2D Gradient Vector, Exact Magnitude, Approximation, and Direction Angle Calculation

#### ❓ Problem Statement
At spatial location $(x,y)$ in an image, the horizontal partial derivative is calculated as $G_x = \frac{\partial f}{\partial x} = +40$ and the vertical partial derivative is $G_y = \frac{\partial f}{\partial y} = -30$.

1. Construct the 2D gradient vector $\nabla f$.
2. Calculate the **exact Euclidean gradient magnitude** $G = ||\nabla f||_2$.
3. Calculate the **Manhattan distance gradient magnitude approximation** $G_{\text{approx}} = ||\nabla f||_1$.
4. Calculate the **exact gradient direction angle** $\theta = \text{atan2}(G_y, G_x)$ in degrees.
5. Determine the **edge-line orientation angle** $\phi$.

---

#### 💡 Step-by-Step Solution

##### 1. 2D Gradient Vector $\nabla f$:

```math
\nabla f = \begin{bmatrix} G_x \\ G_y \end{bmatrix} = \begin{bmatrix} +40 \\ -30 \end{bmatrix}
```

##### 2. Exact Euclidean Gradient Magnitude $G$:

```math
G = \sqrt{G_x^2 + G_y^2} = \sqrt{(40)^2 + (-30)^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50.0
```

##### 3. Manhattan Magnitude Approximation $G_{\text{approx}}$:

```math
G_{\text{approx}} = |G_x| + |G_y| = |40| + |-30| = 40 + 30 = 70.0
```

> ⚠️ **Note on Approximation Error:** The $L_1$ norm overestimates the Euclidean magnitude by $\frac{70 - 50}{50} = 40\%$. However, it is widely used in real-time hardware due to avoiding expensive square-root operations.

##### 4. Gradient Direction Angle $\theta$:
Using four-quadrant arctangent $\theta = \text{atan2}(G_y, G_x)$:

```math
\theta = \tan^{-1}\left(\frac{-30}{+40}\right) = \tan^{-1}(-0.75) \approx -36.87^\circ \quad (\text{or } 323.13^\circ)
```

##### 5. Edge Line Orientation Angle $\phi$:
The edge line runs **perpendicular** to the gradient direction vector:

```math
\phi = \theta \pm 90^\circ = -36.87^\circ + 90^\circ = +53.13^\circ
```

```text
       ASCII Vector Orientation Diagram:

                 Y-Axis (Up)
                     ^
                     |      / Edge Line (phi = +53.13 deg)
                     |     /
                     |    /
                     |   /
   ------------------+--+-----------------> X-Axis (Right)
                     |    \
                     |     \  Gradient Vector
                     |      \ (theta = -36.87 deg)
                     |       v
```

---

## Section 2: First-Order Gradient Mask Numericals (Prewitt & Sobel Operators)

### Numerical 2.1: 3 x 3 Prewitt Operator Convolution on a Vertical Edge Patch

#### ❓ Problem Statement
Given a $3 \times 3$ image patch $f(x,y)$ exhibiting a vertical step edge:

```math
f(x,y) = \begin{bmatrix} 10 & 10 & 50 \\ 10 & 10 & 50 \\ 10 & 10 & 50 \end{bmatrix}
```

Apply the standard $3 \times 3$ Prewitt spatial operator masks (applied as printed — cross-correlation; see the *Correlation vs. Convolution Convention* note above):

```math
M_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}, \quad M_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}
```

1. Compute the horizontal gradient response $G_x = f * M_x$ (cross-correlation).
2. Compute the vertical gradient response $G_y = f * M_y$.
3. Compute the exact gradient magnitude $G = \sqrt{G_x^2 + G_y^2}$.
4. Compute the gradient direction angle $\theta = \text{atan2}(G_y, G_x)$.

---

#### 💡 Step-by-Step Solution

##### 1. Horizontal Response $G_x$ (Element-by-Element Sum of Products):

```math
G_x = (-1)(10) + (0)(10) + (1)(50) + (-1)(10) + (0)(10) + (1)(50) + (-1)(10) + (0)(10) + (1)(50)
```

```math
G_x = (-10 + 0 + 50) + (-10 + 0 + 50) + (-10 + 0 + 50) = 40 + 40 + 40 = +120
```

##### 2. Vertical Response $G_y$:

```math
G_y = (-1)(10) + (-1)(10) + (-1)(50) + (0)(10) + (0)(10) + (0)(50) + (1)(10) + (1)(10) + (1)(50)
```

```math
G_y = (-10 - 10 - 50) + 0 + (10 + 10 + 50) = -70 + 0 + 70 = 0
```

##### 3. Exact Gradient Magnitude $G$:

```math
G = \sqrt{G_x^2 + G_y^2} = \sqrt{(120)^2 + 0^2} = 120.0
```

##### 4. Gradient Direction Angle $\theta$:

```math
\theta = \text{atan2}(0, 120) = 0^\circ
```

> 🧠 **Interpretation:** The gradient direction is $0^\circ$ (pointing horizontally right, directly across the intensity step), confirming that the edge line is perfectly vertical ($\phi = 90^\circ$).

---

### Numerical 2.2: 3 x 3 Sobel Operator Convolution on a 5 x 5 Image Matrix

#### ❓ Problem Statement
Given a $5 \times 5$ grayscale image $I(x,y)$:

```math
I(x,y) = \begin{bmatrix} 50 & 50 & 50 & 100 & 100 \\ 50 & 50 & 50 & 100 & 100 \\ 50 & 50 & 50 & 100 & 100 \\ 50 & 50 & 50 & 100 & 100 \\ 50 & 50 & 50 & 100 & 100 \end{bmatrix}
```

Apply the standard $3 \times 3$ Sobel operator masks with center smoothing weight of $2$:

```math
S_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad S_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
```

Compute the interior $3 \times 3$ response matrices for $G_x(x,y)$, $G_y(x,y)$, and the gradient magnitude matrix $G(x,y)$.

---

#### 💡 Step-by-Step Solution

##### 1. Horizontal Response Matrix $G_x(x,y)$ (for interior pixels $r, c \in [2,4]$):

* **Column 2 ($c=2$, centered over $x=2$):**
  Neighborhood spans columns $[1, 2, 3]$ with values $[50, 50, 50]$:

```math
G_x(r, 2) = (-1)(50) + 0(50) + 1(50) + (-2)(50) + 0(50) + 2(50) + (-1)(50) + 0(50) + 1(50) = 0
```

* **Column 3 ($c=3$, centered over $x=3$, the step edge boundary):**
  Neighborhood spans columns $[2, 3, 4]$ with values $[50, 50, 100]$:

```math
G_x(r, 3) = (-1)(50) + 0(50) + 1(100) + (-2)(50) + 0(50) + 2(100) + (-1)(50) + 0(50) + 1(100)
```

```math
G_x(r, 3) = (-50 + 100) + (-100 + 200) + (-50 + 100) = 50 + 100 + 50 = +200
```

* **Column 4 ($c=4$, centered over $x=4$):**
  Neighborhood spans columns $[3, 4, 5]$ with values $[50, 100, 100]$:

```math
G_x(r, 4) = (-1)(50) + 0(100) + 1(100) + (-2)(50) + 0(100) + 2(100) + (-1)(50) + 0(100) + 1(100)
```

```math
G_x(r, 4) = (-50 + 100) + (-100 + 200) + (-50 + 100) = +200
```

##### Resulting Interior $3 \times 3$ Matrix $G_x$:

```math
G_x = \begin{bmatrix} 0 & +200 & +200 \\ 0 & +200 & +200 \\ 0 & +200 & +200 \end{bmatrix}
```

##### 2. Vertical Response Matrix $G_y(x,y)$:
Because all row intensities are identical down each column, vertical differences are identically zero for all interior pixels:

```math
G_y = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
```

##### 3. Gradient Magnitude Matrix $G(x,y) = \sqrt{G_x^2 + G_y^2}$:

```math
G = \begin{bmatrix} 0 & 200 & 200 \\ 0 & 200 & 200 \\ 0 & 200 & 200 \end{bmatrix}
```

---

### Numerical 2.3: Diagonal Sobel Operator Convolution (+45° and -45° Masks)

#### ❓ Problem Statement
Given a $3 \times 3$ corner edge image patch $f(x,y)$:

```math
f(x,y) = \begin{bmatrix} 10 & 10 & 80 \\ 10 & 80 & 80 \\ 80 & 80 & 80 \end{bmatrix}
```

Apply the $+45^\circ$ and $-45^\circ$ diagonal Sobel spatial masks:

```math
S_{+45^\circ} = \begin{bmatrix} 0 & 1 & 2 \\ -1 & 0 & 1 \\ -2 & -1 & 0 \end{bmatrix}, \quad S_{-45^\circ} = \begin{bmatrix} -2 & -1 & 0 \\ -1 & 0 & 1 \\ 0 & 1 & 2 \end{bmatrix}
```

1. Compute the $+45^\circ$ diagonal gradient response $G_{+45^\circ} = f * S_{+45^\circ}$.
2. Compute the $-45^\circ$ diagonal gradient response $G_{-45^\circ} = f * S_{-45^\circ}$.
3. Compute the combined diagonal gradient magnitude $G_{\text{diag}} = \sqrt{G_{+45^\circ}^2 + G_{-45^\circ}^2}$.

---

#### 💡 Step-by-Step Solution

##### 1. $+45^\circ$ Response $G_{+45^\circ}$:

```math
G_{+45^\circ} = (0)(10) + (1)(10) + (2)(80) + (-1)(10) + (0)(80) + (1)(80) + (-2)(80) + (-1)(80) + (0)(80)
```

```math
G_{+45^\circ} = (0 + 10 + 160) + (-10 + 0 + 80) + (-160 - 80 + 0) = 170 + 70 - 240 = 0
```

> 🧠 **Insight:** The $+45^\circ$ mask response is $0$ because the intensity contour runs perfectly parallel to the $+45^\circ$ diagonal axis!

##### 2. $-45^\circ$ Response $G_{-45^\circ}$:

```math
G_{-45^\circ} = (-2)(10) + (-1)(10) + (0)(80) + (-1)(10) + (0)(80) + (1)(80) + (0)(80) + (1)(80) + (2)(80)
```

```math
G_{-45^\circ} = (-30) + 70 + 240 = +280
```

##### 3. Combined Diagonal Gradient Magnitude $G_{\text{diag}}$:

```math
G_{\text{diag}} = \sqrt{0^2 + (280)^2} = 280.0
```

---

### Numerical 2.4: Kirsch Compass Operator 8-Directional Maximum Response Calculation

> ⚠️ **Scope note:** The Kirsch compass operator (and the diagonal Sobel masks in Numerical 2.3) are **not** part of the strict Unit 5 syllabus list in this workbook's scope boundary (Section 0). Both are included here as **supporting practice material** on the general theme of directional edge masks, not as compulsory examinable operators.

#### ❓ Problem Statement
Given a $3 \times 3$ image patch $f(x,y)$:

```math
f(x,y) = \begin{bmatrix} 20 & 20 & 20 \\ 20 & 100 & 20 \\ 100 & 100 & 100 \end{bmatrix}
```

The Kirsch Compass Mask set evaluates edge strength across 8 directional compass orientations. All 8 masks are rotations of the same $\pm5/\pm3$ pattern:

```math
K_N = \begin{bmatrix} 5 & 5 & 5 \\ -3 & 0 & -3 \\ -3 & -3 & -3 \end{bmatrix}, \quad
K_{NE} = \begin{bmatrix} 5 & 5 & -3 \\ 5 & 0 & -3 \\ -3 & -3 & -3 \end{bmatrix}, \quad
K_E = \begin{bmatrix} 5 & -3 & -3 \\ 5 & 0 & -3 \\ 5 & -3 & -3 \end{bmatrix}, \quad
K_{SE} = \begin{bmatrix} -3 & -3 & -3 \\ 5 & 0 & -3 \\ 5 & 5 & -3 \end{bmatrix}
```

```math
K_S = \begin{bmatrix} -3 & -3 & -3 \\ -3 & 0 & -3 \\ 5 & 5 & 5 \end{bmatrix}, \quad
K_{SW} = \begin{bmatrix} -3 & -3 & -3 \\ -3 & 0 & 5 \\ -3 & 5 & 5 \end{bmatrix}, \quad
K_W = \begin{bmatrix} -3 & -3 & 5 \\ -3 & 0 & 5 \\ -3 & -3 & 5 \end{bmatrix}, \quad
K_{NW} = \begin{bmatrix} -3 & 5 & 5 \\ -3 & 0 & 5 \\ -3 & -3 & -3 \end{bmatrix}
```

1. Compute the response for all 8 compass masks ($K_N, K_{NE}, K_E, K_{SE}, K_S, K_{SW}, K_W, K_{NW}$).
2. Determine which compass mask produces the maximum edge response $R = \max_k (f * K_k)$.

---

#### 💡 Step-by-Step Solution

##### 1. North Mask Response ($R_N = f * K_N$):

```math
R_N = (5)(20) + (5)(20) + (5)(20) + (-3)(20) + (0)(100) + (-3)(20) + (-3)(100) + (-3)(100) + (-3)(100)
```

```math
R_N = 300 - 120 - 900 = -720
```

##### 2. North-East Mask Response ($R_{NE} = f * K_{NE}$):

```math
R_{NE} = (5)(20) + (5)(20) + (-3)(20) + (5)(20) + (0)(100) + (-3)(20) + (-3)(100) + (-3)(100) + (-3)(100)
```

```math
R_{NE} = (100+100-60) + (100+0-60) + (-300-300-300) = 140 + 40 - 900 = -720
```

##### 3. East Mask Response ($R_E = f * K_E$):

```math
R_E = (5)(20) + (-3)(20) + (-3)(20) + (5)(20) + (0)(100) + (-3)(20) + (5)(100) + (-3)(100) + (-3)(100)
```

```math
R_E = (100-60-60) + (100+0-60) + (500-300-300) = -20 + 40 - 100 = -80
```

##### 4. South-East Mask Response ($R_{SE} = f * K_{SE}$):

```math
R_{SE} = (-3)(20) + (-3)(20) + (-3)(20) + (5)(20) + (0)(100) + (-3)(20) + (5)(100) + (5)(100) + (-3)(100)
```

```math
R_{SE} = (-60-60-60) + (100+0-60) + (500+500-300) = -180 + 40 + 700 = +560
```

##### 5. South Mask Response ($R_S = f * K_S$):

```math
R_S = (-3)(20) + (-3)(20) + (-3)(20) + (-3)(20) + (0)(100) + (-3)(20) + (5)(100) + (5)(100) + (5)(100)
```

```math
R_S = -180 - 120 + 1500 = +1200
```

##### 6. South-West Mask Response ($R_{SW} = f * K_{SW}$):

```math
R_{SW} = (-3)(20) + (-3)(20) + (-3)(20) + (-3)(20) + (0)(100) + (5)(20) + (-3)(100) + (5)(100) + (5)(100)
```

```math
R_{SW} = (-60-60-60) + (-60+0+100) + (-300+500+500) = -180 + 40 + 700 = +560
```

##### 7. West Mask Response ($R_W = f * K_W$):

```math
R_W = (-3)(20) + (-3)(20) + (5)(20) + (-3)(20) + (0)(100) + (5)(20) + (-3)(100) + (-3)(100) + (5)(100)
```

```math
R_W = (-60-60+100) + (-60+0+100) + (-300-300+500) = -20 + 40 - 100 = -80
```

##### 8. North-West Mask Response ($R_{NW} = f * K_{NW}$):

```math
R_{NW} = (-3)(20) + (5)(20) + (5)(20) + (-3)(20) + (0)(100) + (5)(20) + (-3)(100) + (-3)(100) + (-3)(100)
```

```math
R_{NW} = (-60+100+100) + (-60+0+100) + (-300-300-300) = 140 + 40 - 900 = -720
```

##### 9. Full Response Summary & Conclusion:

| Direction | N | NE | E | SE | S | SW | W | NW |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Response | $-720$ | $-720$ | $-80$ | $+560$ | $\mathbf{+1200}$ | $+560$ | $-80$ | $-720$ |

The **South ($K_S$)** mask yields the maximum response, $+1200$. This confirms that a powerful horizontal edge with a dark-to-light transition facing South exists across the bottom row of the patch — consistent with the checked full 8-direction comparison, not just the North/South pair.

---

## Section 3: Second-Order Operator Numericals (Laplacian & LoG Zero-Crossings)

### Numerical 3.1: 4-Neighbor vs. 8-Neighbor Laplacian Convolution on a Step Edge Image

#### ❓ Problem Statement
Given a $5 \times 5$ grayscale image containing a horizontal step edge:

```math
f(x,y) = \begin{bmatrix} 30 & 30 & 30 & 30 & 30 \\ 30 & 30 & 30 & 30 & 30 \\ 30 & 30 & 30 & 30 & 30 \\ 90 & 90 & 90 & 90 & 90 \\ 90 & 90 & 90 & 90 & 90 \end{bmatrix}
```

Apply the standard 4-neighbor ($L_4$) and 8-neighbor ($L_8$) discrete Laplacian masks with negative center weights:

```math
L_4 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \quad L_8 = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix}
```

Compute the interior $3 \times 5$ response matrices for $\nabla_4^2 f(x,y)$ and $\nabla_8^2 f(x,y)$.

> ℹ️ **Note on output size:** A $3 \times 3$ mask applied without padding to a $5 \times 5$ image loses exactly one border row/column on each side it needs a neighbor from. Here, all 5 columns have a valid left/right neighbor (the step edge is vertical, running the full height of the image), so no columns are lost — only the top and bottom rows are lost (rows 1 and 5, which lack a row above/below). The valid interior is therefore rows $2$–$4$ (3 rows) $\times$ columns $1$–$5$ (5 columns) $= 3 \times 5$, not $3 \times 3$.

---

#### 💡 Step-by-Step Solution

##### 1. 4-Neighbor Laplacian $\nabla_4^2 f(x,y)$ Calculation:

* **Row 2 ($r=2$, Dark Side of Edge, intensity 30):**
  Top neighbor ($r=1$) = 30, Bottom neighbor ($r=3$) = 30, Left = 30, Right = 30, Center = 30.

```math
\nabla_4^2 f(2, c) = (1)(30) + (1)(30) + (1)(30) + (1)(30) - 4(30) = 120 - 120 = 0
```

* **Row 3 ($r=3$, Upper Edge Boundary, intensity 30):**
  Top neighbor ($r=2$) = 30, Bottom neighbor ($r=4$) = 90, Left = 30, Right = 30, Center = 30.

```math
\nabla_4^2 f(3, c) = (1)(30) + (1)(90) + (1)(30) + (1)(30) - 4(30) = 180 - 120 = +60
```

* **Row 4 ($r=4$, Lower Edge Boundary, intensity 90):**
  Top neighbor ($r=3$) = 30, Bottom neighbor ($r=5$) = 90, Left = 90, Right = 90, Center = 90.

```math
\nabla_4^2 f(4, c) = (1)(30) + (1)(90) + (1)(90) + (1)(90) - 4(90) = 300 - 360 = -60
```

##### Resulting Interior $3 \times 5$ Matrix $\nabla_4^2 f(x,y)$:

```math
\nabla_4^2 f = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ +60 & +60 & +60 & +60 & +60 \\ -60 & -60 & -60 & -60 & -60 \end{bmatrix}
```

##### 2. 8-Neighbor Laplacian $\nabla_8^2 f(x,y)$ Calculation:

* **Row 2 ($r=2$):** All 8 neighbors = 30. Response = $8(30) - 8(30) = 0$.
* **Row 3 ($r=3$):** Top 3 neighbors ($r=2$) = 30, Left & Right ($r=3$) = 30, Bottom 3 neighbors ($r=4$) = 90. Center = 30.

```math
\nabla_8^2 f(3, c) = 3(30) + 2(30) + 3(90) - 8(30) = 90 + 60 + 270 - 240 = +180
```

* **Row 4 ($r=4$):** Top 3 neighbors ($r=3$) = 30, Left & Right ($r=4$) = 90, Bottom 3 neighbors ($r=5$) = 90. Center = 90.

```math
\nabla_8^2 f(4, c) = 3(30) + 2(90) + 3(90) - 8(90) = 90 + 180 + 270 - 720 = -180
```

##### Resulting Interior $3 \times 5$ Matrix $\nabla_8^2 f(x,y)$:

```math
\nabla_8^2 f = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ +180 & +180 & +180 & +180 & +180 \\ -180 & -180 & -180 & -180 & -180 \end{bmatrix}
```

##### 🧠 Observations:
The 8-neighbor Laplacian produces **3 times the edge response** ($+180$ vs. $+60$) compared to $L_4$ because it incorporates diagonal neighbor derivatives.

---

### Numerical 3.2: Laplacian Center-Weight Sign Conventions and Edge Sharpening Analysis

#### ❓ Problem Statement
Given the $3 \times 5$ Laplacian response matrix $\nabla_8^2 f(x,y)$ calculated in Numerical 3.1 and the original image values at Row 3 ($f=30$) and Row 4 ($f=90$):

1. Demonstrate edge sharpening using the **negative center weight** rule ($w_c = -8 \implies g = f - \nabla^2 f$).
2. Demonstrate edge sharpening using the **positive center weight** rule ($w_c = +8 \implies g = f + \nabla^2 f$).
3. Verify that both sign conventions yield identical sharpened intensity outputs.

---

#### 💡 Step-by-Step Solution

##### 1. Negative Center Weight Rule ($w_c = -8 \implies g = f - \nabla^2 f$):
* **Row 3 ($f = 30, \nabla^2 f = +180$):**

```math
g(3, c) = 30 - (+180) = -150 \xrightarrow{\text{Clip to }[0,255]} 0
```

* **Row 4 ($f = 90, \nabla^2 f = -180$):**

```math
g(4, c) = 90 - (-180) = 90 + 180 = 270 \xrightarrow{\text{Clip to }[0,255]} 255
```

##### 2. Positive Center Weight Rule ($w_c = +8 \implies g = f + \nabla^2 f$):
When using a positive center weight mask $L_8^+$, all output signs invert:

```math
L_8^+ = \begin{bmatrix} -1 & -1 & -1 \\ -1 & 8 & -1 \\ -1 & -1 & -1 \end{bmatrix}
```

* $\nabla_{8+}^2 f(3, c) = -180$
* $\nabla_{8+}^2 f(4, c) = +180$

Applying addition $g = f + \nabla_{8+}^2 f$:
* **Row 3 ($f = 30, \nabla_{8+}^2 f = -180$):** $g(3,c) = 30 + (-180) = -150 \to 0$.
* **Row 4 ($f = 90, \nabla_{8+}^2 f = +180$):** $g(4,c) = 90 + (+180) = 270 \to 255$.

##### 3. Conclusion:
Both conventions produce identical sharpened output values ($0$ on the dark side, $255$ on the light side). The edge contrast transitions from $30 \to 90$ (difference of 60) in the original image to $0 \to 255$ (difference of 255) in the sharpened image!

---

### Numerical 3.3: 5 x 5 Discrete Laplacian of Gaussian (LoG) Convolution and Zero-Crossing Extraction

#### ❓ Problem Statement
Given a $5 \times 5$ image patch $f(x,y)$:

```math
f(x,y) = \begin{bmatrix} 10 & 10 & 10 & 10 & 10 \\ 10 & 10 & 10 & 10 & 10 \\ 10 & 10 & 50 & 50 & 50 \\ 50 & 50 & 50 & 50 & 50 \\ 50 & 50 & 50 & 50 & 50 \end{bmatrix}
```

Apply the standard $5 \times 5$ Discrete LoG (Mexican Hat) mask $M_{\text{LoG}}$:

```math
M_{\text{LoG}} = \begin{bmatrix} 0 & 0 & -1 & 0 & 0 \\ 0 & -1 & -2 & -1 & 0 \\ -1 & -2 & 16 & -2 & -1 \\ 0 & -1 & -2 & -1 & 0 \\ 0 & 0 & -1 & 0 & 0 \end{bmatrix}
```

1. Verify that the sum of mask weights equals zero.
2. Compute the LoG filter response at center pixel $(3,3)$ (value 50).
3. Compute the full LoG response at the neighboring pixels $(2,3)$ and $(3,2)$ (using replicate/edge padding for the one out-of-bounds mask row or column each needs), and use those — not intermediate row-sums from the $(3,3)$ convolution — to determine whether a genuine zero-crossing exists near $(3,3)$.

---

#### 💡 Step-by-Step Solution

##### 1. Mask Weight Sum Verification:
* Center weight: $+16$
* Surrounding weight sum: $4(-2) + 8(-1) = -8 - 8 = -16$
* Total Sum: $16 + (-16) = 0$. (Verified! Passed constant background zero-response condition).

##### 2. LoG Convolution at Center Pixel $(3,3)$:
Multiply $f(x,y)$ elementwise with $M_{\text{LoG}}$:

```math
\text{Row 1: } (0)(10) + (0)(10) + (-1)(10) + (0)(10) + (0)(10) = -10
```

```math
\text{Row 2: } (0)(10) + (-1)(10) + (-2)(10) + (-1)(10) + (0)(10) = -40
```

```math
\text{Row 3: } (-1)(10) + (-2)(10) + (16)(50) + (-2)(50) + (-1)(50) = -10 - 20 + 800 - 100 - 50 = +620
```

```math
\text{Row 4: } (0)(50) + (-1)(50) + (-2)(50) + (-1)(50) + (0)(50) = -200
```

```math
\text{Row 5: } (0)(50) + (0)(50) + (-1)(50) + (0)(50) + (0)(50) = -50
```

Summing all row products:

```math
R_{\text{LoG}}(3,3) = -10 - 40 + 620 - 200 - 50 = +320
```

##### 3. Zero-Crossing Analysis (Full Responses at Neighboring Pixels):

> ⚠️ **Correction:** The individual row-products used to build $R_{\text{LoG}}(3,3) = +320$ above (e.g., the Row 2 partial sum of $-40$) are **intermediate terms of that same single convolution at $(3,3)$** — they are not the LoG filter's output at a different pixel location. A zero-crossing claim requires computing the **complete, independent LoG response** at an adjacent pixel by re-centering the $5 \times 5$ mask there. That calculation is done below.

To evaluate pixel $(2,3)$ and $(3,2)$, the mask (centered at each of those locations) needs one row or column beyond the given $5 \times 5$ patch. We use **replicate (edge-extension) padding** — the standard convention for this workbook — where the out-of-bounds row/column repeats the nearest valid row/column of $f$.

* **Response at $(2,3)$** (mask centered one row above $(3,3)$; needs row $0$, replicated from row $1$):
```math
R_{\text{LoG}}(2,3) = -160
```
* **Response at $(3,2)$** (mask centered one column left of $(3,3)$; needs column $0$, replicated from column $1$):
```math
R_{\text{LoG}}(3,2) = -320
```

Both neighbors are **negative**, while the center is **positive** ($+320$), and the magnitude of the sign change at each boundary clearly exceeds any reasonable noise threshold $T_{zc}$. This is a genuine, independently-computed sign change between $(3,3)$ and its top and left neighbors:

```math
R_{\text{LoG}}(2,3) = -160 \;<\; 0 \;<\; +320 = R_{\text{LoG}}(3,3), \qquad R_{\text{LoG}}(3,2) = -320 \;<\; 0 \;<\; +320 = R_{\text{LoG}}(3,3)
```

**Conclusion:** Pixel $(3,3)$ **does** represent a zero-crossing edge location, confirmed by comparing complete LoG responses at $(3,3)$ against its own top and left neighbors — not by the sign of intermediate row-sums within a single convolution. (Note: the response at $(4,3)$, the neighbor below, is $+80$ under replicate padding — the **same sign** as the center — so the sign change is confirmed along the top/left directions checked here, not uniformly in every direction from $(3,3)$.)

---

## Section 4: Canny Edge Detector Multi-Stage Pipeline Numericals

### Numerical 4.1: Canny Step 2 — Gradient Magnitude and Sector Quantization (Given Pre-Computed Sobel Values)

> ℹ️ **Renamed for accuracy:** This problem starts from already-given $G_x, G_y$ values and only covers magnitude calculation and angle sector quantization — it does **not** compute a Gaussian smoothing stage (no image patch or Gaussian kernel is given here). See Numerical 4.4 for a walkthrough that includes the smoothing stage.

#### ❓ Problem Statement
At spatial position $(x,y)$, the horizontal and vertical Sobel gradient components are calculated as $G_x = +30$ and $G_y = +70$ (already computed from a prior, unshown Sobel step).

1. Compute the gradient magnitude $M = \sqrt{G_x^2 + G_y^2}$.
2. Compute the raw gradient angle $\theta = \text{atan2}(G_y, G_x)$ in degrees.
3. Quantize $\theta$ into one of the four standard Canny direction sectors ($0^\circ, 45^\circ, 90^\circ, 135^\circ$).

---

#### 💡 Step-by-Step Solution

##### 1. Gradient Magnitude $M$:

```math
M = \sqrt{(30)^2 + (70)^2} = \sqrt{900 + 4900} = \sqrt{5800} \approx 76.16
```

##### 2. Raw Angle $\theta$:

```math
\theta = \text{atan2}(70, 30) = \tan^{-1}(2.333) \approx 66.8^\circ
```

##### 3. Sector Quantization Rules:
Canny quantizes raw angles into 4 sectors based on $22.5^\circ$ angular boundaries:
* **Sector 0 ($0^\circ$):** $[-22.5^\circ, 22.5^\circ] \cup [157.5^\circ, 180^\circ] \cup [-180^\circ, -157.5^\circ]$
* **Sector 1 ($45^\circ$):** $[22.5^\circ, 67.5^\circ] \cup [-157.5^\circ, -112.5^\circ]$
* **Sector 2 ($90^\circ$):** $[67.5^\circ, 112.5^\circ] \cup [-112.5^\circ, -67.5^\circ]$
* **Sector 3 ($135^\circ$):** $[112.5^\circ, 157.5^\circ] \cup [-67.5^\circ, -22.5^\circ]$

##### Decision:
Since $\theta = 66.8^\circ$ falls within $[22.5^\circ, 67.5^\circ]$, it quantizes directly to **Sector 1 ($45^\circ$)**.

---

### Numerical 4.2: Canny Step 3 — Non-Maximum Suppression (NMS) on a 5 x 5 Gradient Matrix

#### ❓ Problem Statement
Given a $5 \times 5$ gradient magnitude matrix $M(x,y)$:

```math
M(x,y) = \begin{bmatrix} 10 & 20 & 30 & 20 & 10 \\ 20 & 80 & 90 & 70 & 20 \\ 30 & 85 & 120 & 95 & 30 \\ 20 & 75 & 100 & 80 & 20 \\ 10 & 20 & 30 & 20 & 10 \end{bmatrix}
```

Assume the quantized gradient sector angle across all interior pixels is $\theta = 0^\circ$ (horizontal gradient direction).

1. Perform Non-Maximum Suppression (NMS) on the interior $3 \times 3$ sub-matrix.
2. Produce the thinned magnitude output matrix $M_{\text{NMS}}(x,y)$.

---

#### 💡 Step-by-Step Solution

##### 1. NMS Rule for Sector $0^\circ$:
For a horizontal gradient ($\theta = 0^\circ$), compare target pixel $M(r,c)$ with its **left neighbor $M(r, c-1)$** and **right neighbor $M(r, c+1)$**:
* If $M(r,c) \ge M(r, c-1)$ **AND** $M(r,c) \ge M(r, c+1)$, retain $M_{\text{NMS}}(r,c) = M(r,c)$.
* Otherwise, suppress $M_{\text{NMS}}(r,c) = 0$.

##### 2. Cell-by-Cell Interior Calculations:

* **Row 2 ($r=2$):**
  * $c=2$ (val 80): Neighbors 20, 90. Since $80 < 90$, **suppress to 0**.
  * $c=3$ (val 90): Neighbors 80, 70. Since $90 \ge 80$ and $90 \ge 70$, **retain 90**.
  * $c=4$ (val 70): Neighbors 90, 20. Since $70 < 90$, **suppress to 0**.

* **Row 3 ($r=3$):**
  * $c=2$ (val 85): Neighbors 30, 120. Since $85 < 120$, **suppress to 0**.
  * $c=3$ (val 120): Neighbors 85, 95. Since $120 \ge 85$ and $120 \ge 95$, **retain 120**.
  * $c=4$ (val 95): Neighbors 120, 30. Since $95 < 120$, **suppress to 0**.

* **Row 4 ($r=4$):**
  * $c=2$ (val 75): Neighbors 20, 100. Since $75 < 100$, **suppress to 0**.
  * $c=3$ (val 100): Neighbors 75, 80. Since $100 \ge 75$ and $100 \ge 80$, **retain 100**.
  * $c=4$ (val 80): Neighbors 100, 20. Since $80 < 100$, **suppress to 0**.

##### 3. Resulting Thinned NMS Matrix $M_{\text{NMS}}$ (Interior $3 \times 3$):

```math
M_{\text{NMS}} = \begin{bmatrix} 0 & 90 & 0 \\ 0 & 120 & 0 \\ 0 & 100 & 0 \end{bmatrix}
```

> 🧠 **Result:** All thick gradient ridge shoulders are successfully suppressed to 0, producing a single-pixel-thin edge line down Column 3!

---

### Numerical 4.3: Canny Step 4 & 5 — Double Thresholding and 8-Connected Hysteresis Edge Tracking

#### ❓ Problem Statement
Given a $5 \times 5$ thinned Non-Maximum Suppressed (NMS) magnitude matrix $M_{\text{NMS}}(x,y)$:

```math
M_{\text{NMS}} = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 25 & 60 & 15 & 0 \\ 0 & 85 & 110 & 40 & 0 \\ 0 & 30 & 70 & 20 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

Given double threshold values: High Threshold $T_{\text{high}} = 80$, Low Threshold $T_{\text{low}} = 30$.

1. Perform **Double Thresholding** to classify pixels into Strong, Weak, and Non-edge sets.
2. Perform **8-Connected Hysteresis Edge Tracking** to produce the final binary Canny edge map $E(x,y)$.

---

#### 💡 Step-by-Step Solution

##### 1. Double Thresholding Classification:
* **Strong Edge Pixel ($1$):** $M_{\text{NMS}} \ge 80$
* **Weak Edge Pixel ($W$):** $30 \le M_{\text{NMS}} < 80$
* **Non-Edge Pixel ($0$):** $M_{\text{NMS}} < 30$

##### Classified Matrix:

```math
\text{Classified} = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & W & 0 & 0 \\ 0 & 1 & 1 & W & 0 \\ 0 & W & W & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

Specifically:
* **Strong Pixels ($1$):** $(3,2)$ [val 85] and $(3,3)$ [val 110].
* **Weak Pixels ($W$):** $(2,3)$ [val 60], $(3,4)$ [val 40], $(4,2)$ [val 30], $(4,3)$ [val 70].
* **Rejected Pixels ($0$):** Values $25, 15, 20$.

##### 2. 8-Connected Hysteresis Connectivity Tracking:
Evaluate each Weak Pixel ($W$):
* **Weak Pixel $(2,3)$ [val 60]:** Directly adjacent (bottom-left) to Strong pixel $(3,2)$ and (bottom) to Strong pixel $(3,3)$. **Promoted to Strong ($1$)!**
* **Weak Pixel $(3,4)$ [val 40]:** Directly adjacent (left) to Strong pixel $(3,3)$. **Promoted to Strong ($1$)!**
* **Weak Pixel $(4,2)$ [val 30]:** Directly adjacent (top) to Strong pixel $(3,2)$. **Promoted to Strong ($1$)!**
* **Weak Pixel $(4,3)$ [val 70]:** Directly adjacent (top) to Strong pixel $(3,3)$. **Promoted to Strong ($1$)!**

##### 3. Final Binary Canny Edge Map $E(x,y)$:

```math
E(x,y) = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

---

### Numerical 4.4: Complete End-to-End Canny Pipeline Walkthrough on a 5 x 5 Image Matrix

#### ❓ Problem Statement
Given a $5 \times 5$ raw grayscale image $I(x,y)$ (1-indexed, rows and columns $1$–$5$):

```math
I(x,y) = \begin{bmatrix} 10 & 10 & 10 & 80 & 80 \\ 10 & 10 & 10 & 80 & 80 \\ 10 & 10 & 10 & 80 & 80 \\ 10 & 10 & 10 & 80 & 80 \\ 10 & 10 & 10 & 80 & 80 \end{bmatrix}
```

Given $T_{\text{high}} = 150, T_{\text{low}} = 50$. Walk through the complete Canny pipeline — **including an explicit Gaussian smoothing pass** — to determine the final edge map $E(x,y)$ for interior pixels. **Padding convention:** replicate (edge-extension) padding is used at every stage that needs pixels outside the $5 \times 5$ image (both the Gaussian and Sobel passes).

---

#### 💡 Step-by-Step Solution

##### Step 1: Gaussian Smoothing
Apply the standard $3 \times 3$ discrete Gaussian kernel ($\sigma \approx 1.0$):

```math
G = \frac{1}{16}\begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}
```

Because every row of $I$ is identical, smoothing has no effect **vertically** — but it **does** blur the sharp step **horizontally**, since the kernel averages columns $2$–$4$ and $3$–$5$ across the boundary. Convolving (cross-correlation with replicate padding) at each column of any row (all rows are identical) gives the smoothed image $I_s(x,y)$:

```math
I_s(x,y) = \begin{bmatrix} 10 & 10 & 27.5 & 62.5 & 80 \\ 10 & 10 & 27.5 & 62.5 & 80 \\ 10 & 10 & 27.5 & 62.5 & 80 \\ 10 & 10 & 27.5 & 62.5 & 80 \\ 10 & 10 & 27.5 & 62.5 & 80 \end{bmatrix}
```

For example, at column $3$: $I_s(r,3) = \tfrac{1}{16}\big[1(10)+2(10)+1(10) + 2(10)+4(10)+2(10) + 1(80)+2(80)+1(80)\big] = \tfrac{1}{16}(40+80+320) = \tfrac{440}{16} = 27.5$. **This smoothed matrix — not the raw step image — is what the Sobel stage below is applied to.**

##### Step 2: Sobel Gradient Magnitude & Angle (Applied to the Smoothed Image $I_s$)
Applying $S_x$ and $S_y$ to $I_s$ (replicate padding at the left/right edges) yields, for every row (all identical):
* $G_y(r,c) = 0$ for all columns (still no vertical variation).
* $G_x(r,2) = +70$, $G_x(r,3) = +210$, $G_x(r,4) = +210$, $G_x(r,5) = +70$ (edge columns via replicate padding).
* Magnitude $M = |G_x|$ since $G_y=0$: $M(r,2)=70$, $M(r,3)=210$, $M(r,4)=210$, $M(r,5)=70$. Angle $\theta = 0^\circ$ (Sector 0) everywhere non-zero.

> ⚠️ **Correction from the unsmoothed version:** Skipping Step 1 and applying Sobel directly to the raw step image gives $G_x(r,3)=G_x(r,4)=+280$ instead. Those values belong to a **simplified, unsmoothed illustration** of the pipeline, not this smoothed walkthrough — the two should not be mixed.

##### Step 3: Non-Maximum Suppression (NMS along Sector 0)
Comparing each pixel with its horizontal (left, right) neighbors, using $M(r,1)=0$ (replicate-padded boundary, since column $1$ is flat) as needed:
* $M(r,2)=70$: neighbors $M(r,1)=0$ and $M(r,3)=210$. Since $70 < 210$, **suppressed to $0$**.
* $M(r,3)=210$: neighbors $M(r,2)=70$ and $M(r,4)=210$. Since $210 \ge 70$ **and** $210 \ge 210$ (tie), **retained as $210$** — see tie rule below.
* $M(r,4)=210$: neighbors $M(r,3)=210$ and $M(r,5)=70$. Since $210 \ge 210$ (tie) **and** $210 \ge 70$, **retained as $210$**.

> ℹ️ **NMS tie rule:** When the center pixel is **exactly equal** to one of its two directional neighbors (as at columns $3$ and $4$ here), this workbook's convention is to use $\ge$ (non-strict inequality) on both sides, so **both** tied pixels are retained rather than one arbitrarily suppressed. This can leave a 2-pixel-wide ridge at an exact plateau, which double thresholding and/or hysteresis will typically resolve; state this rule explicitly whenever a tie occurs, since some references instead break ties by keeping only the first-encountered pixel in scan order.

##### Step 4: Double Thresholding ($T_{\text{high}} = 150, T_{\text{low}} = 50$)
* $M_{\text{NMS}}(r,3) = 210 \ge 150 \implies$ **Strong Edge ($1$)**.
* $M_{\text{NMS}}(r,4) = 210 \ge 150 \implies$ **Strong Edge ($1$)**.
* $M_{\text{NMS}}(r,2) = 0 < 50 \implies$ **Rejected ($0$)**.

##### Step 5: Hysteresis Tracking
All candidate edge pixels are already classified Strong ($1$); there are no Weak pixels to resolve by connectivity in this example.

##### Final Binary Edge Map $E(x,y)$ (Interior $3 \times 3$, columns $2$–$4$):

```math
E = \begin{bmatrix} 0 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{bmatrix}
```

**Note:** The final binary edge map is **unchanged** from the unsmoothed shortcut ($[0,1,1]$ per row either way) — but that is a coincidence of this particular clean step image (both the smoothed and unsmoothed gradients peak at the same two columns and clear both thresholds). The **intermediate values differ substantially** ($M=210$ here vs. $M=280$ unsmoothed), and for a noisier or less extreme input, skipping the smoothing stage could change which pixels survive thresholding. Always show the smoothing stage explicitly rather than assuming the final map will match.

---

## Section 5: Formula Master Reference Sheet

```math
\text{1D Central Difference:} \quad \frac{\partial f}{\partial x} = \frac{f(x+1) - f(x-1)}{2}
```

```math
\text{1D Second Difference:} \quad \frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)
```

```math
\text{Gradient Vector:} \quad \nabla f = \begin{bmatrix} G_x \\ G_y \end{bmatrix} = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}
```

```math
\text{Euclidean Magnitude:} \quad G = \sqrt{G_x^2 + G_y^2}, \quad \text{Manhattan Approx:} \quad G \approx |G_x| + |G_y|
```

```math
\text{Gradient Direction Angle:} \quad \theta = \text{atan2}(G_y, G_x)
```

```math
\text{2D Discrete Laplacian (4-Neighbor):} \quad \nabla^2 f(x,y) = f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1) - 4f(x,y)
```

---

## Section 6: Summary Answer Index Table

| Problem # | Primary Topic | Source Status | Input Size | Key Numerical Output / Result |
|---|---|---|---|---|
| **Numerical 1.1** | 1D Scanline Derivatives | Reported PYQ | 12 Samples | Ramp $1^{\text{st}}$ diff = $+10$, $2^{\text{nd}}$ diff pair = $+10, -10$; Roof peak $2^{\text{nd}}$ diff = $+50$ |
| **Numerical 1.2** | 2D Gradient & Direction | Practice Problem | Point $(x,y)$ | $G_x=+40, G_y=-30 \implies G=50.0, G_{\text{approx}}=70.0, \theta=-36.87^\circ, \phi=+53.13^\circ$ |
| **Numerical 2.1** | $3 \times 3$ Prewitt Operator | Reported PYQ | $3 \times 3$ | $G_x = +120, G_y = 0, G = 120.0, \theta = 0^\circ$ |
| **Numerical 2.2** | $3 \times 3$ Sobel Operator | Reported PYQ (unverified) | $5 \times 5$ | Interior $G_x$ col 3 & 4 = $+200, G_y = 0, G = 200$ |
| **Numerical 2.3** | Diagonal Sobel Operator | Practice Problem | $3 \times 3$ | $G_{+45^\circ} = 0, G_{-45^\circ} = +280, G_{\text{diag}} = 280.0$ |
| **Numerical 2.4** | Kirsch Compass Operator | Practice Problem | $3 \times 3$ | $R_N = -720, R_S = +1200 \implies \text{Max Response Direction} = \text{South } (K_S)$ |
| **Numerical 3.1** | 4- vs 8-Neighbor Laplacian | Reported PYQ (unverified) | $5 \times 5$ | $\nabla_4^2 f = \pm 60, \nabla_8^2 f = \pm 180$ (8-neighbor is $3\times$ stronger) |
| **Numerical 3.2** | Laplacian Sign Conventions | Practice Problem | $3 \times 5$ | Both $g = f - \nabla^2 f$ and $g = f + \nabla_+^2 f$ yield $g_{\text{dark}}=0, g_{\text{light}}=255$ |
| **Numerical 3.3** | $5 \times 5$ LoG Zero-Crossing | Reported PYQ | $5 \times 5$ | Mask sum = 0; $R_{\text{LoG}}(3,3) = +320$ (Sign transition confirms zero-crossing) |
| **Numerical 4.1** | Canny Sector Quantization | Practice Problem | Point $(x,y)$ | $G_x=30, G_y=70 \implies M=76.16, \theta=66.8^\circ \implies \text{Quantized Sector } 1 \,(45^\circ)$ |
| **Numerical 4.2** | Canny NMS Thinning | Reported PYQ | $5 \times 5$ | Ridge shoulder pixels suppressed to 0; single-pixel column retained at 90, 120, 100 |
| **Numerical 4.3** | Canny Double Thresh & Hysteresis | Reported PYQ (unverified) | $5 \times 5$ | Strong at $(3,2),(3,3)$; Weak pixels $(2,3),(3,4),(4,2),(4,3)$ promoted via 8-connectivity |
| **Numerical 4.4** | Full Canny Pipeline (with explicit Gaussian smoothing) | Practice Problem | $5 \times 5$ | Smoothed Sobel $M=210$ at cols 3–4 (vs. $M=280$ unsmoothed); final binary edge line at cols 3 and 4 |

---

## Section 7: Common Numerical Mistakes & Pitfalls

1. ❌ **Confusing Gradient Angle $\theta$ with Edge Line Direction $\phi$:** The gradient vector $\theta = \text{atan2}(G_y, G_x)$ points **perpendicular** to the edge boundary. The edge line orientation is $\phi = \theta \pm 90^\circ$.
2. ❌ **Reversing Center-Weight Sign Rules in Laplacian Sharpening:**
   * If mask center weight is **negative** ($-4$ or $-8$), **subtract** Laplacian: $g = f - \nabla^2 f$.
   * If mask center weight is **positive** ($+4$ or $+8$), **add** Laplacian: $g = f + \nabla^2 f$.
3. ❌ **Forgetting Absolute Value in $L_1$ Gradient Approximation:** Writing $G \approx G_x + G_y$ instead of $|G_x| + |G_y|$ leads to erroneous cancellation when components have opposite signs.
4. ❌ **Misidentifying Sector Neighbors during Canny NMS:**
   * $0^\circ$ Sector: Compare horizontal left $(0,-1)$ and right $(0,1)$.
   * $45^\circ$ Sector: Compare bottom-left $(1,-1)$ and top-right $(-1,1)$.
   * $90^\circ$ Sector: Compare top $(-1,0)$ and bottom $(1,0)$.
   * $135^\circ$ Sector: Compare top-left $(-1,-1)$ and bottom-right $(1,1)$.

---

## Section 8: Source Status & Verification Checklist

* [x] **Numerical 1.1:** Reported PYQ (unverified) — 1D Scanline Derivatives
* [x] **Numerical 1.2:** Practice Problem — 2D Gradient Vector & Direction
* [x] **Numerical 2.1:** Reported PYQ (unverified) — $3 \times 3$ Prewitt Operator
* [x] **Numerical 2.2:** Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2025-26 [Q2b]
* [x] **Numerical 2.3:** Practice Problem — Diagonal Sobel Operator
* [x] **Numerical 2.4:** Practice Problem — Kirsch Compass Operator
* [x] **Numerical 3.1:** Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2022-23 [Q4a]
* [x] **Numerical 3.2:** Practice Problem — Laplacian Center-Weight Sign Rules
* [x] **Numerical 3.3:** Reported PYQ (unverified) — $5 \times 5$ LoG Zero-Crossing
* [x] **Numerical 4.1:** Practice Problem — Canny Sector Quantization
* [x] **Numerical 4.2:** Reported PYQ (unverified) — Canny Non-Maximum Suppression
* [x] **Numerical 4.3:** Reported PYQ (unverified) — SVKM's NMIMS Re-Exam 2023-24 [Q5b]
* [x] **Numerical 4.4:** Practice Problem — Complete Canny Pipeline Walkthrough (now includes an explicit Gaussian kernel, smoothed intermediate matrix, and NMS tie rule)
