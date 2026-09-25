# ARTIFICIAL INTELLIGENCE (AI) — UNIT 5: LEARNING (UP TO DECISION TREES)
## WORKED NUMERICALS & DECISION TREE WORKBOOK
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## WORKBOOK OVERVIEW & SCOPE

This study workbook is a dedicated, step-by-step problem-solving guide covering **Decision Tree Induction (ID3 Algorithm), Entropy, Information Gain, Tree Construction, Class Prediction, and IF-THEN Rule Extraction**. 

### **Strict Scope Boundary:**
* **Included:** ID3 Algorithm, Shannon Entropy ($H$), Weighted Partition Entropy ($H_A$), Maximum Information Gain ($\text{Gain}$), Top-Down Recursive Partitioning, Tree Formatting, Predictor Tracing, IF-THEN Rule Extraction, Empty Branch Handling, and Feature Conflict Resolution.
* **Excluded:** Gini Impurity and CART (Classification and Regression Trees). If a past university exam question contains a multi-part query involving both Gini Index and Information Gain, the Gini/CART portion is explicitly identified as outside this workbook's scope, and the **ID3 / Information Gain portion is solved completely and rigorously**.

### **Source Verification Status:**
* Every numerical calculation in this workbook (entropies, weighted entropies, information gains, and tree structures) has been **independently recalculated from each problem's own training table** and cross-checked programmatically — these figures are verified.
* The **exam attributions** (paper name, year, question number, marks) for Problems 1–3 are **not** independently confirmed against original NMIMS question papers and are marked accordingly at each problem. Treat them as best-effort labels, not certified citations.

---

## SECTION 1: FORMULA & RULE REFERENCE LIST

Before solving numericals, review the mathematical definitions, notation, and algorithmic rules governing the ID3 decision tree induction process.

### **1.1 Mathematical Definitions & Formulas**

1. **Class Probability ($p_i$):**
   The proportion of instances in dataset $S$ belonging to target class $c_i$:
   $$p_i = \frac{|S_{c_i}|}{|S|}$$
   where $|S_{c_i}|$ is the count of records with class label $c_i$, and $|S|$ is the total number of records in dataset partition $S$.

2. **Parent Dataset Entropy ($H(S)$):**
   Entropy measures the class uncertainty or impurity within a dataset partition $S$ containing $k$ distinct target classes:
   $$H(S) = -\sum_{i=1}^{k} p_i \log_2(p_i)$$
   * **Boundary Convention:** $0 \log_2(0) \equiv 0$ (if a class count is $0$, its entropy contribution is $0$).
   * **Minimum Entropy ($H = 0.0\text{ bits}$):** Reached when a node is **completely pure** (all instances belong to a single class).
   * **Maximum Entropy ($H = 1.0\text{ bit}$ for binary classification):** Reached when instances are evenly split (e.g., $50\%$ Class A, $50\%$ Class B).

3. **Binary Class Entropy Formula:**
   For a dataset $S$ with positive class count $p$ and negative class count $n$ (total $N = p + n$):
   $$p_+ = \frac{p}{p+n}, \quad p_- = \frac{n}{p+n}$$
   $$H(S) = -p_+ \log_2(p_+) - p_- \log_2(p_-) = -\left(\frac{p}{N}\right)\log_2\left(\frac{p}{N}\right) - \left(\frac{n}{N}\right)\log_2\left(\frac{n}{N}\right)$$

4. **Weighted Partition Entropy ($H_A(S)$):**
   When dataset $S$ is partitioned by candidate attribute $A$ into sub-datasets $\{S_v\}$ corresponding to each distinct attribute value $v \in \text{Values}(A)$, the expected residual entropy across all child nodes is:
   $$H_A(S) = \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
   where $\frac{|S_v|}{|S|}$ represents the weight (fraction of records) falling into child branch $v$.

5. **Information Gain ($\text{Gain}(S, A)$):**
   Information Gain measures the expected reduction in entropy achieved by splitting dataset $S$ on attribute $A$:
   $$\text{Gain}(S, A) = H(S) - H_A(S) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$

---

### **1.2 Base-2 Logarithm Conversion & Value Cheat Sheet**

In written university examinations where base-2 scientific calculators are restricted, convert standard base-10 logarithms ($\log_{10}$) or natural logarithms ($\ln$) using the change-of-base formula:
$$\log_2(x) = \frac{\log_{10}(x)}{\log_{10}(2)} \approx \frac{\log_{10}(x)}{0.30103}$$

#### **Frequently Used Base-2 Logarithm & Entropy Values:**
* $\log_2(1) = 0.0000$
* $\log_2(2) = 1.0000$
* $\log_2(3) \approx 1.5850$
* $\log_2(4) = 2.0000$
* $\log_2(5) \approx 2.3219$
* $\log_2(6) \approx 2.5850$
* $\log_2(7) \approx 2.8074$
* $\log_2(8) = 3.0000$
* $\log_2(9) \approx 3.1699$
* $\log_2(10) \approx 3.3219$
* $\log_2(12) \approx 3.5850$
* $\log_2(14) \approx 3.8074$

#### **Standard Binary Entropy Values:**
* $H(1/2, 1/2) = 1.0000\text{ bits}$ ($50\% - 50\%$)
* $H(2/3, 1/3) \approx 0.9183\text{ bits}$ ($66.7\% - 33.3\%$)
* $H(3/4, 1/4) \approx 0.8113\text{ bits}$ ($75\% - 25\%$)
* $H(4/5, 1/5) \approx 0.7219\text{ bits}$ ($80\% - 20\%$)
* $H(3/5, 2/5) \approx 0.9710\text{ bits}$ ($60\% - 40\%$)
* $H(7/12, 5/12) \approx 0.9799\text{ bits}$ ($58.3\% - 41.7\%$)
* $H(9/14, 5/14) \approx 0.9403\text{ bits}$ ($64.3\% - 35.7\%$)

---

### **1.3 Special Algorithmic Rules & Edge Case Handling**

1. **Principle of Maximum Information Gain:**
   At each decision node, ID3 evaluates all candidate attributes that have not yet been used along the current path. It selects the attribute $A^*$ that maximizes Information Gain:
   $$A^* = \arg\max_{A} \text{Gain}(S, A)$$

2. **Stopping Criteria for Tree Expansion:**
   A branch terminates and creates a **Leaf Node** if any of these conditions are met:
   * **Pure Subset:** All records in partition $S$ belong to the exact same target class.
   * **Exhausted Attributes:** All candidate attributes have been used along the current path, but partition $S$ is still impure. Create a leaf node labeled with the **majority target class** in $S$.
   * **Empty Partition:** An attribute value $v$ creates an empty sub-dataset ($|S_v| = 0$). Create a leaf node labeled with the **majority target class of the parent node**.

3. **Handling Class Ties:**
   If a subset reaches a stopping condition with an exact equal tie between two target classes (e.g., $1$ Yes and $1$ No), apply the following deterministic tie-breaker, **in order**, and state which rule was used:
   1. **Global parent majority:** If the immediate parent node (or an ancestor, up to the root) has an overall majority class, assign that class to the leaf.
   2. **First-encountered record:** If no majority exists at any ancestor level (e.g., the tied subset *is* the entire dataset), assign the class of the first record in the original dataset listing. This is arbitrary but deterministic and reproducible.
   Always report the underlying class distribution (e.g., $P(\text{Yes}) = 0.5, P(\text{No}) = 0.5$) alongside the single-class leaf, since the tie-break is a default, not a discovered pattern.

