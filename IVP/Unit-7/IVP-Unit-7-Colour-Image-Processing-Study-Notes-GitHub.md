# Unit 7: Colour Image Processing — Comprehensive Study Notes & Exam Guide

## 1. Introduction, Physics of Light, and Human Visual Perception

Colour image processing plays a central role in computer vision, digital image analysis, and visual multimedia systems. While monochrome images contain only intensity information (gray levels), colour images provide rich spectral information that significantly enhances object detection, segmentation, and human interpretation.

---

### 1.1 Nature of Light and Visual Spectrum

Light is electromagnetic radiation capable of stimulating the human visual system. It exhibits a dual wave-particle nature:

1. **Wave Theory:** Light propagates as transverse electromagnetic waves defined by wavelength ($`\lambda`$) and frequency ($`f`$). The relationship is given by:

```math
c = \lambda \cdot f
```

where $`c \approx 3 \times 10^8 \text{ m/s}`$ is the speed of light in vacuum.

2. **Visible Spectrum:** The human eye perceives electromagnetic radiation within a narrow band of wavelengths ranging approximately from $`380 \text{ nm}`$ (violet) to $`780 \text{ nm}`$ (red):
   - **Violet / Blue:** $`380 \text{ nm} - 490 \text{ nm}`$
   - **Green:** $`490 \text{ nm} - 560 \text{ nm}`$
   - **Yellow / Orange:** $`560 \text{ nm} - 630 \text{ nm}`$
   - **Red:** $`630 \text{ nm} - 780 \text{ nm}`$

```text
Electromagnetic Spectrum:
[ Gamma Rays | X-Rays | UV | Visible Spectrum (380-780 nm) | Infrared | Microwaves | Radio ]
                             |--- Violet-Blue-Green-Yellow-Red ---|
```

---

### 1.2 Human Visual System and Tristimulus Theory

Human colour perception is governed by photoreceptor cells located in the retina:

* **Rods:** Responsible for scotopic (low-light / achromatic) vision. They provide monochrome perception without colour distinction.
* **Cones:** Responsible for photopic (bright-light / chromatic) vision. The human retina contains approximately $`6`$ to $`7`$ million cones, divided into three principal sensor categories based on spectral sensitivity peaks:
  1. **L-Cones (Long wavelength):** Peak sensitivity near $`560 \text{ nm}`$ (Red sensory perception).
  2. **M-Cones (Medium wavelength):** Peak sensitivity near $`530 \text{ nm}`$ (Green sensory perception).
  3. **S-Cones (Short wavelength):** Peak sensitivity near $`430 \text{ nm}`$ (Blue sensory perception).

#### Tristimulus Theory and CIE Chromaticity

