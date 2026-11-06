# Unit 7: Colour Image Processing — Solved Numericals & Exam Guide

---

## 1. Overview of Unit 7 Numericals and Exam Strategy

Unit 7 (Colour Image Processing) tests mathematical transformations across different color spaces, vector-based color processing, and intensity-decoupled histogram equalization. In Term End Examinations (TEE) and Continuous Assessment (CA) tests, numerical problems account for a significant portion of Unit 7 weightage.

---

### Key Numerical Categories in Unit 7

| Category | Primary Concept / Transformation | Mathematical Focus | Common Exam Marks |
| :--- | :--- | :--- | :--- |
| **Category 1** | RGB to HSI Color Space Conversion | Non-linear geometric polar mapping ($`I`$, $`S`$, $`\theta`$, $`H`$) | 5 – 10 Marks |
| **Category 2** | HSI to RGB Color Space Conversion | Inverse sector-based trigonometric transformation | 5 – 10 Marks |
| **Category 3** | RGB to CMY and CMYK Conversions | Subtractive transformation & Black key extraction ($`K`$) | 4 – 6 Marks |
| **Category 4** | RGB to YUV and YIQ Matrix Transformations | Linear matrix transformation & Luminance decoupling | 4 – 6 Marks |
| **Category 5** | Vector-Based Color Slicing | 3D Spherical Euclidean distance & Cubic bounding box | 5 – 8 Marks |
| **Category 6** | Histogram Equalization of Colour Images | Independent RGB vs. Intensity-Decoupled HSI/YUV | 5 – 8 Marks |

---

### General Exam Solving Tips and Formatting Rules

1. **Check Scale Range:** Always verify whether input RGB values are given in normalized range $`[0, 1]`$ or standard 8-bit integer range $`[0, 255]`$. Convert to normalized range $`[0, 1]`$ when applying $`S`$ and $`\theta`$ formulas if required by the question variant.
2. **Hue Sector Condition ($`B \le G`$ vs. $`B > G`$):** In RGB to HSI conversion, always check the condition of Blue ($`B`$) relative to Green ($`G`$). If $`B > G`$, final Hue is $`H = 360^\circ - \theta`$; if $`B \le G`$, $`H = \theta`$.
3. **Precision:** Carry at least 4 decimal places throughout intermediate calculation steps and state the final rounding explicitly.
4. **Units:** Express Hue ($`H`$) in degrees ($`^\circ`$) and specify normalized values clearly.

---

## 2. Category 1: RGB to HSI Color Space Conversion

---

### Formula Summary for RGB to HSI

Given normalized RGB components $`R, G, B \in [0, 1]`$:

1. **Intensity ($`I`$):**

```math
I = \frac{R + G + B}{3}
```

2. **Saturation ($`S`$):**

```math
S = 1 - \frac{3}{R + G + B} \cdot \min(R, G, B)
```

If $`R = G = B = 0`$, set $`S = 0`$.

3. **Hue Angle ($`\theta`$):**

```math
\theta = \cos^{-1} \left[ \frac{0.5 \cdot [(R - G) + (R - B)]}{\sqrt{(R - G)^2 + (R - B)(G - B)}} \right]
```

4. **Final Hue ($`H`$):**

```math
H = \begin{cases}
\theta & \text{if } B \le G \\
360^\circ - \theta & \text{if } B > G
\end{cases}
```

---

### Problem 1.1: Complete RGB to HSI Conversion (Un-normalized RGB)

#### Problem Statement
A pixel in an RGB image has un-normalized color components $`R = 100`$, $`G = 200`$, and $`B = 50`$ (on an 8-bit scale $`[0, 255]`$). 

1. Normalize the RGB values to the range $`[0, 1]`$.
2. Calculate the Intensity ($`I`$) in both 8-bit scale and normalized scale.
3. Calculate the Saturation ($`S`$).
4. Calculate the Hue angle ($`\theta`$) and final Hue ($`H`$) in degrees.

