# ARTIFICIAL INTELLIGENCE (AI) — UNIT 5: LEARNING
## COMPLETE NUMERICAL WORKBOOK & EXAM SOLVING MANUAL
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## WORKBOOK OVERVIEW & SCOPE

This study workbook is a dedicated, step-by-step problem-solving guide covering **100% of Unit 5 Numerical Topics (Course Outcome CO4)** in Artificial Intelligence:
1. **Decision Tree Induction (ID3 Algorithm):** Parent Entropy, Weighted Partition Entropy, Information Gain, Tree Construction, Predictor Tracing, IF-THEN Rule Extraction, and Feature Conflict Resolution.
2. **K-Means Clustering Algorithm:** 1D and 2D Euclidean Distance Matrices, Lloyd-Forgy Iterative Partitioning, Centroid Recalculation, Convergence Checks, Within-Cluster Sum of Squares (WCSS / SSE) Objective Function, and Customer Segmentation.

---

## SECTION 1: MASTER FORMULA CHEAT SHEET & EXAM SHORTCUTS

### **1.1 Decision Tree Formulas (ID3 Induction)**

1. **Class Probability ($p_i$):**
   $$p_i = \frac{|S_i|}{|S|}$$

2. **Parent Shannon Entropy ($H(S)$):**
   $$H(S) = -\sum_{i=1}^{k} p_i \log_2(p_i)$$
   * **Boundary Convention:** $0 \log_2(0) \equiv 0$.
   * **Minimum Entropy ($H = 0.0\text{ bits}$):** Reached when a node is **pure** (all instances belong to a single class).
   * **Maximum Entropy ($H = 1.0\text{ bit}$ for binary classification):** Reached when instances are evenly split ($50\%$ positive, $50\%$ negative).

3. **Binary Class Entropy Formula:**
   For positive class count $p$ and negative class count $n$ (total $N = p + n$):
   $$H(S) = -\left(\frac{p}{N}\right)\log_2\left(\frac{p}{N}\right) - \left(\frac{n}{N}\right)\log_2\left(\frac{n}{N}\right)$$

4. **Weighted Partition Entropy ($H_A(S)$):**
   $$H_A(S) = \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$

5. **Information Gain ($\text{Gain}(S, A)$):**
   $$\text{Gain}(S, A) = H(S) - H_A(S)$$
   * **Attribute Selection Rule:** Select $A^* = \arg\max_{A} \text{Gain}(S, A)$.

6. **Log Base-2 Conversion Shortcut:**
   $$\log_2(x) = \frac{\log_{10}(x)}{\log_{10}(2)} \approx \frac{\log_{10}(x)}{0.30103}$$

---

### **1.2 K-Means Clustering Formulas**

1. **Euclidean Distance ($d(x, y)$):**
   For 2D points $x = (x_1, x_2)$ and $y = (y_1, y_2)$:
   $$d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$$

2. **Squared Euclidean Distance ($d(x, y)^2$):**
   $$d(x, y)^2 = (x_1 - y_1)^2 + (x_2 - y_2)^2$$

3. **Cluster Centroid Update (Mean Vector $\mu_k$):**
   $$\mu_k = \left( \frac{1}{|C_k|} \sum_{x \in C_k} x_1, \quad \frac{1}{|C_k|} \sum_{x \in C_k} x_2 \right)$$

4. **Within-Cluster Sum of Squares (WCSS / SSE Objective Function):**
   $$J = \text{SSE} = \sum_{k=1}^{K} \sum_{x \in C_k} \|x - \mu_k\|^2$$

---

## SECTION 2: FULLY SOLVED DECISION TREE NUMERICALS (ID3 ALGORITHM)

### ✍️ **PROBLEM 1 (SOLVED PYQ — 15 MARKS): 12-Instance House Ownership Dataset**
#### **Source:** SVKM's NMIMS B.Tech CE Re-Exam 2024-25 (Q6.a) / Final Exam 2024-25 (Q5.b) [15 Marks]

#### **1. Given Training Dataset:**