4. **Handling Feature Conflicts (Inconsistent Data):**
   If two or more training instances possess **identical feature vectors** across all available attributes but carry **conflicting target labels** (e.g., $X = (\text{High}, \text{Good}) \to \text{Approved = Yes}$ and $X = (\text{High}, \text{Good}) \to \text{Approved = No}$), no deterministic decision tree can achieve $100\%$ training accuracy. 
   * **Protocol:** Flag the data conflict explicitly, compute the probabilities for each label, and set the leaf node to the majority class or class distribution.

---

## SECTION 2: FULLY SOLVED PAST-PAPER-STYLE NUMERICALS (SOURCES UNVERIFIED — SEE NOTES)

---

### ✍️ **PROBLEM 1 (PAST-PAPER-STYLE NUMERICAL — SOURCE UNVERIFIED)**
#### **Attributed Source (unverified):** SVKM's NMIMS B.Tech CE Re-Examination 2024-25 (Q6.a) / Final Examination 2024-25 (Q5.b) — reported as 15 Marks
> ⚠️ **Verification note:** The exact wording, question number, marks weight, and paper year for this dataset could not be cross-checked against an original NMIMS question paper in this session. Treat this as a **past-paper-style practice numerical modelled on the topic**, not a confirmed verbatim PYQ, until you check it against the actual paper. The dataset and all calculations below are internally correct and self-consistent regardless of source.

#### **1. Original Question Statement:**
Given the following training dataset for predicting house ownership (`Own House`), construct a complete decision tree using the ID3 algorithm. Show all calculations for dataset entropy, attribute entropies, and information gains. Draw the final decision tree, extract the IF-THEN rules, and predict the class label for a new applicant with:
$$\text{Applicant X} = (\text{Income} = \text{Medium}, \text{Age} = \text{Old})$$

#### **2. Given Training Dataset:**

| Record ID | Income | Age | Own House (Target) |
| :---: | :---: | :---: | :---: |
| **D1** | Very High | Young | **Yes** |
| **D2** | High | Medium | **Yes** |
| **D3** | Low | Young | **Rented** |
| **D4** | Medium | Medium | **Rented** |
| **D5** | High | Old | **Yes** |
| **D6** | Very High | Medium | **Yes** |
| **D7** | Low | Old | **Rented** |
| **D8** | High | Young | **Yes** |
| **D9** | Medium | Old | **Rented** |
| **D10** | Low | Medium | **Rented** |
| **D11** | High | Young | **Yes** |
| **D12** | Medium | Young | **Yes** |

---

#### **3. Step-by-Step Solution Trace:**

##### **Step 1: Dataset Characterization & Parent Entropy $H(S)$**
* **Total Instances ($|S|$):** $12$
* **Target Classes:** `Yes` (Positive) and `Rented` (Negative).
* **Class Frequencies:**
  * `Yes` count ($p$): $7$ instances (D1, D2, D5, D6, D8, D11, D12)
  * `Rented` count ($n$): $5$ instances (D3, D4, D7, D9, D10)
* **Class Probabilities:**
  $$p_{\text{Yes}} = \frac{7}{12} \approx 0.5833, \quad p_{\text{Rented}} = \frac{5}{12} \approx 0.4167$$

* **Parent Entropy Calculation:**
  $$H(S) = -p_{\text{Yes}} \log_2(p_{\text{Yes}}) - p_{\text{Rented}} \log_2(p_{\text{Rented}})$$
  $$H(S) = -\left(\frac{7}{12}\right)\log_2\left(\frac{7}{12}\right) - \left(\frac{5}{12}\right)\log_2\left(\frac{5}{12}\right)$$
  $$\log_2\left(\frac{7}{12}\right) = \log_2(7) - \log_2(12) \approx 2.8074 - 3.5850 = -0.7776$$
  $$\log_2\left(\frac{5}{12}\right) = \log_2(5) - \log_2(12) \approx 2.3219 - 3.5850 = -1.2631$$
  $$H(S) = -\left(0.5833 \times -0.7776\right) - \left(0.4167 \times -1.2631\right)$$
  $$H(S) = 0.4535 + 0.5263 = \mathbf{0.9799\text{ bits}}$$

---

##### **Step 2: Candidate Attribute Evaluation at Root Node**

###### **Evaluation of Attribute 1: `Income`**
`Income` has 4 distinct values: `Very High`, `High`, `Low`, `Medium`.

1. **Branch `Income = Very High` ($S_{\text{Very High}}$):**
   * Records: D1, D6 (Total: $2$)
   * Class Distribution: $2\text{ Yes}, 0\text{ Rented}$ (Pure Subset!)
   * Entropy: $H(S_{\text{Very High}}) = 0.0000\text{ bits}$

2. **Branch `Income = High` ($S_{\text{High}}$):**
   * Records: D2, D5, D8, D11 (Total: $4$)
   * Class Distribution: $4\text{ Yes}, 0\text{ Rented}$ (Pure Subset!)
   * Entropy: $H(S_{\text{High}}) = 0.0000\text{ bits}$

3. **Branch `Income = Low` ($S_{\text{Low}}$):**
   * Records: D3, D7, D10 (Total: $3$)
   * Class Distribution: $0\text{ Yes}, 3\text{ Rented}$ (Pure Subset!)
   * Entropy: $H(S_{\text{Low}}) = 0.0000\text{ bits}$

4. **Branch `Income = Medium` ($S_{\text{Medium}}$):**
   * Records: D4, D9, D12 (Total: $3$)
   * Class Distribution: $1\text{ Yes}\text{ (D12)}, 2\text{ Rented}\text{ (D4, D9)}$
   * Entropy Calculation:
     $$H(S_{\text{Medium}}) = -\left(\frac{1}{3}\right)\log_2\left(\frac{1}{3}\right) - \left(\frac{2}{3}\right)\log_2\left(\frac{2}{3}\right)$$
     $$H(S_{\text{Medium}}) = -(0.3333 \times -1.5850) - (0.6667 \times -0.5850) = 0.5283 + 0.3900 = \mathbf{0.9183\text{ bits}}$$

* **Weighted Partition Entropy ($H_{\text{Income}}(S)$):**
  $$H_{\text{Income}}(S) = \frac{2}{12}(0.0) + \frac{4}{12}(0.0) + \frac{3}{12}(0.0) + \frac{3}{12}(0.9183)$$
  $$H_{\text{Income}}(S) = \frac{3}{12} \times 0.9183 = 0.25 \times 0.9183 = \mathbf{0.2296\text{ bits}}$$

* **Information Gain ($\text{Gain}(S, \text{Income})$):**
  $$\text{Gain}(S, \text{Income}) = H(S) - H_{\text{Income}}(S) = 0.9799 - 0.2296 = \mathbf{0.7503\text{ bits}}$$

---

###### **Evaluation of Attribute 2: `Age`**
`Age` has 3 distinct values: `Young`, `Medium`, `Old`.

1. **Branch `Age = Young` ($S_{\text{Young}}$):**
   * Records: D1, D3, D8, D11, D12 (Total: $5$)
   * Class Distribution: $4\text{ Yes}\text{ (D1, D8, D11, D12)}, 1\text{ Rented}\text{ (D3)}$
   * Entropy Calculation:
     $$H(S_{\text{Young}}) = -\left(\frac{4}{5}\right)\log_2\left(\frac{4}{5}\right) - \left(\frac{1}{5}\right)\log_2\left(\frac{1}{5}\right)$$
     $$H(S_{\text{Young}}) = -(0.8 \times -0.3219) - (0.2 \times -2.3219) = 0.2575 + 0.4644 = \mathbf{0.7219\text{ bits}}$$

2. **Branch `Age = Medium` ($S_{\text{Medium-Age}}$):**
   * Records: D2, D4, D6, D10 (Total: $4$)
   * Class Distribution: $2\text{ Yes}\text{ (D2, D6)}, 2\text{ Rented}\text{ (D4, D10)}$ (Equal 50/50 split!)
   * Entropy: $H(S_{\text{Medium-Age}}) = \mathbf{1.0000\text{ bit}}$

