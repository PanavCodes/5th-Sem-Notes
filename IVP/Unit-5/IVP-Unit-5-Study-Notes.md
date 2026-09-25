# 📚 IVP Unit 5: Edge Detection — Comprehensive Study Notes

---

## 📌 Syllabus & Exam Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 5 — Edge Detection
* **Target Audience:** B.Tech (CSE / EXTC / IT) Examination & Lab Review
* **Format:** GitHub Flavored Markdown (GFM) with GFM Math (` ```math `)
* **Strict Unit 5 Syllabus Coverage:**
  1. Gradient-based edge detection using First-Order Derivatives
  2. Edge detection using Second-Order Derivatives
  3. Prewitt Operator
  4. Sobel Operator
  5. Laplacian Operator
  6. Laplacian of Gaussian (LoG) / Marr-Hildreth Filter
  7. Canny Edge Detector

---

## 📑 Table of Contents

1. [Section 1: Fundamentals of Image Edges & Derivative Operations](#section-1-fundamentals-of-image-edges--derivative-operations)
   * 1.1 [What is an Image Edge? Types of Intensity Profiles](#11-what-is-an-image-edge-types-of-intensity-profiles)
   * 1.2 [First-Order vs. Second-Order Derivatives in Edge Detection](#12-first-order-vs-second-order-derivatives-in-edge-detection)
   * 1.3 [Gradient Vector, Magnitude, and Direction](#13-gradient-vector-magnitude-and-direction)
   * 1.4 [Noise Sensitivity & Smoothing Trade-offs](#14-noise-sensitivity--smoothing-trade-offs)
2. [Section 2: First-Order Gradient-Based Edge Operators](#section-2-first-order-gradient-based-edge-operators)
   * 2.1 [Prewitt Operator](#21-prewitt-operator)
   * 2.2 [Sobel Operator](#22-sobel-operator)
   * 2.3 [Mask Orientations & Sign Conventions](#23-mask-orientations--sign-conventions)
   * 2.4 [Diagonal & Compass Edge Masks](#24-diagonal--compass-edge-masks)
   * 2.5 [Worked Numerical Example: Prewitt & Sobel Correlation](#25-worked-numerical-example-prewitt--sobel-convolution)
3. [Section 3: Second-Order Edge Operators](#section-3-second-order-edge-operators)
   * 3.1 [The 2D Discrete Laplacian Operator](#31-the-2d-discrete-laplacian-operator)
   * 3.2 [Laplacian Masks & Center-Weight Sign Rules](#32-laplacian-masks--center-weight-sign-rules)
   * 3.3 [Zero-Crossing Detection Mechanism](#33-zero-crossing-detection-mechanism)
   * 3.4 [Worked Numerical Example: 2D Spatial Laplacian](#34-worked-numerical-example-2d-spatial-laplacian)
4. [Section 4: Laplacian of Gaussian (LoG) & Marr-Hildreth Operator](#section-4-laplacian-of-gaussian-log--marr-hildreth-operator)
   * 4.1 [Motivation: Combining Gaussian Smoothing with Laplacian](#41-motivation-combining-gaussian-smoothing-with-laplacian)
   * 4.2 [Mathematical Derivation of the LoG Function](#42-mathematical-derivation-of-the-log-function)
   * 4.3 [Role of Scale Parameter ($\sigma$)](#43-role-of-scale-parameter-sigma)
   * 4.4 [Difference of Gaussians (DoG) Approximation](#44-difference-of-gaussians-dog-approximation)
   * 4.5 [Discrete LoG Kernels & Zero-Crossing Extraction](#45-discrete-log-kernels--zero-crossing-extraction)
5. [Section 5: Canny Edge Detector](#section-5-canny-edge-detector)
   * 5.1 [Canny's Optimal Edge Detection Criteria](#51-cannys-optimal-edge-detection-criteria)
   * 5.2 [Step 1: Noise Reduction via Gaussian Filtering](#52-step-1-noise-reduction-via-gaussian-filtering)
   * 5.3 [Step 2: Gradient Calculation (Sobel Magnitude & Direction)](#53-step-2-gradient-calculation-sobel-magnitude--direction)
   * 5.4 [Step 3: Non-Maximum Suppression (NMS) for Edge Thinning](#54-step-3-non-maximum-suppression-nms-for-edge-thinning)
   * 5.5 [Step 4: Double Thresholding](#55-step-4-double-thresholding)
   * 5.6 [Step 5: Edge Tracking by Hysteresis](#56-step-5-edge-tracking-by-hysteresis)
   * 5.7 [Worked Canny Double-Thresholding and Hysteresis Numerical Example](#57-complete-step-by-step-canny-pipeline-numerical-example)
6. [Section 6: Comprehensive Comparison of Edge Operators](#section-6-comprehensive-comparison-of-edge-operators)
   * 6.1 [Master Operator Comparison Matrix](#61-master-operator-comparison-matrix)
   * 6.2 [Trade-offs: Localization, Noise Robustness, and Complexity](#62-trade-offs-localization-noise-robustness-and-complexity)
7. [Section 7: Formula Master Reference & Quick Revision](#section-7-formula-master-reference--quick-revision)
   * 7.1 [Summary Formula Sheet](#71-summary-formula-sheet)
   * 7.2 [Operator Mask Reference Sheet](#72-operator-mask-reference-sheet)
   * 7.3 [Common Exam Mistakes & Pitfalls](#73-common-exam-mistakes--pitfalls)
   * 7.4 [Unit 5 Complete Coverage Checklist](#74-unit-5-complete-coverage-checklist)

---

<a id="section-1-fundamentals-of-image-edges--derivative-operations"></a>

## Section 1: Fundamentals of Image Edges & Derivative Operations

<a id="11-what-is-an-image-edge-types-of-intensity-profiles"></a>

### 1.1 What is an Image Edge? Types of Intensity Profiles

An **edge** in a digital image is a localized boundary characterized by a significant, abrupt change or discontinuity in pixel intensity. Edges mark physical boundaries such as object contours, surface orientation changes, depth discontinuities, material property changes, or illumination boundaries (shadows).

#### Idealized 1D Intensity Edge Profiles:

```text
 1. Step Edge             2. Ramp Edge             3. Roof Edge (Line)
 Intensity                Intensity                Intensity
    ^                        ^                        ^
 255|      /------        255|        /----       255|    /\
    |     /                  |       /               |   /  \
   0|----/                  0|------/               0|--/    \---
    +----------> x           +----------> x          +----------> x
```

1. **Step Edge:** An ideal transition where pixel intensity jumps instantly from a low value to a high value within a spatial distance of 1 pixel. True step edges rarely occur in real digital images due to optical blurring, lens aberration, and sensor sampling.
2. **Ramp Edge:** A realistic transition where pixel intensity changes gradually over a finite spatial distance (typically 2 to 6 pixels). The slope of the ramp indicates the sharpness of the edge.
3. **Roof / Line Edge:** A profile where pixel intensity increases to a peak and immediately decreases, representing a thin line, wire, or ridge structure in the image.

---

<a id="12-first-order-vs-second-order-derivatives-in-edge-detection"></a>

### 1.2 First-Order vs. Second-Order Derivatives in Edge Detection

Digital images are discrete 2D arrays $f(x,y)$, so derivatives are approximated using **finite differences**.

#### 1D Continuous vs. Discrete Derivative Approximations:

* **First Derivative (Forward Difference):**

```math
\frac{\partial f}{\partial x} = f(x+1) - f(x)
```

* **First Derivative (Central Difference):**

```math
\frac{\partial f}{\partial x} = \frac{f(x+1) - f(x-1)}{2}
```

* **Second Derivative (Central Difference):**

```math
\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)
```

#### Derivative Response Across a Step/Ramp Edge:

For this table only, use backward differences $d_1(x)=f(x)-f(x-1)$ and $d_2(x)=d_1(x)-d_1(x-1)$, with constant extension $f(x)=5$ for $x<0$. The central-difference formulas above are alternative conventions and produce differently indexed responses.

```text
Pixel Position x:     0   1   2   3   4   5   6   7
Intensity f(x):       5   5   5  15  25  35  35  35   (Ramp Edge)

