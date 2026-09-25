# 🧮 IVP Unit 2: Image Enhancement — M2 Solved Numericals Master Workbook

---

## 📌 Document Overview & Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 2 — Image Enhancement (M2 Examination Scope)
* **Target Audience:** M2 Mid-Term & End-Semester Examinations
* **Format:** Strict GitHub Flavored Markdown (GFM) with Standalone Fenced Math Blocks (` ```math `)
* **Scope Boundary Notice:** This document is **strictly numerical-only** and covers exclusively the **M2 Examination Scope** for Unit 2:
  1. **Frequency-Domain Filtering Numericals:** Step-by-step 2D DFT pipeline, centering $(-1)^{x+y}$, 2D DFT/IDFT transformations, distance functions $D(u,v)$, transfer functions $H(u,v)$ (Ideal, Butterworth, Gaussian), spectral multiplication $G(u,v)$, DC component tracking, and average intensity evaluation.
  2. **Spatial-Sharpening Numericals:** 1D scanline finite differences (1st & 2nd derivatives), 2D spatial Laplacian convolution (4-neighbor & 8-neighbor masks), sign conventions, composite edge sharpening ($g = f \mp \nabla^2 f$), unsharp masking, and high-boost spatial filter mask construction with amplification factor $A$.
  3. **Frequency-Domain High-Boost Evaluations:** Derivation and numerical evaluation of high-boost frequency transfer functions $H_{\text{HB}}(u,v)$ across different low-pass response functions.

> ❌ **Excluded Out-of-Scope Topics:** Standalone point processing (digital negative, contrast stretching, global thresholding, intensity slicing, log/gamma transforms), histogram equalization, standalone spatial smoothing (box filter, median filter), and general edge-detection operators (Sobel, Prewitt, Canny). A spatial averaging blur calculation appears *only* as a necessary intermediate step within unsharp masking or high-boost filtering.

---

> **Source status:** Exam attributions are unverified until checked against original question papers.

## 📑 Table of Contents

1. [Notation, Conventions, and High-Boost Taxonomy](#1-notation-conventions-and-high-boost-taxonomy)
2. [Section 1: Frequency-Domain Filtering Numericals](#2-section-1-frequency-domain-filtering-numericals)
   * 2.1 [Numerical 1.1: Complete $4 \times 4$ Step-by-Step DFT High-Pass Filtering ($D_0 = 0.5$, IHPF)](#numerical-11) — *[Reported PYQ (unverified)]*
   * 2.2 [Numerical 1.2: Complete $4 \times 4$ Step-by-Step DFT Low-Pass Filtering ($D_0 = 1.5$, GLPF)](#numerical-12) — *[Practice Numerical]*
   * 2.3 [Numerical 1.3: Comparative Grid Evaluation of Ideal, Butterworth, and Gaussian Filters](#numerical-13) — *[Practice Numerical]*
3. [Section 2: Spatial-Sharpening Numericals](#3-section-2-spatial-sharpening-numericals)
   * 3.1 [Numerical 2.1: 1D Scanline First and Second Finite Differences Across Step and Ramp Edges](#numerical-21) — *[Reported PYQ (unverified; NMIMS TEE attribution not checked)]*
   * 3.2 [Numerical 2.2: 2D Spatial Laplacian Convolution on a $6 \times 6$ Step Edge Image ($8$-Neighbor)](#numerical-22) — *[Reported PYQ (unverified; NMIMS 2023–24 attribution not checked)]*
   * 3.3 [Numerical 2.3: 2D Spatial Laplacian Edge Enhancement on a $5 \times 5$ Grid ($4$- & $8$-Neighbor)](#numerical-23) — *[Reported PYQ (unverified)]*
   * 3.4 [Numerical 2.4: High-Boost Spatial Filter Mask Construction and Convolution ($A = 1.0, 1.5, 2.0$)](#numerical-24) — *[Reported PYQ (unverified; NMIMS Dec 2025 attribution not checked)]*
4. [Section 3: Frequency-Domain High-Boost & Unsharp Masking Evaluations](#4-section-3-frequency-domain-high-boost--unsharp-masking-evaluations)
   * 4.1 [Numerical 3.1: Derivation & Numerical Evaluation of High-Boost Frequency Transfer Functions](#numerical-31) — *[Reported PYQ (unverified)]*
5. [Section 4: Master Formula & Mask Quick Reference](#5-section-4-master-formula--mask-quick-reference)
6. [Section 5: Common Numerical Pitfalls & Exam Checklist](#6-section-5-common-numerical-pitfalls--exam-checklist)

---

## 1. Notation, Conventions, and High-Boost Taxonomy

### 1.1 Coordinate & Frequency Conventions

1. **Spatial Image Grid $f(x,y)$:**
   * $x \in \{0, 1, \dots, M-1\}$ denotes the row index (top to bottom).
   * $y \in \{0, 1, \dots, N-1\}$ denotes the column index (left to right).
2. **Frequency Domain Grid $F(u,v)$:**
   * $u \in \{0, 1, \dots, M-1\}$ denotes the row-direction frequency index.
   * $v \in \{0, 1, \dots, N-1\}$ denotes the column-direction frequency index.
3. **Centering Property:**
   * Multiplying $f(x,y)$ by $(-1)^{x+y}$ shifts the frequency spectrum origin $(0,0)$ to the grid center $(u_0, v_0) = (M/2, N/2)$.
4. **Distance Function $D(u,v)$:**
   * Euclidean distance from coordinate $(u,v)$ to centered frequency origin $(M/2, N/2)$:

```math
D(u,v) = \sqrt{\left(u - \frac{M}{2}\right)^2 + \left(v - \frac{N}{2}\right)^2}
```

---

### 1.2 High-Boost Filtering Conventions (CRITICAL DISAMBIGUATION)

Exam problems formulate high-boost filtering using three distinct mathematical conventions. To eliminate ambiguity, every numerical in this workbook explicitly states which convention is being deployed:

```text
+---------------------------------------------------------------------------------------------------+
| THREE HIGH-BOOST FILTERING CONVENTIONS                                                           |
+---------------------------------------------------------------------------------------------------+
| CONVENTION 1: Weighted Unsharp Masking                                                            |
| Spatial Definition:   g(x,y) = f(x,y) + k * g_mask(x,y) = f(x,y) + k * [f(x,y) - f_bar(x,y)]          |
| Amplification Parameter: k >= 0 (When k = 1, it reduces to standard unsharp masking)            |
| Frequency Response:   H_HB(u,v) = (1 + k) - k * H_LP(u,v) = A - (A - 1) * H_LP(u,v)  [where A=1+k] |
| Spatial Mask Center:  Uses a normalized averaging blur f_bar first, then adds k * detail mask.     |
+---------------------------------------------------------------------------------------------------+
| CONVENTION 2: Amplified-Original Filtering                                                        |
| Spatial Definition:   g(x,y) = A * f(x,y) - f_LP(x,y) = (A - 1) * f(x,y) + f_HP(x,y)               |
| Amplification Parameter: A >= 1 (When A = 1, it reduces to standard high-pass filtering)         |
| Frequency Response:   H_HB(u,v) = A - H_LP(u,v) = (A - 1) + H_HP(u,v)                              |
| Spatial Mask Center:  Direct subtraction of low-pass filtered image from amplified original.      |
+---------------------------------------------------------------------------------------------------+
| CONVENTION 3: Unnormalized Laplacian High Boost                                                   |
| Spatial Definition:   g(x,y) = (A - 1) * f(x,y) + L(x,y)                                          |
| Amplification Parameter: A >= 1                                                                   |
| 4-Neighbor Center Weight: w_c = A + 4 - 1 = A + 3                                                  |
| 8-Neighbor Center Weight: w_c = A + 8 - 1 = A + 7                                                  |
| Spatial Mask Form:    Constructs a composite 3x3 filter mask directly with center weight w_c.   |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Section 1: Frequency-Domain Filtering Numericals

<a id="numerical-11"></a>

### Numerical 1.1: Complete $4 \times 4$ Step-by-Step DFT High-Pass Filtering ($D_0 = 0.5$, IHPF)

#### ❓ Problem Statement
* **Source Label:** Reported PYQ (unverified)
* **Given Grid:** $4 \times 4$ spatial image $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0
\end{bmatrix}
```

* **Filter Type:** Ideal High-Pass Filter (IHPF)
* **Cutoff Frequency:** $D_0 = 0.5$
* **Task:** Perform full step-by-step frequency-domain filtering (centering, 2D DFT, distance calculation, filter response, spectral multiplication, 2D IDFT, un-centering). Evaluate the DC component and final average image intensity.

---

#### 💡 Step-by-Step Solution

##### Step 1: Pre-processing (Centering the Image)
Multiply $f(x,y)$ elementwise by $(-1)^{x+y}$:

```math
(-1)^{x+y} = \begin{bmatrix}
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1 \\
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1
\end{bmatrix}
```

```math
f'(x,y) = f(x,y) \cdot (-1)^{x+y} = \begin{bmatrix}
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0 \\
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0
\end{bmatrix}
```

---

##### Step 2: Compute 2D DFT $F(u,v)$
Using 2D matrix transformation $F = K \cdot f' \cdot K^T$, where the 4-point 1D DFT matrix $K$ ($W_4^k = e^{-j 2\pi k / 4}$) is:

```math
K = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

1. **First Matrix Multiplication $A = K \cdot f'$:**

```math
A = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0 \\
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0
\end{bmatrix} = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
4 & 0 & 4 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

2. **Second Matrix Multiplication $F = A \cdot K^T$:**

```math
F(u,v) = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
4 & 0 & 4 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix} = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
8 & 0 & 8 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