3. **Branch `Age = Old` ($S_{\text{Old}}$):**
   * Records: D5, D7, D9 (Total: $3$)
   * Class Distribution: $1\text{ Yes}\text{ (D5)}, 2\text{ Rented}\text{ (D7, D9)}$
   * Entropy Calculation: $H(S_{\text{Old}}) = \mathbf{0.9183\text{ bits}}$

* **Weighted Partition Entropy ($H_{\text{Age}}(S)$):**
  $$H_{\text{Age}}(S) = \frac{5}{12}(0.7219) + \frac{4}{12}(1.0000) + \frac{3}{12}(0.9183)$$
  $$H_{\text{Age}}(S) = (0.4167 \times 0.7219) + (0.3333 \times 1.0000) + (0.2500 \times 0.9183)$$
  $$H_{\text{Age}}(S) = 0.3008 + 0.3333 + 0.2296 = \mathbf{0.8637\text{ bits}}$$

* **Information Gain ($\text{Gain}(S, \text{Age})$):**
  $$\text{Gain}(S, \text{Age}) = H(S) - H_{\text{Age}}(S) = 0.9799 - 0.8637 = \mathbf{0.1162\text{ bits}}$$

---

##### **Step 3: Root Node Selection**
Comparing Information Gains:
$$\text{Gain}(S, \text{Income}) = 0.7503\text{ bits}$$
$$\text{Gain}(S, \text{Age}) = 0.1162\text{ bits}$$

**Decision:** `Income` provides the maximum Information Gain ($0.7503\text{ bits} > 0.1162\text{ bits}$) and is selected as the **Root Node** of the decision tree.

---

##### **Step 4: Recursive Sub-tree Expansion**

1. **Branch `Income = Very High`:**
   * Contains D1, D6 ($2\text{ Yes}, 0\text{ Rented}$). 
   * Partition is pure $\to$ Create **Leaf Node: `Yes`**.

2. **Branch `Income = High`:**
   * Contains D2, D5, D8, D11 ($4\text{ Yes}, 0\text{ Rented}$). 
   * Partition is pure $\to$ Create **Leaf Node: `Yes`**.

3. **Branch `Income = Low`:**
   * Contains D3, D7, D10 ($0\text{ Yes}, 3\text{ Rented}$). 
   * Partition is pure $\to$ Create **Leaf Node: `Rented`**.

4. **Branch `Income = Medium`:**
   * Contains D4, D9, D12 ($1\text{ Yes}, 2\text{ Rented}$). Partition is impure!
   * Subset $S_{\text{Medium}} = \{\text{D4 (Medium Age, Rented)}, \text{D9 (Old Age, Rented)}, \text{D12 (Young Age, Yes)}\}$.
   * Expand sub-node using remaining candidate attribute: **`Age`**.
     * Sub-branch `Age = Young` (D12): Class is `Yes` $\to$ Create **Leaf Node: `Yes`**.
     * Sub-branch `Age = Medium` (D4): Class is `Rented` $\to$ Create **Leaf Node: `Rented`**.
     * Sub-branch `Age = Old` (D9): Class is `Rented` $\to$ Create **Leaf Node: `Rented`**.

---

##### **Step 5: Final Decision Tree Diagram**

```text
                              [ Income ]
                 /               |               |               \
      Very High /           High |        Medium |            Low \
               /                 |               |                 \
              v                  v                v                 v
          ( Yes )             ( Yes )         [ Age ]           ( Rented )
                                              /   |    \
                                      Young  /    |     \  Old
                                            /  Medium    \
                                           v      v        v
                                       ( Yes ) (Rented) (Rented)
```

**Branch key (root):** `Very High → Yes` | `High → Yes` | `Medium → [Age]` | `Low → Rented`
**Branch key (Age sub-node, under `Income = Medium` only):** `Young → Yes` | `Medium → Rented` | `Old → Rented`

---

##### **Step 6: IF-THEN Rule Extraction**

* **Rule 1:** IF $(\text{Income} = \text{Very High})$ THEN $(\text{Own House} = \text{Yes})$
* **Rule 2:** IF $(\text{Income} = \text{High})$ THEN $(\text{Own House} = \text{Yes})$
* **Rule 3:** IF $(\text{Income} = \text{Low})$ THEN $(\text{Own House} = \text{Rented})$
* **Rule 4:** IF $(\text{Income} = \text{Medium})$ AND $(\text{Age} = \text{Young})$ THEN $(\text{Own House} = \text{Yes})$
* **Rule 5:** IF $(\text{Income} = \text{Medium})$ AND $(\text{Age} = \text{Medium})$ THEN $(\text{Own House} = \text{Rented})$
* **Rule 6:** IF $(\text{Income} = \text{Medium})$ AND $(\text{Age} = \text{Old})$ THEN $(\text{Own House} = \text{Rented})$

---

##### **Step 7: Prediction for Test Instance & Verification**

* **Test Applicant X:** $(\text{Income} = \text{Medium}, \text{Age} = \text{Old})$
* **Execution Trace:**
  1. Start at Root Node `Income`.
  2. Applicant's `Income` is `Medium` $\to$ Follow `Medium` branch down to internal node `Age`.
  3. Applicant's `Age` is `Old` $\to$ Follow `Old` branch down to Leaf Node.
  4. Leaf Node reached: **`Rented`**.
* **Final Prediction:** **`Own House = Rented`**.
* **Training Data Consistency Check:** Matches record D9 $(\text{Medium}, \text{Old} \to \text{Rented})$. The decision tree achieves $100\%$ accuracy across all 12 training instances.

---

### ✍️ **PROBLEM 2 (PAST-PAPER-STYLE NUMERICAL — SOURCE UNVERIFIED)**
#### **Attributed Source (unverified):** SVKM's NMIMS B.Tech AI Final Examination 2025-26 (Q6.a) — reported as 15 Marks
> ⚠️ **Verification note:** As with Problem 1, the exact paper, question number, and marks could not be confirmed against an original NMIMS paper in this session. Note also that this dataset differs from the "stock returns" table appearing in the separate Unit 5 PYQ file referenced earlier — the two should **not** be assumed to be the same verified question. Treat this as a practice numerical until checked against the actual paper.

#### **1. Original Question Statement:**
A stock market investment firm collected the following 5-instance dataset to predict stock portfolio performance (`Return` = `Profit` or `Loss`). Construct an ID3 decision tree by calculating the parent entropy and the Information Gain for `Past Trend`, `Open Interest`, and `Trading Volume`. Identify the root split and draw the complete decision tree.

#### **2. Given Training Dataset:**

| Instance ID | Past Trend | Open Interest | Trading Volume | Return (Target) |
| :---: | :---: | :---: | :---: | :---: |
| **X1** | Up | High | High | **Profit** |
| **X2** | Up | High | Low | **Profit** |
| **X3** | Down | Low | High | **Loss** |
| **X4** | Down | High | Low | **Loss** |
| **X5** | Up | Low | High | **Profit** |

---

#### **3. Step-by-Step Solution Trace:**

##### **Step 1: Dataset Characterization & Parent Entropy $H(S)$**
* **Total Instances ($|S|$):** $5$
* **Target Class Counts:**
  * `Profit` ($p$): $3$ instances (X1, X2, X5)
  * `Loss` ($n$): $2$ instances (X3, X4)
* **Class Probabilities:**
  $$p_{\text{Profit}} = \frac{3}{5} = 0.60, \quad p_{\text{Loss}} = \frac{2}{5} = 0.40$$