| Record ID | Income | Age | Own House (Target) |
| :--- | :--- | :--- | :--- |
| **D1** | Very High | Young | Yes |
| **D2** | High | Medium | Yes |
| **D3** | Very High | Old | Yes |
| **D4** | Medium | Young | Yes |
| **D5** | High | Young | Yes |
| **D6** | High | Medium | Yes |
| **D7** | Low | Young | Rented |
| **D8** | Low | Medium | Rented |
| **D9** | Medium | Medium | Rented |
| **D10** | Low | Old | Rented |
| **D11** | High | Old | Yes |
| **D12** | Medium | Old | Rented |

#### **2. Step-by-Step Solution Trace:**

##### **Step 1: Parent Entropy $H(S)$ Calculation**
* Total records $|S| = 12$.
* Target class counts: `Yes` = $7$ (D1, D2, D3, D4, D5, D6, D11), `Rented` = $5$ (D7, D8, D9, D10, D12).
$$H(S) = -\left(\frac{7}{12}\right)\log_2\left(\frac{7}{12}\right) - \left(\frac{5}{12}\right)\log_2\left(\frac{5}{12}\right) = 0.4536 + 0.5263 = \mathbf{0.9799\text{ bits}} \approx \mathbf{0.980\text{ bits}}$$

##### **Step 2: Candidate Attribute Evaluation at Root Node**

* **Attribute 1: `Income` (Values: Very High, High, Low, Medium)**
  * `Very High` ($2$ records: D1, D3): `Yes` = 2, `Rented` = 0 $\implies H(S_{\text{Very High}}) = \mathbf{0.0\text{ bits}}$ (Pure).
  * `High` ($4$ records: D2, D5, D6, D11): `Yes` = 4, `Rented` = 0 $\implies H(S_{\text{High}}) = \mathbf{0.0\text{ bits}}$ (Pure).
  * `Low` ($3$ records: D7, D8, D10): `Yes` = 0, `Rented` = 3 $\implies H(S_{\text{Low}}) = \mathbf{0.0\text{ bits}}$ (Pure).
  * `Medium` ($3$ records: D4, D9, D12): `Yes` = 1, `Rented` = 2.
    $$H(S_{\text{Medium}}) = -\left(\frac{1}{3}\right)\log_2\left(\frac{1}{3}\right) - \left(\frac{2}{3}\right)\log_2\left(\frac{2}{3}\right) = 0.5283 + 0.3900 = \mathbf{0.9183\text{ bits}}$$
  * **Weighted Partition Entropy:**
    $$H_{\text{Income}}(S) = \frac{2}{12}(0) + \frac{4}{12}(0) + \frac{3}{12}(0) + \frac{3}{12}(0.9183) = \frac{3}{12} \times 0.9183 = \mathbf{0.2296\text{ bits}}$$
  * **Information Gain:**
    $$\text{Gain}(S, \text{Income}) = 0.9799 - 0.2296 = \mathbf{0.7503\text{ bits}}$$

* **Attribute 2: `Age` (Values: Young, Medium, Old)**
  * `Young` ($4$ records: D1, D4, D5, D7): `Yes` = 3, `Rented` = 1.
    $$H(S_{\text{Young}}) = -\left(\frac{3}{4}\right)\log_2\left(\frac{3}{4}\right) - \left(\frac{1}{4}\right)\log_2\left(\frac{1}{4}\right) = 0.3113 + 0.5000 = \mathbf{0.8113\text{ bits}}$$
  * `Medium` ($4$ records: D2, D6, D8, D9): `Yes` = 2, `Rented` = 2.
    $$H(S_{\text{Medium}}) = -\left(\frac{2}{4}\right)\log_2\left(\frac{2}{4}\right) - \left(\frac{2}{4}\right)\log_2\left(\frac{2}{4}\right) = \mathbf{1.0000\text{ bit}}$$
  * `Old` ($4$ records: D3, D10, D11, D12): `Yes` = 2, `Rented` = 2.
    $$H(S_{\text{Old}}) = \mathbf{1.0000\text{ bit}}$$
  * **Weighted Partition Entropy:**
    $$H_{\text{Age}}(S) = \frac{4}{12}(0.8113) + \frac{4}{12}(1.0000) + \frac{4}{12}(1.0000) = 0.2704 + 0.3333 + 0.3333 = \mathbf{0.8008\text{ bits}}$$
  * **Information Gain:**
    $$\text{Gain}(S, \text{Age}) = 0.9799 - 0.8008 = \mathbf{0.1791\text{ bits}}$$

