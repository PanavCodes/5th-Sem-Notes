# Unit 6: Image Segmentation — Past Year Questions (PYQs) & Exam Solutions

---

## 1. Overview of Unit 6 Syllabus and Exam Weightage

Unit 6 covers Image Segmentation, a critical stage in computer vision where an image is partitioned into homogeneous, non-overlapping regions. The topic weightage in Term End Examinations (TEE) and Continuous Assessment (CA) tests spans both theoretical derivations and step-by-step numerical calculations.

* **Course Outcome Mapping:** CO4 — Compare different image segmentation methods, including thresholding, region-based segmentation, and the Otsu method.
* **Core Topics:** Pixel relationships and connectivity ($`4`$-adjacency, $`8`$-adjacency, $`m`$-adjacency), Connected Component Labeling (CCL), intensity thresholding (global, local, adaptive), Bayesian classification, Expectation-Maximization (EM) binarization, Otsu's optimal thresholding method, region growing algorithms, and region splitting and merging using Quadtree structures.

---

## 2. Part 1: Detailed Theory Questions and Answers

### Question 1: Fundamental Definition and Mathematical Axioms of Image Segmentation

#### Exam Context
* **Marks:** 5 Marks / 10 Marks
* **Source Reference:** Course Policy CO4, DIP Chapter 6

#### Question
Define image segmentation. State the five fundamental mathematical conditions that must be satisfied for complete segmentation of an image domain $`R`$. Classify image segmentation algorithms based on intensity properties.

#### Answer

##### 1. Definition
Image segmentation is the process of partitioning a digital image into multiple constituent, non-overlapping, homogeneous regions or sets of pixels that share similar spatial or intensity characteristics (such as gray level, color, or texture).

##### 2. Mathematical Formulation
Let $`R`$ represent the entire spatial domain of an image containing $`M \times N`$ pixels. Segmentation partitions $`R`$ into $`n`$ sub-regions $`R_1, R_2, \dots, R_n`$ such that all of the following five conditions are satisfied:

1. **Completeness / Exhaustive Coverage:**
   ```math
   \bigcup_{i=1}^{n} R_i = R
   ```
   Every pixel in the image domain $`R`$ must belong to at least one segmented region.

2. **Connectivity:**
   $`R_i`$ is a connected region for $`i = 1, 2, \dots, n`$. All pixels within a region $`R_i`$ must be spatially connected according to a defined adjacency criterion ($`4`$-connectivity or $`8`$-connectivity).

3. **Disjointness / Non-Overlapping Regions:**
   ```math
   R_i \cap R_j = \emptyset \quad \text{for all } i \neq j
   ```
   The segmented regions are mutually exclusive; no single pixel can belong to more than one region.

4. **Homogeneity Predicate:**
   ```math
   P(R_i) = \text{TRUE} \quad \text{for } i = 1, 2, \dots, n
   ```
   All pixels within region $`R_i`$ satisfy a logical uniformity predicate $`P`$ (for instance, the intensity variance within $`R_i`$ is less than a specified threshold).

5. **Maximality / Heterogeneity Across Boundaries:**
   ```math
   P(R_i \cup R_j) = \text{FALSE} \quad \text{for any adjacent regions } R_i \text{ and } R_j
   ```
   Two adjacent regions cannot be merged into a single region because their union fails to satisfy the homogeneity predicate $`P`$.

##### 3. Taxonomy of Segmentation Approaches

```text
                       Image Segmentation Taxonomy
                                   |
         +-------------------------+-------------------------+
         |                                                   |
 Discontinuity-Based                                  Similarity-Based
 (Boundary Approach)                                  (Region Approach)
         |                                                   |
 +-------+-------+                           +---------------+---------------+
 |               |                           |               |               |
Edge         Zero-Crossing             Thresholding    Region Growing  Split & Merge
Detection    (Laplacian)               (Global/Otsu)   (Seed-Based)    (Quadtree)
```

---

### Question 2: Pixel Adjacency, Mixed Connectivity, and Component Labeling

#### Exam Context
* **Marks:** 8 Marks / 10 Marks
* **Source Reference:** Final Exam 2025-26 Q6a, Re-Exam 2023-24

#### Question
Explain $`4`$-adjacency, $`8`$-adjacency, and $`m`$-adjacency (mixed adjacency) between pixels. Illustrate why $`m`$-adjacency is necessary to eliminate topological ambiguities. Describe the two-pass Connected Component Labeling (CCL) algorithm.

#### Answer

##### 1. Pixel Neighborhoods and Adjacency
Let $`p`$ be a pixel at spatial coordinates $`(x,y)`$ and $`V`$ be the set of intensity values used to define connectivity (e.g., $`V = \{1\}`$ for binary images).

* **4-Adjacency:** Two pixels $`p`$ and $`q`$ with values from $`V`$ are $`4`$-adjacent if $`q \in N_4(p)`$, where:
  ```math
  N_4(p) = \{(x+1, y), (x-1, y), (x, y+1), (x, y-1)\}
  ```

* **8-Adjacency:** Two pixels $`p`$ and $`q`$ with values from $`V`$ are $`8`$-adjacent if $`q \in N_8(p) = N_4(p) \cup N_D(p)`$, where $`N_D(p)`$ contains the four diagonal neighbors.