According to the **CIE (Commission Internationale de l'Éclairage)** tristimulus specification, any perceived colour can be produced by matching amounts of three primary monochromatic lights: Red ($`700 \text{ nm}`$), Green ($`546.1 \text{ nm}`$), and Blue ($`435.8 \text{ nm}`$).

Let $`X`$, $`Y`$, and $`Z`$ represent the CIE tristimulus values (amounts of primary light required to match a given colour). The normalized **chromaticity coordinates** $`x`$, $`y`$, and $`z`$ are defined as:

```math
x = \frac{X}{X + Y + Z}, \quad y = \frac{Y}{X + Y + Z}, \quad z = \frac{Z}{X + Y + Z}
```

Since the sum of normalized coordinates equals unity ($`x + y + z = 1`$), any colour chromaticity is completely specified by two coordinates ($`x, y`$).

```text
CIE 1931 Chromaticity Diagram Structure:
y-axis (Greenness)
  ^
1.0|         Pure Spectral Colors (Tongue Boundary)
   |            /  \
0.8|           /    \
0.6|          /  White (0.33, 0.33)
0.4|         /        \
0.2|        /__________\
0.0+-------------------------> x-axis (Redness)
   0.0  0.2  0.4  0.6  0.8  1.0
```

---

### 1.3 Key Perceptual Attributes of Colour

Human visual perception describes colour using three fundamental subjective quantities:

1. **Brightness (Luminance):** The achromatic intensity or total radiant energy perceived from a light source (ranging from dark to bright white).
2. **Hue ($`H`$):** The dominant spectral attribute that identifies the colour family (such as red, yellow, green, or cyan). Hue is measured as an angle from $`0^\circ`$ to $`360^\circ`$.
3. **Saturation ($`S`$):** The purity or degree of dilution of a colour by white light. A fully saturated colour contains no white light (e.g., pure red), whereas zero saturation corresponds to a shade of gray.

Together, **Hue** and **Saturation** are referred to as **Chrominance** (or chromaticity).

---

## 2. Taxonomies of Colour Models and Spaces

A **colour model** (or colour space) is a mathematical specification of a coordinate system wherein each colour is represented by a single point. Colour models are categorized based on their technical hardware implementation or visual perception characteristics.

---

### 2.1 Additive vs. Subtractive Primary Models

```text
Additive Light Mixing (RGB):            Subtractive Pigment Mixing (CMY):
     Red + Green = Yellow                    Cyan + Magenta = Blue
     Red + Blue  = Magenta                   Cyan + Yellow  = Green
     Green + Blue = Cyan                     Magenta + Yellow = Red
     Red + Green + Blue = White              Cyan + Magenta + Yellow = Black
```

| Feature | Additive Model (RGB) | Subtractive Model (CMY / CMYK) |
| :--- | :--- | :--- |
| **Physical Basis** | Superimposition of emitted light beams | Absorption and reflection of ambient light by inks/pigments |
| **Primary Colours** | Red ($`R`$), Green ($`G`$), Blue ($`B`$) | Cyan ($`C`$), Magenta ($`M`$), Yellow ($`Y`$) |
| **Secondary Colours** | Cyan, Magenta, Yellow | Red, Green, Blue |
| **Zero State (Origin)** | Darkness / Black ($`0,0,0`$) | Blank White Paper ($`0,0,0`$) |
| **Full Mixture** | White Light ($`1,1,1`$) | Muddy Black / Dark Brown ($`1,1,1`$) |
| **Primary Applications** | CRT displays, LCD/LED monitors, digital cameras | Color printing, lithography, commercial publishing |

---

### 2.2 Comprehensive Survey of Major Colour Models

#### 1. RGB Colour Model (Device-Dependent Additive)
* **Coordinate System:** 3D Cartesian Unit Cube $`[0,1]^3`$.
* **Axes:** $`R`$-axis (Red), $`G`$-axis (Green), $`B`$-axis (Blue).
* **Vertices:**
  - $`(0,0,0)`$: Black origin
  - $`(1,1,1)`$: White vertex
  - Main diagonal connecting $`(0,0,0)`$ to $`(1,1,1)`$ represents the **grayscale line** (equal amounts of $`R=G=B`$).

#### 2. CMY and CMYK Models (Subtractive Printing)
* **CMY:** Cyan, Magenta, and Yellow are the complements of Red, Green, and Blue, respectively.
* **CMYK:** In practical printing, combining equal parts of $`C`$, $`M`$, and $`Y`$ produces an imperfect, muddy dark brown due to pigment impurities. To save expensive colored inks and produce deep neutral blacks, a fourth key component—**Key / Black ($`K`$)**—is extracted.

#### 3. HSI / HSV Colour Models (Perceptual Models)
* **Decoupling Principle:** Both models explicitly separate the intensity/luminance component from the chromatic information (Hue and Saturation).
* **HSI (Hue, Saturation, Intensity):** Represented geometrically as a double hexcone or double cone. Intensity ($`I`$) is the vertical axis ranging from $`0`$ (black) to $`1`$ (white).
* **HSV (Hue, Saturation, Value):** Represented geometrically as an inverted single hexcone or cylinder. Value ($`V`$) measures max channel brightness ($`V = \max(R,G,B)`$).

#### 4. YUV Colour Model (Luminance / Chrominance Transmission)
* **Components:**
  - $`Y`$: Luminance (brightness component, fully compatible with legacy black-and-white television).
  - $`U, V`$: Chrominance (color-difference components: $`U \propto B - Y`$, $`V \propto R - Y`$).
* **Advantage:** Human vision is far more sensitive to luminance variations than to chrominance details. Decoupling allows **chroma subsampling** (e.g., 4:2:2 or 4:2:0 formats) to compress video bandwidth by up to 50% without noticeable visual degradation.

---

### 2.3 Master Summary Table of Colour Models

| Model | Category | Key Components | Geometry / Representation | Primary Application |
| :--- | :--- | :--- | :--- | :--- |
| **RGB** | Additive Light | Red, Green, Blue | 3D Cartesian Unit Cube | Monitors, TVs, Digital Sensors |
| **CMY** | Subtractive Ink | Cyan, Magenta, Yellow | Complementary Cartesian Cube | Basic Color Printers |
| **CMYK** | Subtractive Printing | Cyan, Magenta, Yellow, Black | 4D Normalized Vector Space | Commercial Offset Printing |
| **HSI** | Perceptual | Hue, Saturation, Intensity | Double Pyramid / Double Cone | Human Perception, Image Processing |
| **HSV** | Perceptual | Hue, Saturation, Value | Inverted Single Hexcone | Computer Graphics, UI Color Pickers |
| **YUV** | Transmission / Video | Luminance ($`Y`$), Chrominance ($`U, V`$) | Linear Matrix Transformation | Video Encoding, PAL/NTSC Broadcasting |

---

## 3. Mathematical Transformations Between Colour Spaces

All colour model conversions assume normalized RGB values in the range $`R, G, B \in [0, 1]`$. If input RGB values are given in 8-bit scale ($`0`$ to $`255`$), they must first be divided by $`255`$.

---

### 3.1 RGB to CMY and CMY to CMYK Transformations

#### 1. RGB to CMY Conversion

```math
C = 1 - R, \quad M = 1 - G, \quad Y = 1 - B
```

#### 2. CMY to RGB Conversion

```math
R = 1 - C, \quad G = 1 - M, \quad B = 1 - Y
```

#### 3. CMY to CMYK Conversion
To extract pure black ($`K`$) and scale the remaining color pigments ($`C', M', Y'`$):

```math
K = \min(C, M, Y)
```

If $`K = 1`$ (pure black), then $`C' = 0, M' = 0, Y' = 0`$. Otherwise:

```math
C' = \frac{C - K}{1 - K}, \quad M' = \frac{M - K}{1 - K}, \quad Y' = \frac{Y - K}{1 - K}
```

#### 4. CMYK to CMY Conversion

```math
C = C' \cdot (1 - K) + K, \quad M = M' \cdot (1 - K) + K, \quad Y = Y' \cdot (1 - K) + K
```

---

### 3.2 RGB to HSI Transformation Derivations

Given normalized $`R, G, B \in [0, 1]`$:

#### 1. Intensity Component ($`I`$)

```math
I = \frac{1}{3}(R + G + B)
```

#### 2. Saturation Component ($`S`$)

```math
S = 1 - \frac{3}{R + G + B} \left[ \min(R, G, B) \right]
```

If $`R = G = B`$ (grayscale pixel), $`S = 0`$.

#### 3. Hue Component ($`H`$)

```math
\theta = \cos^{-1} \left[ \frac{\frac{1}{2} \left[ (R - G) + (R - B) \right]}{\sqrt{(R - G)^2 + (R - B)(G - B)}} \right]
```

The hue angle $`H`$ (in degrees) is calculated based on the blue-green relationship:

```math
H = \begin{cases} \theta & \text{if } B \le G \\ 360^\circ - \theta & \text{if } B > G \end{cases}
```

---

### 3.3 HSI to RGB Transformation Equations

Given normalized HSI values with $`H \in [0^\circ, 360^\circ]`$, $`S \in [0, 1]`$, and $`I \in [0, 1]`$:

#### Case 1: RG Sector ($`0^\circ \le H < 120^\circ`$)

```math
B = I(1 - S)
```

```math
R = I \left[ 1 + \frac{S \cos(H)}{\cos(60^\circ - H)} \right]
```

```math
G = 3I - (R + B)
```

#### Case 2: GB Sector ($`120^\circ \le H < 240^\circ`$)
Subtract $`120^\circ`$ from hue: $`H' = H - 120^\circ`$.

```math
R = I(1 - S)
```

```math
G = I \left[ 1 + \frac{S \cos(H')}{\cos(60^\circ - H')} \right]
```

```math
B = 3I - (R + G)
```

#### Case 3: BR Sector ($`240^\circ \le H < 360^\circ`$)
Subtract $`240^\circ`$ from hue: $`H' = H - 240^\circ`$.

```math
G = I(1 - S)
```

```math
B = I \left[ 1 + \frac{S \cos(H')}{\cos(60^\circ - H')} \right]
```

```math
R = 3I - (G + B)
```

---

### 3.4 RGB to HSV Transformation

Given normalized $`R, G, B \in [0, 1]`$:

Let $`M_{\max} = \max(R, G, B)`$, $`M_{\min} = \min(R, G, B)`$, and $`\Delta = M_{\max} - M_{\min}`$.

#### 1. Value ($`V`$)

```math
V = M_{\max}
```

#### 2. Saturation ($`S`$)

```math
S = \begin{cases} 0 & \text{if } V = 0 \\ \frac{\Delta}{V} & \text{if } V \neq 0 \end{cases}
```

#### 3. Hue ($`H`$)

```math
H = \begin{cases} 0^\circ & \text{if } \Delta = 0 \\ 60^\circ \times \left( \frac{G - B}{\Delta} \bmod 6 \right) & \text{if } V = R \\ 60^\circ \times \left( \frac{B - R}{\Delta} + 2 \right) & \text{if } V = G \\ 60^\circ \times \left( \frac{R - G}{\Delta} + 4 \right) & \text{if } V = B \end{cases}
```

If $`H < 0^\circ`$, add $`360^\circ`$.

---

### 3.5 Linear Matrix Transformations: RGB to YUV

For NTSC / PAL television encoding standards, normalized RGB is transformed into YUV space via linear matrix multiplication:

#### Forward Transformation (RGB to YUV)

```math
\begin{bmatrix} Y \\ U \\ V \end{bmatrix} = \begin{bmatrix} 0.299 & 0.587 & 0.114 \\ -0.14713 & -0.28886 & 0.436 \\ 0.615 & -0.51499 & -0.10001 \end{bmatrix} \begin{bmatrix} R \\ G \\ B \end{bmatrix}
```

Simplified standard approximation equations:

```math
Y = 0.299 R + 0.587 G + 0.114 B
```

```math
U = 0.492 (B - Y)
```

```math
V = 0.877 (R - Y)
```

#### Inverse Transformation (YUV to RGB)

```math
R = Y + 1.140 V
```

```math
G = Y - 0.395 U - 0.581 V
```

```math
B = Y + 2.032 U
```

---

## 4. Vector-Based Colour Slicing and Spatial Segmentation

Colour slicing is a technique used to isolate and highlight a specific range of colours in an image while suppressing or converting surrounding background colours to monochrome gray.

Unlike scalar grayscale thresholding, colour processing requires **vector-based slicing** because each pixel is represented by a 3D colour vector $`\mathbf{z} = [R, G, B]^T`$.

---

### 4.1 Spherical vs. Cubic Colour Slicing Formulations

Let $`\mathbf{a} = [R_0, G_0, B_0]^T`$ represent the prototype target color vector, and let $`\mathbf{z} = [R, G, B]^T`$ be any arbitrary pixel vector.

#### 1. Cubic (Hyper-Cube) Colour Slicing
Define a 3D bounding box centered at prototype color $`\mathbf{a}`$ with radius threshold $`W`$:

```math
g(x,y) = \begin{cases} [R_{\text{pass}}, G_{\text{pass}}, B_{\text{pass}}]^T & \text{if } \lvert R - R_0 \rvert \le \frac{W}{2} \text{ AND } \lvert G - G_0 \rvert \le \frac{W}{2} \text{ AND } \lvert B - B_0 \rvert \le \frac{W}{2} \\ [0.5, 0.5, 0.5]^T & \text{otherwise} \end{cases}
```

#### 2. Spherical (Euclidean Distance) Colour Slicing
Define a 3D sphere centered at $`\mathbf{a}`$ with distance threshold $`D_0`$:

```math
D(\mathbf{z}, \mathbf{a}) = \sqrt{(R - R_0)^2 + (G - G_0)^2 + (B - B_0)^2}
```

```math
g(x,y) = \begin{cases} \mathbf{z} & \text{if } D(\mathbf{z}, \mathbf{a}) \le D_0 \\ [0.5, 0.5, 0.5]^T & \text{otherwise} \end{cases}
```

```text
Colour Slicing Geometries:
  Cubic Bounding Box:                     Spherical Euclidean Boundary:
  +---------------+                       /-------------\
  |   (R0,G0,B0)  |                      /  (R0,G0,B0)   \
  |       *       |                     |        *        |
  |               |                      \   D0 Radius   /
  +---------------+                       \-------------/
```

---

## 5. Histogram Processing and Enhancement of Colour Images

Histogram processing techniques (such as histogram equalization) enhance image contrast by redistributing pixel intensity distributions. However, directly applying histogram equalization to individual $`R`$, $`G`$, and $`B`$ channels independently leads to severe **colour distortion** and unnatural hue shifts.

---

### 5.1 Why Independent RGB Channel Equalization Fails

When histogram equalization is computed independently on the Red, Green, and Blue channels:

1. **Hue Shift:** Equalization non-linearly alters the ratios between $`R`$, $`G`$, and $`B`$ components ($`R:G:B`$). Since hue depends strictly on relative channel ratios, the original colours of objects are drastically altered (e.g., skin tones turn purple or green).
2. **Saturation Artifacts:** Independent channel stretching creates unnatural, over-saturated or washed-out pixels.

---

### 5.2 Correct Protocol: Intensity-Decoupled Colour Enhancement

To enhance contrast without altering object colour (hue and saturation), histogram processing must be applied to an **intensity-decoupled colour model** (such as HSI, HSV, or YUV).

#### Step-by-Step Enhancement Protocol

1. **Colour Space Transformation:** Convert the input image from RGB to a decoupled colour space (e.g., HSI or YUV).
2. **Intensity Channel Processing:** Extract the Intensity ($`I`$), Value ($`V`$), or Luminance ($`Y`$) channel. Apply histogram equalization or contrast stretching **only** to this monochromatic component.
3. **Preserve Chrominance:** Leave the Hue ($`H`$) and Saturation ($`S`$) channels completely unmodified.
4. **Inverse Transformation:** Recombine the modified intensity channel with the original hue and saturation channels, and convert back to RGB for display.

```text
Correct Colour Enhancement Pipeline:
Input RGB ---> [ RGB to HSI ] ---> Separate Channels: H, S (Preserved Unmodified)
                                                ---> I (Histogram Equalization)
                                                         |
Recombined H, S, I_equalized ---> [ HSI to RGB ] ---> Output Enhanced RGB
```

---

## 6. Worked Step-by-Step Numerical Examples

### Worked Numerical 1: RGB to CMY and CMYK Model Conversion

#### Problem Statement
Given an un-normalized RGB pixel with color values $`R = 51`$, $`G = 102`$, $`B = 178.5`$ (on a $`0-255`$ 8-bit scale):
1. Normalize the RGB values to the range $`[0, 1]`$.
2. Calculate the corresponding CMY color representation.
3. Extract the key black component $`K`$ and calculate the final CMYK representation.

Carry calculations to 4 decimal places.

---

#### Step-by-Step Solution

##### Step 1: Normalize RGB Values to $`[0, 1]`$

```math
R_{\text{norm}} = \frac{51}{255} = 0.2000
```

```math
G_{\text{norm}} = \frac{102}{255} = 0.4000
```

```math
B_{\text{norm}} = \frac{178.5}{255} = 0.7000
```

##### Step 2: Compute CMY Values

```math
C = 1 - R_{\text{norm}} = 1 - 0.2000 = 0.8000
```

```math
M = 1 - G_{\text{norm}} = 1 - 0.4000 = 0.6000
```

```math
Y = 1 - B_{\text{norm}} = 1 - 0.7000 = 0.3000
```

Thus, $`\text{CMY} = (0.8000, 0.6000, 0.3000)`$.

##### Step 3: Compute CMYK Values

1. **Key / Black ($`K`$):**

```math
K = \min(C, M, Y) = \min(0.8000, 0.6000, 0.3000) = 0.3000
```

2. **Scaled Pigments ($`C', M', Y'`$):**

```math
C' = \frac{C - K}{1 - K} = \frac{0.8000 - 0.3000}{1 - 0.3000} = \frac{0.5000}{0.7000} \approx 0.7143
```

```math
M' = \frac{M - K}{1 - K} = \frac{0.6000 - 0.3000}{1 - 0.3000} = \frac{0.3000}{0.7000} \approx 0.4286
```

```math
Y' = \frac{Y - K}{1 - K} = \frac{0.3000 - 0.3000}{1 - 0.3000} = \frac{0.0000}{0.7000} = 0.0000
```

Final Answer:
* **Normalized RGB:** $`(0.2000, 0.4000, 0.7000)`$
* **CMY Representation:** $`(0.8000, 0.6000, 0.3000)`$
* **CMYK Representation:** $`(0.7143, 0.4286, 0.0000, 0.3000)`$

---

### Worked Numerical 2: RGB to HSI Model Conversion

#### Problem Statement
Given a normalized RGB pixel with coordinates $`R = 0.5000`$, $`G = 0.4000`$, and $`B = 0.2000`$:
1. Calculate the Intensity component ($`I`$).
2. Calculate the Saturation component ($`S`$).
3. Calculate the Hue component angle ($`H`$).

Carry calculations to 4 decimal places.

---

#### Step-by-Step Solution

##### Step 1: Calculate Intensity ($`I`$)

```math
I = \frac{1}{3}(R + G + B) = \frac{0.5000 + 0.4000 + 0.2000}{3} = \frac{1.1000}{3} \approx 0.3667
```

##### Step 2: Calculate Saturation ($`S`$)

```math
\min(R, G, B) = \min(0.5000, 0.4000, 0.2000) = 0.2000
```

```math
S = 1 - \frac{3}{R + G + B} \left[ \min(R, G, B) \right] = 1 - \frac{3}{1.1000} (0.2000) = 1 - \frac{0.6000}{1.1000} \approx 1 - 0.5455 = 0.4545
```

##### Step 3: Calculate Hue Angle ($`H`$)

1. **Numerator:**

```math
\text{Num} = \frac{1}{2} \left[ (R - G) + (R - B) \right] = \frac{1}{2} \left[ (0.5000 - 0.4000) + (0.5000 - 0.2000) \right] = \frac{1}{2} [0.1000 + 0.3000] = 0.2000
```

2. **Denominator:**

```math
(R - G)^2 = (0.5000 - 0.4000)^2 = (0.1000)^2 = 0.0100
```

```math
(R - B)(G - B) = (0.5000 - 0.2000)(0.4000 - 0.2000) = (0.3000)(0.2000) = 0.0600
```

```math
\text{Denom} = \sqrt{0.0100 + 0.0600} = \sqrt{0.0700} \approx 0.2646
```

3. **Theta Angle ($\theta$):**

```math
\cos(\theta) = \frac{0.2000}{0.2646} \approx 0.7559
```

```math
\theta = \cos^{-1}(0.7559) \approx 40.89^\circ
```

4. **Case Evaluation:**
   Since $`B = 0.2000 \le G = 0.4000`$, condition $`B \le G`$ holds true.
   Therefore, $`H = \theta = 40.89^\circ`$.

Final Answer:
* **Intensity ($`I`$):** $`0.3667`$
* **Saturation ($`S`$):** $`0.4545`$
* **Hue ($`H`$):** $`40.89^\circ`$ (or $`0.1136`$ when normalized to $`[0, 1]`$ by dividing by $`360^\circ`$)

---

### Worked Numerical 3: RGB to YUV Transmission Transformation

#### Problem Statement
Given an RGB pixel $`R = 0.6000`$, $`G = 0.2000`$, $`B = 0.1000`$:
1. Compute Luminance $`Y`$.
2. Compute Chrominance components $`U`$ and $`V`$.
3. Perform inverse transformation to verify recovery of original RGB.

Carry calculations to 4 decimal places.

---

#### Step-by-Step Solution

##### Step 1: Forward Transformation (RGB to YUV)

1. **Luminance ($`Y`$):**

```math
Y = 0.299 (0.6000) + 0.587 (0.2000) + 0.114 (0.1000) = 0.1794 + 0.1174 + 0.0114 = 0.3082
```

2. **Chrominance ($`U`$):**

```math
U = 0.492 (B - Y) = 0.492 (0.1000 - 0.3082) = 0.492 (-0.2082) \approx -0.1024
```

3. **Chrominance ($`V`$):**

```math
V = 0.877 (R - Y) = 0.877 (0.6000 - 0.3082) = 0.877 (0.2918) \approx 0.2559
```

##### Step 2: Inverse Transformation (YUV to RGB Verification)

1. **Recover Red ($`R`$):**

```math
R = Y + 1.140 V = 0.3082 + 1.140 (0.2559) = 0.3082 + 0.2917 = 0.5999 \approx 0.6000
```

2. **Recover Green ($`G`$):**

```math
G = Y - 0.395 U - 0.581 V = 0.3082 - 0.395 (-0.1024) - 0.581 (0.2559)
```

```math
G = 0.3082 + 0.0404 - 0.1487 = 0.1999 \approx 0.2000
```

3. **Recover Blue ($`B`$):**

```math
B = Y + 2.032 U = 0.3082 + 2.032 (-0.1024) = 0.3082 - 0.2081 = 0.1001 \approx 0.1000
```

Final Answer:
* **Forward YUV Vector:** $`Y = 0.3082`$, $`U = -0.1024`$, $`V = 0.2559`$
* **Recovered RGB Vector:** $`R = 0.6000`$, $`G = 0.2000`$, $`B = 0.1000`$ (Exact match)

---

## 7. High-Yield Exam Summary and Formula Cheat Sheet

### 7.1 Master Formula Cheat Sheet

1. **RGB to CMY:**

```math
C = 1 - R, \quad M = 1 - G, \quad Y = 1 - B
```

2. **CMY to CMYK:**

```math
K = \min(C, M, Y), \quad C' = \frac{C - K}{1 - K}, \quad M' = \frac{M - K}{1 - K}, \quad Y' = \frac{Y - K}{1 - K}
```

3. **RGB to HSI Intensity & Saturation:**

```math
I = \frac{1}{3}(R + G + B), \quad S = 1 - \frac{3}{R + G + B} \left[ \min(R, G, B) \right]
```

4. **RGB to HSI Hue Angle:**

```math
\theta = \cos^{-1} \left[ \frac{\frac{1}{2} \left[ (R - G) + (R - B) \right]}{\sqrt{(R - G)^2 + (R - B)(G - B)}} \right], \quad H = \begin{cases} \theta & \text{if } B \le G \\ 360^\circ - \theta & \text{if } B > G \end{cases}
```

5. **RGB to YUV Transmission:**

```math
Y = 0.299 R + 0.587 G + 0.114 B, \quad U = 0.492(B - Y), \quad V = 0.877(R - Y)
```

6. **Spherical Colour Slicing Distance:**

```math
D(\mathbf{z}, \mathbf{a}) = \sqrt{(R - R_0)^2 + (G - G_0)^2 + (B - B_0)^2} \le D_0
```

---

### 7.2 Exam Pitfalls and Revision Checklist

* **Normalization First:** Always check whether RGB values are given in $`0-255`$ or normalized $`[0, 1]`$. Divide by $`255`$ before evaluating HSI or CMY conversion equations.
* **Hue Case Condition:** Never forget to check if $`B > G`$ in HSI conversion. If $`B > G`$, hue must be subtracted from $`360^\circ`$ ($`H = 360^\circ - \theta`$).
* **Histogram Distortion:** In theory questions, emphasize that histogram equalization must **never** be applied directly to RGB channels individually due to non-linear hue shifting. Always convert to HSI/HSV/YUV first and process only the intensity/luminance channel.