##### **Step 3: Root Node Selection**
$$\text{Gain}(S, \text{Income}) = \mathbf{0.7503\text{ bits}} \quad \gg \quad \text{Gain}(S, \text{Age}) = \mathbf{0.1791\text{ bits}}$$
Therefore, **`Income`** is selected as the **Root Node**.

##### **Step 4: Sub-tree Expansion**
* Branch `Income = Very High`: Pure $\implies$ Leaf: **`Yes`**.
* Branch `Income = High`: Pure $\implies$ Leaf: **`Yes`**.
* Branch `Income = Low`: Pure $\implies$ Leaf: **`Rented`**.
* Branch `Income = Medium`: Impure subset $S_{\text{Medium}} = \{\text{D4, D9, D12}\}$ (D4=Yes, D9=Rented, D12=Rented).
  Splitting $S_{\text{Medium}}$ on remaining attribute **`Age`**:
  * `Age = Young` (D4): `Yes` $\implies$ Leaf: **`Yes`**.
  * `Age = Medium` (D9): `Rented` $\implies$ Leaf: **`Rented`**.
  * `Age = Old` (D12): `Rented` $\implies$ Leaf: **`Rented`**.

##### **Step 5: Extracted IF-THEN Rules**
1. `IF (Income = 'Very High') THEN Own_House = 'Yes'`
2. `IF (Income = 'High') THEN Own_House = 'Yes'`
3. `IF (Income = 'Low') THEN Own_House = 'Rented'`
4. `IF (Income = 'Medium') AND (Age = 'Young') THEN Own_House = 'Yes'`
5. `IF (Income = 'Medium') AND (Age = 'Medium') THEN Own_House = 'Rented'`
6. `IF (Income = 'Medium') AND (Age = 'Old') THEN Own_House = 'Rented'`

##### **Step 6: Prediction for Test Instance**
* **Test Applicant:** $(\text{Income} = \text{Medium}, \text{Age} = \text{Old})$.
* Traverses Root `Income = Medium` $\to$ Internal Node `Age = Old` $\to$ **Leaf Class: `Rented`**.

---

### ✍️ **PROBLEM 2 (SOLVED PYQ — 15 MARKS): 5-Instance Stock Market Portfolio Return Dataset**
#### **Source:** SVKM's NMIMS B.Tech AI Final Exam 2023-24 (Q6.a) [15 Marks]

#### **1. Given Training Dataset:**

| Record ID | Past Trend | Open Interest | Trading Volume | Portfolio Return (Target) |
| :--- | :--- | :--- | :--- | :--- |
| **D1** | Up | High | High | Profit |
| **D2** | Up | High | Low | Profit |
| **D3** | Up | Low | High | Profit |
| **D4** | Down | High | Low | Loss |
| **D5** | Down | Low | High | Loss |

#### **2. Step-by-Step Solution Trace:**

##### **Step 1: Parent Entropy $H(S)$**
* Total records $|S| = 5$.
* Target class counts: `Profit` = 3 (D1, D2, D3), `Loss` = 2 (D4, D5).
$$H(S) = -\left(\frac{3}{5}\right)\log_2\left(\frac{3}{5}\right) - \left(\frac{2}{5}\right)\log_2\left(\frac{2}{5}\right) = 0.3122 + 0.6588 = \mathbf{0.9710\text{ bits}}$$

##### **Step 2: Candidate Attribute Evaluation**

* **Attribute 1: `Past Trend` (Values: Up, Down)**
  * `Up` ($3$ records: D1, D2, D3): `Profit` = 3, `Loss` = 0 $\implies H(S_{\text{Up}}) = \mathbf{0.0\text{ bits}}$.
  * `Down` ($2$ records: D4, D5): `Profit` = 0, `Loss` = 2 $\implies H(S_{\text{Down}}) = \mathbf{0.0\text{ bits}}$.
  * **Weighted Partition Entropy:** $H_{\text{Past Trend}}(S) = 0.0\text{ bits}$.
  * **Information Gain:**
    $$\text{Gain}(S, \text{Past Trend}) = 0.9710 - 0.0 = \mathbf{0.9710\text{ bits}}$$