* **m-Adjacency (Mixed Adjacency):** Two pixels $`p`$ and $`q`$ with values from $`V`$ are $`m`$-adjacent if:
  1. $`q \in N_4(p)`$, **OR**
  2. $`q \in N_D(p)`$ **AND** the intersection set $`N_4(p) \cap N_4(q)`$ contains **no** pixels with intensity values belonging to set $`V`$.

##### 2. Significance of $`m`$-Adjacency
Under $`8`$-adjacency, diagonal steps permit multiple redundant paths between pixels, creating closed loops or false boundary thickness. Mixed connectivity ($`m`$-adjacency) eliminates ambiguous diagonal paths whenever a direct $`4`$-connected path is present.

```text
Pixel Grid (V = {1}):
0   1   1
0   1   0
0   0   1

8-Connectivity Paths:             m-Connectivity Paths:
0 - 1 - 1                         0 - 1 - 1
    | \ /                             |
0   1   0                         0   1   0
        \                             \
0   0   1                         0   0   1
(Ambiguous closed loop)           (Unique single path)
```

##### 3. Two-Pass Connected Component Labeling (CCL) Algorithm

```text
Pass 1: Scan image row-by-row
        Assign temporary labels
        Record equivalence pairs in Union-Find table
             |
             v
Pass 2: Re-scan image
        Replace temporary labels with root equivalence label
```

* **Pass 1 (Scanning and Equivalence Generation):**
  1. Scan the binary matrix row-by-row from top-left to bottom-right.
  2. For each foreground pixel $`p`$ with intensity $`1`$, inspect its processed neighbors (top neighbor $`t`$ and left neighbor $`l`$).
  3. If both $`t`$ and $`l`$ have value $`0`$, assign a new unique integer label to $`p`$.
  4. If only one neighbor is labeled, copy that label to $`p`$.
  5. If both neighbors are labeled:
     * If $`L(t) = L(l)`$, copy $`L(t)`$ to $`p`$.
     * If $`L(t) \neq L(l)`$, assign $`\min(L(t), L(l))`$ to $`p`$ and record the equivalence pair $`(L(t) \equiv L(l))`$ in an Equivalence Table.

* **Pass 2 (Label Resolution):**
  Scan the matrix a second time and replace every temporary label $`L(p)`$ with the smallest root label from its equivalence class.

---

### Question 3: Global Thresholding vs. Local / Adaptive Thresholding

#### Exam Context
* **Marks:** 8 Marks / 10 Marks
* **Source Reference:** Special Re-Exam 2022-23 Q7b, DIP Chapter 6

#### Question
Explain the thresholding technique for image segmentation. Discuss the major limitations of global thresholding under non-uniform illumination and explain how variable/local thresholding overcomes these limitations.

#### Answer

##### 1. Intensity Thresholding Principle
Thresholding converts a grayscale image $`f(x,y)`$ into a binary segmented output $`g(x,y)`$:

```math
g(x,y) = \begin{cases}
  1 & \text{if } f(x,y) > T \\
  0 & \text{if } f(x,y) \le T
\end{cases}
```

Where $`1`$ represents foreground objects and $`0`$ represents the background.

```text
Histogram-Based Thresholding:

Pixel Count
    ^
    |      Background           Foreground
    |       Class C1             Class C2
    |        /----\               /----\
    |       /      \             /      \
    |      /        \     |     /        \
    +-----+----------+----+----+----------+----> Gray Level Intensity
                          ^
                     Threshold T
```

##### 2. Limitations of Global Thresholding
* **Single Cut-off Value:** Global thresholding assumes $`T`$ is constant across the entire image matrix.
* **Failure Under Shading / Gradients:** When an image suffers from non-uniform illumination, uneven background reflections, or shadow gradients, foreground pixel intensities in dark regions fall below $`T`$, while background pixel intensities in brightly lit regions exceed $`T`$. This causes massive false-positive and false-negative segmentation errors.

##### 3. Local / Variable / Adaptive Thresholding Solution
Variable thresholding partitions the image domain into non-overlapping spatial neighborhoods $`A(x,y)`$ or evaluates a moving window where threshold $`T(x,y)`$ varies dynamically:

```math
T(x,y) = f_{\text{local}}(x,y) + T_{\text{offset}}
```

Where $`f_{\text{local}}(x,y)`$ is the local mean or median intensity within a local $`N \times N`$ window.

##### 4. Comparative Summary Table

| Feature | Global Fixed Thresholding | Local / Adaptive Thresholding |
| :--- | :--- | :--- |
| **Formula** | $`T = \text{constant}`$ | $`T = T(x, y, f_{\text{local}}(x,y))`$ |
| **Computational Overhead** | Very Low ($`O(MN)`$ single pass) | Moderate to High (sliding window local statistics) |
| **Illumination Robustness** | Fails under shading gradients | Highly robust against non-uniform lighting |
| **Best Application** | Controlled lighting, high contrast | Document scanning, medical imaging, real-world scenes |

---

### Question 4: Bayesian Classification and Expectation-Maximization (EM) Binarization

#### Exam Context
* **Marks:** 8 Marks / 10 Marks
* **Source Reference:** Course Policy CO4, PowerPoint Lecture "Bayesian_classification_of_foreground..."

#### Question
Derive the Bayes decision rule for minimum error binarization of an image. Explain how the Expectation-Maximization (EM) algorithm estimates parameters of a Gaussian Mixture Model (GMM) for unsupervised image thresholding.