> 🎯 **Key Observation:** Because of centering, the DC component (total sum of $f(x,y)$ = $8$) is located at the spectrum center $F(2,2) = 8$.

---

##### Step 3: Distance Matrix $D(u,v)$ Calculation
With $M=4, N=4$, the center is $(u_0, v_0) = (2,2)$. Distance formula $D(u,v) = \sqrt{(u-2)^2 + (v-2)^2}$:

```math
D(u,v) = \begin{bmatrix}
\sqrt{8} & \sqrt{5} & 2 & \sqrt{5} \\
\sqrt{5} & \sqrt{2} & 1 & \sqrt{2} \\
2 & 1 & 0 & 1 \\
\sqrt{5} & \sqrt{2} & 1 & \sqrt{2}
\end{bmatrix} \approx \begin{bmatrix}
2.828 & 2.236 & 2.000 & 2.236 \\
2.236 & 1.414 & 1.000 & 1.414 \\
2.000 & 1.000 & 0.000 & 1.000 \\
2.236 & 1.414 & 1.000 & 1.414
\end{bmatrix}
```

---

##### Step 4: Ideal High-Pass Filter Response $H_{IHPF}(u,v)$ ($D_0 = 0.5$)

```math
H(u,v) = \begin{cases}
0 & \text{if } D(u,v) \le 0.5 \\
1 & \text{if } D(u,v) > 0.5
\end{cases}
```

Since $D(2,2) = 0.0 \le 0.5$, $H(2,2) = 0$. All other $D(u,v) > 0.5$, so $H(u,v) = 1$:

```math
H(u,v) = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
1 & 1 & 0 & 1 \\
1 & 1 & 1 & 1
\end{bmatrix}
```

---

##### Step 5: Elementwise Spectral Multiplication $G(u,v) = F(u,v) \circ H(u,v)$