---

#### Step-by-Step Solution

##### Step 1: Normalize RGB Values
Divide each component by 255:

```math
R_{\text{norm}} = \frac{100}{255} = 0.392157 \approx 0.3922
```

```math
G_{\text{norm}} = \frac{200}{255} = 0.784314 \approx 0.7843
```

```math
B_{\text{norm}} = \frac{50}{255} = 0.196078 \approx 0.1961
```

---

##### Step 2: Compute Intensity ($`I`$)
Using un-normalized RGB values:

```math
I_{\text{raw}} = \frac{R + G + B}{3} = \frac{100 + 200 + 50}{3} = \frac{350}{3} = 116.6667
```

Using normalized RGB values:

```math
I_{\text{norm}} = \frac{0.392157 + 0.784314 + 0.196078}{3} = \frac{0.772549}{3} = 0.457509 \approx 0.4575
```

Note: $`I_{\text{norm}} = \frac{116.6667}{255} = 0.4575`$.

---

##### Step 3: Compute Saturation ($`S`$)
Find minimum component: $`\min(R, G, B) = \min(100, 200, 50) = 50`$.

Using normalized values (or raw ratio):

```math
S = 1 - \frac{3}{R + G + B} \cdot \min(R, G, B)
```

```math
S = 1 - \frac{3 \cdot 50}{100 + 200 + 50} = 1 - \frac{150}{350} = 1 - 0.428571 = 0.571429 \approx 0.5714
```

---

##### Step 4: Compute Hue Angle ($`\theta`$)
Calculate terms using normalized values $`R = 0.3922`$, $`G = 0.7843`$, $`B = 0.1961`$:

* $`R - G = 0.392157 - 0.784314 = -0.392157`$
* $`R - B = 0.392157 - 0.196078 = 0.196079`$
* $`G - B = 0.784314 - 0.196078 = 0.588236`$

1. **Numerator:**

```math
\text{Num} = 0.5 \cdot [(-0.392157) + 0.196079] = 0.5 \cdot (-0.196078) = -0.098039
```

2. **Denominator:**

```math
(R - G)^2 = (-0.392157)^2 = 0.153787
```

```math
(R - B)(G - B) = (0.196079)(0.588236) = 0.115341
```

```math
\text{Den} = \sqrt{0.153787 + 0.115341} = \sqrt{0.269128} = 0.518776
```

3. **Cosine Value:**

```math
\cos(\theta) = \frac{-0.098039}{0.518776} = -0.188982
```

4. **Angle $`\theta`$:**

```math
\theta = \cos^{-1}(-0.188982) = 100.8934^\circ
```

---

##### Step 5: Determine Final Hue ($`H`$)
Compare $`B`$ and $`G`$:
$`B = 50`$ and $`G = 200`$. Since $`B \le G`$ ($`50 \le 200`$):

```math
H = \theta = 100.8934^\circ
```

---

#### Final Answer
* **Normalized RGB:** $`R = 0.3922`$, $`G = 0.7843`$, $`B = 0.1961`$
* **Intensity:** $`I = 116.6667`$ (or $`I_{\text{norm}} = 0.4575`$)
* **Saturation:** $`S = 0.5714`$
* **Hue:** $`H = 100.8934^\circ`$ (rounded to 4 decimal places)

---

### Problem 1.2: RGB to HSI Conversion with $`B > G`$ Condition

#### Problem Statement
Given normalized RGB color values $`R = 0.8`$, $`G = 0.2`$, and $`B = 0.6`$, calculate $`I`$, $`S`$, and $`H`$.

---

#### Step-by-Step Solution

##### Step 1: Compute Intensity ($`I`$)

```math
I = \frac{0.8 + 0.2 + 0.6}{3} = \frac{1.6}{3} = 0.533333 \approx 0.5333
```