1st Deriv f'(x):      0   0   0  10  10  10   0   0   (Pulse / Ramp Slope)
2nd Deriv f''(x):     0   0   0 +10   0   0 -10   0   (Positive Peak, Negative Trough)
                             +10 at x=3; zeros at x=4,5; -10 at x=6.
The zero-valued plateau lies within the ramp; this example does not define one unique zero-crossing pixel.
```

#### Key Differences between 1st and 2nd Order Derivative Responses:

| Feature / Behavior | First-Order Derivative ($\nabla f$) | Second-Order Derivative ($\nabla^2 f$) |
| :--- | :--- | :--- |
| **Edge Indicator** | Local maximum or peak in gradient magnitude. | **Zero-crossing** (transition from positive peak to negative trough). |
| **Response Width** | Produces a thick, broad response across ramp edges. | Produces a thin double-response (one positive, one negative side). |
| **Sign Information** | Non-negative magnitude ($|G| \ge 0$); direction indicates light-to-dark vs. dark-to-light. | Signed scalar ($+$ on dark side of ramp, $-$ on bright side of ramp). |
| **Line/Point Response** | Can respond to isolated point noise; first derivatives are generally less noise-sensitive than unsmoothed second derivatives. | **Extremely strong response** to isolated point noise and fine detail. |
| **Directionality** | **Directional** (vector with $x$ and $y$ spatial components). | **Continuous Laplacian is isotropic**; sampled 4- and 8-neighbor masks have only approximate rotational symmetry. |

---

<a id="13-gradient-vector-magnitude-and-direction"></a>

### 1.3 Gradient Vector, Magnitude, and Direction

For a continuous 2D image function $f(x,y)$, the **spatial gradient** is a 2D vector $\nabla f$ pointing in the direction of the maximum rate of intensity increase:

```math
\nabla f(x,y) = \begin{bmatrix}
G_x \\
G_y
\end{bmatrix} = \begin{bmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y}
\end{bmatrix}
```

#### 1. Gradient Magnitude ($G$ or $M$):
The magnitude of vector $\nabla f$ measures the rate of intensity change per unit distance:

```math
G[f(x,y)] = |\nabla f| = \sqrt{G_x^2 + G_y^2}
```

In practical hardware and exam numericals, the computationally expensive square root is often approximated using the **absolute sum (Manhattan metric)**:

```math
G_1=|G_x|+|G_y| \quad \quad\text{alternative }L_1\text{ magnitude, with }G_1\ge\sqrt{G_x^2+G_y^2}
```

#### 2. Gradient Direction ($\alpha$ or $\theta$):
The direction angle of the gradient vector relative to the horizontal $x$-axis is best computed with the quadrant-aware two-argument arctangent (undefined when $G_x=G_y=0$):

```math
\theta(x,y) = \operatorname{atan2}(G_y,G_x)
```

> ✍️ **Exam Focus:** The gradient vector $\nabla f$ points **perpendicular to the edge boundary** (in the direction of steepest intensity change). The edge line itself runs **orthogonal (at $90^\circ$)** to the gradient direction $\theta$.

---

<a id="14-noise-sensitivity--smoothing-trade-offs"></a>

### 1.4 Noise Sensitivity & Smoothing Trade-offs

Derivatives act as high-pass spatial filters, amplifying high-frequency noise components present in an image.

```text
Clean Ramp Edge:               Noisy Ramp Edge:
Intensity f(x)                 Intensity f(x)
   /----                          /\/\--/\--
  /                              /  \/  \/