```math
G(u,v) = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
8 & 0 & 8 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} \circ \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 \\
1 & 1 & 0 & 1 \\
1 & 1 & 1 & 1
\end{bmatrix} = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
8 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

> ⚠️ **DC Component Elimination:** Notice that $G(2,2) = 8 \times 0 = 0$. The High-Pass Filter completely blocked the DC component.

---

##### Step 6: 2D Inverse DFT $g'(x,y)$ and Un-centering $g(x,y)$
Applying 2D IDFT formula $g' = \frac{1}{16} K^* \cdot G \cdot (K^*)^T$:

1. $A_{inv} = K^* \cdot G$:

```math
A_{inv} = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & j & -1 & -j \\
1 & -1 & 1 & -1 \\
1 & -j & -1 & j
\end{bmatrix} \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
8 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} = \begin{bmatrix}
8 & 0 & 0 & 0 \\
-8 & 0 & 0 & 0 \\
8 & 0 & 0 & 0 \\
-8 & 0 & 0 & 0
\end{bmatrix}
```

2. $g' = \frac{1}{16} A_{inv} \cdot (K^*)^T$:

```math
g'(x,y) = \frac{1}{16} \begin{bmatrix}
8 & 0 & 0 & 0 \\
-8 & 0 & 0 & 0 \\
8 & 0 & 0 & 0 \\
-8 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & j & -1 & -j \\
1 & -1 & 1 & -1 \\
1 & -j & -1 & j
\end{bmatrix} = \begin{bmatrix}
0.5 & 0.5 & 0.5 & 0.5 \\
-0.5 & -0.5 & -0.5 & -0.5 \\
0.5 & 0.5 & 0.5 & 0.5 \\
-0.5 & -0.5 & -0.5 & -0.5
\end{bmatrix}
```

3. **Un-centering Multiplication $g(x,y) = g'(x,y) \circ (-1)^{x+y}$ (elementwise):**

```math
g(x,y) = \begin{bmatrix}
0.5 & 0.5 & 0.5 & 0.5 \\
-0.5 & -0.5 & -0.5 & -0.5 \\
0.5 & 0.5 & 0.5 & 0.5 \\
-0.5 & -0.5 & -0.5 & -0.5
\end{bmatrix} \circ \begin{bmatrix}
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1 \\
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1
\end{bmatrix} = \begin{bmatrix}
0.5 & -0.5 & 0.5 & -0.5 \\
0.5 & -0.5 & 0.5 & -0.5 \\
0.5 & -0.5 & 0.5 & -0.5 \\
0.5 & -0.5 & 0.5 & -0.5
\end{bmatrix}
```

---

##### 🎯 Final Results & Property Verification
1. **Final Output Image Grid $g(x,y)$:**

```math
g(x,y) = \begin{bmatrix}
0.5 & -0.5 & 0.5 & -0.5 \\
0.5 & -0.5 & 0.5 & -0.5 \\
0.5 & -0.5 & 0.5 & -0.5 \\
0.5 & -0.5 & 0.5 & -0.5
\end{bmatrix}
```

2. **Average Image Intensity Check:**
   * Sum of elements in $g(x,y) = 0.5 \times 8 + (-0.5) \times 8 = 0.0$.
   * Mean intensity $\bar{g} = 0.0$.
   * **Verification:** Since the High-Pass Filter eliminated the DC component $F(2,2)$, the average intensity of the output image MUST be zero.

---

<a id="numerical-12"></a>

### Numerical 1.2: Complete $4 \times 4$ Step-by-Step DFT Low-Pass Filtering ($D_0 = 1.5$, GLPF)

#### ❓ Problem Statement
* **Source Label:** Practice Numerical
* **Given Grid:** $4 \times 4$ spatial image $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
10 & 10 & 10 & 10 \\
10 & 50 & 50 & 10 \\
10 & 50 & 50 & 10 \\
10 & 10 & 10 & 10
\end{bmatrix}
```

* **Filter Type:** Gaussian Low-Pass Filter (GLPF)
* **Cutoff Frequency:** $D_0 = 1.5$
* **Task:** Calculate the distance matrix $D(u,v)$, the GLPF transfer function matrix $H_{\text{GLPF}}(u,v)$, the centered DC component, and prove that GLPF preserves the average image intensity.

---

#### 💡 Step-by-Step Solution

##### Step 1: Compute Centered DC Component $F(2,2)$
1. Total sum of input pixels:

```math
\sum_{x=0}^3 \sum_{y=0}^3 f(x,y) = (12 \times 10) + (4 \times 50) = 120 + 200 = 320
```

2. Under the centering property $f'(x,y) = f(x,y) \cdot (-1)^{x+y}$, the DC component shifts to $(u_0,v_0) = (2,2)$:

```math
F(2,2) = \sum_{x=0}^3 \sum_{y=0}^3 f(x,y) = 320
```

---

##### Step 2: Distance Matrix $D(u,v)$ ($4 \times 4$, Center at $(2,2)$)

```math
D(u,v) = \begin{bmatrix}
2.828 & 2.236 & 2.000 & 2.236 \\
2.236 & 1.414 & 1.000 & 1.414 \\
2.000 & 1.000 & 0.000 & 1.000 \\
2.236 & 1.414 & 1.000 & 1.414
\end{bmatrix}
```

---

##### Step 3: Gaussian Low-Pass Filter Response Matrix $H_{\text{GLPF}}(u,v)$ ($D_0 = 1.5$)
Formula: $H(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}} = e^{-\frac{D^2(u,v)}{2 (1.5)^2}} = e^{-\frac{D^2(u,v)}{4.5}}$

* $D^2(2,2) = 0 \implies H(2,2) = e^0 = 1.0000$
* $D^2(2,1) = 1 \implies H(2,1) = e^{-1/4.5} = e^{-0.2222} \approx 0.8007$
* $D^2(1,1) = 2 \implies H(1,1) = e^{-2/4.5} = e^{-0.4444} \approx 0.6412$
* $D^2(2,0) = 4 \implies H(2,0) = e^{-4/4.5} = e^{-0.8889} \approx 0.4111$
* $D^2(1,0) = 5 \implies H(1,0) = e^{-5/4.5} = e^{-1.1111} \approx 0.3292$
* $D^2(0,0) = 8 \implies H(0,0) = e^{-8/4.5} = e^{-1.7778} \approx 0.1690$

```math
H_{\text{GLPF}}(u,v) = \begin{bmatrix}
0.1690 & 0.3292 & 0.4111 & 0.3292 \\
0.3292 & 0.6412 & 0.8007 & 0.6412 \\
0.4111 & 0.8007 & 1.0000 & 0.8007 \\
0.3292 & 0.6412 & 0.8007 & 0.6412
\end{bmatrix}
```

---

##### Step 4: DC Component Preservation and Average Intensity
1. **Filtered DC Component $G(2,2)$:**

```math
G(2,2) = F(2,2) \times H(2,2) = 320 \times 1.0000 = 320
```

2. **Average Intensity of Filtered Image $\bar{g}$:**

```math
\bar{g} = \frac{G(2,2)}{N \times N} = \frac{320}{16} = 20.0
```

3. **Comparison with Input Image Mean $\bar{f}$:**

```math
\bar{f} = \frac{320}{16} = 20.0
```

> ⭐ **Must Remember:** Any Low-Pass Filter with $H(u_0, v_0) = 1.0$ at the DC origin preserves the exact mean intensity of the original image ($\bar{g} = \bar{f}$).

##### Step 5: Center the Image and Compute the Full 2D DFT
Use the same unnormalized forward DFT and $1/16$ inverse-DFT convention as Numerical 1.1. Multiplication by $(-1)^{x+y}$ is elementwise; the centered DC value is $F_c(2,2)=320$.

```math
f_c(x,y)=f(x,y)(-1)^{x+y}=\begin{bmatrix}
10 & -10 & 10 & -10 \\
-10 & 50 & -50 & 10 \\
10 & -50 & 50 & -10 \\
-10 & 10 & -10 & 10
\end{bmatrix}
```

```math
F_c(u,v)=\sum_{x=0}^{3}\sum_{y=0}^{3}f_c(x,y)e^{-j2\pi(ux/4+vy/4)}=\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & -80j & -80+80j & 80 \\
0 & -80+80j & 320 & -80-80j \\
0 & 80 & -80-80j & 80j
\end{bmatrix}
```

