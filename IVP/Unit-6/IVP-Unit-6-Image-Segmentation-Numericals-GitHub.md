# Unit 6: Image Segmentation — Solved Numericals & Exam Guide

---

## 1. Overview of Unit 6 Numerical Problem Types

Unit 6 (Image Segmentation) numerical problems in Image and Video Processing (IVP) term-end examinations test both fundamental pixel-level relationships and statistical region-partitioning algorithms. This study guide provides comprehensive, step-by-step solved numericals for all six core problem types asked in university question papers.

### Summary of Unit 6 Numerical Problem Types

| Problem Type | Topic / Algorithm | Core Formulas & Operational Steps | Key Exam Objective |
| :--- | :--- | :--- | :--- |
| **Type 1** | Pixel Connectivity & Distance Measures | $`D_e, D_4, D_8`$, 4-Adjacency, 8-Adjacency, $`m`$-Adjacency, 2-Pass CCL | Compute distances, determine shortest paths, and perform component labeling. |
| **Type 2** | Bayesian Pixel Classification | $`P(C_i \mid z) = \frac{p(z \mid C_i)P(C_i)}{p(z)}`$, Likelihood Ratio Test, Threshold $`T^*`$ | Classify pixels as foreground/background and find optimal minimum-error threshold. |
| **Type 3** | Expectation-Maximization (EM) Binarization | E-step (Responsibilities $`\gamma_{i,k}`$), M-step (Updates for $`\mu_k, \sigma_k^2, \pi_k`$) | Iteratively estimate Gaussian Mixture Model (GMM) parameters for overlapping distributions. |
| **Type 4** | Otsu's Optimal Thresholding | Maximize $`\sigma_B^2(k) = \omega_0(k) \omega_1(k) [\mu_0(k) - \mu_1(k)]^2`$ | Compute cumulative weights, class means, and find optimal threshold $`T^*`$. |
| **Type 5** | Region Growing Segmentation | Seed selection, Predicate $`\lvert f(x,y) - \mu_R \rvert \le T`$, Iterative Aggregation | Grow contiguous regions from initial seed pixels until stopping criteria are met. |
| **Type 6** | Region Splitting & Merging (Quadtree) | Homogeneity Predicate $`Q(R_i) = (\max - \min) \le T`$, Quadtree Decomposition | Perform hierarchical 4-way splitting and merge adjacent uniform sub-quadrants. |

---

## 2. Solved Numerical Type 1: Pixel Connectivity, Distance Measures, and Component Labeling

### Mathematical Formulas & Concepts

1. **Euclidean Distance ($`D_e`$):**

```math
D_e(p, q) = \sqrt{(x - s)^2 + (y - t)^2}
```

2. **City-Block / Manhattan Distance ($`D_4`$):**

```math
D_4(p, q) = \lvert x - s \rvert + \lvert y - t \rvert
```

3. **Chessboard Distance ($`D_8`$):**

```math
D_8(p, q) = \max(\lvert x - s \rvert, \lvert y - t \rvert)
```

4. **m-Adjacency (Mixed Adjacency):**
   Two pixels $`p`$ and $`q`$ with values from intensity set $`V`$ are $`m`$-adjacent if:
   * $`q \in N_4(p)`$, **OR**
   * $`q \in N_D(p)`$ **AND** the intersection set $`N_4(p) \cap N_4(q)`$ contains **no** pixels with intensity values belonging to set $`V`$.

---

### Solved Problem 1.1: Distance Measures and $`m`$-Connectivity Path

#### Problem Statement

Consider the following $`4 \times 4`$ grayscale image matrix $`I`$ with pixel coordinates indexed from $`(0,0)`$ at top-left to $`(3,3)`$ at bottom-right:

```math
I = \begin{bmatrix}
0 & 1 & 2 & 0 \\
2 & 5 & 6 & 1 \\
1 & 4 & 7 & 3 \\
0 & 2 & 5 & 1
\end{bmatrix}
```

1. Calculate the Euclidean distance $`D_e`$, City-Block distance $`D_4`$, and Chessboard distance $`D_8`$ between pixel $`p(0,0)`$ and pixel $`q(3,3)`$.
2. For the intensity value set $`V = \{1, 2, 4, 5, 6, 7\}`$, determine whether an $`m`$-connected path exists between pixel $`a(2,0)`$ (value $`1`$) and pixel $`b(0,2)`$ (value $`2`$). If it exists, write the complete coordinate path and state the path length.

---

#### Step-by-Step Solution

##### Step 1: Calculate Distance Measures between $`p(0,0)`$ and $`q(3,3)`$

Given coordinates $`(x,y) = (0,0)`$ and $`(s,t) = (3,3)`$:

1. **Euclidean Distance ($`D_e`$):**

```math
D_e(p, q) = \sqrt{(3 - 0)^2 + (3 - 0)^2} = \sqrt{9 + 9} = \sqrt{18} \approx 4.2426
```

2. **City-Block Distance ($`D_4`$):**