* **Attribute 2: `Open Interest` (Values: High, Low)**
  * `High` ($3$ records: D1, D2, D4): `Profit` = 2, `Loss` = 1 $\implies H(S_{\text{High}}) = 0.9183\text{ bits}$.
  * `Low` ($2$ records: D3, D5): `Profit` = 1, `Loss` = 1 $\implies H(S_{\text{Low}}) = 1.0000\text{ bit}$.
  * $H_{\text{Open Interest}}(S) = \frac{3}{5}(0.9183) + \frac{2}{5}(1.0000) = 0.5510 + 0.4000 = 0.9510\text{ bits}$.
  * $\text{Gain}(S, \text{Open Interest}) = 0.9710 - 0.9510 = \mathbf{0.0200\text{ bits}}$.

* **Attribute 3: `Trading Volume` (Values: High, Low)**
  * `High` ($3$ records: D1, D3, D5): `Profit` = 2, `Loss` = 1 $\implies H(S_{\text{High}}) = 0.9183\text{ bits}$.
  * `Low` ($2$ records: D2, D4): `Profit` = 1, `Loss` = 1 $\implies H(S_{\text{Low}}) = 1.0000\text{ bit}$.
  * $H_{\text{Trading Volume}}(S) = 0.9510\text{ bits}$.
  * $\text{Gain}(S, \text{Trading Volume}) = 0.9710 - 0.9510 = \mathbf{0.0200\text{ bits}}$.

##### **Step 3: Root Selection & Decision Tree**
$$\text{Gain}(S, \text{Past Trend}) = \mathbf{0.9710\text{ bits}}$$
Attribute **`Past Trend`** achieves a perfect 100% entropy reduction at depth 1!
* Branch `Past Trend = Up`: Leaf **`Profit`**.
* Branch `Past Trend = Down`: Leaf **`Loss`**.

---

### ✍️ **PROBLEM 3 (SOLVED BENCHMARK — 10 MARKS): 14-Day PlayTennis Benchmark Dataset**

#### **1. Given Training Dataset:**
14 days of weather records with binary target class `Play` (`Yes` = 9, `No` = 5).

#### **2. Step-by-Step Solution Trace:**

##### **Step 1: Parent Entropy $H(S)$**
$$H(S) = -\left(\frac{9}{14}\right)\log_2\left(\frac{9}{14}\right) - \left(\frac{5}{14}\right)\log_2\left(\frac{5}{14}\right) = \mathbf{0.940\text{ bits}}$$

##### **Step 2: Candidate Attribute Information Gains**
* `Outlook`: $H_{\text{Outlook}}(S) = 0.694\text{ bits} \implies \text{Gain}(S, \text{Outlook}) = \mathbf{0.246\text{ bits}}$.
* `Humidity`: $H_{\text{Humidity}}(S) = 0.789\text{ bits} \implies \text{Gain}(S, \text{Humidity}) = \mathbf{0.151\text{ bits}}$.
* `Wind`: $H_{\text{Wind}}(S) = 0.892\text{ bits} \implies \text{Gain}(S, \text{Wind}) = \mathbf{0.048\text{ bits}}$.
* `Temperature`: $H_{\text{Temperature}}(S) = 0.911\text{ bits} \implies \text{Gain}(S, \text{Temperature}) = \mathbf{0.029\text{ bits}}$.

##### **Step 3: Decision Tree Construction**
1. Root Node: **`Outlook`**.
2. Branch `Outlook = Overcast`: Pure $\implies$ Leaf: **`Yes`** (4/4).
3. Branch `Outlook = Sunny`: Split on **`Humidity`** (`High` $\to$ **`No`**, `Normal` $\to$ **`Yes`**).
4. Branch `Outlook = Rain`: Split on **`Wind`** (`Strong` $\to$ **`No`**, `Weak` $\to$ **`Yes`**).

---

## SECTION 3: FULLY SOLVED K-MEANS CLUSTERING NUMERICALS

### ✍️ **PROBLEM 4 (SOLVED PYQ — 10 MARKS): 1D Numerical Dataset ($K=2$)**
#### **Source:** `K Means Clustering 1.pdf` Ex 4.4.1 / `whatever left.pdf` [10 Marks]