##### Step 6: Multiply by the Gaussian Filter
Use exact $H(u,v)=e^{-D^2(u,v)/4.5}$ before rounding the displayed result.

```math
G(u,v)=F_c(u,v)\circ H_{\mathrm{GLPF}}(u,v)\approx \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & -51.2944j & -64.059+64.059j & 51.2944 \\
0 & -64.059+64.059j & 320 & -64.059-64.059j \\
0 & 51.2944 & -64.059-64.059j & 51.2944j
\end{bmatrix}
```

##### Step 7: Inverse DFT and Un-centering
Compute $g_c=\operatorname{Re}\{\operatorname{IDFT}[G]\}$ and multiply it elementwise by $(-1)^{x+y}$. The imaginary residual is zero to numerical precision.

```math
g_c(x,y)\approx \begin{bmatrix}
10.3971 & -13.5882 & 13.5882 & -10.3971 \\
-13.5882 & 42.4266 & -42.4266 & 13.5882 \\
13.5882 & -42.4266 & 42.4266 & -13.5882 \\
-10.3971 & 13.5882 & -13.5882 & 10.3971
\end{bmatrix}
```

```math
g(x,y)=g_c(x,y)\circ(-1)^{x+y}\approx \begin{bmatrix}
10.3971 & 13.5882 & 13.5882 & 10.3971 \\
13.5882 & 42.4266 & 42.4266 & 13.5882 \\
13.5882 & 42.4266 & 42.4266 & 13.5882 \\
10.3971 & 13.5882 & 13.5882 & 10.3971
\end{bmatrix}
```

**Verification:** The exact output sum is 320 and its mean is $320/16=20$. The four-decimal entries may introduce slight rounding differences. This DFT example uses periodic boundary conditions; different padding changes border pixels.

---

<a id="numerical-13"></a>

### Numerical 1.3: Comparative Grid Evaluation of Ideal, Butterworth, and Gaussian Filters

#### ❓ Problem Statement
* **Source Label:** Practice Numerical
* **Task:** Given a $4 \times 4$ frequency grid centered at $(2,2)$ and a cutoff frequency $D_0 = 1.0$, construct and compare the transfer function matrices for:
  1. **Ideal Low-Pass Filter (ILPF)**
  2. **Butterworth Low-Pass Filter (BLPF)** of order $n=2$
  3. **Gaussian Low-Pass Filter (GLPF)**

---

#### 💡 Step-by-Step Solution

##### 1. Distance Matrix $D(u,v)$ ($4 \times 4$, Center $(2,2)$)

```math
D(u,v) = \begin{bmatrix}
2.828 & 2.236 & 2.000 & 2.236 \\
2.236 & 1.414 & 1.000 & 1.414 \\
2.000 & 1.000 & 0.000 & 1.000 \\
2.236 & 1.414 & 1.000 & 1.414
\end{bmatrix}
```

---

##### 2. Ideal Low-Pass Filter Matrix $H_{\text{ILPF}}(u,v)$ ($D_0 = 1.0$)
$$H(u,v) = 1 \text{ if } D(u,v) \le 1.0 \text{ else } 0$$
Only coordinates with $D(u,v) \le 1.0$ are $(2,2), (2,1), (2,3), (1,2), (3,2)$:

```math
H_{\text{ILPF}}(u,v) = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
```

---

##### 3. Butterworth Low-Pass Filter Matrix $H_{\text{BLPF}}(u,v)$ ($D_0 = 1.0, n=2$)
Formula: $H(u,v) = \frac{1}{1 + [D(u,v)/D_0]^{2n}} = \frac{1}{1 + D(u,v)^4}$

* $D = 0.0 \implies H = \frac{1}{1 + 0} = 1.0000$
* $D = 1.0 \implies H = \frac{1}{1 + 1^4} = 0.5000$
* $D = 1.414 \implies H = \frac{1}{1 + (1.414)^4} = \frac{1}{1 + 4} = 0.2000$
* $D = 2.000 \implies H = \frac{1}{1 + 2^4} = \frac{1}{17} \approx 0.0588$
* $D = 2.236 \implies H = \frac{1}{1 + (2.236)^4} = \frac{1}{1 + 25} = 0.0385$
* $D = 2.828 \implies H = \frac{1}{1 + (2.828)^4} = \frac{1}{1 + 64} = 0.0154$

```math
H_{\text{BLPF}}(u,v) = \begin{bmatrix}
0.0154 & 0.0385 & 0.0588 & 0.0385 \\
0.0385 & 0.2000 & 0.5000 & 0.2000 \\
0.0588 & 0.5000 & 1.0000 & 0.5000 \\
0.0385 & 0.2000 & 0.5000 & 0.2000
\end{bmatrix}
```

---

##### 4. Gaussian Low-Pass Filter Matrix $H_{\text{GLPF}}(u,v)$ ($D_0 = 1.0$)
Formula: $H(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}} = e^{-\frac{D^2(u,v)}{2}}$

* $D^2 = 0.0 \implies H = e^0 = 1.0000$
* $D^2 = 1.0 \implies H = e^{-0.5} \approx 0.6065$
* $D^2 = 2.0 \implies H = e^{-1.0} \approx 0.3679$
* $D^2 = 4.0 \implies H = e^{-2.0} \approx 0.1353$
* $D^2 = 5.0 \implies H = e^{-2.5} \approx 0.0821$
* $D^2 = 8.0 \implies H = e^{-4.0} \approx 0.0183$

```math
H_{\text{GLPF}}(u,v) = \begin{bmatrix}
0.0183 & 0.0821 & 0.1353 & 0.0821 \\
0.0821 & 0.3679 & 0.6065 & 0.3679 \\
0.1353 & 0.6065 & 1.0000 & 0.6065 \\
0.0821 & 0.3679 & 0.6065 & 0.3679
\end{bmatrix}
```

---

##### 📊 Comparative Summary Table

| Metric / Filter | Ideal Low-Pass Filter | Butterworth LPF ($n=2$) | Gaussian LPF |
|---|---|---|---|
| **Value at Origin $D=0$** | $1.0000$ | $1.0000$ | $1.0000$ |
| **Value at Cutoff $D=D_0$** | $1.0000$ (Discontinuous drop) | $0.5000$ (Exactly 50% cutoff) | $0.6065$ ($e^{-0.5}$) |
| **Transition Smoothness** | Abrupt Step Function | Smooth controlled roll-off | Perfectly smooth exponential |
| **Spatial Ringing Effect** | **Severe Ringing** (oscillatory spatial sidelobes for a circular cutoff) | Mild Ringing ($n \le 2$) | Avoids ideal-cutoff ringing; other artifacts remain possible |

---

## 3. Section 2: Spatial-Sharpening Numericals

<a id="numerical-21"></a>