#### Answer

##### 1. Bayesian Decision Theory Formulation
Let $`z`$ be the gray-level intensity of a pixel. Let $`C_1 = F`$ (Foreground) and $`C_2 = B`$ (Background). By Bayes' Theorem, the posterior probability $`P(C_i \mid z)`$ that a pixel with intensity $`z`$ belongs to class $`C_i`$ is:

```math
P(C_i \mid z) = \frac{p(z \mid C_i) P(C_i)}{p(z)}
```

Where:
* $`P(C_i)`$ is the prior probability of class $`C_i`$, satisfying $`P(F) + P(B) = 1`$.
* $`p(z \mid C_i)`$ is the class-conditional probability density function (likelihood).
* $`p(z) = p(z \mid F) P(F) + p(z \mid B) P(B)`$ is the total evidence probability density.

##### 2. Bayes Decision Rule (Minimum Error Classification)
A pixel with intensity $`z`$ is classified as **Foreground ($`F`$)** if:

```math
P(F \mid z) > P(B \mid z) \implies p(z \mid F) P(F) > p(z \mid B) P(B)
```

Dividing both sides gives the **Likelihood Ratio Test**:

```math
\frac{p(z \mid F)}{p(z \mid B)} > \frac{P(B)}{P(F)}
```

Assuming 1D Gaussian distributions $`\mathcal{N}(\mu_i, \sigma_i^2)`$:

```math
p(z \mid C_i) = \frac{1}{\sqrt{2\pi}\sigma_i} \exp\left( -\frac{(z - \mu_i)^2}{2\sigma_i^2} \right)
```

##### 3. Expectation-Maximization (EM) Algorithm for GMM Binarization
When class parameters $`\Theta = \{\mu_b, \sigma_b^2, \pi_b, \mu_f, \sigma_f^2, \pi_f\}`$ are unknown, the EM algorithm computes Maximum Likelihood Estimates (MLE) through two iterative steps:

1. **E-Step (Expectation):** Calculate the responsibility $`\gamma_{i,k}`$ (posterior probability that pixel $`x_i`$ belongs to Gaussian component $`k \in \{b, f\}`$):
   ```math
   \gamma_{i, b} = \frac{\pi_b \mathcal{N}(x_i \mid \mu_b, \sigma_b^2)}{\pi_b \mathcal{N}(x_i \mid \mu_b, \sigma_b^2) + \pi_f \mathcal{N}(x_i \mid \mu_f, \sigma_f^2)}
   ```
   ```math
   \gamma_{i, f} = 1 - \gamma_{i, b}
   ```

2. **M-Step (Maximization):** Update GMM parameters using calculated responsibilities:
   * **Effective Pixel Counts:** $`N_b = \sum_{i=1}^{N} \gamma_{i,b}`$, $`N_f = \sum_{i=1}^{N} \gamma_{i,f}`$
   * **Updated Means:**
     ```math
     \mu_b^{\text{new}} = \frac{\sum_{i=1}^N \gamma_{i,b} x_i}{N_b}, \quad \mu_f^{\text{new}} = \frac{\sum_{i=1}^N \gamma_{i,f} x_i}{N_f}
     ```
   * **Updated Variances:**
     ```math
     (\sigma_b^2)^{\text{new}} = \frac{\sum_{i=1}^N \gamma_{i,b} (x_i - \mu_b^{\text{new}})^2}{N_b}, \quad (\sigma_f^2)^{\text{new}} = \frac{\sum_{i=1}^N \gamma_{i,f} (x_i - \mu_f^{\text{new}})^2}{N_f}
     ```
   * **Updated Priors:** $`\pi_b^{\text{new}} = \frac{N_b}{N}`$, $`\pi_f^{\text{new}} = \frac{N_f}{N}`$

---

### Question 5: Region Growing vs. Region Splitting and Merging (Quadtree Approach)

#### Exam Context
* **Marks:** 8 Marks / 10 Marks
* **Source Reference:** Special Re-Exam 2022-23 Q3a, Final Exam 2025-26 Q6b

#### Question
Compare region growing and region splitting/merging techniques. Explain Quadtree spatial representation and detail the steps for Quadtree-based image decomposition.

#### Answer

##### 1. Region Growing Algorithm
Region growing is a bottom-up approach that starts with a set of seed pixels $`S_1, S_2, \dots, S_k`$ and iteratively appends unassigned adjacent neighbors if they satisfy a growth predicate $`Q`$:

```math
Q(p, \mu_R) = \text{TRUE} \quad \text{if } \lvert f(p) - \mu_R \rvert \le T
```

Where $`\mu_R`$ is the mean intensity of the growing region and $`T`$ is the threshold tolerance.

##### 2. Region Splitting and Merging (Top-Down Quadtree Approach)
Region splitting and merging begins with the entire image domain $`R`$ and recursively subdivides or merges sub-regions based on a region homogeneity predicate $`Q(R_i)`$.

```text
Quadtree Hierarchical Subdivision:

                   Root Node R (Full Image Domain)
                                |
         +----------------------+----------------------+
         |                      |                      |
    Quadrant R1            Quadrant R2            Quadrant R3
    (Top-Left)             (Top-Right)            (Bottom-Left)
                                |
                   +------------+------------+
                   |            |            |
                  R21          R22          R23
```

