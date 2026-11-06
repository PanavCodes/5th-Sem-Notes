# Unit 7: Colour Image Processing — Past Year Questions (PYQs) & Exam Solutions

---

## 1. Overview of Unit 7 Syllabus and Exam Weightage

Unit 7 covers Colour Image Processing, focusing on color perception, color models (RGB, CMY, CMYK, HSI, HSV, YUV), color transformations, vector-based color slicing, and intensity-decoupled color histogram equalization.

### Course Outcome Mapping

* **CO1:** Explain the fundamentals of digital images, including color models.
* **CO2:** Apply color transformations, color slicing, and histogram processing for color image enhancement.

### Exam Distribution & Weightage

| Question Type | Topics Covered | Typical Marks |
| :--- | :--- | :--- |
| **Numerical Problems** | RGB to HSI conversion, RGB to CMY/CMYK conversion, Color Slicing thresholds | 5 – 10 Marks |
| **Theory & Derivations** | YUV color space in video compression, Additive vs. Subtractive color mixing | 5 – 8 Marks |
| **Comparative Analysis** | RGB vs. CMYK vs. HSI vs. HSV vs. YUV matrix comparisons, Chroma Subsampling ($`J:a:b`$) | 5 – 10 Marks |
| **Algorithmic Workflows** | Histogram Equalization of color images (RGB vs. HSI/YUV decoupling) | 5 – 8 Marks |

---

## 2. PYQ 1: RGB to HSI Color Model Conversion Numerical

### Exam Context

* **Marks:** 10 Marks
* **Frequency:** High (Appears frequently in Term End Exams)

### Question Statement

Given an unnormalized RGB pixel vector $\mathbf{z}_{\text{RGB}} = [100, 200, 50]^T$ where component values range from $0$ to $255$:

1. Compute the Intensity ($I$).
2. Compute the Saturation ($S$).
3. Compute the Hue angle ($\theta$) and the final Hue value ($H$).
4. Express the final HSI representation of the pixel.

---

### Step-by-Step Solution

#### Step 1: State the HSI Conversion Formulas

For an RGB color vector with components $R$, $G$, $B \in [0, 255]$:

1. **Intensity** ($I$):

```math
I = \frac{R + G + B}{3}
```

2. **Saturation** ($S$):

```math
S = 1 - \frac{3}{R + G + B} \cdot \min(R, G, B)
```

3. **Hue Angle** ($\theta$):

```math
\theta = \cos^{-1} \left[ \frac{0.5 \cdot \left( (R - G) + (R - B) \right)}{\sqrt{(R - G)^2 + (R - B)(G - B)}} \right]
```

4. **Final Hue** ($H$):

```math
H = \begin{cases}
\theta & \text{if } B \le G \\
360^\circ - \theta & \text{if } B > G
\end{cases}
```

---

#### Step 2: Compute Intensity ($I$)

Substitute $R = 100$, $G = 200$, and $B = 50$:

```math
I = \frac{100 + 200 + 50}{3} = \frac{350}{3} = 116.6667
```

* **Normalized Intensity:** $I_{\text{norm}} = \frac{116.6667}{255} = 0.4575$.

---

#### Step 3: Compute Saturation ($S$)

Identify $\min(R, G, B) = \min(100, 200, 50) = 50$:

```math
S = 1 - \frac{3}{100 + 200 + 50} \cdot 50
```

```math
S = 1 - \frac{3}{350} \cdot 50 = 1 - \frac{150}{350} = 1 - 0.4286 = 0.5714
```

---

#### Step 4: Compute Hue Angle ($\theta$) and Final Hue ($H$)

1. **Calculate Differences:**
   * $R - G = 100 - 200 = -100$
   * $R - B = 100 - 50 = 50$
   * $G - B = 200 - 50 = 150$

2. **Calculate Numerator:**

```math
\text{Numerator} = 0.5 \cdot \left[ (-100) + 50 \right] = 0.5 \cdot (-50) = -25.0000
```

3. **Calculate Denominator:**

```math
\text{Denominator} = \sqrt{(-100)^2 + (50)(150)} = \sqrt{10000 + 7500} = \sqrt{17500} = 132.2876
```