* **Parent Entropy Calculation:**
  $$H(S) = -0.60 \log_2(0.60) - 0.40 \log_2(0.40)$$
  $$\log_2(0.60) \approx -0.7370, \quad \log_2(0.40) \approx -1.3219$$
  $$H(S) = -(0.60 \times -0.7370) - (0.40 \times -1.3219) = 0.4422 + 0.5288 = \mathbf{0.9710\text{ bits}}$$

---

##### **Step 2: Information Gain Calculations for Candidate Attributes**

###### **Candidate 1: `Past Trend` (Values: Up, Down)**
1. **Branch `Past Trend = Up` ($S_{\text{Up}}$):**
   * Records: X1, X2, X5 (Total: $3$)
   * Class Distribution: $3\text{ Profit}, 0\text{ Loss}$ (Pure Subset!)
   * Entropy: $H(S_{\text{Up}}) = 0.0000\text{ bits}$

2. **Branch `Past Trend = Down` ($S_{\text{Down}}$):**
   * Records: X3, X4 (Total: $2$)
   * Class Distribution: $0\text{ Profit}, 2\text{ Loss}$ (Pure Subset!)
   * Entropy: $H(S_{\text{Down}}) = 0.0000\text{ bits}$

* **Weighted Partition Entropy ($H_{\text{Past Trend}}(S)$):**
  $$H_{\text{Past Trend}}(S) = \frac{3}{5}(0.0) + \frac{2}{5}(0.0) = \mathbf{0.0000\text{ bits}}$$

* **Information Gain ($\text{Gain}(S, \text{Past Trend})$):**
  $$\text{Gain}(S, \text{Past Trend}) = H(S) - H_{\text{Past Trend}}(S) = 0.9710 - 0.0000 = \mathbf{0.9710\text{ bits}}$$

---

###### **Candidate 2: `Open Interest` (Values: High, Low)**
1. **Branch `Open Interest = High` ($S_{\text{High}}$):**
   * Records: X1 (Profit), X2 (Profit), X4 (Loss) (Total: $3$)
   * Class Distribution: $2\text{ Profit}, 1\text{ Loss}$
   * Entropy: $H(S_{\text{High}}) = -\left(\frac{2}{3}\right)\log_2\left(\frac{2}{3}\right) - \left(\frac{1}{3}\right)\log_2\left(\frac{1}{3}\right) = \mathbf{0.9183\text{ bits}}$

2. **Branch `Open Interest = Low` ($S_{\text{Low}}$):**
   * Records: X3 (Loss), X5 (Profit) (Total: $2$)
   * Class Distribution: $1\text{ Profit}, 1\text{ Loss}$ (50/50 split)
   * Entropy: $H(S_{\text{Low}}) = \mathbf{1.0000\text{ bit}}$

* **Weighted Partition Entropy ($H_{\text{Open Interest}}(S)$):**
  $$H_{\text{Open Interest}}(S) = \frac{3}{5}(0.9183) + \frac{2}{5}(1.0000) = 0.5510 + 0.4000 = \mathbf{0.9510\text{ bits}}$$

* **Information Gain ($\text{Gain}(S, \text{Open Interest})$):**
  $$\text{Gain}(S, \text{Open Interest}) = 0.9710 - 0.9510 = \mathbf{0.0200\text{ bits}}$$

---

###### **Candidate 3: `Trading Volume` (Values: High, Low)**
1. **Branch `Trading Volume = High` ($S_{\text{Vol-High}}$):**
   * Records: X1 (Profit), X3 (Loss), X5 (Profit) (Total: $3$)
   * Class Distribution: $2\text{ Profit}, 1\text{ Loss}$
   * Entropy: $H(S_{\text{Vol-High}}) = \mathbf{0.9183\text{ bits}}$

2. **Branch `Trading Volume = Low` ($S_{\text{Vol-Low}}$):**
   * Records: X2 (Profit), X4 (Loss) (Total: $2$)
   * Class Distribution: $1\text{ Profit}, 1\text{ Loss}$
   * Entropy: $H(S_{\text{Vol-Low}}) = \mathbf{1.0000\text{ bit}}$

* **Weighted Partition Entropy & Information Gain:**
  $$H_{\text{Trading Volume}}(S) = \frac{3}{5}(0.9183) + \frac{2}{5}(1.0000) = \mathbf{0.9510\text{ bits}}$$
  $$\text{Gain}(S, \text{Trading Volume}) = 0.9710 - 0.9510 = \mathbf{0.0200\text{ bits}}$$

---

##### **Step 3: Root Selection & Decision Tree Construction**
Comparing Information Gains:
* $\text{Gain}(S, \text{Past Trend}) = \mathbf{0.9710\text{ bits}}$ (Maximum!)
* $\text{Gain}(S, \text{Open Interest}) = 0.0200\text{ bits}$
* $\text{Gain}(S, \text{Trading Volume}) = 0.0200\text{ bits}$

`Past Trend` splits the dataset into $100\%$ pure child nodes at Depth 1. Tree construction terminates immediately.

```text
                  [ Past Trend ]
                   /          \
                Up/            \Down
                 /              \
                v                v
            ( Profit )        ( Loss )
```

##### **Step 4: IF-THEN Rules**
* **Rule 1:** IF $(\text{Past Trend} = \text{Up})$ THEN $(\text{Return} = \text{Profit})$
* **Rule 2:** IF $(\text{Past Trend} = \text{Down})$ THEN $(\text{Return} = \text{Loss})$

---

### ✍️ **PROBLEM 3 (PAST-PAPER-STYLE NUMERICAL — SOURCE UNVERIFIED)**
#### **Attributed Source (unverified):** SVKM's NMIMS Final Examination 2022-23 (Q5.A) — reported as 10 Marks
> ⚠️ **Verification note:** The exact paper, question number, and marks could not be confirmed against an original NMIMS paper in this session. Treat this as a practice numerical until checked against the actual paper.

#### **1. Original Question Statement:**
Given the following dataset for student weekend activity selection (`Decision`), construct the decision tree using Information Gain.

> **Scope Note:** The original university question paper asked to compare Gini Index (CART) and Information Gain (ID3). As specified in this workbook's scope, the Gini/CART section is explicitly noted as outside scope, and the **ID3 / Information Gain decision tree induction is fully solved below**.

#### **2. Given Training Dataset:**

| Day | Weather | Parents | Money | Decision (Target) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | Sunny | Yes | Rich | **Cinema** |
| **2** | Sunny | No | Rich | **Tennis** |
| **3** | Windy | Yes | Rich | **Cinema** |
| **4** | Rainy | Yes | Poor | **Cinema** |
| **5** | Rainy | No | Rich | **Stay-In** |
| **6** | Rainy | Yes | Poor | **Cinema** |
| **7** | Windy | No | Poor | **Cinema** |
| **8** | Windy | Yes | Rich | **Cinema** |
| **9** | Windy | No | Rich | **Shopping** |
| **10** | Sunny | No | Rich | **Tennis** |

---

#### **3. Step-by-Step Solution Trace:**

##### **Step 1: Dataset Characterization & Parent Entropy $H(S)$**
* **Total Records ($|S|$):** $10$
* **Target Classes (4 distinct outcomes):** `Cinema` ($6$), `Tennis` ($2$), `Stay-In` ($1$), `Shopping` ($1$).
* **Class Probabilities:**
  $$p_{\text{Cinema}} = \frac{6}{10} = 0.6, \quad p_{\text{Tennis}} = \frac{2}{10} = 0.2, \quad p_{\text{Stay-In}} = \frac{1}{10} = 0.1, \quad p_{\text{Shopping}} = \frac{1}{10} = 0.1$$