-/                             -/
1st Deriv: Single clean peak.  1st Deriv: Multiple false, noisy peaks!
2nd Deriv: Clear zero-crossing. 2nd Deriv: Massive spurious zero-crossings!
```

* **Core Takeaway:** Direct application of derivative operators to noisy raw images results in severe false edge detections.
* **Solution:** Image pre-smoothing using a **Gaussian low-pass filter** before computing derivatives (as done in LoG and Canny edge detection).

---

<a id="section-2-first-order-gradient-based-edge-operators"></a>

## Section 2: First-Order Gradient-Based Edge Operators

<a id="21-prewitt-operator"></a>

### 2.1 Prewitt Operator

Developed by Judith M. S. Prewitt (1970), the **Prewitt operator** uses $3 \times 3$ derivative masks to approximate horizontal and vertical derivatives while incorporating spatial averaging along the orthogonal direction to reduce noise sensitivity.

#### $3 \times 3$ Prewitt Spatial Kernels:

Horizontal Kernel $G_x$ (Detects Vertical Edges):
```math
G_x = \begin{bmatrix}
-1 & 0 & 1 \\
-1 & 0 & 1 \\
-1 & 0 & 1
\end{bmatrix}
```

Vertical Kernel $G_y$ (Detects Horizontal Edges):
```math
G_y = \begin{bmatrix}
-1 & -1 & -1 \\
0 & 0 & 0 \\
1 & 1 & 1
\end{bmatrix}
```

#### Structural Decomposition:
Notice that $G_x$ and $G_y$ are 1D separable convolution filters:

```math
G_x = \begin{bmatrix}
1 \\
1 \\
1
\end{bmatrix} * \begin{bmatrix}
-1 & 0 & 1
\end{bmatrix}
```

This decomposition shows that Prewitt performs **1D uniform spatial smoothing** across 3 rows combined with a **1D central difference derivative** across columns.

---

<a id="22-sobel-operator"></a>

### 2.2 Sobel Operator

The **Sobel operator** (Sobel & Feldman, 1968) weights the middle row/column of its separable smoothing component by $2$. The derivative-mask coefficient at the center pixel itself is $0$.

#### $3 \times 3$ Sobel Spatial Kernels:

Horizontal Kernel $G_x$ (Detects Vertical Edges):
```math
G_x = \begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
```

Vertical Kernel $G_y$ (Detects Horizontal Edges):
```math
G_y = \begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1
\end{bmatrix}
```

#### Structural Decomposition:
```math
G_x = \begin{bmatrix}
1 \\
2 \\
1
\end{bmatrix} * \begin{bmatrix}
-1 & 0 & 1
\end{bmatrix}
```

* The vector $[1, 2, 1]^T$ is a 1D **triangular / Gaussian approximation mask** providing effective noise smoothing.
* **Advantage over Prewitt:** Weighting the middle row/column by $2$ changes the smoothing response; relative noise behavior and localization depend on the image and mask normalization, rather than being universally superior.

---

<a id="23-mask-orientations--sign-conventions"></a>

### 2.3 Mask Orientations & Sign Conventions

Different textbooks and exam question papers present equivalent gradient masks with inverted signs.

#### Sign Conventions Comparison:

1. **Standard Convention A (Right/Bottom Positive):**
   Horizontal Kernel $G_x$:

```math
G_x = \begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}

```
   Vertical Kernel $G_y$:

```math
G_y = \begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1
\end{bmatrix}

```
   * $G_x > 0$ for transitions from dark (left) to bright (right).
   * $G_y > 0$ for transitions from dark (top) to bright (bottom).

2. **Alternative Convention B (Left/Top Positive):**
   Horizontal Kernel $G_x$:

```math
G_x = \begin{bmatrix}
1 & 0 & -1 \\
2 & 0 & -2 \\
1 & 0 & -1
\end{bmatrix}

```
   Vertical Kernel $G_y$:

```math
G_y = \begin{bmatrix}
1 & 2 & 1 \\
0 & 0 & 0 \\
-1 & -2 & -1
\end{bmatrix}

