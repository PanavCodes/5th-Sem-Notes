# ARTIFICIAL INTELLIGENCE (AI) — UNIT 5: LEARNING (UP TO DECISION TREES)
## PAST YEAR QUESTION (PYQ) & EXAM-ORIENTED STUDY BANK
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## DOCUMENT OVERVIEW

This document is a Past Year Question (PYQ)-style practice bank for **Artificial Intelligence (AI) — Unit 5: Learning (Up to Decision Trees)**, covering Inductive Learning, the three ML paradigms, Decision Tree anatomy, the ID3 algorithm, and Entropy/Information Gain calculations.

> ⚠️ **Provenance Disclaimer:** The exam years, question numbers, marks, and "repeated/grouped" labels attached to questions below (and the Topic Weightage & Question Frequency table) **have not been verified against original Unit 5 question papers**. Treat every problem here as a **practice numerical in PYQ format**, not a confirmed past-paper citation, until checked against the actual papers.

### Unit 5 Topic Weightage & Question Frequency (Unverified — see disclaimer above)

| Topic ID | Topic Name | Exam Marks Range | Question Frequency | Primary Question Types |
| :---: | :--- | :---: | :---: | :--- |
| **Topic 1** | Inductive Learning & Machine Learning Paradigms | 5–10 Marks | High | Comparative tables (Supervised vs. Unsupervised vs. RL), definitions, inductive bias. |
| **Topic 2** | Supervised Learning & Decision Tree Anatomy | 5 Marks | High | Component definitions (root, internal decision nodes, branches, leaves), prediction mechanics. |
| **Topic 3** | ID3 Algorithm & Tree Induction | 5–10 Marks | Very High | Algorithm working steps, pseudocode, stopping conditions, greedy heuristic selection. |
| **Topic 4** | Entropy & Information Gain Mathematical Foundations | 5 Marks | Very High | Mathematical definitions, base-2 logarithm formulas, weighted average partition entropy. |
| **Topic 5** | Solved Numerical PYQs & Rule Extraction | 10–15 Marks | High | Full ID3 calculations, Information Gain tracing, decision tree drawing, IF-THEN rule extraction. |

---

## SECTION 1: TOPIC-WISE PAST YEAR QUESTIONS & MODEL ANSWERS

---

### TOPIC 1: INDUCTIVE LEARNING & MACHINE LEARNING PARADIGMS

#### **1.1 Practice Questions**

* **Question 1.1a:**
  *"What is Inductive Learning? Explain learning from examples. Differentiate between Supervised, Unsupervised, and Reinforcement Learning with suitable real-world examples."* [10 Marks]

* **Question 1.1b:**
  *"Define learning in AI. Explain how a learning agent improves its performance through experience. Compare supervised and unsupervised learning paradigms."* [5 Marks]

---

#### **Model Answer 1.1: Inductive Learning & Paradigm Comparison**

##### **1. Definition of Inductive Learning**
**Inductive Learning** (or learning from examples) is the process of acquiring general rules or predictive functions from a finite set of specific observed training instances.
Formally, given a training set of pairs:
$$D = \{(x_1, y_1), (x_2, y_2), \dots, (x_N, y_N)\}$$
where $x_i \in X$ represents the input feature vector and $y_i = f(x_i)$ represents the target output value, the learning agent constructs a **hypothesis function** $h(x) \in H$ such that:
$$h(x_i) \approx f(x_i) \quad \forall i \in \{1, \dots, N\}$$
The fundamental goal of inductive learning is **generalization** — ensuring that $h(x)$ accurately predicts the target value $y$ for previously unseen feature vectors $x \notin D$.

