# Unit 6: Image Segmentation — Comprehensive Study Notes & Exam Guide

## 1. Introduction & Mathematical Formulation of Image Segmentation

Image segmentation is a fundamental step in digital image processing and computer vision. Its primary objective is to partition a digital image into its constituent, non-overlapping, homogeneous regions or objects of interest based on specific spatial or spectral characteristics (such as gray-level intensity, color, texture, or motion).

### 1.1 Formal Mathematical Definition

Let $R$ represent the entire spatial domain of an image matrix containing $M \times N$ pixels. Segmentation can be defined as a process that partitions $R$ into $n$ sub-regions or connected components, $R_1, R_2, \dots, R_n$, such that all five of the following fundamental properties are strictly satisfied:

1. **Completeness / Exhaustive Coverage**:
   ```math
   \bigcup_{i=1}^{n} R_i = R
   ```
   Every pixel in the image domain $R$ must belong to at least one segmented region.

2. **Connectivity**:
   $R_i$ is a connected region for $i = 1, 2, \dots, n$.
   All pixels within a specific region $R_i$ must be spatially connected according to a defined connectivity criterion (e.g., 4-connectivity or 8-connectivity).

3. **Disjointness / Non-Overlapping Regions**:
   ```math
   R_i \cap R_j = \emptyset \quad \text{for all } i \neq j
   ```
   The segmented regions are mutually exclusive; no single pixel can belong to more than one region simultaneously.

4. **Homogeneity Predicate**:
   ```math
   P(R_i) = \text{TRUE} \quad \text{for } i = 1, 2, \dots, n
   ```
   All pixels belonging to a given region $R_i$ must satisfy a logical uniformity predicate $P$ (for instance, the intensity variance within $R_i$ is less than a specified threshold $T$).

5. **Maximality / Heterogeneity Across Boundaries**:
   ```math
   P(R_i \cup R_j) = \text{FALSE} \quad \text{for any adjacent regions } R_i \text{ and } R_j
   ```
   Two adjacent regions $R_i$ and $R_j$ cannot be merged into a single region because their union fails to satisfy the homogeneity predicate $P$.

---

### 1.2 Taxonomy of Image Segmentation Approaches

Image segmentation algorithms are fundamentally categorized based on two primary gray-level intensity properties:

| Property Category | Underlying Principle | Core Algorithms |
| :--- | :--- | :--- |
| **Discontinuity-Based (Boundary Approach)** | Partitioning an image based on abrupt local intensity changes (edges, lines, isolated points). | Point Detection, Line Detection, Sobel, Prewitt, Canny Edge Detection, Second-order Zero Crossings. |
| **Similarity-Based (Region Approach)** | Partitioning an image into regions that are homogeneous according to a set of predefined criteria. | Intensity Thresholding (Global, Local, Adaptive), Otsu's Method, Region Growing, Region Splitting and Merging. |
| **Probabilistic & Statistical** | Classifying pixels using statistical distribution modeling and machine learning frameworks. | Bayesian Classification, Expectation-Maximization (EM) Binarization, Gaussian Mixture Models (GMM). |

---

## 2. Pixel Relationships, Connectivity, and Component Labeling

### 2.1 Pixel Neighborhoods

Let $p$ be a pixel at spatial coordinates $(x,y)$. The basic spatial neighborhoods of $p$ are defined as follows:

1. **4-Neighbors of $p$, denoted as $N_4(p)$**:
   The four orthogonal pixels surrounding $p$ at unit distance:
   ```math
   N_4(p) = \{(x+1, y), (x-1, y), (x, y+1), (x, y-1)\}
   ```

2. **Diagonal Neighbors of $p$, denoted as $N_D(p)$**:
   The four diagonal pixels surrounding $p$:
   ```math
   N_D(p) = \{(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)\}
   ```

3. **8-Neighbors of $p$, denoted as $N_8(p)$**:
   The complete set of eight surrounding pixels, combining 4-neighbors and diagonal neighbors:
   ```math
   N_8(p) = N_4(p) \cup N_D(p)
   ```

---

### 2.2 Adjacency and Connectivity Types

Two pixels $p$ and $q$ are considered adjacent if they are spatial neighbors and their gray-level intensity values satisfy a specified set of similarity criteria $V$ (where $V$ is a set of intensity values, e.g., $`V = \{1\}`$ for binary images or $`V = \{128, 129, \dots, 255\}`$ for gray-level ranges).

* **4-Adjacency**: Two pixels $p$ and $q$ with values from set $V$ are 4-adjacent if $q \in N_4(p)$.
* **8-Adjacency**: Two pixels $p$ and $q$ with values from set $V$ are 8-adjacent if $q \in N_8(p)$.
* **m-Adjacency (Mixed Adjacency)**: Two pixels $p$ and $q$ with values from set $V$ are $m$-adjacent if:
  1. $q \in N_4(p)$, **OR**
  2. $q \in N_D(p)$ **AND** the intersection set $N_4(p) \cap N_4(q)$ contains **no** pixels with intensity values belonging to set $V$.

#### Why $m$-Adjacency is Essential

When using 8-adjacency, multiple paths can exist between two pixels, creating closed loops or topological ambiguities (e.g., thick spurious boundaries). Mixed connectivity ($m$-adjacency) explicitly eliminates these ambiguous diagonal paths whenever a direct 4-connected path is already present.

```text
Pixel arrangement (V = {1}), paths from (0,1) to (2,2):

          4-connectivity      8-connectivity      m-connectivity
          (no path)           (2 paths)           (1 unique path)

          0   1---1           0   1---1           0   1---1
              |                   | /                 |
          0   1   0           0   1   0           0   1   0
                                    \                    \
          0   0   1           0   0   1           0   0   1
                  ^                   ^                   ^
            unreachable       ambiguous loop      loop eliminated
```

---

### 2.3 Distance Measures

For pixels $p(x,y)$, $q(s,t)$, and $z(v,w)$:

1. **Euclidean Distance ($D_e$)**:
   ```math
   D_e(p,q) = \sqrt{(x - s)^2 + (y - t)^2}
   ```

2. **City-Block Distance / Manhattan Distance ($D_4$)**:
   ```math
   D_4(p,q) = |x - s| + |y - t|
   ```
   Pixels with $D_4(p,q) \le 1$ form the 4-neighbors of $p$.

3. **Chessboard Distance ($D_8$)**:
   ```math
   D_8(p,q) = \max(|x - s|, |y - t|)
   ```
   Pixels with $D_8(p,q) \le 1$ form the 8-neighbors of $p$.