```

> ⚠️ **Common Mistake:** Inverting all signs in a gradient mask inverts the sign of $G_x$ and $G_y$, but **gradient magnitude $G = \sqrt{G_x^2 + G_y^2}$ remains 100% identical!**

---

<a id="24-diagonal--compass-edge-masks"></a>

### 2.4 Diagonal & Compass Edge Masks (Supporting Material Outside Strict Syllabus)

> These masks and Kirsch are optional context, not additional compulsory topics in the supplied Unit 5 scope.

#### 1. $45^\circ$ and $135^\circ$ Diagonal Sobel Masks:

$+45^\circ$ Diagonal Edge Mask ($G_{+45^\circ}$):
```math
G_{+45^\circ} = \begin{bmatrix}
0 & 1 & 2 \\
-1 & 0 & 1 \\
-2 & -1 & 0
\end{bmatrix}
```

$-45^\circ$ ($135^\circ$) Diagonal Edge Mask ($G_{-45^\circ}$):
```math
G_{-45^\circ} = \begin{bmatrix}
-2 & -1 & 0 \\
-1 & 0 & 1 \\
0 & 1 & 2
\end{bmatrix}
```

#### 2. Kirsch Compass Mask Set (8 Directions):
The Kirsch operator uses 8 directional $3 \times 3$ masks rotated in $45^\circ$ increments ($N, NW, W, SW, S, SE, E, NE$). One common directional edge-strength rule takes the **maximum magnitude of the responses** across the eight oriented masks; specify whether signed or absolute responses are compared:

```math
G(x,y) = \max_{k=0..7} \left\{ |f(x,y) * K_k| \right\}
```

---

<a id="25-worked-numerical-example-prewitt--sobel-convolution"></a>

### 2.5 Worked Numerical Example: Prewitt & Sobel Correlation

#### Problem Statement:
Consider the following $3 \times 3$ image neighborhood $I$:

```math
I = \begin{bmatrix}
10 & 10 & 20 \\
10 & 10 & 20 \\
10 & 10 & 20
\end{bmatrix}
```

Compute the horizontal gradient $G_x$, vertical gradient $G_y$, gradient magnitude $G$, and gradient direction $\theta$ at center pixel $I(2,2) = 10$ using both **Prewitt** and **Sobel** operators. **Convention:** Apply the masks as printed by elementwise multiplication and summation (cross-correlation, without a 180-degree kernel flip). True convolution with these antisymmetric derivative masks reverses the signs of $G_x$ and $G_y$ but preserves the magnitude.

---

#### 1. Prewitt Operator Calculations:

* **Horizontal Gradient $G_x$:**

```math
G_x = (-1)(10) + (0)(10) + (1)(20) + (-1)(10) + (0)(10) + (1)(20) + (-1)(10) + (0)(10) + (1)(20)
```


```math
G_x = -10 + 20 - 10 + 20 - 10 + 20 = 30
```

* **Vertical Gradient $G_y$:**

```math
G_y = (-1)(10) + (-1)(10) + (-1)(20) + (0)(10) + (0)(10) + (0)(20) + (1)(10) + (1)(10) + (1)(20)
```


```math
G_y = -10 - 10 - 20 + 0 + 10 + 10 + 20 = 0
```

* **Gradient Magnitude $G$:**

```math
G = \sqrt{G_x^2 + G_y^2} = \sqrt{30^2 + 0^2} = 30
```

* **Gradient Direction $\theta$:**

```math
\theta = \tan^{-1}\left(\frac{G_y}{G_x}\right) = \tan^{-1}\left(\frac{0}{30}\right) = 0^\circ \quad \text{(Horizontal Gradient, Vertical Edge!)}
```

---

#### 2. Sobel Operator Calculations:

* **Horizontal Gradient $G_x$:**

```math
G_x = (-1)(10) + (0)(10) + (1)(20) + (-2)(10) + (0)(10) + (2)(20) + (-1)(10) + (0)(10) + (1)(20)
```


```math
G_x = -10 + 20 - 20 + 40 - 10 + 20 = 40
```

* **Vertical Gradient $G_y$:**

```math
G_y = (-1)(10) + (-2)(10) + (-1)(20) + (0)(10) + (0)(10) + (0)(20) + (1)(10) + (2)(10) + (1)(20)
```


```math
G_y = -10 - 20 - 20 + 0 + 10 + 20 + 20 = 0
```

* **Gradient Magnitude $G$:**

```math
G = \sqrt{40^2 + 0^2} = 40
```

* **Gradient Direction $\theta$:**

```math
\theta = \tan^{-1}\left(\frac{0}{40}\right) = 0^\circ
```

---

<a id="section-3-second-order-edge-operators"></a>

## Section 3: Second-Order Edge Operators

<a id="31-the-2d-discrete-laplacian-operator"></a>

### 3.1 The 2D Discrete Laplacian Operator

The **continuous Laplacian** is a 2D second-order isotropic (rotationally invariant) continuous differential operator; its displayed discrete masks are only approximately rotation-invariant:

```math
\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}
```

#### Derivation using 2D Central Differences:

```math
\frac{\partial^2 f}{\partial x^2} = f(x+1, y) + f(x-1, y) - 2f(x,y)
```


```math
\frac{\partial^2 f}{\partial y^2} = f(x, y+1) + f(x, y-1) - 2f(x,y)
```

Combining both partial second derivatives yields the **4-Neighbor Discrete Laplacian**:

```math
\nabla^2 f(x,y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4f(x,y)
```

---

<a id="32-laplacian-masks--center-weight-sign-rules"></a>

### 3.2 Laplacian Masks & Center-Weight Sign Rules

#### Standard 2D Laplacian Spatial Masks:

1. **4-Neighbor Mask (Negative Center Weight):**

```math
L_4 = \begin{bmatrix}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0
\end{bmatrix}

```

2. **8-Neighbor Mask (Negative Center Weight, Incorporating Diagonals):**

```math
L_8 = \begin{bmatrix}
1 & 1 & 1 \\
1 & -8 & 1 \\
1 & 1 & 1
\end{bmatrix}

```

3. **Inverted Center Sign Masks (Positive Center Weight):**
   4-Neighbor Positive Center Mask $L_4^+$:

```math
L_4^+ = \begin{bmatrix}
0 & -1 & 0 \\
-1 & 4 & -1 \\
0 & -1 & 0
\end{bmatrix}

```
   8-Neighbor Positive Center Mask $L_8^+$:

```math
L_8^+ = \begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1
\end{bmatrix}

```

> ⭐ **Must Remember for Image Sharpening vs. Edge Detection:**
> * If using the **negative-center mask** $L$, a common sharpening convention is $g=f-L*f$; replacing $L$ by $-L$ requires changing subtraction to addition.
> * If using the **positive-center mask** $L^+=-L$ for sharpening, add its response: $g=f+L^+*f$; equivalently, for the negative-center Laplacian $L$, use $g=f-L*f$. The sign must be tied to the chosen mask, not inferred from the word "Laplacian" alone.

---

<a id="33-zero-crossing-detection-mechanism"></a>

### 3.3 Zero-Crossing Detection Mechanism

With the negative-center Laplacian convention for a dark-to-bright ramp, the second derivative can have a positive response before the transition and a negative response after it. An edge candidate is found at a **zero crossing or sign change**; sampling and smoothing determine its estimated location, which is not necessarily exact.

```text
Intensity Profile:   [ 10   10   10   50   50   50 ]
Laplacian Response:  [  0    0  +40  -40    0    0 ]
                                 ^----^ Zero-Crossing! Edge is located between x=2 and x=3!
```

#### How Zero-Crossings are Computed in a $3 \times 3$ Neighborhood:
A pixel $P(x,y)$ in a Laplacian-filtered image is declared a **Zero-Crossing Edge Pixel** if:
1. The sign of $P(x,y)$ differs from at least one of its 8 neighbors across 4 oppositional axes:
   * Left vs. Right
   * Top vs. Bottom
   * Top-Left vs. Bottom-Right
   * Top-Right vs. Bottom-Left
2. The absolute difference between the opposing pixel values exceeds a specified noise threshold $T_{zc}$.

---

<a id="34-worked-numerical-example-2d-spatial-laplacian"></a>

### 3.4 Worked Numerical Example: 2D Spatial Laplacian

#### Problem Statement:
Apply the 8-neighbor Laplacian mask $L_8$ (negative center weight $-8$) to the center pixel $I(2,2) = 50$ of the following image patch:

```math
I = \begin{bmatrix}
10 & 10 & 10 \\
10 & 50 & 50 \\
50 & 50 & 50
\end{bmatrix}
```

#### Step-by-Step Solution:
```math
L_8 = \begin{bmatrix}
1 & 1 & 1 \\
1 & -8 & 1 \\
1 & 1 & 1
\end{bmatrix}
```

```math
\nabla^2 I(2,2) = \sum_{s=-1}^1 \sum_{t=-1}^1 w(s,t) I(2+s, 2+t)
```


```math
\nabla^2 I(2,2) = (1)(10) + (1)(10) + (1)(10) + (1)(10) + (-8)(50) + (1)(50) + (1)(50) + (1)(50) + (1)(50)
```


```math
\nabla^2 I(2,2) = 10 + 10 + 10 + 10 - 400 + 50 + 50 + 50 + 50
```


```math
\nabla^2 I(2,2) = 240 - 400 = -160
```

Since the response is non-zero ($-160$), this indicates a strong second-order intensity transition near the boundary of the bright region ($50$).

---

<a id="section-4-laplacian-of-gaussian-log--marr-hildreth-operator"></a>

## Section 4: Laplacian of Gaussian (LoG) & Marr-Hildreth Operator

<a id="41-motivation-combining-gaussian-smoothing-with-laplacian"></a>

### 4.1 Motivation: Combining Gaussian Smoothing with Laplacian

The unsmoothed Laplacian operator is unacceptably sensitive to image noise. To overcome this limitation, David Marr and Ellen Hildreth (1980) proposed pre-smoothing the image with a 2D Gaussian filter before applying the Laplacian.

By the **associative property of linear spatial convolution**:

```math
\nabla^2 [G_\sigma(x,y) * f(x,y)] = [\nabla^2 G_\sigma(x,y)] * f(x,y)
```

This fundamental identity allows us to pre-calculate a single composite filter kernel—the **Laplacian of Gaussian (LoG)** kernel—and convolve it directly with the input image in one single filtering pass!

---

<a id="42-mathematical-derivation-of-the-log-function"></a>

### 4.2 Mathematical Derivation of the LoG Function

The 2D rotationally symmetric Gaussian smoothing function with standard deviation $\sigma$ is:

```math
G_\sigma(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
```

Let $r^2 = x^2 + y^2$. Then $G_\sigma(r) = \frac{1}{2\pi\sigma^2} e^{-\frac{r^2}{2\sigma^2}}$.

Applying the Laplacian operator $\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ to $G_\sigma(x,y)$:

```math
\frac{\partial G_\sigma}{\partial x} = -\frac{x}{2\pi\sigma^4} e^{-\frac{x^2+y^2}{2\sigma^2}}
```

```math
\frac{\partial^2 G_\sigma}{\partial x^2} = \left( \frac{x^2}{\sigma^2} - 1 \right) \frac{1}{2\pi\sigma^4} e^{-\frac{x^2+y^2}{2\sigma^2}}
```

Similarly for $y$:

```math
\frac{\partial^2 G_\sigma}{\partial y^2} = \left( \frac{y^2}{\sigma^2} - 1 \right) \frac{1}{2\pi\sigma^4} e^{-\frac{x^2+y^2}{2\sigma^2}}
```

Summing both partial second derivatives yields the **2D LoG Expression**:

```math
\text{LoG}(x,y) = \nabla^2 G_\sigma(x,y) = \left[ \frac{x^2 + y^2 - 2\sigma^2}{\sigma^4} \right] \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}
```

#### The Mexican Hat Profile:
The formula for $\nabla^2G_\sigma$ above has a **negative center and positive surround**. The sketch below depicts its sign-reversed form $-\nabla^2G_\sigma$ (a positive central lobe), also called a Mexican-hat profile. Both signs have the same zero-crossing locations.

```text
Sign-reversed LoG cross-section: -LoG (schematic, not to scale):
          Intensity
             ^
             |       /\       <- Positive Central Lobe
             |      /  \
      -------+-----/----\----- Zero-Crossings at r = +/- (sqrt(2) * sigma)
            / \   /      \   /
           /   \_/        \_/ <- Negative Outer Trench
          +--------------------> Spatial Coordinate r
```

---

<a id="43-role-of-scale-parameter-sigma"></a>

### 4.3 Role of Scale Parameter ($\sigma$)

* **Zero-Crossing Distance:** The zero-crossings of $\nabla^2 G_\sigma$ occur at spatial radius $r = \sqrt{x^2+y^2} = \sqrt{2}\sigma$.
* **Small $\sigma$ (e.g., $\sigma = 1.0$):** Narrow kernel; detects fine, detailed edges but remains slightly more sensitive to small noise structures.
* **Large $\sigma$ (e.g., $\sigma = 3.0$):** Broad kernel; blurs fine details and detects only prominent, large-scale structural edges.
* **Kernel Diameter Support:** Choose a sufficiently wide, usually odd-sized support for the Gaussian/LoG at the selected $\sigma$ (often about $6\sigma$ across); there is no universal mandatory minimum, and truncation error depends on the chosen tolerance.

---

<a id="44-difference-of-gaussians-dog-approximation"></a>

### 4.4 Difference of Gaussians (DoG) Approximation (Supporting Material Outside Strict Syllabus)

> DoG is included only to explain a related approximation to LoG; it is not a separately listed Unit 5 operator.

Computing the exact LoG function can be computationally demanding. At suitable scale ratios, the LoG operator can be approximated by calculating the **Difference of Two Gaussians (DoG)** with different standard deviations $\sigma_1$ and $\sigma_2$:

```math
\text{DoG}(x,y) = \frac{1}{2\pi\sigma_1^2} e^{-\frac{x^2+y^2}{2\sigma_1^2}} - \frac{1}{2\pi\sigma_2^2} e^{-\frac{x^2+y^2}{2\sigma_2^2}}
```

A scale ratio of approximately **$\sigma_1 : \sigma_2 = 1 : 1.6$** is one commonly used DoG approximation to a scale-normalized LoG; its suitability depends on the scale and application and is not universally optimal.

---

<a id="45-discrete-log-kernels--zero-crossing-extraction"></a>

### 4.5 Discrete LoG Kernels & Zero-Crossing Extraction

A popular discrete $5 \times 5$ integer approximation of the negative LoG operator is:

```math
\text{LoG}_{5 \times 5} = \begin{bmatrix}
0 & 0 & -1 & 0 & 0 \\
0 & -1 & -2 & -1 & 0 \\
-1 & -2 & 16 & -2 & -1 \\
0 & -1 & -2 & -1 & 0 \\
0 & 0 & -1 & 0 & 0
\end{bmatrix}
```

#### Properties of Discrete LoG Kernels:
1. **Sum of Coefficients Equals Zero:** $\sum_{i,j} \text{LoG}(i,j) = 0$. This ensures that flat constant-intensity regions produce a response of exactly zero.
2. **Discrete symmetry:** The continuous LoG is radially symmetric; this sampled integer mask has discrete 90-degree/reflection symmetry, not exact continuous circular symmetry.

---

<a id="section-5-canny-edge-detector"></a>

## Section 5: Canny Edge Detector

<a id="51-cannys-optimal-edge-detection-criteria"></a>

### 5.1 Canny's Optimal Edge Detection Criteria

In 1986, John F. Canny formulated edge detection as an optimal statistical estimation problem based on three performance criteria:

1. **Low Error Rate (Good Detection):** The algorithm must mark as many real edges as possible while minimizing false edge detections caused by noise.
2. **Good Localization:** The distance between detected edge pixels and actual physical edge centers must be minimized.
3. **Single Response Criterion:** The design aims for one response per physical edge; discrete images, noise, and parameter choices can still produce multiple or interrupted responses.

---

<a id="52-step-1-noise-reduction-via-gaussian-filtering"></a>

### 5.2 Step 1: Noise Reduction via Gaussian Filtering

To reduce high-frequency noise while retaining useful edge transitions, the raw input image $I(x,y)$ is convolved with a 2D Gaussian filter kernel $G_\sigma(x,y)$:

```math
I_s(x,y) = I(x,y) * G_\sigma(x,y)
```

A standard $3 \times 3$ discrete Gaussian smoothing kernel ($\sigma \approx 1.0$) is:

```math
G = \frac{1}{16} \begin{bmatrix}
1 & 2 & 1 \\
2 & 4 & 2 \\
1 & 2 & 1
\end{bmatrix}
```

---

<a id="53-step-2-gradient-calculation-sobel-magnitude--direction"></a>

### 5.3 Step 2: Gradient Calculation (Sobel Magnitude & Direction)

First-order derivatives $G_x$ and $G_y$ can be computed by correlating the smoothed image $I_s(x,y)$ with the displayed Sobel masks. An implementation using mathematical convolution flips each mask and reverses the derivative signs:

```math
S_x = \begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}, \quad S_y = \begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1
\end{bmatrix}
```

#### Gradient Magnitude & Angle Calculations:

```math
M(x,y) = \sqrt{G_x^2 + G_y^2}
```


```math
\theta(x,y) = \operatorname{atan2}(G_y,G_x)
```

#### Quantization of Gradient Angles into 4 Sectors:
To perform non-maximum suppression across a discrete $3 \times 3$ pixel grid, continuous angle $\theta(x,y)$ is rounded to the nearest of four sector directions. For the NMS neighbor pairs below, $(x,y)$ denotes (row, column), with rows increasing downward and columns increasing rightward; $G_x$ is the horizontal/column response and $G_y$ the vertical/row response. Thus a positive $45^\circ$ gradient follows the top-left to bottom-right diagonal:

```text
Sector 0  (0° / 180°):   Horizontal direction  [-22.5° to +22.5°] & [157.5° to 180° / -157.5°]
Sector 1  (45° / 225°):  Positive Diagonal     [+22.5° to +67.5°]
Sector 2  (90° / 270°):  Vertical direction    [+67.5° to +112.5°]
Sector 3  (135° / 315°): Negative Diagonal     [+112.5° to +157.5°]
```

```text
Discrete Sector Neighbor Map:
      q1 (45°)    q2 (90°)   q3 (135°)
             \       |       /
              \      |      /
      q0 (0°) --- P(x,y) --- q0 (0°)
              /      |      \
             /       |       \
      q3 (135°)   q2 (90°)   q1 (45°)