##### Step 2: Compute Saturation ($`S`$)
Minimum value $`\min(0.8, 0.2, 0.6) = 0.2`$:

```math
S = 1 - \frac{3 \cdot 0.2}{1.6} = 1 - \frac{0.6}{1.6} = 1 - 0.3750 = 0.6250
```

##### Step 3: Compute Hue Angle ($`\theta`$)
* $`R - G = 0.8 - 0.2 = 0.6`$
* $`R - B = 0.8 - 0.6 = 0.2`$
* $`G - B = 0.2 - 0.6 = -0.4`$

1. **Numerator:**

```math
\text{Num} = 0.5 \cdot (0.6 + 0.2) = 0.5 \cdot 0.8 = 0.4000
```

2. **Denominator:**

```math
(R - G)^2 = (0.6)^2 = 0.3600
```

```math
(R - B)(G - B) = (0.2)(-0.4) = -0.0800
```

```math
\text{Den} = \sqrt{0.3600 + (-0.0800)} = \sqrt{0.2800} = 0.529150
```

3. **Cosine Value:**

```math
\cos(\theta) = \frac{0.4000}{0.529150} = 0.755929
```

4. **Angle $`\theta`$:**

```math
\theta = \cos^{-1}(0.755929) = 40.8934^\circ
```

##### Step 4: Determine Final Hue ($`H`$)
Check condition: $`B = 0.6`$ and $`G = 0.2`$.
Since $`B > G`$ ($`0.6 > 0.2`$):

```math
H = 360^\circ - \theta = 360^\circ - 40.8934^\circ = 319.1066^\circ
```

---

#### Final Answer
* **Intensity:** $`I = 0.5333`$
* **Saturation:** $`S = 0.6250`$
* **Hue:** $`H = 319.1066^\circ`$ (rounded to 4 decimal places)

---

## 3. Category 2: HSI to RGB Color Space Conversion

---

### Sector-Based HSI to RGB Formulas

Given $`H \in [0^\circ, 360^\circ]`$, $`S \in [0, 1]`$, $`I \in [0, 1]`$:

#### 1. RG-Sector ($`0^\circ \le H < 120^\circ`$)

```math
B = I(1 - S)
```

```math
R = I \left[ 1 + \frac{S \cdot \cos(H)}{\cos(60^\circ - H)} \right]
```

```math
G = 3I - (R + B)
```

#### 2. GB-Sector ($`120^\circ \le H < 240^\circ`$)
Subtract $`120^\circ`$ from $`H`$: $`H' = H - 120^\circ`$.

```math
R = I(1 - S)
```

```math
G = I \left[ 1 + \frac{S \cdot \cos(H')}{\cos(60^\circ - H')} \right]
```

```math
B = 3I - (R + G)
```

#### 3. BR-Sector ($`240^\circ \le H \le 360^\circ`$)
Subtract $`240^\circ`$ from $`H`$: $`H'' = H - 240^\circ`$.

```math
G = I(1 - S)
```

```math
B = I \left[ 1 + \frac{S \cdot \cos(H'')}{\cos(60^\circ - H'')} \right]
```

```math
R = 3I - (G + B)
```

---

### Problem 2.1: HSI to RGB Conversion (RG-Sector)

#### Problem Statement
Convert HSI color components $`H = 60^\circ`$, $`S = 0.5`$, and $`I = 0.6`$ into normalized RGB components.

---

#### Step-by-Step Solution

##### Step 1: Identify Sector
Since $`0^\circ \le H = 60^\circ < 120^\circ`$, the color lies in the **RG-Sector**.

##### Step 2: Compute Blue Component ($`B`$)

```math
B = I(1 - S) = 0.6 \cdot (1 - 0.5) = 0.6 \cdot 0.5 = 0.3000
```

##### Step 3: Compute Red Component ($`R`$)
Evaluate trigonometric terms for $`H = 60^\circ`$:
* $`\cos(60^\circ) = 0.5`$
* $`\cos(60^\circ - 60^\circ) = \cos(0^\circ) = 1.0`$