---

### 2.4 Connected Component Labeling Algorithm

Connected Component Labeling (CCL) scans a binary image row-by-row to group connected foreground pixels into distinct spatial objects and assign each object a unique integer label.

#### Two-Pass Sequential CCL Algorithm (using 4-connectivity)

* **First Pass (Scanning & Equivalence Table Generation)**:
  Scan the binary image row-by-row from top-left to bottom-right. For each foreground pixel $p = (x,y)$ with intensity $1$:
  1. Inspect its previously processed top neighbor $t = (x-1, y)$ and left neighbor $l = (x, y-1)$.
  2. If both $t$ and $l$ have value $0$ (background), assign a new unique label to $p$.
  3. If only one neighbor has a label, copy that label to $p$.
  4. If both $t$ and $l$ have labels:
     * If $L(t) = L(l)$, assign $L(t)$ to $p$.
     * If $L(t) \neq L(l)$, assign $\min(L(t), L(l))$ to $p$ and record the equivalence pair $(L(t) \equiv L(l))$ in the Equivalence Union-Find Table.

* **Second Pass (Label Resolution)**:
  Scan the image a second time. Replace each provisional label $L(p)$ with the minimum root label from its equivalence class in the Equivalence Table.

---

### 2.5 Worked Numerical 1: Adjacency, $m$-Connectivity, and Component Labeling

#### Problem Statement

Consider the following binary image grid where the foreground pixel value set is $`V = \{1\}`$:

```math
I = \begin{bmatrix}
  0 & 1 & 1 \\
  0 & 1 & 0 \\
  0 & 0 & 1
\end{bmatrix}
```

Perform the following calculations:
1. Identify all 4-connected, 8-connected, and $m$-connected paths from pixel $p(0,1)$ to pixel $q(2,2)$.
2. Apply 4-connected and 8-connected component labeling to the $4 \times 4$ binary matrix below and show the resulting label matrices:

```math
B = \begin{bmatrix}
  1 & 1 & 0 & 0 \\
  1 & 1 & 0 & 0 \\
  0 & 0 & 1 & 1 \\
  0 & 0 & 1 & 1
\end{bmatrix}
```

---

#### Step-by-Step Solution

##### Part 1: Connectivity Paths

Coordinate mapping for $I$:
* $p = (0,1)$ with value $1$
* Right neighbor = $(0,2)$ with value $1$
* Down neighbor = $(1,1)$ with value $1$
* Target $q = (2,2)$ with value $1$

1. **4-Connected Paths**:
   From $(0,1)$, 4-neighbors with value $1$ are $(0,2)$ and $(1,1)$.
   From $(1,1)$, 4-neighbors with value $1$ are $(0,1)$. There is **no 4-connected neighbor** to $(2,2)$ because $(2,1)=0$ and $(1,2)=0$.
   Therefore, **No 4-connected path exists between $(0,1)$ and $(2,2)$**.

2. **8-Connected Paths**:
   Diagonal step from $(1,1)$ to $(2,2)$ is valid because $(2,2) \in N_8(1,1)$.
   Path 1: $(0,1) \to (1,1) \to (2,2)$
   Path 2: $(0,1) \to (0,2) \to (1,1) \to (2,2)$
   Since both paths exist, 8-connectivity exhibits path redundancy.

3. **$m$-Connected Paths**:
   Check diagonal transition between $p_1(1,1)$ and $q_1(2,2)$:
   * $q_1(2,2) \in N_D(1,1)$.
   * Calculate intersection $N_4(1,1) \cap N_4(2,2)$:
     $`N_4(1,1) = \{(0,1), (2,1), (1,0), (1,2)\}`$
     $`N_4(2,2) = \{(1,2), (2,1)\}`$
     Intersection $`N_4(1,1) \cap N_4(2,2) = \{(1,2), (2,1)\}`$.
   * Intensity values at $(1,2)$ and $(2,1)$ are both $0 \notin V$.
   * Since the intersection contains no pixels with value $1$, $m$-adjacency condition 2 is satisfied!
   * Therefore, $m$-connected path is unique: **$(0,1) \to (1,1) \to (2,2)$**.

---

##### Part 2: Connected Component Labeling on Matrix $B$

Matrix $B$:
```math
\begin{bmatrix}
  (0,0)=1 & (0,1)=1 & (0,2)=0 & (0,3)=0 \\
  (1,0)=1 & (1,1)=1 & (1,2)=0 & (1,3)=0 \\
  (2,0)=0 & (2,1)=0 & (2,2)=1 & (2,3)=1 \\
  (3,0)=0 & (3,1)=0 & (3,2)=1 & (3,3)=1
\end{bmatrix}
```

1. **4-Connected Component Labeling**:
   * **Pass 1**:
     * Pixel $(0,0)=1 \to$ Assign Label **1**.
     * Pixel $(0,1)=1 \to$ Left neighbor is $1 \to$ Assign Label **1**.
     * Pixel $(1,0)=1 \to$ Top neighbor is $1 \to$ Assign Label **1**.
     * Pixel $(1,1)=1 \to$ Top & Left are $1 \to$ Assign Label **1**.
     * Pixel $(2,2)=1 \to$ Top $(1,2)=0$, Left $(2,1)=0 \to$ Assign Label **2**.
     * Pixel $(2,3)=1 \to$ Left neighbor is $2 \to$ Assign Label **2**.
     * Pixel $(3,2)=1 \to$ Top neighbor is $2 \to$ Assign Label **2**.
     * Pixel $(3,3)=1 \to$ Top & Left are $2 \to$ Assign Label **2**.
   * **Equivalence Table**: None needed (no conflicting labels).
   * **Labeled Matrix (4-Connectivity)**:
     ```math
     L_4 = \begin{bmatrix}
       1 & 1 & 0 & 0 \\
       1 & 1 & 0 & 0 \\
       0 & 0 & 2 & 2 \\
       0 & 0 & 2 & 2
     \end{bmatrix}
     ```
     *(Number of 4-connected components = **2**)*

2. **8-Connected Component Labeling**:
   If we add a diagonal connection between $(1,1)$ and $(2,2)$:
   * Pixel $(2,2)$ has diagonal neighbor $(1,1)$ with Label **1**.
   * Under 8-connectivity, pixel $(2,2)$ connects to Label **1**.
   * **Labeled Matrix (8-Connectivity)**:
     ```math
     L_8 = \begin{bmatrix}
       1 & 1 & 0 & 0 \\
       1 & 1 & 0 & 0 \\
       0 & 0 & 1 & 1 \\
       0 & 0 & 1 & 1
     \end{bmatrix}
     ```
     *(Number of 8-connected components = **1**)*

