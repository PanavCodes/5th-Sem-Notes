# 📚 IVP Unit 3: Image Transforms — Solved Numerical Workbook

---

## 📌 Document Metadata & Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 3 — Image Transforms
* **Target Assessment:** Mid-Term Exams, Class Tests, Term End Examinations (TEE)
* **Format:** GitHub Flavored Markdown (GFM) with Standalone Math Fences
* **Strict Scope Boundary:** This workbook contains numerical problems strictly covering the three prescribed Unit 3 syllabus topics:
  1. **Discrete Fourier Transform (DFT)** and 2D Inverse DFT (IDFT)
  2. **Hadamard Transform** and 2D Inverse Hadamard Transform (IHadamard)
  3. **Discrete Cosine Transform (DCT)**, 2D Inverse DCT (IDCT), and DCT-Based Image Compression / Energy Retention

---

## 📋 Syllabus Mapping & Source Attribution Directory

> **Source-status note:** The reported exam names, years, and question numbers are preserved, but original question papers were not supplied for independent verification. Another PYQ bank labels Numerical 1.2 as practice, reports a different year for Numerical 2.2, and uses a different coefficient matrix for Numerical 3.3. Compare against original papers before calling these verified PYQs.


| Problem ID | Topic / Transformation | Problem Type | Source Attribution / Exam Reference | Verification Status |
|---|---|---|---|---|
| **Numerical 1.1** | 1D 4-Point DFT & Parseval Check | 1D Spectrum & Energy | SVKM's NMIMS Re-Exam 2023-24 (Q5b) / Final Exam 2022-23 | **Reported PYQ (unverified)** |
| **Numerical 1.2** | $2 \times 2$ 2D DFT & IDFT Reconstruction | 2D Matrix Product & IDFT | SVKM's NMIMS Final Exam 2025-26 (Q3a) / Re-Exam 2023-24 | **Reported PYQ (unverified)** |
| **Numerical 1.3** | $2 \times 2$ 2D DFT Variant Transformation | 2D Matrix Product | Reported PYQ List (Classroom / Lab Reference) | **Reported PYQ (unverified)** |
| **Numerical 1.4** | $4 \times 4$ 2D DFT Matrix Product & Centering | 2D Centering & Spectrum | University Exam / AKTU Final Paper | **Reported PYQ (unverified)** |
| **Numerical 2.1** | 1D 4-Point Hadamard & Sequency Order | 1D Matrix & Sequency | Classroom Lecture Notes / Test Reference | **Reported PYQ (unverified)** |
| **Numerical 2.2** | $2 \times 2$ 2D Hadamard & IHadamard Reconstruction | 2D Matrix Product & IHadamard | SVKM's NMIMS Final Exam 2022-23 (Nov/Dec 2022 - Q3a) | **Reported PYQ (unverified)** |
| **Numerical 2.3** | $2 \times 2$ 2D Hadamard Matrix Product Variant | 2D Matrix Product | Reported PYQ List (Student Tutorial Reference) | **Reported PYQ (unverified)** |
| **Numerical 2.4** | $4 \times 4$ 2D Hadamard Truncation & MSE Loss | 2D Truncation & Reconstruction | SVKM's NMIMS Special Re-Exam 2022-23 (Q4b) | **Reported PYQ (unverified)** |
| **Numerical 3.1** | $2 \times 2$ 2D DCT Orthonormal Matrix Product | 2D DCT & Parseval Check | Concept Practice Problem | **Practice Problem** |
| **Numerical 3.2** | $4 \times 4$ 2D DCT Energy Compaction Analysis | 2D Orthonormal DCT | University Exam / AKTU Final Paper | **Reported PYQ (unverified)** |
| **Numerical 3.3** | DCT Energy Retention Thresholding (86%, 87.5%, 94%) | Energy Compaction & Masking | SVKM's NMIMS Final Exam 2024-25 (Q4a) / 2022-23 (Q4a) | **Reported PYQ (unverified)** |
| **Numerical 3.4** | JPEG $8 \times 8$ Transform/Quantization Walkthrough | JPEG Block Processing | Standard Image Compression Practice Problem | **Practice Problem** |

---

## 📑 Table of Contents

