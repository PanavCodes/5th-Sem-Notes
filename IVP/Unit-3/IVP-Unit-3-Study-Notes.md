# 📚 IVP Unit 3: Image Transforms — Comprehensive Study Notes

---

## 📌 Syllabus & Exam Scope Coverage Checklist

| Syllabus Topic | Sub-Topics & Concepts | Included Section | Coverage Status |
| :--- | :--- | :--- | :---: |
| **1. Discrete Fourier Transform (DFT)** | Spatial vs. Frequency Domain, 2D DFT & IDFT equations, Magnitude & Phase, DC Component, Centering, Twiddle Factor Matrix ($W_N$), Separability, Periodicity, Conjugate Symmetry, Parseval's Relation, $2 \times 2$ & $4 \times 4$ Worked Numericals | [Section 1](#1-discrete-fourier-transform-dft) | ✅ Complete |
| **2. Hadamard Transform** | Hadamard Matrix ($H_N$), $+1/-1$ Binary Basis, Orthogonality, Recursive Generation ($H_{2N} = H_2 \otimes H_N$), Sequency Ordering, Normalized vs. Unnormalized Conventions, 1D & $4 \times 4$ 2D Worked Numericals | [Section 2](#2-hadamard-transform) | ✅ Complete |
| **3. Discrete Cosine Transform (DCT) & Compression** | 1D & 2D DCT/IDCT Formulations, Real-Valued Cosine Basis, Orthogonal Coefficient Matrix ($C$), Energy Compaction, DCT vs. DFT Comparison, JPEG Compression Workflow ($8 \times 8$ Blocks, Level Shift, Quantization, Zig-Zag, Reconstruction), $4 \times 4$ Worked Numerical | [Section 3](#3-discrete-cosine-transform-dct-and-image-compression) | ✅ Complete |
| **Transform Comparisons** | Energy Compaction, Computational Complexity, Basis Functions, Artifacts, Primary Applications | [Section 4](#4-comparative-analysis-of-image-transforms) | ✅ Complete |
| **Formula & Matrix Reference** | Complete Formula Sheet, Twiddle Matrices, Hadamard Matrices, DCT Matrices | [Section 5](#5-formula-and-transform-matrix-master-reference) | ✅ Complete |
| **Common Exam Mistakes** | Pitfalls in Centering, Scaling, Sequency, Matrix Multiplication, and Quantization | [Section 6](#6-common-exam-mistakes-and-pitfalls) | ✅ Complete |
| **Quick Revision & Checklist** | Last-Minute Summary & Complete Readiness Verification | [Section 7](#7-quick-revision-and-last-minute-checklist) | ✅ Complete |

---

## 📑 Table of Contents

1. [Section 1: Discrete Fourier Transform (DFT)](#1-discrete-fourier-transform-dft)
   * 1.1 [Spatial Domain vs Frequency Domain Representation](#11-spatial-domain-vs-frequency-domain-representation)
   * 1.2 [Mathematical Formulation of 2D DFT and IDFT](#12-mathematical-formulation-of-2d-dft-and-idft)
   * 1.3 [Fourier Spectrum, Phase Angle, Power Spectrum, and DC Component](#13-fourier-spectrum-phase-angle-power-spectrum-and-dc-component)
   * 1.4 [Frequency Centering Property (-1)^(x+y)](#14-frequency-centering-property--1xy)
   * 1.5 [Matrix Formulation and Twiddle Factor Matrix W_N](#15-matrix-formulation-and-twiddle-factor-matrix-w_n)
   * 1.6 [Key Properties of 2D DFT](#16-key-properties-of-2d-dft)
   * 1.7 [Worked Numerical Examples (2x2 and 4x4 DFT)](#17-worked-numerical-examples-2x2-and-4x4-dft)
2. [Section 2: Hadamard Transform](#2-hadamard-transform)
   * 2.1 [Definition and Basis Functions](#21-definition-and-basis-functions)
   * 2.2 [Hadamard Matrix Properties and Orthogonality](#22-hadamard-matrix-properties-and-orthogonality)
   * 2.3 [Recursive Construction and Sequency Ordering](#23-recursive-construction-and-sequency-ordering)
   * 2.4 [Normalized vs Unnormalized Conventions](#24-normalized-vs-unnormalized-conventions)
   * 2.5 [Forward and Inverse 2D Hadamard Transform Formulation](#25-forward-and-inverse-2d-hadamard-transform-formulation)
   * 2.6 [Worked Numerical Examples (1D Sequence and 4x4 Image)](#26-worked-numerical-examples-1d-sequence-and-4x4-image)
3. [Section 3: Discrete Cosine Transform (DCT) and Image Compression](#3-discrete-cosine-transform-dct-and-image-compression)
   * 3.1 [Mathematical Definition of 1D and 2D DCT and IDCT](#31-mathematical-definition-of-1d-and-2d-dct-and-idct)
   * 3.2 [Cosine Basis Functions and Real-Valued Computation](#32-cosine-basis-functions-and-real-valued-computation)
   * 3.3 [Energy Compaction Property and DC vs AC Coefficients](#33-energy-compaction-property-and-dc-vs-ac-coefficients)
   * 3.4 [Why DCT is Preferred over DFT for Image Compression](#34-why-dct-is-preferred-over-dft-for-image-compression)
   * 3.5 [JPEG Image Compression Workflow (8x8 Block Processing)](#35-jpeg-image-compression-workflow-8x8-block-processing)
   * 3.6 [Worked Numerical Example (4x4 DCT Matrix Multiplication)](#36-worked-numerical-example-4x4-dct-matrix-multiplication)
4. [Section 4: Comparative Analysis of Image Transforms](#4-comparative-analysis-of-image-transforms)
5. [Section 5: Formula and Transform Matrix Master Reference](#5-formula-and-transform-matrix-master-reference)
6. [Section 6: Common Exam Mistakes and Pitfalls](#6-common-exam-mistakes-and-pitfalls)
7. [Section 7: Quick Revision and Last-Minute Checklist](#7-quick-revision-and-last-minute-checklist)

---

<a id="1-discrete-fourier-transform-dft"></a>

## 1. Discrete Fourier Transform (DFT)

<a id="11-spatial-domain-vs-frequency-domain-representation"></a>

### 1.1 Spatial Domain vs Frequency Domain Representation

In digital image processing, an image can be represented in two complementary domains:

```text
+-----------------------------------------------------------------------+
|                           SPATIAL DOMAIN                              |
| Represents image as a 2D grid of pixel intensities f(x,y).            |
| Coordinates (x,y) specify physical spatial positions.                 |
+-----------------------------------------------------------------------+
                                  │
                                  │ Forward 2D DFT [F(u,v) = F{f(x,y)}]
                                  ▼
+-----------------------------------------------------------------------+
|                          FREQUENCY DOMAIN                             |
| Represents image by the rate of spatial intensity variations.          |
| Frequency indices (u,v) specify horizontal & vertical spatial frequencies.|
+-----------------------------------------------------------------------+
                                  │
                                  │ Inverse 2D DFT [f(x,y) = F^-1{F(u,v)}]
                                  ▼
+-----------------------------------------------------------------------+
|                 RECONSTRUCTED SPATIAL IMAGE f(x,y)                    |
+-----------------------------------------------------------------------+
```

* **Spatial Domain:** Images are represented directly by pixel intensities $f(x,y)$ at spatial coordinates $(x,y)$, where $x \in \{0, 1, \dots, M-1\}$ and $y \in \{0, 1, \dots, N-1\}$.
* **Frequency Domain:** Images are decomposed into a sum of complex sinusoidal basis functions oscillating at various spatial frequencies $(u,v)$.
  * **Low Frequencies (near origin):** Correspond to smooth, gradually varying intensity regions (e.g., background, flat surfaces).
  * **High Frequencies (away from origin):** Correspond to abrupt intensity changes, sharp edges, fine textures, and noise.

---

<a id="12-mathematical-formulation-of-2d-dft-and-idft"></a>

### 1.2 Mathematical Formulation of 2D DFT and IDFT

For an $M \times N$ discrete digital image $f(x,y)$, the **Forward 2D Discrete Fourier Transform (2D DFT)** converts spatial pixels into complex frequency coefficients $F(u,v)$:

```math
F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) \cdot e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}
```

where:
* $x, u \in \{0, 1, \dots, M-1\}$ are spatial row coordinate and row-direction frequency index.
* $y, v \in \{0, 1, \dots, N-1\}$ are spatial column coordinate and column-direction frequency index.
* $j = \sqrt{-1}$ is the imaginary unit.

The **Inverse 2D Discrete Fourier Transform (2D IDFT)** exactly reconstructs the spatial image $f(x,y)$ from its frequency spectrum $F(u,v)$:

```math
f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) \cdot e^{+j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}
```

> 🧠 **Normalization Convention Note:** In standard DIP terminology (Gonzalez & Woods), the forward transform has a scaling factor of $1$ and the inverse transform carries $\frac{1}{MN}$. Some symmetric mathematical formulations place $\frac{1}{\sqrt{MN}}$ on both forward and inverse operations. In exam problems, always state the normalization convention being used!

---

<a id="13-fourier-spectrum-phase-angle-power-spectrum-and-dc-component"></a>

### 1.3 Fourier Spectrum, Phase Angle, Power Spectrum, and DC Component

Since $F(u,v)$ is a complex quantity, it can be expressed in rectangular or polar form:

```math
F(u,v) = R(u,v) + j \cdot I(u,v) = |F(u,v)| \cdot e^{j \phi(u,v)}
```

where $R(u,v)$ is the real part and $I(u,v)$ is the imaginary part.

1. **Fourier Magnitude Spectrum $|F(u,v)|$:**
   Represents the energy/amplitude of spatial frequency $(u,v)$:

```math
   |F(u,v)| = \sqrt{R^2(u,v) + I^2(u,v)}
```

2. **Phase Angle $\phi(u,v)$:**
   Contains essential structural and positional information of image features:

```math
   \phi(u,v) = \tan^{-1}\left( \frac{I(u,v)}{R(u,v)} \right)
```

3. **Power Spectrum $P(u,v)$:**
   Represents the power distribution across frequencies:

```math
   P(u,v) = |F(u,v)|^2 = R^2(u,v) + I^2(u,v)
```

4. **DC Component $F(0,0)$:**
   At zero frequency $(u=0, v=0)$, the exponential term reduces to $e^0 = 1$:

```math
   F(0,0) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) = MN \cdot \bar{f}
```

   The DC component equals $MN$ times the average spatial intensity $\bar{f}$ of the image.

---

<a id="14-frequency-centering-property--1xy"></a>

### 1.4 Frequency Centering Property (-1)^(x+y)

By default, the 2D DFT places the zero-frequency (DC) component $F(0,0)$ at the top-left corner of the $M \times N$ matrix. For even $M$ and $N$, to center $F(0,0)$ at $(M/2, N/2)$ for intuitive spectrum visualization and frequency domain filtering (indices interpreted modulo $M,N$):

```math
f'(x,y) = f(x,y) \cdot (-1)^{x+y} \quad \stackrel{\mathcal{F}}{\Longleftrightarrow} \quad F'(u,v) = F\left(u - \frac{M}{2}, v - \frac{N}{2}\right)
```

**Proof:**
Using Euler's identity, $(-1)^{x+y} = e^{j\pi(x+y)} = e^{j 2\pi (x \cdot \frac{M/2}{M} + y \cdot \frac{N/2}{N})}$.
Multiplying $f(x,y)$ by $(-1)^{x+y}$ in the spatial domain applies a frequency shift of $u_0 = M/2$ and $v_0 = N/2$ in the frequency domain.

---

<a id="15-matrix-formulation-and-twiddle-factor-matrix-w_n"></a>

### 1.5 Matrix Formulation and Twiddle Factor Matrix W_N

The 1D DFT of a column vector $\mathbf{x}$ of length $N$ is expressed using the **Twiddle Factor Matrix** $W_N$:

```math
\mathbf{X} = W_N \cdot \mathbf{x}
```

where the twiddle factor entries are defined as:

```math
(W_N)_{k,n} = e^{-j \frac{2\pi}{N} k n} \quad \text{for } k,n \in \{0, 1, \dots, N-1\}
```

#### Standard Twiddle Factor Matrices:

* **2x2 Twiddle Matrix $W_2$:**
  Since $e^{-j\pi} = -1$:

```math
  W_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

* **4x4 Twiddle Matrix $W_4$:**
  Since $e^{-j\pi/2} = -j$, $e^{-j\pi} = -1$, and $e^{-j 3\pi/2} = j$:

```math
  W_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

#### 2D DFT Matrix Multiplication:
For an $M \times N$ spatial image matrix $f$, the 2D DFT matrix $F$ is computed using separable 1D transformations:

```math
F = W_M \cdot f \cdot W_N^T
```

And the 2D IDFT matrix reconstruction is given by:

```math
f = \frac{1}{MN} W_M^H \cdot F \cdot (W_N^T)^H = \frac{1}{MN} W_M^* \cdot F \cdot W_N^*
```

where $W^*$ means elementwise conjugation and $W^H=(W^*)^T$ means conjugate transpose. The DFT twiddle matrices are symmetric, so $W_M^H=W_M^*$ in this particular formula.

---

<a id="16-key-properties-of-2d-dft"></a>

### 1.6 Key Properties of 2D DFT

1. **Separability:**
   A 2D DFT can be computed by taking 1D DFTs along the rows of $f(x,y)$, followed by 1D DFTs along the columns of the intermediate result:

```math
   F(u,v) = \sum_{x=0}^{M-1} \left[ \sum_{y=0}^{N-1} f(x,y)e^{-j2\pi vy/N} \right]e^{-j2\pi ux/M}
```

2. **Periodicity:**
   The 2D DFT and its inverse are infinitely periodic with periods $M$ and $N$:

```math
   F(u,v) = F(u + k_1 M, v + k_2 N) \quad \text{for any integers } k_1, k_2
```

3. **Conjugate Symmetry (for Real Images):**
   If $f(x,y)$ is real-valued, its Fourier transform exhibits conjugate symmetry about the origin:

```math
   F(u,v) = F^*(-u, -v) \implies |F(u,v)| = |F(-u, -v)|
```

4. **Parseval's Theorem (Energy Conservation):**
   Total energy in the spatial domain equals total energy in the frequency domain:

```math
   \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} |f(x,y)|^2 = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} |F(u,v)|^2
```

---

<a id="17-worked-numerical-examples-2x2-and-4x4-dft"></a>

### 1.7 Worked Numerical Examples (2x2 and 4x4 DFT)

#### 📍 Worked Problem 1.1: 2x2 2D DFT Calculation

**Given Image $f$:**

```math
f = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
```

**Task:** Compute the 2D DFT $F = W_2 \cdot f \cdot W_2^T$ and verify IDFT reconstruction.

**Step-by-Step Solution:**

1. **Twiddle Matrix $W_2$:**

```math
   W_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

2. **Step 1: Compute Row Transform $R = W_2 \cdot f$:**

```math
   R = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} = \begin{bmatrix}
(1+3) & (2+4) \\
(1-3) & (2-4)
\end{bmatrix} = \begin{bmatrix}
4 & 6 \\
-2 & -2
\end{bmatrix}
```

3. **Step 2: Compute Column Transform $F = R \cdot W_2^T$:**

```math
   F = \begin{bmatrix}
4 & 6 \\
-2 & -2
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
(4+6) & (4-6) \\
(-2-2) & (-2+2)
\end{bmatrix} = \begin{bmatrix}
10 & -2 \\
-4 & 0
\end{bmatrix}
```

4. **Verification via IDFT ($f = \frac{1}{4} W_2^* \cdot F \cdot W_2^*$):**

```math
   W_2^* \cdot F = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
10 & -2 \\
-4 & 0
\end{bmatrix} = \begin{bmatrix}
6 & -2 \\
14 & -2
\end{bmatrix}
```

```math
   (W_2^* \cdot F) \cdot W_2^* = \begin{bmatrix}
6 & -2 \\
14 & -2
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
4 & 8 \\
12 & 16
\end{bmatrix}
```

```math
   f = \frac{1}{4} \begin{bmatrix}
4 & 8 \\
12 & 16
\end{bmatrix} = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} \quad \text{(Exact Match!)}
```

---

#### 📍 Worked Problem 1.2: 4x4 2D DFT Calculation

**Given Image $f$:**

```math
f = \begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12 \\
13 & 14 & 15 & 16
\end{bmatrix}
```

**Step 1: Row Transformation $R = W_4 \cdot f$**

```math
R = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix} \begin{bmatrix}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12 \\
13 & 14 & 15 & 16
\end{bmatrix} = \begin{bmatrix}
28 & 32 & 36 & 40 \\
-8+8j & -8+8j & -8+8j & -8+8j \\
-8 & -8 & -8 & -8 \\
-8-8j & -8-8j & -8-8j & -8-8j
\end{bmatrix}
```

**Step 2: Column Transformation $F = R \cdot W_4^T$**

```math
F = \begin{bmatrix}
28 & 32 & 36 & 40 \\
-8+8j & -8+8j & -8+8j & -8+8j \\
-8 & -8 & -8 & -8 \\
-8-8j & -8-8j & -8-8j & -8-8j
\end{bmatrix} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

```math
F = \begin{bmatrix}
136 & -8+8j & -8 & -8-8j \\
-32+32j & 0 & 0 & 0 \\
-32 & 0 & 0 & 0 \\
-32-32j & 0 & 0 & 0
\end{bmatrix}
```

> ✍️ **Exam Key Takeaway:**
> * $F(0,0) = 136 = \sum \text{all pixels}$ (DC Component!).
> * All AC off-diagonal coefficients in this linear gradient matrix evaluate strictly to $0$.

---

<a id="2-hadamard-transform"></a>

## 2. Hadamard Transform

<a id="21-definition-and-basis-functions"></a>

### 2.1 Definition and Basis Functions

The **Hadamard Transform** (also known as the Walsh-Hadamard Transform) is a non-sinusoidal orthogonal transform that decomposes an image into a set of rectangular, binary square-wave basis functions taking values of strictly $+1$ and $-1$.

```text
 sinusoidal Basis (DFT / DCT)          Binary Square-Wave Basis (Hadamard)
      Smooth Continuous Waves                   Rectangular Step Waves
    ~~~~~~~~~~~~~~~~~~~~~~~~~~                 ┌──┐  ┌──┐  ┌──┐  ┌──┐
    ~~~~~~~~~~~~~~~~~~~~~~~~~~                 └──┘  └──┘  └──┘  └──┘
  Requires Complex/Float Mults               Zero Multiplications (+ / - Only)
```

---

<a id="22-hadamard-matrix-properties-and-orthogonality"></a>

### 2.2 Hadamard Matrix Properties and Orthogonality

A Hadamard matrix $H_N$ of order $N$ is an $N \times N$ matrix whose entries are strictly $+1$ or $-1$. The Sylvester matrices displayed below are symmetric; a general Hadamard matrix need not be.

1. **Orthogonality:**
   The rows (and columns) of $H_N$ are mutually orthogonal:

```math
   H_N \cdot H_N^T = N \cdot I_N
```

2. **Symmetry & Inverse:**
   Orthogonality gives the general inverse; for the symmetric Sylvester matrices shown here, $H_N^T=H_N$:

```math
   H_N^{-1} = \frac{1}{N} H_N^T \quad (\text{equal to }H_N/N\text{ for symmetric Sylvester matrices})
```

3. **Matrix Order Requirement:**
   A necessary order condition is $N=1$, $N=2$, or $N=4k$ for a positive integer $k$. Existence for every multiple of four is not established. The recursive Sylvester construction below produces powers of two, commonly used in image processing.

---

<a id="23-recursive-construction-and-sequency-ordering"></a>

### 2.3 Recursive Construction and Sequency Ordering

Hadamard matrices of order $2^n$ are generated recursively using the **Kronecker Product (Tensor Product)**:

```math
H_{2N} = H_2 \otimes H_N = \begin{bmatrix}
1 \cdot H_N & 1 \cdot H_N \\
1 \cdot H_N & -1 \cdot H_N
\end{bmatrix} = \begin{bmatrix}
H_N & H_N \\
H_N & -H_N
\end{bmatrix}
```

#### 1. Base Order $N=2$ ($H_2$):

```math
H_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

#### 2. Order $N=4$ ($H_4$):

```math
H_4 = \begin{bmatrix}
H_2 & H_2 \\
H_2 & -H_2
\end{bmatrix} = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix}
```

#### 3. Order $N=8$ ($H_8$):

```math
H_8 = \begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 & 1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 & 1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 \\
1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 \\
1 & -1 & 1 & -1 & -1 & 1 & -1 & 1 \\
1 & 1 & -1 & -1 & -1 & -1 & 1 & 1 \\
1 & -1 & -1 & 1 & -1 & 1 & 1 & -1
\end{bmatrix}
```

#### Sequency Concept:
**Sequency** here means the number of sign changes between adjacent entries of a row vector; some continuous Walsh-function conventions instead describe zero crossings per unit interval. It serves as the binary equivalent of frequency.

| Matrix Row ($H_4$) | Values | Sign Changes | Sequency Value |
| :---: | :---: | :---: | :---: |
| Row 0 | $[+1, +1, +1, +1]$ | $0$ | $0$ (DC component) |
| Row 1 | $[+1, -1, +1, -1]$ | $3$ | $3$ (High sequency) |
| Row 2 | $[+1, +1, -1, -1]$ | $1$ | $1$ (Low sequency) |
| Row 3 | $[+1, -1, -1, +1]$ | $2$ | $2$ (Mid sequency) |

> 🧠 **Walsh Transform Connection:** Rearranging the rows of a Hadamard matrix in monotonically increasing order of sequency ($0, 1, 2, 3$) converts the Hadamard matrix into a **Walsh Matrix**.

---

<a id="24-normalized-vs-unnormalized-conventions"></a>

### 2.4 Normalized vs Unnormalized Conventions

In academic literature and university exam papers, two conventions are used:

* **Unnormalized Convention (Standard Class/Slide Notation):**
  Uses pure integer matrix $H_N$ with $+1/-1$ entries. Scaling factor $\frac{1}{N}$ (1D) or $\frac{1}{N^2}$ (2D) is placed entirely on the inverse transform.

```math
  \text{Forward: } F = H_N \cdot f \cdot H_N^T \qquad \text{Inverse: } f = \frac{1}{N^2} H_N^T \cdot F \cdot H_N
```

* **Normalized Orthonormal Convention ($A_W$):**
  Includes a factor of $\frac{1}{\sqrt{N}}$ on the matrix so that $A_W \cdot A_W^T = I_N$.

```math
  A_W = \frac{1}{\sqrt{N}} H_N \implies \text{Forward: } F = A_W \cdot f \cdot A_W^T \qquad \text{Inverse: } f = A_W^T \cdot F \cdot A_W
```

---

<a id="25-forward-and-inverse-2d-hadamard-transform-formulation"></a>

### 2.5 Forward and Inverse 2D Hadamard Transform Formulation

Using the unnormalized convention for an $N \times N$ image matrix $f$:

* **Forward 2D Hadamard Transform:**

```math
  F = H_N \cdot f \cdot H_N^T
```

* **Inverse 2D Hadamard Transform:**

```math
  f = \frac{1}{N^2} H_N^T \cdot F \cdot H_N
```

---

<a id="26-worked-numerical-examples-1d-sequence-and-4x4-image"></a>

### 2.6 Worked Numerical Examples (1D Sequence and 4x4 Image)

#### 📍 Worked Problem 2.1: 1D Hadamard Transform

**Given Sequence $\mathbf{x}$:**

```math
\mathbf{x} = \begin{bmatrix}
1 \\
2 \\
0 \\
3
\end{bmatrix}
```

**Step 1: Compute Forward Transform $\mathbf{X} = H_4 \cdot \mathbf{x}$**

```math
\mathbf{X} = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} \begin{bmatrix}
1 \\
2 \\
0 \\
3
\end{bmatrix} = \begin{bmatrix}
1+2+0+3 \\
1-2+0-3 \\
1+2-0-3 \\
1-2-0+3
\end{bmatrix} = \begin{bmatrix}
6 \\
-4 \\
0 \\
2
\end{bmatrix}
```

**Step 2: Verify Inverse Transform $\mathbf{x} = \frac{1}{4} H_4 \cdot \mathbf{X}$**

```math
\mathbf{x} = \frac{1}{4} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} \begin{bmatrix}
6 \\
-4 \\
0 \\
2
\end{bmatrix} = \frac{1}{4} \begin{bmatrix}
6 - 4 + 0 + 2 \\
6 + 4 + 0 - 2 \\
6 - 4 - 0 - 2 \\
6 + 4 - 0 + 2
\end{bmatrix} = \frac{1}{4} \begin{bmatrix}
4 \\
8 \\
0 \\
12
\end{bmatrix} = \begin{bmatrix}
1 \\
2 \\
0 \\
3
\end{bmatrix} \quad \text{(Exact!)}
```

---

#### 📍 Worked Problem 2.2: 4x4 2D Hadamard Transform

**Given Image $f$:**

```math
f = \begin{bmatrix}
10 & 10 & 10 & 10 \\
20 & 20 & 20 & 20 \\
20 & 20 & 20 & 20 \\
20 & 20 & 20 & 20
\end{bmatrix}
```

**Step 1: Compute Intermediate Matrix $A = H_4 \cdot f$**

```math
A = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} \begin{bmatrix}
10 & 10 & 10 & 10 \\
20 & 20 & 20 & 20 \\
20 & 20 & 20 & 20 \\
20 & 20 & 20 & 20
\end{bmatrix} = \begin{bmatrix}
70 & 70 & 70 & 70 \\
-10 & -10 & -10 & -10 \\
-10 & -10 & -10 & -10 \\
-10 & -10 & -10 & -10
\end{bmatrix}
```

**Step 2: Compute Final Transform $F = A \cdot H_4$**

```math
F = \begin{bmatrix}
70 & 70 & 70 & 70 \\
-10 & -10 & -10 & -10 \\
-10 & -10 & -10 & -10 \\
-10 & -10 & -10 & -10
\end{bmatrix} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} = \begin{bmatrix}
280 & 0 & 0 & 0 \\
-40 & 0 & 0 & 0 \\
-40 & 0 & 0 & 0 \\
-40 & 0 & 0 & 0
\end{bmatrix}
```

> 🎯 **Observation:**
> * $F(0,0) = 280 = \sum \text{all pixels}$.
> * All columns for $v > 0$ evaluate to zero because each image row is constant across its columns.

---

<a id="3-discrete-cosine-transform-dct-and-image-compression"></a>

## 3. Discrete Cosine Transform (DCT) and Image Compression

<a id="31-mathematical-definition-of-1d-and-2d-dct-and-idct"></a>

### 3.1 Mathematical Definition of 1D and 2D DCT and IDCT

The **Discrete Cosine Transform (DCT)** expresses spatial image pixels as a weighted sum of real-valued cosine basis functions.

#### 1D DCT and IDCT Pair (for sequence $x(n)$ of length $N$):

```math
F(u) = \alpha(u) \sum_{n=0}^{N-1} f(n) \cos\left[ \frac{(2n + 1) u \pi}{2N} \right] \quad \text{for } u = 0, 1, \dots, N-1
```

```math
f(n) = \sum_{u=0}^{N-1} \alpha(u) F(u) \cos\left[ \frac{(2n + 1) u \pi}{2N} \right] \quad \text{for } n = 0, 1, \dots, N-1
```

where the orthogonal scale factor $\alpha(u)$ is defined as:

```math
\alpha(u) = \begin{cases}
\sqrt{\frac{1}{N}} & \text{if } u = 0 \\
\sqrt{\frac{2}{N}} & \text{if } u > 0
\end{cases}
```

#### 2D DCT and IDCT Pair (for $M \times N$ image $f(x,y)$):

For rectangular images, use separate orthonormal scale factors $\alpha_M(u)$ and $\alpha_N(v)$, defined by $\alpha_L(0)=\sqrt{1/L}$ and $\alpha_L(k)=\sqrt{2/L}$ for $k>0$. For square blocks, both reduce to the same $\alpha$.

```math
F(u,v) = \alpha_M(u) \alpha_N(v) \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) \cos\left[ \frac{(2x + 1) u \pi}{2M} \right] \cos\left[ \frac{(2y + 1) v \pi}{2N} \right]
```

```math
f(x,y) = \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} \alpha_M(u) \alpha_N(v) F(u,v) \cos\left[ \frac{(2x + 1) u \pi}{2M} \right] \cos\left[ \frac{(2y + 1) v \pi}{2N} \right]
```

---

<a id="32-cosine-basis-functions-and-real-valued-computation"></a>

### 3.2 Cosine Basis Functions and Real-Valued Computation

Unlike the DFT (which uses complex exponentials $e^{-j\theta} = \cos\theta - j\sin\theta$), the DCT uses **strictly real-valued cosine functions**.

```text
DFT Basis Functions: Complex Exponentials (Real + Imaginary Components)
DCT Basis Functions: Real Cosines Only (Zero Imaginary Parts)
```

#### Advantages of Real Cosine Basis:
1. **Zero Imaginary Arithmetic:** Avoids complex multiplications and floating-point storage overhead.
2. **Symmetric Boundary Extension:** Implicitly extends $f(x,y)$ symmetrically (even symmetry) across image boundaries, often reducing boundary discontinuities.

---

<a id="33-energy-compaction-property-and-dc-vs-ac-coefficients"></a>

### 3.3 Energy Compaction Property and DC vs AC Coefficients

**Energy Compaction** is the ability of a transform to concentrate the vast majority of total image energy into a very small subset of transform coefficients.

```text
+-------------------------------------------------------------+
| [DC]  AC1  AC2  AC3 ...  (Top-Left: Low Frequencies)        |
|  AC4  AC5  AC6  ...     ---> Often concentrates energy in low-frequency coefficients   |
|  AC7  AC8  ...  ...                                         |
|  ...  ...  ...   0      ---> High Frequencies (Near Zero)   |
+-------------------------------------------------------------+
```

* **DC Coefficient $F(0,0)$:** Located at the top-left corner $(0,0)$. Contains average background intensity and has an image-dependent share of total image energy; no fixed percentage applies.
* **AC Coefficients $F(u,v)$ for $(u,v) \neq (0,0)$:** Represent specific spatial frequency details. Mid-to-high frequency AC coefficients in smooth natural images evaluate to near-zero values.

---

<a id="34-why-dct-is-preferred-over-dft-for-image-compression"></a>

### 3.4 Why DCT is Preferred over DFT for Image Compression

| Feature / Property | Discrete Fourier Transform (DFT) | Discrete Cosine Transform (DCT) |
| :--- | :--- | :--- |
| **Basis Functions** | Complex exponentials ($e^{-j\theta}$) | Real-valued cosine functions ($\cos\theta$) |
| **Boundary Extension** | **Periodic Extension:** Can create discontinuities at periodically extended boundaries | **Symmetric (Mirror) Extension:** Often reduces boundary mismatch compared with periodic extension |
| **High-Frequency Artifacts** | High artificial high-frequency coefficients due to boundary jumps | Often reduces boundary-related high-frequency leakage |
| **Energy Compaction** | Moderate energy compaction | **Exceptional energy compaction** (close to optimal KLT) |
| **Blocking Artifacts** | Blocking depends on block processing and quantization, not the transform alone | Blocking artifacts can appear after strong blockwise quantization |
| **Computational Overhead** | Requires complex arithmetic (double memory) | Real arithmetic only (fast $O(N \log N)$ implementations) |

---

<a id="35-jpeg-image-compression-workflow-8x8-block-processing"></a>

### 3.5 JPEG Image Compression Workflow (8x8 Block Processing)

The international **JPEG (Joint Photographic Experts Group)** standard relies on 2D DCT for lossy image compression:

```text
[ Input Image ] ──► [ 1. 8x8 Block Division ] ──► [ 2. Level Shift (-128) ]
                                                              │
                                                              ▼
[ Compressed Bitstream ] ◄── [ 5. Entropy Coding ] ◄── [ 4. Zig-Zag Scan ] ◄── [ 3. 2D DCT + Quantization ]
```

#### Step-by-Step Compression Pipeline:

1. **$8 \times 8$ Block Decomposition:**
   The image is partitioned into non-overlapping $8 \times 8$ pixel sub-blocks $f(x,y)$.
2. **Level Shifting:**
   For an 8-bit image ($[0, 255]$), $128$ is subtracted from each pixel so intensities are centered around zero ($[-128, +127]$).
3. **2D DCT Computation:**
   Forward 2D DCT converts the $8 \times 8$ pixel block into an $8 \times 8$ coefficient block $F(u,v)$.
4. **Quantization (LOSSY STEP):**
   Each DCT coefficient is divided by a corresponding entry in a perceptual **Quantization Matrix** $Q(u,v)$ and rounded to the nearest integer:

```math
   F_Q(u,v) = \text{round}\left( \frac{F(u,v)}{Q(u,v)} \right)
```

   > ⚠️ **Crucial Concept:** Quantization is the **principal intentional lossy coefficient step** in this simplified JPEG pipeline; practical decoding and color conversion can introduce additional rounding. It forces high-frequency AC coefficients (where human vision is less sensitive) to exact zeros.

5. **Zig-Zag Scanning & Entropy Encoding:**
   The $8 \times 8$ quantized matrix is converted into a 1D sequence using a **Zig-Zag Scan** to group long runs of zeros together, followed by Run-Length Encoding (RLE) and Huffman Coding.

6. **Reconstruction (Decoder):**
   De-quantization restores approximate coefficients $F_{deQ}(u,v) = F_Q(u,v) \times Q(u,v)$, followed by Inverse 2D DCT (IDCT) and adding $128$ back.

---

<a id="36-worked-numerical-example-4x4-dct-matrix-multiplication"></a>

### 3.6 Worked Numerical Example (4x4 DCT Matrix Multiplication)

#### 📍 Worked Problem 3.1: 4x4 2D DCT Calculation

**Given $4 \times 4$ DCT Transformation Matrix $C$:**

```math
C = \begin{bmatrix}
0.5 & 0.5 & 0.5 & 0.5 \\
0.6532 & 0.2706 & -0.2706 & -0.6532 \\
0.5 & -0.5 & -0.5 & 0.5 \\
0.2706 & -0.6532 & 0.6532 & -0.2706
\end{bmatrix}
```

**Given Image Block $f$:**

```math
f = \begin{bmatrix}
1 & 2 & 2 & 1 \\
2 & 1 & 2 & 1 \\
1 & 2 & 2 & 1 \\
2 & 1 & 2 & 1
\end{bmatrix}
```

**Task:** Compute 2D DCT matrix $F = C \cdot f \cdot C^T$. The displayed $C$ entries are rounded to four decimals, so the computed coefficients are approximate.

**Step 1: Compute Intermediate Matrix $A = C \cdot f$**

```math
A = \begin{bmatrix}
0.5 & 0.5 & 0.5 & 0.5 \\
0.6532 & 0.2706 & -0.2706 & -0.6532 \\
0.5 & -0.5 & -0.5 & 0.5 \\
0.2706 & -0.6532 & 0.6532 & -0.2706
\end{bmatrix} \begin{bmatrix}
1 & 2 & 2 & 1 \\
2 & 1 & 2 & 1 \\
1 & 2 & 2 & 1 \\
2 & 1 & 2 & 1
\end{bmatrix} = \begin{bmatrix}
3.0000 & 3.0000 & 4.0000 & 2.0000 \\
-0.3826 & 0.3826 & 0 & 0 \\
0 & 0 & 0 & 0 \\
-0.9238 & 0.9238 & 0 & 0
\end{bmatrix}
```

**Step 2: Compute Final DCT Matrix $F = A \cdot C^T$**

```math
F = \begin{bmatrix}
3.0000 & 3.0000 & 4.0000 & 2.0000 \\
-0.3826 & 0.3826 & 0 & 0 \\
0 & 0 & 0 & 0 \\
-0.9238 & 0.9238 & 0 & 0
\end{bmatrix} \begin{bmatrix}
0.5 & 0.6532 & 0.5 & 0.2706 \\
0.5 & 0.2706 & -0.5 & -0.6532 \\
0.5 & -0.2706 & -0.5 & 0.6532 \\
0.5 & -0.6532 & 0.5 & -0.2706
\end{bmatrix}
```

```math
F = \begin{bmatrix}
6.0000 & 0.3826 & -1.0000 & 0.9238 \\
0 & -0.1464 & -0.3826 & -0.3534 \\
0 & 0 & 0 & 0 \\
0 & -0.3534 & -0.9238 & -0.8534
\end{bmatrix}
```

> 🧠 **Analysis:**
> * $F(0,0) = 6.0$ holds the DC background energy.
> * For this particular block, the larger-magnitude coefficients include the DC and several low-frequency terms; energy compaction varies with image content. Coefficients computed with rounded $C$ entries are approximate.

---

<a id="4-comparative-analysis-of-image-transforms"></a>

## 4. Comparative Analysis of Image Transforms

| Feature | Discrete Fourier Transform (DFT) | Hadamard Transform | Discrete Cosine Transform (DCT) |
| :--- | :--- | :--- | :--- |
| **Basis Functions** | Complex Exponentials ($e^{-j\theta}$) | Binary Square Waves ($\pm 1$) | Real Cosine Waves ($\cos\theta$) |
| **Domain Type** | Complex Frequency Domain | Binary Sequency Domain | Real Frequency Domain |
| **Computational Complexity** | $O(N \log_2 N)$ Complex Mults | **$O(N \log_2 N)$ Additions ONLY** | $O(N \log_2 N)$ Real Mults |
| **Energy Compaction** | Low to Moderate | Moderate | **Very High** (Near-Optimal KLT) |
| **Boundary Discontinuities** | High (Periodic extension) | High (Rectangular jumps) | Reduced boundary mismatch for many smooth blocks; not zero in every case |
| **Primary Use Cases** | Frequency-domain filtering, phase analysis | Fast real-time hardware processing, CDMA | **JPEG / MPEG image/video compression** |

---

<a id="5-formula-and-transform-matrix-master-reference"></a>

## 5. Formula and Transform Matrix Master Reference

### 1. 2D DFT Matrix Multiplication Formula

```math
F = W_M \cdot f \cdot W_N^T \qquad f = \frac{1}{MN} W_M^H \cdot F \cdot (W_N^T)^H
```

### 2. 4x4 Twiddle Factor Matrix W_4

```math
W_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

### 3. 4x4 Hadamard Matrix H_4

```math
H_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix}
```

### 4. 4x4 DCT Coefficient Matrix C_4

```math
C_4 = \begin{bmatrix}
0.5 & 0.5 & 0.5 & 0.5 \\
0.6532 & 0.2706 & -0.2706 & -0.6532 \\
0.5 & -0.5 & -0.5 & 0.5 \\
0.2706 & -0.6532 & 0.6532 & -0.2706
\end{bmatrix}
```

---

<a id="6-common-exam-mistakes-and-pitfalls"></a>

## 6. Common Exam Mistakes and Pitfalls

1. ❌ **Mixing Complex Conjugates in IDFT Matrix Formulation:**
   Forgetting that IDFT uses conjugated twiddle matrices. In general $W^*$ is elementwise conjugation and $W^H=(W^*)^T$; the symmetric DFT twiddle matrix is a special case.
2. ❌ **Forgetting the $\frac{1}{N^2}$ Scaling in Inverse Hadamard:**
   Unnormalized inverse Hadamard requires dividing by $N^2$ (or $N$ for 1D).
3. ❌ **Claiming DCT is Lossy:**
   The ideal mathematical DCT is invertible; finite-precision implementations may introduce rounding. In this simplified JPEG pipeline, coefficient quantization is the principal intentional lossy step; reconstruction and color conversion can introduce further rounding.
4. ❌ **Confusing Frequency with Sequency:**
   Frequency measures sinusoidal cycles per unit distance; sequency measures sign changes per unit distance.
5. ❌ **Forgetting Level Shift in JPEG:**
   Failing to subtract $128$ from 8-bit image pixels before computing DCT.

---

<a id="7-quick-revision-and-last-minute-checklist"></a>

## 7. Quick Revision and Last-Minute Checklist

* [x] **2D DFT:** Converts spatial pixels into complex frequency spectrum $F(u,v)$. $F(0,0) = \sum f(x,y) = MN \bar{f}$.
* [x] **Twiddle Matrix $W_4$:** Uses entries $\{1, -j, -1, j\}$.
* [x] **Hadamard Matrix $H_N$:** Built recursively via Kronecker product 

```math
H_{2N} = \begin{bmatrix}
H_N & H_N \\
H_N & -H_N
\end{bmatrix}
```

. Uses additions/subtractions only.
* [x] **Sequency:** Count of sign changes along a row vector.
* [x] **2D DCT:** Uses real cosine basis functions. Concentrates image energy into top-left low-frequency coefficients.
* [x] **JPEG Compression:** Uses $8 \times 8$ blocks, $-128$ level shift, 2D DCT, Quantization (lossy), Zig-zag scan, RLE/Huffman coding.

---
