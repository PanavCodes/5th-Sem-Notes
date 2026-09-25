# IVP Unit 2: Image Enhancement (M2 Exam Notes)

---

## 📌 Document Metadata & Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 2 — Image Enhancement (M2 Specific Exam Scope)
* **Target Assessment:** M2 Exam / Class Test / Mid-Term Review
* **Format:** GitHub Flavored Markdown (GFM) with LaTeX Math
* **Scope Boundary Notice:** This document is strictly tailored to the **M2 Examination Scope** for Unit 2. In strict accordance with M2 syllabus directives, this document focuses exclusively on **Frequency-Domain Filtering** (Low-Pass, High-Pass, Fourier Spectrum, Filter Responses, Ringing Artifacts) and **Spatial Sharpening** (Neighborhood Processing, First & Second Derivatives, Laplacian Masks, Unsharp Masking, High-Boost Filtering). Standalone spatial smoothing filters, point processing (digital negatives, contrast stretching, thresholding, intensity slicing, log/gamma transforms), and histogram equalization are excluded from this M2 summary notes file.

---

## 📑 Table of Contents

1. [Unit Overview & Core Concepts](#1-unit-overview--core-concepts)
2. [Section 1: Frequency-Domain Filtering](#2-section-1-frequency-domain-filtering)
   * 2.1 [Image Frequency Domain & Fourier Spectrum Fundamentals](#21-image-frequency-domain--fourier-spectrum-fundamentals)
   * 2.2 [The Frequency-Domain Filtering Pipeline](#22-the-frequency-domain-filtering-pipeline)
   * 2.3 [Frequency-Domain Low-Pass Filters (ILPF, BLPF, GLPF)](#23-frequency-domain-low-pass-filters-ilpf-blpf-glpf)
   * 2.4 [Frequency-Domain High-Pass Filters (IHPF, BHPF, GHPF)](#24-frequency-domain-high-pass-filters-ihpf-bhpf-ghpf)
   * 2.5 [Comparative Analysis & Ringing Artifacts](#25-comparative-analysis--ringing-artifacts)
3. [Section 2: Spatial Filtering & Image Sharpening](#3-section-2-spatial-filtering--image-sharpening)
   * 3.1 [Neighborhood Processing & Filter Masks](#31-neighborhood-processing--filter-masks)
   * 3.2 [First and Second Derivative Properties in Image Sharpening](#32-first-and-second-derivative-properties-in-image-sharpening)
   * 3.3 [Laplacian-Based Sharpening & Sign Conventions](#33-laplacian-based-sharpening--sign-conventions)
   * 3.4 [Unsharp Masking & High-Boost Filtering](#34-unsharp-masking--high-boost-filtering)
   * 3.5 [Comparative Analysis: High-Pass vs. Laplacian vs. High-Boost](#35-comparative-analysis-high-pass-vs-laplacian-vs-high-boost)
4. [Section 3: Formula & Filter-Mask Master Reference](#4-section-3-formula--filter-mask-master-reference)
5. [Section 4: Step-by-Step Computational Procedures](#5-section-4-step-by-step-computational-procedures)
6. [Section 5: Solved Worked Numerical Problems](#6-section-5-solved-worked-numerical-problems)
   * [Problem 1: Step-by-Step Frequency-Domain Filtering ($4 \times 4$ Matrix, $D_0 = 0.5$)](#problem-1-step-by-step-frequency-domain-filtering-4-times-4-matrix-d_0--05)
   * [Problem 2: 1D Scanline First and Second Derivative Calculation](#problem-2-1d-scanline-first-and-second-derivative-calculation)
   * [Problem 3: 2D Spatial Laplacian Convolution on $6 \times 6$ Step Edge Image](#problem-3-2d-spatial-laplacian-convolution-on-6-times-6-step-edge-image)
   * [Problem 4: High-Boost Spatial Filter Mask Construction & Application](#problem-4-high-boost-spatial-filter-mask-construction--application)
   * [Problem 5: Frequency-Domain High-Boost Transfer Function Derivation](#problem-5-frequency-domain-high-boost-transfer-function-derivation)
7. [Section 6: Quick Revision & Exam Essentials](#7-section-6-quick-revision--exam-essentials)
   * [Quick Revision Summary](#quick-revision-summary)
   * [Important Definitions](#important-definitions)
   * [Frequency-Filtering Steps Summary](#frequency-filtering-steps-summary)
   * [Spatial-Sharpening Steps Summary](#spatial-sharpening-steps-summary)
   * [Formula and Mask List](#formula-and-mask-list)
   * [Common Mistakes (⚠️)](#%EF%B8%8F-common-mistakes)
   * [Last-Minute Checklist (✍️)](#%E2%9C%8D%EF%B8%8F-last-minute-checklist)
   * [Complete M2 Unit 2 Coverage Checklist](#complete-m2-unit-2-coverage-checklist)

---

## 1. Unit Overview & Core Concepts

Image enhancement transforms an input image $f(x,y)$ into a processed image $g(x,y)$ that is visually or computationally more suitable for a specific application. In M2 Unit 2, enhancement is categorized into two fundamental operational domains:

1. **Frequency Domain Filtering:** Operations performed on the Discrete Fourier Transform (DFT) coefficients of an image, where filtering attenuates or emphasizes specific spatial frequencies.
2. **Spatial Sharpening:** Direct manipulation of pixel values using local neighborhood convolution masks derived from discrete differential operators (first and second derivatives).

```text
+-----------------------------------------------------------------------------------+
|                            M2 UNIT 2 ENHANCEMENT SCOPE                            |
+---------------------------------------------------+-------------------------------+
|             FREQUENCY DOMAIN FILTERING            |       SPATIAL SHARPENING      |
+---------------------------------------------------+-------------------------------+
| * Fourier Spectrum & Spatial Frequency Concept    | * Spatial Neighborhood Masks  |
| * Filtering Pipeline (DFT -> H(u,v) -> IDFT)      | * 1st & 2nd Derivative Rules  |
| * Low-Pass Filters: ILPF, BLPF, GLPF (Smoothing)  | * Discrete Laplacian Operators|
| * High-Pass Filters: IHPF, BHPF, GHPF (Edges)     | * Mask Sign Conventions       |
| * Ringing Artifacts & Spatial Representation      | * Unsharp Masking & High-Boost|
+---------------------------------------------------+-------------------------------+
```

---

## 2. Section 1: Frequency-Domain Filtering

### 2.1 Image Frequency Domain & Fourier Spectrum Fundamentals

The spatial frequency of an image measures the rate of intensity changes across spatial coordinates $(x,y)$:
* **Low Frequencies ($u, v$ near origin):** Correspond to smooth, slowly varying intensity regions (e.g., background, flat surfaces, global illumination).
* **High Frequencies ($u, v$ far from origin):** Correspond to rapid intensity transitions, sharp edges, fine noise, and object contours.

#### 2D Discrete Fourier Transform (DFT) Pair

> Only the DFT definitions needed for Unit 2 frequency filtering are summarized here; full image-transform theory belongs to Unit 3.
For an image $f(x,y)$ of size $M \times N$:


```math
\text{Forward DFT:} \quad F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j 2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}
```


```math
\text{Inverse DFT (IDFT):} \quad f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j 2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}
```


where $u = 0, 1, \dots, M-1$ and $v = 0, 1, \dots, N-1$.

#### Fourier Spectrum, Phase, and Power Spectrum
* **Fourier Spectrum (Magnitude):** $|F(u,v)| = \sqrt{R^2(u,v) + I^2(u,v)}$, where $R$ and $I$ are real and imaginary parts.
* **Phase Angle:** $\phi(u,v)=\operatorname{atan2}(I(u,v),R(u,v))$; the two-argument form handles the correct quadrant.
* **Power Spectrum:** $P(u,v) = |F(u,v)|^2 = R^2(u,v) + I^2(u,v)$

> 🧠 **Must Understand:** The DC component $F(0,0) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) = MN \cdot \bar{f}$ represents $MN$ times the average intensity of the image.

#### Centering the Transform
For even $M,N$, multiplying by $(-1)^{x+y}$ before the DFT shifts the DC coefficient to $(M/2,N/2)$; for odd sizes use an explicit spectrum shift:


```math
F_c(u,v)=\mathcal{F}\{f(x,y)(-1)^{x+y}\}=F\bigl((u-M/2)\bmod M,(v-N/2)\bmod N\bigr),\quad M,N\text{ even}.
```


---

### 2.2 The Frequency-Domain Filtering Pipeline

Frequency-domain filtering relies on the **Convolution Theorem**: spatial convolution $f(x,y) * h(x,y)$ is mathematically equivalent to pointwise frequency multiplication $F(u,v) \cdot H(u,v)$.

```text
Input f(x,y)
   | multiply by (-1)^(x+y) [even M,N: center the spectrum]
   v
Centered spatial image f'(x,y)
   | 2D DFT
   v
Centered spectrum F_c(u,v)
   | pointwise multiply by filter H(u,v)
   v
Filtered spectrum G(u,v) = F_c(u,v) H(u,v)
   | inverse 2D DFT
   v
Spatial result g'(x,y)
   | take real part; multiply by (-1)^(x+y)
   v
Enhanced output g(x,y)
```

#### Step-by-Step Pipeline Equations:
1. **Pre-processing / Centering:** $f'(x,y) = f(x,y) \cdot (-1)^{x+y}$
2. **Forward Transform:** $F(u,v) = \mathcal{F}\{f'(x,y)\}$
3. **Filter Function Construction:** Generate transfer function $H(u,v)$ using the Euclidean distance from center:
   

```math
D(u,v) = \sqrt{\left(u - \frac{M}{2}\right)^2 + \left(v - \frac{N}{2}\right)^2}
```


4. **Spectral Filtering:** $G(u,v) = F(u,v) \cdot H(u,v)$
5. **Inverse Transform:** $g'(x,y) = \mathcal{F}^{-1}\{G(u,v)\}$
6. **Post-processing / Un-centering:** $g(x,y) = \text{Real}\left\{g'(x,y)\right\} \cdot (-1)^{x+y}$

---

### 2.3 Frequency-Domain Low-Pass Filters (ILPF, BLPF, GLPF)

Low-pass frequency filters attenuate high frequencies while passing low frequencies, resulting in image smoothing/blurring.

```text
ILPF (Ideal)                   BLPF (Butterworth, n=2)         GLPF (Gaussian)
H(u,v)                         H(u,v)                          H(u,v)
 1.0 |---------\                1.0 |----\                      1.0 |     |          |                   |     \                         |  0.0 +----------+----> D(u,v)   0.0 +------\------> D(u,v)      0.0 +---\--------> D(u,v)
          D0                             D0                             D0
  (Sharp Cutoff -> Ringing)     (Smooth Transition -> Low Ringing) (Gaussian -> Zero Ringing)
```

#### 1. Ideal Low-Pass Filter (ILPF)
Sets all frequencies beyond cutoff distance $D_0$ strictly to zero:


```math
H_{ILPF}(u,v) = \begin{cases} 1 & \text{if } D(u,v) \le D_0 \\ 0 & \text{if } D(u,v) > D_0 \end{cases}
```


* **Characteristics:** Completely attenuates high frequencies outside radius $D_0$.
* **Drawback:** Causes severe **ringing artifacts** (concentric ripples around edges) in the spatial domain due to the oscillatory spatial response of an ideal abrupt cutoff.

#### 2. Butterworth Low-Pass Filter (BLPF)
Introduces a smooth transition controlled by filter order $n$:


```math
H_{BLPF}(u,v) = \frac{1}{1 + \left[\frac{D(u,v)}{D_0}\right]^{2n}}
```


* **Characteristics:** At distance $D(u,v) = D_0$, $H(u,v) = 0.5$ (down $50\%$ or $-3\text{ dB}$).
* **Behavior with Order $n$:**
  * Low order ($n=1, 2$): Smooth transition, no visible ringing.
  * High order ($n \ge 5$): Approaches ILPF step behavior, introducing noticeable ringing.

#### 3. Gaussian Low-Pass Filter (GLPF)
Uses a perfectly smooth Gaussian function with standard deviation $\sigma = D_0$:


```math
H_{GLPF}(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}}
```


* **Characteristics:** At distance $D(u,v) = D_0$, $H(u,v) = e^{-0.5} \approx 0.607$.
* **Key Advantage:** The inverse Fourier transform of a Gaussian function is strictly another Gaussian function. Therefore GLPF avoids the characteristic abrupt-cutoff ringing of an ideal filter, although boundary processing can introduce other artifacts.

---

### 2.4 Frequency-Domain High-Pass Filters (IHPF, BHPF, GHPF)

High-pass frequency filters attenuate low frequencies while passing high frequencies, performing image sharpening and edge enhancement.

#### High-Pass Transfer Function Relation


```math
H_{HPF}(u,v) = 1 - H_{LPF}(u,v)
```


```text
+---------------------------+-------------------------------------------------------+
| High-Pass Filter Type     | Transfer Function $H_{HPF}(u,v)$                      |
+---------------------------+-------------------------------------------------------+
| Ideal High-Pass (IHPF)    | $H(u,v) = \begin{cases} 0 & D(u,v) \le D_0 \ 1 & D(u,v) > D_0 \end{cases}$ |
+---------------------------+-------------------------------------------------------+
| Butterworth High-Pass     | $H(u,v) = \frac{1}{1 + \left[\frac{D_0}{D(u,v)}\right]^{2n}}$         |
| (BHPF, order $n$)         |                                                       |
+---------------------------+-------------------------------------------------------+
| Gaussian High-Pass (GHPF) | $H(u,v) = 1 - e^{-\frac{D^2(u,v)}{2 D_0^2}}$          |
+---------------------------+-------------------------------------------------------+
```

> ⭐ **Must Remember:** In a centered spectrum, high-pass filters set $H(M/2,N/2)=0$; equivalently, $H(0,0)=0$ before centering. Thus the DC component is eliminated. Consequently, high-pass filtered spatial images have zero average intensity, appearing predominantly dark with highlighted bright/dark edge lines.

---

### 2.5 Comparative Analysis & Ringing Artifacts

```text
+-------------------+----------------------+------------------------+-------------------+
| Filter Category   | Ideal Filter         | Butterworth Filter     | Gaussian Filter   |
+-------------------+----------------------+------------------------+-------------------+
| Transition Profile| Discontinuous Step   | Smooth Polynomial      | Exponential Curve |
| Ringing Effect    | Severe (oscillations)| Increases with high $n$ | No ideal-cutoff ringing   |
| Implementation    | Non-realizable       | Realizable             | Realizable        |
| Primary Application| Theoretical Benchmark| Practical Trade-off    | Smooth Sharpening |
+-------------------+----------------------+------------------------+-------------------+
```

---

## 3. Section 2: Spatial Filtering & Image Sharpening

### 3.1 Neighborhood Processing & Filter Masks

Spatial domain filtering operates directly on pixels using a spatial mask (kernel/template) $w$ of size $m \times n$ (typically $3 \times 3$, $5 \times 5$):


```math
g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t) \cdot f(x+s, y+t)
```


where $a=(m-1)/2$ and $b=(n-1)/2$ for odd masks. The displayed weighted sum uses the correlation convention; symmetric Laplacian masks give the same result under convolution.

```text
Spatial Neighborhood (3x3):            Mask Weights (3x3):
[ f(x-1,y-1)  f(x-1,y)  f(x-1,y+1) ]    [ w(-1,-1)  w(-1,0)  w(-1,1) ]
[ f(x,y-1)    f(x,y)    f(x,y+1)   ]  * [ w(0,-1)   w(0,0)   w(0,1)  ]
[ f(x+1,y-1)  f(x+1,y)  f(x+1,y+1) ]    [ w(1,-1)   w(1,0)   w(1,1)  ]
```

---

### 3.2 First and Second Derivative Properties in Image Sharpening

Image sharpening highlights intensity transitions (edges, ramps, points). Differentiation in digital images is defined using finite differences.

#### Definitions of Finite Differences:
* **First Derivative (1D):**
  

```math
\frac{\partial f}{\partial x} = f(x+1) - f(x)
```


* **Second Derivative (1D):**
  

```math
\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)
```


```text
+------------------------------------+------------------+-------------------+
| Intensity Feature Profile          | 1st Derivative   | 2nd Derivative    |
+------------------------------------+------------------+-------------------+
| Flat Constant Region               | Zero             | Zero              |
| Onset of Step / Ramp               | Non-Zero         | Non-Zero          |
| Along Constant Slope Ramp          | Constant Non-Zero| Zero              |
| Isolated Noise Point               | Medium Response  | Very Strong       |
| Sign along Edge Transition         | Same Sign        | Double Sign (+/-) |
+------------------------------------+------------------+-------------------+
```

> ✍️ **Exam Focus Key Differences:**
> 1. First derivatives produce thick edges along ramps.
> 2. Second derivatives produce fine, double-line response along ramps and zero response on constant slopes.
> 3. Second derivatives respond much more strongly to isolated points and fine details.

---

### 3.3 Laplacian-Based Sharpening & Sign Conventions

The continuous Laplacian is an isotropic second-order derivative operator; discrete 4- and 8-neighbor masks approximate this symmetry:


```math
\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}
```


#### Discrete Formulation:


```math
\nabla^2 f(x,y) = f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1) - 4f(x,y)
```


Including diagonal neighbors yields the 8-neighbor Laplacian formulation:


```math
\nabla^2 f(x,y) = \sum_{\text{8-neighbors}} f_{\text{neighbor}} - 8f(x,y)
```


#### Laplacian Masks and Sign Conventions

```text
Mask 1 (4-Neighbor, Negative Center):       Mask 2 (8-Neighbor, Negative Center):
       [  0   1   0 ]                              [  1   1   1 ]
       [  1  -4   1 ]                              [  1  -8   1 ]
       [  0   1   0 ]                              [  1   1   1 ]
Enhancement: g(x,y) = f(x,y) - \nabla^2 f        Enhancement: g(x,y) = f(x,y) - \nabla^2 f

Mask 3 (4-Neighbor, Positive Center):       Mask 4 (8-Neighbor, Positive Center):
       [  0  -1   0 ]                              [ -1  -1  -1 ]
       [ -1   4  -1 ]                              [ -1   8  -1 ]
       [  0  -1   0 ]                              [ -1  -1  -1 ]
Enhancement: g(x,y) = f(x,y) + \nabla^2 f        Enhancement: g(x,y) = f(x,y) + \nabla^2 f
```

#### Composite Sharpening Masks (Single-Step Application)
By substituting the Laplacian mask directly into $g(x,y) = f(x,y) \pm \nabla^2 f(x,y)$, we obtain composite sharpening masks:

```text
4-Neighbor Composite Kernel (Center = 5):     8-Neighbor Composite Kernel (Center = 9):
       [  0  -1   0 ]                              [ -1  -1  -1 ]
       [ -1   5  -1 ]                              [ -1   9  -1 ]
       [  0  -1   0 ]                              [ -1  -1  -1 ]
```

---

### 3.4 Unsharp Masking & High-Boost Filtering

Unsharp masking subtracts a smoothed (blurred) version of an image from the original image to extract high-frequency detail.

#### The 3-Step Unsharp Masking Algorithm:
1. **Blur** the original image: $\overline{f}(x,y) = \text{Smooth}\{f(x,y)\}$
2. **Subtract** the blurred image from the original to produce the unsharp mask:
   

```math
g_{\text{mask}}(x,y) = f(x,y) - \overline{f}(x,y)
```


3. **Add** a weighted portion of the mask to the original:
   

```math
g(x,y) = f(x,y) + k \cdot g_{\text{mask}}(x,y)
```


#### Role of Weight Parameter $k$:
* **$k = 1$:** Standard Unsharp Masking, $g=2f-\bar f$.
* **$k > 1$:** Stronger weighted unsharp masking (amplifies high frequencies and noise; DC gain remains one for normalized blur).
* **$k < 1$:** De-emphasized unsharp masking.

#### High-Boost Amplification Factor Formulation ($A$)
There are two related but distinct conventions. For weighted unsharp masking $g_k=f+k(f-\bar f)$, set $A=1+k$ to obtain $g_k=Af-(A-1)\bar f$. The alternative amplified-original convention below defines $g_A=Af-\bar f$ directly; its $A$ is NOT the same as $1+k$ except at $A=2$:


```math
g_{hb}(x,y) = A \cdot f(x,y) - \overline{f}(x,y) = (A-1)f(x,y) + \left[f(x,y) - \overline{f}(x,y)\right]
```


```math
g_{A}(x,y) = (A-1)f(x,y) + f_{hp}(x,y),\qquad f_{hp}=f-\bar f.
```


**DC-gain check:** If the blur has unit-sum weights, weighted unsharp masking has DC gain $1$, while $g_A=Af-\bar f$ has DC gain $A-1$. For $A=1$, the latter is a pure high-pass output; for $A=2$, it is standard unsharp masking.

```text
High-Boost Composite Mask (4-Neighbor):       High-Boost Composite Mask (8-Neighbor):
       [  0  -1   0 ]                              [ -1  -1  -1 ]
       [ -1 w_c  -1 ]                              [ -1 w_c  -1 ]
       [  0  -1   0 ]                              [ -1  -1  -1 ]
where w_c = A + 3 (unnormalized 4-neighbor)    where w_c = A + 7 (unnormalized 8-neighbor)
```

**Mask convention:** These integer-neighbor masks implement $g_A=(A-1)f-\nabla^2f$ with a negative-center Laplacian; they are NOT the normalized-blur mask of $Af-\bar f$. For a normalized 5-point box blur, $Af-\bar f$ has center $A-1/5$ and axial neighbors $-1/5$. The original worked Problem 4 uses the unnormalized mask, so its pixel values remain 20, 35, and 50.

---

### 3.5 Comparative Analysis: High-Pass vs. Laplacian vs. High-Boost

```text
+----------------------+----------------------+----------------------+----------------------+
| Feature              | High-Pass Filter     | Laplacian Sharpening | High-Boost Filter    |
+----------------------+----------------------+----------------------+----------------------+
| Mask Sum             | Zero                 | Zero for Laplacian; one for composite sharpening | $A-1$ for the shown $A+3$ mask          |
| Background Intensity | Completely Lost (Dark| Preserved when added | Fully Preserved &    |
|                      | image)               | back to original     | Amplified ($A \cdot f$) |
| Edge Enhancement     | Strong               | Sharp double-edges   | Controllable ($k$)   |
| Noise Sensitivity    | High                 | Often high            | Depends on boost gain             |
+----------------------+----------------------+----------------------+----------------------+
```

---

## 4. Section 3: Formula & Filter-Mask Master Reference

### Frequency Domain Transfer Functions $H(u,v)$


```math
\text{Distance Function:} \quad D(u,v) = \sqrt{\left(u - \frac{M}{2}\right)^2 + \left(v - \frac{N}{2}\right)^2}
```


```text
+---------------------+---------------------------------------+---------------------------------------+
| Filter Family       | Low-Pass Filter $H_{LPF}(u,v)$         | High-Pass Filter $H_{HPF}(u,v)$        |
+---------------------+---------------------------------------+---------------------------------------+
| Ideal               | \begin{cases} 1 & D \le D_0 \ 0 & D > D_0 \end{cases} | \begin{cases} 0 & D \le D_0 \ 1 & D > D_0 \end{cases} |
+---------------------+---------------------------------------+---------------------------------------+
| Butterworth (Order $n$)| $\frac{1}{1 + \left[D(u,v)/D_0\right]^{2n}}$ | $\frac{1}{1 + \left[D_0/D(u,v)\right]^{2n}}$ |
+---------------------+---------------------------------------+---------------------------------------+
| Gaussian            | $e^{-\frac{D^2(u,v)}{2 D_0^2}}$       | $1 - e^{-\frac{D^2(u,v)}{2 D_0^2}}$   |
+---------------------+---------------------------------------+---------------------------------------+
```

### Master Spatial Filter Masks

```text
1. 4-Neighbor Laplacian (Center = -4):        2. 8-Neighbor Laplacian (Center = -8):
   [  0   1   0 ]                                [  1   1   1 ]
   [  1  -4   1 ]                                [  1  -8   1 ]
   [  0   1   0 ]                                [  1   1   1 ]

3. 4-Neighbor Sharpening (Center = 5):         4. 8-Neighbor Sharpening (Center = 9):
   [  0  -1   0 ]                                [ -1  -1  -1 ]
   [ -1   5  -1 ]                                [ -1   9  -1 ]
   [  0  -1   0 ]                                [ -1  -1  -1 ]

5. High-Boost 4-Neighbor (w_c = A + 3):         6. High-Boost 8-Neighbor (w_c = A + 7):
   [  0  -1   0 ]                                [ -1  -1  -1 ]
   [ -1 A+3  -1 ]                                [ -1 A+7  -1 ]
   [  0  -1   0 ]                                [ -1  -1  -1 ]
```

---

## 5. Section 4: Step-by-Step Computational Procedures

### Procedure 1: Frequency-Domain Filtering Workflow
1. Given $M \times N$ spatial image $f(x,y)$.
2. Calculate pre-processed matrix: $f'(x,y) = f(x,y) \cdot (-1)^{x+y}$.
3. Compute 2D DFT: $F(u,v) = \text{DFT}\{f'(x,y)\}$.
4. Compute distance matrix $D(u,v)$ from origin $(M/2, N/2)$.
5. Construct filter transfer function matrix $H(u,v)$ for given cutoff $D_0$.
6. Perform pointwise multiplication: $G(u,v) = F(u,v) \cdot H(u,v)$.
7. Compute inverse 2D DFT: $g'(x,y) = \text{IDFT}\{G(u,v)\}$.
8. Extract real part and un-center: $g(x,y) = \text{Real}\left\{g'(x,y)\right\} \cdot (-1)^{x+y}$.

---

### Procedure 2: Spatial Laplacian Convolution Workflow
1. Overlay $3 \times 3$ Laplacian mask $w$ over target pixel $f(x,y)$.
2. Multiply corresponding mask weights with underlying pixel intensities.
3. Sum all 9 products to calculate $\nabla^2 f(x,y)$.
4. Apply sign-convention sharpening equation:
   * If the Laplacian center weight is negative ($-4$ or $-8$): $g(x,y) = f(x,y) - \nabla^2 f(x,y)$.
   * If the Laplacian center weight is positive ($+4$ or $+8$): $g(x,y) = f(x,y) + \nabla^2 f(x,y)$.
5. Truncate/scale resulting values to $[0, 255]$ range if necessary.

---

## 6. Section 5: Solved Worked Numerical Problems

### Problem 1: Step-by-Step Frequency-Domain Filtering ($4 \times 4$ Matrix, $D_0 = 0.5$)

#### Problem Statement:
Given a $4 \times 4$ spatial domain image $f(x,y)$:


```math
f(x,y) = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \end{bmatrix}
```


Perform frequency-domain filtering using an **Ideal High-Pass Filter (IHPF)** with cutoff frequency $D_0 = 0.5$. Show step-by-step procedures.

---

#### Step-by-Step Solution:

##### Step 1: Pre-processing (Centering)
Multiply $f(x,y)$ by $(-1)^{x+y}$:


```math
(-1)^{x+y} = \begin{bmatrix} +1 & -1 & +1 & -1 \\ -1 & +1 & -1 & +1 \\ +1 & -1 & +1 & -1 \\ -1 & +1 & -1 & +1 \end{bmatrix}
```


```math
f'(x,y) = f(x,y) \cdot (-1)^{x+y} = \begin{bmatrix} 1 & 0 & 1 & 0 \\ -1 & 0 & -1 & 0 \\ 1 & 0 & 1 & 0 \\ -1 & 0 & -1 & 0 \end{bmatrix}
```


##### Step 2: Compute 2D DFT $F(u,v)$
Using matrix multiplication $F = K \cdot f' \cdot K^T$, where 1D 4-point DFT kernel $K$ is:


```math
K = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix}
```


1. First compute $A = K \cdot f'$:


```math
A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix} \begin{bmatrix} 1 & 0 & 1 & 0 \\ -1 & 0 & -1 & 0 \\ 1 & 0 & 1 & 0 \\ -1 & 0 & -1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 4 & 0 & 4 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
```


2. Now compute $F = A \cdot K^T$:


```math
F(u,v) = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 4 & 0 & 4 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -j & -1 & j \\ 1 & -1 & 1 & -1 \\ 1 & j & -1 & -j \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 8 & 0 & 8 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
```


##### Step 3: Distance Matrix $D(u,v)$ Calculation
Frequency rectangle size is $4 \times 4$, so center is at $(u_0, v_0) = (2, 2)$.


```math
D(u,v) = \sqrt{(u-2)^2 + (v-2)^2}
```


Distance values for $u, v \in \{0, 1, 2, 3\}$:
* $u=0, v=0 \implies D(0,0) = \sqrt{(-2)^2 + (-2)^2} = \sqrt{8} \approx 2.828$
* $u=2, v=0 \implies D(2,0) = \sqrt{(0)^2 + (-2)^2} = 2.0$
* $u=2, v=2 \implies D(2,2) = \sqrt{0 + 0} = 0.0$

Distance Matrix $D(u,v)$:


```math
D(u,v) = \begin{bmatrix} 2.828 & 2.236 & 2.000 & 2.236 \\ 2.236 & 1.414 & 1.000 & 1.414 \\ 2.000 & 1.000 & 0.000 & 1.000 \\ 2.236 & 1.414 & 1.000 & 1.414 \end{bmatrix}
```


##### Step 4: Construct Ideal High-Pass Filter $H_{IHPF}(u,v)$ ($D_0 = 0.5$)


```math
H(u,v) = \begin{cases} 0 & \text{if } D(u,v) \le 0.5 \\ 1 & \text{if } D(u,v) > 0.5 \end{cases}
```


Since $D(2,2) = 0.0 \le 0.5$, $H(2,2) = 0$. All other coordinates have $D(u,v) > 0.5$, so $H(u,v) = 1$:


```math
H(u,v) = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix}
```


##### Step 5: Spectral Filtering $G(u,v) = F(u,v) \cdot H(u,v)$


```math
G(u,v) = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 8 & 0 & 8 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \circ \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 8 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
```


##### Step 6: Inverse DFT and Un-centering
Using IDFT matrix relation $g' = \frac{1}{16} K^* \cdot G \cdot (K^*)^T$:


```math
g'(x,y) = \begin{bmatrix} 0.5 & 0.5 & 0.5 & 0.5 \\ -0.5 & -0.5 & -0.5 & -0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \\ -0.5 & -0.5 & -0.5 & -0.5 \end{bmatrix}
```


Multiplying by $(-1)^{x+y}$ to un-center:


```math
g(x,y) = g'(x,y) \cdot (-1)^{x+y} = \begin{bmatrix} 0.5 & -0.5 & 0.5 & -0.5 \\ 0.5 & -0.5 & 0.5 & -0.5 \\ 0.5 & -0.5 & 0.5 & -0.5 \\ 0.5 & -0.5 & 0.5 & -0.5 \end{bmatrix}
```


---

### Problem 2: 1D Scanline First and Second Derivative Calculation

#### Problem Statement:
Given a 1D image scanline segment $f(x)$:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $f(x)$ | 5 | 5 | 5 | 5 | 2 | 1 | 0 | 0 | 6 | 0 | 0 | 0 |

Compute the first derivative $\frac{\partial f}{\partial x}$ and second derivative $\frac{\partial^2 f}{\partial x^2}$. State key observations.

---

#### Step-by-Step Solution:

1. **First Derivative Equation:** $\frac{\partial f}{\partial x} = f(x+1) - f(x)$
2. **Second Derivative Equation:** $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$

#### Calculation Table:

At $x=0$, use replicated boundary value $f(-1)=f(0)=5$; at $x=11$, the forward difference and second difference require $f(12)$, which is unspecified, so both remain undefined.

| Coordinate ($x$) | Intensity $f(x)$ | First Derivative $\frac{\partial f}{\partial x}$ | Second Derivative $\frac{\partial^2 f}{\partial x^2}$ | Feature Type |
|---|---|---|---|---|
| 0 | 5 | $5-5 = 0$ | $5+5-2(5) = 0$ | Boundary (replicate $f(-1)=5$) |
| 1 | 5 | $5-5 = 0$ | $5+5-2(5) = 0$ | Constant Flat |
| 2 | 5 | $5-5 = 0$ | $5+5-2(5) = 0$ | Constant Flat |
| 3 | 5 | $2-5 = -3$ | $2+5-2(5) = -3$ | Ramp Onset |
| 4 | 2 | $1-2 = -1$ | $1+5-2(2) = +2$ | Along Ramp |
| 5 | 1 | $0-1 = -1$ | $0+2-2(1) = 0$ | Along Ramp |
| 6 | 0 | $0-0 = 0$ | $0+1-2(0) = +1$ | Ramp End |
| 7 | 0 | $6-0 = +6$ | $6+0-2(0) = +6$ | Isolated Point Onset |
| 8 | 6 | $0-6 = -6$ | $0+0-2(6) = -12$| Isolated Point Peak |
| 9 | 0 | $0-0 = 0$ | $0+6-2(0) = +6$ | Isolated Point End |
| 10| 0 | $0-0 = 0$ | $0+0-2(0) = 0$ | Constant Flat |
| 11| 0 | - | - | Boundary |

#### Key Observations:
1. **Ramp Transition ($x=3 \to 6$):** First derivative stays non-zero ($-3, -1, -1$) throughout the ramp, whereas the second derivative is $-3$ at $x=3$, $+2$ at $x=4$ where the slope changes, $0$ at $x=5$ along the constant-slope portion, and $+1$ at $x=6$ where the ramp ends.
2. **Isolated Point ($x=8$, value $6$):** Second derivative yields extremely strong double-sign response ($+6, -12, +6$), proving second derivatives are far more sensitive to fine details/noise than first derivatives.

---

### Problem 3: 2D Spatial Laplacian Convolution on $6 \times 6$ Step Edge Image

#### Problem Statement:
Given a $6 \times 6$ grayscale image containing a horizontal step edge transition from intensity 50 to 100:


```math
f(x,y) = \begin{bmatrix} 50 & 50 & 50 & 50 & 50 & 50 \\ 50 & 50 & 50 & 50 & 50 & 50 \\ 50 & 50 & 50 & 50 & 50 & 50 \\ 100 & 100 & 100 & 100 & 100 & 100 \\ 100 & 100 & 100 & 100 & 100 & 100 \\ 100 & 100 & 100 & 100 & 100 & 100 \end{bmatrix}
```


Apply the 8-neighbor Laplacian mask with negative center weight:


```math
w = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix}
```


1. Compute the Laplacian response $\nabla^2 f(x,y)$ for all interior pixels.
2. Compute the sharpened image $g(x,y) = f(x,y) - \nabla^2 f(x,y)$ on the interior; the image boundary has no specified padding rule.

---

#### Step-by-Step Solution:

##### 1. Interior Pixel Calculations for $\nabla^2 f(x,y)$:

* **Row 1 (Flat Intensity 50):**
  Neighborhood centered at $(1,c)$ contains all 50s.
  

```math
\nabla^2 f = (1 \times 50) \times 8 - 8 \times 50 = 400 - 400 = 0
```


* **Row 2 (Upper Side of Edge, Intensity 50):**
  Top 3 neighbors (Row 1) = 50. Left & Right neighbors (Row 2) = 50. Center = 50.
  Bottom 3 neighbors (Row 3) = 100.
  

```math
\nabla^2 f = (3 \times 50) + (2 \times 50) + (3 \times 100) - (8 \times 50) = 150 + 100 + 300 - 400 = +150
```


* **Row 3 (Lower Side of Edge, Intensity 100):**
  Top 3 neighbors (Row 2) = 50. Left & Right neighbors (Row 3) = 100. Center = 100.
  Bottom 3 neighbors (Row 4) = 100.
  

```math
\nabla^2 f = (3 \times 50) + (2 \times 100) + (3 \times 100) - (8 \times 100) = 150 + 200 + 300 - 800 = -150
```


* **Row 4 (Flat Intensity 100):**
  Neighborhood centered at $(4,c)$ contains all 100s.
  

```math
\nabla^2 f = (1 \times 100) \times 8 - 8 \times 100 = 800 - 800 = 0
```


##### Resulting Laplacian matrix $\nabla^2 f(x,y)$ for the **4 interior rows and 4 interior columns** (row and column indices $1$ through $4$):


```math
\nabla^2 f_{\mathrm{interior}}=\begin{bmatrix}0&0&0&0\\150&150&150&150\\-150&-150&-150&-150\\0&0&0&0\end{bmatrix}.
```


##### 2. Sharpened Image Calculation $g(x,y) = f(x,y) - \nabla^2 f(x,y)$:

* **Row 1:** $50 - 0 = 50$
* **Row 2:** $50 - (+150) = -100 \implies 0$ (Truncated/Clipped to 0)
* **Row 3:** $100 - (-150) = 250$
* **Row 4:** $100 - 0 = 100$

##### Resulting Sharpened Matrix $g(x,y)$:


```math
g_{\mathrm{interior}}=\begin{bmatrix}50&50&50&50\\0&0&0&0\\250&250&250&250\\100&100&100&100\end{bmatrix}.
```


The original problem does not specify padding or another boundary rule, so the **outer border is deliberately not computed**. These $4\times4$ results apply only to interior pixels; choosing zero, replicate, or reflect padding would give different border values.

> 🧠 **Must Understand:** The subtraction $-150$ at Row 2 creates an **undershoot** ($0$), while the addition $+150$ at Row 3 creates an **overshoot** ($250$). This sharpens edge contrast dramatically.

---

### Problem 4: High-Boost Spatial Filter Mask Construction & Application

#### Problem Statement:
Given a $3 \times 3$ image neighborhood $f$, use the **unnormalized negative-Laplacian high-pass mask** $g_A=(A-1)f-\nabla^2_4f$, not a normalized five-point blur:


```math
f = \begin{bmatrix} 10 & 20 & 30 \\ 40 & 30 & 20 \\ 10 & 20 & 30 \end{bmatrix}
```


Construct a 4-neighbor high-boost filter mask for amplification factors $A = 1.0, 1.5, 2.0$. Calculate the enhanced center pixel intensity for each case.

---

#### Step-by-Step Solution:

##### 1. High-Boost Mask Equation (4-Neighbor)


```math
w_{hb} = \begin{bmatrix} 0 & -1 & 0 \\ -1 & w_c & -1 \\ 0 & -1 & 0 \end{bmatrix} \quad \text{where } w_c = A + 4 - 1 = A + 3
```


* **Case 1 ($A = 1.0$ - Pure High-Pass Output):**
  $w_c = 1.0 + 3 = 4 \implies w_{hb} = \begin{bmatrix} 0 & -1 & 0 \ -1 & 4 & -1 \ 0 & -1 & 0 \end{bmatrix}$
  

```math
\text{Response} = 4(30) - 1(20) - 1(40) - 1(20) - 1(20) = 120 - 100 = 20
```


* **Case 2 ($A = 1.5$ - High-Boost Filtering):**
  $w_c = 1.5 + 3 = 4.5 \implies w_{hb} = \begin{bmatrix} 0 & -1 & 0 \ -1 & 4.5 & -1 \ 0 & -1 & 0 \end{bmatrix}$
  

```math
\text{Response} = 4.5(30) - 100 = 135 - 100 = 35
```


* **Case 3 ($A = 2.0$ - High-Boost Filtering):**
  $w_c = 2.0 + 3 = 5.0 \implies w_{hb} = \begin{bmatrix} 0 & -1 & 0 \ -1 & 5.0 & -1 \ 0 & -1 & 0 \end{bmatrix}$
  

```math
\text{Response} = 5.0(30) - 100 = 150 - 100 = 50
```


---

### Problem 5: Frequency-Domain High-Boost Transfer Function Derivation

#### Problem Statement:
Derive the frequency-domain transfer function $H_{HB}(u,v)$ for high-boost filtering in terms of a low-pass filter transfer function $H_{LP}(u,v)$ and amplification factor $A$.

#### Step-by-Step Derivation:

1. By spatial definition, the unsharp mask is:
   

```math
g_{\text{mask}}(x,y) = f(x,y) - f_{lp}(x,y)
```


2. High-boost filtered image is defined as:
   

```math
g_{hb}(x,y) = f(x,y) + k \cdot g_{\text{mask}}(x,y) \quad (k \ge 1)
```


3. Substituting $g_{\text{mask}}$:
   

```math
g_{hb}(x,y) = f(x,y) + k\left[f(x,y) - f_{lp}(x,y)\right] = (1+k)f(x,y) - k \cdot f_{lp}(x,y)
```


4. Let $A=1+k$, so $k=A-1$. For the **weighted-unsharp convention**,
   

```math
g_k(x,y)=A f(x,y)-(A-1)f_{lp}(x,y).
```


   The **amplified-original convention** instead defines $g_A=Af-f_{lp}$ directly; it does not follow from setting $A=1+k$ in step 3.
5. Taking the Fourier transform: weighted-unsharp $G_k=F[A-(A-1)H_{LP}]$; amplified-original $G_A=F[A-H_{LP}]$. Assume $H_{LP}(0,0)=1$ in uncentered coordinates.
6. Therefore the **amplified-original** transfer function is $H_A=A-H_{LP}=(A-1)+H_{HP}$, where $H_{HP}=1-H_{LP}$. The **weighted-unsharp** function is $H_k=A-(A-1)H_{LP}=1+(A-1)H_{HP}$. Both are valid when their definitions are kept separate.

---

## 7. Section 6: Quick Revision & Exam Essentials

### Quick Revision Summary
* **Frequency Domain Filtering:** Modifies 2D DFT coefficients. Smooth blurring is achieved via Low-Pass Filters ($H_{LPF}$); edge sharpening is achieved via High-Pass Filters ($H_{HPF}$).
* **Ringing Artifacts:** Caused by discontinuous frequency transitions (ILPF/IHPF step function). Eliminated using smooth Gaussian filters ($GLPF/GHPF$).
* **Derivative Sharpening:** First derivatives generate thick edges along ramps; second derivatives (Laplacian) generate fine double-lines and strong point-noise responses.
* **Laplacian Mask Sign Rule:**
  * Negative Center Weight ($-4$ or $-8$): Subtract from original image $g = f - \nabla^2 f$.
  * Positive Center Weight ($+4$ or $+8$): Add to original image $g = f + \nabla^2 f$.
* **High-Boost Filtering:** Amplified-original $g_A=Af-f_{lp}=(A-1)f+f_{hp}$ has DC gain $A-1$; weighted-unsharp $g_k=f+k(f-f_{lp})$ has DC gain $1$. The integer-weight $A+3$ mask instead uses an unnormalized Laplacian high-pass response.

---

### Important Definitions
1. **Spatial Frequency:** Rate of intensity variation per unit spatial distance across an image.
2. **Fourier Spectrum:** Magnitude matrix $|F(u,v)|$ representing spatial frequency energy content.
3. **DC Component:** $F(0,0)$, equal to $MN$ times the average image intensity.
4. **Cutoff Frequency ($D_0$):** Boundary distance in frequency rectangle separating passed vs attenuated frequencies.
5. **Ringing Artifact:** Spatial ripple patterns caused by sinc-like inverse transform of abrupt frequency cutoffs.
6. **Laplacian:** Isotropic second-order differential operator $\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$.
7. **Unsharp Masking:** Sharpening technique subtracting a smoothed image from the original to extract edge detail.
8. **High-Boost Filtering:** An amplified-original or weighted-unsharp sharpening method; state which definition of $A$ and blur normalization is used. $A=1$ in the $A+3$ mask gives only a high-pass response, not preserved background.

---

### Frequency-Filtering Steps Summary
1. Pre-process: $f'(x,y) = f(x,y) \cdot (-1)^{x+y}$.
2. Forward DFT: $F(u,v) = \mathcal{F}\{f'(x,y)\}$.
3. Construct Transfer Function $H(u,v)$ using distance $D(u,v) = \sqrt{(u-M/2)^2 + (v-N/2)^2}$.
4. Multiply: $G(u,v) = F(u,v) \cdot H(u,v)$.
5. Inverse DFT: $g'(x,y) = \mathcal{F}^{-1}\{G(u,v)\}$.
6. Un-center: $g(x,y) = \text{Real}\{g'(x,y)\} \cdot (-1)^{x+y}$.

---

### Spatial-Sharpening Steps Summary
1. Overlay spatial mask $w(s,t)$ over target pixel $f(x,y)$.
2. Compute sum of products: $R = \sum w(s,t) f(x+s, y+t)$.
3. Combine response $R$ with original pixel $f(x,y)$ based on operator type (Laplacian addition/subtraction or High-Boost weighting).
4. Clamp/Scale output to valid display range $[0, 255]$.

---

### Formula and Mask List


```math
\text{Distance Function:} \quad D(u,v) = \sqrt{(u-M/2)^2 + (v-N/2)^2}
```


```math
\text{Gaussian Low-Pass:} \quad H_{GLPF}(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}}
```


```math
\text{Gaussian High-Pass:} \quad H_{GHPF}(u,v) = 1 - e^{-\frac{D^2(u,v)}{2 D_0^2}}
```


```math
\text{Butterworth Low-Pass:} \quad H_{BLPF}(u,v) = \frac{1}{1 + \left[D(u,v)/D_0\right]^{2n}}
```


```math
\text{High-Boost Formulation:} \quad g_{hb}(x,y) = A \cdot f(x,y) - f_{lp}(x,y)
```


```text
4-Neighbor Sharpening Mask (Center = 5):      8-Neighbor Sharpening Mask (Center = 9):
       [  0  -1   0 ]                              [ -1  -1  -1 ]
       [ -1   5  -1 ]                              [ -1   9  -1 ]
       [  0  -1   0 ]                              [ -1  -1  -1 ]
```

---

### ⚠️ Common Mistakes
1. ❌ **Forgetting Centering Multiplication:** Computing DFT without $(-1)^{x+y}$ places DC component at $(0,0)$ top-left instead of matrix center $(M/2, N/2)$.
2. ❌ **Reversing Laplacian Sign Rules:** Adding a negative-center Laplacian mask instead of subtracting it (yields image smoothing instead of sharpening).
3. ❌ **Confusing ILPF Ringing with GLPF:** Claiming Gaussian filters produce ringing. (GLPF avoids ideal-cutoff ringing; other artifacts can still occur!).
4. ❌ **Mixing High-Boost Conventions:** $A+3$ (4-neighbor) and $A+7$ (8-neighbor) apply to the unnormalized Laplacian mask; $Af-\bar f$ with a normalized five-point blur instead uses center $A-1/5$ and neighbors $-1/5$.

---

### ✍️ Last-Minute Checklist
* [x] Can you calculate Euclidean distance $D(u,v)$ from frequency center $(M/2, N/2)$?
* [x] Can you construct ILPF, BLPF, GLPF, IHPF, BHPF, GHPF transfer function matrices?
* [x] Do you know why Ideal filters produce ringing while Gaussian filters do not?
* [x] Can you write down all 4 standard 2D Laplacian spatial masks?
* [x] Do you know the exact formula for Unsharp Masking ($k=1$) and High-Boost Filtering ($A > 1$)?
* [x] Can you compute 1D and 2D spatial derivatives step-by-step on given numerical matrices?

---

### Complete M2 Unit 2 Coverage Checklist
* [x] Frequency-domain filtering process & pipeline
* [x] Low-pass frequency filters (ILPF, BLPF, GLPF)
* [x] High-pass frequency filters (IHPF, BHPF, GHPF)
* [x] Ringing artifacts analysis
* [x] Neighborhood processing & spatial filter masks
* [x] Spatial sharpening via 1st and 2nd derivatives
* [x] Laplacian-based sharpening & sign conventions
* [x] Unsharp masking & high-boost filtering ($A$ factor)
* [x] Complete worked numerical problems (practice examples; exam provenance not asserted)