1. [Section 1: Discrete Fourier Transform (DFT) & IDFT Numericals](#section-1-discrete-fourier-transform-dft-idft-numericals)
   * 1.1 [Numerical 1.1: 1D 4-Point DFT Calculation & Parseval Energy Check](#numerical-11-1d-4-point-dft-calculation-parseval-energy-check)
   * 1.2 [Numerical 1.2: Complete $2 \times 2$ 2D DFT & IDFT Reconstruction](#numerical-12-complete-2-times-2-2d-dft-idft-reconstruction)
   * 1.3 [Numerical 1.3: $2 \times 2$ 2D DFT Matrix Transformation Variant](#numerical-13-2-times-2-2d-dft-matrix-transformation-variant)
   * 1.4 [Numerical 1.4: Step-by-Step $4 \times 4$ 2D DFT Matrix Multiplication & Centering](#numerical-14-step-by-step-4-times-4-2d-dft-matrix-multiplication-centering)
2. [Section 2: Hadamard Transform & IHadamard Numericals](#section-2-hadamard-transform-ihadamard-numericals)
   * 2.1 [Numerical 2.1: 1D 4-Point Hadamard Transform & Sequency Analysis](#numerical-21-1d-4-point-hadamard-transform-sequency-analysis)
   * 2.2 [Numerical 2.2: Complete $2 \times 2$ 2D Hadamard Transform & Inverse Reconstruction](#numerical-22-complete-2-times-2-2d-hadamard-transform-inverse-reconstruction)
   * 2.3 [Numerical 2.3: $2 \times 2$ 2D Hadamard Matrix Product Variant](#numerical-23-2-times-2-2d-hadamard-matrix-product-variant)
   * 2.4 [Numerical 2.4: $4 \times 4$ 2D Hadamard Transform, Coefficient Truncation & MSE Loss](#numerical-24-4-times-4-2d-hadamard-transform-coefficient-truncation-mse-loss)
3. [Section 3: Discrete Cosine Transform (DCT) & Image Compression Numericals](#section-3-discrete-cosine-transform-dct-image-compression-numericals)
   * 3.1 [Numerical 3.1: $2 \times 2$ 2D DCT Matrix Multiplication & Parseval Energy Check](#numerical-31-2-times-2-2d-dct-matrix-multiplication-parseval-energy-check)
   * 3.2 [Numerical 3.2: $4 \times 4$ 2D DCT Matrix Multiplication & Energy Compaction](#numerical-32-4-times-4-2d-dct-matrix-multiplication-energy-compaction)
   * 3.3 [Numerical 3.3: DCT Energy Retention Thresholding (86%, 87.5%, 94% Thresholds)](#numerical-33-dct-energy-retention-thresholding-86-875-94-thresholds)
   * 3.4 [Numerical 3.4: JPEG $8 \times 8$ Transform/Quantization Walkthrough](#numerical-34-complete-8-times-8-jpeg-compression-pipeline-walkthrough)
4. [Section 4: Formula & Transform Matrix Master Reference](#section-4-formula-transform-matrix-master-reference)
5. [Section 5: Summary Answer Index](#section-5-summary-answer-index)
6. [Section 6: Common Numerical Mistakes & Pitfalls](#section-6-common-numerical-mistakes-pitfalls)
7. [Section 7: Source Status Checklist](#section-7-source-status-checklist)

---

<a id="section-1-discrete-fourier-transform-dft-idft-numericals"></a>

## Section 1: Discrete Fourier Transform (DFT) & IDFT Numericals

<a id="numerical-11-1d-4-point-dft-calculation-parseval-energy-check"></a>

### Numerical 1.1: 1D 4-Point DFT Calculation & Parseval Energy Check

#### ❓ Problem Statement
**[Reported PYQ (unverified) — SVKM's NMIMS Re-Exam 2023-24 (Q5b) / Final Exam 2022-23]**  
Given a 1D spatial sequence $x(n) = \{0, 1, 2, 1\}$ for $n = 0, 1, 2, 3$:
1. Calculate the 4-point Discrete Fourier Transform $X(k)$ using the twiddle factor matrix.
2. Determine the magnitude $|X(k)|$ and phase angle $\angle X(k)$ for each frequency component.
3. Reconstruct the spatial sequence $x(n)$ using the Inverse 1D DFT (IDFT).
4. Verify Parseval's energy conservation theorem between spatial and frequency domains.

---

#### 💡 Step-by-Step Solution

##### 1. Forward 1D DFT Matrix Calculation
The 1D $N$-point DFT formula is:

```math
X(k) = \sum_{n=0}^{N-1} x(n) e^{-j \frac{2\pi k n}{N}} = \sum_{n=0}^{N-1} x(n) W_N^{kn}
```

For $N = 4$, the twiddle factor $W_4 = e^{-j \frac{2\pi}{4}} = e^{-j \frac{\pi}{2}} = -j$.  
The $4 \times 4$ twiddle factor matrix $W_4$ is:

```math
W_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

Multiplying $W_4$ by the column vector $x = [0, 1, 2, 1]^T$:

```math
X = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix} \begin{bmatrix}
0 \\
1 \\
2 \\
1
\end{bmatrix}
```

Computing row-by-row matrix products:
* **$X(0)$ (DC Component):** $1(0) + 1(1) + 1(2) + 1(1) = 0 + 1 + 2 + 1 = \mathbf{4}$
* **$X(1)$:** $1(0) + (-j)(1) + (-1)(2) + (j)(1) = 0 - j - 2 + j = \mathbf{-2 + 0j}$
* **$X(2)$:** $1(0) + (-1)(1) + 1(2) + (-1)(1) = 0 - 1 + 2 - 1 = \mathbf{0}$
* **$X(3)$:** $1(0) + (j)(1) + (-1)(2) + (-j)(1) = 0 + j - 2 - j = \mathbf{-2 + 0j}$

Resulting DFT sequence vector $X(k)$:

```math
X(k) = \{4, -2, 0, -2\}
```

##### 2. Magnitude $|X(k)|$ and Phase Angle $\angle X(k)$
For a complex number $Z = R + jI$, magnitude is $|Z| = \sqrt{R^2 + I^2}$ and phase is $\angle Z = \tan^{-1}(I / R)$:
* **$X(0) = 4 + 0j$:** $|X(0)| = 4$, $\angle X(0) = 0^\circ$
* **$X(1) = -2 + 0j$:** $|X(1)| = \sqrt{(-2)^2 + 0^2} = 2$, $\angle X(1) = \tan^{-1}(0 / -2) = 180^\circ$ ($\pi$ rad)
* **$X(2) = 0 + 0j$:** $|X(2)| = 0$, $\angle X(2) = 0^\circ$
* **$X(3) = -2 + 0j$:** $|X(3)| = \sqrt{(-2)^2 + 0^2} = 2$, $\angle X(3) = 180^\circ$ ($\pi$ rad)

##### 3. Inverse 1D DFT (IDFT) Reconstruction
The 1D IDFT matrix relation is $x = \frac{1}{N} W_4^* X$, where $W_4^*$ is the complex conjugate of $W_4$:

```math
x = \frac{1}{4} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & j & -1 & -j \\
1 & -1 & 1 & -1 \\
1 & -j & -1 & j
\end{bmatrix} \begin{bmatrix}
4 \\
-2 \\
0 \\
-2
\end{bmatrix}
```

Computing row-by-row:
* **$x(0)$:** $\frac{1}{4} [1(4) + 1(-2) + 1(0) + 1(-2)] = \frac{1}{4} [4 - 2 + 0 - 2] = \frac{0}{4} = \mathbf{0}$
* **$x(1)$:** $\frac{1}{4} [1(4) + j(-2) + (-1)(0) + (-j)(-2)] = \frac{1}{4} [4 - 2j + 0 + 2j] = \frac{4}{4} = \mathbf{1}$
* **$x(2)$:** $\frac{1}{4} [1(4) + (-1)(-2) + 1(0) + (-1)(-2)] = \frac{1}{4} [4 + 2 + 0 + 2] = \frac{8}{4} = \mathbf{2}$
* **$x(3)$:** $\frac{1}{4} [1(4) + (-j)(-2) + (-1)(0) + j(-2)] = \frac{1}{4} [4 + 2j + 0 - 2j] = \frac{4}{4} = \mathbf{1}$

The reconstructed sequence is $\mathbf{x(n) = \{0, 1, 2, 1\}}$, matching the original input.

##### 4. Parseval's Energy Conservation Check
Parseval's theorem states:

```math
E_{\text{spatial}} = \sum_{n=0}^{N-1} |x(n)|^2 = \frac{1}{N} \sum_{k=0}^{N-1} |X(k)|^2 = E_{\text{spectral}}
```

* **Spatial Energy $E_{\text{spatial}}$:**
  

```math
E_{\text{spatial}} = |0|^2 + |1|^2 + |2|^2 + |1|^2 = 0 + 1 + 4 + 1 = \mathbf{6}
```


* **Spectral Energy $E_{\text{spectral}}$:**
  

```math
E_{\text{spectral}} = \frac{1}{4} \left[ |4|^2 + |-2|^2 + |0|^2 + |-2|^2 \right] = \frac{1}{4} \left[ 16 + 4 + 0 + 4 \right] = \frac{24}{4} = \mathbf{6}
```



Since $E_{\text{spatial}} = E_{\text{spectral}} = 6$, **Parseval's energy conservation theorem holds perfectly**.

---

<a id="numerical-12-complete-2-times-2-2d-dft-idft-reconstruction"></a>

### Numerical 1.2: Complete $2 \times 2$ 2D DFT & IDFT Reconstruction

#### ❓ Problem Statement
**[Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2025-26 (Q3a) / Re-Exam 2023-24]**  
Given a $2 \times 2$ spatial domain image $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
```

1. Compute the 2D Discrete Fourier Transform $F(u,v)$ using matrix multiplication.
2. Verify that $F(0,0)$ equals the total sum of spatial pixel intensities (DC component).
3. Perform exact spatial reconstruction using the Inverse 2D DFT (IDFT).
4. Verify Parseval's 2D energy conservation theorem.

---

#### 💡 Step-by-Step Solution

##### 1. Forward 2D DFT Matrix Product
The separable 2D DFT for an $N \times N$ matrix is given by $F = W_N f W_N^T$, where for $N = 2$:

```math
W_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

**Step 1.1: Compute Intermediate Matrix $A = W_2 \cdot f$**

```math
A = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} = \begin{bmatrix}
(1\cdot 1 + 1\cdot 3) & (1\cdot 2 + 1\cdot 4) \\
(1\cdot 1 - 1\cdot 3) & (1\cdot 2 - 1\cdot 4)
\end{bmatrix} = \begin{bmatrix}
4 & 6 \\
-2 & -2
\end{bmatrix}
```

**Step 1.2: Compute Spectral Matrix $F = A \cdot W_2^T$**  
Since $W_2^T = W_2$:

```math
F = \begin{bmatrix}
4 & 6 \\
-2 & -2
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
(4\cdot 1 + 6\cdot 1) & (4\cdot 1 - 6\cdot 1) \\
(-2\cdot 1 - 2\cdot 1) & (-2\cdot 1 + 2\cdot 1)
\end{bmatrix} = \begin{bmatrix}
10 & -2 \\
-4 & 0
\end{bmatrix}
```

##### 2. DC Component Verification
The total sum of all spatial pixels is:



```math
\sum_{x=0}^{1} \sum_{y=0}^{1} f(x,y) = 1 + 2 + 3 + 4 = \mathbf{10}
```



From our computed $F(u,v)$ matrix, $F(0,0) = \mathbf{10}$. This verifies $F(0,0) = \sum \sum f(x,y)$.

##### 3. Inverse 2D DFT (IDFT) Reconstruction
The separable 2D IDFT formula is $f = \frac{1}{N^2} W_2^* F (W_2^*)^T$. For $N = 2$, $N^2 = 4$ and $W_2^* = W_2$:

**Step 3.1: Compute Intermediate Matrix $B = W_2 \cdot F$**

```math
B = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
10 & -2 \\
-4 & 0
\end{bmatrix} = \begin{bmatrix}
(10 - 4) & (-2 + 0) \\
(10 - (-4)) & (-2 - 0)
\end{bmatrix} = \begin{bmatrix}
6 & -2 \\
14 & -2
\end{bmatrix}
```

**Step 3.2: Compute $f' = B \cdot W_2$**

```math
f' = \begin{bmatrix}
6 & -2 \\
14 & -2
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
(6 - 2) & (6 + 2) \\
(14 - 2) & (14 + 2)
\end{bmatrix} = \begin{bmatrix}
4 & 8 \\
12 & 16
\end{bmatrix}
```

**Step 3.3: Multiply by Scaling Factor $\frac{1}{4}$**

```math
f = \frac{1}{4} \begin{bmatrix}
4 & 8 \\
12 & 16
\end{bmatrix} = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
```

The reconstructed matrix matches the original image $f(x,y)$ exactly.

##### 4. Parseval's 2D Energy Verification
Parseval's 2D theorem states $E_{\text{spatial}} = \sum \sum |f(x,y)|^2 = \frac{1}{N^2} \sum \sum |F(u,v)|^2 = E_{\text{spectral}}$:
* **Spatial Energy:** $E_{\text{spatial}} = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = \mathbf{30}$
* **Spectral Energy:** $E_{\text{spectral}} = \frac{1}{4} \left[ 10^2 + (-2)^2 + (-4)^2 + 0^2 \right] = \frac{1}{4} \left[ 100 + 4 + 16 + 0 \right] = \frac{120}{4} = \mathbf{30}$

Parseval's energy relation is fully confirmed.

---

<a id="numerical-13-2-times-2-2d-dft-matrix-transformation-variant"></a>

### Numerical 1.3: $2 \times 2$ 2D DFT Matrix Transformation Variant

#### ❓ Problem Statement
**[Reported PYQ (unverified) — Student Tutorial Reference]**  
Given a $2 \times 2$ image matrix $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix}
```

Compute the 2D Discrete Fourier Transform $F(u,v)$ and verify Parseval's energy theorem.

---

#### 💡 Step-by-Step Solution

##### 1. 2D DFT Matrix Product $F = W_2 f W_2$

```math
A = W_2 \cdot f = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix} = \begin{bmatrix}
3 & 5 \\
1 & 1
\end{bmatrix}
```

```math
F = A \cdot W_2 = \begin{bmatrix}
3 & 5 \\
1 & 1
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
8 & -2 \\
2 & 0
\end{bmatrix}
```

##### 2. Parseval's Energy Verification
* **Spatial Energy:** $E_{\text{spatial}} = 2^2 + 3^2 + 1^2 + 2^2 = 4 + 9 + 1 + 4 = \mathbf{18}$
* **Spectral Energy:** $E_{\text{spectral}} = \frac{1}{4} \left[ 8^2 + (-2)^2 + 2^2 + 0^2 \right] = \frac{1}{4} \left[ 64 + 4 + 4 + 0 \right] = \frac{72}{4} = \mathbf{18}$

Both energy measures equal $18$, confirming accuracy.

---

<a id="numerical-14-step-by-step-4-times-4-2d-dft-matrix-multiplication-centering"></a>

### Numerical 1.4: Step-by-Step $4 \times 4$ 2D DFT Matrix Multiplication & Centering

#### ❓ Problem Statement
**[Reported PYQ (unverified) — AKTU / University Exam Paper]**  
Given a $4 \times 4$ spatial domain image $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0
\end{bmatrix}
```

1. Pre-process the image for frequency spectrum centering by multiplying $f(x,y)$ by $(-1)^{x+y}$.
2. Compute the centered 2D DFT matrix $F(u,v)$ using the 4-point 1D DFT twiddle matrix $W_4$.
3. Identify the location of the centered DC component and explain the physical meaning of the resulting spectral matrix.

---

#### 💡 Step-by-Step Solution

##### 1. Pre-processing for Frequency Centering
Multiplying $f(x,y)$ by $(-1)^{x+y}$ shifts the frequency spectrum origin $(0,0)$ to the matrix center $(u_0, v_0) = (2,2)$.  
The sign pattern matrix $(-1)^{x+y}$ for $4 \times 4$ is:

```math
(-1)^{x+y} = \begin{bmatrix}
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1 \\
+1 & -1 & +1 & -1 \\
-1 & +1 & -1 & +1
\end{bmatrix}
```

Multiplying elementwise $f'(x,y) = f(x,y) \circ (-1)^{x+y}$:

```math
f'(x,y) = \begin{bmatrix}
1(1) & 0(-1) & 1(1) & 0(-1) \\
1(-1) & 0(1) & 1(-1) & 0(1) \\
1(1) & 0(-1) & 1(1) & 0(-1) \\
1(-1) & 0(1) & 1(-1) & 0(1)
\end{bmatrix} = \begin{bmatrix}
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0 \\
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0
\end{bmatrix}
```

##### 2. Centered 2D DFT Matrix Multiplication
Using $F = W_4 f' W_4^T$, where the 4-point DFT matrix $W_4$ is:

```math
W_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

**Step 2.1: Compute $A = W_4 \cdot f'$**

```math
A = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix} \begin{bmatrix}
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0 \\
1 & 0 & 1 & 0 \\
-1 & 0 & -1 & 0
\end{bmatrix}
```

* **Row 0 of A:** $[1(1) - 1(1) + 1(1) - 1(1), \quad 0, \quad 1(1) - 1(1) + 1(1) - 1(1), \quad 0] = [0, 0, 0, 0]$
* **Row 1 of A:** $[1(1) - (-j)(1) + (-1)(1) - (j)(1), \quad 0, \quad 1(1) - (-j)(1) + (-1)(1) - (j)(1), \quad 0] = [1 + j - 1 - j, 0, 1 + j - 1 - j, 0] = [0, 0, 0, 0]$
* **Row 2 of A:** $[1(1) - (-1)(1) + 1(1) - (-1)(1), \quad 0, \quad 1(1) - (-1)(1) + 1(1) - (-1)(1), \quad 0] = [1 + 1 + 1 + 1, 0, 1 + 1 + 1 + 1, 0] = [4, 0, 4, 0]$
* **Row 3 of A:** $[1(1) - (j)(1) + (-1)(1) - (-j)(1), \quad 0, \quad 1(1) - (j)(1) + (-1)(1) - (-j)(1), \quad 0] = [1 - j - 1 + j, 0, 1 - j - 1 + j, 0] = [0, 0, 0, 0]$

Thus:

```math
A = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
4 & 0 & 4 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

**Step 2.2: Compute $F = A \cdot W_4^T$**

```math
F = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
4 & 0 & 4 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

* **Row 2 of F:** $[4(1) + 0 + 4(1) + 0, \quad 4(1) + 0 + 4(-1) + 0, \quad 4(1) + 0 + 4(1) + 0, \quad 4(1) + 0 + 4(-1) + 0] = [8, 0, 8, 0]$

All other rows evaluate to zero. Therefore:

```math
F(u,v) = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
8 & 0 & 8 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

##### 3. Spectral Analysis & DC Component
* **DC Component:** The original image has 8 unit-valued pixels, so its uncentered DC is 8. In the centered transform, $F(2,2)=8$ is shifted DC, while $F(2,0)=8$ is a separate non-DC peak.
* **Physical Interpretation:** The input image consists of alternating vertical stripes of 1s and 0s (a vertical square wave). In frequency space, this creates strong impulses in row $u=2$ at column frequencies $v=0$ and $v=2$ in the centered spectrum.

---

<a id="section-2-hadamard-transform-ihadamard-numericals"></a>

## Section 2: Hadamard Transform & IHadamard Numericals

<a id="numerical-21-1d-4-point-hadamard-transform-sequency-analysis"></a>

### Numerical 2.1: 1D 4-Point Hadamard Transform & Sequency Analysis

#### ❓ Problem Statement
**[Reported PYQ (unverified) — Classroom Lecture Reference]**  
Given a 1D sequence $x = [1, 2, 0, 3]^T$:
1. Compute the unnormalized 4-point 1D Hadamard transform $y = H_4 x$.
2. Determine the sequency (number of zero-crossings) for each row of $H_4$.
3. Reconstruct $x$ using the unnormalized inverse Hadamard transform relation $x = \frac{1}{4} H_4 y$.

---

#### 💡 Step-by-Step Solution

##### 1. Forward 1D Hadamard Transform
The 4-point Sylvester-constructed Hadamard matrix $H_4$ is:

```math
H_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix}
```

Multiplying $H_4$ by $x = [1, 2, 0, 3]^T$:

```math
y = \begin{bmatrix}
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
1(1) + 1(2) + 1(0) + 1(3) \\
1(1) - 1(2) + 1(0) - 1(3) \\
1(1) + 1(2) - 1(0) - 1(3) \\
1(1) - 1(2) - 1(0) + 1(3)
\end{bmatrix} = \begin{bmatrix}
6 \\
-4 \\
0 \\
2
\end{bmatrix}
```

The transformed coefficient vector is $\mathbf{y = [6, -4, 0, 2]^T}$.

##### 2. Sequency (Zero-Crossing) Analysis
Sequency measures the number of sign changes across a row of the transform matrix:
* **Row 0 (`[ 1,  1,  1,  1]`):** 0 sign changes $\implies$ **Sequency = 0** (DC basis)
* **Row 1 (`[ 1, -1,  1, -1]`):** $+1 	o -1 	o +1 	o -1$ (3 changes) $\implies$ **Sequency = 3**
* **Row 2 (`[ 1,  1, -1, -1]`):** $+1 	o +1 	o -1 	o -1$ (1 change) $\implies$ **Sequency = 1**
* **Row 3 (`[ 1, -1, -1,  1]`):** $+1 	o -1 	o -1 	o +1$ (2 changes) $\implies$ **Sequency = 2**

##### 3. Unnormalized Inverse Hadamard Transform
The inverse relation is $x = \frac{1}{4} H_4 y$:

```math
x = \frac{1}{4} \begin{bmatrix}
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
\end{bmatrix}
```

The reconstructed vector matches $x = [1, 2, 0, 3]^T$ exactly.

---

<a id="numerical-22-complete-2-times-2-2d-hadamard-transform-inverse-reconstruction"></a>

### Numerical 2.2: Complete $2 \times 2$ 2D Hadamard Transform & Inverse Reconstruction

#### ❓ Problem Statement
**[Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2022-23 (Nov/Dec 2022 - Q3a)]**  
Given a $2 \times 2$ image matrix $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
2 & 6 \\
3 & 5
\end{bmatrix}
```

1. Compute the 2D Hadamard transform matrix $F(u,v)$ using $F = H_2 f H_2$.
2. Reconstruct the spatial image $f(x,y)$ using the inverse 2D Hadamard transform $f = \frac{1}{4} H_2 F H_2$.

---

#### 💡 Step-by-Step Solution

##### 1. Forward 2D Hadamard Transform
For $N = 2$, 

```math
H_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

.

**Step 1.1: Compute $A = H_2 \cdot f$**

```math
A = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
2 & 6 \\
3 & 5
\end{bmatrix} = \begin{bmatrix}
(2+3) & (6+5) \\
(2-3) & (6-5)
\end{bmatrix} = \begin{bmatrix}
5 & 11 \\
-1 & 1
\end{bmatrix}
```

**Step 1.2: Compute $F = A \cdot H_2$**

```math
F = \begin{bmatrix}
5 & 11 \\
-1 & 1
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
(5+11) & (5-11) \\
(-1+1) & (-1-1)
\end{bmatrix} = \begin{bmatrix}
16 & -6 \\
0 & -2
\end{bmatrix}
```

##### 2. Inverse 2D Hadamard Reconstruction
Applying $f = \frac{1}{4} H_2 F H_2$:

**Step 2.1: Compute $B = H_2 \cdot F$**

```math
B = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
16 & -6 \\
0 & -2
\end{bmatrix} = \begin{bmatrix}
(16+0) & (-6-2) \\
(16-0) & (-6+2)
\end{bmatrix} = \begin{bmatrix}
16 & -8 \\
16 & -4
\end{bmatrix}
```

**Step 2.2: Compute $f' = B \cdot H_2$**

```math
f' = \begin{bmatrix}
16 & -8 \\
16 & -4
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
(16-8) & (16+8) \\
(16-4) & (16+4)
\end{bmatrix} = \begin{bmatrix}
8 & 24 \\
12 & 20
\end{bmatrix}
```

**Step 2.3: Scale by $\frac{1}{4}$**

```math
f = \frac{1}{4} \begin{bmatrix}
8 & 24 \\
12 & 20
\end{bmatrix} = \begin{bmatrix}
2 & 6 \\
3 & 5
\end{bmatrix}
```

The reconstructed matrix matches 

```math
f(x,y) = \begin{bmatrix}
2 & 6 \\
3 & 5
\end{bmatrix}
```

 perfectly.

---

<a id="numerical-23-2-times-2-2d-hadamard-matrix-product-variant"></a>

### Numerical 2.3: $2 \times 2$ 2D Hadamard Matrix Product Variant

#### ❓ Problem Statement
**[Reported PYQ (unverified) — Student Tutorial Reference]**  
Given an image matrix 

```math
f(x,y) = \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix}
```

, calculate its 2D Hadamard transform and perform inverse reconstruction.

---

#### 💡 Step-by-Step Solution

##### 1. Forward Transform $F = H_2 f H_2$

```math
A = H_2 f = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix} = \begin{bmatrix}
3 & 5 \\
1 & 1
\end{bmatrix}
```

```math
F = A H_2 = \begin{bmatrix}
3 & 5 \\
1 & 1
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \begin{bmatrix}
8 & -2 \\
2 & 0
\end{bmatrix}
```

##### 2. Inverse Reconstruction $f = \frac{1}{4} H_2 F H_2$

```math
B = H_2 F = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
8 & -2 \\
2 & 0
\end{bmatrix} = \begin{bmatrix}
10 & -2 \\
6 & -2
\end{bmatrix}
```

```math
f = \frac{1}{4} B H_2 = \frac{1}{4} \begin{bmatrix}
10 & -2 \\
6 & -2
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} = \frac{1}{4} \begin{bmatrix}
8 & 12 \\
4 & 8
\end{bmatrix} = \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix}
```

---

<a id="numerical-24-4-times-4-2d-hadamard-transform-coefficient-truncation-mse-loss"></a>

### Numerical 2.4: $4 \times 4$ 2D Hadamard Transform, Coefficient Truncation & MSE Loss

#### ❓ Problem Statement
**[Reported PYQ (unverified) — SVKM's NMIMS Special Re-Exam 2022-23 (Q4b)]**  
Given a $4 \times 4$ binary step-edge image matrix $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
10 & 10 & 10 & 10 \\
10 & 10 & 10 & 10 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

1. Compute the unnormalized 2D Hadamard transform $F = H_4 f H_4$.
2. Truncate the spectral matrix by retaining only the single DC coefficient $F(0,0)$ (setting all AC coefficients to zero).
3. Reconstruct the spatial image $\hat{f}(x,y) = \frac{1}{16} H_4 \hat{F} H_4$ from the truncated matrix.
4. Calculate the Mean Squared Error (MSE) between the original image $f(x,y)$ and the reconstructed image $\hat{f}(x,y)$.

---

#### 💡 Step-by-Step Solution

##### 1. Forward 2D Hadamard Transform $F = H_4 f H_4$
The $4 \times 4$ Hadamard matrix $H_4$ is:

```math
H_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix}
```

**Step 1.1: Compute Intermediate Matrix $A = H_4 \cdot f$**

```math
A = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} \begin{bmatrix}
10 & 10 & 10 & 10 \\
10 & 10 & 10 & 10 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} = \begin{bmatrix}
20 & 20 & 20 & 20 \\
0 & 0 & 0 & 0 \\
20 & 20 & 20 & 20 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

**Step 1.2: Compute $F = A \cdot H_4$**

```math
F = \begin{bmatrix}
20 & 20 & 20 & 20 \\
0 & 0 & 0 & 0 \\
20 & 20 & 20 & 20 \\
0 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} = \begin{bmatrix}
80 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
80 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

##### 2. Coefficient Truncation
Retaining only the single DC coefficient $F(0,0) = 80$ and setting $F(2,0) = 80 	o 0$ produces the truncated spectrum $\hat{F}$:

```math
\hat{F}(u,v) = \begin{bmatrix}
80 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

##### 3. Reconstructing $\hat{f}(x,y) = \frac{1}{16} H_4 \hat{F} H_4$
**Step 3.1: Compute $B = H_4 \cdot \hat{F}$**

```math
B = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} \begin{bmatrix}
80 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} = \begin{bmatrix}
80 & 0 & 0 & 0 \\
80 & 0 & 0 & 0 \\
80 & 0 & 0 & 0 \\
80 & 0 & 0 & 0
\end{bmatrix}
```

**Step 3.2: Compute $C = B \cdot H_4$**

```math
C = \begin{bmatrix}
80 & 0 & 0 & 0 \\
80 & 0 & 0 & 0 \\
80 & 0 & 0 & 0 \\
80 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix} = \begin{bmatrix}
80 & 80 & 80 & 80 \\
80 & 80 & 80 & 80 \\
80 & 80 & 80 & 80 \\
80 & 80 & 80 & 80
\end{bmatrix}
```

**Step 3.3: Multiply by $\frac{1}{16}$**

```math
\hat{f}(x,y) = \frac{1}{16} \begin{bmatrix}
80 & 80 & 80 & 80 \\
80 & 80 & 80 & 80 \\
80 & 80 & 80 & 80 \\
80 & 80 & 80 & 80
\end{bmatrix} = \begin{bmatrix}
5 & 5 & 5 & 5 \\
5 & 5 & 5 & 5 \\
5 & 5 & 5 & 5 \\
5 & 5 & 5 & 5
\end{bmatrix}
```

The reconstructed image is a completely uniform grey image of intensity $5$ (the exact global average intensity of $f(x,y)$).

##### 4. Mean Squared Error (MSE) Calculation
The error matrix $e(x,y) = f(x,y) - \hat{f}(x,y)$ is:
* For top 2 rows ($10 - 5 = 5$): $e^2 = 5^2 = 25$ across 8 pixels.
* For bottom 2 rows ($0 - 5 = -5$): $e^2 = (-5)^2 = 25$ across 8 pixels.

```math
\text{MSE} = \frac{1}{16} \sum_{x=0}^3 \sum_{y=0}^3 \left[ f(x,y) - \hat{f}(x,y) \right]^2 = \frac{1}{16} \left[ 16 	imes 25 \right] = \mathbf{25.0}
```

---

<a id="section-3-discrete-cosine-transform-dct-image-compression-numericals"></a>

## Section 3: Discrete Cosine Transform (DCT) & Image Compression Numericals

<a id="numerical-31-2-times-2-2d-dct-matrix-multiplication-parseval-energy-check"></a>

### Numerical 3.1: $2 \times 2$ 2D DCT Matrix Multiplication & Parseval Energy Check

#### ❓ Problem Statement
**[Practice Problem — Core Concept Verification]**  
Given a $2 \times 2$ spatial image matrix $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
4 & 2 \\
1 & 3
\end{bmatrix}
```

1. Compute the 2D Discrete Cosine Transform $F(u,v)$ using the $2 \times 2$ orthonormal DCT matrix $C_2$.
2. Verify Parseval's energy conservation theorem between spatial and spectral domains.

---

#### 💡 Step-by-Step Solution

##### 1. Orthonormal $2 \times 2$ DCT Matrix Formulation
The 1D orthonormal $N$-point DCT matrix entries are $C(p,q) = \alpha(p) \cos\left[ \frac{(2q+1)p\pi}{2N} \right]$, where $\alpha(0) = \frac{1}{\sqrt{N}}$ and $\alpha(p) = \sqrt{\frac{2}{N}}$ for $p > 0$.  
For $N = 2$:
* $C(0,0) = \frac{1}{\sqrt{2}}$, $C(0,1) = \frac{1}{\sqrt{2}}$
* $C(1,0) = \sqrt{\frac{2}{2}} \cos\left(\frac{\pi}{4}\right) = \frac{1}{\sqrt{2}}$, $C(1,1) = \sqrt{\frac{2}{2}} \cos\left(\frac{3\pi}{4}\right) = -\frac{1}{\sqrt{2}}$

```math
C_2 = \begin{bmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

##### 2. Forward 2D DCT Matrix Product $F = C_2 f C_2^T$
**Step 2.1: Compute $A = C_2 \cdot f$**

```math
A = \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \begin{bmatrix}
4 & 2 \\
1 & 3
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
5 & 5 \\
3 & -1
\end{bmatrix}
```

**Step 2.2: Compute $F = A \cdot C_2^T$**

```math
F = \left( \frac{1}{\sqrt{2}} \begin{bmatrix}
5 & 5 \\
3 & -1
\end{bmatrix} \right) \left( \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix} \right) = \frac{1}{2} \begin{bmatrix}
5 & 5 \\
3 & -1
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

```math
F = \frac{1}{2} \begin{bmatrix}
(5+5) & (5-5) \\
(3-1) & (3+1)
\end{bmatrix} = \frac{1}{2} \begin{bmatrix}
10 & 0 \\
2 & 4
\end{bmatrix} = \begin{bmatrix}
5 & 0 \\
1 & 2
\end{bmatrix}
```

##### 3. Parseval Energy Verification
* **Spatial Energy:** $E_{\text{spatial}} = 4^2 + 2^2 + 1^2 + 3^2 = 16 + 4 + 1 + 9 = \mathbf{30}$
* **Spectral Energy:** $E_{\text{spectral}} = 5^2 + 0^2 + 1^2 + 2^2 = 25 + 0 + 1 + 4 = \mathbf{30}$

Since $E_{\text{spatial}} = E_{\text{spectral}} = 30$, **energy is 100% conserved under orthonormal DCT**.

---

<a id="numerical-32-4-times-4-2d-dct-matrix-multiplication-energy-compaction"></a>

### Numerical 3.2: $4 \times 4$ 2D DCT Matrix Multiplication & Energy Compaction

#### ❓ Problem Statement
**[Reported PYQ (unverified) — AKTU / University Exam Paper]**  
Given a $4 \times 4$ spatial image matrix $f(x,y)$:

```math
f(x,y) = \begin{bmatrix}
100 & 100 & 100 & 100 \\
100 & 100 & 100 & 100 \\
50 & 50 & 50 & 50 \\
50 & 50 & 50 & 50
\end{bmatrix}
```

1. Compute the 2D Discrete Cosine Transform $F(u,v)$ using the 4-point orthonormal DCT matrix $C_4$.
2. Calculate the total spectral energy and determine the percentage of energy concentrated in the DC component $F(0,0)$.

---

#### 💡 Step-by-Step Solution

##### 1. $4 \times 4$ Orthonormal DCT Matrix $C_4$
Evaluating $C_4(p,q) = \alpha(p) \cos\left[ \frac{(2q+1)p\pi}{8} \right]$:

```math
C_4 \approx \begin{bmatrix}
0.5000 & 0.5000 & 0.5000 & 0.5000 \\
0.6533 & 0.2706 & -0.2706 & -0.6533 \\
0.5000 & -0.5000 & -0.5000 & 0.5000 \\
0.2706 & -0.6533 & 0.6533 & -0.2706
\end{bmatrix}
```

##### 2. Matrix Product $F = C_4 f C_4^T$
**Step 2.1: Row-by-Row Product $A = C_4 \cdot f$**  
Note that $f$ has identical columns, so multiplying each row of $C_4$ by the columns of $f$:
* Row 0 of $C_4 \cdot f$: $0.5(100+100+50+50) = 0.5(300) = \mathbf{150}$ across all columns.
* Row 1 of $C_4 \cdot f$: $100(0.6533 + 0.2706) + 50(-0.2706 - 0.6533) = 100(0.9239) - 50(0.9239) = 50(0.9239) = \mathbf{46.195}$ across all columns.
* Row 2 of $C_4 \cdot f$: $0.5(100 - 100 - 50 + 50) = \mathbf{0}$ across all columns.
* Row 3 of $C_4 \cdot f$: $100(0.2706 - 0.6533) + 50(0.6533 - 0.2706) = 100(-0.3827) + 50(0.3827) = -50(0.3827) = \mathbf{-19.135}$ across all columns.

```math
A = C_4 \cdot f = \begin{bmatrix}
150.0 & 150.0 & 150.0 & 150.0 \\
46.195 & 46.195 & 46.195 & 46.195 \\
0.0 & 0.0 & 0.0 & 0.0 \\
-19.135 & -19.135 & -19.135 & -19.135
\end{bmatrix}
```

**Step 2.2: Compute $F = A \cdot C_4^T$**  
Multiplying row vector $[v, v, v, v]$ by Row 0 of $C_4^T$ ($[0.5, 0.5, 0.5, 0.5]^T$) yields $2v$, while multiplying by orthogonal rows 1, 2, 3 yields $0$:

```math
F(u,v) = \begin{bmatrix}
300.0 & 0.0 & 0.0 & 0.0 \\
92.390 & 0.0 & 0.0 & 0.0 \\
0.0 & 0.0 & 0.0 & 0.0 \\
-38.270 & 0.0 & 0.0 & 0.0
\end{bmatrix}
```

##### 3. Energy Compaction & Percentage Calculations
* **Total Spatial Energy $E_{\text{total}}$:**
  

```math
E_{\text{total}} = 8 	imes (100)^2 + 8 	imes (50)^2 = 80,000 + 20,000 = \mathbf{100,000}
```


* **Total Spectral Energy check (displayed four-decimal coefficients are approximate; exact orthonormal DCT gives 100,000):**
  

```math
E_{\text{spectral}} = (300)^2 + (92.390)^2 + (0)^2 + (-38.270)^2 = 90,000 + 8,535.9121 + 1,464.5929 = \mathbf{100,000.5050} \approx 100,000
```


* **DC Energy Percentage:**
  

```math
\text{DC Energy \%} = \frac{F(0,0)^2}{E_{\text{total}}} 	imes 100 = \frac{300^2}{100,000} 	imes 100 = \frac{90,000}{100,000} 	imes 100 = \mathbf{90.0\%}
```



A single coefficient $F(0,0)$ contains **90.0% of the entire image energy**, illustrating energy compaction for this particular image; the percentage is image-dependent.

---

<a id="numerical-33-dct-energy-retention-thresholding-86-875-94-thresholds"></a>

### Numerical 3.3: DCT Energy Retention Thresholding (86%, 87.5%, 94% Thresholds)

> **Attribution caveat:** This workbook uses the 120/-40 coefficient example; another supplied PYQ bank reports a different coefficient matrix for the same threshold percentages. Do not conflate their answers.

#### ❓ Problem Statement
**[Reported PYQ (unverified) — SVKM's NMIMS Final Exam 2024-25 (Q4a) / 2022-23 (Q4a)]**  
Given the following $4 \times 4$ Discrete Cosine Transform (DCT) coefficient matrix $F(u,v)$:

```math
F(u,v) = \begin{bmatrix}
120 & -30 & 10 & 0 \\
-40 & 15 & -5 & 0 \\
20 & -10 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

1. Compute the total energy $E_{\text{total}}$ present in the transform matrix.
2. Construct the squared energy matrix $E_{\text{sq}}(u,v) = |F(u,v)|^2$.
3. Perform coefficient selection to retain at least **86%**, **87.5%**, and **94%** of the total energy.
4. For each threshold, write down the truncated coefficient matrix $\hat{F}$, the number of retained coefficients, and the achieved energy percentage.

---

#### 💡 Step-by-Step Solution

##### 1. Total Energy $E_{\text{total}}$ & Squared Energy Matrix
The squared energy matrix $E_{\text{sq}}(u,v) = |F(u,v)|^2$ is:

```math
E_{\text{sq}}(u,v) = \begin{bmatrix}
120^2 & (-30)^2 & 10^2 & 0 \\
(-40)^2 & 15^2 & (-5)^2 & 0 \\
20^2 & (-10)^2 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix} = \begin{bmatrix}
14400 & 900 & 100 & 0 \\
1600 & 225 & 25 & 0 \\
400 & 100 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```

The total energy $E_{\text{total}}$ is the sum of all elements:



```math
E_{\text{total}} = 14400 + 900 + 100 + 1600 + 225 + 25 + 400 + 100 = \mathbf{17,750}
```



##### 2. Ranked Coefficient Cumulative Energy Table
Sorting non-zero coefficients in decreasing order of squared magnitude:

| Rank | Coefficient $F(u,v)$ | Value | Squared Energy | Cumulative Energy | Cumulative % of $E_{\text{total}}$ |
|---|---|---|---|---|---|
| **1** | $F(0,0)$ | $120$ | $14,400$ | $14,400$ | **81.13%** |
| **2** | $F(1,0)$ | $-40$ | $1,600$ | $16,000$ | **90.14%** |
| **3** | $F(0,1)$ | $-30$ | $900$ | $16,900$ | **95.21%** |
| **4** | $F(2,0)$ | $20$ | $400$ | $17,300$ | **97.46%** |
| **5** | $F(1,1)$ | $15$ | $225$ | $17,525$ | **98.73%** |
| **6** | $F(0,2)$ | $10$ | $100$ | $17,625$ | **99.30%** |
| **7** | $F(2,1)$ | $-10$ | $100$ | $17,725$ | **99.86%** |
| **8** | $F(1,2)$ | $-5$ | $25$ | $17,750$ | **100.00%** |

##### 3. Energy Threshold Selection & Masking

###### **Case A: Retaining $\ge 86\%$ Energy Target**
* Target energy requirement: $E_{\text{target}} = 0.86 \times 17,750 = \mathbf{15,265.0}$
* From the cumulative table:
  * 1 coefficient ($14,400$) $< 15,265.0$ (81.13%)
  * **2 coefficients** ($16,000$) $> 15,265.0$ (**90.14%**)
* **Retained Coefficients:** $F(0,0) = 120$ and $F(1,0) = -40$.
* **Truncated Matrix $\hat{F}_{86\%}$:**

```math
\hat{F}_{86\%} = \begin{bmatrix}
120 & 0 & 0 & 0 \\
-40 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```
* **Summary:** 2 coefficients retained out of 16 (87.5% of coefficients zeroed (not a measured bit-rate compression ratio)), achieving **90.14% energy retention**.

---

###### **Case B: Retaining $\ge 87.5\%$ Energy Target**
* Target energy requirement: $E_{\text{target}} = 0.875 \times 17,750 = \mathbf{15,531.25}$
* From the cumulative table:
  * 1 coefficient ($14,400$) $< 15,531.25$
  * **2 coefficients** ($16,000$) $> 15,531.25$ (**90.14%**)
* **Retained Coefficients:** $F(0,0) = 120$ and $F(1,0) = -40$.
* **Truncated Matrix $\hat{F}_{87.5\%}$:**

```math
\hat{F}_{87.5\%} = \begin{bmatrix}
120 & 0 & 0 & 0 \\
-40 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```
* **Summary:** Exactly 2 coefficients retained, achieving **90.14% energy retention**.

---

###### **Case C: Retaining $\ge 94\%$ Energy Target**
* Target energy requirement: $E_{\text{target}} = 0.94 \times 17,750 = \mathbf{16,685.0}$
* From the cumulative table:
  * 2 coefficients ($16,000$) $< 16,685.0$ (90.14%)
  * **3 coefficients** ($16,900$) $> 16,685.0$ (**95.21%**)
* **Retained Coefficients:** $F(0,0) = 120$, $F(1,0) = -40$, and $F(0,1) = -30$.
* **Truncated Matrix $\hat{F}_{94\%}$:**

```math
\hat{F}_{94\%} = \begin{bmatrix}
120 & -30 & 0 & 0 \\
-40 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
```
* **Summary:** 3 coefficients retained out of 16 (81.25% of coefficients zeroed (not a measured bit-rate compression ratio)), achieving **95.21% energy retention**.

---

<a id="numerical-34-complete-8-times-8-jpeg-compression-pipeline-walkthrough"></a>

### Numerical 3.4: JPEG $8 \times 8$ Transform/Quantization Walkthrough

#### ❓ Problem Statement
**[Practice Problem — JPEG Workflow Verification]**  
Work through an $8 \times 8$ block JPEG transform, quantization, and reconstruction example for an $8 \times 8$ spatial block with a uniform intensity of $f(x,y) = 160$:
1. Perform Level Shift (subtract 128).
2. Calculate the 2D DCT $F(u,v)$.
3. Quantize $F(u,v)$ using the standard JPEG Luminance Quantization Matrix $Q_{luminance}$ (where $Q(0,0) = 16$).
4. Dequantize and reconstruct the spatial block using Inverse 2D DCT (IDCT) and Inverse Level Shift (+128).

---

#### 💡 Step-by-Step Solution

##### 1. Level Shift (-128)
Subtracting $128$ from $f(x,y) = 160$ gives a shifted block $f_{\text{shift}}(x,y) = 32$ across all $8 \times 8$ pixels.

##### 2. $8 \times 8$ 2D DCT Calculation
For a uniform matrix where all pixels equal $32$:
* **DC Component $F(0,0)$:**
  

```math
F(0,0) = \alpha(0)\alpha(0) \sum_{x=0}^7 \sum_{y=0}^7 32 = \frac{1}{\sqrt{8}} \frac{1}{\sqrt{8}} (64 	imes 32) = \frac{1}{8} (2048) = \mathbf{256}
```


* **AC Components $F(u,v)$ for $(u,v) \neq (0,0)$:**
  Since the image is completely flat, spatial variation is zero, so all AC coefficients evaluate to $\mathbf{0}$.

```math
F(u,v) = \begin{bmatrix}
256 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

##### 3. Quantization Step
Dividing $F(u,v)$ by the standard JPEG Luminance matrix $Q$, where $Q(0,0) = 16$:

```math
F_Q(0,0) = \text{round}\left( \frac{F(0,0)}{Q(0,0)} \right) = \text{round}\left( \frac{256}{16} \right) = \mathbf{16}
```

All AC coefficients remain $0 / Q(u,v) = 0$.  
The quantized matrix has **1 non-zero coefficient for $F_Q(0,0) = 16$ and 63 zeroes**, yielding extreme compression via run-length encoding.

##### 4. Dequantization & IDCT Reconstruction
* **Dequantized DC:** $\hat{F}(0,0) = F_Q(0,0) 	imes Q(0,0) = 16 	imes 16 = \mathbf{256}$.
* **IDCT Reconstruction:** Converts $\hat{F}(0,0) = 256$ back to spatial domain $\hat{f}_{\text{shift}}(x,y) = 32$.
* **Inverse Level Shift (+128):** $\hat{f}(x,y) = 32 + 128 = \mathbf{160}$.

In this simplified block example, the spatial image is reconstructed **without loss** because $256$ is an exact integer multiple of $Q(0,0) = 16$.

---

<a id="section-4-formula-transform-matrix-master-reference"></a>

## Section 4: Formula & Transform Matrix Master Reference

### 1. Discrete Fourier Transform (DFT)

```math
\text{1D Forward DFT:} \quad X(k) = \sum_{n=0}^{N-1} x(n) W_N^{kn} \quad \text{where } W_N = e^{-j \frac{2\pi}{N}}
```

```math
\text{1D Inverse DFT:} \quad x(n) = \frac{1}{N} \sum_{k=0}^{N-1} X(k) W_N^{-kn}
```

```math
\text{2D Separable DFT Matrix Product:} \quad F = W_M f W_N^T
```

```math
\text{2D Separable IDFT Matrix Product:} \quad f = \frac{1}{MN} W_M^* F (W_N^*)^T
```

```math
\text{2-Point DFT Matrix } W_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}, \quad \text{4-Point DFT Matrix } W_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -j & -1 & j \\
1 & -1 & 1 & -1 \\
1 & j & -1 & -j
\end{bmatrix}
```

---

### 2. Hadamard Transform

```math
\text{2-Point Hadamard Matrix } H_2 = \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

```math
\text{4-Point Hadamard Matrix } H_4 = \begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & -1 & 1 & -1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1
\end{bmatrix}
```

```math
\text{Recursive Construction:} \quad H_{2N} = \begin{bmatrix}
H_N & H_N \\
H_N & -H_N
\end{bmatrix}
```

```math
\text{2D Unnormalized Hadamard Pair:} \quad F = H_N f H_N \quad \iff \quad f = \frac{1}{N^2} H_N F H_N
```

---

### 3. Discrete Cosine Transform (DCT)

```math
\text{1D Orthonormal DCT:} \quad C(p,q) = \alpha(p) \cos\left[ \frac{(2q+1)p\pi}{2N} \right] \quad \text{where } \alpha(0) = \sqrt{\frac{1}{N}}, \quad \alpha(p) = \sqrt{\frac{2}{N}}
```

```math
\text{2D Separable DCT Pair:} \quad F = C_N f C_N^T \quad \iff \quad f = C_N^T F C_N
```

```math
\text{2-Point Orthonormal DCT } C_2 = \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
```

```math
\text{4-Point Orthonormal DCT } C_4 \approx \begin{bmatrix}
0.5000 & 0.5000 & 0.5000 & 0.5000 \\
0.6533 & 0.2706 & -0.2706 & -0.6533 \\
0.5000 & -0.5000 & -0.5000 & 0.5000 \\
0.2706 & -0.6533 & 0.6533 & -0.2706
\end{bmatrix}
```

---

<a id="section-5-summary-answer-index"></a>

## Section 5: Summary Answer Index

#### Numerical 1.1
**Key Input Parameters:**
$x(n) = \{0, 1, 2, 1\}$
**Primary Result / Matrix:**
$X(k) = \{4, -2, 0, -2\}$
**Energy / Key Metric:**
$E_{\text{spatial}} = E_{\text{spectral}} = 6$

#### Numerical 1.2
**Key Input Parameters:**

```math
f = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
```

**Primary Result / Matrix:**

```math
F = \begin{bmatrix}
10 & -2 \\
-4 & 0
\end{bmatrix}
```

**Energy / Key Metric:**
$E_{\text{spatial}} = E_{\text{spectral}} = 30$, $F(0,0)=10$

#### Numerical 1.3
**Key Input Parameters:**

```math
f = \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix}
```

**Primary Result / Matrix:**

```math
F = \begin{bmatrix}
8 & -2 \\
2 & 0
\end{bmatrix}
```

**Energy / Key Metric:**
$E_{\text{spatial}} = E_{\text{spectral}} = 18$

#### Numerical 1.4
**Key Input Parameters:**
$4 \times 4$ stripe pattern
**Primary Result / Matrix:**
$F(2,0)=8$ and $F(2,2)=8$; all other coefficients are zero
**Energy / Key Metric:**
Shifted DC at $F(2,2)=8$; $F(2,0)=8$ is non-DC

#### Numerical 2.1
**Key Input Parameters:**
$x = [1, 2, 0, 3]^T$
**Primary Result / Matrix:**
$y = [6, -4, 0, 2]^T$
**Energy / Key Metric:**
Sequencies = $\{0, 3, 1, 2\}$

#### Numerical 2.2
**Key Input Parameters:**

```math
f = \begin{bmatrix}
2 & 6 \\
3 & 5
\end{bmatrix}
```

**Primary Result / Matrix:**

```math
F = \begin{bmatrix}
16 & -6 \\
0 & -2
\end{bmatrix}
```

**Energy / Key Metric:**
Exact $f$ reconstruction with $\frac{1}{4}$ scaling

#### Numerical 2.3
**Key Input Parameters:**

```math
f = \begin{bmatrix}
2 & 3 \\
1 & 2
\end{bmatrix}
```

**Primary Result / Matrix:**

```math
F = \begin{bmatrix}
8 & -2 \\
2 & 0
\end{bmatrix}
```

**Energy / Key Metric:**
Exact $f$ reconstruction with $\frac{1}{4}$ scaling

#### Numerical 2.4
**Key Input Parameters:**
$4 \times 4$ edge image
**Primary Result / Matrix:**
$\hat{f} = \text{matrix of all } 5\text{s}$
**Energy / Key Metric:**
$\text{MSE} = 25.0$ after DC truncation

#### Numerical 3.1
**Key Input Parameters:**

```math
f = \begin{bmatrix}
4 & 2 \\
1 & 3
\end{bmatrix}
```

**Primary Result / Matrix:**

```math
F = \begin{bmatrix}
5 & 0 \\
1 & 2
\end{bmatrix}
```

**Energy / Key Metric:**
$E_{\text{spatial}} = E_{\text{spectral}} = 30$

#### Numerical 3.2
**Key Input Parameters:**
$4 \times 4$ step matrix
**Primary Result / Matrix:**

```math
F = \begin{bmatrix}
300 & 0 & 0 & 0 \\
92.39 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
-38.27 & 0 & 0 & 0
\end{bmatrix}
```

**Energy / Key Metric:**
$E_{\text{total}} = 100,000$, $\text{DC \%} = 90.0\%$

#### Numerical 3.3
**Key Input Parameters:**
$4 \times 4$ DCT matrix
**Primary Result / Matrix:**
$86\% 	o 2 \text{ coeffs } (90.14\%)$, $87.5\% 	o 2 \text{ coeffs } (90.14\%)$, $94\% 	o 3 \text{ coeffs } (95.21\%)$
**Energy / Key Metric:**
$E_{\text{total}} = 17,750$

#### Numerical 3.4
**Key Input Parameters:**
$8 \times 8$ uniform 160
**Primary Result / Matrix:**
$F_Q(0,0) = 16$, all AC = 0
**Energy / Key Metric:**
Perfect reconstruction after dequantization


---

<a id="section-6-common-numerical-mistakes-pitfalls"></a>

## Section 6: Common Numerical Mistakes & Pitfalls

1. ⚠️ **Forgetting the Inverse Scaling Factor ($\frac{1}{N^2}$):**
   * Unnormalized 2D Hadamard and 2D DFT inverse transforms require dividing by $N^2$ (or $MN$). Forgetting $\frac{1}{4}$ ($2 \times 2$) or $\frac{1}{16}$ ($4 \times 4$) yields outputs scaled up by $N^2$.

2. ⚠️ **Confusing Orthonormal DCT with Unnormalized Transforms:**
   * Orthonormal DCT matrices ($C \cdot C^T = I$) preserve energy directly ($E_{\text{spatial}} = E_{\text{spectral}}$) without additional $\frac{1}{N^2}$ scaling during inverse transformation ($f = C^T F C$).

3. ⚠️ **Incorrect Energy Thresholding Sorting Criterion:**
   * In DCT energy retention problems, coefficients MUST be ranked by **squared magnitude $|F(u,v)|^2$**, not raw coefficient values. A negative coefficient like $-40$ has squared energy $1600$, which is larger than $+30$ (squared energy $900$).

4. ⚠️ **Mixing up $W_4$ Twiddle Factor Signs:**
   * In 1D/2D DFT twiddle matrix $W_4$, the second row is $[1, -j, -1, j]$ (negative $j$). In the conjugate matrix $W_4^*$ used for IDFT, the second row becomes $[1, +j, -1, -j]$.

---

<a id="section-7-source-status-checklist"></a>

## Section 7: Source Status Checklist

- [ ] Original NMIMS and AKTU examination papers not supplied; the paper attributions above remain reported and unverified
- [x] All Hadamard matrix products and sequency problems checked
- [x] $4 	imes 4$ Hadamard truncation and MSE calculation independently re-derived
- [x] DCT orthonormal matrix products and 86%/87.5%/94% energy thresholding re-calculated in Python
- [x] Complete formula reference sheet and answer index updated
- [x] GitHub math formatting checked: balanced standalone `math` fences and multiline matrices