```math
R = 0.6 \cdot \left[ 1 + \frac{0.5 \cdot 0.5}{1.0} \right] = 0.6 \cdot (1 + 0.25) = 0.6 \cdot 1.25 = 0.7500
```

##### Step 4: Compute Green Component ($`G`$)

```math
G = 3I - (R + B) = 3(0.6) - (0.7500 + 0.3000) = 1.8000 - 1.0500 = 0.7500
```

---

#### Final Answer
* **Red:** $`R = 0.7500`$
* **Green:** $`G = 0.7500`$
* **Blue:** $`B = 0.3000`$ (rounded to 4 decimal places)

---

## 4. Category 3: RGB to CMY and CMYK Conversions

---

### Formula Summary for CMY and CMYK

Given normalized RGB components $`R, G, B \in [0, 1]`$:

1. **RGB to CMY Conversion:**

```math
\begin{bmatrix}
C \\
M \\
Y
\end{bmatrix} = \begin{bmatrix}
1 - R \\
1 - G \\
1 - B
\end{bmatrix}
```

2. **CMY to CMYK Conversion:**

```math
K = \min(C, M, Y)
```

```math
C' = \frac{C - K}{1 - K}, \quad M' = \frac{M - K}{1 - K}, \quad Y' = \frac{Y - K}{1 - K}
```

If $`K = 1`$ (pure black), set $`C' = M' = Y' = 0`$.

---

### Problem 3.1: RGB to CMY and CMYK Conversion

#### Problem Statement
Given normalized RGB color vector $`\mathbf{z}_{\text{RGB}} = [0.2000, 0.4000, 0.7000]^T`$:

1. Calculate the CMY color components ($`C, M, Y`$).
2. Extract the Black key component ($`K`$) and compute the purified CMYK components ($`C', M', Y', K`$).

---

#### Step-by-Step Solution

##### Step 1: Compute CMY Components

```math
C = 1 - R = 1 - 0.2000 = 0.8000
```

```math
M = 1 - G = 1 - 0.4000 = 0.6000
```

```math
Y = 1 - B = 1 - 0.7000 = 0.3000
```

---

##### Step 2: Compute Black Key ($`K`$)

```math
K = \min(C, M, Y) = \min(0.8000, 0.6000, 0.3000) = 0.3000
```

---

##### Step 3: Compute Purified CMYK Components
Scale factor denominator: $`1 - K = 1 - 0.3000 = 0.7000`$.

1. **Cyan ($`C'`$):**

```math
C' = \frac{C - K}{1 - K} = \frac{0.8000 - 0.3000}{0.7000} = \frac{0.5000}{0.7000} = 0.714286 \approx 0.7143
```

2. **Magenta ($`M'`$):**

```math
M' = \frac{M - K}{1 - K} = \frac{0.6000 - 0.3000}{0.7000} = \frac{0.3000}{0.7000} = 0.428571 \approx 0.4286
```

3. **Yellow ($`Y'`$):**

```math
Y' = \frac{Y - K}{1 - K} = \frac{0.3000 - 0.3000}{0.7000} = \frac{0.0000}{0.7000} = 0.0000
```

---

#### Final Answer
* **CMY Representation:** $`C = 0.8000`$, $`M = 0.6000`$, $`Y = 0.3000`$
* **CMYK Representation:** $`C' = 0.7143`$, $`M' = 0.4286`$, $`Y' = 0.0000`$, $`K = 0.3000`$ (rounded to 4 decimal places)

---

## 5. Category 4: RGB to YUV Linear Matrix Transformation

---

### Formula Summary for YUV Transformation

The conversion matrix from normalized RGB to YUV is:

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

Scalar equations:
* $`Y = 0.299 R + 0.587 G + 0.114 B`$
* $`U = -0.147 R - 0.289 G + 0.436 B = 0.492 (B - Y)`$
* $`V = 0.615 R - 0.515 G - 0.100 B = 0.877 (R - Y)`$