4. **Calculate Cosine of** $\theta$:

```math
\cos(\theta) = \frac{-25.0000}{132.2876} = -0.188982
```

5. **Calculate** $\theta$ **in Degrees:**

```math
\theta = \cos^{-1}(-0.188982) = 100.8934^\circ
```

6. **Determine Final Hue** ($H$):
   Since $B = 50 \le G = 200$, we keep $H = \theta$:

```math
H = 100.8934^\circ
```

---

#### Step 5: State the Final Answer

**Final Answer:**

* **Intensity** ($I$): $116.6667$ (or normalized $I_{\text{norm}} = 0.4575$)
* **Saturation** ($S$): $0.5714$
* **Hue** ($H$): $100.8934^\circ$

---

### Key Exam Tips & Common Pitfalls

1. **Arithmetic Order:** Evaluate $(R-G)^2$ and $(R-B)(G-B)$ inside the square root carefully before taking the square root.
2. **Check the $B > G$ Condition:** Always verify whether $B > G$. If $B > G$, you must subtract $\theta$ from $360^\circ$ (i.e., $H = 360^\circ - \theta$). In this question, $50 \le 200$, so $H = \theta$.
3. **Units:** State Hue in degrees ($^\circ$), Saturation as a dimensionless ratio between $0$ and $1$, and Intensity either on the $[0, 255]$ scale or normalized $[0, 1]$ scale.

---

## 3. PYQ 2: YUV Color Model and Significance in Video Processing

### Exam Context

* **Marks:** 8 Marks
* **Frequency:** High (Core video processing theory question)

### Question Statement

1. Define the YUV color space and write the linear transformation equations converting RGB to YUV.
2. Express the RGB to YUV transformation in matrix form.
3. Explain why the YUV color model is widely preferred over RGB in video compression and television broadcasting.

---

### Step-by-Step Solution

#### 1. Definition and Concept

The **YUV color space** defines a color model in terms of one **Luminance** component ($Y$) and two **Chrominance** (color-difference) components ($U$ and $V$). It decouples brightness information from color information.

* **$Y$ (Luminance):** Captures monochrome brightness and gray-scale structure.
* **$U$ (Chrominance / Blue Difference):** Proportional to $B - Y$.
* **$V$ (Chrominance / Red Difference):** Proportional to $R - Y$.

---

#### 2. Component Equations

The standard ITU-R BT.601 conversion formulas for RGB inputs normalized to $[0, 1]$ are:

1. **Luminance** ($Y$): Represents perceived monochrome brightness.

```math
Y = 0.299 R + 0.587 G + 0.114 B
```

*(Green accounts for $58.7\%$ of perceived luminance because the human eye is most sensitive to green wavelength light)*.

2. **U-Chrominance** ($U$): Scaled difference between Blue and Luminance.

```math
U = 0.492 (B - Y) = -0.147 R - 0.289 G + 0.436 B
```

3. **V-Chrominance** ($V$): Scaled difference between Red and Luminance.

```math
V = 0.877 (R - Y) = 0.615 R - 0.515 G - 0.100 B
```

* **Matrix Representation:**

```math
\begin{bmatrix}
Y \\
U \\
V
\end{bmatrix} = \begin{bmatrix}
0.299 & 0.587 & 0.114 \\
-0.147 & -0.289 & 0.436 \\
0.615 & -0.515 & -0.100
\end{bmatrix} \begin{bmatrix}
R \\
G \\
B
\end{bmatrix}
```

---

#### 3. Significance in Video Processing

1. **Human Visual System (HVS) Exploitation:** The human eye contains far more rods (brightness sensitive) than cones (color sensitive). Human vision has high spatial resolution for luminance variations but lower spatial resolution for color variations. YUV isolates luminance, allowing chrominance components ($U, V$) to be downsampled (subsampled) without noticeable perceptual quality loss.
2. **Bandwidth Compression:** Subsampling chrominance (such as 4:2:0 or 4:2:2) reduces video data rates by $50\%$ or more while maintaining image quality.
3. **Backward Compatibility:** During the transition from black-and-white to color television broadcasting, black-and-white receivers could simply extract and display the $Y$ signal, while color receivers decoded $Y$, $U$, and $V$ to reconstruct full-color displays.