### Numerical 2.1: 1D Scanline First and Second Finite Differences Across Step and Ramp Edges

#### ❓ Problem Statement
* **Source Label:** Reported PYQ (unverified; NMIMS TEE attribution not checked)
* **Given Scanline:** 1D discrete intensity profile $f(x)$:

| Index $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **$f(x)$** | 5 | 5 | 5 | 5 | 2 | 1 | 0 | 0 | 6 | 0 | 0 | 0 |

* **Tasks:**
  1. Compute the first finite difference $\frac{\partial f}{\partial x} = f(x+1) - f(x)$.
  2. Compute the second finite difference $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$.
  3. Analyze derivative behavior across constant plateaus, ramp slopes, step edges, and isolated points.

---

#### 💡 Step-by-Step Solution

##### 1. Formula Definitions
* **Forward First Derivative:** $\frac{\partial f}{\partial x} = f(x+1) - f(x)$
* **Centered Second Derivative:** $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$

---

##### 2. Detailed Point-by-Point Calculations

* **$x=0$:** Boundary pixel ($f(x-1)$ unavailable). First diff = $f(1)-f(0) = 5-5 = 0$.
* **$x=1$:** $f(1)=5$. First diff = $5-5 = 0$. Second diff = $5 + 5 - 2(5) = 0$.
* **$x=2$:** $f(2)=5$. First diff = $f(3)-f(2) = 5-5 = 0$. Second diff = $5 + 5 - 2(5) = 0$.
* **$x=3$ (Ramp Onset):** $f(3)=5$.
  * First diff = $f(4)-f(3) = 2 - 5 = -3$.
  * Second diff = $f(4) + f(2) - 2f(3) = 2 + 5 - 2(5) = 7 - 10 = -3$.
* **$x=4$ (Ramp Slope):** $f(4)=2$.
  * First diff = $f(5)-f(4) = 1 - 2 = -1$.
  * Second diff = $f(5) + f(3) - 2f(4) = 1 + 5 - 2(2) = 6 - 4 = +2$.
* **$x=5$ (Ramp Slope):** $f(5)=1$.
  * First diff = $f(6)-f(5) = 0 - 1 = -1$.
  * Second diff = $f(6) + f(4) - 2f(5) = 0 + 2 - 2(1) = 0$.
* **$x=6$ (Ramp End):** $f(6)=0$.
  * First diff = $f(7)-f(6) = 0 - 0 = 0$.
  * Second diff = $f(7) + f(5) - 2f(6) = 0 + 1 - 2(0) = +1$.
* **$x=7$ (Constant Zero):** $f(7)=0$.
  * First diff = $f(8)-f(7) = 6 - 0 = +6$.
  * Second diff = $f(8) + f(6) - 2f(7) = 6 + 0 - 0 = +6$.
* **$x=8$ (Isolated Point / Peak):** $f(8)=6$.
  * First diff = $f(9)-f(8) = 0 - 6 = -6$.
  * Second diff = $f(9) + f(7) - 2f(8) = 0 + 0 - 2(6) = -12$.
* **$x=9$ (Step Edge Return):** $f(9)=0$.
  * First diff = $f(10)-f(9) = 0 - 0 = 0$.
  * Second diff = $f(10) + f(8) - 2f(9) = 0 + 6 - 0 = +6$.
* **$x=10$:** Constant flat region. Both derivatives = $0$.

---

##### 📊 Complete 1D Derivative Computation Table

| Index $x$ | $f(x)$ | $\frac{\partial f}{\partial x}$ | $\frac{\partial^2 f}{\partial x^2}$ | Region Feature Description |
|---|---|---|---|---|
| 0 | 5 | 0 | — | Constant Plateau |
| 1 | 5 | 0 | 0 | Constant Plateau |
| 2 | 5 | 0 | 0 | Constant Plateau |
| 3 | 5 | **-3** | **-3** | Ramp Start (Negative Spike) |
| 4 | 2 | **-1** | **+2** | Ramp Transition |
| 5 | 1 | **-1** | **0** | Ramp Slope (First diff non-zero, Second diff ZERO) |
| 6 | 0 | **0** | **+1** | Ramp End (Positive Spike) |
| 7 | 0 | **+6** | **+6** | Step Edge Transition Onset |
| 8 | 6 | **-6** | **-12** | **Isolated Point Peak** (Massive Negative Double Response) |
| 9 | 0 | **0** | **+6** | Step Edge Return |
| 10 | 0 | 0 | 0 | Constant Plateau |
| 11 | 0 | — | — | Boundary Pixel |

---

##### 🧠 Theoretical Insights & Exam Takeaways
1. **Constant Areas:** Both 1st and 2nd derivatives evaluate to **zero** in flat regions.
2. **Ramp Slopes ($x=4,5$):**
   * **First derivative** remains non-zero ($-1$) throughout the entire ramp.
   * **Second derivative** is non-zero ONLY at the start ($-3$) and end ($+1$) of the ramp, and evaluates to **zero** along the constant slope.
3. **Step Edges / Isolated Points ($x=8$):**
   * The second derivative exhibits a **double-response** sign reversal ($-3$ to $+2$, $+6$ to $-12$ to $+6$).
   * This sign reversal produces a **zero-crossing**, which marks the exact center location of an edge.

---

<a id="numerical-22"></a>

### Numerical 2.2: 2D Spatial Laplacian Convolution on a $6 \times 6$ Step Edge Image ($8$-Neighbor)

#### ❓ Problem Statement
* **Source Label:** Reported PYQ (unverified; NMIMS 2023–24 attribution not checked)
* **Given Image:** $6 \times 6$ matrix with a horizontal step edge from 50 to 100:

```math
f(x,y) = \begin{bmatrix}
50 & 50 & 50 & 50 & 50 & 50 \\
50 & 50 & 50 & 50 & 50 & 50 \\
50 & 50 & 50 & 50 & 50 & 50 \\
100 & 100 & 100 & 100 & 100 & 100 \\
100 & 100 & 100 & 100 & 100 & 100 \\
100 & 100 & 100 & 100 & 100 & 100
\end{bmatrix}
```

* **Mask:** 8-neighbor Laplacian mask with negative center weight:

```math
w = \begin{bmatrix}
1 & 1 & 1 \\
1 & -8 & 1 \\
1 & 1 & 1
\end{bmatrix}
```

* **Tasks:**
  1. Compute the interior Laplacian response $\nabla^2 f(x,y)$.
  2. Compute the composite sharpened image $g(x,y) = f(x,y) - \nabla^2 f(x,y)$ with display range clipping $[0, 255]$.

---

#### 💡 Step-by-Step Solution