```math
D_4(p, q) = \lvert 3 - 0 \rvert + \lvert 3 - 0 \rvert = 3 + 3 = 6
```

3. **Chessboard Distance ($`D_8`$):**

```math
D_8(p, q) = \max(\lvert 3 - 0 \rvert, \lvert 3 - 0 \rvert) = \max(3, 3) = 3
```

---

##### Step 2: Determine $`m`$-Connected Path between $`a(2,0)`$ and $`b(0,2)`$

Intensity set $`V = \{1, 2, 4, 5, 6, 7\}`$.

1. **From $`a(2,0)`$ (value $`1`$) to $`(2,1)`$ (value $`4`$):**
   $`(2,1) \in N_4(2,0)`$ and intensity $`4 \in V`$. Valid 4-adjacent transition.

2. **From $`(2,1)`$ (value $`4`$) to $`(1,2)`$ (value $`6`$):**
   * $`(1,2)`$ is a diagonal neighbor of $`(2,1)`$, so $`(1,2) \in N_D(2,1)`$.
   * Calculate intersection of 4-neighbors: $`N_4(2,1) \cap N_4(1,2)`$.
     $`N_4(2,1) = \{(1,1), (3,1), (2,0), (2,2)\}`$.
     $`N_4(1,2) = \{(0,2), (2,2), (1,1), (1,3)\}`$.
     Intersection set $`N_4(2,1) \cap N_4(1,2) = \{(1,1), (2,2)\}`$.
   * Intensity at $`(1,1) = 5 \in V`$.
   * Since $`(1,1) \in V`$, the diagonal transition $`(2,1) \to (1,2)`$ fails $`m`$-adjacency condition 2!
   * Therefore, we must go through 4-neighbor $`(1,1)`$ instead:
     $`(2,1) \to (1,1)`$ (since $`(1,1) \in N_4(2,1)`$) and $`(1,1) \to (1,2)`$ (since $`(1,2) \in N_4(1,1)`$).

3. **From $`(1,2)`$ (value $`6`$) to $`b(0,2)`$ (value $`2`$):**
   $`(0,2) \in N_4(1,2)`$ and intensity $`2 \in V`$. Valid 4-adjacent transition.

---

#### Final Answer

1. Distance measures:
   * **Euclidean Distance ($`D_e`$):** $`4.2426`$ (rounded to 4 decimal places)
   * **City-Block Distance ($`D_4`$):** $`6`$
   * **Chessboard Distance ($`D_8`$):** $`3`$
2. $`m`$-Connected Path:
   * **Path:** $`(2,0) \to (2,1) \to (1,1) \to (1,2) \to (0,2)`$
   * **Path Length:** $`4`$ path segments ($`5`$ pixels)

---

### Solved Problem 1.2: Connected Component Labeling (CCL)

#### Problem Statement

Apply the **Two-Pass Sequential Connected Component Labeling (CCL)** algorithm using **4-connectivity** and **8-connectivity** on the following binary image matrix $`B`$ (where foreground set $`V = \{1\}`$):

```math
B = \begin{bmatrix}
1 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 1 & 1
\end{bmatrix}
```

Show the provisional label matrix after Pass 1, the equivalence table, and the final resolved label matrix after Pass 2.

---

#### Step-by-Step Solution

##### Step 1: 4-Connected Component Labeling

* **Pass 1 (Scanning & Equivalence Generation):**
  * Pixel $`(0,0) = 1`$: No top or left neighbor $\implies$ Assign **Label 1**.
  * Pixel $`(0,1) = 1`$: Left neighbor is $`1`$ (Label 1) $\implies$ Assign **Label 1**.
  * Pixel $`(1,0) = 1`$: Top neighbor is $`1`$ (Label 1) $\implies$ Assign **Label 1**.
  * Pixel $`(1,1) = 1`$: Top & Left neighbors have Label 1 $\implies$ Assign **Label 1**.
  * Pixel $`(2,2) = 1`$: Top $`(1,2)=0$` and Left $`(2,1)=0$` $\implies$ Assign **Label 2**.
  * Pixel $`(2,3) = 1`$: Left neighbor is Label 2 $\implies$ Assign **Label 2**.
  * Pixel $`(3,2) = 1`$: Top neighbor is Label 2 $\implies$ Assign **Label 2**.
  * Pixel $`(3,3) = 1`$: Top & Left neighbors have Label 2 $\implies$ Assign **Label 2**.

* **Equivalence Table:** No label conflicts occurred.

* **Final 4-Connected Label Matrix ($`L_4`$):**

```math
L_4 = \begin{bmatrix}
1 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 \\
0 & 0 & 2 & 2 \\
0 & 0 & 2 & 2
\end{bmatrix}
```

---

##### Step 2: 8-Connected Component Labeling

* **Pass 1 (8-Neighborhood Inspection):**
  * Pixels $`(0,0), (0,1), (1,0), (1,1)`$ are assigned **Label 1**.
  * Pixel $`(2,2) = 1`$: Inspect 8-neighbors already processed: top-left diagonal neighbor is $`(1,1)`$ with **Label 1**. Assign **Label 1**.
  * Pixels $`(2,3), (3,2), (3,3)`$ inherit **Label 1** from their neighbors.