* **Parent Entropy Calculation:**
  $$H(S) = -\sum p_i \log_2(p_i)$$
  $$H(S) = -\left[0.6\log_2(0.6) + 0.2\log_2(0.2) + 0.1\log_2(0.1) + 0.1\log_2(0.1)\right]$$
  $$\log_2(0.6) \approx -0.7370, \quad \log_2(0.2) \approx -2.3219, \quad \log_2(0.1) \approx -3.3219$$
  $$H(S) = -[ (0.6 \times -0.7370) + (0.2 \times -2.3219) + (0.1 \times -3.3219) + (0.1 \times -3.3219) ]$$
  $$H(S) = -[ -0.4422 - 0.4644 - 0.3322 - 0.3322 ] = \mathbf{1.5710\text{ bits}}$$

---

##### **Step 2: Candidate Attribute Evaluation**

###### **Candidate 1: `Weather` (Values: Sunny, Windy, Rainy)**
1. **`Weather = Sunny` ($S_{\text{Sunny}}$):** Days 1, 2, 10 (Total: $3$). Classes: $1\text{ Cinema}, 2\text{ Tennis}$.
   $$H(S_{\text{Sunny}}) = -\left(\frac{1}{3}\right)\log_2\left(\frac{1}{3}\right) - \left(\frac{2}{3}\right)\log_2\left(\frac{2}{3}\right) = \mathbf{0.9183\text{ bits}}$$

2. **`Weather = Windy` ($S_{\text{Windy}}$):** Days 3, 7, 8, 9 (Total: $4$). Classes: $3\text{ Cinema}, 1\text{ Shopping}$.
   $$H(S_{\text{Windy}}) = -\left(\frac{3}{4}\right)\log_2\left(\frac{3}{4}\right) - \left(\frac{1}{4}\right)\log_2\left(\frac{1}{4}\right) = \mathbf{0.8113\text{ bits}}$$

3. **`Weather = Rainy` ($S_{\text{Rainy}}$):** Days 4, 5, 6 (Total: $3$). Classes: $2\text{ Cinema}, 1\text{ Stay-In}$.
   $$H(S_{\text{Rainy}}) = -\left(\frac{2}{3}\right)\log_2\left(\frac{2}{3}\right) - \left(\frac{1}{3}\right)\log_2\left(\frac{1}{3}\right) = \mathbf{0.9183\text{ bits}}$$

* **Weighted Entropy & Information Gain:**
  $$H_{\text{Weather}}(S) = \frac{3}{10}(0.9183) + \frac{4}{10}(0.8113) + \frac{3}{10}(0.9183) = 0.2755 + 0.3245 + 0.2755 = \mathbf{0.8755\text{ bits}}$$
  $$\text{Gain}(S, \text{Weather}) = 1.5710 - 0.8755 = \mathbf{0.6955\text{ bits}}$$

---

###### **Candidate 2: `Parents` (Values: Yes, No)**
1. **`Parents = Yes` ($S_{\text{Yes}}$):** Days 1, 3, 4, 6, 8 (Total: $5$). Classes: $5\text{ Cinema}, 0\text{ Others}$ (Pure!).
   $$H(S_{\text{Yes}}) = \mathbf{0.0000\text{ bits}}$$

2. **`Parents = No` ($S_{\text{No}}$):** Days 2, 5, 7, 9, 10 (Total: $5$). Classes: $1\text{ Cinema}, 2\text{ Tennis}, 1\text{ Stay-In}, 1\text{ Shopping}$.
   $$H(S_{\text{No}}) = -\left[0.2\log_2(0.2) + 0.4\log_2(0.4) + 0.2\log_2(0.2) + 0.2\log_2(0.2)\right] = \mathbf{1.9219\text{ bits}}$$

* **Weighted Entropy & Information Gain:**
  $$H_{\text{Parents}}(S) = \frac{5}{10}(0.0) + \frac{5}{10}(1.9219) = \mathbf{0.9610\text{ bits}}$$
  $$\text{Gain}(S, \text{Parents}) = 1.5710 - 0.9610 = \mathbf{0.6100\text{ bits}}$$

---

###### **Candidate 3: `Money` (Values: Rich, Poor)**
1. **`Money = Rich` ($S_{\text{Rich}}$):** Days 1, 2, 3, 5, 8, 9, 10 (Total: $7$). Classes: $3\text{ Cinema}, 2\text{ Tennis}, 1\text{ Stay-In}, 1\text{ Shopping}$.
   $$H(S_{\text{Rich}}) = \mathbf{1.8424\text{ bits}}$$

2. **`Money = Poor` ($S_{\text{Poor}}$):** Days 4, 6, 7 (Total: $3$). Classes: $3\text{ Cinema}$ (Pure!).
   $$H(S_{\text{Poor}}) = \mathbf{0.0000\text{ bits}}$$

* **Weighted Entropy & Information Gain:**
  $$H_{\text{Money}}(S) = \frac{7}{10}(1.8424) + \frac{3}{10}(0.0) = \mathbf{1.2897\text{ bits}}$$
  $$\text{Gain}(S, \text{Money}) = 1.5710 - 1.2897 = \mathbf{0.2813\text{ bits}}$$

---

##### **Step 3: Root Selection & Decision Tree Construction**
Comparing Information Gains:
* $\text{Gain}(S, \text{Weather}) = \mathbf{0.6955\text{ bits}}$ (Maximum!)
* $\text{Gain}(S, \text{Parents}) = 0.6100\text{ bits}$
* $\text{Gain}(S, \text{Money}) = 0.2813\text{ bits}$

`Weather` is selected as the **Root Node**. Each impure child branch is now expanded by repeating the Information Gain calculation over the **remaining** candidate attributes (`Parents`, `Money`) restricted to that branch's records.

---

###### **Child Node 1: `Weather = Sunny`** (Days 1, 2, 10 — $1\text{ Cinema}, 2\text{ Tennis}$)
* $H(S_{\text{Sunny}}) = 0.9183\text{ bits}$ (already computed in Step 2).
* **Split on `Parents`:** `Yes` (Day 1) $\to 1\text{ Cinema}$ (pure, $H=0$); `No` (Days 2, 10) $\to 2\text{ Tennis}$ (pure, $H=0$).
  $$H_{\text{Parents}}(S_{\text{Sunny}}) = \tfrac{1}{3}(0) + \tfrac{2}{3}(0) = 0.0000, \quad \text{Gain} = 0.9183 - 0.0000 = \mathbf{0.9183\text{ bits}}$$
* **Split on `Money`:** all 3 Sunny records (Days 1, 2, 10) have `Money = Rich`, so the split has only one branch and cannot separate the classes.
  $$H_{\text{Money}}(S_{\text{Sunny}}) = 1 \times 0.9183 = 0.9183, \quad \text{Gain} = 0.9183 - 0.9183 = \mathbf{0.0000\text{ bits}}$$
* **Decision:** `Parents` wins ($0.9183 > 0.0000$) and yields two pure leaves.
  * `Parents = Yes` (Day 1) $\to$ **`Cinema`**
  * `Parents = No` (Days 2, 10) $\to$ **`Tennis`**

---

###### **Child Node 2: `Weather = Windy`** (Days 3, 7, 8, 9 — $3\text{ Cinema}, 1\text{ Shopping}$)
* $H(S_{\text{Windy}}) = 0.8113\text{ bits}$ (already computed in Step 2).
* **Split on `Parents`:** `Yes` (Days 3, 8) $\to 2\text{ Cinema}$ (pure, $H=0$); `No` (Days 7, 9) $\to 1\text{ Cinema}, 1\text{ Shopping}$ ($H=1.0000$).
  $$H_{\text{Parents}}(S_{\text{Windy}}) = \tfrac{2}{4}(0) + \tfrac{2}{4}(1.0000) = 0.5000, \quad \text{Gain} = 0.8113 - 0.5000 = \mathbf{0.3113\text{ bits}}$$