##### 1. Boundary Handling Policy
Since no padding is specified, convolution is evaluated strictly on **valid interior pixels** (Rows 2 to 5, Columns 2 to 5), yielding an interior output matrix.

---

##### 2. Interior Pixel Laplacian Calculations

* **Row 2 (Upper Side of Step Edge, Intensity 50):**
  Neighborhood centered at $(2,c)$:
  * Top 3 neighbors (Row 1) = $50, 50, 50$
  * Left & Right neighbors (Row 2) = $50, 50$
  * Center pixel = $50$
  * Bottom 3 neighbors (Row 3) = $100, 100, 100$

```math
\nabla^2 f(2,c) = (3 \times 50) + (2 \times 50) + (3 \times 100) - (8 \times 50) = 150 + 100 + 300 - 400 = +150
```

* **Row 3 (Lower Side of Step Edge, Intensity 100):**
  Neighborhood centered at $(3,c)$:
  * Top 3 neighbors (Row 2) = $50, 50, 50$
  * Left & Right neighbors (Row 3) = $100, 100$
  * Center pixel = $100$
  * Bottom 3 neighbors (Row 4) = $100, 100, 100$

```math
\nabla^2 f(3,c) = (3 \times 50) + (2 \times 100) + (3 \times 100) - (8 \times 100) = 150 + 200 + 300 - 800 = -150
```

* **Flat Regions (Rows 1, 4):**
  All 9 neighbors are identical ($50$ or $100$).
  $\nabla^2 f = 8(50) - 8(50) = 0$ or $8(100) - 8(100) = 0$.

---

##### 3. Intermediate Output Laplacian Matrix $\nabla^2 f(x,y)$ (Interior $4 \times 4$)

```math
\nabla^2 f(x,y) = \begin{bmatrix}
0 & 0 & 0 & 0 \\
+150 & +150 & +150 & +150 \\
-150 & -150 & -150 & -150 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

---

##### 4. Composite Sharpening $g(x,y) = f(x,y) - \nabla^2 f(x,y)$ & Display Range Clipping
Because the center weight is **negative** ($-8$), the composite formula requires **subtracting** the Laplacian response:

* **Row 1 (Flat 50):** $g = 50 - 0 = 50$
* **Row 2 (Upper Edge 50):** $g = 50 - (+150) = -100 \implies \mathbf{0}$ *(Clipped to 0)*
* **Row 3 (Lower Edge 100):** $g = 100 - (-150) = 250 \implies \mathbf{250}$ *(Valid in $[0,255]$)*
* **Row 4 (Flat 100):** $g = 100 - 0 = 100$

---

##### 🎯 Final Sharpened Output Matrix $g(x,y)$

```math
g(x,y) = \begin{bmatrix}
50 & 50 & 50 & 50 \\
0 & 0 & 0 & 0 \\
250 & 250 & 250 & 250 \\
100 & 100 & 100 & 100
\end{bmatrix}
```

> 🧠 **Must Understand:** The edge transition in the original image was $50 \to 100$ (a difference of $50$). In the sharpened output image, the transition becomes $0 \to 250$ (a difference of $250$). This massive contrast enhancement represents the essence of Laplacian edge sharpening!

---

<a id="numerical-23"></a>

### Numerical 2.3: 2D Spatial Laplacian Edge Enhancement on a $5 \times 5$ Grid ($4$- & $8$-Neighbor)

#### ❓ Problem Statement
* **Source Label:** Reported PYQ (unverified)
* **Given Image:** $5 \times 5$ grayscale image $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
10 & 10 & 10 & 10 & 10 \\
10 & 20 & 20 & 20 & 10 \\
10 & 20 & 40 & 20 & 10 \\
10 & 20 & 20 & 20 & 10 \\
10 & 10 & 10 & 10 & 10
\end{bmatrix}
```

* **Tasks:**
  1. Apply 4-neighbor negative-center Laplacian mask $w_4$:

```math
w_4 = \begin{bmatrix}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0
\end{bmatrix}
```

  2. Apply 8-neighbor negative-center Laplacian mask $w_8$:

```math
w_8 = \begin{bmatrix}
1 & 1 & 1 \\
1 & -8 & 1 \\
1 & 1 & 1
\end{bmatrix}
```

  3. Compute the interior $3 \times 3$ sharpened image matrices $g(x,y) = f(x,y) - \nabla^2 f(x,y)$ for both masks.

---

#### 💡 Step-by-Step Solution

##### 1. Center Pixel Calculation at $(2,2)$ ($f(2,2) = 40$)
* **Neighborhood centered at $(2,2)$:**
  * Top row: $20, 20, 20$
  * Middle row: $20, \mathbf{40}, 20$
  * Bottom row: $20, 20, 20$

1. **4-Neighbor Laplacian $\nabla^2_4 f(2,2)$:**

```math
\nabla^2_4 f = 1(20) + 1(20) + 1(20) + 1(20) - 4(40) = 80 - 160 = -80
```

2. **8-Neighbor Laplacian $\nabla^2_8 f(2,2)$:**

```math
\nabla^2_8 f = 8(20) - 8(40) = 160 - 320 = -160
```

3. **Sharpened Intensity $g(2,2) = f(2,2) - \nabla^2 f(2,2)$:**
   * **4-Neighbor:** $g(2,2) = 40 - (-80) = \mathbf{120}$
   * **8-Neighbor:** $g(2,2) = 40 - (-160) = \mathbf{200}$

---

##### 2. Complete Interior $3 \times 3$ Matrix Computations

1. **For 4-Neighbor Mask $w_4$:**

* **At $(1,1)$ ($f=20$):** Neighbors (0,1)=10, (2,1)=20, (1,0)=10, (1,2)=20.
  $\nabla^2 f = 10+20+10+20 - 4(20) = 60 - 80 = -20 \implies g = 20 - (-20) = 40$.
* **At $(1,2)$ ($f=20$):** Neighbors (0,2)=10, (2,2)=40, (1,1)=20, (1,3)=20.
  $\nabla^2 f = 10+40+20+20 - 4(20) = 90 - 80 = +10 \implies g = 20 - 10 = 10$.

```math
\nabla^2_4 f(x,y) = \begin{bmatrix}
-20 & +10 & -20 \\
+10 & -80 & +10 \\
-20 & +10 & -20
\end{bmatrix}
```

```math
g_4(x,y) = f - \nabla^2_4 f = \begin{bmatrix}
40 & 10 & 40 \\
10 & 120 & 10 \\
40 & 10 & 40
\end{bmatrix}
```

2. **For 8-Neighbor Mask $w_8$:**

```math
\nabla^2_8 f(x,y) = \begin{bmatrix}
-30 & -10 & -30 \\
-10 & -160 & -10 \\
-30 & -10 & -30
\end{bmatrix}
```