##### 3. Quadtree Decomposition Workflow
1. **Splitting Step:** If $`Q(R_i) = \text{FALSE}`$ for any region $`R_i`$, split $`R_i`$ into four equal quadrants: $`R_{i1}, R_{i2}, R_{i3}, R_{i4}`$. Repeat recursively until $`Q(R_k) = \text{TRUE}`$ for all leaf nodes.
2. **Merging Step:** Compare adjacent regions $`R_j`$ and $`R_k`$ across Quadtree boundaries. If $`Q(R_j \cup R_k) = \text{TRUE}`$, merge them into a single continuous region.
3. **Termination:** Stop when no further splitting or merging operations satisfy $`Q`$.

---

## 3. Part 2: Step-by-Step Worked Numerical Problems

### Question 6: Otsu's Optimal Thresholding Calculation (4 Gray Levels)

#### Exam Paper Reference
* **Source:** Final Examination (2025-26) / QP 702EX0E004 Q5b

#### Problem Statement
An image has 4 gray levels: 0, 1, 2, 3. The number of pixels corresponding to each gray level is given below:

| Gray Level ($r$) | 0 | 1 | 2 | 3 |
| :--- | :---: | :---: | :---: | :---: |
| **No. of Pixels ($n$)** | 4 | 5 | 3 | 2 |

Find the optimal Otsu threshold $`T^*`$ by evaluating between-class variance $`\sigma_B^2`$ for threshold values $`T = 1`$ and $`T = 2`$ only.

#### Step-by-Step Solution

##### Step 1: Calculate Total Pixels ($N$), Normalized Probabilities ($p_i$), and Global Mean ($m_G$)

* Total pixels $`N = 4 + 5 + 3 + 2 = 14`$.
* Probability $`p_0 = \frac{4}{14} = 0.285714 \approx 0.2857`$
* Probability $`p_1 = \frac{5}{14} = 0.357143 \approx 0.3571`$
* Probability $`p_2 = \frac{3}{14} = 0.214286 \approx 0.2143`$
* Probability $`p_3 = \frac{2}{14} = 0.142857 \approx 0.1429`$

Calculate the Global Mean Intensity ($`m_G`$):
```math
m_G = \sum_{i=0}^{3} i \cdot p_i = (0 \times 0.285714) + (1 \times 0.357143) + (2 \times 0.214286) + (3 \times 0.142857)
```
```math
m_G = 0 + 0.357143 + 0.428571 + 0.428571 = 1.214286 \approx 1.2143
```

##### Step 2: Evaluate Between-Class Variance for Candidate Threshold $T = 1$

Threshold $`T = 1`$ partitions gray levels into Background $`C_0 = \{0, 1\}`$ and Foreground $`C_1 = \{2, 3\}`$.

1. **Background Weight ($`\omega_0`$):**
   ```math
   \omega_0(1) = p_0 + p_1 = \frac{4}{14} + \frac{5}{14} = \frac{9}{14} = 0.642857 \approx 0.6429
   ```

2. **Foreground Weight ($`\omega_1`$):**
   ```math
   \omega_1(1) = 1 - \omega_0(1) = 1 - \frac{9}{14} = \frac{5}{14} = 0.357143 \approx 0.3571
   ```

3. **Background Mean ($`\mu_0`$):**
   ```math
   \mu_0(1) = \frac{\sum_{i=0}^{1} i \cdot p_i}{\omega_0(1)} = \frac{0(4/14) + 1(5/14)}{9/14} = \frac{5/14}{9/14} = \frac{5}{9} = 0.555556 \approx 0.5556
   ```

4. **Foreground Mean ($`\mu_1`$):**
   ```math
   \mu_1(1) = \frac{\sum_{i=2}^{3} i \cdot p_i}{\omega_1(1)} = \frac{2(3/14) + 3(2/14)}{5/14} = \frac{6/14 + 6/14}{5/14} = \frac{12}{5} = 2.400000 \approx 2.4000
   ```

5. **Between-Class Variance ($`\sigma_B^2(1)`$):**
   ```math
   \sigma_B^2(1) = \omega_0(1) \cdot \omega_1(1) \cdot [\mu_0(1) - \mu_1(1)]^2
   ```
   ```math
   \sigma_B^2(1) = (0.642857) \times (0.357143) \times (0.555556 - 2.400000)^2
   ```
   ```math
   \sigma_B^2(1) = 0.229592 \times (-1.844444)^2 = 0.229592 \times 3.401975 = 0.781066 \approx 0.7811
   ```

##### Step 3: Evaluate Between-Class Variance for Candidate Threshold $T = 2$

Threshold $`T = 2`$ partitions gray levels into Background $`C_0 = \{0, 1, 2\}`$ and Foreground $`C_1 = \{3\}`$.

1. **Background Weight ($`\omega_0`$):**
   ```math
   \omega_0(2) = p_0 + p_1 + p_2 = \frac{4}{14} + \frac{5}{14} + \frac{3}{14} = \frac{12}{14} = 0.857143 \approx 0.8571
   ```

2. **Foreground Weight ($`\omega_1`$):**
   ```math
   \omega_1(2) = 1 - \omega_0(2) = 1 - \frac{12}{14} = \frac{2}{14} = 0.142857 \approx 0.1429
   ```