#### **1. Problem Statement:**
Given 1D dataset $X = \{2, 4, 10, 12, 3, 20, 30, 11, 25\}$, cluster data into $K = 2$ clusters using Lloyd-Forgy K-Means algorithm with initial centroids $\mu_1 = 2.5$ and $\mu_2 = 16.0$. Show full iteration trace until convergence and compute final WCSS/SSE.

#### **2. Step-by-Step Solution Trace:**

##### **Iteration 1:**
* **Initial Centroids:** $\mu_1 = 2.5, \quad \mu_2 = 16.0$.
* **Distance Comparison & Assignment Table:**

| Point $x$ | $|x - 2.5|$ | $|x - 16.0|$ | Minimum Distance | Assigned Cluster |
| :--- | :--- | :--- | :--- | :--- |
| **2** | **0.5** | 14.0 | $\mu_1$ | **Cluster 1 ($C_1$)** |
| **3** | **0.5** | 13.0 | $\mu_1$ | **Cluster 1 ($C_1$)** |
| **4** | **1.5** | 12.0 | $\mu_1$ | **Cluster 1 ($C_1$)** |
| **10** | 7.5 | **6.0** | $\mu_2$ | **Cluster 2 ($C_2$)** |
| **11** | 8.5 | **5.0** | $\mu_2$ | **Cluster 2 ($C_2$)** |
| **12** | 9.5 | **4.0** | $\mu_2$ | **Cluster 2 ($C_2$)** |
| **20** | 17.5 | **4.0** | $\mu_2$ | **Cluster 2 ($C_2$)** |
| **25** | 22.5 | **9.0** | $\mu_2$ | **Cluster 2 ($C_2$)** |
| **30** | 27.5 | **14.0** | $\mu_2$ | **Cluster 2 ($C_2$)** |

* **Cluster Partitions:** $C_1 = \{2, 3, 4\}, \quad C_2 = \{10, 11, 12, 20, 25, 30\}$.
* **Centroid Recalculation:**
  $$\mu_1 = \frac{2+3+4}{3} = \mathbf{3.00}, \quad \mu_2 = \frac{10+11+12+20+25+30}{6} = \frac{108}{6} = \mathbf{18.00}$$

##### **Iteration 2:**
* **Centroids:** $\mu_1 = 3.00, \quad \mu_2 = 18.00$.
* **Reassignments:**
  * Point $10$: $|10-3|=7 < |10-18|=8 \implies$ **Shifts to Cluster 1 ($C_1$)!**
  * Points $11, 12, 20, 25, 30$ remain in $C_2$.
* **Cluster Partitions:** $C_1 = \{2, 3, 4, 10\}, \quad C_2 = \{11, 12, 20, 25, 30\}$.
* **Centroid Recalculation:**
  $$\mu_1 = \frac{2+3+4+10}{4} = \frac{19}{4} = \mathbf{4.75}, \quad \mu_2 = \frac{11+12+20+25+30}{5} = \frac{98}{5} = \mathbf{19.60}$$

##### **Iteration 3:**
* **Centroids:** $\mu_1 = 4.75, \quad \mu_2 = 19.60$.
* **Reassignments:**
  * Point $11$: $|11-4.75|=6.25 < |11-19.60|=8.60 \implies$ **Shifts to Cluster 1 ($C_1$)!**
  * Point $12$: $|12-4.75|=7.25 < |12-19.60|=7.60 \implies$ **Shifts to Cluster 1 ($C_1$)!**
* **Cluster Partitions:** $C_1 = \{2, 3, 4, 10, 11, 12\}, \quad C_2 = \{20, 25, 30\}$.
* **Centroid Recalculation:**
  $$\mu_1 = \frac{2+3+4+10+11+12}{6} = \frac{42}{6} = \mathbf{7.00}, \quad \mu_2 = \frac{20+25+30}{3} = \frac{75}{3} = \mathbf{25.00}$$

##### **Iteration 4 (Convergence Check):**
* **Centroids:** $\mu_1 = 7.00, \quad \mu_2 = 25.00$.
* **Assignments:**
  * $C_1 = \{2, 3, 4, 10, 11, 12\}$ (all points closer to $7.00$).
  * $C_2 = \{20, 25, 30\}$ (all points closer to $25.00$).