---

## 3. Thresholding Techniques

Thresholding converts a grayscale image $f(x,y)$ into a binary segmented image $g(x,y)$:

```math
g(x,y) = \begin{cases}
  1 & \text{if } f(x,y) \ge T \\
  0 & \text{if } f(x,y) < T
\end{cases}
```

Where $1$ represents the foreground object and $0$ represents the background.

```text
Global thresholding (single T)

Count
  ^
  |      ___            |             ___
  |     /   \           |            /   \
  |    /     \          |           /     \
  |   /       \         |          /       \
  +---------------------+-------------------------> Gray level (0 to 255)
                        T
      Background                         Foreground
      (Class 0)                         (Class 1)
```

**Local / adaptive thresholding** computes a threshold for each pixel from its neighbourhood, which overcomes non-uniform illumination:

```text
T(x,y) = f_local(x,y) + T_offset
```

---

### 3.1 Global vs. Local / Variable / Adaptive Thresholding

| Parameter | Global Thresholding | Local / Adaptive Thresholding |
| :--- | :--- | :--- |
| **Formulation** | $T = \text{constant}$ across the entire image | $T = T(x,y, f_{local}(x,y))$ varies across spatial coordinates |
| **Computational Complexity** | Very Low ($O(MN)$ histogram pass) | Moderate to High (sliding window local mean/variance) |
| **Sensitivity to Illumination** | Fails under non-uniform illumination or gradients | Robust against uneven lighting and shading gradients |
| **Best Application** | High-contrast images with bimodal histograms | Document scanning, medical images, real-world scenes |

---

### 3.2 Bayesian Classification for Foreground/Background Segmentation

Bayesian Decision Theory provides an optimal probabilistic framework for pixel classification when the underlying statistical probability distributions of foreground ($F$) and background ($B$) intensities are known or estimated.

#### Mathematical Formulation

Let $z$ denote the gray-level intensity of a pixel. Let $C_1 = F$ (Foreground) and $C_2 = B$ (Background).

By Bayes' Theorem, the posterior probability $P(C_i | z)$ that a pixel with intensity $z$ belongs to class $C_i$ is:

```math
P(C_i | z) = \frac{p(z | C_i) P(C_i)}{p(z)}
```

Where:
* $P(C_i)$ is the **prior probability** of class $C_i$, satisfying $P(F) + P(B) = 1$.
* $p(z | C_i)$ is the **class-conditional probability density function (likelihood)**.
* $p(z) = p(z|F)P(F) + p(z|B)P(B)$ is the marginal probability density.

#### Bayes Decision Rule (Minimum Error Classification)

A pixel with intensity $z$ is classified as **Foreground ($F$)** if:

```math
P(F | z) > P(B | z) \implies p(z | F) P(F) > p(z | B) P(B)
```

Dividing both sides yields the **Likelihood Ratio Test**:

```math
\frac{p(z | F)}{p(z | B)} > \frac{P(B)}{P(F)}
```

#### Gaussian Class-Conditional Model

Assuming class-conditional likelihoods follow 1D Gaussian distributions $\mathcal{N}(\mu_i, \sigma_i^2)$:

```math
p(z | C_i) = \frac{1}{\sqrt{2\pi}\sigma_i} \exp\left( -\frac{(z - \mu_i)^2}{2\sigma_i^2} \right)
```

---

### 3.3 Worked Numerical 2: Bayesian Pixel Classification

#### Problem Statement

In an image binarization problem, foreground ($F$) and background ($B$) pixel intensities follow Gaussian distributions with the following parameters:

* **Foreground ($F$)**: Mean $\mu_F = 180$, Standard Deviation $\sigma_F = 20$, Prior $P(F) = 0.4$
* **Background ($B$)**: Mean $\mu_B = 60$, Standard Deviation $\sigma_B = 15$, Prior $P(B) = 0.6$

Given an observed pixel with intensity value $z = 120$:
1. Calculate the likelihoods $p(z|F)$ and $p(z|B)$.
2. Calculate the posterior probabilities $P(F|z)$ and $P(B|z)$.
3. Classify the pixel as Foreground or Background using the Bayes Decision Rule.

---

#### Step-by-Step Solution

##### Step 1: Calculate Class Likelihoods $p(z|F)$ and $p(z|B)$

1. **Foreground Likelihood $p(z=120 | F)$**:
   ```math
   p(z|F) = \frac{1}{\sqrt{2\pi}(20)} \exp\left( -\frac{(120 - 180)^2}{2(20)^2} \right)
   ```
   ```math
   \text{Exponent factor} = -\frac{(-60)^2}{2(400)} = -\frac{3600}{800} = -4.5
   ```
   ```math
   \exp(-4.5) \approx 0.011109
   ```
   ```math
   \frac{1}{\sqrt{2\pi}(20)} = \frac{1}{25.0663 \times 20} = \frac{1}{50.1326} \approx 0.019947
   ```
   ```math
   p(z|F) = 0.019947 \times 0.011109 = \mathbf{2.216 \times 10^{-4}}
   ```

2. **Background Likelihood $p(z=120 | B)$**:
   ```math
   p(z|B) = \frac{1}{\sqrt{2\pi}(15)} \exp\left( -\frac{(120 - 60)^2}{2(15)^2} \right)
   ```
   ```math
   \text{Exponent factor} = -\frac{(60)^2}{2(225)} = -\frac{3600}{450} = -8.0
   ```
   ```math
   \exp(-8.0) \approx 3.3546 \times 10^{-4}
   ```
   ```math
   \frac{1}{\sqrt{2\pi}(15)} = \frac{1}{37.5994} \approx 0.026596
   ```
   ```math
   p(z|B) = 0.026596 \times 3.3546 \times 10^{-4} = \mathbf{8.922 \times 10^{-6}}
   ```

---

##### Step 2: Calculate Weighted Likelihoods & Posterior Probabilities

1. **Weighted Foreground Likelihood**:
   ```math
   p(z|F) P(F) = (2.216 \times 10^{-4}) \times 0.4 = \mathbf{8.864 \times 10^{-5}}
   ```

2. **Weighted Background Likelihood**:
   ```math
   p(z|B) P(B) = (8.922 \times 10^{-6}) \times 0.6 = \mathbf{5.353 \times 10^{-6}}
   ```