```

---

<a id="54-step-3-non-maximum-suppression-nms-for-edge-thinning"></a>

### 5.4 Step 3: Non-Maximum Suppression (NMS) for Edge Thinning

Gradient magnitude images derived from Sobel operators display broad, thick ridge responses across ramp edges. **Non-Maximum Suppression (NMS)** aims to thin broad gradient ridges to approximately one-pixel-wide responses on a discrete grid; ties and sampling can affect the result.

#### Algorithm for NMS at Pixel $P(x,y)$:
1. Identify the quantized gradient direction sector $S_\theta$ of pixel $P(x,y)$.
2. Identify the two immediate neighbors $N_1$ and $N_2$ along direction $S_\theta$:
   * If $\theta \in \text{Sector } 0^\circ$: Compare $P(x,y)$ with Left $(x, y-1)$ and Right $(x, y+1)$ pixels.
   * If $\theta \in \text{Sector } 45^\circ$: Compare $P(x,y)$ with Top-Left $(x-1, y-1)$ and Bottom-Right $(x+1, y+1)$ pixels (image coordinates, downward-positive rows).
   * If $\theta \in \text{Sector } 90^\circ$: Compare $P(x,y)$ with Top $(x-1, y)$ and Bottom $(x+1, y)$ pixels.
   * If $\theta \in \text{Sector } 135^\circ$: Compare $P(x,y)$ with Top-Right $(x-1, y+1)$ and Bottom-Left $(x+1, y-1)$ pixels (image coordinates, downward-positive rows).
3. **Suppression Condition:**
   * If $M(P) \ge M(N_1)$ AND $M(P) \ge M(N_2)$, preserve $M(P)$ in $NMS(x,y)$.
   * Otherwise, set $NMS(x,y) = 0$ (suppress non-maximum pixel).

---

<a id="55-step-4-double-thresholding"></a>

### 5.5 Step 4: Double Thresholding

To eliminate spurious edge responses caused by noise or color variations while preserving true weak edge segments, Canny applies **Double Thresholding** using two preset thresholds: High Threshold $T_{\text{high}}$ and Low Threshold $T_{\text{low}}$ (typically $T_{\text{high}} : T_{\text{low}} = 2:1$ or $3:1$).

Pixel intensities in the thinned $NMS(x,y)$ map are classified into three distinct categories:

```math
\text{EdgeClass}(x,y) = \begin{cases} \mathbf{\text{Strong Edge}} & \text{if } NMS(x,y) \ge T_{\text{high}} \\ \mathbf{\text{Weak Edge}} & \text{if } T_{\text{low}} \le NMS(x,y) < T_{\text{high}} \\ \mathbf{\text{Rejected (Non-Edge)}} & \text{if } NMS(x,y) < T_{\text{low}} \end{cases}
```

```text
Threshold Classification Map:
Gradient Magnitude
  ^
  |   Strong Edges (Accepted Immediately)