* **Final 8-Connected Label Matrix ($`L_8`$):**

```math
L_8 = \begin{bmatrix}
1 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 1 & 1
\end{bmatrix}
```

---

#### Final Answer

* **4-Connected Components Count:** $`2`$ distinct foreground objects.
* **8-Connected Components Count:** $`1`$ connected foreground object (merged via diagonal connection at $`(1,1) \to (2,2)`$).

---

## 3. Solved Numerical Type 2: Bayesian Pixel Classification & Optimal Thresholding

### Mathematical Formulas

1. **Bayes Posterior Probability:**

```math
P(C_i \mid z) = \frac{p(z \mid C_i) P(C_i)}{p(z)}
```

2. **1D Gaussian Class-Conditional Likelihood:**

```math
p(z \mid C_i) = \frac{1}{\sqrt{2\pi}\sigma_i} \exp\left(-\frac{(z - \mu_i)^2}{2\sigma_i^2}\right)
```

3. **Bayes Decision Boundary Equation (Equal Risk Threshold $`T^*`$):**

```math
p(T^* \mid F) P(F) = p(T^* \mid B) P(B)
```

---

### Solved Problem 2.1: Bayesian Posterior Calculation and Classification

#### Problem Statement

In a medical image binarization task, pixel gray levels for Foreground ($`F`$) and Background ($`B`$) follow 1D Gaussian distributions with the following parameters:
* **Foreground ($`F`$):** Mean $`\mu_F = 180`$, Standard Deviation $`\sigma_F = 20`$, Prior $`P(F) = 0.4`$
* **Background ($`B`$):** Mean $`\mu_B = 60`$, Standard Deviation $`\sigma_B = 15`$, Prior $`P(B) = 0.6`$

Given an observed pixel with gray-level intensity $`z = 120`$:
1. Calculate class likelihoods $`p(z \mid F)`$ and $`p(z \mid B)`$.
2. Calculate posterior probabilities $`P(F \mid z)`$ and $`P(B \mid z)`$.
3. Classify the pixel using Bayes Minimum Error Decision Rule.

---

#### Step-by-Step Solution

##### Step 1: Calculate Likelihoods $`p(z=120 \mid F)`$ and $`p(z=120 \mid B)`$

1. **Foreground Likelihood $`p(120 \mid F)`$:**

```math
p(120 \mid F) = \frac{1}{\sqrt{2\pi}(20)} \exp\left(-\frac{(120 - 180)^2}{2(20)^2}\right)
```

   * Scaling factor: $`\frac{1}{20\sqrt{2\pi}} = \frac{1}{50.132565} \approx 0.019947`$
   * Exponent factor: $`-\frac{(-60)^2}{2(400)} = -\frac{3600}{800} = -4.5`$
   * Exponential value: $`\exp(-4.5) \approx 0.011109`$
   * $`p(120 \mid F) = 0.019947 \times 0.011109 = 0.00022159 = 2.2159 \times 10^{-4}`$

2. **Background Likelihood $`p(120 \mid B)`$:**

```math
p(120 \mid B) = \frac{1}{\sqrt{2\pi}(15)} \exp\left(-\frac{(120 - 60)^2}{2(15)^2}\right)
```

   * Scaling factor: $`\frac{1}{15\sqrt{2\pi}} = \frac{1}{37.599424} \approx 0.026596`$
   * Exponent factor: $`-\frac{(60)^2}{2(225)} = -\frac{3600}{450} = -8.0`$
   * Exponential value: $`\exp(-8.0) \approx 0.00033546`$
   * $`p(120 \mid B) = 0.026596 \times 0.00033546 = 0.000008922 = 8.9220 \times 10^{-6}`$

---

##### Step 2: Calculate Weighted Likelihoods & Posterior Probabilities

1. **Weighted Foreground Likelihood:**

```math
p(120 \mid F) P(F) = (2.2159 \times 10^{-4}) \times 0.4 = 8.8636 \times 10^{-5}
```

2. **Weighted Background Likelihood:**

```math
p(120 \mid B) P(B) = (8.9220 \times 10^{-6}) \times 0.6 = 5.3532 \times 10^{-6}
```

3. **Total Evidence $`p(z=120)`$:**

```math
p(120) = 8.8636 \times 10^{-5} + 5.3532 \times 10^{-6} = 9.3989 \times 10^{-5}
```

4. **Posterior Probabilities:**

```math
P(F \mid z=120) = \frac{8.8636 \times 10^{-5}}{9.3989 \times 10^{-5}} \approx 0.9430 \quad (94.30\%)
```

```math
P(B \mid z=120) = \frac{5.3532 \times 10^{-6}}{9.3989 \times 10^{-5}} \approx 0.0570 \quad (5.70\%)
```

---

#### Final Answer