* **Split on `Money`:** `Rich` (Days 3, 8, 9) $\to 2\text{ Cinema}, 1\text{ Shopping}$ ($H = 0.9183$); `Poor` (Day 7) $\to 1\text{ Cinema}$ (pure, $H=0$).
  $$H_{\text{Money}}(S_{\text{Windy}}) = \tfrac{3}{4}(0.9183) + \tfrac{1}{4}(0) = 0.6887, \quad \text{Gain} = 0.8113 - 0.6887 = \mathbf{0.1226\text{ bits}}$$
* **Decision:** `Parents` wins ($0.3113 > 0.1226$).
  * `Parents = Yes` (Days 3, 8) $\to$ **`Cinema`**
  * `Parents = No` (Days 7, 9) $\to$ impure ($1\text{ Cinema}, 1\text{ Shopping}$); expand with the one remaining attribute, `Money`:
    * `Money = Rich` (Day 9) $\to$ **`Shopping`**
    * `Money = Poor` (Day 7) $\to$ **`Cinema`**
    * (Splitting this 2-record subset on `Money` gives $\text{Gain} = H([1,1]) - 0 = 1.0000\text{ bit}$ — a fully pure split, so no further expansion is needed.)

---

###### **Child Node 3: `Weather = Rainy`** (Days 4, 5, 6 — $2\text{ Cinema}, 1\text{ Stay-In}$)
* $H(S_{\text{Rainy}}) = 0.9183\text{ bits}$ (already computed in Step 2).
* **Split on `Parents`:** `Yes` (Days 4, 6) $\to 2\text{ Cinema}$ (pure, $H=0$); `No` (Day 5) $\to 1\text{ Stay-In}$ (pure, $H=0$).
  $$H_{\text{Parents}}(S_{\text{Rainy}}) = \tfrac{2}{3}(0) + \tfrac{1}{3}(0) = 0.0000, \quad \text{Gain} = 0.9183 - 0.0000 = \mathbf{0.9183\text{ bits}}$$
* **Split on `Money`:** all 3 Rainy records (Days 4, 5, 6) — Days 4 and 6 are `Poor`, Day 5 is `Rich`. `Poor` (Days 4, 6) $\to 2\text{ Cinema}$ (pure); `Rich` (Day 5) $\to 1\text{ Stay-In}$ (pure).
  $$H_{\text{Money}}(S_{\text{Rainy}}) = \tfrac{2}{3}(0) + \tfrac{1}{3}(0) = 0.0000, \quad \text{Gain} = \mathbf{0.9183\text{ bits}}$$
* **Decision:** `Parents` and `Money` are **tied** at $0.9183\text{ bits}$ (both give a fully pure 2/1 split on this subset). Either attribute produces an identical tree; this workbook selects `Parents` for consistency with the other two branches.
  * `Parents = Yes` (Days 4, 6) $\to$ **`Cinema`**
  * `Parents = No` (Day 5) $\to$ **`Stay-In`**

```text
                        [ Weather ]
                       /     |     \
               Sunny  /      |      \ Rainy
                     /     Windy     \
                    v        v        v
               [Parents]  [Parents]  [Parents]
                /     \    /     \    /     \
             Yes|   No| Yes|   No| Yes|   No|
                v     v    v     v    v     v
             (Cin) (Ten)(Cin) [Money](Cin) (Stay-In)
                              /   \
                         Rich/     \Poor
                            v       v
                          (Shop)  (Cin)
```

---

## SECTION 3: PRACTICE PROBLEMS & EXTENSIVE BENCHMARKS

---

### ✍️ **PROBLEM 4 (PRACTICE PROBLEM — CLASSIC 14-DAY PLAYTENNIS BENCHMARK)**

#### **1. Training Dataset:**

| Day | Outlook | Temperature | Humidity | Wind | PlayTennis (Target) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **D1** | Sunny | Hot | High | Weak | **No** |
| **D2** | Sunny | Hot | High | Strong | **No** |
| **D3** | Overcast | Hot | High | Weak | **Yes** |
| **D4** | Rain | Mild | High | Weak | **Yes** |
| **D5** | Rain | Cool | Normal | Weak | **Yes** |
| **D6** | Rain | Cool | Normal | Strong | **No** |
| **D7** | Overcast | Cool | Normal | Strong | **Yes** |
| **D8** | Sunny | Mild | High | Weak | **No** |
| **D9** | Sunny | Cool | Normal | Weak | **Yes** |
| **D10** | Rain | Mild | Normal | Weak | **Yes** |
| **D11** | Sunny | Mild | Normal | Strong | **Yes** |
| **D12** | Overcast | Mild | High | Strong | **Yes** |
| **D13** | Overcast | Hot | Normal | Weak | **Yes** |
| **D14** | Rain | Mild | High | Strong | **No** |

---

#### **2. Complete Solution Trace:**

##### **Step 1: Parent Entropy $H(S)$**
* $|S| = 14$, Positive (`Yes`): $9$, Negative (`No`): $5$.
* $H(S) = -\left(\frac{9}{14}\right)\log_2\left(\frac{9}{14}\right) - \left(\frac{5}{14}\right)\log_2\left(\frac{5}{14}\right) = \mathbf{0.9403\text{ bits}}$.

##### **Step 2: Information Gain Calculations for All Root Candidate Attributes**

###### **Candidate 1: `Outlook` (Values: Sunny, Overcast, Rain)**
1. `Outlook = Sunny` (D1, D2, D8, D9, D11 — Total $5$): $2\text{ Yes}, 3\text{ No}$.
   $$H(S_{\text{Sunny}}) = -\left(\tfrac{2}{5}\right)\log_2\left(\tfrac{2}{5}\right) - \left(\tfrac{3}{5}\right)\log_2\left(\tfrac{3}{5}\right) = \mathbf{0.9710\text{ bits}}$$
2. `Outlook = Overcast` (D3, D7, D12, D13 — Total $4$): $4\text{ Yes}, 0\text{ No}$ (Pure). $H(S_{\text{Overcast}}) = \mathbf{0.0000\text{ bits}}$
3. `Outlook = Rain` (D4, D5, D6, D10, D14 — Total $5$): $3\text{ Yes}, 2\text{ No}$. $H(S_{\text{Rain}}) = \mathbf{0.9710\text{ bits}}$

* **Weighted Entropy & Gain:**
  $$H_{\text{Outlook}}(S) = \tfrac{5}{14}(0.9710) + \tfrac{4}{14}(0.0000) + \tfrac{5}{14}(0.9710) = 0.3468 + 0 + 0.3468 = \mathbf{0.6936\text{ bits}}$$
  $$\text{Gain}(S, \text{Outlook}) = 0.9403 - 0.6936 = \mathbf{0.2467\text{ bits}}$$

###### **Candidate 2: `Temperature` (Values: Hot, Mild, Cool)**
1. `Hot` (D1, D2, D3, D13 — Total $4$): $2\text{ Yes}, 2\text{ No}$ (50/50). $H(S_{\text{Hot}}) = \mathbf{1.0000\text{ bit}}$
2. `Mild` (D4, D8, D10, D11, D12, D14 — Total $6$): $4\text{ Yes}, 2\text{ No}$. $H(S_{\text{Mild}}) = \mathbf{0.9183\text{ bits}}$
3. `Cool` (D5, D6, D7, D9 — Total $4$): $3\text{ Yes}, 1\text{ No}$. $H(S_{\text{Cool}}) = \mathbf{0.8113\text{ bits}}$