--+------------------------------------- T_high
  |   Weak Edges (Candidate Pool)
--+------------------------------------- T_low
  |   Rejected Pixels (Discarded = 0)
  +-------------------------------------> Spatial Coordinates
```

---

<a id="56-step-5-edge-tracking-by-hysteresis"></a>

### 5.6 Step 5: Edge Tracking by Hysteresis

Isolated weak edge pixels are usually produced by noise, whereas valid weak edge pixels connected to strong edge pixels form continuous physical boundaries.

#### Hysteresis Algorithm Rules:
1. All **Strong Edge** pixels are unconditionally accepted as final edge pixels ($g(x,y) = 1$).
2. A **Weak Edge** pixel is accepted ($g(x,y) = 1$) **IF AND ONLY IF** it is 8-connected to at least one Strong Edge pixel (either directly or recursively through a chain of connected weak pixels).
3. All remaining isolated **Weak Edge** pixels disconnected from any strong edge chain are set to zero ($g(x,y) = 0$).

---

<a id="57-complete-step-by-step-canny-pipeline-numerical-example"></a>

### 5.7 Worked Canny Double-Thresholding and Hysteresis Numerical Example

#### Problem Statement:
Consider the following $5 \times 5$ thinned gradient magnitude matrix $NMS$ **provided after** Non-Maximum Suppression. The Gaussian, gradient, and NMS stages are explained above but are not numerically calculated in this example:

```math
NMS = \begin{bmatrix}
10 & 15 & 10 & 0 & 0 \\
12 & \mathbf{55} & 25 & 10 & 0 \\
0 & 20 & \mathbf{45} & 15 & 0 \\
0 & 0 & 30 & \mathbf{60} & 10 \\
0 & 0 & 10 & 15 & 10
\end{bmatrix}
```

Given thresholds **$T_{\text{high}} = 50$** and **$T_{\text{low}} = 20$**, perform Double Thresholding and Edge Tracking by Hysteresis to generate the final binary Canny edge map $E(x,y)$.

---

#### Step 1: Double Thresholding Classification ($T_H = 50, T_L = 20$)

Classify every pixel in $NMS$:
* $NMS \ge 50 \implies \mathbf{\text{Strong Edge (S = 1)}}$
* $20 \le NMS < 50 \implies \mathbf{\text{Weak Edge (W)}}$
* $NMS < 20 \implies \mathbf{\text{Rejected (0)}}$

Classification Map:
```math
\text{ClassMap} = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & \mathbf{S} & W(25) & 0 & 0 \\
0 & W(20) & W(45) & 0 & 0 \\
0 & 0 & W(30) & \mathbf{S} & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