3. **Total Evidence $p(z)$**:
   ```math
   p(z) = 8.864 \times 10^{-5} + 5.353 \times 10^{-6} = \mathbf{9.3993 \times 10^{-5}}
   ```

4. **Posterior Probabilities**:
   ```math
   P(F | z=120) = \frac{8.864 \times 10^{-5}}{9.3993 \times 10^{-5}} \approx \mathbf{0.9431 \quad (94.31\%)}
   ```
   ```math
   P(B | z=120) = \frac{5.353 \times 10^{-6}}{9.3993 \times 10^{-5}} \approx \mathbf{0.0569 \quad (5.69\%)}
   ```

---

##### Step 3: Bayes Classification Decision

Since $P(F | z=120) = 0.9431 > P(B | z=120) = 0.0569$, the pixel at $z=120$ is **classified as Foreground ($F$)**.

---

### 3.4 Expectation-Maximization (EM) Algorithm for Image Binarization

When gray-level images contain overlapping background and foreground distributions whose exact parameters $(\mu, \sigma^2, \pi)$ are unknown, the **Expectation-Maximization (EM) algorithm** iteratively computes Maximum Likelihood Estimates (MLE) for Gaussian Mixture Models (GMM).

#### Mathematical Formulation of 2-Class GMM

The marginal probability density of pixel intensity $x_i$ is modeled as:

```math
p(x_i | \Theta) = \pi_b \mathcal{N}(x_i | \mu_b, \sigma_b^2) + \pi_f \mathcal{N}(x_i | \mu_f, \sigma_f^2)
```

Where $\pi_b + \pi_f = 1$ are the mixing coefficients (priors).

#### Algorithmic Workflow

1. **Initialization Step**:
   Choose initial guesses for parameters $`\Theta^{(0)} = \{\mu_b, \sigma_b, \pi_b, \mu_f, \sigma_f, \pi_f\}`$.

2. **E-Step (Expectation)**:
   Calculate the responsibility $\gamma_{i,k}$ (posterior probability that pixel $x_i$ belongs to Gaussian component $`k \in \{b, f\}`$):

   ```math
   \gamma_{i, b} = \frac{\pi_b \mathcal{N}(x_i | \mu_b, \sigma_b^2)}{\pi_b \mathcal{N}(x_i | \mu_b, \sigma_b^2) + \pi_f \mathcal{N}(x_i | \mu_f, \sigma_f^2)}
   ```
   ```math
   \gamma_{i, f} = 1 - \gamma_{i, b}
   ```

3. **M-Step (Maximization)**:
   Update the GMM parameters using calculated responsibilities:

   * **Effective class pixel counts**:
     ```math
     N_b = \sum_{i=1}^{N} \gamma_{i,b}, \quad N_f = \sum_{i=1}^{N} \gamma_{i,f}
     ```

   * **Updated Means**:
     ```math
     \mu_b^{new} = \frac{\sum_{i=1}^N \gamma_{i,b} x_i}{N_b}, \quad \mu_f^{new} = \frac{\sum_{i=1}^N \gamma_{i,f} x_i}{N_f}
     ```

   * **Updated Variances**:
     ```math
     \left(\sigma_b^2\right)^{new} = \frac{\sum_{i=1}^N \gamma_{i,b} (x_i - \mu_b^{new})^2}{N_b}, \quad \left(\sigma_f^2\right)^{new} = \frac{\sum_{i=1}^N \gamma_{i,f} (x_i - \mu_f^{new})^2}{N_f}
     ```

   * **Updated Prior Mixing Coefficients**:
     ```math
     \pi_b^{new} = \frac{N_b}{N}, \quad \pi_f^{new} = \frac{N_f}{N}
     ```

4. **Convergence Check**:
   Repeat E-step and M-step until parameter updates satisfy $|\mu^{(t+1)} - \mu^{(t)}| < \epsilon$. Assign pixel $x_i \to \text{Foreground if } \gamma_{i,f} > \gamma_{i,b}$.

---

### 3.5 Worked Numerical 3: EM Algorithm Iteration

#### Problem Statement

Given a 1D sample pixel array $X = [10, 200]$, initialize a 2-component GMM with parameters:
* Background ($b$): $\mu_b = 15$, $\sigma_b = 5$, $\pi_b = 0.5$
* Foreground ($f$): $\mu_f = 200$, $\sigma_f = 5$, $\pi_f = 0.5$

Perform **one complete iteration (E-step and M-step)** of the EM algorithm to compute the updated parameters $\mu_b^{new}, \mu_f^{new}, \pi_b^{new}, \pi_f^{new}$.

---

#### Step-by-Step Solution

##### Step 1: E-Step (Compute Responsibilities)

Gaussian PDF formula: $\mathcal{N}(x | \mu, \sigma) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)$.
With $\sigma_b = \sigma_f = 5$, $2\sigma^2 = 50$, scaling factor $\frac{1}{\sqrt{2\pi}(5)} \approx 0.07979$.

1. **For Pixel $x_1 = 10$**:
   * Likelihood $\mathcal{N}(10 | 15, 5^2)$:
     ```math
     \text{Exponent} = -\frac{(10-15)^2}{50} = -\frac{25}{50} = -0.5
     ```
     ```math
     \mathcal{N}(10 | 15, 5^2) = 0.07979 \times e^{-0.5} = 0.07979 \times 0.60653 = 0.04839
     ```
   * Likelihood $\mathcal{N}(10 | 200, 5^2)$:
     ```math
     \text{Exponent} = -\frac{(10-200)^2}{50} = -\frac{36100}{50} = -722 \implies \approx 0
     ```
   * Responsibilities:
     ```math
     \gamma_{1,b} = \frac{0.5 \times 0.04839}{0.5 \times 0.04839 + 0} = \mathbf{1.0}, \quad \gamma_{1,f} = \mathbf{0.0}
     ```

2. **For Pixel $x_2 = 200$**:
   * Likelihood $\mathcal{N}(200 | 15, 5^2) \approx 0$.
   * Likelihood $\mathcal{N}(200 | 200, 5^2)$:
     ```math
     \text{Exponent} = -\frac{(200-200)^2}{50} = 0 \implies e^0 = 1.0
     ```
     ```math
     \mathcal{N}(200 | 200, 5^2) = 0.07979 \times 1.0 = 0.07979
     ```
   * Responsibilities:
     ```math
     \gamma_{2,b} = \mathbf{0.0}, \quad \gamma_{2,f} = \mathbf{1.0}
     ```