* **Class Likelihoods:** $`p(120 \mid F) = 2.2159 \times 10^{-4}`$, $`p(120 \mid B) = 8.9220 \times 10^{-6}`$
* **Posterior Probabilities:** $`P(F \mid z=120) = 0.9430`$, $`P(B \mid z=120) = 0.0570`$
* **Decision:** Since $`P(F \mid z=120) = 0.9430 > P(B \mid z=120) = 0.0570`$, the pixel is **classified as Foreground ($`F`$)**.

---

## 4. Solved Numerical Type 3: Expectation-Maximization (EM) Algorithm Iteration

### Mathematical Formulas

1. **E-Step (Responsibility Calculation $`\gamma_{i,k}`$):**

```math
\gamma_{i,k} = \frac{\pi_k \mathcal{N}(x_i \mid \mu_k, \sigma_k^2)}{\sum_{j} \pi_j \mathcal{N}(x_i \mid \mu_j, \sigma_j^2)}
```

2. **M-Step (Parameter Updates):**

```math
N_k = \sum_{i=1}^N \gamma_{i,k}
```

```math
\mu_k^{\text{new}} = \frac{\sum_{i=1}^N \gamma_{i,k} x_i}{N_k}
```

```math
(\sigma_k^2)^{\text{new}} = \frac{\sum_{i=1}^N \gamma_{i,k} (x_i - \mu_k^{\text{new}})^2}{N_k}
```

```math
\pi_k^{\text{new}} = \frac{N_k}{N}
```

---

### Solved Problem 3.1: Full EM Algorithm Iteration

#### Problem Statement

Given a 1D pixel intensity dataset $`X = [10, 20, 180, 200]`$, initialize a 2-component Gaussian Mixture Model (GMM) with initial parameters:
* **Background ($`b`$):** $`\mu_b^{(0)} = 15`$, $`\sigma_b^{(0)} = 10`$, $`\pi_b^{(0)} = 0.5`$
* **Foreground ($`f`$):** $`\mu_f^{(0)} = 190`$, $`\sigma_f^{(0)} = 10`$, $`\pi_f^{(0)} = 0.5`$

Perform **one complete EM iteration** (E-Step and M-Step) to compute updated parameters $`\mu_b^{\text{new}}, \mu_f^{\text{new}}, (\sigma_b^2)^{\text{new}}, (\sigma_f^2)^{\text{new}}, \pi_b^{\text{new}}, \pi_f^{\text{new}}`$.

---

#### Step-by-Step Solution

##### Step 1: E-Step (Compute Likelihoods and Responsibilities $`\gamma_{i,k}`$)

Gaussian PDF: $`\mathcal{N}(x \mid \mu, \sigma) = \frac{1}{\sqrt{2\pi}(10)} \exp\left(-\frac{(x-\mu)^2}{200}\right)`$.
Scaling factor: $`\frac{1}{10\sqrt{2\pi}} \approx 0.039894`$.

1. **For $`x_1 = 10`$:**
   * $`\mathcal{N}(10 \mid 15, 10^2) = 0.039894 \times e^{-25/200} = 0.039894 \times e^{-0.125} = 0.0352065`$
   * $`\mathcal{N}(10 \mid 190, 10^2) = 0.039894 \times e^{-32400/200} = 0.039894 \times e^{-162} \approx 0.0000`$
   * Responsibilities: $`\gamma_{1,b} \approx 1.0000`$, $`\gamma_{1,f} \approx 0.0000`$.

2. **For $`x_2 = 20`$:**
   * $`\mathcal{N}(20 \mid 15, 10^2) = 0.039894 \times e^{-25/200} = 0.0352065`$
   * $`\mathcal{N}(20 \mid 190, 10^2) \approx 0.0000`$
   * Responsibilities: $`\gamma_{2,b} \approx 1.0000`$, $`\gamma_{2,f} \approx 0.0000`$.

3. **For $`x_3 = 180`$:**
   * $`\mathcal{N}(180 \mid 15, 10^2) \approx 0.0000`$
   * $`\mathcal{N}(180 \mid 190, 10^2) = 0.039894 \times e^{-100/200} = 0.039894 \times e^{-0.5} = 0.024197`$
   * Responsibilities: $`\gamma_{3,b} \approx 0.0000`$, $`\gamma_{3,f} \approx 1.0000`$.

4. **For $`x_4 = 200`$:**
   * $`\mathcal{N}(200 \mid 15, 10^2) \approx 0.0000`$
   * $`\mathcal{N}(200 \mid 190, 10^2) = 0.039894 \times e^{-100/200} = 0.024197`$
   * Responsibilities: $`\gamma_{4,b} \approx 0.0000`$, $`\gamma_{4,f} \approx 1.0000`$.

---

##### Step 2: M-Step (Update GMM Parameters)

1. **Effective Pixel Counts:**
   * $`N_b = \sum \gamma_{i,b} = 1.0 + 1.0 + 0.0 + 0.0 = 2.0000`$
   * $`N_f = \sum \gamma_{i,f} = 0.0 + 0.0 + 1.0 + 1.0 = 2.0000`$

2. **Updated Means:**