---

### Problem 4.1: RGB to YUV Conversion

#### Problem Statement
A pixel has RGB values $`R = 0.5`$, $`G = 0.8`$, and $`B = 0.2`$. Compute its YUV representation ($`Y, U, V`$).

---

#### Step-by-Step Solution

##### Step 1: Compute Luminance ($`Y`$)

```math
Y = (0.299 \cdot 0.5) + (0.587 \cdot 0.8) + (0.114 \cdot 0.2)
```

```math
Y = 0.1495 + 0.4696 + 0.0228 = 0.6419
```

##### Step 2: Compute Chrominance $`U`$

```math
U = (-0.147 \cdot 0.5) + (-0.289 \cdot 0.8) + (0.436 \cdot 0.2)
```

```math
U = -0.0735 - 0.2312 + 0.0872 = -0.2175
```

Alternative formula check:

```math
U = 0.492(B - Y) = 0.492(0.2 - 0.6419) = 0.492(-0.4419) = -0.217415 \approx -0.2174
```

##### Step 3: Compute Chrominance $`V`$

```math
V = (0.615 \cdot 0.5) + (-0.515 \cdot 0.8) + (-0.100 \cdot 0.2)
```

```math
V = 0.3075 - 0.4120 - 0.0200 = -0.1245
```

Alternative formula check:

```math
V = 0.877(R - Y) = 0.877(0.5 - 0.6419) = 0.877(-0.1419) = -0.124446 \approx -0.1244
```

---

#### Final Answer
* **Luminance ($`Y`$):** $`0.6419`$
* **Chrominance ($`U`$):** $`-0.2175`$
* **Chrominance ($`V`$):** $`-0.1245`$ (rounded to 4 decimal places)

---

## 6. Category 5: Vector-Based Color Slicing

---

### Formulas for Color Slicing

Let $`\mathbf{z} = [z_R, z_G, z_B]^T`$ be an arbitrary pixel color vector, and $`\mathbf{a} = [a_R, a_G, a_B]^T`$ be the prototype target color vector.

1. **Spherical Color Slicing (Euclidean Distance):**

```math
D(\mathbf{z}, \mathbf{a}) = \|\mathbf{z} - \mathbf{a}\| = \sqrt{(z_R - a_R)^2 + (z_G - a_G)^2 + (z_B - a_B)^2}
```

Output transformation:

```math
\mathbf{s} = \begin{cases}
\mathbf{z} & \text{if } D(\mathbf{z}, \mathbf{a}) \le R_0 \\
[0.5, 0.5, 0.5]^T & \text{if } D(\mathbf{z}, \mathbf{a}) > R_0
\end{cases}
```

2. **Cubic Color Slicing (Bounding Box):**

```math
\mathbf{s} = \begin{cases}
\mathbf{z} & \text{if } |z_R - a_R| \le d_R \text{ AND } |z_G - a_G| \le d_G \text{ AND } |z_B - a_B| \le d_B \\
[0.5, 0.5, 0.5]^T & \text{otherwise}
\end{cases}
```

---

### Problem 5.1: Spherical and Cubic Color Slicing

#### Problem Statement
Given a target prototype color vector $`\mathbf{a} = [0.6, 0.2, 0.2]^T`$:

1. For spherical color slicing with sphere radius $`R_0 = 0.25`$, determine whether pixel $`\mathbf{z}_1 = [0.7, 0.3, 0.1]^T`$ lies inside the highlighted region.
2. For cubic color slicing with half-width tolerance $`d_R = d_G = d_B = 0.15`$, determine whether pixel $`\mathbf{z}_1`$ lies inside the highlighted region.

---

#### Step-by-Step Solution

##### Part 1: Spherical Color Slicing Evaluation
Calculate Euclidean distance $`D(\mathbf{z}_1, \mathbf{a})`$:

* $`z_R - a_R = 0.7 - 0.6 = 0.1`$
* $`z_G - a_G = 0.3 - 0.2 = 0.1`$
* $`z_B - a_B = 0.1 - 0.2 = -0.1`$

```math
D(\mathbf{z}_1, \mathbf{a}) = \sqrt{(0.1)^2 + (0.1)^2 + (-0.1)^2} = \sqrt{0.01 + 0.01 + 0.01} = \sqrt{0.03} = 0.173205 \approx 0.1732
```

Compare distance with radius $`R_0 = 0.25`$:

```math
D(\mathbf{z}_1, \mathbf{a}) = 0.1732 \le R_0 = 0.25
```

Since the condition is satisfied, pixel $`\mathbf{z}_1`$ lies **inside** the spherical slicing region and is **highlighted**.

---

##### Part 2: Cubic Color Slicing Evaluation
Check component-wise absolute differences against tolerance $`d = 0.15`$:

* Red channel difference: $`|0.7 - 0.6| = 0.1000 \le 0.15`$ (True)
* Green channel difference: $`|0.3 - 0.2| = 0.1000 \le 0.15`$ (True)
* Blue channel difference: $`|0.1 - 0.2| = 0.1000 \le 0.15`$ (True)

Since all three channel conditions hold true simultaneously, pixel $`\mathbf{z}_1`$ lies **inside** the cubic slicing bounding box and is **highlighted**.

---

#### Final Answer
* **Spherical Slicing:** Distance $`D = 0.1732 \le 0.25`$ (Pixel is **highlighted**).
* **Cubic Slicing:** All channel differences equal $`0.1000 \le 0.15`$ (Pixel is **highlighted**).

---

## 7. Category 6: Intensity-Decoupled Histogram Equalization

---

### Algorithm Summary for Color Histogram Equalization

1. **Do NOT equalize R, G, B channels independently**, as this causes severe color shifting and distortion.
2. **Convert RGB image to HSI (or YUV) color space.**
3. **Keep Hue ($`H`$) and Saturation ($`S`$) channels unchanged.**
4. **Apply standard histogram equalization ONLY to the Intensity ($`I`$) or Luminance ($`Y`$) channel:**

```math
s_k = T(r_k) = (L - 1) \sum_{j=0}^{k} p_I(r_j)
```

5. **Recombine $`H`$, $`S`$, and equalized $`I'`$ and convert back to RGB.**

---

### Problem 6.1: Intensity Channel Equalization Numerical

#### Problem Statement
A $`4 \times 4`$ color image has an 8-level Intensity channel ($`L = 8`$, gray levels $`0`$ to $`7`$) with the following histogram distribution:

| Intensity Level ($`r_k`$) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Pixel Count ($`n_k`$)** | 0 | 0 | 4 | 6 | 4 | 2 | 0 | 0 |

Perform histogram equalization on the Intensity channel and determine the transformed output intensity levels $`s_k`$.

---

#### Step-by-Step Solution

##### Step 1: Calculate Probability Density Function ($`p_I(r_k) = \frac{n_k}{M N}`$)
Total pixels $`N = 4 \times 4 = 16`$.

* $`p_I(0) = 0/16 = 0.0000`$
* $`p_I(1) = 0/16 = 0.0000`$
* $`p_I(2) = 4/16 = 0.2500`$
* $`p_I(3) = 6/16 = 0.3750`$
* $`p_I(4) = 4/16 = 0.2500`$
* $`p_I(5) = 2/16 = 0.1250`$
* $`p_I(6) = 0/16 = 0.0000`$
* $`p_I(7) = 0/16 = 0.0000`$

---

##### Step 2: Calculate Cumulative Distribution Function ($`\text{CDF}(r_k)`$)