---

##### Step 2: M-Step (Update Parameters)

1. **Effective Counts**:
   ```math
   N_b = \gamma_{1,b} + \gamma_{2,b} = 1.0 + 0.0 = \mathbf{1.0}
   ```
   ```math
   N_f = \gamma_{1,f} + \gamma_{2,f} = 0.0 + 1.0 = \mathbf{1.0}
   ```

2. **Updated Means**:
   ```math
   \mu_b^{new} = \frac{\gamma_{1,b}(10) + \gamma_{2,b}(200)}{N_b} = \frac{1.0(10) + 0}{1.0} = \mathbf{10.0}
   ```
   ```math
   \mu_f^{new} = \frac{\gamma_{1,f}(10) + \gamma_{2,f}(200)}{N_f} = \frac{0 + 1.0(200)}{1.0} = \mathbf{200.0}
   ```

3. **Updated Mixing Coefficients**:
   ```math
   \pi_b^{new} = \frac{N_b}{N} = \frac{1.0}{2} = \mathbf{0.5}, \quad \pi_f^{new} = \frac{N_f}{N} = \frac{1.0}{2} = \mathbf{0.5}
   ```

---

### 3.6 Otsu's Thresholding Method (Optimal Non-Parametric Binarization)

Otsu's method automatically calculates the optimal global threshold $T^*$ by maximizing the **between-class variance ($\sigma_B^2$)** or equivalently minimizing the **within-class variance ($\sigma_W^2$)** of gray-level histogram classes.

#### Mathematical Derivation

Let an image contain $N$ total pixels with gray levels $`\{0, 1, 2, \dots, L-1\}`$.
Let $n_i$ be the number of pixels at gray level $i$. Normalized histogram probability $p_i = \frac{n_i}{N}$.

When thresholded at level $k$, pixels are partitioned into two classes:
* $C_0$ (Background): Gray levels $[0, k]$
* $C_1$ (Foreground): Gray levels $[k+1, L-1]$

1. **Class Cumulative Probabilities (Weights)**:
   ```math
   \omega_0(k) = \sum_{i=0}^{k} p_i, \quad \omega_1(k) = \sum_{i=k+1}^{L-1} p_i = 1 - \omega_0(k)
   ```

2. **Class Mean Intensity Levels**:
   ```math
   \mu_0(k) = \sum_{i=0}^{k} \frac{i \cdot p_i}{\omega_0(k)} = \frac{m(k)}{\omega_0(k)}
   ```
   ```math
   \mu_1(k) = \sum_{i=k+1}^{L-1} \frac{i \cdot p_i}{\omega_1(k)} = \frac{m_G - m(k)}{1 - \omega_0(k)}
   ```

   Where $m(k) = \sum_{i=0}^k i \cdot p_i$ is the cumulative mean up to level $k$, and $m_G = \sum_{i=0}^{L-1} i \cdot p_i$ is the global mean intensity of the image.

3. **Between-Class Variance ($\sigma_B^2$)**:
   ```math
   \sigma_B^2(k) = \omega_0(k)(\mu_0 - m_G)^2 + \omega_1(k)(\mu_1 - m_G)^2 = \omega_0(k)\omega_1(k)[\mu_0(k) - \mu_1(k)]^2
   ```

   Substituting $\mu_0$ and $\mu_1$ yields the computationally efficient form:
   ```math
   \sigma_B^2(k) = \frac{[m_G \cdot \omega_0(k) - m(k)]^2}{\omega_0(k)(1 - \omega_0(k))}
   ```

4. **Optimal Threshold Selection**:
   ```math
   T^* = \arg\max_{0 \le k < L-1} \sigma_B^2(k)
   ```

---

### 3.7 Worked Numerical 4: Complete Otsu's Thresholding Calculation

#### Problem Statement

An image with $L = 6$ gray levels ($0$ to $5$) and total $N = 36$ pixels has the following histogram count distribution:

| Gray Level ($i$) | 0 | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Pixel Count ($n_i$)** | 9 | 6 | 4 | 5 | 8 | 4 |

Find the optimal Otsu threshold $T^*$ by calculating $\omega_0(k)$, $\mu_0(k)$, $\omega_1(k)$, $\mu_1(k)$, and $\sigma_B^2(k)$ for all possible candidate threshold levels $`k \in \{0, 1, 2, 3, 4\}`$.

---

#### Step-by-Step Solution

##### Step 1: Calculate Normalized Histogram Probabilities ($p_i$) and Global Mean ($m_G$)

Total pixels $N = 36$.
* $p_0 = 9/36 = 0.250$
* $p_1 = 6/36 = 0.1667$
* $p_2 = 4/36 = 0.1111$
* $p_3 = 5/36 = 0.1389$
* $p_4 = 8/36 = 0.2222$
* $p_5 = 4/36 = 0.1111$

**Global Mean ($m_G$)**:
```math
m_G = \sum_{i=0}^{5} i \cdot p_i = (0 \times 0.25) + (1 \times 0.1667) + (2 \times 0.1111) + (3 \times 0.1389) + (4 \times 0.2222) + (5 \times 0.1111)
```
```math
m_G = 0 + 0.1667 + 0.2222 + 0.4167 + 0.8888 + 0.5555 = \mathbf{2.25}
```

---

##### Step 2: Evaluate Between-Class Variance $\sigma_B^2(k) = \omega_0 \omega_1 (\mu_0 - \mu_1)^2$ for each Threshold Candidate $k$

1. **Candidate $k = 0$ (Background: $`\{0\}`$, Foreground: $`\{1, 2, 3, 4, 5\}`$)**:
   * $\omega_0 = p_0 = 0.25$
   * $\omega_1 = 1 - 0.25 = 0.75$
   * $\mu_0 = 0/0.25 = 0.0$
   * $\mu_1 = \frac{m_G - m(0)}{\omega_1} = \frac{2.25 - 0}{0.75} = 3.0$
   * $\sigma_B^2(0) = (0.25) \times (0.75) \times (0.0 - 3.0)^2 = 0.1875 \times 9.0 = \mathbf{1.6875}$