```math
\mu_b^{\text{new}} = \frac{(1.0 \times 10) + (1.0 \times 20)}{2.0} = \frac{30}{2.0} = 15.0000
```

```math
\mu_f^{\text{new}} = \frac{(1.0 \times 180) + (1.0 \times 200)}{2.0} = \frac{380}{2.0} = 190.0000
```

3. **Updated Variances:**

```math
(\sigma_b^2)^{\text{new}} = \frac{1.0 \times (10 - 15)^2 + 1.0 \times (20 - 15)^2}{2.0} = \frac{25 + 25}{2.0} = 25.0000
```

```math
(\sigma_f^2)^{\text{new}} = \frac{1.0 \times (180 - 190)^2 + 1.0 \times (200 - 190)^2}{2.0} = \frac{100 + 100}{2.0} = 100.0000
```

4. **Updated Prior Mixing Coefficients:**

```math
\pi_b^{\text{new}} = \frac{2.0}{4} = 0.5000, \quad \pi_f^{\text{new}} = \frac{2.0}{4} = 0.5000
```

---

#### Final Answer

* **Updated Background Parameters:** $`\mu_b^{\text{new}} = 15.0000`$, $`(\sigma_b^2)^{\text{new}} = 25.0000`$, $`\pi_b^{\text{new}} = 0.5000`$
* **Updated Foreground Parameters:** $`\mu_f^{\text{new}} = 190.0000`$, $`(\sigma_f^2)^{\text{new}} = 100.0000`$, $`\pi_f^{\text{new}} = 0.5000`$

---

## 5. Solved Numerical Type 4: Otsu's Thresholding Method

### Mathematical Formulas

1. **Normalized Histogram Probability:**

```math
p_i = \frac{n_i}{N}
```

2. **Global Mean Intensity ($`m_G`$):**

```math
m_G = \sum_{i=0}^{L-1} i \cdot p_i
```

3. **Class Cumulative Probabilities (Weights):**

```math
\omega_0(k) = \sum_{i=0}^k p_i, \quad \omega_1(k) = 1 - \omega_0(k)
```

4. **Class Mean Intensities:**

```math
\mu_0(k) = \frac{\sum_{i=0}^k i \cdot p_i}{\omega_0(k)}, \quad \mu_1(k) = \frac{m_G - \sum_{i=0}^k i \cdot p_i}{1 - \omega_0(k)}
```

5. **Between-Class Variance ($`\sigma_B^2(k)`$):**

```math
\sigma_B^2(k) = \omega_0(k) \omega_1(k) [\mu_0(k) - \mu_1(k)]^2
```

---

### Solved Problem 4.1: Otsu Thresholding on 6 Gray Levels

#### Problem Statement

An image with $`L = 6`$ gray levels ($`0`$ to $`5`$) and total pixel count $`N = 36`$ has the following histogram distribution:

| Gray Level ($`i`$) | 0 | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Pixel Count ($`n_i`$)** | 9 | 6 | 4 | 5 | 8 | 4 |

Calculate $`\omega_0(k), \mu_0(k), \omega_1(k), \mu_1(k)`$, and between-class variance $`\sigma_B^2(k)`$ for all candidate thresholds $`k \in \{0, 1, 2, 3, 4\}`$, and determine the optimal Otsu threshold $`T^*`$.

---

#### Step-by-Step Solution

##### Step 1: Compute Probabilities $`p_i`$ and Global Mean $`m_G`$

Total pixels $`N = 36`$.
* $`p_0 = 9/36 = 0.2500`$
* $`p_1 = 6/36 = 0.1667`$
* $`p_2 = 4/36 = 0.1111`$
* $`p_3 = 5/36 = 0.1389`$
* $`p_4 = 8/36 = 0.2222`$
* $`p_5 = 4/36 = 0.1111`$

Global Mean $`m_G`$:

```math
m_G = (0 \times 0.25) + (1 \times 0.1667) + (2 \times 0.1111) + (3 \times 0.1389) + (4 \times 0.2222) + (5 \times 0.1111) = 2.2500
```

---

##### Step 2: Evaluate Candidate Thresholds $`k`$

1. **For $`k = 0`$:**
   * $`\omega_0 = 0.2500`$, $`\omega_1 = 0.7500`$
   * $`\mu_0 = 0.0000`$, $`\mu_1 = \frac{2.2500 - 0}{0.7500} = 3.0000`$
   * $`\sigma_B^2(0) = (0.2500)(0.7500)(0.0000 - 3.0000)^2 = 0.1875 \times 9.0 = 1.6875`$

2. **For $`k = 1`$:**
   * $`\omega_0 = 0.2500 + 0.1667 = 0.4167`$, $`\omega_1 = 0.5833`$
   * Cumulative mean $`m(1) = 0 + (1 \times 0.1667) = 0.1667`$
   * $`\mu_0 = 0.1667 / 0.4167 = 0.4000`$
   * $`\mu_1 = \frac{2.2500 - 0.1667}{0.5833} = \frac{2.0833}{0.5833} = 3.5714`$
   * $`\sigma_B^2(1) = (0.4167)(0.5833)(0.4000 - 3.5714)^2 = 0.2431 \times 10.0578 = 2.4446`$