---

## 4. PYQ 3: Additive Mixing in the RGB Color Model

### Exam Context

* **Marks:** 6 Marks
* **Frequency:** Medium

### Question Statement

1. Explain the principle of additive color mixing in the RGB model.
2. List the primary and secondary colors of the RGB model and state their normalized vector representations.
3. Describe the structure of the 3D RGB Color Cube.
4. Name two hardware applications that rely on additive color mixing.

---

### Step-by-Step Solution

#### 1. Principle of Additive Mixing

The **RGB (Red, Green, Blue) color model** is an **additive color model**. It is based on the principle that colors are created by combining primary colored light sources emitted directly toward the observer's eye.

* **Mechanism:** As red, green, and blue light beams are added together, the resulting light spectrum becomes brighter until all three primaries at maximum intensity yield white light ($[255, 255, 255]^T$).

---

#### 2. Primary and Secondary Color Combinations

The three primary colors of light are **Red (R)**, **Green (G)**, and **Blue (B)**. Combining equal amounts of two primary lights yields the secondary subtractive colors:

```math
\begin{aligned}
\text{Red} + \text{Green} &= \text{Yellow} \quad (1, 1, 0) \\
\text{Green} + \text{Blue} &= \text{Cyan} \quad (0, 1, 1) \\
\text{Red} + \text{Blue} &= \text{Magenta} \quad (1, 0, 1) \\
\text{Red} + \text{Green} + \text{Blue} &= \text{White} \quad (1, 1, 1)
\end{aligned}
```

---

#### 3. RGB Color Cube Representation

The RGB color space is modeled as a 3D Cartesian unit cube $[0, 1]^3$:

* **Origin $(0,0,0)$:** Black (absence of light).
* **Opposite Corner $(1,1,1)$:** White (full light intensity).
* **Primary Axes:** Red axis $(1,0,0)$, Green axis $(0,1,0)$, Blue axis $(0,0,1)$.
* **Secondary Vertices:** Cyan $(0,1,1)$, Magenta $(1,0,1)$, Yellow $(1,1,0)$.
* **Main Diagonal:** Line connecting Black $(0,0,0)$ to White $(1,1,1)$ represents the neutral gray scale where $R = G = B$.

---

#### 4. Hardware Applications

1. **Digital Display Screens:** OLED, LCD, and LED monitors use sub-pixel triads of Red, Green, and Blue light-emitting elements.
2. **Projectors:** Combine three primary light beams to display full-color images.

---

## 5. PYQ 4: Concept of Vector-Based Color Slicing

### Exam Context

* **Marks:** 8 Marks
* **Frequency:** Medium-High

### Question Statement

1. Explain the concept of vector-based color slicing in multidimensional color space.
2. Mathematically formulate Spherical (Euclidean) Color Slicing and Cubic (Bounding Box) Color Slicing.
3. Compare Spherical vs. Cubic Color Slicing in terms of computational complexity and region boundary shape.

---

### Step-by-Step Solution

#### 1. Concept and Objective

**Color Slicing** is a vector-based thresholding technique used to highlight a specific range of colors in a multi-spectral image while suppressing or transforming all other colors. Unlike gray-level slicing, color slicing operates on 3D color vectors $\mathbf{z} = [R, G, B]^T$.

---

#### 2. Mathematical Formulations

##### Approach 1: Spherical Color Slicing (Euclidean Distance)

Defines a spherical region of interest in 3D color space centered at a prototype color vector $\mathbf{a} = [a_R, a_G, a_B]^T$ with radius $R_0$:

1. **Euclidean Distance Measure:**

```math
D(\mathbf{z}, \mathbf{a}) = \|\mathbf{z} - \mathbf{a}\| = \sqrt{(z_R - a_R)^2 + (z_G - a_G)^2 + (z_B - a_B)^2}
```

2. **Transformation Rule:**

```math
\mathbf{s} = \begin{cases}
[0.5, 0.5, 0.5]^T & \text{if } \|\mathbf{z} - \mathbf{a}\| \le R_0 \\
[0.0, 0.0, 0.0]^T & \text{if } \|\mathbf{z} - \mathbf{a}\| > R_0
\end{cases}
```