```math
g_8(x,y) = f - \nabla^2_8 f = \begin{bmatrix}
50 & 30 & 50 \\
30 & 200 & 30 \\
50 & 30 & 50
\end{bmatrix}
```

---

##### 🎯 Comparison of 4-Neighbor vs. 8-Neighbor Results
* At the center, the 8-neighbor Laplacian response is $-160$ versus $-80$ for the 4-neighbor mask; the sharpened center values are $200$ and $120$. The corrected side response is $-10$, giving a sharpened side value of $30$.

---

<a id="numerical-24"></a>

### Numerical 2.4: High-Boost Spatial Filter Mask Construction and Convolution ($A = 1.0, 1.5, 2.0$)

#### ❓ Problem Statement
* **Source Label:** Reported PYQ (unverified; NMIMS Dec 2025 attribution not checked)
* **Given Neighborhood:** $3 \times 3$ image segment $f$:

```math
f = \begin{bmatrix}
10 & 20 & 30 \\
40 & 30 & 20 \\
10 & 20 & 30
\end{bmatrix}
```

* **Tasks:**
  1. Identify High-Boost Convention 3 (Unnormalized Laplacian High-Boost) for 4-neighbor and 8-neighbor formulations.
  2. Construct the 4-neighbor high-boost filter mask for amplification factors $A = 1.0$, $A = 1.5$, and $A = 2.0$.
  3. Calculate the center pixel response for each $A$.
  4. Compare with High-Boost Convention 1 (Weighted Unsharp Masking using $3 \times 3$ Box Blur).

---

#### 💡 Step-by-Step Solution

##### Part A: Convention 3 (Unnormalized Laplacian Mask Construction)
1. **Formula for Center Weight $w_c$ (4-Neighbor Mask):**

```math
w_{hb} = \begin{bmatrix}
0 & -1 & 0 \\
-1 & w_c & -1 \\
0 & -1 & 0
\end{bmatrix} \quad \text{where } w_c = A + 4 - 1 = A + 3
```

2. **Constructing Masks and Computing Center Responses:**

* **Case 1 ($A = 1.0$ — Standard High-Pass Sharpening):**
  Center weight: $w_c = 1.0 + 3 = 4$.

```math
w_{hb1} = \begin{bmatrix}
0 & -1 & 0 \\
-1 & 4 & -1 \\
0 & -1 & 0
\end{bmatrix}
```

```math
\text{Response} = 4(30) - 1(20) - 1(40) - 1(20) - 1(20) = 120 - 100 = \mathbf{20}
```

* **Case 2 ($A = 1.5$ — High-Boost Filtering):**
  Center weight: $w_c = 1.5 + 3 = 4.5$.

```math
w_{hb1.5} = \begin{bmatrix}
0 & -1 & 0 \\
-1 & 4.5 & -1 \\
0 & -1 & 0
\end{bmatrix}
```

```math
\text{Response} = 4.5(30) - 100 = 135 - 100 = \mathbf{35}
```

* **Case 3 ($A = 2.0$ — High-Boost Filtering):**
  Center weight: $w_c = 2.0 + 3 = 5.0$.

```math
w_{hb2} = \begin{bmatrix}
0 & -1 & 0 \\
-1 & 5.0 & -1 \\
0 & -1 & 0
\end{bmatrix}
```

```math
\text{Response} = 5.0(30) - 100 = 150 - 100 = \mathbf{50}
```

---

##### Part B: Convention 1 (Weighted Unsharp Masking Comparison)
1. **Compute $3 \times 3$ Averaging Blur $\bar{f}(1,1)$:**

```math
\bar{f} = \frac{10 + 20 + 30 + 40 + 30 + 20 + 10 + 20 + 30}{9} = \frac{210}{9} = 23.333
```

2. **Compute Detail Unsharp Mask $g_{\text{mask}} = f - \bar{f}$:**

```math
g_{\text{mask}}(1,1) = 30 - 23.333 = +6.667
```

3. **Compute High-Boost Output $g_{\text{hb}} = f + k \cdot g_{\text{mask}}$ (where $k = A - 1$):**
   * **For $A = 1.0 \implies k = 0$:** $g_{\text{hb}} = 30 + 0 = 30.00$
   * **For $A = 1.5 \implies k = 0.5$:** $g_{\text{hb}} = 30 + 0.5(6.667) = 30 + 3.333 = \mathbf{33.33}$
   * **For $A = 2.0 \implies k = 1.0$:** $g_{\text{hb}} = 30 + 1.0(6.667) = 30 + 6.667 = \mathbf{36.67}$

> 🧠 **Must Understand:** Convention 3 sharpens edges strictly using 2D derivative differences, while Convention 1 sharpens relative to local neighborhood area smoothing. Always state which convention you are using!

---

## 4. Section 3: Frequency-Domain High-Boost & Unsharp Masking Evaluations

<a id="numerical-31"></a>

### Numerical 3.1: Derivation & Numerical Evaluation of High-Boost Frequency Transfer Functions

#### ❓ Problem Statement
* **Source Label:** Reported PYQ (unverified)
* **Tasks:**
  1. Derive the Frequency-Domain Transfer Function $H_{\text{HB}}(u,v)$ under Convention 2 ($g = A f - f_{\text{lp}}$) and Convention 1 ($g = f + k(f - f_{\text{lp}})$).
  2. Numerically evaluate $H_{\text{HB}}(u,v)$ for a Gaussian Low-Pass Filter ($D_0 = 50$) at distance $D = 50$ for amplification factors $A = 1.0, 1.25, 1.50, 2.00$.
  3. Numerically evaluate $H_{\text{HB}}(u,v)$ for a Butterworth Low-Pass Filter ($n=2, D_0 = 50$) at distances $D = 25, 50, 100$ with $A = 1.5$.

---

#### 💡 Step-by-Step Solution

##### Part 1: Theoretical Derivations

1. **Derivation under Convention 2 (Amplified Original):**
   * Spatial equation: $g_{\text{hb}}(x,y) = A \cdot f(x,y) - f_{\text{lp}}(x,y)$
   * Taking Fourier Transform: $G_{\text{hb}}(u,v) = A \cdot F(u,v) - F(u,v) \cdot H_{\text{LP}}(u,v) = F(u,v) [A - H_{\text{LP}}(u,v)]$
   * **Transfer Function:**

```math
H_{\text{HB, Conv2}}(u,v) = A - H_{\text{LP}}(u,v) = (A - 1) + H_{\text{HP}}(u,v)
```