2. **Candidate $k = 1$ (Background: $`\{0, 1\}`$, Foreground: $`\{2, 3, 4, 5\}`$)**:
   * $\omega_0 = p_0 + p_1 = 0.25 + 0.1667 = 0.4167 \approx 0.42$
   * $\omega_1 = 1 - 0.4167 = 0.5833 \approx 0.58$
   * $m(1) = 0 + (1 \times 0.1667) = 0.1667$
   * $\mu_0 = 0.1667 / 0.4167 = 0.40$
   * $\mu_1 = \frac{2.25 - 0.1667}{0.5833} = \frac{2.0833}{0.5833} = 3.571$
   * $\sigma_B^2(1) = (0.4167) \times (0.5833) \times (0.40 - 3.571)^2 = 0.2431 \times (-3.171)^2 = 0.2431 \times 10.055 = \mathbf{2.444}$

3. **Candidate $k = 2$ (Background: $`\{0, 1, 2\}`$, Foreground: $`\{3, 4, 5\}`$)**:
   * $\omega_0 = 0.4167 + p_2 = 0.4167 + 0.1111 = 0.5278 \approx 0.53$
   * $\omega_1 = 1 - 0.5278 = 0.4722 \approx 0.47$
   * $m(2) = 0.1667 + (2 \times 0.1111) = 0.3889$
   * $\mu_0 = 0.3889 / 0.5278 = 0.7368 \approx 0.74$
   * $\mu_1 = \frac{2.25 - 0.3889}{0.4722} = \frac{1.8611}{0.4722} = 3.941$
   * $\sigma_B^2(2) = (0.5278) \times (0.4722) \times (0.7368 - 3.941)^2 = 0.2492 \times (-3.2042)^2 = 0.2492 \times 10.267 = \mathbf{2.558}$

4. **Candidate $k = 3$ (Background: $`\{0, 1, 2, 3\}`$, Foreground: $`\{4, 5\}`$)**:
   * $\omega_0 = 0.5278 + p_3 = 0.5278 + 0.1389 = 0.6667 \approx 0.67$
   * $\omega_1 = 1 - 0.6667 = 0.3333 \approx 0.33$
   * $m(3) = 0.3889 + (3 \times 0.1389) = 0.8056$
   * $\mu_0 = 0.8056 / 0.6667 = 1.208$
   * $\mu_1 = \frac{2.25 - 0.8056}{0.3333} = \frac{1.4444}{0.3333} = 4.333$
   * $\sigma_B^2(3) = (0.6667) \times (0.3333) \times (1.208 - 4.333)^2 = 0.2222 \times (-3.125)^2 = 0.2222 \times 9.7656 = \mathbf{2.170}$

5. **Candidate $k = 4$ (Background: $`\{0, 1, 2, 3, 4\}`$, Foreground: $`\{5\}`$)**:
   * $\omega_0 = 0.6667 + p_4 = 0.6667 + 0.2222 = 0.8889 \approx 0.89$
   * $\omega_1 = 1 - 0.8889 = 0.1111 \approx 0.11$
   * $m(4) = 0.8056 + (4 \times 0.2222) = 1.6944$
   * $\mu_0 = 1.6944 / 0.8889 = 1.906$
   * $\mu_1 = 5.0$
   * $\sigma_B^2(4) = (0.8889) \times (0.1111) \times (1.906 - 5.0)^2 = 0.09875 \times (-3.094)^2 = 0.09875 \times 9.573 = \mathbf{0.945}$

---

##### Step 3: Summary Table & Final Decision