* $`\text{CDF}(0) = 0.0000`$
* $`\text{CDF}(1) = 0.0000`$
* $`\text{CDF}(2) = 0.2500`$
* $`\text{CDF}(3) = 0.2500 + 0.3750 = 0.6250`$
* $`\text{CDF}(4) = 0.6250 + 0.2500 = 0.8750`$
* $`\text{CDF}(5) = 0.8750 + 0.1250 = 1.0000`$
* $`\text{CDF}(6) = 1.0000`$
* $`\text{CDF}(7) = 1.0000`$

---

##### Step 3: Compute Output Gray Levels $`s_k = \text{round}[(L - 1) \cdot \text{CDF}(r_k)]`$
For $`L - 1 = 7`$:

* $`s_0 = \text{round}(7 \cdot 0.0000) = 0`$
* $`s_1 = \text{round}(7 \cdot 0.0000) = 0`$
* $`s_2 = \text{round}(7 \cdot 0.2500) = \text{round}(1.7500) = 2`$
* $`s_3 = \text{round}(7 \cdot 0.6250) = \text{round}(4.3750) = 4`$
* $`s_4 = \text{round}(7 \cdot 0.8750) = \text{round}(6.1250) = 6`$
* $`s_5 = \text{round}(7 \cdot 1.0000) = \text{round}(7.0000) = 7`$
* $`s_6 = \text{round}(7 \cdot 1.0000) = 7`$
* $`s_7 = \text{round}(7 \cdot 1.0000) = 7`$

---

#### Final Equalized Intensity Mapping Table

| Original Level ($`r_k`$) | Count ($`n_k`$) | $`p_I(r_k)`$ | CDF | Unrounded $`7 \cdot \text{CDF}`$ | Equalized Level ($`s_k`$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 0.0000 | 0.0000 | 0.0000 | **0** |
| **1** | 0 | 0.0000 | 0.0000 | 0.0000 | **0** |
| **2** | 4 | 0.2500 | 0.2500 | 1.7500 | **2** |
| **3** | 6 | 0.3750 | 0.6250 | 4.3750 | **4** |
| **4** | 4 | 0.2500 | 0.8750 | 6.1250 | **6** |
| **5** | 2 | 0.1250 | 1.0000 | 7.0000 | **7** |
| **6** | 0 | 0.0000 | 1.0000 | 7.0000 | **7** |
| **7** | 0 | 0.0000 | 1.0000 | 7.0000 | **7** |

---

## 8. Summary Exam Formula Cheat Sheet

---

### Quick Reference Matrix

| Transformation | Core Formula | Special Case / Exam Trap |
| :--- | :--- | :--- |
| **RGB to HSI ($`I`$)** | $`I = \frac{R+G+B}{3}`$ | Divide by 255 if raw values are given. |
| **RGB to HSI ($`S`$)** | $`S = 1 - \frac{3 \cdot \min(R,G,B)}{R+G+B}`$ | If $`R=G=B=0`$, $`S = 0`$. |
| **RGB to HSI ($`H`$)** | $`H = \theta`$ if $`B \le G`$; $`H = 360^\circ - \theta`$ if $`B > G`$ | Always check $`B > G`$ condition! |
| **RGB to CMY** | $`C = 1-R, \quad M = 1-G, \quad Y = 1-B`$ | Linear subtractive complement. |
| **CMY to CMYK** | $`K = \min(C,M,Y), \quad C' = \frac{C-K}{1-K}`$ | Denominator is $`1-K`$. |
| **RGB to YUV ($`Y`$)** | $`Y = 0.299R + 0.587G + 0.114B`$ | Green carries the largest weight ($`0.587`$). |
| **Spherical Color Slicing** | $`\|\mathbf{z} - \mathbf{a}\| \le R_0`$ | 3D Euclidean distance formula. |
| **Cubic Color Slicing** | $`\lvert z_i - a_i \rvert \le d_i \quad \text{for all } i \in \{R,G,B\}`$ | Component-wise threshold check. |

---