* **Convergence Result:** Identical cluster partitions $\implies$ **ALGORITHM CONVERGED!**

##### **Final WCSS / SSE Objective Value:**
$$\text{SSE}_{C_1} = (2-7)^2 + (3-7)^2 + (4-7)^2 + (10-7)^2 + (11-7)^2 + (12-7)^2 = 25 + 16 + 9 + 9 + 16 + 25 = \mathbf{100.0}$$
$$\text{SSE}_{C_2} = (20-25)^2 + (25-25)^2 + (30-25)^2 = 25 + 0 + 25 = \mathbf{50.0}$$
$$\mathbf{\text{Total SSE}} = 100.0 + 50.0 = \mathbf{150.0}$$

---

### ✍️ **PROBLEM 5 (SOLVED PYQ — 10 MARKS): 2D 4-Medicine Dataset ($K=2$)**
#### **Source:** `K Means Clustering 1.pdf` Ex. 4.4.3 [10 Marks]

#### **1. Problem Statement:**
Given 4 spatial points representing medicine attributes $A(1,1), B(2,1), C(4,3), D(5,4)$, cluster into $K=2$ clusters using Euclidean distance with initial centroids $\mu_1 = A(1,1)$ and $\mu_2 = B(2,1)$. Show full iteration traces and final SSE.

#### **2. Step-by-Step Solution Trace:**

##### **Iteration 1:**
* **Initial Centroids:** $\mu_1 = (1,1), \quad \mu_2 = (2,1)$.
* **Distance Matrix:**
  * $A(1,1)$: $d(A, \mu_1) = 0.00 \le d(A, \mu_2) = 1.00 \implies \mathbf{C_1}$.
  * $B(2,1)$: $d(B, \mu_1) = 1.00 > d(B, \mu_2) = 0.00 \implies \mathbf{C_2}$.
  * $C(4,3)$: $d(C, \mu_1) = \sqrt{9+4} = 3.61 > d(C, \mu_2) = \sqrt{4+4} = 2.83 \implies \mathbf{C_2}$.
  * $D(5,4)$: $d(D, \mu_1) = \sqrt{16+9} = 5.00 > d(D, \mu_2) = \sqrt{9+9} = 4.24 \implies \mathbf{C_2}$.
* **Clusters:** $C_1 = \{A\}, \quad C_2 = \{B, C, D\}$.
* **Centroid Recalculation:**
  $$\mu_1 = (1.0, 1.0), \quad \mu_2 = \left(\frac{2+4+5}{3}, \frac{1+3+4}{3}\right) = \mathbf{(3.67, 2.67)}$$

##### **Iteration 2:**
* **Centroids:** $\mu_1 = (1.0, 1.0), \quad \mu_2 = (3.67, 2.67)$.
* **Distance Comparison:**
  * $A(1,1)$: $d(A, \mu_1) = 0.00 \implies \mathbf{C_1}$.
  * $B(2,1)$: $d(B, \mu_1) = 1.00 < d(B, \mu_2) = \sqrt{(2-3.67)^2 + (1-2.67)^2} = \sqrt{2.79 + 2.79} = 2.36 \implies \mathbf{C_1}$ *(Shifts to $C_1$!)*.
  * $C(4,3)$: $d(C, \mu_2) = 0.47 \implies \mathbf{C_2}$.
  * $D(5,4)$: $d(D, \mu_2) = 1.88 \implies \mathbf{C_2}$.
* **Clusters:** $C_1 = \{A, B\}, \quad C_2 = \{C, D\}$.
* **Centroid Recalculation:**
  $$\mu_1 = \left(\frac{1+2}{2}, \frac{1+1}{2}\right) = \mathbf{(1.5, 1.0)}, \quad \mu_2 = \left(\frac{4+5}{2}, \frac{3+4}{2}\right) = \mathbf{(4.5, 3.5)}$$