* **Strong Edge Locations ($S$):** Pixel $(2,2) = 55$ and Pixel $(4,4) = 60$.
* **Weak Edge Locations ($W$):**
  * $(2,3) = 25$
  * $(3,2) = 20$
  * $(3,3) = 45$
  * $(4,3) = 30$

---

#### Step 2: Edge Tracking by Hysteresis (8-Connectivity)

1. **Start at Strong Edge Pixel $S_1 = (2,2)$ ($NMS = 55$):**
   * Check 8-neighbors of $(2,2)$:
     * Neighbor $(2,3) = 25 \implies$ **Connected Weak Edge!** Promoted to Valid Edge ($1$).
     * Neighbor $(3,2) = 20 \implies$ **Connected Weak Edge!** Promoted to Valid Edge ($1$).
     * Neighbor $(3,3) = 45 \implies$ **Connected Weak Edge!** Promoted to Valid Edge ($1$).

2. **Propagate from newly promoted Weak Edge Pixel $(3,3)$ ($NMS = 45$):**
   * Check 8-neighbors of $(3,3)$:
     * Neighbor $(4,3) = 30 \implies$ **Connected Weak Edge!** Promoted to Valid Edge ($1$).
     * Neighbor $(4,4) = 60 \implies$ **Connected to Strong Edge $S_2$!**

3. **Verify Strong Edge Pixel $S_2 = (4,4)$ ($NMS = 60$):**
   * Unconditionally accepted as Valid Edge ($1$).

#### Final Binary Canny Edge Map $E(x,y)$:

```math
E(x,y) = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & \mathbf{1} & \mathbf{1} & 0 & 0 \\
0 & \mathbf{1} & \mathbf{1} & 0 & 0 \\
0 & 0 & \mathbf{1} & \mathbf{1} & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

All 4 weak edge pixels were successfully preserved because they formed an unbroken 8-connected path connecting Strong Edge $(2,2)$ to Strong Edge $(4,4)$!

---

<a id="section-6-comprehensive-comparison-of-edge-operators"></a>

## Section 6: Comprehensive Comparison of Edge Operators

<a id="61-master-operator-comparison-matrix"></a>

### 6.1 Master Operator Comparison Matrix

| Edge Operator | Derivative Order | Mask Sizes / Support | Noise Sensitivity | Edge Localization | Edge Thickness | Computational Complexity | Primary Application / Best Use |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Prewitt** | 1st Order | $3 \times 3$ | Moderate (1D Box Smoothing) | Fair | Thick (Requires Thresholding) | Low per pixel ($O(N^2)$ for an $N\times N$ image) | Real-time simple edge detection |
| **Sobel** | 1st Order | $3 \times 3$ | Often moderate (triangular smoothing) | Good | Thick (Requires Thresholding) | Low per pixel ($O(N^2)$ for an $N\times N$ image) | General-purpose fast edge detection |
| **Laplacian** | 2nd Order | $3 \times 3$ | High without presmoothing | Noise-sensitive without smoothing | Double-Line Profile | Low per pixel | Unsharp masking, zero-crossing checks |
| **LoG (Marr-Hildreth)** | 2nd Order | $5 \times 5$ to $9 \times 9+$ | Scale-dependent after Gaussian smoothing | Scale-dependent zero-crossing localization | Zero-crossing contours; continuity and thickness depend on extraction | Moderate | Scale-space edge detection, biological vision |
| **Canny** | 1st Order + NMS + Hysteresis | Multi-stage ($5 \times 5$ Gaussian + $3 \times 3$ Sobel) | Often robust after smoothing; depends on noise and thresholds | Often good; pixel-grid NMS does not by itself guarantee subpixel localization | Typically thin pixel-grid edges after NMS; not guaranteed | High (Multi-pass Pipeline) | Industrial machine vision, precise contouring |

---

<a id="62-trade-offs-localization-noise-robustness-and-complexity"></a>

### 6.2 Trade-offs: Localization, Noise Robustness, and Complexity

1. **First-Order vs. Second-Order Trade-off:**
   * First-order operators (Sobel/Prewitt) are simple and fast but produce thick edges requiring manual thresholding.
   * Second-order operators detect zero-crossings after smoothing in LoG; an unsmoothed Laplacian is noise-sensitive and may generate spurious responses.

2. **Smoothing vs. Localization Trade-off (Scale-Space):**
   * Increasing Gaussian width $\sigma$ generally suppresses more noise but may blur nearby details and reduce localization; edge shifts are possible but not inevitable.

3. **Canny's design trade-offs:**
   * Canny combines gradient thinning (NMS) with two thresholds and hysteresis to improve continuity and suppress some noise responses; output still depends on smoothing scale, thresholds, and implementation.

---

<a id="section-7-formula-master-reference--quick-revision"></a>

## Section 7: Formula Master Reference & Quick Revision

<a id="71-summary-formula-sheet"></a>

### 7.1 Summary Formula Sheet

Gradient Vector:
```math
\nabla f = \begin{bmatrix}
G_x \\
G_y
\end{bmatrix} = \begin{bmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y}
\end{bmatrix}
```

```math
\text{Gradient Magnitude:} \quad G_2 = \sqrt{G_x^2 + G_y^2}, \qquad G_1=|G_x|+|G_y| \text{ is an alternative measure with }G_1\ge G_2
```

```math
\text{Gradient Orientation:} \quad \theta = \operatorname{atan2}(G_y,G_x) \quad ((G_x,G_y)\ne(0,0))
```

```math
\text{2D Continuous Laplacian:} \quad \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}
```

```math
\text{4-Neighbor Discrete Laplacian:} \quad \nabla^2 f(x,y) = f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1) - 4f(x,y)
```

```math
\text{2D Gaussian Smoothing Function:} \quad G_\sigma(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}
```

```math
\text{Laplacian of Gaussian (LoG):} \quad \text{LoG}(x,y) = \left[ \frac{x^2+y^2-2\sigma^2}{\sigma^4} \right] \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}
```

```math
\text{Difference of Gaussians (DoG):} \quad \text{DoG}(x,y) = G_{\sigma_1}(x,y) - G_{\sigma_2}(x,y) \quad (\sigma_1 : \sigma_2 = 1 : 1.6)
```

```math
\text{Canny Double Threshold Classification:} \quad \text{Pixel } P \in \begin{cases} \text{Strong} & \text{if } P \ge T_H \\ \text{Weak} & \text{if } T_L \le P < T_H \\ \text{Rejected} & \text{if } P < T_L \end{cases}
```

---

<a id="72-operator-mask-reference-sheet"></a>

### 7.2 Operator Mask Reference Sheet

#### 1. Prewitt Masks ($3 \times 3$):
Horizontal Kernel $G_x$:
```math
G_x = \begin{bmatrix}
-1 & 0 & 1 \\
-1 & 0 & 1 \\
-1 & 0 & 1
\end{bmatrix}
```
Vertical Kernel $G_y$:
```math
G_y = \begin{bmatrix}
-1 & -1 & -1 \\
0 & 0 & 0 \\
1 & 1 & 1
\end{bmatrix}
```

#### 2. Sobel Masks ($3 \times 3$):
Horizontal Kernel $G_x$:
```math
G_x = \begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
```
Vertical Kernel $G_y$:
```math
G_y = \begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1
\end{bmatrix}
```

#### 3. Laplacian Masks ($3 \times 3$):
4-Neighbor Mask $L_4$:
```math
L_4 = \begin{bmatrix}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0
\end{bmatrix}
```
8-Neighbor Mask $L_8$:
```math
L_8 = \begin{bmatrix}
1 & 1 & 1 \\
1 & -8 & 1 \\
1 & 1 & 1
\end{bmatrix}
```

#### 4. Discrete LoG Mask ($5 \times 5$):
```math
\text{LoG}_{5 \times 5} = \begin{bmatrix}
0 & 0 & -1 & 0 & 0 \\
0 & -1 & -2 & -1 & 0 \\
-1 & -2 & 16 & -2 & -1 \\
0 & -1 & -2 & -1 & 0 \\
0 & 0 & -1 & 0 & 0
\end{bmatrix}
```

---

<a id="73-common-exam-mistakes--pitfalls"></a>

### 7.3 Common Exam Mistakes & Pitfalls

1. ❌ **Confusing Gradient Direction with Edge Line Direction:**
   * The gradient vector $\nabla f$ points **perpendicular** to the edge. The physical edge line runs at $\theta + 90^\circ$.
2. ❌ **Forgetting Non-Maximum Suppression Sector Matching:**
   * NMS compares gradient magnitude strictly along the gradient vector direction, NOT along the edge line!
3. ❌ **Assuming Weak Edge Pixels are Always Rejected:**
   * Weak edge pixels connected to strong edge pixels via an 8-connected chain are **preserved** in Canny edge detection!
4. ❌ **Inverting Laplacian Sharpening Signs:**
   * Negative center weight ($-4$ or $-8$) requires **subtraction**: $g = f - \nabla^2 f$.

---

<a id="74-unit-5-complete-coverage-checklist"></a>

### 7.4 Unit 5 Complete Coverage Checklist

* [x] Definition of image edges and intensity profiles (Step, Ramp, Roof)
* [x] First-order vs. Second-order derivative responses across edges
* [x] Gradient vector, magnitude, and direction mathematical formulations
* [x] Prewitt operator masks, decomposition, and worked numerical example
* [x] Sobel operator masks, decomposition, and worked numerical example
* [x] 2D Laplacian operator derivation, 4-neighbor and 8-neighbor masks
* [x] Zero-crossing detection principles and sign rules
* [x] LoG (Marr-Hildreth) mathematical derivation, scale parameter $\sigma$, and DoG approximation
* [x] Canny edge detector: 5-step pipeline (Gaussian smoothing, Sobel gradients, NMS, Double thresholding, Hysteresis)
* [x] Worked Canny double-thresholding and hysteresis numerical problem using an already NMS-processed input; NMS is explained separately
* [x] Operator comparison matrix covering complexity, noise sensitivity, and localization
* [x] Formula sheet, operator mask reference, and exam pitfalls checklist

---