3. **For $`k = 2`$:**
   * $`\omega_0 = 0.4167 + 0.1111 = 0.5278`$, $`\omega_1 = 0.4722`$
   * Cumulative mean $`m(2) = 0.1667 + (2 \times 0.1111) = 0.3889`$
   * $`\mu_0 = 0.3889 / 0.5278 = 0.7368`$
   * $`\mu_1 = \frac{2.2500 - 0.3889}{0.4722} = \frac{1.8611}{0.4722} = 3.9412`$
   * $`\sigma_B^2(2) = (0.5278)(0.4722)(0.7368 - 3.9412)^2 = 0.2492 \times 10.2682 = 2.5590`$

4. **For $`k = 3`$:**
   * $`\omega_0 = 0.5278 + 0.1389 = 0.6667`$, $`\omega_1 = 0.3333`$
   * Cumulative mean $`m(3) = 0.3889 + (3 \times 0.1389) = 0.8056`$
   * $`\mu_0 = 0.8056 / 0.6667 = 1.2083`$
   * $`\mu_1 = \frac{2.2500 - 0.8056}{0.3333} = \frac{1.4444}{0.3333} = 4.3333`$
   * $`\sigma_B^2(3) = (0.6667)(0.3333)(1.2083 - 4.3333)^2 = 0.2222 \times 9.7656 = 2.1701`$

5. **For $`k = 4`$:**
   * $`\omega_0 = 0.6667 + 0.2222 = 0.8889`$, $`\omega_1 = 0.1111`$
   * Cumulative mean $`m(4) = 0.8056 + (4 \times 0.2222) = 1.6944`$
   * $`\mu_0 = 1.6944 / 0.8889 = 1.9063`$
   * $`\mu_1 = 5.0000`$
   * $`\sigma_B^2(4) = (0.8889)(0.1111)(1.9063 - 5.0000)^2 = 0.0988 \times 9.5707 = 0.9453`$

---

##### Step 3: Tabular Summary & Final Decision