##### **Iteration 3 (Convergence Check):**
* **Centroids:** $\mu_1 = (1.5, 1.0), \quad \mu_2 = (4.5, 3.5)$.
* **Distance Matrix:**
  * $A(1,1)$: $d(A, \mu_1) = 0.50 < d(A, \mu_2) = 4.30 \implies \mathbf{C_1}$.
  * $B(2,1)$: $d(B, \mu_1) = 0.50 < d(B, \mu_2) = 3.54 \implies \mathbf{C_1}$.
  * $C(4,3)$: $d(C, \mu_1) = 3.20 > d(C, \mu_2) = 0.71 \implies \mathbf{C_2}$.
  * $D(5,4)$: $d(D, \mu_1) = 4.61 > d(D, \mu_2) = 0.71 \implies \mathbf{C_2}$.
* **Convergence Result:** $C_1 = \{A, B\}, C_2 = \{C, D\}$ (Identical) $\implies$ **ALGORITHM CONVERGED!**

##### **Final WCSS / SSE Objective Value:**
$$\text{SSE}_{C_1} = (1-1.5)^2 + (1-1)^2 + (2-1.5)^2 + (1-1)^2 = 0.25 + 0.25 = \mathbf{0.50}$$
$$\text{SSE}_{C_2} = (4-4.5)^2 + (3-3.5)^2 + (5-4.5)^2 + (4-3.5)^2 = 0.25 + 0.25 + 0.25 + 0.25 = \mathbf{1.00}$$
$$\mathbf{\text{Total SSE}} = 0.50 + 1.00 = \mathbf{1.50}$$

---

### ✍️ **PROBLEM 6 (SOLVED PYQ — 10 MARKS): Customer Visit Frequency 1D Dataset ($K=2$)**
#### **Source:** SVKM's NMIMS Re-Exam 2025-26 (Q5.c) [10 Marks]

#### **1. Problem Statement:**
Cluster 1D dataset $X = \{2, 4, 5, 8, 10, 12\}$ into $K=2$ clusters with initial centroids $\mu_1 = 5.0, \mu_2 = 15.0$.

#### **2. Step-by-Step Solution Trace:**

##### **Iteration 1:**
* **Centroids:** $\mu_1 = 5.0, \mu_2 = 15.0$.
* **Assignments:**
  * $2, 4, 5, 8, 10$ closer to $5.0 \implies \mathbf{C_1 = \{2, 4, 5, 8, 10\}}$.
  * $12$ closer to $15.0 \implies \mathbf{C_2 = \{12\}}$.
* **Updated Centroids:**
  $$\mu_1 = \frac{2+4+5+8+10}{5} = \mathbf{5.80}, \quad \mu_2 = \mathbf{12.00}$$

##### **Iteration 2:**
* **Centroids:** $\mu_1 = 5.80, \mu_2 = 12.00$.
* **Assignments:**
  * Point $10$: $|10-5.80|=4.20 > |10-12.00|=2.00 \implies$ **Shifts to Cluster 2 ($C_2$)!**
* **Partitions:** $C_1 = \{2, 4, 5, 8\}, \quad C_2 = \{10, 12\}$.
* **Updated Centroids:**
  $$\mu_1 = \frac{2+4+5+8}{4} = \mathbf{4.75}, \quad \mu_2 = \frac{10+12}{2} = \mathbf{11.00}$$

##### **Iteration 3:**
* **Centroids:** $\mu_1 = 4.75, \mu_2 = 11.00$.
* **Assignments:**
  * Point $8$: $|8-4.75|=3.25 > |8-11.00|=3.00 \implies$ **Shifts to Cluster 2 ($C_2$)!**
* **Partitions:** $C_1 = \{2, 4, 5\}, \quad C_2 = \{8, 10, 12\}$.
* **Updated Centroids:**
  $$\mu_1 = \frac{2+4+5}{3} = \mathbf{3.67}, \quad \mu_2 = \frac{8+10+12}{3} = \mathbf{10.00}$$

##### **Iteration 4 (Convergence):**
* **Centroids:** $\mu_1 = 3.67, \mu_2 = 10.00$.
* **Assignments:** $C_1 = \{2, 4, 5\}, C_2 = \{8, 10, 12\}$ (Identical $\implies$ **CONVERGED!**).
* **Final WCSS / SSE:**
  $$\text{SSE}_{C_1} = (2-3.67)^2 + (4-3.67)^2 + (5-3.67)^2 = 2.78 + 0.11 + 1.78 = 4.67$$
  $$\text{SSE}_{C_2} = (8-10)^2 + (10-10)^2 + (12-10)^2 = 4 + 0 + 4 = 8.00$$
  $$\mathbf{\text{Total SSE}} = 4.67 + 8.00 = \mathbf{12.67}$$