*(Pixels within distance $R_0$ of prototype $\mathbf{a}$ are retained or highlighted, while outside pixels are set to a neutral background)*.

---

##### Approach 2: Cubic / Bounding Box Color Slicing

Defines an axis-aligned 3D rectangular box centered at prototype color $\mathbf{a}$ with half-width tolerances $[d_R, d_G, d_B]^T$:

```math
\mathbf{s} = \begin{cases}
\mathbf{z}_{\text{highlight}} & \text{if } \lvert z_R - a_R \rvert \le d_R \quad \text{AND} \quad \lvert z_G - a_G \rvert \le d_G \quad \text{AND} \quad \lvert z_B - a_B \rvert \le d_B \\
\mathbf{z}_{\text{background}} & \text{otherwise}
\end{cases}
```

---

#### 3. Comparison of Spherical vs. Cubic Slicing

| Feature | Spherical Color Slicing | Cubic (Bounding Box) Color Slicing |
| :--- | :--- | :--- |
| **Boundary Geometry** | Smooth 3D Sphere | Axis-aligned 3D Cube / Box |
| **Distance Metric** | Euclidean Distance ($\|\mathbf{z} - \mathbf{a}\|$) | Absolute per-channel differences ($\lvert z_i - a_i \rvert$) |
| **Computational Cost** | High (Requires square root and multiplications) | Very Low (Simple range checks / comparison logic) |
| **Color Specificity** | Isotropic color tolerance in all directions | Independent channel tolerance widths |

---

#### 4. Applications

1. **Object Detection:** Isolating specific colored objects (e.g., traffic signs, fruits, medical stain dyes).
2. **Background Removal:** Chroma-key green/blue screen background segmentation.

---

## 6. PYQ 5: Comparative Breakdown of RGB, CMYK, HSI, HSV, and YUV Color Models

### Exam Context

* **Marks:** 10 Marks
* **Frequency:** High (Comprehensive comparison question)

### Question Statement

Construct a comparative matrix analyzing RGB, CMYK, HSI, HSV, and YUV color models across: Components, Primary Domain, Decoupling of Intensity, Best Application, and Major Advantage.

---

### Step-by-Step Solution

#### Comprehensive Comparison Matrix

| Color Model | Components | Primary Domain | Decouples Intensity? | Best Application | Major Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RGB** | Red ($R$), Green ($G$), Blue ($B$) | Additive Light Model | No (Intensity mixed across all 3 channels) | Monitors, digital cameras, graphics hardware | Direct match with hardware display emitters |
| **CMY / CMYK** | Cyan ($C$), Magenta ($M$), Yellow ($Y$), Black ($K$) | Subtractive Pigment Model | No (Reflectance based) | Color printing, publishing, ink dyes | Accurately models light absorption of physical inks |
| **HSI** | Hue ($H$), Saturation ($S$), Intensity ($I$) | Perceptual Polar Model | Yes ($I$ is completely isolated) | Image segmentation, human vision modeling | Decouples color/chroma from brightness; ideal for processing |
| **HSV** | Hue ($H$), Saturation ($S$), Value ($V$) | Perceptual Cylindrical Model | Yes ($V$ represents max brightness) | Computer vision, color picking UI controls | Intuitive for artistic color selection and thresholding |
| **YUV** | Luminance ($Y$), Chrominance ($U, V$) | Video Broadcast & Compression | Yes ($Y$ is isolated from $U, V$) | Video compression (H.264, MPEG), TV broadcasting | Enables chroma subsampling for major bandwidth reduction |

---

#### Key Takeaway Explanations for Exam

1. **Why RGB is not ideal for Image Processing:** In RGB, light intensity and chromaticity are fused across all three channels ($R, G, B$). Applying spatial filters or histogram processing directly to individual RGB channels alters the relative channel ratios, causing severe unnatural color shifts.
2. **Why HSI and YUV are preferred for Processing:** Both models isolate intensity/luminance into a single channel ($I$ or $Y$). Enhancement operations can be applied solely to the intensity channel while leaving color information ($H, S$ or $U, V$) unchanged.

---