* **Weighted Entropy & Gain:**
  $$H_{\text{Temperature}}(S) = \tfrac{4}{14}(1.0000) + \tfrac{6}{14}(0.9183) + \tfrac{4}{14}(0.8113) = 0.2857 + 0.3936 + 0.2318 = \mathbf{0.9111\text{ bits}}$$
  $$\text{Gain}(S, \text{Temperature}) = 0.9403 - 0.9111 = \mathbf{0.0292\text{ bits}}$$

###### **Candidate 3: `Humidity` (Values: High, Normal)**
1. `High` (D1, D2, D3, D4, D8, D12, D14 — Total $7$): $3\text{ Yes}, 4\text{ No}$. $H(S_{\text{High}}) = \mathbf{0.9852\text{ bits}}$
2. `Normal` (D5, D6, D7, D9, D10, D11, D13 — Total $7$): $6\text{ Yes}, 1\text{ No}$. $H(S_{\text{Normal}}) = \mathbf{0.5917\text{ bits}}$

* **Weighted Entropy & Gain:**
  $$H_{\text{Humidity}}(S) = \tfrac{7}{14}(0.9852) + \tfrac{7}{14}(0.5917) = 0.4926 + 0.2959 = \mathbf{0.7884\text{ bits}}$$
  $$\text{Gain}(S, \text{Humidity}) = 0.9403 - 0.7884 = \mathbf{0.1518\text{ bits}}$$

###### **Candidate 4: `Wind` (Values: Weak, Strong)**
1. `Weak` (D1, D3, D4, D5, D8, D9, D10, D13 — Total $8$): $6\text{ Yes}, 2\text{ No}$. $H(S_{\text{Weak}}) = \mathbf{0.8113\text{ bits}}$
2. `Strong` (D2, D6, D7, D11, D12, D14 — Total $6$): $3\text{ Yes}, 3\text{ No}$ (50/50). $H(S_{\text{Strong}}) = \mathbf{1.0000\text{ bit}}$

* **Weighted Entropy & Gain:**
  $$H_{\text{Wind}}(S) = \tfrac{8}{14}(0.8113) + \tfrac{6}{14}(1.0000) = 0.4636 + 0.4286 = \mathbf{0.8922\text{ bits}}$$
  $$\text{Gain}(S, \text{Wind}) = 0.9403 - 0.8922 = \mathbf{0.0481\text{ bits}}$$

##### **Step 3: Root Selection & Sub-tree Expansion**
Comparing all four gains — `Outlook` ($0.2467$), `Humidity` ($0.1518$), `Wind` ($0.0481$), `Temperature` ($0.0292$) — `Outlook` is selected as Root Node.

* **`Outlook = Overcast`** is already pure ($4\text{ Yes}$) — no expansion needed.
* **`Outlook = Sunny`** (D1, D2, D8, D9, D11 — $2\text{ Yes}, 3\text{ No}$) is impure. Evaluating the remaining candidates on this subset:
  * `Humidity`: `High` (D1, D2, D8) $\to 0\text{ Yes}, 3\text{ No}$ (pure); `Normal` (D9, D11) $\to 2\text{ Yes}, 0\text{ No}$ (pure). $H_{\text{Humidity}} = 0$, so $\text{Gain} = 0.9710 - 0 = \mathbf{0.9710}$.
  * `Temperature`: gives $\text{Gain} = \mathbf{0.5710}$ (mixed, not pure).
  * `Wind`: `Weak` (D1, D8, D9) $\to 1\text{ Yes}, 2\text{ No}$; `Strong` (D2, D11) $\to 1\text{ Yes}, 1\text{ No}$. $\text{Gain} = \mathbf{0.0200}$.
  * **`Humidity` wins** ($0.9710$, fully pure) → `High` $\to$ **No**, `Normal` $\to$ **Yes**.
* **`Outlook = Rain`** (D4, D5, D6, D10, D14 — $3\text{ Yes}, 2\text{ No}$) is impure. Evaluating the remaining candidates:
  * `Wind`: `Weak` (D4, D5, D10) $\to 3\text{ Yes}, 0\text{ No}$ (pure); `Strong` (D6, D14) $\to 0\text{ Yes}, 2\text{ No}$ (pure). $H_{\text{Wind}} = 0$, so $\text{Gain} = 0.9710 - 0 = \mathbf{0.9710}$.
  * `Humidity`: gives $\text{Gain} = \mathbf{0.0200}$ (mixed, not pure).
  * `Temperature`: gives $\text{Gain} = \mathbf{0.0200}$ (mixed, not pure).
  * **`Wind` wins** ($0.9710$, fully pure) → `Weak` $\to$ **Yes**, `Strong` $\to$ **No**.

##### **Step 4: Decision Tree Structure**
`Outlook` is selected as Root Node ($\text{Gain} = 0.2467$); `Humidity` and `Wind` complete Depth 2 as shown above.

```text
                     [ Outlook ]
                   /      |      \
           Sunny  /   Overcast    \ Rain
                 /        |        \
                v         v         v
           [Humidity]  ( Yes )   [ Wind ]
            /      \              /    \
      High /        \Normal Weak /      \Strong
          v          v          v        v
        ( No )    ( Yes )    ( Yes )   ( No )
```

##### **Step 4: IF-THEN Rules**
1. IF $(\text{Outlook} = \text{Sunny})$ AND $(\text{Humidity} = \text{High})$ THEN $(\text{PlayTennis} = \text{No})$
2. IF $(\text{Outlook} = \text{Sunny})$ AND $(\text{Humidity} = \text{Normal})$ THEN $(\text{PlayTennis} = \text{Yes})$
3. IF $(\text{Outlook} = \text{Overcast})$ THEN $(\text{PlayTennis} = \text{Yes})$
4. IF $(\text{Outlook} = \text{Rain})$ AND $(\text{Wind} = \text{Weak})$ THEN $(\text{PlayTennis} = \text{Yes})$
5. IF $(\text{Outlook} = \text{Rain})$ AND $(\text{Wind} = \text{Strong})$ THEN $(\text{PlayTennis} = \text{No})$

---

### ✍️ **PROBLEM 5 (PRACTICE PROBLEM — INCONSISTENT FEATURE CONFLICT RESOLUTION)**

#### **1. Problem Statement:**
Demonstrate how the ID3 algorithm handles a training set containing **feature conflicts** (identical attribute values with contradictory target labels).

#### **2. Given Training Dataset:**

| Record | Credit History | Income Level | Loan Approved (Target) |
| :---: | :---: | :---: | :---: |
| **R1** | Good | High | **Yes** |
| **R2** | Good | High | **No** |

#### **3. Analytical Solution & Protocol:**
1. **Conflict Detection:**
   Both R1 and R2 possess identical feature vectors $X = (\text{Credit History} = \text{Good}, \text{Income Level} = \text{High})$, but R1 carries label `Yes` while R2 carries label `No`.
2. **Algorithmic Result:**
   * Attribute `Credit History` has 1 value (`Good`), yielding $H = 1.0\text{ bit}$ and $\text{Gain} = 0.0\text{ bits}$.
   * Attribute `Income Level` has 1 value (`High`), yielding $H = 1.0\text{ bit}$ and $\text{Gain} = 0.0\text{ bits}$.
   * No candidate attributes remain to split the dataset, but the node is impure ($1\text{ Yes}, 1\text{ No}$).