2. **Derivation under Convention 1 (Weighted Unsharp Masking, $A = 1+k$):**
   * Spatial equation: $g_{\text{hb}}(x,y) = f(x,y) + k [f(x,y) - f_{\text{lp}}(x,y)] = (1+k) f(x,y) - k \cdot f_{\text{lp}}(x,y)$
   * Substituting $A = 1+k \implies k = A-1$:
   * **Transfer Function:**

```math
H_{\text{HB, Conv1}}(u,v) = A - (A - 1) H_{\text{LP}}(u,v)
```

---

##### Part 2: Numerical Evaluation for Gaussian Filter ($D_0 = 50, D = 50$)
For Gaussian LPF: $H_{\text{GLPF}}(50) = e^{-\frac{50^2}{2(50)^2}} = e^{-0.5} \approx 0.6065$.

Using Convention 2 formula $H_{\text{HB}}(u,v) = A - H_{\text{LP}}(u,v)$:

* **For $A = 1.00$:** $H_{\text{HB}} = 1.00 - 0.6065 = \mathbf{0.3935}$ (Standard High-Pass Filter)
* **For $A = 1.25$:** $H_{\text{HB}} = 1.25 - 0.6065 = \mathbf{0.6435}$
* **For $A = 1.50$:** $H_{\text{HB}} = 1.50 - 0.6065 = \mathbf{0.8935}$
* **For $A = 2.00$:** $H_{\text{HB}} = 2.00 - 0.6065 = \mathbf{1.3935}$

> ⭐ **Must Remember:** When $A > 1.0$, the transfer function magnitude $H_{\text{HB}}(u,v)$ exceeds $1.0$ at high frequencies, actively boosting high-frequency detail while preserving low frequencies!

---

##### Part 3: Numerical Evaluation for Butterworth Filter ($n=2, D_0 = 50, A = 1.5$)
Butterworth LPF formula: $H_{\text{BLPF}}(D) = \frac{1}{1 + (D/50)^4}$

1. **At $D = 25$ ($D = 0.5 D_0$):**
   * $H_{\text{BLPF}}(25) = \frac{1}{1 + (0.5)^4} = \frac{1}{1 + 0.0625} = \frac{1}{1.0625} \approx 0.9412$
   * $H_{\text{HB}}(25) = 1.50 - 0.9412 = \mathbf{0.5588}$
2. **At $D = 50$ ($D = D_0$):**
   * $H_{\text{BLPF}}(50) = \frac{1}{1 + 1^4} = 0.5000$
   * $H_{\text{HB}}(50) = 1.50 - 0.5000 = \mathbf{1.0000}$
3. **At $D = 100$ ($D = 2 D_0$):**
   * $H_{\text{BLPF}}(100) = \frac{1}{1 + 2^4} = \frac{1}{17} \approx 0.0588$
   * $H_{\text{HB}}(100) = 1.50 - 0.0588 = \mathbf{1.4412}$

---

## 5. Section 4: Master Formula & Mask Quick Reference

### 5.1 Frequency-Domain Transfer Functions

```math
D(u,v) = \sqrt{\left(u - \frac{M}{2}\right)^2 + \left(v - \frac{N}{2}\right)^2}
```

* **Ideal Low-Pass / High-Pass:**

```math
H_{\text{ILPF}}(u,v) = \begin{cases} 1 & D(u,v) \le D_0 \\ 0 & D(u,v) > D_0 \end{cases}, \quad H_{\text{IHPF}}(u,v) = 1 - H_{\text{ILPF}}(u,v)
```

* **Butterworth Low-Pass / High-Pass:**

```math
H_{\text{BLPF}}(u,v) = \frac{1}{1 + \left[\frac{D(u,v)}{D_0}\right]^{2n}}, \quad H_{\text{BHPF}}(u,v) = \frac{1}{1 + \left[\frac{D_0}{D(u,v)}\right]^{2n}}
```

* **Gaussian Low-Pass / High-Pass:**

```math
H_{\text{GLPF}}(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}}, \quad H_{\text{GHPF}}(u,v) = 1 - e^{-\frac{D^2(u,v)}{2 D_0^2}}
```

---

### 5.2 Standard Spatial Derivative Masks

* **2D Laplacian Masks (Negative Center Weight):**

```text
4-Neighbor Mask (Negative Center):             8-Neighbor Mask (Negative Center):
        [  0   1   0 ]                                [  1   1   1 ]
        [  1  -4   1 ]                                [  1  -8   1 ]
        [  0   1   0 ]                                [  1   1   1 ]
Composite: g = f - 
abla^2 f                  Composite: g = f - 
abla^2 f
```

* **2D Laplacian Masks (Positive Center Weight):**

```text
4-Neighbor Mask (Positive Center):             8-Neighbor Mask (Positive Center):
        [  0  -1   0 ]                                [ -1  -1  -1 ]
        [ -1   4  -1 ]                                [ -1   8  -1 ]
        [  0  -1   0 ]                                [ -1  -1  -1 ]
Composite: g = f + 
abla^2 f                  Composite: g = f + 
abla^2 f
```

* **High-Boost Spatial Masks (Unnormalized Convention 3):**

```text
4-Neighbor High-Boost Mask:                    8-Neighbor High-Boost Mask:
        [  0  -1   0 ]                                [ -1  -1  -1 ]
        [ -1  A+3 -1 ]                                [ -1  A+7 -1 ]
        [  0  -1   0 ]                                [ -1  -1  -1 ]
```

---

## 6. Section 5: Common Numerical Pitfalls & Exam Checklist

### ⚠️ Common Numerical Pitfalls
1. ❌ **Forgetting Centering Multiplication:** Failing to multiply $f(x,y)$ by $(-1)^{x+y}$ leaves the DC component at $(0,0)$ instead of grid center $(M/2, N/2)$.
2. ❌ **Inverting Laplacian Sign Rules:** Adding a negative-center Laplacian mask instead of subtracting it causes **smoothing** instead of sharpening.
3. ❌ **Confusing High-Boost Center Weights:** Writing center weight $A$ instead of $A+3$ (4-neighbor) or $A+7$ (8-neighbor) in unnormalized spatial masks.
4. ❌ **Treating Border Placeholders as Computed Values:** Filling unpadded border rows/columns with zeroes and claiming they are valid convolution outputs.

---

### ✍️ Final Exam Readiness Checklist
* [x] Have you verified that all multirow matrices are enclosed in standalone ` ```math ` code fences?
* [x] Are all matrix rows separated by newlines with `\\` at row ends?
* [x] Are the High-Boost conventions clearly identified before every derivation?
* [x] Did you check that the DC component $F(M/2, N/2)$ equals the sum of input spatial pixels?
* [x] Is display range clipping $[0, 255]$ checked for all spatial sharpening numericals?