| Threshold Candidate ($k$) | $\omega_0(k)$ | $\mu_0(k)$ | $\omega_1(k)$ | $\mu_1(k)$ | Between-Class Variance ($\sigma_B^2(k)$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0.250 | 0.000 | 0.750 | 3.000 | 1.688 |
| **1** | 0.417 | 0.400 | 0.583 | 3.571 | 2.444 |
| **2** | **0.528** | **0.737** | **0.472** | **3.941** | **2.558 (MAXIMUM)** |
| **3** | 0.667 | 1.208 | 0.333 | 4.333 | 2.170 |
| **4** | 0.889 | 1.906 | 0.111 | 5.000 | 0.945 |

**Conclusion**:
The maximum between-class variance occurs at $k = 2$ ($\sigma_B^2(2) = 2.558$).
Therefore, the **Optimal Otsu Threshold is $T^* = 2$**.
Pixels with intensities $I \le 2$ are classified as Background ($0$), and pixels with $I > 2$ are classified as Foreground ($1$).

---

## 4. Region-Based Segmentation

Region-based segmentation groups pixels directly into uniform spatial regions $R_i$ based on localized similarity rules.

### 4.1 Region Growing Algorithms

Region growing is an approach where pixels are grouped into larger regions starting from a set of initial seed points based on a predefined growth criterion.

#### Algorithmic Workflow

1. **Seed Selection**: Identify one or more initial seed pixels $S_1, S_2, \dots, S_k$ either manually or automatically (e.g., local intensity extrema).
2. **Growth Criterion (Predicate $Q$)**: For each unassigned 4-neighbor or 8-neighbor $p(x,y)$ adjacent to the growing region $R$:
   Check if $|f(x,y) - \mu_R| \le T$ (where $\mu_R$ is the mean intensity of the region, and $T$ is the threshold tolerance).
3. **Iterative Aggregation**: If the condition holds true, append $p(x,y)$ to region $R$ and update $\mu_R$.
4. **Termination**: Stop when no more neighboring pixels satisfy the growth criterion.

---

### 4.2 Region Splitting and Merging (Quadtree Structure Approach)

Instead of starting from seed points, Region Splitting and Merging begins with the entire image region $R$ and recursively subdivides or merges sub-regions to satisfy region homogeneity constraints.

#### Quadtree Decomposition Principle

A Quadtree is a hierarchical tree structure where every non-leaf node has exactly four children, representing a quadrant split of an image region.

```text
Quadtree hierarchical structure:

Root Node (entire image R)
   |
   +-- Quadrant R1 (top-left)
   +-- Quadrant R2 (top-right)
   +-- Quadrant R3 (bottom-left)
   +-- Quadrant R4 (bottom-right)
          |
          +-- Sub-quadrant R41
          +-- Sub-quadrant R42
          +-- Sub-quadrant R43
          +-- Sub-quadrant R44
```

#### Quadtree Splitting and Merging Algorithm

Let $R$ be the entire image domain and $Q$ be a predicate testing homogeneity (e.g., $Q(R_i) = \text{TRUE}$ if $|I_{max} - I_{min}| \le T$).

1. **Splitting Phase**:
   * If $Q(R_i) = \text{FALSE}$ for any region $R_i$, subdivide $R_i$ into four equal quadrant sub-regions: $R_{i1}, R_{i2}, R_{i3}, R_{i4}$.
   * Recursively split any sub-quadrants until $Q(R_k) = \text{TRUE}$ for all leaf regions $R_k$.

2. **Merging Phase**:
   * Compare adjacent sub-regions $R_j$ and $R_k$ (even if they belong to different quadtree parent nodes).
   * If $Q(R_j \cup R_k) = \text{TRUE}$, merge $R_j$ and $R_k$ into a single region.

3. **Termination**:
   Stop when no further splitting or merging operations are possible.

---

### 4.3 Worked Numerical 5: Region Splitting and Merging with Quadtree

#### Problem Statement

Perform Region Splitting and Merging on the following $8 \times 8$ grayscale image matrix $I$ using a homogeneity predicate $Q$:

```math
Q(R_i) = \text{TRUE} \quad \text{if } \left(\max_{(x,y)\in R_i} f(x,y) - \min_{(x,y)\in R_i} f(x,y)\right) \le T
```

Where threshold $T = 3$.

```math
I = \begin{bmatrix}
  5 & 6 & 6 & 6 & 7 & 7 & 6 & 6 \\
  6 & 7 & 6 & 7 & 5 & 5 & 4 & 7 \\
  6 & 6 & 4 & 4 & 3 & 2 & 5 & 6 \\
  5 & 4 & 5 & 4 & 2 & 3 & 4 & 6 \\
  0 & 3 & 2 & 3 & 3 & 2 & 5 & 7 \\
  0 & 0 & 0 & 0 & 2 & 2 & 5 & 6 \\
  1 & 1 & 0 & 1 & 0 & 3 & 4 & 4 \\
  1 & 0 & 1 & 0 & 2 & 3 & 5 & 4
\end{bmatrix}
```

Show all step-by-step splitting decisions, list the resulting sub-regions, draw the hierarchical Quadtree structure representation, and specify final merged regions.

---

#### Step-by-Step Solution

##### Step 1: Initial Quadrant Split (Iteration 1)

Divide the $8 \times 8$ matrix into four $4 \times 4$ quadrants:
* **Quadrant $R_1$ (Top-Left, Rows 0–3, Cols 0–3)**
* **Quadrant $R_2$ (Top-Right, Rows 0–3, Cols 4–7)**
* **Quadrant $R_3$ (Bottom-Left, Rows 4–7, Cols 0–3)**
* **Quadrant $R_4$ (Bottom-Right, Rows 4–7, Cols 4–7)**

Evaluate predicate $Q(R_i)$ for each $4 \times 4$ quadrant:

1. **Quadrant $R_1$**:
   * Values: $`\{5, 6, 7, 4\}`$
   * $\max = 7, \min = 4 \implies |7 - 4| = 3 \le 3$.
   * $Q(R_1) = \text{TRUE}$. **No split required!**

2. **Quadrant $R_2$**:
   * Values: $`\{7, 7, 6, 6, 5, 5, 4, 7, 3, 2, 5, 6, 2, 3, 4, 6\}`$
   * $\max = 7, \min = 2 \implies |7 - 2| = 5 > 3$.
   * $Q(R_2) = \text{FALSE}$. **SPLIT $R_2$ into four $2 \times 2$ sub-quadrants ($R_{21}, R_{22}, R_{23}, R_{24}$)**.

3. **Quadrant $R_3$**:
   * Values: $`\{0, 3, 2, 3, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0\}`$
   * $\max = 3, \min = 0 \implies |3 - 0| = 3 \le 3$.
   * $Q(R_3) = \text{TRUE}$. **No split required!**

4. **Quadrant $R_4$**:
   * Values: $`\{3, 2, 5, 7, 2, 2, 5, 6, 0, 3, 4, 4, 2, 3, 5, 4\}`$
   * $\max = 7, \min = 0 \implies |7 - 0| = 7 > 3$.
   * $Q(R_4) = \text{FALSE}$. **SPLIT $R_4$ into four $2 \times 2$ sub-quadrants ($R_{41}, R_{42}, R_{43}, R_{44}$)**.

---

##### Step 2: Sub-Quadrant Splitting (Iteration 2)

Evaluate $2 \times 2$ sub-regions for $R_2$ and $R_4$:

* **Sub-regions of $R_2$**:
  * $R_{21}$ (Rows 0–1, Cols 4–5): $`\begin{bmatrix} 7 & 7 \\ 5 & 5 \end{bmatrix} \implies \max = 7, \min = 5, |7-5|=2 \le 3 \implies \mathbf{TRUE}`$.
  * $R_{22}$ (Rows 0–1, Cols 6–7): $`\begin{bmatrix} 6 & 6 \\ 4 & 7 \end{bmatrix} \implies \max = 7, \min = 4, |7-4|=3 \le 3 \implies \mathbf{TRUE}`$.
  * $R_{23}$ (Rows 2–3, Cols 4–5): $`\begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix} \implies \max = 3, \min = 2, |3-2|=1 \le 3 \implies \mathbf{TRUE}`$.
  * $R_{24}$ (Rows 2–3, Cols 6–7): $`\begin{bmatrix} 5 & 6 \\ 4 & 6 \end{bmatrix} \implies \max = 6, \min = 4, |6-4|=2 \le 3 \implies \mathbf{TRUE}`$.

* **Sub-regions of $R_4$**:
  * $R_{41}$ (Rows 4–5, Cols 4–5): $`\begin{bmatrix} 3 & 2 \\ 2 & 2 \end{bmatrix} \implies \max = 3, \min = 2, |3-2|=1 \le 3 \implies \mathbf{TRUE}`$.
  * $R_{42}$ (Rows 4–5, Cols 6–7): $`\begin{bmatrix} 5 & 7 \\ 5 & 6 \end{bmatrix} \implies \max = 7, \min = 5, |7-5|=2 \le 3 \implies \mathbf{TRUE}`$.
  * $R_{43}$ (Rows 6–7, Cols 4–5): $`\begin{bmatrix} 0 & 3 \\ 2 & 3 \end{bmatrix} \implies \max = 3, \min = 0, |3-0|=3 \le 3 \implies \mathbf{TRUE}`$.
  * $R_{44}$ (Rows 6–7, Cols 6–7): $`\begin{bmatrix} 4 & 4 \\ 5 & 4 \end{bmatrix} \implies \max = 5, \min = 4, |5-4|=1 \le 3 \implies \mathbf{TRUE}`$.

All sub-quadrants now satisfy $Q(R_k) = \text{TRUE}$.

---

##### Step 3: Quadtree Tree Structure Representation

```text
Quadtree hierarchical structure (8x8 example)

                         Root R (8x8)
                               |
        +-------------+--------+------+-------------+
        |             |               |             |
     R1 (4x4)      R2 (4x4)        R3 (4x4)      R4 (4x4)
     [leaf]        [SPLIT]         [leaf]        [SPLIT]
                      |                             |
              +-----+-+---+-----+            +-----+-+---+-----+
              |     |     |     |            |     |     |     |
             R21   R22   R23   R24          R41   R42   R43   R44
```

---

##### Step 4: Merging Phase

Check adjacent regions to merge if $Q(R_a \cup R_b) = \text{TRUE}$:

1. **Merge $R_1$ with adjacent sub-regions $R_{21}, R_{22}, R_{24}$**:
   * $R_1 \cup R_{21}$: $\max = 7, \min = 4 \implies |7 - 4| = 3 \le 3 \implies \mathbf{MERGE}$.
   * Combined $(R_1 \cup R_{21}) \cup R_{22}$: $\max = 7, \min = 4 \implies |7 - 4| = 3 \le 3 \implies \mathbf{MERGE}$.
   * Combined $(R_1 \cup R_{21} \cup R_{22}) \cup R_{24}$: $\max = 7, \min = 4 \implies |7 - 4| = 3 \le 3 \implies \mathbf{MERGE}$.
   * Add $R_{42}, R_{44}$: $\max = 7, \min = 4 \implies |7 - 4| = 3 \le 3 \implies \mathbf{MERGE}$.

2. **Merge $R_3$ with $R_{23}, R_{41}, R_{43}$**:
   * $R_3 \cup R_{23}$: $\max = 3, \min = 0 \implies |3 - 0| = 3 \le 3 \implies \mathbf{MERGE}$.
   * Combined $(R_3 \cup R_{23}) \cup R_{41} \cup R_{43}$: $\max = 3, \min = 0 \implies |3 - 0| = 3 \le 3 \implies \mathbf{MERGE}$.

---

##### Final Segmented Output Summary

The entire $8 \times 8$ matrix is segmented into **two dominant homogeneous regions**:
* **Region A (Bright / Foreground Object Region)**: Composed of $`\{R_1, R_{21}, R_{22}, R_{24}, R_{42}, R_{44}\}`$ with intensity values ranging between $4$ and $7$.
* **Region B (Dark / Background Region)**: Composed of $`\{R_3, R_{23}, R_{41}, R_{43}\}`$ with intensity values ranging between $0$ and $3$.

---

## 5. Term-End Exam High-Yield Summary & Revision Tables

### 5.1 Comparison of Image Segmentation Thresholding Methods

| Method | Key Optimization Formula / Principle | Input Requirements | Main Advantage | Major Disadvantage |
| :--- | :--- | :--- | :--- | :--- |
| **Global Fixed Thresholding** | $g(x,y) = 1 \text{ if } f(x,y) \ge T$ | Single intensity cut-off value $T$ | Fast ($O(MN)$) | Fails completely under shading/uneven lighting |
| **Otsu's Thresholding** | Maximize $\sigma_B^2(k) = \omega_0 \omega_1 (\mu_0 - \mu_1)^2$ | 1D image gray-level histogram | Fully automatic, non-parametric, optimal for bimodal distributions | Sub-optimal when histogram is not bimodal or object size is tiny |
| **Bayesian Classification** | Maximize $P(C_i \mid z) = \frac{p(z \mid C_i)P(C_i)}{p(z)}$ | Class prior probabilities $P(C_i)$ and probability densities $p(z \mid C_i)$ | Mathematically optimal; minimizes total classification error probability | Requires exact knowledge of class-conditional probability densities |
| **Expectation-Maximization (EM)** | Iteratively compute E-step ($\gamma$) and M-step $(\mu, \sigma^2, \pi)$ | Initial distribution estimates $(\mu^{(0)}, \sigma^{(0)}, \pi^{(0)})$ | Unsupervised parameter estimation for overlapping Mixture Models | Sensitive to initial parameter guesses; iterative convergence can be slow |

---

### 5.2 Comparison of Region-Based Segmentation Techniques

| Feature | Region Growing | Region Splitting and Merging |
| :--- | :--- | :--- |
| **Approach Direction** | Bottom-up (starts from pixel seeds and aggregates outward) | Top-down (starts from entire image domain and subdivides recursively) |
| **Data Structure** | Graph / Neighborhood Adjacency Lists | Hierarchical Quadtree structure |
| **Initial Requirement** | Requires initial seed selection (manual or heuristic) | Requires a region homogeneity predicate $Q(R_i)$ |
| **Computational Issues** | Sensitive to seed selection order and noise points | High memory overhead for quadtree traversal |
| **Boundary Resolution** | Excellent at capturing irregular, fine visual boundaries | Tends to generate blocky boundaries along quadtree division grid lines |

---

### 5.3 High-Yield Exam Formula Cheat Sheet

1. **City-Block Distance**:
   ```math
   D_4(p,q) = |x - s| + |y - t|
   ```

2. **Chessboard Distance**:
   ```math
   D_8(p,q) = \max(|x - s|, |y - t|)
   ```

3. **Bayesian Posterior Probability**:
   ```math
   P(F | z) = \frac{p(z | F) P(F)}{p(z | F) P(F) + p(z | B) P(B)}
   ```

4. **1D Gaussian Probability Density**:
   ```math
   p(z | \mu, \sigma) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(z - \mu)^2}{2\sigma^2} \right)
   ```

5. **Otsu's Between-Class Variance**:
   ```math
   \sigma_B^2(k) = \omega_0(k) \omega_1(k) [\mu_0(k) - \mu_1(k)]^2 = \frac{[m_G \cdot \omega_0(k) - m(k)]^2}{\omega_0(k) (1 - \omega_0(k))}
   ```

6. **EM Algorithm Responsibilities (E-Step)**:
   ```math
   \gamma_{i,k} = \frac{\pi_k \mathcal{N}(x_i | \mu_k, \sigma_k^2)}{\sum_{j} \pi_j \mathcal{N}(x_i | \mu_j, \sigma_j^2)}
   ```

7. **Quadtree Homogeneity Predicate**:
   ```math
   Q(R_i) = \text{TRUE} \quad \text{if } \left(\max_{(x,y)\in R_i} f(x,y) - \min_{(x,y)\in R_i} f(x,y)\right) \le T
   ```