3. **Explicit Handling:**
   * **Flag Conflict:** State explicitly that **no deterministic decision tree can achieve $100\%$ training accuracy** on inconsistent data.
   * **Report the distribution:** $P(\text{Yes}) = 0.5, P(\text{No}) = 0.5$. This is the fully informative answer and should always be reported alongside any single-label prediction.
   * **Deterministic tie-breaker (if the question demands one single-class leaf):** When a stopping condition produces an exact tie and no parent-majority or global-majority class exists to break it (as here, with only these two records in the dataset), apply the following fixed rule, in order, and state which rule you used:
     1. **Global parent majority** — if the immediate parent node (or the full dataset, if this is the root) has an overall majority class, assign that class. *(Not applicable here — the parent dataset is these same two tied records.)*
     2. **First-encountered record** — if no majority exists at any ancestor level, assign the class of the **first record in the original dataset listing** (here, R1 $\to$ `Yes`). This rule is arbitrary but deterministic and reproducible, which is what matters for exam grading.
   * Applying rule 2: **Leaf Node = `Yes`** (from R1), with an explicit note that this is a **tie-break default**, not a genuine pattern in the data, and that $P(\text{Yes}) = P(\text{No}) = 0.5$ should still be quoted if the question asks for confidence or probability.

---

## SECTION 4: ALL SOLVED ID3 NUMERICALS — SUMMARY TABLE

| Problem ID | Attributed Source (unverified unless noted) | Dataset Size | Primary Root Attribute | Max Info Gain | Depth | Key Features |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Problem 1** | NMIMS Re-Exam 24-25 / Final 24-25, reported 15M — *unverified* | 12 rows | `Income` | $0.7503\text{ bits}$ | Depth 2 | 4-way split, predictor tracing |
| **Problem 2** | NMIMS B.Tech AI Final 25-26, reported 15M — *unverified* | 5 rows | `Past Trend` | $0.9710\text{ bits}$ | Depth 1 | $100\%$ pure root split |
| **Problem 3** | NMIMS Final Exam 22-23, reported 10M — *unverified* | 10 rows | `Weather` | $0.6955\text{ bits}$ | Depth 3 | Multi-class target ($4$ outcomes), tie at Rainy node |
| **Problem 4** | Classic benchmark practice problem (not NMIMS-specific) | 14 rows | `Outlook` | $0.2467\text{ bits}$ | Depth 2 | 14-day PlayTennis standard, full sub-node work shown |
| **Problem 5** | Constructed practice example (not NMIMS-specific) | 2 rows | None | $0.0000\text{ bits}$ | Depth 0 | Inconsistent label handling, explicit tie-break rule |

> All figures above were recalculated independently from each problem's own training table and are internally verified. Only the **exam attribution** (paper, year, question number, marks) for Problems 1–3 is unverified — see the note under each problem.

---

## SECTION 5: COMMON NUMERICAL QUESTION PATTERNS (HEURISTIC, NOT AN AUDITED STATISTIC)

> ⚠️ **Note:** The three patterns below are general heuristics for how ID3 numericals tend to be structured in typical exam settings, drawn from the shape of Problems 1–5 in this workbook. They are **not** derived from a statistical audit of actual NMIMS papers, and the "frequency" language here is a rough qualitative impression, not a measured count. Use these as a study checklist, not as a claim about how often each pattern appears on any specific paper.

1. **Pattern 1: High-Gain Root Split (Depth 1 Termination)**
   * *Characteristics:* 5 to 6 records where one binary attribute perfectly aligns with the target (see Problem 2).
   * *Typical setting:* Tends to appear in shorter, lower-mark questions, since the tree terminates after one split.
   * *Key Check:* Verify if any candidate attribute yields $H_A(S) = 0.0$.

2. **Pattern 2: Multi-Level Recursive Tree Construction (Depth 2–3)**
   * *Characteristics:* 10 to 14 records with 2–3 candidate attributes. Requires parent entropy, root split, and at least one sub-node calculation (see Problems 1, 3, 4).
   * *Typical setting:* Tends to appear in longer, higher-mark questions, since more work is required.

3. **Pattern 3: Predictor Tracing & Rule Generation**
   * *Characteristics:* Includes a final sub-question asking to classify a new test instance or extract IF-THEN rules (see Problem 1, Step 7).
   * *Exam Strategy:* Traverse from root node down branches matching the test vector.

---

## SECTION 6: QUICK SOLVING PROCEDURE (EXAM PROTOCOL)

When solving a decision tree numerical in an exam, execute these 6 steps sequentially:

```text
[Step 1: Characterize Dataset] ──> Count total rows |S| and class frequencies (p, n)
              │
              v
[Step 2: Parent Entropy H(S)] ──> Apply -p+ log2(p+) - p- log2(p-)
              │
              v
[Step 3: Attribute Gains]     ──> For EVERY candidate attribute:
                                  1. Group records by attribute value
                                  2. Calculate child entropies H(Sv)
                                  3. Calculate weighted entropy HA(S)
                                  4. Compute Gain(S, A) = H(S) - HA(S)
              │
              v
[Step 4: Select Root Split]   ──> Pick A* = argmax Gain(S, A)
              │
              v
[Step 5: Expand Impure Nodes] ──> Repeat Gain calculations for non-pure child branches
              │
              v
[Step 6: Output Deliverables] ──> Draw tree diagram, write IF-THEN rules, trace test record
```

---

## SECTION 7: TOP 6 COMMON CALCULATION PITFALLS (`⚠️ COMMON MISTAKES`)

1. ⚠️ **Mixing Base-10 and Base-2 Logs:**  
   Always use base-2 logarithms ($\log_2$). If using a standard calculator, divide $\log_{10}(x)$ by $0.30103$.
2. ⚠️ **Forgetting Node Weights in $H_A(S)$:**  
   Multiply each child entropy $H(S_v)$ by its node weight $\frac{|S_v|}{|S|}$ before summing.
3. ⚠️ **Sign Errors in Entropy:**  
   Entropy is always non-negative ($H(S) \ge 0$). A negative entropy value indicates a sign error in $-\sum p_i \log_2(p_i)$.
4. ⚠️ **Calculating Gain for Pure Child Nodes:**  
   If a child partition is pure ($100\%$ Class A), its entropy is instantly $0.0\text{ bits}$. Do not waste time computing $\log_2$ for pure branches!
5. ⚠️ **Re-evaluating Used Attributes:**  
   Once an attribute is used at a parent node, it cannot be reused along the same downstream path in ID3.
6. ⚠️ **Inconsistent IF-THEN Rules:**  
   Every path from the root node to a leaf node forms exactly ONE rule. Ensure all conditions along the path are joined by `AND`.

---

## SECTION 8: LAST-MINUTE EXAM CHECKLIST

- [ ] Can you calculate base-2 logarithms quickly using $\log_2(x) = \frac{\log_{10}(x)}{0.30103}$?
- [ ] Do you remember the binary entropy values for $50/50$ ($1.0$), $66/33$ ($0.9183$), $75/25$ ($0.8113$), and $80/20$ ($0.7219$)?
- [ ] Are you showing intermediate calculations for EVERY candidate attribute (not just the winner)?
- [ ] Are all pure branches terminating at Leaf Nodes?
- [ ] Is every root-to-leaf path represented as an IF-THEN rule?
- [ ] Have you tested your final decision tree against the training table for $100\%$ consistency?

---

## SECTION 9: SYLLABUS & NUMERICAL COVERAGE CHECKLIST

- [x] **Class probability and Parent Entropy $H(S)$**
- [x] **Weighted Partition Entropy $H_A(S)$ and Information Gain $\text{Gain}(S, A)$**
- [x] **ID3 Maximum Information Gain root selection**
- [x] **Top-down recursive dataset partitioning**
- [x] **Tree diagrams in clean GFM text format**
- [x] **IF-THEN rule extraction from root-to-leaf paths**
- [x] **Classification prediction for new test records**
- [x] **Handling empty branches, class ties, and inconsistent feature conflicts**
- [x] **Complete step-by-step mathematical trace for all worked numericals, including every impure sub-node**