| Threshold Candidate ($`k`$) | $`\omega_0(k)`$ | $`\mu_0(k)`$ | $`\omega_1(k)`$ | $`\mu_1(k)`$ | Between-Class Variance ($`\sigma_B^2(k)`$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0.2500 | 0.0000 | 0.7500 | 3.0000 | 1.6875 |
| **1** | 0.4167 | 0.4000 | 0.5833 | 3.5714 | 2.4446 |
| **2** | **0.5278** | **0.7368** | **0.4722** | **3.9412** | **2.5590 (MAXIMUM)** |
| **3** | 0.6667 | 1.2083 | 0.3333 | 4.3333 | 2.1701 |
| **4** | 0.8889 | 1.9063 | 0.1111 | 5.0000 | 0.9453 |

---

#### Final Answer

The maximum between-class variance is $`\sigma_B^2(2) = 2.5590`$.
Therefore, the **Optimal Otsu Threshold is $`T^* = 2`$**.

---

## 6. Solved Numerical Type 5: Region Growing Segmentation

### Solved Problem 5.1: 4-Connected Region Growing

#### Problem Statement

Given the following $`4 \times 4`$ grayscale image matrix $`I`$:

```math
I = \begin{bmatrix}
1 & 1 & 2 & 0 \\
2 & 5 & 6 & 1 \\
1 & 4 & 7 & 3 \\
0 & 2 & 5 & 1
\end{bmatrix}
```

Perform **Region Growing** using **4-connectivity** starting from initial seed pixel $`s = (2,2)`$ (with intensity $`7`$). The region predicate condition for adding an adjacent pixel $`(x,y)`$ to region $`R`$ is:

```math
\lvert f(x,y) - \mu_R \rvert \le 2
```

Where $`\mu_R`$ is the mean intensity of the region (updated dynamically). Show the step-by-step pixel additions and the final segmented binary region mask.

---

#### Step-by-Step Solution

##### Step 1: Initialize Seed Pixel

* Seed pixel $`s = (2,2)`$ with intensity $`f(2,2) = 7`$.
* Region set $`R = \{(2,2)\}`$, region sum $`S = 7`$, mean $`\mu_R = 7.0000`$.

##### Step 2: Iteration 1 — Inspect 4-Neighbors of $`(2,2)`$

4-Neighbors of $`(2,2)`$:
* Top neighbor $`(1,2) = 6`$: $`\lvert 6 - 7.0 \rvert = 1 \le 2 \implies`$ **ACCEPT (1,2)**.
* Bottom neighbor $`(3,2) = 5`$: $`\lvert 5 - 7.0 \rvert = 2 \le 2 \implies`$ **ACCEPT (3,2)**.
* Left neighbor $`(2,1) = 4`$: $`\lvert 4 - 7.0 \rvert = 3 > 2 \implies`$ REJECT.
* Right neighbor $`(2,3) = 3`$: $`\lvert 3 - 7.0 \rvert = 4 > 2 \implies`$ REJECT.

Region $`R = \{(2,2), (1,2), (3,2)\}`$.
Updated mean: $`\mu_R = \frac{7 + 6 + 5}{3} = \frac{18}{3} = 6.0000`$.

##### Step 3: Iteration 2 — Inspect Unvisited 4-Neighbors of Newly Added Pixels

1. **Neighbors of $`(1,2)`$ (value $`6`$):**
   * Top neighbor $`(0,2) = 2`$: $`\lvert 2 - 6.0 \rvert = 4 > 2 \implies`$ REJECT.
   * Left neighbor $`(1,1) = 5`$: $`\lvert 5 - 6.0 \rvert = 1 \le 2 \implies`$ **ACCEPT (1,1)**.
   * Right neighbor $`(1,3) = 1`$: $`\lvert 1 - 6.0 \rvert = 5 > 2 \implies`$ REJECT.

2. **Neighbors of $`(3,2)`$ (value $`5`$):**
   * Left neighbor $`(3,1) = 2`$: $`\lvert 2 - 6.0 \rvert = 4 > 2 \implies`$ REJECT.
   * Right neighbor $`(3,3) = 1`$: $`\lvert 1 - 6.0 \rvert = 5 > 2 \implies`$ REJECT.

Region $`R = \{(2,2), (1,2), (3,2), (1,1)\}`$.
Updated mean: $`\mu_R = \frac{7 + 6 + 5 + 5}{4} = \frac{23}{4} = 5.7500`$.

##### Step 4: Iteration 3 — Check Unvisited Neighbors of $`(1,1)`$ (value $`5`$)

* Top neighbor $`(0,1) = 1`$: $`\lvert 1 - 5.75 \rvert = 4.75 > 2 \implies`$ REJECT.
* Left neighbor $`(1,0) = 2`$: $`\lvert 2 - 5.75 \rvert = 3.75 > 2 \implies`$ REJECT.

No further pixels satisfy the growth criterion. Algorithm terminates!

---

#### Final Answer

* **Segmented Region Pixels:** $`\{(1,1), (1,2), (2,2), (3,2)\}`$
* **Final Segmented Binary Mask ($`1`$ for Region, $`0`$ for Background):**

```math
\text{Segmented Mask} = \begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
```

---

## 7. Solved Numerical Type 6: Region Splitting & Merging (Quadtree)

### Solved Problem 6.1: Quadtree Decomposition and Merging

#### Problem Statement

Perform **Region Splitting and Merging** on the following $`4 \times 4`$ grayscale matrix $`I`$:

```math
I = \begin{bmatrix}
80 & 85 & 78 & 82 \\
83 & 82 & 79 & 84 \\
200 & 195 & 198 & 202 \\
199 & 201 & 197 & 196
\end{bmatrix}
```

Using the homogeneity predicate $`Q(R_i) = \text{TRUE}`$ if $`\left(\max_{(x,y)\in R_i} f(x,y) - \min_{(x,y)\in R_i} f(x,y)\right) \le 10`$.

Show initial quadrant splits, check region homogeneity, draw the Quadtree structure representation, and perform adjacent region merging.

---

#### Step-by-Step Solution

##### Step 1: Check Homogeneity of Entire $`4 \times 4`$ Image $`R`$

* Entire image values: $`\max = 202`$, $`\min = 78`$.
* Range difference: $`202 - 78 = 124 > 10`$.
* $`Q(R) = \text{FALSE}`$. **SPLIT $`R`$ into four $`2 \times 2`$ sub-quadrants ($`R_1, R_2, R_3, R_4`$)**.

---

##### Step 2: Evaluate $`2 \times 2`$ Sub-Quadrants

1. **Quadrant $`R_1`$ (Top-Left, Rows 0–1, Cols 0–1):**

```math
R_1 = \begin{bmatrix}
80 & 85 \\
83 & 82
\end{bmatrix} \implies \max = 85, \min = 80, \text{diff} = 5 \le 10 \implies \text{TRUE}
```

2. **Quadrant $`R_2`$ (Top-Right, Rows 0–1, Cols 2–3):**

```math
R_2 = \begin{bmatrix}
78 & 82 \\
79 & 84
\end{bmatrix} \implies \max = 84, \min = 78, \text{diff} = 6 \le 10 \implies \text{TRUE}
```

3. **Quadrant $`R_3`$ (Bottom-Left, Rows 2–3, Cols 0–1):**

```math
R_3 = \begin{bmatrix}
200 & 195 \\
199 & 201
\end{bmatrix} \implies \max = 201, \min = 195, \text{diff} = 6 \le 10 \implies \text{TRUE}
```

4. **Quadrant $`R_4`$ (Bottom-Right, Rows 2–3, Cols 2–3):**

```math
R_4 = \begin{bmatrix}
198 & 202 \\
197 & 196
\end{bmatrix} \implies \max = 202, \min = 196, \text{diff} = 6 \le 10 \implies \text{TRUE}
```

All four $`2 \times 2`$ sub-quadrants satisfy $`Q(R_i) = \text{TRUE}`$.

---

##### Step 3: Quadtree Tree Structure Representation

```text
Quadtree Hierarchy Representation:

                    Root Node R (4x4)
                         |
       +-----------------+-----------------+-----------------+
       |                 |                 |                 |
    R1 (2x2)          R2 (2x2)          R3 (2x2)          R4 (2x2)
   [Unsplit]         [Unsplit]         [Unsplit]         [Unsplit]
```

---

##### Step 4: Merging Phase

Check adjacent sub-quadrants to merge if $`Q(R_a \cup R_b) = \text{TRUE}`$:

1. **Merge $`R_1`$ and $`R_2`$ (Horizontal Top Neighbors):**
   * Combined values: $`\{80, 85, 83, 82, 78, 82, 79, 84\}`$.
   * $`\max = 85, \min = 78 \implies \text{diff} = 7 \le 10 \implies \text{TRUE}`$.
   * **MERGE $`R_1`$ and $`R_2`$ into Region $`R_{\text{Top}}`$**.

2. **Merge $`R_3`$ and $`R_4`$ (Horizontal Bottom Neighbors):**
   * Combined values: $`\{200, 195, 199, 201, 198, 202, 197, 196\}`$.
   * $`\max = 202, \min = 195 \implies \text{diff} = 7 \le 10 \implies \text{TRUE}`$.
   * **MERGE $`R_3`$ and $`R_4`$ into Region $`R_{\text{Bottom}}`$**.

3. **Check Vertical Merge between $`R_{\text{Top}}`$ and $`R_{\text{Bottom}}`$:**
   * Combined values range: $`\max = 202, \min = 78 \implies \text{diff} = 124 > 10 \implies \text{FALSE}`$.
   * Do not merge vertically.

---

#### Final Answer

The $`4 \times 4`$ matrix is segmented into **two homogeneous regions**:
* **Region $`R_{\text{Top}}`$ (Background/Dark Region):** Composed of $`R_1 \cup R_2`$ (Rows 0–1, Cols 0–3) with intensity values $`78`$ to $`85`$.
* **Region $`R_{\text{Bottom}}`$ (Foreground/Bright Region):** Composed of $`R_3 \cup R_4`$ (Rows 2–3, Cols 0–3) with intensity values $`195`$ to $`202`$.

---

## 8. High-Yield Exam Formulas & Numerical Exam Tips

### High-Yield Formula Summary

| Formula Name | Mathematical Equation | Key Notes for Calculation |
| :--- | :--- | :--- |
| **Euclidean Distance** | $`D_e(p,q) = \sqrt{(x-s)^2 + (y-t)^2}`$ | Continuous straight-line distance; use 4 decimal places rounding. |
| **City-Block Distance** | $`D_4(p,q) = \lvert x-s \rvert + \lvert y-t \rvert`$ | Integer grid distance along 4-connected steps. |
| **Chessboard Distance** | $`D_8(p,q) = \max(\lvert x-s \rvert, \lvert y-t \rvert)`$ | Integer grid distance along 8-connected steps. |
| **Bayes Posterior** | $`P(F \mid z) = \frac{p(z \mid F)P(F)}{p(z \mid F)P(F) + p(z \mid B)P(B)}`$ | Normalize weighted likelihoods by total evidence $`p(z)`$. |
| **Otsu Between-Class Variance** | $`\sigma_B^2(k) = \omega_0(k)\omega_1(k)[\mu_0(k) - \mu_1(k)]^2`$ | Maximize $`\sigma_B^2(k)`$ over candidate thresholds $`k`$. |
| **EM Responsibility** | $`\gamma_{i,k} = \frac{\pi_k \mathcal{N}(x_i \mid \mu_k, \sigma_k^2)}{\sum_j \pi_j \mathcal{N}(x_i \mid \mu_j, \sigma_j^2)}`$ | Sum of responsibilities across components $`k`$ equals $`1.0`$. |

---

### Common Exam Pitfalls & Shortcuts

1. **m-Adjacency Checks:**
   Never assume diagonal pixels can be connected directly under $`m`$-adjacency. Always explicitly calculate the intersection set $`N_4(p) \cap N_4(q)`$ and verify if any pixel in that set belongs to $`V`$. If yes, the diagonal step is forbidden.

2. **Otsu Variance Computation Trick:**
   When calculating Otsu's threshold, use the cumulative mean formula $`m(k) = \sum_{i=0}^k i \cdot p_i`$. Then $`\mu_0(k) = \frac{m(k)}{\omega_0(k)}`$ and $`\mu_1(k) = \frac{m_G - m(k)}{1 - \omega_0(k)}`$. This avoids re-summing from scratch for every threshold candidate!

3. **Quadtree Splitting vs. Merging Order:**
   Always perform **all necessary splits** down to leaf level first until every leaf node satisfies $`Q(R_k) = \text{TRUE}`$. Only then begin the **merging phase** by comparing adjacent sub-quadrants across quadtree boundaries.