##### **2. Inductive Bias (`🧠 MUST UNDERSTAND`)**
An inductive learning agent cannot generalize beyond the training set without making prior assumptions about the target function $f$. The set of assumptions that the learner uses to predict outputs for unseen inputs is called the **Inductive Bias**.
* **ID3 Decision Tree Bias:** Prefers shorter, simpler trees over longer trees (Occam's Razor) and prefers trees that place attributes with high Information Gain closer to the root.

##### **3. Comparative Matrix: Supervised, Unsupervised, and Reinforcement Learning**

| Dimension / Feature | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
| :--- | :--- | :--- | :--- |
| **Input Data Format** | Labeled pairs $(x_i, y_i)$ containing features and ground-truth target outputs. | Unlabeled features $x_i$ without target outputs or supervisor labels. | Environmental state observations $s_t$, actions $a_t$, and scalar rewards $r_t$. |
| **Learning Goal** | Learn a mapping function $h: X \to Y$ to predict $y$ for new inputs. | Discover underlying structures, patterns, distributions, or groupings in data. | Learn an optimal action-selection policy $\pi(s)$ to maximize cumulative long-term reward. |
| **Feedback Mechanism** | Immediate, direct error correction based on known target label $y_i$. | None (evaluates intrinsic mathematical metrics like cluster distance). | Delayed reward or penalty signal $r_t$ received from the environment after action execution. |
| **Primary Tasks** | Classification (discrete output) and Regression (continuous output). | Clustering (K-Means, Hierarchical), Dimensionality Reduction, Anomaly Detection. | Game playing (Chess, Go), Robot navigation, Autonomous vehicle control. |
| **Canonical Algorithms** | Decision Trees (ID3/C4.5), Naïve Bayes, Support Vector Machines (SVM), Linear Regression. | K-Means Clustering, Principal Component Analysis (PCA), Expectation-Maximization (EM). | Q-Learning, Deep Q-Networks (DQN), Policy Gradient methods. |
| **Real-World Example** | Email spam classification (Spam vs. Not Spam based on text features). | Customer market-segmentation based on purchasing history. | Training an autonomous agent to balance a pole or play Atari games. |

---

### TOPIC 2: SUPERVISED LEARNING & DECISION TREE ANATOMY

#### **2.1 Practice Question**

* **Question 2.1a:**
  *"Explain the structure and components of a Decision Tree classifier. How does a decision tree classify an unseen test record?"* [5 Marks]

---

#### **Model Answer 2.1: Structural Components & Prediction Mechanics**

##### **1. Anatomical Components of a Decision Tree**
A **Decision Tree** is a hierarchical, non-parametric flowchart structure used for classification and regression tasks. It partitions the feature space into axis-aligned regions through a series of recursive conditional tests.

```text
                     ┌────────────────────────┐
                     │       ROOT NODE        │  ◄── Full Dataset
                     │  (Highest Info Gain)   │      (Tests First Attribute)
                     └───────────┬────────────┘
                                 │
                     ┌───────────┴────────────┐
                     │         BRANCH         │  ◄── Attribute Value Split
                     └───────────┬────────────┘
                                 │
                     ┌───────────▼────────────┐
                     │ INTERNAL DECISION NODE │  ◄── Tests Next Attribute
                     └───────────┬────────────┘
                                 │
                     ┌───────────┴────────────┐
                     │         BRANCH         │
                     └───────────┬────────────┘
                                 │
                     ┌───────────▼────────────┐
                     │       LEAF NODE        │  ◄── Final Class Label
                     └────────────────────────┘
```

1. **Root Node:** The topmost node, representing the entire dataset. It tests the single most informative attribute selected via a statistical criterion (e.g., Information Gain).
2. **Internal Decision Nodes:** Intermediate nodes that test specific feature values ($A_i = v_{i,k}$). Each internal node branches into two or more child nodes based on attribute values.
3. **Branches (Edges):** Outcome paths representing specific attribute-value assignments resulting from a parent node test.
4. **Leaf Nodes (Terminal Nodes):** End nodes with no further splits. A leaf node stores the final **Class Label** assigned to all training instances reaching that terminal state.

##### **2. Test Example Classification Procedure**
To classify an unseen input record $x_{\text{test}} = (A_1 = v_1, A_2 = v_2, \dots, A_m = v_m)$:
1. Start at the **Root Node**.
2. Evaluate the attribute condition specified by the node for $x_{\text{test}}$.
3. Follow the matching **Branch** corresponding to the value of that attribute in $x_{\text{test}}$.
4. Repeat steps 2–3 recursively at each internal decision node until a **Leaf Node** is reached.
5. Assign the class label stored at the leaf node as the final prediction for $x_{\text{test}}$.

---

### TOPIC 3: ID3 ALGORITHM & TREE CONSTRUCTION

#### **3.1 Practice Question**

* **Question 3.1a:**
  *"Write the complete ID3 algorithm for Decision Tree Induction. Explain its stopping conditions and attribute selection mechanism."* [5–7 Marks]

---

#### **Model Answer 3.1: The ID3 Induction Algorithm**

##### **1. Core Principles of ID3**
The **ID3 (Iterative Dichotomiser 3)** algorithm, developed by Ross Quinlan, constructs a decision tree top-down using a greedy heuristic search through the space of possible trees. At each step, ID3 evaluates all candidate attributes using **Information Gain** and selects the single attribute that best separates the training instances into pure class subsets.

##### **2. ID3 Pseudocode**

```text
Algorithm ID3(Examples, Target_Attribute, Attributes):
    // Examples: Set of training instances
    // Target_Attribute: The class label to be predicted
    // Attributes: Set of candidate predictor attributes

    Create a Root node for the tree

    // Base Case 1: All examples belong to the same class (Pure Node)
    If all Examples have the same Target_Attribute value c:
        Return a single leaf node Root with label = c

    // Base Case 2: No attributes remaining to split on
    If Attributes is empty:
        Return a single leaf node Root with label = Most_Common_Value(Target_Attribute, Examples)

    // Step 1: Select Best Attribute using Information Gain
    A_best = Attribute_With_Max_Information_Gain(Examples, Target_Attribute, Attributes)
    Set Root.decision_attribute = A_best

    // Step 2: Recursively grow child trees for each value of A_best
    For each possible value v of A_best:
        Add a new branch below Root corresponding to test (A_best = v)
        Examples_v = Subset of Examples where A_best = v

        // Base Case 3: Empty subset branch
        If Examples_v is empty:
            Add a leaf node with label = Most_Common_Value(Target_Attribute, Examples)
        Else:
            Add the subtree returned by ID3(Examples_v, Target_Attribute, Attributes \ {A_best})

    Return Root
```

##### **3. The Three Base-Case Stopping Conditions (`⭐ MUST REMEMBER`)**
1. **Pure Dataset:** All training instances at the current node belong to the exact same target class $c$. (Create a leaf node labeled $c$).
2. **Exhausted Attributes:** The set of remaining candidate attributes is empty, but instances have mixed classes. (Create a leaf node labeled with the majority class at the current node).
3. **Empty Subset:** A specific branch value $A_{\text{best}} = v$ yields no training instances ($\text{Examples}_v = \emptyset$). (Create a leaf node labeled with the parent dataset's majority class).

---

### TOPIC 4: MATHEMATICAL FOUNDATIONS (ENTROPY & INFORMATION GAIN)

#### **4.1 Practice Question**

* **Question 4.1a:**
  *"Define Entropy and Information Gain mathematically. Explain how Information Gain is used by ID3 to select the root node of a decision tree."* [5 Marks]

---

#### **Model Answer 4.1: Mathematical Formulas & Symbols**

##### **1. Entropy (Class Impurity / Uncertainty)**
**Entropy** measures the degree of impurity or randomness in a training dataset $S$ relative to a target classification. For a multi-class target variable with $C$ discrete classes:

$$H(S) = - \sum_{i=1}^{C} p_i \log_2(p_i)$$

where $p_i$ is the proportion of training instances in $S$ belonging to target class $i$.

* **Binary Classification Special Case ($C=2$, e.g., Positive $p_+$ and Negative $p_-$):**
  $$H(S) = - p_+ \log_2(p_+) - p_- \log_2(p_-)$$
* **Pure Node Boundary Condition:** If $p_+=1$ and $p_-=0$, then $H(S) = -1\log_2(1) - 0 = 0.0 \text{ bits}$ (minimum entropy / maximum certainty).
* **Equally Impure Node Boundary Condition:** If $p_+=0.5$ and $p_-=0.5$, then $H(S) = -0.5\log_2(0.5) - 0.5\log_2(0.5) = 1.0 \text{ bit}$ (maximum entropy / complete uncertainty).

##### **2. Weighted Average Partition Entropy**
When an attribute $A$ with $K$ distinct values $\{v_1, v_2, \dots, v_K\}$ is used to split dataset $S$, it partitions $S$ into $K$ subsets $\{S_{v_1}, S_{v_2}, \dots, S_{v_K}\}$. The expected remaining entropy after the split is the weighted average of subset entropies:

$$H_A(S) = \sum_{k=1}^{K} \frac{|S_{v_k}|}{|S|} H(S_{v_k})$$

where $|S_{v_k}|$ is the number of instances in subset $S_{v_k}$, and $|S|$ is the total number of instances in parent dataset $S$.

##### **3. Information Gain (Entropy Reduction)**
**Information Gain** $\text{Gain}(S, A)$ is the expected reduction in entropy achieved by partitioning dataset $S$ according to candidate attribute $A$:

$$\text{Gain}(S, A) = H(S) - H_A(S) = H(S) - \sum_{k=1}^{K} \frac{|S_{v_k}|}{|S|} H(S_{v_k})$$

ID3 evaluates $\text{Gain}(S, A)$ for all candidate attributes $A \in \text{Attributes}$ and selects the attribute $A^*$ that maximizes Information Gain:
$$A^* = \arg\max_{A} \text{Gain}(S, A)$$

---

## SECTION 2: SOLVED PAST YEAR NUMERICAL QUESTIONS (STEP-BY-STEP)

---

### ✍️ **SOLVED PYQ 1: 12-INSTANCE HOUSE OWNERSHIP DATASET** [15 Marks]

* **Question Wording:**
  *"Given the following training dataset for predicting house ownership ('Own House' target class with values 'Yes' and 'Rented'), construct a decision tree using the ID3 algorithm. Calculate parent entropy, information gain for candidate attributes 'Income' and 'Age', draw the completed decision tree, extract IF-THEN rules, and classify a new instance: (Income = Medium, Age = Old)."*

#### **Given Training Dataset (Table 5.1):**

| Instance ID | Income | Age | Own House (Target Class) |
| :---: | :---: | :---: | :---: |
| **1** | Very High | Young | Yes |
| **2** | High | Medium | Yes |
| **3** | Low | Young | Rented |
| **4** | High | Medium | Yes |
| **5** | Very High | Medium | Yes |
| **6** | Low | Medium | Rented |
| **7** | High | Old | Yes |
| **8** | Medium | Young | Yes |
| **9** | Medium | Young | Rented |
| **10** | Low | Old | Rented |
| **11** | Medium | Medium | Rented |
| **12** | High | Old | Yes |

> ⚠️ **Data Note:** Instances **8** and **9** have identical attribute values (`Income = Medium, Age = Young`) but opposite class labels. With only `Income` and `Age` as candidate attributes, no split can separate these two rows — see Step 4 below.

---

#### **Step-by-Step Mathematical Solution:**

##### **Step 1: Total Class Counts and Parent Dataset Entropy $H(D)$**
* Total training instances $|D| = 12$.
* Target Class `Own House` frequency breakdown:
  * `Yes` count = $7$ (Instances 1, 2, 4, 5, 7, 8, 12)
  * `Rented` count = $5$ (Instances 3, 6, 9, 10, 11)
* Class probabilities:
  * $p_{\text{Yes}} = \frac{7}{12} \approx 0.5833$
  * $p_{\text{Rented}} = \frac{5}{12} \approx 0.4167$

$$H(D) = - \left( \frac{7}{12} \log_2 \frac{7}{12} + \frac{5}{12} \log_2 \frac{5}{12} \right) = -(0.5833 \times (-0.7776) + 0.4167 \times (-1.2630)) = 0.4536 + 0.5263 = \mathbf{0.9799 \text{ bits}}$$

---

##### **Step 2: Information Gain for Attribute `Income`**
Attribute `Income` has 4 distinct values: `Very High`, `High`, `Medium`, `Low`.

1. **`Income = Very High`** (Instances 1, 5), Total = 2: `Yes` = 2, `Rented` = 0 (Pure)
   $$H(S_{\text{Very High}}) = \mathbf{0.0000 \text{ bits}}$$

2. **`Income = High`** (Instances 2, 4, 7, 12), Total = 4: `Yes` = 4, `Rented` = 0 (Pure)
   $$H(S_{\text{High}}) = \mathbf{0.0000 \text{ bits}}$$

3. **`Income = Low`** (Instances 3, 6, 10), Total = 3: `Yes` = 0, `Rented` = 3 (Pure)
   $$H(S_{\text{Low}}) = \mathbf{0.0000 \text{ bits}}$$

4. **`Income = Medium`** (Instances 8, 9, 11), Total = 3: `Yes` = 1 (Inst 8), `Rented` = 2 (Inst 9, 11)
   $$H(S_{\text{Medium}}) = -\left( \frac{1}{3}\log_2\frac{1}{3} + \frac{2}{3}\log_2\frac{2}{3} \right) = 0.5283 + 0.3900 = \mathbf{0.9183 \text{ bits}}$$

* **Weighted Partition Entropy:**
  $$H_{\text{Income}}(D) = \frac{2}{12}(0) + \frac{4}{12}(0) + \frac{3}{12}(0) + \frac{3}{12}(0.9183) = \mathbf{0.2296 \text{ bits}}$$

* **Information Gain:**
  $$\text{Gain}(D, \text{Income}) = H(D) - H_{\text{Income}}(D) = 0.9799 - 0.2296 = \mathbf{0.7503 \text{ bits}}$$

---

##### **Step 3: Information Gain for Attribute `Age`**

> ✅ **Corrected calculation.** The `Age = Young` group is Instances **1, 3, 8, 9** — i.e. **2 `Yes` (1, 8) and 2 `Rented` (3, 9)**, not 3 Yes / 1 Rented as an earlier draft of this problem stated. That earlier version skipped Instance 9. The corrected counts are used below.

1. **`Age = Young`** (Instances 1, 3, 8, 9), Total = 4: `Yes` = 2 (Inst 1, 8), `Rented` = 2 (Inst 3, 9)
   $$H(S_{\text{Young}}) = -\left( \frac{2}{4}\log_2\frac{2}{4} + \frac{2}{4}\log_2\frac{2}{4} \right) = \mathbf{1.0000 \text{ bit}} \quad \text{(perfectly balanced — maximum entropy)}$$

2. **`Age = Medium`** (Instances 2, 4, 5, 6, 11), Total = 5: `Yes` = 3 (Inst 2, 4, 5), `Rented` = 2 (Inst 6, 11)
   $$H(S_{\text{Medium}}) = -\left( \frac{3}{5}\log_2\frac{3}{5} + \frac{2}{5}\log_2\frac{2}{5} \right) = \mathbf{0.9710 \text{ bits}}$$

3. **`Age = Old`** (Instances 7, 10, 12), Total = 3: `Yes` = 2 (Inst 7, 12), `Rented` = 1 (Inst 10)
   $$H(S_{\text{Old}}) = -\left( \frac{2}{3}\log_2\frac{2}{3} + \frac{1}{3}\log_2\frac{1}{3} \right) = \mathbf{0.9183 \text{ bits}}$$

* **Weighted Partition Entropy:**
  $$H_{\text{Age}}(D) = \frac{4}{12}(1.0000) + \frac{5}{12}(0.9710) + \frac{3}{12}(0.9183) = 0.3333 + 0.4046 + 0.2296 = \mathbf{0.9675 \text{ bits}}$$

* **Information Gain (corrected):**
  $$\text{Gain}(D, \text{Age}) = H(D) - H_{\text{Age}}(D) = 0.9799 - 0.9675 = \mathbf{0.0124 \text{ bits}}$$

  *(The earlier, uncorrected count gave a different, incorrect gain value. The corrected value is $\approx 0.0124$ bits. This does **not** change which attribute is selected as root — see Step 4.)*

---

##### **Step 4: Select Root Node and Partition Data**
Comparing candidate attributes:
* $\text{Gain}(D, \text{Income}) = \mathbf{0.7503 \text{ bits}}$
* $\text{Gain}(D, \text{Age}) = \mathbf{0.0124 \text{ bits}}$

Since `Income` provides the maximum Information Gain (by a wide margin), **`Income` is selected as the Root Node**.

**Sub-Branch Evaluations:**
1. `Income = Very High` → Pure Leaf Node: **`Own House = Yes`**
2. `Income = High` → Pure Leaf Node: **`Own House = Yes`**
3. `Income = Low` → Pure Leaf Node: **`Own House = Rented`**
4. `Income = Medium` → Impure subset $S_{\text{Medium}}$ (Instances 8, 9, 11). Evaluate the only remaining attribute, `Age`:
   * Instance 8: `Age = Young` → `Yes`
   * Instance 9: `Age = Young` → `Rented`
   * Instance 11: `Age = Medium` → `Rented`
   * `Age = Medium` → Pure leaf: **`Own House = Rented`**
   * `Age = Old` → No instances in $S_{\text{Medium}}$ → inherit the parent subset's majority class ($S_{\text{Medium}}$ majority = Rented): **`Own House = Rented`**
   * `Age = Young` → **Tied leaf: 1 `Yes` (Inst 8) vs. 1 `Rented` (Inst 9).** No candidate attribute can split these two instances further, since they are identical on both `Income` and `Age`. This is a genuine contradiction in the training data (two records with the same features but different labels), not a modeling choice. ID3 cannot achieve 100% training accuracy at this leaf.
     * **Tie-breaking rule used here:** default to the **majority class of the immediate parent node** ($S_{\text{Medium}}$: 1 Yes, 2 Rented → Rented). This is one common convention; an alphabetically-first class, or a randomly/arbitrarily chosen class, are equally defensible alternatives — **state whichever rule you use explicitly in an exam answer**, since the "correct" leaf label depends entirely on that stated convention, not on the data.

---

##### **Step 5: Completed Decision Tree Diagram**

```text
                                 ┌─────────────────────────┐
                                 │      ROOT: INCOME       │
                                 └────────────┬────────────┘
                                              │
       ┌───────────────────┬─────────────────┼──────────────────┐
       │ Very High          │ High            │ Medium            │ Low
       ▼                    ▼                 ▼                   ▼
┌──────────────┐    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  LEAF: YES   │    │  LEAF: YES   │   │  NODE: AGE   │   │ LEAF: RENTED │
└──────────────┘    └──────────────┘   └──────┬───────┘   └──────────────┘
                                               │
                        ┌──────────────────────┼──────────────────────┐
                        │ Young                │ Medium                │ Old
                        ▼                      ▼                       ▼
                ┌───────────────┐      ┌──────────────┐        ┌──────────────┐
                │ LEAF: RENTED* │      │ LEAF: RENTED │        │ LEAF: RENTED │
                │ (tie, see     │      └──────────────┘        └──────────────┘
                │  Step 4 note) │
                └───────────────┘
```

---

##### **Step 6: IF-THEN Rule Extraction**
* **Rule 1:** `IF (Income = 'Very High') THEN Own House = 'Yes'`
* **Rule 2:** `IF (Income = 'High') THEN Own House = 'Yes'`
* **Rule 3:** `IF (Income = 'Low') THEN Own House = 'Rented'`
* **Rule 4:** `IF (Income = 'Medium') AND (Age = 'Young') THEN Own House = 'Rented'` *(tie-break — see Step 4; training data is contradictory here)*
* **Rule 5:** `IF (Income = 'Medium') AND (Age = 'Medium') THEN Own House = 'Rented'`
* **Rule 6:** `IF (Income = 'Medium') AND (Age = 'Old') THEN Own House = 'Rented'` *(no training instances; inherited from parent majority)*

---

##### **Step 7: Classification of New Instance**
* **New Instance Query:** `(Income = Medium, Age = Old)`
* **Traversal Trace:**
  1. Root `Income` = `Medium` → follow to node `Age`.
  2. `Age` = `Old` → follow to the leaf node.
  3. Leaf yields: **`Own House = Rented`**.
* **Final Answer:** The model predicts **`Rented`**.

---

### ✍️ **SOLVED PYQ 2: STOCK MARKET RETURN DATASET** [15 Marks]

* **Question Wording:**
  *"Given the following stock market dataset predicting 'Return' (Profit vs. Loss), construct a decision tree using ID3 algorithm. Show all entropy and information gain calculations clearly."*

#### **Given Training Dataset (Table 5.2):**

| Day | Past Trend | Open Interest | Trading Volume | Return (Target Class) |
| :---: | :---: | :---: | :---: | :---: |
| **D1** | Up | High | High | Profit |
| **D2** | Up | Low | High | Profit |
| **D3** | Down | Low | Low | Loss |
| **D4** | Down | High | Low | Loss |
| **D5** | Up | High | Low | Profit |

---

#### **Step-by-Step Mathematical Solution:**

##### **Step 1: Parent Dataset Entropy $H(D)$**
* Total instances $|D| = 5$.
* Target Class `Return` counts: `Profit` = 3 (D1, D2, D5), `Loss` = 2 (D3, D4).

$$H(D) = -\left( \frac{3}{5}\log_2\frac{3}{5} + \frac{2}{5}\log_2\frac{2}{5} \right) = -(0.6 \times (-0.7370) + 0.4 \times (-1.3219)) = \mathbf{0.9710 \text{ bits}}$$

##### **Step 2: Evaluate Attribute `Past Trend`**
Values: `Up` (D1, D2, D5), `Down` (D3, D4).
* `Past Trend = Up`: `Profit` = 3, `Loss` = 0 → $H(S_{\text{Up}}) = \mathbf{0.0000}$
* `Past Trend = Down`: `Profit` = 0, `Loss` = 2 → $H(S_{\text{Down}}) = \mathbf{0.0000}$
* $H_{\text{Past Trend}}(D) = \frac{3}{5}(0) + \frac{2}{5}(0) = \mathbf{0.0000 \text{ bits}}$
* $\text{Gain}(D, \text{Past Trend}) = 0.9710 - 0.0000 = \mathbf{0.9710 \text{ bits}}$

##### **Step 3: Evaluate Attribute `Open Interest`**
Values: `High` (D1, D4, D5), `Low` (D2, D3).
* `Open Interest = High`: `Profit` = 2 (D1, D5), `Loss` = 1 (D4) → $H = \mathbf{0.9183}$
* `Open Interest = Low`: `Profit` = 1 (D2), `Loss` = 1 (D3) → $H = \mathbf{1.0000}$
* $H_{\text{Open Interest}}(D) = \frac{3}{5}(0.9183) + \frac{2}{5}(1.0000) = 0.5510 + 0.4000 = \mathbf{0.9510 \text{ bits}}$
* $\text{Gain}(D, \text{Open Interest}) = 0.9710 - 0.9510 = \mathbf{0.0200 \text{ bits}}$

##### **Step 4: Evaluate Attribute `Trading Volume`**
Values: `High` (D1, D2), `Low` (D3, D4, D5).
* `Trading Volume = High`: `Profit` = 2, `Loss` = 0 → $H = \mathbf{0.0000}$
* `Trading Volume = Low`: `Profit` = 1 (D5), `Loss` = 2 (D3, D4) → $H = \mathbf{0.9183}$
* $H_{\text{Trading Volume}}(D) = \frac{2}{5}(0.0000) + \frac{3}{5}(0.9183) = \mathbf{0.5510 \text{ bits}}$
* $\text{Gain}(D, \text{Trading Volume}) = 0.9710 - 0.5510 = \mathbf{0.4200 \text{ bits}}$

##### **Step 5: Select Root Node and Complete Decision Tree**
Comparing Gains:
* $\text{Gain}(D, \text{Past Trend}) = \mathbf{0.9710 \text{ bits}}$ (maximum possible gain)
* $\text{Gain}(D, \text{Trading Volume}) = 0.4200 \text{ bits}$
* $\text{Gain}(D, \text{Open Interest}) = 0.0200 \text{ bits}$

Since `Past Trend` achieves a perfect partition with zero residual entropy, the tree terminates immediately at depth 1:

```text
                       ┌─────────────────────────┐
                       │    ROOT: PAST TREND     │
                       └────────────┬────────────┘
                                    │
                       ┌────────────┴────────────┐
                       │ Up                      │ Down
                       ▼                         ▼
               ┌──────────────┐          ┌──────────────┐
               │ LEAF: PROFIT │          │  LEAF: LOSS  │
               └──────────────┘          └──────────────┘
```

##### **Extracted Rules:**
1. `IF (Past Trend = 'Up') THEN Return = 'Profit'`
2. `IF (Past Trend = 'Down') THEN Return = 'Loss'`

---

### ✍️ **SOLVED PYQ 3: ID3 (INFORMATION GAIN) VS. CART (GINI IMPURITY) COMPARISON** [10 Marks]

* **Question Wording:**
  *"Given the following weekend activity dataset, evaluate the root node selection using BOTH Information Gain (ID3) and Gini Impurity (CART). Compare the attributes selected by both criteria."*

> 🚧 **OUT-OF-SCOPE FLAG:** This problem's **Gini Index / CART** portion (the Weighted Gini, Gini Reduction columns, and the "CART selects Parents" conclusion) goes beyond a syllabus defined strictly as *"up to decision trees, ID3, entropy, and information gain."* Gini Impurity belongs to **CART**, not ID3. Keep this problem for extra practice, but do **not** treat the Gini/CART material as required Unit 5 revision unless your syllabus explicitly includes CART. The **Information Gain / entropy** portion (used to pick the root node under ID3) *is* in scope, and its reported values check out: `Weather` wins under Information Gain, `Parents` wins under weighted Gini.

#### **Given Training Dataset (Table 5.3):**

| Day | Weather | Parents | Money | Decision (Target Class) |
| :---: | :---: | :---: | :---: | :---: |
| **D1** | Sunny | Yes | Rich | Cinema |
| **D2** | Sunny | No | Rich | Tennis |
| **D3** | Windy | Yes | Rich | Cinema |
| **D4** | Rainy | Yes | Poor | Cinema |
| **D5** | Rainy | No | Rich | Stay-In |
| **D6** | Rainy | Yes | Poor | Cinema |
| **D7** | Windy | No | Poor | Cinema |
| **D8** | Windy | Yes | Rich | Cinema |
| **D9** | Windy | No | Rich | Shopping |
| **D10** | Sunny | No | Rich | Tennis |

---

#### **Comparative Calculation Trace:**

##### **1. Target Class Counts & Parent Dataset Metrics**
* Total instances $|D| = 10$.
* Classes: `Cinema` = 6, `Tennis` = 2, `Stay-In` = 1, `Shopping` = 1.
* **Parent Entropy $H(D)$ (ID3, in scope):**
  $$H(D) = -\left( \frac{6}{10}\log_2\frac{6}{10} + \frac{2}{10}\log_2\frac{2}{10} + \frac{1}{10}\log_2\frac{1}{10} + \frac{1}{10}\log_2\frac{1}{10} \right) = \mathbf{1.5710 \text{ bits}}$$
* **Parent Gini Impurity $\text{Gini}(D)$ (CART, out of scope):**
  $$\text{Gini}(D) = 1 - \sum p_i^2 = 1 - \left( \left(\frac{6}{10}\right)^2 + \left(\frac{2}{10}\right)^2 + \left(\frac{1}{10}\right)^2 + \left(\frac{1}{10}\right)^2 \right) = 1 - 0.42 = \mathbf{0.5800}$$

##### **2. Attribute Evaluation Summary Table**

| Candidate Attribute | Weighted Entropy $H_A(D)$ (in scope) | Information Gain $\text{Gain}(D, A)$ (in scope) | Weighted Gini $\text{Gini}_A(D)$ (out of scope) | Gini Reduction $\Delta\text{Gini}(A)$ (out of scope) |
| :--- | :---: | :---: | :---: | :---: |
| **`Weather`** | $0.8755$ bits | $\mathbf{0.6955}$ bits *(Winner, ID3)* | $0.4167$ | $0.1633$ |
| **`Parents`** | $0.9610$ bits | $0.6100$ bits | $0.3600$ | $\mathbf{0.2200}$ *(Winner, CART)* |
| **`Money`** | $1.2897$ bits | $0.2813$ bits | $0.4857$ | $0.0943$ |

##### **3. Comparison Finding (`🧠 MUST UNDERSTAND`)**
* **ID3 (Information Gain, in scope)** selects **`Weather`** as the root node ($\text{Gain} = \mathbf{0.6955}$ bits).
* **CART (Gini Impurity, out of scope)** selects **`Parents`** as the root node ($\Delta\text{Gini} = \mathbf{0.2200}$), because `Parents = Yes` creates a completely pure subset ($\text{Gini} = 0$) for 5 instances where `Decision = Cinema`.
* For a strict ID3-only syllabus, only the `Weather`-as-root conclusion under Information Gain is required.

---

## SECTION 3: PYQ / SOURCE ATTRIBUTION (UNVERIFIED)

> ⚠️ See the Provenance Disclaimer at the top of this document. The table below is retained only as a rough index of which worked example covers which dataset — treat the "Exam & Year Source" and "Marks" columns as **unconfirmed**.

| Topic / Concept | Primary Question Wording | Exam & Year Source (unverified) | Marks (unverified) |
| :--- | :--- | :--- | :---: |
| **ID3 Numerical** | 12-Instance House Ownership Dataset (`Income`, `Age`) | Not independently confirmed | 15 |
| **ID3 Numerical** | 5-Instance Stock Market Dataset (`Past Trend`, `Volume`) | Not independently confirmed | 15 |
| **ID3 vs CART** | 10-Instance Weekend Activity Dataset (`Weather`, `Parents`) | Not independently confirmed | 10 |
| **ID3 Theory** | ID3 Algorithm Pseudocode & Base Stopping Conditions | Not independently confirmed | 5 |
| **Learning Types** | Supervised vs. Unsupervised vs. Reinforcement Learning Matrix | Not independently confirmed | 10 |

---

## SECTION 4: IMPORTANT ALGORITHM & PSEUDOCODE QUESTIONS

### **Q4.1: Explain the Working of the ID3 Algorithm with Pseudocode**
* **Answer Summary:** Refer to **Model Answer 3.1** in Section 1 for the 3-case stopping conditions and full recursive pseudocode.

---

## SECTION 5: COMMON EXAM PITFALLS (`⚠️ COMMON MISTAKES`)

1. **Logarithm Base Error:** Calculating entropy using natural log $\ln()$ or base-10 log $\log_{10}()$ instead of base-2 log $\log_2()$. *(Correction: $\log_2(x) = \frac{\ln(x)}{\ln(2)} = \frac{\log_{10}(x)}{0.30103}$)*.
2. **Forgetting the $\log_2(0)$ Boundary Condition:** Attempting to compute $\log_2(0)$ for pure subsets. *(Correction: define $0 \log_2(0) \equiv 0$ by convention)*.
3. **Inverted Information Gain Formula:** Subtracting parent entropy from partition entropy instead of $H(D) - H_A(D)$.
4. **Incorrect Rule Extraction:** Omitting internal node conditions along a root-to-leaf path when generating IF-THEN rules.
5. **Miscounting a subset's class split** (as in the Age = Young group above) — always recount directly from the training table rather than trusting a remembered total.
6. **Silently resolving a tie without stating the rule** — if two identical-feature training rows have different labels, state your tie-breaking convention explicitly rather than picking a label with no justification.

---

## SECTION 6: ID3 QUICK SOLVING CHECKLIST & FORMULA CHEAT SHEET

### **Cheat Sheet Formulas:**
1. **Entropy:** $H(S) = -\sum p_i \log_2(p_i)$
2. **Log Base-2 Trick:** $\log_2(p) = \frac{\log_{10}(p)}{0.30103}$
3. **Weighted Entropy:** $H_A(S) = \sum \frac{|S_v|}{|S|} H(S_v)$
4. **Information Gain:** $\text{Gain}(S, A) = H(S) - H_A(S)$

---

## SECTION 7: COMPLETE COVERAGE CHECKLIST

- [x] Inductive Learning & Paradigm Comparisons (Supervised, Unsupervised, RL)
- [x] Decision Tree Components (Root, Decision Nodes, Branches, Leaves)
- [x] ID3 Algorithm Pseudocode & 3 Base Stopping Conditions
- [x] Entropy & Information Gain Mathematical Formulas
- [x] Fully Solved ID3 House Ownership Numerical (corrected Age calculation + tie-break note)
- [x] Fully Solved ID3 Stock Market Numerical
- [x] Fully Solved ID3 vs. CART Weekend Activity Numerical (CART portion flagged out of scope)
- [x] IF-THEN Rule Extraction Mechanics
- [x] Common Exam Mistakes & Logarithm Base Conversion Tricks