3. **Background Mean ($`\mu_0`$):**
   ```math
   \mu_0(2) = \frac{\sum_{i=0}^{2} i \cdot p_i}{\omega_0(2)} = \frac{0(4/14) + 1(5/14) + 2(3/14)}{12/14} = \frac{11/14}{12/14} = \frac{11}{12} = 0.916667 \approx 0.9167
   ```

4. **Foreground Mean ($`\mu_1`$):**
   ```math
   \mu_1(2) = \frac{3(2/14)}{2/14} = 3.000000 \approx 3.0000
   ```

5. **Between-Class Variance ($`\sigma_B^2(2)`$):**
   ```math
   \sigma_B^2(2) = \omega_0(2) \cdot \omega_1(2) \cdot [\mu_0(2) - \mu_1(2)]^2
   ```
   ```math
   \sigma_B^2(2) = (0.857143) \times (0.142857) \times (0.916667 - 3.000000)^2
   ```
   ```math
   \sigma_B^2(2) = 0.122449 \times (-2.083333)^2 = 0.122449 \times 4.340278 = 0.531463 \approx 0.5315
   ```

##### Step 4: Summary Table and Final Decision

| Threshold Candidate ($T$) | Background Weight ($`\omega_0`$) | Foreground Weight ($`\omega_1`$) | Background Mean ($`\mu_0`$) | Foreground Mean ($`\mu_1`$) | Between-Class Variance ($`\sigma_B^2`$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **0.6429** | **0.3571** | **0.5556** | **2.4000** | **0.7811 (MAXIMUM)** |
| **2** | 0.8571 | 0.1429 | 0.9167 | 3.0000 | 0.5315 |

**Final Answer:**
The maximum between-class variance occurs at threshold $`T = 1`$ ($`\sigma_B^2(1) = 0.7811`$). Therefore, the optimal Otsu threshold is **Threshold** $`T^* = 1`$ (rounded to 4 decimal places).

---

### Question 7: Otsu's Optimal Thresholding Calculation (6 Gray Levels, 6x6 Image)

#### Exam Paper Reference
* **Source:** Re-Exam / Final Examination Batch 2024-25 Q5b / IVP M2 Notes

#### Problem Statement
Consider a $`6 \times 6`$ grayscale image containing 6 gray levels ($`0, 1, 2, 3, 4, 5`$) with the following histogram counts:

| Gray Level ($i$) | 0 | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Pixel Count ($n_i$)** | 9 | 6 | 4 | 5 | 8 | 4 |

Evaluate between-class variance $`\sigma_B^2(k)`$ for candidate threshold values $`k = 2, 3, 4`$ and find the optimal Otsu threshold $`T^*`$.

#### Step-by-Step Solution

##### Step 1: Calculate Probability Distribution and Global Mean ($m_G$)

Total pixels $`N = 9 + 6 + 4 + 5 + 8 + 4 = 36`$.

* $`p_0 = \frac{9}{36} = 0.250000 \approx 0.2500`$
* $`p_1 = \frac{6}{36} = 0.166667 \approx 0.1667`$
* $`p_2 = \frac{4}{36} = 0.111111 \approx 0.1111`$
* $`p_3 = \frac{5}{36} = 0.138889 \approx 0.1389`$
* $`p_4 = \frac{8}{36} = 0.222222 \approx 0.2222`$
* $`p_5 = \frac{4}{36} = 0.111111 \approx 0.1111`$

Global Mean ($`m_G`$):
```math
m_G = \sum_{i=0}^{5} i \cdot p_i = (0 \times 0.25) + (1 \times 0.166667) + (2 \times 0.111111) + (3 \times 0.138889) + (4 \times 0.222222) + (5 \times 0.111111)
```
```math
m_G = 0 + 0.166667 + 0.222222 + 0.416667 + 0.888889 + 0.555556 = 2.250000 \approx 2.2500
```

##### Step 2: Candidate Threshold $k = 2$ (Background $`\{0,1,2\}`$, Foreground $`\{3,4,5\}`$)

1. **Weights:**
   ```math
   \omega_0(2) = p_0 + p_1 + p_2 = \frac{9+6+4}{36} = \frac{19}{36} = 0.527778 \approx 0.5278
   ```
   ```math
   \omega_1(2) = 1 - \omega_0(2) = \frac{17}{36} = 0.472222 \approx 0.4722
   ```

2. **Means:**
   ```math
   \mu_0(2) = \frac{0(9) + 1(6) + 2(4)}{19} = \frac{14}{19} = 0.736842 \approx 0.7368
   ```
   ```math
   \mu_1(2) = \frac{3(5) + 4(8) + 5(4)}{17} = \frac{15 + 32 + 20}{17} = \frac{67}{17} = 3.941176 \approx 3.9412
   ```

3. **Between-Class Variance:**
   ```math
   \sigma_B^2(2) = (0.527778) \times (0.472222) \times (0.736842 - 3.941176)^2
   ```
   ```math
   \sigma_B^2(2) = 0.249228 \times (-3.204334)^2 = 0.249228 \times 10.267756 = 2.559017 \approx 2.5590
   ```

##### Step 3: Candidate Threshold $k = 3$ (Background $`\{0,1,2,3\}`$, Foreground $`\{4,5\}`$)

1. **Weights:**
   ```math
   \omega_0(3) = \frac{19+5}{36} = \frac{24}{36} = 0.666667 \approx 0.6667
   ```
   ```math
   \omega_1(3) = \frac{12}{36} = 0.333333 \approx 0.3333
   ```

2. **Means:**
   ```math
   \mu_0(3) = \frac{14 + 3(5)}{24} = \frac{29}{24} = 1.208333 \approx 1.2083
   ```
   ```math
   \mu_1(3) = \frac{4(8) + 5(4)}{12} = \frac{52}{12} = 4.333333 \approx 4.3333
   ```

3. **Between-Class Variance:**
   ```math
   \sigma_B^2(3) = (0.666667) \times (0.333333) \times (1.208333 - 4.333333)^2
   ```
   ```math
   \sigma_B^2(3) = 0.222222 \times (-3.125000)^2 = 0.222222 \times 9.765625 = 2.170139 \approx 2.1701
   ```

##### Step 4: Candidate Threshold $k = 4$ (Background $`\{0,1,2,3,4\}`$, Foreground $`\{5\}`$)

1. **Weights:**
   ```math
   \omega_0(4) = \frac{24+8}{36} = \frac{32}{36} = 0.888889 \approx 0.8889
   ```
   ```math
   \omega_1(4) = \frac{4}{36} = 0.111111 \approx 0.1111
   ```

2. **Means:**
   ```math
   \mu_0(4) = \frac{29 + 4(8)}{32} = \frac{61}{32} = 1.906250 \approx 1.9063
   ```
   ```math
   \mu_1(4) = 5.000000 \approx 5.0000
   ```

3. **Between-Class Variance:**
   ```math
   \sigma_B^2(4) = (0.888889) \times (0.111111) \times (1.906250 - 5.000000)^2
   ```
   ```math
   \sigma_B^2(4) = 0.098765 \times (-3.093750)^2 = 0.098765 \times 9.571289 = 0.945313 \approx 0.9453
   ```

##### Step 5: Summary Table and Final Decision

| Threshold Candidate ($k$) | Background Weight ($`\omega_0`$) | Foreground Weight ($`\omega_1`$) | Background Mean ($`\mu_0`$) | Foreground Mean ($`\mu_1`$) | Between-Class Variance ($`\sigma_B^2`$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2** | **0.5278** | **0.4722** | **0.7368** | **3.9412** | **2.5590 (MAXIMUM)** |
| **3** | 0.6667 | 0.3333 | 1.2083 | 4.3333 | 2.1701 |
| **4** | 0.8889 | 0.1111 | 1.9063 | 5.0000 | 0.9453 |

**Final Answer:**
The maximum between-class variance occurs at threshold $`k = 2`$ ($`\sigma_B^2(2) = 2.5590`$). Therefore, the optimal Otsu threshold is **Threshold** $`T^* = 2`$ (rounded to 4 decimal places).

---

### Question 8: Quadtree Region Splitting and Merging Numerical (4x4 Matrix)

#### Exam Paper Reference
* **Source:** Final Examination (2025-26) Q6b / AY 2022-23

#### Problem Statement
Perform region splitting and merging on the following $`4 \times 4`$ grayscale image matrix $`I`$ using a homogeneity predicate $`Q`$:

```math
Q(R_i) = \text{TRUE} \quad \text{if } (\max_{R_i} - \min_{R_i}) \le T
```

Where threshold $`T = 10`$.

```math
I = \begin{bmatrix}
  80 & 85 & 78 & 82 \\
  83 & 82 & 79 & 84 \\
  200 & 195 & 198 & 202 \\
  199 & 201 & 197 & 196
\end{bmatrix}
```

Show all splitting decisions, represent the Quadtree structure, and specify the final merged region map.

#### Step-by-Step Solution

##### Step 1: Initial Region Test and Quadrant Split (Iteration 1)

Evaluate predicate $`Q(R)`$ for the entire $`4 \times 4`$ matrix $`R`$:
* $`\max = 202`$, $`\min = 78`$.
* Range $`= 202 - 78 = 124 > 10`$.
* Predicate $`Q(R) = \text{FALSE}`$. **SPLIT $`R`$ into four $`2 \times 2`$ sub-quadrants ($`R_1, R_2, R_3, R_4`$)**.

##### Step 2: Evaluate Sub-Quadrant Homogeneity (Iteration 2)

1. **Quadrant $`R_1`$ (Top-Left, Rows 0–1, Cols 0–1):**
   ```math
   R_1 = \begin{bmatrix}
     80 & 85 \\
     83 & 82
   \end{bmatrix}
   ```
   * $`\max = 85`$, $`\min = 80 \implies 85 - 80 = 5 \le 10`$.
   * $`Q(R_1) = \text{TRUE}`$. **Unsplit**.

2. **Quadrant $`R_2`$ (Top-Right, Rows 0–1, Cols 2–3):**
   ```math
   R_2 = \begin{bmatrix}
     78 & 82 \\
     79 & 84
   \end{bmatrix}
   ```
   * $`\max = 84`$, $`\min = 78 \implies 84 - 78 = 6 \le 10`$.
   * $`Q(R_2) = \text{TRUE}`$. **Unsplit**.

3. **Quadrant $`R_3`$ (Bottom-Left, Rows 2–3, Cols 0–1):**
   ```math
   R_3 = \begin{bmatrix}
     200 & 195 \\
     199 & 201
   \end{bmatrix}
   ```
   * $`\max = 201`$, $`\min = 195 \implies 201 - 195 = 6 \le 10`$.
   * $`Q(R_3) = \text{TRUE}`$. **Unsplit**.

4. **Quadrant $`R_4`$ (Bottom-Right, Rows 2–3, Cols 2–3):**
   ```math
   R_4 = \begin{bmatrix}
     198 & 202 \\
     197 & 196
   \end{bmatrix}
   ```
   * $`\max = 202`$, $`\min = 196 \implies 202 - 196 = 6 \le 10`$.
   * $`Q(R_4) = \text{TRUE}`$. **Unsplit**.

##### Step 3: Quadtree Tree Data Structure Representation

```text
                     Root Node R (4x4 Matrix)
                                |
         +----------------------+----------------------+
         |                      |                      |
      R1 (2x2)               R2 (2x2)               R3 (2x2)               R4 (2x2)
     [Unsplit]              [Unsplit]              [Unsplit]              [Unsplit]
```

##### Step 4: Merging Phase

Check adjacent regions to evaluate if $`Q(R_a \cup R_b) = \text{TRUE}`$:

1. **Merge $`R_1`$ and $`R_2`$ (Horizontal Top Neighbors):**
   * Combined values: $`\{80, 85, 83, 82, 78, 82, 79, 84\}`$.
   * $`\max = 85`$, $`\min = 78 \implies 85 - 78 = 7 \le 10`$.
   * $`Q(R_1 \cup R_2) = \text{TRUE}`$. **MERGE into Region** $`R_{\text{Top}}`$.

2. **Merge $`R_3`$ and $`R_4`$ (Horizontal Bottom Neighbors):**
   * Combined values: $`\{200, 195, 199, 201, 198, 202, 197, 196\}`$.
   * $`\max = 202`$, $`\min = 195 \implies 202 - 195 = 7 \le 10`$.
   * $`Q(R_3 \cup R_4) = \text{TRUE}`$. **MERGE into Region** $`R_{\text{Bottom}}`$.

3. **Check Vertical Merge between $`R_{\text{Top}}`$ and $`R_{\text{Bottom}}`$:**
   * $`\max = 202`$, $`\min = 78 \implies 202 - 78 = 124 > 10`$.
   * Cannot merge.

**Final Answer:**
The image is segmented into **2 final merged regions**:
1. **Top Region ($`R_{\text{Top}}`$):** Rows 0–1, Cols 0–3 (Background region with mean intensity $`81.6250`$).
2. **Bottom Region ($`R_{\text{Bottom}}`$):** Rows 2–3, Cols 0–3 (Foreground region with mean intensity $`198.6250`$).

---

### Question 9: Pixel Connectivity Paths and Distance Measures (3x3 Matrix)

#### Exam Paper Reference
* **Source:** Final Examination (2025-26) Q6a / AY 2022-23

#### Problem Statement
Consider the following $`3 \times 3`$ image segment:

```math
I = \begin{bmatrix}
  0 & 1 & 2 \\
  2 & 3 & 2 \\
  1 & 1 & 3
\end{bmatrix}
```

Let $`p = (2,0)`$ (bottom-left pixel with value $`1`$) and $`q = (0,2)`$ (top-right pixel with value $`2`$).
For the intensity connectivity set $`V = \{1, 2\}`$, compute:
1. Euclidean distance $`D_e(p,q)`$
2. City-block distance $`D_4(p,q)`$
3. Chessboard distance $`D_8(p,q)`$
4. Mixed-connectivity distance $`D_m(p,q)`$

#### Step-by-Step Solution

##### Step 1: Identify Coordinates and Direct Spatial Distances
* Pixel $`p = (x_1, y_1) = (2,0)`$ with intensity $`1 \in V`$.
* Pixel $`q = (x_2, y_2) = (0,2)`$ with intensity $`2 \in V`$.

1. **Euclidean Distance ($`D_e`$):**
   ```math
   D_e(p,q) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} = \sqrt{(2 - 0)^2 + (0 - 2)^2} = \sqrt{4 + 4} = \sqrt{8} \approx 2.8284
   ```

2. **City-Block Distance ($`D_4`$):**
   ```math
   D_4(p,q) = \lvert x_1 - x_2 \rvert + \lvert y_1 - y_2 \rvert = \lvert 2 - 0 \rvert + \lvert 0 - 2 \rvert = 2 + 2 = 4.0000
   ```

3. **Chessboard Distance ($`D_8`$):**
   ```math
   D_8(p,q) = \max(\lvert x_1 - x_2 \rvert, \lvert y_1 - y_2 \rvert) = \max(2, 2) = 2.0000
   ```

##### Step 2: Determine $`m`$-Connectivity Path ($`D_m`$)
Trace valid steps from $`p(2,0)`$ to $`q(0,2)`$ using values in $`V = \{1, 2\}`$:

```text
Path Tracing Grid:
(0,0)=0   (0,1)=1   (0,2)=2(q)
(1,0)=2   (1,1)=3   (1,2)=2
(2,0)=1(p)(2,1)=1   (2,2)=3

Step 1: From (2,0)=1 to 4-neighbor (2,1)=1 (Value 1 in V). Length = 1.
Step 2: From (2,1)=1 to diagonal neighbor (1,2)=2 (Value 2 in V).
        Check m-adjacency condition between (2,1) and (1,2):
        N4(2,1) = {(2,0), (2,2), (1,1)}
        N4(1,2) = {(0,2), (2,2), (1,1)}
        Intersection N4(2,1) \cap N4(1,2) = {(2,2), (1,1)}.
        Intensities at (2,2) and (1,1) are both 3 \notin V.
        Since intersection contains no pixels in V, m-adjacency holds! Length = 2.
Step 3: From (1,2)=2 to 4-neighbor (0,2)=2(q) (Value 2 in V). Length = 3.
```

The shortest $`m`$-connected path is **Path:** $`(2,0) \to (2,1) \to (1,2) \to (0,2)`$, consisting of **3 path segments**.

##### Step 3: Final Answer Summary Table

| Distance Metric | Exact Formula Expression | Calculated Value (4 Decimal Places) |
| :--- | :--- | :---: |
| **Euclidean ($`D_e`$)** | $`\sqrt{(2-0)^2 + (0-2)^2} = \sqrt{8}`$ | **2.8284 units** |
| **City-Block ($`D_4`$)** | $`\lvert 2-0 \rvert + \lvert 0-2 \rvert = 4`$ | **4.0000 units** |
| **Chessboard ($`D_8`$)** | $`\max(2, 2) = 2`$ | **2.0000 units** |
| **Mixed Path ($`D_m`$)** | $`3 \text{ path steps}`$ | **3.0000 units** |

---

### Question 10: Region Growing Numerical with Seed Point (4x4 Matrix)

#### Exam Paper Reference
* **Source:** Batch 2024-25 Final Exam Q2c / Re-Exam 2023-24

#### Problem Statement
Apply region growing on the following $`4 \times 4`$ image matrix starting from seed point $`(2,2)`$ (0-indexed coordinates, value $`7`$) using $`4`$-connectivity.

```math
I = \begin{bmatrix}
  0 & 1 & 2 & 0 \\
  2 & 5 & 6 & 1 \\
  1 & 4 & 7 & 3 \\
  0 & 2 & 5 & 1
\end{bmatrix}
```

Growth Predicate: $`\lvert f(x,y) - \text{seed} \rvert \le 2`$.

#### Step-by-Step Solution

##### Step 1: Identify Seed Point and Growth Condition
* Seed pixel $`S = (2,2)`$ with intensity $`f(2,2) = 7`$.
* Predicate condition: Accept pixel $`p`$ if $`\lvert f(p) - 7 \rvert \le 2 \implies f(p) \in [5, 9]`$.

##### Step 2: Iterative 4-Connected Region Expansion

1. **Initial Region:** $`R = \{(2,2)\}`$ (Value 7).
2. **Inspect 4-Neighbors of $`(2,2)`$:**
   * Top neighbor $`(1,2) = 6`$: $`\lvert 6 - 7 \rvert = 1 \le 2`$. **ACCEPT** $`(1,2)`$.
   * Bottom neighbor $`(3,2) = 5`$: $`\lvert 5 - 7 \rvert = 2 \le 2`$. **ACCEPT** $`(3,2)`$.
   * Left neighbor $`(2,1) = 4`$: $`\lvert 4 - 7 \rvert = 3 > 2`$. REJECT.
   * Right neighbor $`(2,3) = 3`$: $`\lvert 3 - 7 \rvert = 4 > 2`$. REJECT.
   * Region now: $`R = \{(2,2), (1,2), (3,2)\}`$.

3. **Inspect 4-Neighbors of Newly Added Pixel $`(1,2)`$:**
   * Top neighbor $`(0,2) = 2`$: $`\lvert 2 - 7 \rvert = 5 > 2`$. REJECT.
   * Left neighbor $`(1,1) = 5`$: $`\lvert 5 - 7 \rvert = 2 \le 2`$. **ACCEPT** $`(1,1)`$.
   * Right neighbor $`(1,3) = 1`$: $`\lvert 1 - 7 \rvert = 6 > 2`$. REJECT.
   * Region now: $`R = \{(2,2), (1,2), (3,2), (1,1)\}`$.

4. **Inspect 4-Neighbors of Newly Added Pixel $`(3,2)`$:**
   * Left neighbor $`(3,1) = 2`$: $`\lvert 2 - 7 \rvert = 5 > 2`$. REJECT.
   * Right neighbor $`(3,3) = 1`$: $`\lvert 1 - 7 \rvert = 6 > 2`$. REJECT.

5. **Inspect 4-Neighbors of Newly Added Pixel $`(1,1)`$:**
   * Top neighbor $`(0,1) = 1`$: REJECT.
   * Left neighbor $`(1,0) = 2`$: REJECT.

6. **Termination:** No further adjacent pixels satisfy $`f(p) \in [5, 9]`$.

##### Step 3: Final Output Segmented Mask and Summary

```math
\text{Segmented Region Mask} = \begin{bmatrix}
  0 & 0 & 0 & 0 \\
  0 & 1 & 1 & 0 \\
  0 & 0 & 1 & 0 \\
  0 & 0 & 1 & 0
\end{bmatrix}
```

**Final Answer:**
The region growing algorithm identifies **4 connected pixels** belonging to the segmented object: $`\{(1,1), (1,2), (2,2), (3,2)\}`$ with corresponding intensity values $`\{5, 6, 7, 5\}`$.
