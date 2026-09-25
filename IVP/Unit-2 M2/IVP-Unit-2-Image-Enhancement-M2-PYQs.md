# 📚 IVP Unit 2: Image Enhancement — M2 Previous Year Question (PYQ) Bank

---

## 📌 Document Overview & Exam Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 2 — Image Enhancement (M2 Exam Specific Scope)
* **Target Output:** Master PYQ Bank & Exam Problem Solver
* **Format:** GitHub Flavored Markdown (GFM) with LaTeX Math
* **Scope Boundary Notice:** In strict compliance with M2 examination directives, this document is strictly restricted to **Frequency-Domain Filtering** (Fourier spectrum, DFT-filter-IDFT workflow, Ideal/Butterworth/Gaussian Low-Pass and High-Pass filters, ringing artifacts) and **Spatial Sharpening** (Neighborhood processing, First/Second derivatives, Laplacian masks, Unsharp Masking, High-Boost Filtering). Standalone spatial smoothing filters, point processing (digital negatives, contrast stretching, log/gamma transforms, intensity slicing), and histogram equalization are excluded except where explicitly flagged as out-of-scope sub-parts of historical paper questions.

---

## 📑 Table of Contents

1. [Verified Question Paper Index](#1-verified-question-paper-index)
2. [Category A: Conceptual & Theoretical PYQs](#2-category-a-conceptual--theoretical-pyqs)
   * A.1 [Frequency Domain Filtering Process & Centering Workflow](#a1-frequency-domain-filtering-process--centering-workflow)
   * A.2 [Low-Pass vs. High-Pass Frequency Domain Filters (ILPF, BLPF, GLPF)](#a2-low-pass-vs-high-pass-frequency-domain-filters-ilpf-blpf-glpf)
   * A.3 [Ringing Artifacts & Gibbs Phenomenon Analysis](#a3-ringing-artifacts--gibbs-phenomenon-analysis)
   * A.4 [Spatial Sharpening Principles & Derivative Properties](#a4-spatial-sharpening-principles--derivative-properties)
   * A.5 [Unsharp Masking & High-Boost Filtering Mechanisms](#a5-unsharp-masking--high-boost-filtering-mechanisms)
3. [Category B: Comparative Analysis PYQs](#3-category-b-comparative-analysis-pyqs)
   * B.1 [Spatial Domain vs. Frequency Domain Filtering](#b1-spatial-domain-vs-frequency-domain-filtering)
   * B.2 [Low-Pass (Smoothing) vs. High-Pass (Sharpening) Filters](#b2-low-pass-smoothing-vs-high-pass-sharpening-filters)
   * B.3 [Ideal vs. Butterworth vs. Gaussian Frequency Filters](#b3-ideal-vs-butterworth-vs-gaussian-frequency-filters)
   * B.4 [High-Pass vs. Laplacian vs. High-Boost Spatial Filters](#b4-high-pass-vs-laplacian-vs-high-boost-spatial-filters)
4. [Category C: Mathematical Derivations & Mask Formulations](#4-category-c-mathematical-derivations--mask-formulations)
   * C.1 [2D Spatial Laplacian Mask Derivation (4-Way & 8-Way)](#c1-2d-spatial-laplacian-mask-derivation-4-way--8-way)
   * C.2 [High-Boost Spatial Filter Mask Derivation ($A$ Parameter)](#c2-high-boost-spatial-filter-mask-derivation-a-parameter)
   * C.3 [Frequency Domain High-Pass & High-Boost Transfer Function Derivations](#c3-frequency-domain-high-pass--high-boost-transfer-function-derivations)
   * C.4 [Frequency Domain Laplacian Transfer Function Derivation](#c4-frequency-domain-laplacian-transfer-function-derivation)
5. [Category D: Step-by-Step Worked Numerical Problems](#5-category-d-step-by-step-worked-numerical-problems)
   * [Numerical 1: $4 \times 4$ Image Step-by-Step Frequency Domain Filtering ($D_0 = 0.5$)](#numerical-1-4-times-4-image-step-by-step-frequency-domain-filtering-d_0--05)
   * [Numerical 2: 2D Spatial Laplacian Convolution on $5 \times 5$ Edge Image](#numerical-2-2d-spatial-laplacian-convolution-on-5-times-5-edge-image)
   * [Numerical 3: 1D Scanline First and Second Derivative Calculation](#numerical-3-1d-scanline-first-and-second-derivative-calculation)
   * [Numerical 4: High-Boost Spatial Filtering with Amplification Factor $A = 1.5$](#numerical-4-high-boost-spatial-filtering-with-amplification-factor-a--15)
   * [Numerical 5: High-Boost Frequency Transfer Function Numerical Evaluation](#numerical-5-high-boost-frequency-transfer-function-numerical-evaluation)
6. [Category E: Multi-Part Combined PYQs (Flagged Out-of-Scope Parts)](#6-category-e-multi-part-combined-pyqs-flagged-out-of-scope-parts)
7. [Section 7: Last-Minute Exam Mastery Checklist](#7-section-7-last-minute-exam-mastery-checklist)

---

## 1. Verified Question Paper Index

The questions compiled in this PYQ bank are verified against original semester examination question papers and official university mark schemes:

| Paper Source / University | Exam Session / Year | Q. No. | Topic Covered | Verified Marks |
| :--- | :--- | :--- | :--- | :--- |
| **AKTU End Semester Exam** | 2018–19 | Q.3(b) | Frequency Domain Filtering Process (LPF & HPF) | 10 Marks |
| **AKTU End Semester Exam** | 2017–18 | Q.2.26 / Q.5(b) | Working & Derivation of 2D Laplacian Filter | 10 Marks |
| **AKTU End Semester Exam** | 2014–15 | Q.2.25 | Frequency Response of Laplacian Mask | 5 Marks |
| **AKTU End Semester Exam** | 2014–15 | Q.2.22 / Q.3(d) | Laplacian Filter Application on Step Edge Matrix | 5 Marks |
| **AKTU End Semester Exam** | 2015–16 / 2018–19 | Q.2.2 (2-Mark) | Standard $3 \times 3$ Sobel and Prewitt Masks | 2 Marks |
| **NMIMS Semester V Exam** | 2022–23 | Q.4(a) | $3 \times 3$ Laplacian Filter on $5 \times 5$ Matrix | 10 Marks |
| **IVP Class Test / M2 Notes** | 2024–25 | Problem 1 | $4 \times 4$ Matrix Frequency Domain Ideal Filtering ($D_0=0.5$) | 10 Marks |
| **IVP Class Test / M2 Notes** | 2024–25 | Problem 2 | Spatial Laplacian Convolution & High-Boost Calculation | 10 Marks |

---

## 2. Category A: Conceptual & Theoretical PYQs

### A.1 Frequency Domain Filtering Process & Centering Workflow

#### ❓ Master Question (Grouped Identical & Equivalent PYQs)
> **Source:** AKTU 2018–19 (Q.3b, 10 Marks) | Practice Question
> 
> *(a) Explain the complete step-by-step process of filtering an image in the frequency domain with a neat block diagram.*
> *(b) Why do we multiply the spatial input image $f(x,y)$ by $(-1)^{x+y}$ before computing the Discrete Fourier Transform (DFT)? Prove mathematically how this centers the transform in the frequency plane.*

---

#### 💡 Master Answer

##### (a) Step-by-Step Frequency-Domain Filtering Workflow

Filtering in the frequency domain consists of modifying the Fourier transform coefficients of an image using a transfer function $H(u,v)$, followed by computing the inverse Fourier transform to return to the spatial domain.

```
+------------------------------------+
|  Input Image f(x,y) (Size M x N)   |
+------------------------------------+
                  |
                  v
+------------------------------------+
| Step 1: Center Transform           |
| Multiply by (-1)^(x+y)             |
+------------------------------------+
                  |
                  v
+------------------------------------+
| Step 2: Compute 2D DFT             |
| F(u,v) = DFT[ f(x,y) (-1)^(x+y) ]  |
+------------------------------------+
                  |
                  v
+------------------------------------+
| Step 3: Pointwise Multiplication   |
| G(u,v) = H(u,v) * F(u,v)           |
+------------------------------------+
                  |
                  v
+------------------------------------+
| Step 4: Compute Inverse 2D DFT     |
| g_p(x,y) = Real{ IDFT[ G(u,v) ] }  |
+------------------------------------+
                  |
                  v
+------------------------------------+
| Step 5: Decentralize Result        |
| g(x,y) = g_p(x,y) * (-1)^(x+y)     |
+------------------------------------+
                  |
                  v
+------------------------------------+
| Output Filtered Image g(x,y)       |
+------------------------------------+
```

##### (b) Mathematical Proof of Shift/Centering Property

**Objective:** To show that multiplying $f(x,y)$ by $(-1)^{x+y}$ shifts the origin of the Discrete Fourier Transform to the center of the frequency rectangle, i.e., $(u_0, v_0) = (M/2, N/2)$.

**Proof:**
The 2D Discrete Fourier Transform formula for an $M \times N$ image is:
$$F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}$$

Recall Euler's identity for $(-1)^{x+y}$:
$$(-1)^{x+y} = (-1)^x (-1)^y = (e^{j\pi})^x (e^{j\pi})^y = e^{j\pi x} e^{j\pi y} = e^{j 2\pi \left( \frac{(M/2)x}{M} + \frac{(N/2)y}{N} \right)}$$

Now, substitute $f(x,y) (-1)^{x+y}$ into the DFT equation:
$$\mathcal{F} \left[ f(x,y) (-1)^{x+y} \right] = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} \left[ f(x,y) e^{j 2\pi \left( \frac{(M/2)x}{M} + \frac{(N/2)y}{N} \right)} \right] e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}$$

Combining the exponential exponents:
$$= \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j 2\pi \left( \frac{(u - M/2)x}{M} + \frac{(v - N/2)y}{N} \right)} = F\left( u - \frac{M}{2}, v - \frac{N}{2} \right)$$

$$\therefore \mathcal{F}\left[ f(x,y) (-1)^{x+y} \right] = F\left( u - \frac{M}{2}, v - \frac{N}{2} \right) \quad \text{(Q.E.D.)}$$

**Exam Significance:** Without this multiplication, the low-frequency DC component $F(0,0)$ resides at the top-left corner $(0,0)$. Centering moves $F(0,0)$ to $(M/2, N/2)$, allowing radially symmetric filters $H(u,v)$ based on Euclidean distance $D(u,v)$ to be applied easily around the center.

---

### A.2 Low-Pass vs. High-Pass Frequency Domain Filters (ILPF, BLPF, GLPF)

#### ❓ Master Question
> **Source:** AKTU 2018–19 (Q.3b) | Practice Question
> 
> *Define and state the transfer functions $H(u,v)$ for the following 2D frequency-domain filters:*
> *(i) Ideal Low-Pass Filter (ILPF) and Ideal High-Pass Filter (IHPF)*
> *(ii) Butterworth Low-Pass Filter (BLPF) and Butterworth High-Pass Filter (BHPF)*
> *(iii) Gaussian Low-Pass Filter (GLPF) and Gaussian High-Pass Filter (GHPF)*
> *Define the distance measure $D(u,v)$ and the cutoff frequency $D_0$.*

---

#### 💡 Master Answer

##### 1. Distance Measure Definition
For an $M \times N$ frequency rectangle centered at $(M/2, N/2)$, the Euclidean distance $D(u,v)$ from any point $(u,v)$ to the center is:
$$D(u,v) = \sqrt{\left( u - \frac{M}{2} \right)^2 + \left( v - \frac{N}{2} \right)^2}$$

##### 2. Low-Pass Filters (Smoothing / Noise Reduction)
Low-pass filters attenuate high frequencies while passing low frequencies unchanged:

* **Ideal Low-Pass Filter (ILPF):**
  $$H_{\text{ILPF}}(u,v) = \begin{cases} 1 & \text{if } D(u,v) \le D_0 \\ 0 & \text{if } D(u,v) > D_0 \end{cases}$$

* **Butterworth Low-Pass Filter (BLPF) of order $n$:**
  $$H_{\text{BLPF}}(u,v) = \frac{1}{1 + \left[ \frac{D(u,v)}{D_0} \right]^{2n}}$$

* **Gaussian Low-Pass Filter (GLPF):**
  $$H_{\text{GLPF}}(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}}$$

##### 3. High-Pass Filters (Sharpening / Edge Enhancement)
High-pass filters attenuate low frequencies and pass high frequencies. Every high-pass filter transfer function is exactly related to its corresponding low-pass filter by:
$$H_{\text{HP}}(u,v) = 1 - H_{\text{LP}}(u,v)$$

* **Ideal High-Pass Filter (IHPF):**
  $$H_{\text{IHPF}}(u,v) = \begin{cases} 0 & \text{if } D(u,v) \le D_0 \\ 1 & \text{if } D(u,v) > D_0 \end{cases}$$

* **Butterworth High-Pass Filter (BHPF) of order $n$:**
  $$H_{\text{BHPF}}(u,v) = \frac{1}{1 + \left[ \frac{D_0}{D(u,v)} \right]^{2n}}$$

* **Gaussian High-Pass Filter (GHPF):**
  $$H_{\text{GHPF}}(u,v) = 1 - e^{-\frac{D^2(u,v)}{2 D_0^2}}$$

---

### A.3 Ringing Artifacts & Gibbs Phenomenon Analysis

#### ❓ Master Question
> **Source:** Practice Question / Standard Examination Theory
> 
> *What is the 'ringing effect' in frequency-domain low-pass and high-pass filtering? Explain why Ideal filters produce severe ringing artifacts while Gaussian filters produce none. How does the Butterworth filter order $n$ affect ringing?*

---

#### 💡 Master Answer

##### 1. Cause of Ringing (The Convolution Theorem Connection)
Multiplying an image transform $F(u,v)$ by a filter $H(u,v)$ in the frequency domain is mathematically equivalent to convolving the spatial image $f(x,y)$ with the spatial filter kernel $h(x,y) = \mathcal{F}^{-1}[H(u,v)]$.

##### 2. Ideal Filter Analysis (Severe Ringing)
An Ideal Low-Pass Filter $H(u,v)$ is a perfectly sharp 2D rectangular box function with an instantaneous step discontinuity at $D(u,v) = D_0$.
* The inverse Fourier transform of a 2D rectangular box function is a 2D **sinc function**:
  $$h(x,y) \propto \frac{J_1(2\pi D_0 r)}{r}$$
* A sinc function consists of a main central lobe surrounded by concentric, decaying periodic side lobes (ripples).
* Convolving the image with these spatial side lobes causes visible **concentric ringing artifacts (ripples)** around sharp edges (known as the **Gibbs phenomenon**).

##### 3. Gaussian Filter Analysis (Zero Ringing)
The continuous Fourier transform of a Gaussian function is **another Gaussian function**:
$$\mathcal{F}^{-1}\left[ e^{-\frac{D^2(u,v)}{2 D_0^2}} \right] \propto e^{-2\pi^2 \sigma^2 (x^2 + y^2)}$$
* A spatial Gaussian kernel is completely smooth and positive everywhere, with **zero negative side lobes or ripples**.
* Therefore, Gaussian low-pass and high-pass filters produce **zero ringing artifacts**.

##### 4. Butterworth Filter Order Analysis
The Butterworth filter acts as a smooth transition between the Gaussian filter and the Ideal filter:
* For **low orders ($n = 1, 2$)**, the transfer function transition is smooth, and ringing is imperceptible.
* As the order **$n \to \infty$**, $H_{\text{BLPF}}(u,v)$ approaches the Ideal step function, causing spatial side lobes to emerge and **increasing ringing severity**.

---

### A.4 Spatial Sharpening Principles & Derivative Properties

#### ❓ Master Question
> **Source:** Practice Question / Lecture Notes
> 
> *Explain the principle of spatial image sharpening using digital differentiation. Compare the characteristics of first-order derivatives ($\frac{\partial f}{\partial x}$) and second-order derivatives ($\frac{\partial^2 f}{\partial x^2}$) along an intensity transition (step edge).*

---

#### 💡 Master Answer

##### 1. Principle of Digital Differentiation
Image blurring is equivalent to spatial integration (averaging pixel neighborhoods). Conversely, **image sharpening is achieved by spatial differentiation**, which highlights abrupt intensity transitions (edges, noise, fine detail) while suppressing constant or slowly varying background areas.

##### 2. 1D Discrete Derivative Definitions
For a 1D discrete intensity sequence $f(x)$:
* **First Derivative (Forward Difference):**
  $$\frac{\partial f}{\partial x} = f(x+1) - f(x)$$
* **Second Derivative (Central Difference):**
  $$\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$$

##### 3. Comparison of Derivative Responses Across a Step Edge

| Feature / Behavior | First-Order Derivative ($\frac{\partial f}{\partial x}$) | Second-Order Derivative ($\frac{\partial^2 f}{\partial x^2}$) |
| :--- | :--- | :--- |
| **Response in Constant Areas** | Zero ($0$) | Zero ($0$) |
| **Response at Edge Ramp Start** | Non-zero (positive or negative) | Non-zero |
| **Response along Constant Ramp** | Constant non-zero value | Zero ($0$) |
| **Response at Edge Ramp End** | Non-zero | Non-zero (opposite sign) |
| **Edge Structure Produced** | Thick, single-line response | Fine, **double-line response** |
| **Zero-Crossing Property** | No zero-crossing | **Crosses zero** at the center of an edge |
| **Fine Detail / Noise Sensitivity** | Moderately sensitive | **Highly sensitive** to fine details and noise |

---

### A.5 Unsharp Masking & High-Boost Filtering Mechanisms

#### ❓ Master Question
> **Source:** Practice Question / Standard Textbook Theory
> 
> *(a) Describe the 3-step process of Unsharp Masking in the spatial domain.*
> *(b) What is High-Boost Filtering? How does the amplification factor $A$ (or $k$) control the balance between edge enhancement and original background detail?*

---

#### 💡 Master Answer

##### (a) 3-Step Unsharp Masking Process
Unsharp masking has been used in publishing since the 1930s to sharpen images by subtracting a blurred (unsharp) version of an image from itself.

1. **Step 1 (Blur):** Create a blurred version $\bar{f}(x,y)$ of the original image $f(x,y)$ using a spatial smoothing filter (e.g., Gaussian or box filter).
2. **Step 2 (Mask Generation):** Subtract the blurred image from the original to generate the unsharp mask $g_{\text{mask}}(x,y)$:
   $$g_{\text{mask}}(x,y) = f(x,y) - \bar{f}(x,y)$$
3. **Step 3 (Recombination):** Add a weighted portion of the mask back to the original image:
   $$g(x,y) = f(x,y) + k \cdot g_{\text{mask}}(x,y) \quad (k \ge 0)$$

##### (b) High-Boost Filtering Analysis
* When **$k = 1$**, the process is standard **Unsharp Masking**.
* When **$k > 1$**, the process is termed **High-Boost Filtering**.

Alternatively, high-boost filtering is expressed using the amplification factor $A$:
$$g_{\text{HB}}(x,y) = A \cdot f(x,y) - \bar{f}(x,y) = (A - 1) f(x,y) + [f(x,y) - \bar{f}(x,y)] = (A - 1) f(x,y) + f_{\text{HP}}(x,y)$$

* **If $A = 1$:** The operation reduces to standard High-Pass Filtering ($g_{\text{HB}} = f_{\text{HP}}$), where constant background areas are reduced to zero (black).
* **If $A > 1$:** A portion of the original image $f(x,y)$ is re-injected into the output. This **retains the low-frequency background brightness and context** while boosting high-frequency edge contrast.

---

## 3. Category B: Comparative Analysis PYQs

### B.1 Spatial Domain vs. Frequency Domain Filtering

#### ❓ Master Question
> **Source:** Practice Question / Exam Review
> 
> *Compare and contrast Spatial Domain Filtering and Frequency Domain Filtering.*

---

#### 💡 Master Answer

| Feature / Attribute | Spatial Domain Filtering | Frequency Domain Filtering |
| :--- | :--- | :--- |
| **Core Operation** | Direct convolution of spatial pixel values with a 2D filter mask ($h \ast f$). | Pointwise multiplication of 2D DFT coefficients with a filter transfer function ($H \cdot F$). |
| **Mathematical Basis** | Direct spatial neighborhood processing. | Fourier Transform / Inverse Fourier Transform. |
| **Computational Complexity** | $\mathcal{O}(M N \cdot m n)$ for image $M \times N$ and mask $m \times n$. Very fast for small masks ($3 \times 3$). | $\mathcal{O}(M N \log_2(M N))$ using FFT. Faster for large spatial kernels. |
| **Filter Design Intuition** | Intuitive for local geometric/gradient operations (e.g., $3 \times 3$ Sobel, Laplacian). | Intuitive for global frequency manipulation (e.g., cutoff frequency $D_0$, notch filtering). |
| **Boundary Effects** | Requires explicit padding handling (zero-padding, edge replication). | Requires spectral padding ($P \ge 2M-1$) to prevent wrap-around spatial crosstalk. |
| **Artifacts** | Minimal global artifacts; localized mask boundary effects. | Ideal cutoffs cause global ringing (Gibbs phenomenon). |

---

### B.2 Low-Pass (Smoothing) vs. High-Pass (Sharpening) Filters

#### ❓ Master Question
> **Source:** Practice Question / Review Questions
> 
> *Distinguish between Low-Pass (Smoothing) and High-Pass (Sharpening) filters in both spatial and frequency domains.*

---

#### 💡 Master Answer

| Parameter / Aspect | Low-Pass Filters (LPF) | High-Pass Filters (HPF) |
| :--- | :--- | :--- |
| **Primary Objective** | Image smoothing, noise attenuation, blurring. | Image sharpening, edge enhancement, detail extraction. |
| **Frequencies Passed** | Retains low spatial frequencies ($D(u,v) \le D_0$). | Retains high spatial frequencies ($D(u,v) > D_0$). |
| **Frequencies Blocked** | Attenuates high frequencies (edges, fine noise). | Attenuates low frequencies (smooth background, DC component). |
| **Spatial Mask Characteristics** | All mask coefficients are **positive**; sum of mask weights $= 1$ (normalized). | Center weight is **positive**, surrounding weights are **negative**; sum of weights $= 0$. |
| **DC Component Effect** | Preserves average background intensity $F(0,0)$. | Sets DC component $F(0,0)$ to $0$, turning constant backgrounds black. |
| **Output Image Appearance** | Blurred, smooth, reduced noise, softer edges. | Dark background with highlighted bright edges and fine lines. |

---

### B.3 Ideal vs. Butterworth vs. Gaussian Frequency Filters

#### ❓ Master Question
> **Source:** Practice Question / Comprehensive Review
> 
> *Compare Ideal, Butterworth, and Gaussian low-pass/high-pass frequency filters in terms of transfer function, smoothness, and ringing artifacts.*

---

#### 💡 Master Answer

| Filter Type | Transfer Function Profile | Cutoff Transition | Ringing Artifacts (Gibbs Phenomenon) | Physical Realizability |
| :--- | :--- | :--- | :--- | :--- |
| **Ideal (ILPF / IHPF)** | Discontinuous step function | Perfectly sharp / abrupt at $D_0$ | **Severe ringing** due to spatial sinc side lobes | Not physically realizable in hardware |
| **Butterworth (BLPF / BHPF)** | Continuous smooth curve controlled by order $n$ | Smooth for low $n$; sharp for large $n$ | **No ringing for $n=1,2$**; mild ringing for $n \ge 5$ | Realizable in analog/digital circuits |
| **Gaussian (GLPF / GHPF)** | Completely smooth exponential Gaussian curve | Gradual / smooth transition | **Zero ringing** (spatial inverse is also Gaussian) | Realizable; benchmark smooth filter |

---

### B.4 High-Pass vs. Laplacian vs. High-Boost Spatial Filters

#### ❓ Master Question
> **Source:** Practice Question / Exam Review
> 
> *Compare High-Pass, Laplacian, and High-Boost spatial filters.*

---

#### 💡 Master Answer

| Characteristic | High-Pass Spatial Filter | Laplacian Filter | High-Boost Spatial Filter |
| :--- | :--- | :--- | :--- |
| **Derivative Order** | First or second derivative approximation | Isotropic **second derivative** ($\nabla^2 f$) | Original image + weighted High-Pass component |
| **Sum of Mask Weights** | Sum $= 0$ | Sum $= 0$ | Sum $= A \ge 1$ (Sum $= 1$ when $A=1$) |
| **Background Preservation** | Eliminates background (becomes black) | Eliminates background (becomes zero/gray) | **Preserves background illumination** and context |
| **Center Weight Formula** | Positive center, negative neighbors | Center $= \pm 4$ or $\pm 8$; sum $= 0$ | Center $w_{\text{center}} = (A - 1) + 4$ or $(A - 1) + 8$ |
| **Primary Application** | Edge isolation | Fine detail and edge enhancement | Sharpening low-contrast or blurred images |

---

## 4. Category C: Mathematical Derivations & Mask Formulations

### C.1 2D Spatial Laplacian Mask Derivation (4-Way & 8-Way)

#### ❓ Master Question
> **Source:** AKTU 2017–18 (Q.2.26 / Q.5b, 10 Marks) | Practice Question
> 
> *(a) Derive the 2D spatial discrete Laplacian operator from continuous partial derivatives.*
> *(b) Show how the 4-way and 8-way isotropic Laplacian masks are constructed.*

---

#### 💡 Master Answer

##### (a) Derivation of 2D Discrete Laplacian
The 2D continuous Laplacian operator $\nabla^2 f$ is defined as the sum of second-order partial derivatives:
$$\nabla^2 f(x,y) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$

Using the 1D discrete central difference approximation for the second derivative:
$$\frac{\partial^2 f}{\partial x^2} \approx f(x+1, y) + f(x-1, y) - 2f(x,y)$$
$$\frac{\partial^2 f}{\partial y^2} \approx f(x, y+1) + f(x, y-1) - 2f(x,y)$$

Summing both partial derivatives gives the **4-Way Discrete Laplacian**:
$$\nabla^2 f(x,y) = [f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1)] - 4f(x,y)$$

##### (b) 4-Way and 8-Way Mask Formulations

**1. Standard 4-Way Laplacian Mask (Negative Center):**
```
  0   1   0
  1  -4   1
  0   1   0
```

**2. Standard 4-Way Laplacian Mask (Positive Center):**
```
  0  -1   0
 -1   4  -1
  0  -1   0
```

**3. Isotropic 8-Way Laplacian Mask (Includes Diagonals):**
Adding diagonal second derivatives $\frac{\partial^2 f}{\partial d1^2} + \frac{\partial^2 f}{\partial d2^2}$ yields:
```
  1   1   1
  1  -8   1
  1   1   1
   (or with positive center: center = +8, all neighbors = -1)
```

##### (c) Image Enhancement Formula
To sharpen an image using the Laplacian:
* If the mask has a **negative center** ($-4$ or $-8$):
  $$g(x,y) = f(x,y) - \nabla^2 f(x,y)$$
* If the mask has a **positive center** ($+4$ or $+8$):
  $$g(x,y) = f(x,y) + \nabla^2 f(x,y)$$

Substituting the negative center mask into $g(x,y) = f(x,y) - \nabla^2 f(x,y)$:
$$g(x,y) = f(x,y) - [f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1) - 4f(x,y)] = 5f(x,y) - f(x+1,y) - f(x-1,y) - f(x,y+1) - f(x,y-1)$$

This yields the **Composite Sharpening Mask**:
```
  0  -1   0
 -1   5  -1
  0  -1   0
```

---

### C.2 High-Boost Spatial Filter Mask Derivation ($A$ Parameter)

#### ❓ Master Question
> **Source:** Practice Question / Exam Formulation
> 
> *Derive the $3 \times 3$ spatial filter mask for High-Boost Filtering with amplification factor $A$ for both 4-neighbor and 8-neighbor Laplacian formulations.*

---

#### 💡 Master Answer

##### Derivation
High-boost filtering in the spatial domain is defined as:
$$g_{\text{HB}}(x,y) = A \cdot f(x,y) - \bar{f}(x,y)$$

Where $\bar{f}(x,y)$ is the smoothed image obtained by neighborhood averaging. Alternatively, using the high-pass image $f_{\text{HP}}(x,y)$:
$$g_{\text{HB}}(x,y) = (A - 1) f(x,y) + f_{\text{HP}}(x,y)$$

##### 1. 4-Neighbor High-Boost Mask Derivation
Using the 4-neighbor High-Pass Mask $W_{\text{HP}} = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 0 \end{bmatrix}$:
$$W_{\text{HB}} = (A - 1) \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 0 \\ -1 & A + 3 & -1 \\ 0 & -1 & 0 \end{bmatrix}$$

##### 2. 8-Neighbor High-Boost Mask Derivation
Using the 8-neighbor High-Pass Mask $W_{\text{HP}} = \begin{bmatrix} -1 & -1 & -1 \\ -1 & 8 & -1 \\ -1 & -1 & -1 \end{bmatrix}$:
$$W_{\text{HB}} = \begin{bmatrix} -1 & -1 & -1 \\ -1 & A + 7 & -1 \\ -1 & -1 & -1 \end{bmatrix}$$

* **Verification:** When $A = 1$, $w_{\text{center}} = 1 + 3 = 4$ (or $1 + 7 = 8$), reducing to standard high-pass filtering.

---

### C.3 Frequency Domain High-Pass & High-Boost Transfer Function Derivation

#### ❓ Master Question
> **Source:** Practice Question / Lecture Notes
> 
> *Derive the frequency-domain transfer function $H_{\text{HB}}(u,v)$ for High-Boost Filtering in terms of a Low-Pass transfer function $H_{\text{LP}}(u,v)$ and amplification parameter $k$ (or $A$).*

---

#### 💡 Master Answer

##### Derivation
In the frequency domain, the unsharp mask $G_{\text{mask}}(u,v)$ is computed using a low-pass filter $H_{\text{LP}}(u,v)$:
$$G_{\text{mask}}(u,v) = F(u,v) - F_{\text{LP}}(u,v) = F(u,v) - H_{\text{LP}}(u,v) F(u,v) = [1 - H_{\text{LP}}(u,v)] F(u,v)$$

The high-boost filtered image $G_{\text{HB}}(u,v)$ is given by:
$$G_{\text{HB}}(u,v) = F(u,v) + k \cdot G_{\text{mask}}(u,v) \quad (k \ge 1)$$

Substitute $G_{\text{mask}}(u,v)$:
$$G_{\text{HB}}(u,v) = F(u,v) + k [1 - H_{\text{LP}}(u,v)] F(u,v) = \left\{ 1 + k [1 - H_{\text{LP}}(u,v)] \right\} F(u,v)$$

Since $1 - H_{\text{LP}}(u,v) = H_{\text{HP}}(u,v)$:
$$G_{\text{HB}}(u,v) = [1 + k \cdot H_{\text{HP}}(u,v)] F(u,v)$$

$$\therefore H_{\text{HB}}(u,v) = 1 + k \cdot H_{\text{HP}}(u,v) = (1 + k) - k \cdot H_{\text{LP}}(u,v)$$

Alternatively, substituting $A = 1 + k$:
$$H_{\text{HB}}(u,v) = (A - 1) + H_{\text{HP}}(u,v) = A - H_{\text{LP}}(u,v)$$

---

### C.4 Frequency Domain Laplacian Transfer Function Derivation

#### ❓ Master Question
> **Source:** AKTU 2014–15 (Q.2.25, 5 Marks)
> 
> *Derive the frequency-domain filter transfer function $H_{\text{Lap}}(u,v)$ for the Laplacian operator.*

---

#### 💡 Master Answer

##### Derivation
Recall the Fourier Transform derivative property:
$$\mathcal{F}\left[ \frac{\partial^n f(x,y)}{\partial x^n} \right] = (j 2\pi u)^n F(u,v)$$

For the second-order partial derivatives ($n = 2$):
$$\mathcal{F}\left[ \frac{\partial^2 f(x,y)}{\partial x^2} \right] = (j 2\pi u)^2 F(u,v) = -4\pi^2 u^2 F(u,v)$$
$$\mathcal{F}\left[ \frac{\partial^2 f(x,y)}{\partial y^2} \right] = (j 2\pi v)^2 F(u,v) = -4\pi^2 v^2 F(u,v)$$

Summing both components to obtain the 2D Fourier transform of $\nabla^2 f(x,y)$:
$$\mathcal{F}[\nabla^2 f(x,y)] = \mathcal{F}\left[ \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} \right] = -4\pi^2 (u^2 + v^2) F(u,v)$$

Thus, the uncentered frequency-domain Laplacian transfer function is:
$$H_{\text{Lap}}(u,v) = -4\pi^2 (u^2 + v^2)$$

When centered at $(M/2, N/2)$ using distance $D(u,v) = \sqrt{(u - M/2)^2 + (v - N/2)^2}$:
$$H_{\text{Lap}}(u,v) = -4\pi^2 D^2(u,v)$$

---

## 5. Category D: Step-by-Step Worked Numerical Problems

### Numerical 1: $4 \times 4$ Image Step-by-Step Frequency Domain Filtering ($D_0 = 0.5$)

#### ❓ Problem Statement
> **Source:** IVP Class Test / M2 Lecture Notes (`Updated_IVP_Frequency_Domain_Notes.pdf`)
> 
> **Given:** A $4 \times 4$ spatial domain image $f(x,y)$:
> $$f(x,y) = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 \end{bmatrix}$$
> Perform Ideal Low-Pass Filtering in the frequency domain with cutoff frequency $D_0 = 0.5$. Show step-by-step procedure including centered matrix, DFT coefficients, distance matrix, filter response, pointwise multiplication, and IDFT result.

---

#### 🛠️ Solving Approach & Assumptions
* **Indexing:** $x, u \in \{0, 1, 2, 3\}$ and $y, v \in \{0, 1, 2, 3\}$. Image size $M = 4, N = 4$.
* **Center Coordinates:** $(M/2, N/2) = (2, 2)$.
* **Boundary Handling:** Exact 2D matrix transformation.

---

#### ✏️ Step-by-Step Solution

##### Step 1: Center the Input Image by Multiplying by $(-1)^{x+y}$
$$(-1)^{x+y} = \begin{bmatrix} +1 & -1 & +1 & -1 \\ -1 & +1 & -1 & +1 \\ +1 & -1 & +1 & -1 \\ -1 & +1 & -1 & +1 \end{bmatrix}$$

Pointwise multiplication $f_c(x,y) = f(x,y) \cdot (-1)^{x+y}$:
$$f_c(x,y) = \begin{bmatrix} 1(1) & 0(-1) & 1(1) & 0(-1) \\ 1(-1) & 0(1) & 1(-1) & 0(1) \\ 1(1) & 0(-1) & 1(1) & 0(-1) \\ 1(-1) & 0(1) & 1(-1) & 0(1) \end{bmatrix} = \begin{bmatrix} 1 & 0 & 1 & 0 \\ -1 & 0 & -1 & 0 \\ 1 & 0 & 1 & 0 \\ -1 & 0 & -1 & 0 \end{bmatrix}$$

##### Step 2: Compute 2D DFT $F(u,v)$ of Centered Image $f_c(x,y)$
Notice that every row of $f_c(x,y)$ is identical: $r = \begin{bmatrix} 1 & 0 & 1 & 0 \end{bmatrix}$ (repeated for $x=0,2$) and $-r = \begin{bmatrix} -1 & 0 & -1 & 0 \end{bmatrix}$ (for $x=1,3$).

* Compute 1D 4-point DFT of row $r = [1, 0, 1, 0]$:
  $$R(v) = \sum_{y=0}^3 r(y) e^{-j \frac{2\pi v y}{4}} = 1 + 1 \cdot e^{-j \pi v}$$
  * For $v=0$: $R(0) = 1 + 1 = 2$
  * For $v=1$: $R(1) = 1 + e^{-j\pi} = 1 - 1 = 0$
  * For $v=2$: $R(2) = 1 + e^{-j 2\pi} = 1 + 1 = 2$
  * For $v=3$: $R(3) = 1 + e^{-j 3\pi} = 1 - 1 = 0$
  * Row 1D DFT result: $R = \begin{bmatrix} 2 & 0 & 2 & 0 \end{bmatrix}$

* Apply 1D DFT along columns across $x = [0, 1, 2, 3]$ for column pattern $c = [1, -1, 1, -1]^T$:
  $$C(u) = \sum_{x=0}^3 c(x) e^{-j \frac{2\pi u x}{4}} = 1 - e^{-j \frac{\pi u}{2}} + e^{-j \pi u} - e^{-j \frac{3\pi u}{2}}$$
  * For $u=0$: $C(0) = 1 - 1 + 1 - 1 = 0$
  * For $u=1$: $C(1) = 1 - (-j) + (-1) - (j) = 0$
  * For $u=2$: $C(2) = 1 - (-1) + 1 - (-1) = 4$
  * For $u=3$: $C(3) = 1 - (j) + (-1) - (-j) = 0$

* Combining row and column transforms via separability:
  $$F(u,v) = C(u) \otimes R(v) = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 8 & 0 & 8 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

##### Step 3: Compute Euclidean Distance Matrix $D(u,v)$ from Center $(2,2)$
$$D(u,v) = \sqrt{(u-2)^2 + (v-2)^2}$$

For $u, v \in \{0, 1, 2, 3\}$:
$$D(u,v) = \begin{bmatrix} \sqrt{8} & \sqrt{5} & 2 & \sqrt{5} \\ \sqrt{5} & \sqrt{2} & 1 & \sqrt{2} \\ 2 & 1 & 0 & 1 \\ \sqrt{5} & \sqrt{2} & 1 & \sqrt{2} \end{bmatrix} \approx \begin{bmatrix} 2.83 & 2.24 & 2.00 & 2.24 \\ 2.24 & 1.41 & 1.00 & 1.41 \\ 2.00 & 1.00 & 0.00 & 1.00 \\ 2.24 & 1.41 & 1.00 & 1.41 \end{bmatrix}$$

##### Step 4: Construct Ideal Low-Pass Filter Response $H(u,v)$ ($D_0 = 0.5$)
$$H(u,v) = \begin{cases} 1 & \text{if } D(u,v) \le 0.5 \\ 0 & \text{if } D(u,v) > 0.5 \end{cases}$$

Looking at $D(u,v)$, only the center element $(2,2)$ has $D(2,2) = 0 \le 0.5$. All other entries exceed $0.5$:
$$H(u,v) = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

##### Step 5: Pointwise Multiplication $G(u,v) = F(u,v) \cdot H(u,v)$
$$G(u,v) = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 8 & 0 & 8 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \cdot \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 8 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

##### Step 6: Compute Inverse 2D DFT $g_c(x,y) = \mathcal{F}^{-1}[G(u,v)]$
$G(u,v)$ has a single non-zero entry at $(u,v) = (2,2)$ with value $8$.
Using the IDFT formula:
$$g_c(x,y) = \frac{1}{M N} \sum_{u=0}^{3} \sum_{v=0}^{3} G(u,v) e^{j 2\pi \left( \frac{ux}{4} + \frac{vy}{4} \right)} = \frac{1}{16} \cdot 8 \cdot e^{j 2\pi \left( \frac{2x}{4} + \frac{2y}{4} \right)} = 0.5 \cdot e^{j \pi (x+y)} = 0.5 \cdot (-1)^{x+y}$$

For all $x, y \in \{0, 1, 2, 3\}$:
$$g_c(x,y) = \begin{bmatrix} 0.5 & -0.5 & 0.5 & -0.5 \\ -0.5 & 0.5 & -0.5 & 0.5 \\ 0.5 & -0.5 & 0.5 & -0.5 \\ -0.5 & 0.5 & -0.5 & 0.5 \end{bmatrix}$$

##### Step 7: Decentralize Result $g(x,y) = g_c(x,y) \cdot (-1)^{x+y}$
$$g(x,y) = \begin{bmatrix} 0.5 & -0.5 & 0.5 & -0.5 \\ -0.5 & 0.5 & -0.5 & 0.5 \\ 0.5 & -0.5 & 0.5 & -0.5 \\ -0.5 & 0.5 & -0.5 & 0.5 \end{bmatrix} \cdot \begin{bmatrix} +1 & -1 & +1 & -1 \\ -1 & +1 & -1 & +1 \\ +1 & -1 & +1 & -1 \\ -1 & +1 & -1 & +1 \end{bmatrix} = \begin{bmatrix} 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \end{bmatrix}$$

#### 🎯 Final Output Matrix
$$g(x,y) = \begin{bmatrix} 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \\ 0.5 & 0.5 & 0.5 & 0.5 \end{bmatrix}$$

**Physical Interpretation:** Extremely severe low-pass filtering ($D_0 = 0.5$) retains only the centered component, completely removing spatial vertical transitions and blurring the image into a uniform average intensity of $0.5$.

---

### Numerical 2: 2D Spatial Laplacian Convolution on $5 \times 5$ Edge Image

#### ❓ Problem Statement
> **Source:** NMIMS Semester V 2022–23 (Q.4a, 10 Marks) | AKTU 2014–15 (Q.2.22, 5 Marks)
> 
> **Given:** A $5 \times 5$ image matrix $f(x,y)$ containing a vertical step edge:
> $$f(x,y) = \begin{bmatrix} 80 & 80 & 40 & 40 & 40 \\ 80 & 80 & 40 & 40 & 40 \\ 80 & 80 & 40 & 40 & 40 \\ 80 & 80 & 40 & 40 & 40 \\ 80 & 80 & 40 & 40 & 40 \end{bmatrix}$$
> Apply the $3 \times 3$ Laplacian Filter $W = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 0 \end{bmatrix}$ to compute the Laplacian response $\nabla^2 f(x,y)$ for all interior pixels. Comment on the output.

---

#### 🛠️ Solving Approach & Assumptions
* **Neighborhood:** $3 \times 3$ spatial convolution.
* **Boundary Handling:** Ignore outer border pixels ($x=0, 4$ and $y=0, 4$) or evaluate only interior submatrix ($x \in \{1,2,3\}, y \in \{1,2,3\}$).

---

#### ✏️ Step-by-Step Solution

Let us evaluate the Laplacian $\nabla^2 f(x,y) = 4 f(x,y) - [f(x-1,y) + f(x+1,y) + f(x,y-1) + f(x,y+1)]$ for interior columns $y = 1, 2, 3$:

##### Column 1 ($y = 1$, intensity $= 80$):
Neighborhood centered at $(x, 1)$:
$$\text{Center} = 80, \quad \text{Left}(y=0) = 80, \quad \text{Right}(y=2) = 40, \quad \text{Top}(x-1) = 80, \quad \text{Bottom}(x+1) = 80$$
$$\nabla^2 f(x,1) = 4(80) - [80 + 80 + 80 + 40] = 320 - 280 = +40$$

##### Column 2 ($y = 2$, intensity $= 40$):
Neighborhood centered at $(x, 2)$:
$$\text{Center} = 40, \quad \text{Left}(y=1) = 80, \quad \text{Right}(y=3) = 40, \quad \text{Top}(x-1) = 40, \quad \text{Bottom}(x+1) = 40$$
$$\nabla^2 f(x,2) = 4(40) - [40 + 40 + 80 + 40] = 160 - 200 = -40$$

##### Column 3 ($y = 3$, intensity $= 40$):
Neighborhood centered at $(x, 3)$:
$$\text{Center} = 40, \quad \text{Left}(y=2) = 40, \quad \text{Right}(y=4) = 40, \quad \text{Top}(x-1) = 40, \quad \text{Bottom}(x+1) = 40$$
$$\nabla^2 f(x,3) = 4(40) - [40 + 40 + 40 + 40] = 160 - 160 = 0$$

##### Column 0 ($y = 0$, intensity $= 80$, constant region):
For uniform region: $\nabla^2 f(x,0) = 0$.

---

#### 🎯 Output Laplacian Matrix $\nabla^2 f(x,y)$ (Interior $3 \times 3$)
$$\nabla^2 f = \begin{bmatrix} \text{Border} & +40 & -40 & 0 & \text{Border} \\ \text{Border} & +40 & -40 & 0 & \text{Border} \\ \text{Border} & +40 & -40 & 0 & \text{Border} \end{bmatrix}$$

#### 🎯 Sharpened Image Matrix $g(x,y) = f(x,y) + \nabla^2 f(x,y)$
$$g(x,y) = \begin{bmatrix} \text{Border} & 80+40=120 & 40-40=0 & 40+0=40 & \text{Border} \\ \text{Border} & 120 & 0 & 40 & \text{Border} \\ \text{Border} & 120 & 0 & 40 & \text{Border} \end{bmatrix}$$

#### 📝 Analysis & Observation
1. The Laplacian produces a **positive pulse ($+40$) on the darker side of the edge boundary** and a **negative pulse ($-40$) on the lighter side**.
2. Adding $\nabla^2 f$ back to $f(x,y)$ enhances local contrast by making the bright side brighter ($80 \to 120$) and the dark side darker ($40 \to 0$), demonstrating **edge sharpening via overshooting/undershooting**.

---

### Numerical 3: 1D Scanline First and Second Derivative Calculation

#### ❓ Problem Statement
> **Source:** Practice Question / Exam Review
> 
> **Given:** A 1D scanline pixel intensity profile across a step edge:
> $$f(x) = [50, 50, 50, 50, 100, 100, 100, 100]$$
> Calculate the First Derivative $\frac{\partial f}{\partial x}$ and Second Derivative $\frac{\partial^2 f}{\partial x^2}$. Identify the zero-crossing position.

---

#### ✏️ Step-by-Step Solution

##### 1. First Derivative: $\frac{\partial f}{\partial x} = f(x+1) - f(x)$
* $x=0$: $f(1) - f(0) = 50 - 50 = 0$
* $x=1$: $f(2) - f(1) = 50 - 50 = 0$
* $x=2$: $f(3) - f(2) = 50 - 50 = 0$
* $x=3$: $f(4) - f(3) = 100 - 50 = +50$
* $x=4$: $f(5) - f(4) = 100 - 100 = 0$
* $x=5$: $f(6) - f(5) = 100 - 100 = 0$
* $x=6$: $f(7) - f(6) = 100 - 100 = 0$

$$\frac{\partial f}{\partial x} = [0, 0, 0, +50, 0, 0, 0]$$

##### 2. Second Derivative: $\frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$
* $x=1$: $f(2) + f(0) - 2f(1) = 50 + 50 - 100 = 0$
* $x=2$: $f(3) + f(1) - 2f(2) = 50 + 50 - 100 = 0$
* $x=3$: $f(4) + f(2) - 2f(3) = 100 + 50 - 100 = +50$
* $x=4$: $f(5) + f(3) - 2f(4) = 100 + 50 - 200 = -50$
* $x=5$: $f(6) + f(4) - 2f(5) = 100 + 100 - 200 = 0$
* $x=6$: $f(7) + f(5) - 2f(6) = 100 + 100 - 200 = 0$

$$\frac{\partial^2 f}{\partial x^2} = [0, 0, +50, -50, 0, 0]$$

#### 🎯 Summary Table

| Index $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$f(x)$** | $50$ | $50$ | $50$ | $50$ | $100$ | $100$ | $100$ | $100$ |
| **$\frac{\partial f}{\partial x}$** | $0$ | $0$ | $0$ | **$+50$** | $0$ | $0$ | $0$ | — |
| **$\frac{\partial^2 f}{\partial x^2}$** | — | $0$ | $0$ | **$+50$** | **$-50$** | $0$ | $0$ | — |

* **Zero-Crossing:** The second derivative transitions directly from **$+50$ at $x=3$** to **$-50$ at $x=4$**, establishing a sharp zero-crossing at the center of the step edge between pixels $3$ and $4$.

---

### Numerical 4: High-Boost Spatial Filtering with Amplification Factor $A = 1.5$

#### ❓ Problem Statement
> **Source:** Practice Question / Exam Numerical
> 
> **Given:** A $3 \times 3$ image neighborhood $f(x,y)$:
> $$f(x,y) = \begin{bmatrix} 10 & 20 & 10 \\ 20 & 80 & 20 \\ 10 & 20 & 10 \end{bmatrix}$$
> Perform High-Boost Spatial Filtering with amplification parameter $A = 1.5$ using an 8-neighbor Laplacian formulation.

---

#### ✏️ Step-by-Step Solution

##### Step 1: Construct the 8-Neighbor High-Boost Spatial Filter Mask
For an 8-neighbor formulation, the High-Boost mask $W_{\text{HB}}$ is:
$$W_{\text{HB}} = \begin{bmatrix} -1 & -1 & -1 \\ -1 & A + 7 & -1 \\ -1 & -1 & -1 \end{bmatrix}$$

Substitute $A = 1.5$:
$$\text{Center Weight} = 1.5 + 7 = 8.5$$
$$W_{\text{HB}} = \begin{bmatrix} -1 & -1 & -1 \\ -1 & 8.5 & -1 \\ -1 & -1 & -1 \end{bmatrix}$$

##### Step 2: Convolve Mask $W_{\text{HB}}$ with Image Neighborhood $f(x,y)$
$$g_{\text{HB}}(x,y) = \sum_{i=-1}^1 \sum_{j=-1}^1 W_{\text{HB}}(i,j) \cdot f(x+i, y+j)$$

$$\text{Positive Center Contribution} = 8.5 \times 80 = 680$$

$$\text{Sum of 8 Neighbor Pixels} = 10 + 20 + 10 + 20 + 20 + 10 + 20 + 10 = 120$$
$$\text{Negative Neighbors Contribution} = -1 \times 120 = -120$$

$$g_{\text{HB}}(x,y) = 680 - 120 = 560$$

##### Step 3: Check Scaling / Dynamic Range
In standard 8-bit unsigned integer representations ($[0, 255]$), $560$ exceeds $255$.
* **Clipped Output:** $g_{\text{clipped}} = \min(255, 560) = 255$.
* **Unclipped Floating Point Value:** $560$.

---

### Numerical 5: High-Boost Frequency Transfer Function Numerical Evaluation

#### ❓ Problem Statement
> **Source:** Practice Question / Frequency Domain Sharpening
> 
> **Given:** An $M \times N$ image processed in the frequency domain using a Gaussian Low-Pass Filter with $D_0 = 20$. Compute the High-Boost Filter Transfer Function $H_{\text{HB}}(u,v)$ for a frequency component located at distance $D(u,v) = 30$ from the center, using amplification factor $A = 1.2$.

---

#### ✏️ Step-by-Step Solution

##### Step 1: Compute GLPF Value $H_{\text{GLPF}}(u,v)$
$$H_{\text{GLPF}}(u,v) = e^{-\frac{D^2(u,v)}{2 D_0^2}}$$

Substitute $D(u,v) = 30$ and $D_0 = 20$:
$$H_{\text{GLPF}} = e^{-\frac{30^2}{2(20^2)}} = e^{-\frac{900}{800}} = e^{-1.125} \approx 0.3247$$

##### Step 2: Compute GHPF Value $H_{\text{GHPF}}(u,v)$
$$H_{\text{GHPF}}(u,v) = 1 - H_{\text{GLPF}}(u,v) = 1 - 0.3247 = 0.6753$$

##### Step 3: Compute High-Boost Transfer Function $H_{\text{HB}}(u,v)$
Using formula $H_{\text{HB}}(u,v) = (A - 1) + H_{\text{GHPF}}(u,v)$:
$$H_{\text{HB}}(u,v) = (1.2 - 1) + 0.6753 = 0.2 + 0.6753 = 0.8753$$

Alternatively using $H_{\text{HB}}(u,v) = A - H_{\text{GLPF}}(u,v)$:
$$H_{\text{HB}}(u,v) = 1.2 - 0.3247 = 0.8753$$

#### 🎯 Final Result
$$H_{\text{HB}}(u,v) = 0.8753$$

---

## 6. Category E: Multi-Part Combined PYQs (Flagged Out-of-Scope Parts)

#### ❓ Historical Multi-Part Paper Question
> **Source:** AKTU 2018–19 / Solved Paper 2014–15
> 
> **Original Question Wording:**
> *"Q.3: Attempt any two parts of the following:*
> *(a) Explain piecewise linear transformation and histogram equalization with suitable examples. (10 Marks)*
> *(b) Explain the process of filtering in the frequency domain. Discuss low-pass and high-pass frequency domain filters. (10 Marks)"*

---

#### 🛡️ Scope Isolation & Exam Answer Strategy
* 🚩 **Out-of-Scope Part (a):** Piecewise linear transformations and histogram equalization belong to Point Processing & Spatial Enhancement, which are **excluded from the M2 Scope**.
* ✅ **In-Scope Part (b):** Fully answered under **Section 2, Category A.1 & A.2** of this document.

---

## 7. Section 7: Last-Minute Exam Mastery Checklist

Before entering your M2 examination, ensure you can confidently answer and derive every item on this checklist:

### 1. Core Formulas & Transfer Functions
* [ ] Distance formula: $D(u,v) = \sqrt{(u - M/2)^2 + (v - N/2)^2}$
* [ ] ILPF / IHPF step function definitions
* [ ] BLPF formula: $H(u,v) = \frac{1}{1 + [D(u,v)/D_0]^{2n}}$ and BHPF conversion
* [ ] GLPF formula: $H(u,v) = e^{-D^2/2D_0^2}$ and GHPF conversion
* [ ] High-Boost spatial mask formula: $w_{\text{center}} = (A - 1) + 4$ or $(A - 1) + 8$
* [ ] Frequency High-Boost formula: $H_{\text{HB}}(u,v) = A - H_{\text{LP}}(u,v)$

### 2. Key Derivations & Proofs
* [ ] Proof of centering property: $\mathcal{F}[f(x,y)(-1)^{x+y}] = F(u - M/2, v - N/2)$
* [ ] Derivation of 2D discrete Laplacian $\nabla^2 f$ from central differences
* [ ] Derivation of spatial High-Boost filter mask from $A \cdot f - \bar{f}$
* [ ] Frequency domain Laplacian transfer function $H_{\text{Lap}}(u,v) = -4\pi^2 D^2(u,v)$

### 3. Numerical & Computational Readiness
* [ ] Can perform $4 \times 4$ DFT/IDFT matrix multiplication and distance calculations
* [ ] Can perform 2D $3 \times 3$ spatial matrix convolution for Laplacian and High-Boost masks
* [ ] Can calculate 1D 1st and 2nd derivatives and locate zero-crossings
* [ ] Can handle dynamic range clipping ($[0, 255]$) for sharpened outputs

---