## 7. PYQ 6: Chroma Subsampling in Video Processing

### Exam Context

* **Marks:** 6 Marks
* **Frequency:** Medium

### Question Statement

1. Define Chroma Subsampling and explain the $J:a:b$ notation.
2. Compare 4:4:4, 4:2:2, and 4:2:0 subsampling schemes in terms of sample layout, bandwidth savings, and visual quality.

---

### Step-by-Step Solution

#### 1. Concept of Chroma Subsampling

**Chroma Subsampling** is the practice of encoding images by implementing lower resolution for chrominance information than for luminance information. It relies on the biological fact that human vision has significantly lower spatial acuity for color detail than for brightness detail.

---

#### 2. Understanding $J:a:b$ Notation

The standard scheme is written as $J:a:b$, defined over a conceptual reference grid of $J$ pixels wide by $2$ pixels high:

* **$J$:** Reference width of the sample block (typically $4$ pixels wide).
* **$a$:** Number of chrominance samples ($U, V$) in the first row of $J$ pixels.
* **$b$:** Number of chrominance samples ($U, V$) in the second row of $J$ pixels (or changes in chrominance samples between the first and second row).

---

#### 3. Subsampling Formats Comparison

| Subsampling Scheme | Chrominance Sample Ratio | Data / Bandwidth Reduction | Common Applications | Visual Quality |
| :--- | :--- | :--- | :--- | :--- |
| **4:4:4** | Uncompressed (4 samples per row) | $0\%$ (Full bandwidth, 24 bits/pixel) | High-end film post-production, VFX | Lossless color fidelity |
| **4:2:2** | 2 samples per row (horizontal 2:1 reduction) | $33.3\%$ reduction (16 bits/pixel) | Professional broadcast video, ProRes | Excellent quality |
| **4:2:0** | 2 samples on row 1, 0 samples on row 2 (2x2 downsampling) | $50\%$ reduction (12 bits/pixel) | Consumer video (H.264/AVC, HEVC, JPEG, Blu-ray) | Standard for consumer media |

---

## 8. PYQ 7: Histogram Equalization of Colour Images (RGB vs. HSI/YUV)

### Exam Context

* **Marks:** 8 Marks
* **Frequency:** High (Crucial procedural question)

### Question Statement

1. Explain why performing independent histogram equalization on the R, G, and B channels of a color image produces severe color distortion.
2. Describe the correct procedure for histogram equalizing a color image using the HSI color space without distorting color tones.

---

### Step-by-Step Solution

#### 1. Why Independent RGB Histogram Equalization Fails

Histogram equalization stretches pixel intensity distributions across the full dynamic range $[0, L-1]$.

* **The Problem:** In RGB space, color hue and saturation are determined by the relative ratios between $R$, $G$, and $B$ values.
* **Result:** Equalizing each channel independently alters these relative channel ratios non-linearly across spatial locations. This causes severe false color artifacts (e.g., skin tones shifting to purple or green) and color saturation distortion.

```text
RGB Independent Equalization:   [R, G, B]^T  ===>  [T_R(R), T_G(G), T_B(B)]^T  (Channel Ratios Corrupted!)
```

---

#### 2. Correct Procedure: Intensity-Decoupled Equalization

To enhance image contrast without altering color information, processing must be performed in a color space that decouples intensity from chromaticity (such as **HSI** or **YUV**).

* **Principle:** Keep Hue ($H$) and Saturation ($S$) completely unchanged. Equalize **only** the Intensity ($I$) component image.

```text
HSI Decoupled Processing:       RGB  ===>  (H, S, I)  ===>  Equalize ONLY I -> I'  ===>  Convert (H, S, I') -> RGB
```

---

#### 3. Step-by-Step Processing Algorithm

1. **Color Space Conversion:** Convert input RGB image $f_{\text{RGB}}(x,y)$ to HSI color space, yielding $H(x,y)$, $S(x,y)$, and $I(x,y)$.
2. **Intensity Histogram Equalization:** Extract 2D intensity matrix $I(x,y)$. Compute its probability density function $p_I(r_k) = \frac{n_k}{M N}$ and cumulative distribution function (CDF):