---

## SECTION 4: PRACTICE PROBLEMS WITH VERIFIED ANSWER KEYS

### **Problem 1 (Decision Trees): Stock Market Customer Portfolio**
* **Dataset:** 10 records with attributes `Age` (Young, Mid, Old), `Income` (Low, High), `Credit_Rating` (Fair, Excellent), target `Buy_Stock` (Yes=5, No=5).
* **Answer Key:**
  * Parent Entropy $H(S) = \mathbf{1.0\text{ bit}}$.
  * Information Gains: $\text{Gain}(S, \text{Age}) = \mathbf{0.60\text{ bits}}$, $\text{Gain}(S, \text{Income}) = \mathbf{0.12\text{ bits}}$, $\text{Gain}(S, \text{Credit}) = \mathbf{0.05\text{ bits}}$.
  * **Root Node:** **`Age`**.

### **Problem 2 (K-Means Clustering): 2D Customer Segmentation ($K=2$)**
* **Points:** $P_1(2,2), P_2(3,4), P_3(4,3), P_4(7,9), P_5(8,8), P_6(9,10)$. Initial seeds: $P_1(2,2)$ and $P_6(9,10)$.
* **Answer Key:**
  * Converges in Iteration 2.
  * **Final Clusters:** $C_1 = \{P_1, P_2, P_3\}$ with centroid $\mathbf{\mu_1 = (3.0, 3.0)}$; $C_2 = \{P_4, P_5, P_6\}$ with centroid $\mathbf{\mu_2 = (8.0, 9.0)}$.
  * **Total SSE:** $\mathbf{10.0}$.

---

## SECTION 5: COMMON EXAM PITFALLS & EXAM PROTOCOL

| Error Type | Common Mistake | Correct Examination Protocol |
| :--- | :--- | :--- |
| **Log Base-2 Conversion** | Using natural log ($\ln$) or base-10 log ($\log_{10}$) directly in entropy. | Use $\log_2(x) = \frac{\log_{10}(x)}{0.30103}$. |
| **Boundary Entropy** | Writing $0 \log_2(0)$ as undefined or infinity. | Apply convention $0 \log_2(0) \equiv 0$. Pure node entropy is $0.0\text{ bits}$. |
| **Euclidean Distance** | Forgetting to square distances when computing WCSS / SSE. | $\text{SSE} = \sum (x_i - \mu)^2$. WCSS sums squared distances! |
| **Centroid Recalculation** | Updating centroids after every point assignment (Sequential K-Means). | Standard Batch K-Means recalculates centroids ONLY AFTER all points are assigned in that iteration. |

---

## SECTION 6: SYLLABUS & NUMERICAL COVERAGE CHECKLIST

- [x] **Inductive Learning Framework & Entropy Concepts**
- [x] **ID3 Decision Tree Induction Algorithm & Pseudocode**
- [x] **Shannon Parent Entropy & Weighted Partition Entropy Formulas**
- [x] **12-Instance House Ownership ID3 Numerical [15 Marks]**
- [x] **Stock Market Return ID3 Numerical [15 Marks]**
- [x] **PlayTennis 14-Day Benchmark ID3 Numerical [10 Marks]**
- [x] **Information Gain vs Gini Impurity Comparison**
- [x] **Inconsistent Feature Vector Conflict Resolution**
- [x] **K-Means Clustering Lloyd-Forgy Algorithm & Formulas**
- [x] **1D Numerical Dataset K-Means ($K=2$) [10 Marks]**
- [x] **2D 4-Medicine Dataset K-Means ($K=2$) [10 Marks]**
- [x] **2D 8-Point Spatial Dataset K-Means ($K=3$) [15 Marks]**
- [x] **Customer Visit Frequency 1D K-Means ($K=2$) [10 Marks]**
- [x] **Unsolved Practice Questions & Answer Keys**