```math
s_k = T(r_k) = (L - 1) \sum_{j=0}^{k} p_I(r_j)
```

Apply transformation $T(I)$ to obtain equalized intensity image $I'(x,y)$.

3. **Recombination & Inverse Conversion:** Combine original $H(x,y)$, original $S(x,y)$, and equalized $I'(x,y)$. Convert $(H, S, I')$ back to RGB space to obtain enhanced output image $g_{\text{RGB}}(x,y)$.

---

## 9. PYQ 8: Solved Numerical on RGB to CMY and CMYK Conversions

### Exam Context

* **Marks:** 6 Marks
* **Frequency:** Medium-High

### Question Statement

Given a normalized RGB color vector $\mathbf{z}_{\text{RGB}} = [0.2000, 0.4000, 0.7000]^T$:

1. Calculate the corresponding CMY color vector $\mathbf{z}_{\text{CMY}} = [C, M, Y]^T$.
2. Calculate the corresponding CMYK color vector $\mathbf{z}_{\text{CMYK}} = [C', M', Y', K]^T$.

---

### Step-by-Step Solution

#### Part 1: Convert RGB to CMY

The subtractive CMY components are calculated as:

```math
\begin{aligned}
C &= 1 - R \\
M &= 1 - G \\
Y &= 1 - B
\end{aligned}
```

Substitute $R = 0.2000$, $G = 0.4000$, $B = 0.7000$:

* $C = 1 - 0.2000 = 0.8000$
* $M = 1 - 0.4000 = 0.6000$
* $Y = 1 - 0.7000 = 0.3000$

```math
\mathbf{z}_{\text{CMY}} = [0.8000, 0.6000, 0.3000]^T
```

---

#### Part 2: Convert CMY to CMYK

1. **Calculate Black Key** ($K$):

```math
K = \min(C, M, Y) = \min(0.8000, 0.6000, 0.3000) = 0.3000
```

2. **Calculate Scale Factor** ($1 - K$):

```math
1 - K = 1 - 0.3000 = 0.7000
```

3. **Calculate Purified CMY Components** ($C', M', Y'$):

```math
C' = \frac{C - K}{1 - K} = \frac{0.8000 - 0.3000}{0.7000} = \frac{0.5000}{0.7000} = 0.7143
```

```math
M' = \frac{M - K}{1 - K} = \frac{0.6000 - 0.3000}{0.7000} = \frac{0.3000}{0.7000} = 0.4286
```

```math
Y' = \frac{Y - K}{1 - K} = \frac{0.3000 - 0.3000}{0.7000} = \frac{0.0000}{0.7000} = 0.0000
```

---

#### Final Answer

* **CMY Color Vector:** $\mathbf{z}_{\text{CMY}} = [0.8000, 0.6000, 0.3000]^T$
* **CMYK Color Vector:** $\mathbf{z}_{\text{CMYK}} = [0.7143, 0.4286, 0.0000, 0.3000]^T$

---

## 10. Summary Cheat Sheet for Unit 7 PYQ Preparation

| Topic / Method | Core Formulas & Equations | Critical Exam Checklist |
| :--- | :--- | :--- |
| **RGB to HSI** | $I = \frac{R+G+B}{3}$, $S = 1 - \frac{3 \cdot \min(R,G,B)}{R+G+B}$ | If $B > G$, set $H = 360^\circ - \theta$. |
| **RGB to YUV** | $Y = 0.299R + 0.587G + 0.114B$ | Green carries highest weight ($0.587$) due to human eye sensitivity. |
| **RGB to CMY** | $C = 1 - R$, $M = 1 - G$, $Y = 1 - B$ | Direct linear inversion. |
| **CMY to CMYK** | $K = \min(C,M,Y)$, $C' = \frac{C-K}{1-K}$ | Denominator is $1-K$. |
| **Color Slicing** | Sphere: $\|\mathbf{z}-\mathbf{a}\| \le R_0$; Cube: $\lvert z_i - a_i \rvert \le d_i$ | Spherical uses Euclidean distance; Cubic uses box range check. |
| **Color Equalization** | Equalize ONLY $I$ channel in HSI or $Y$ in YUV | NEVER equalize RGB channels independently! |
