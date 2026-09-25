# ARTIFICIAL INTELLIGENCE (AI) STUDY NOTES
## UNIT 5: LEARNING (UP TO DECISION TREES)
### Course Code: 702CO0C076 | B.Tech Computer Engineering & AI (SVKM's NMIMS MPSTME / University Pattern)

---

## UNIT OVERVIEW

Machine Learning is a fundamental subfield of Artificial Intelligence that enables computers to learn from data and improve their performance on tasks without being explicitly programmed. This study guide covers the foundational principles of **Inductive Learning**, compares the core paradigms of machine learning (**Supervised**, **Unsupervised**, and **Reinforcement Learning**), and provides a comprehensive, mathematically rigorous treatment of **Decision Tree Classification** using the **ID3 (Iterative Dichotomiser 3)** algorithm.

---

## SECTION 1: INDUCTIVE LEARNING & MACHINE LEARNING TYPES

### 1.1 Concept of Learning & Inductive Bias

An agent is said to **learn** if it improves its performance on future tasks after making observations about the world.

* **Inductive Learning:** The process of extracting general rules, functions, or patterns ($h$) from a finite set of specific observed training examples ($E$).
* **Goal of Inductive Inference:** Given a collection of training pairs $(x_1, y_1), (x_2, y_2), \dots, (x_N, y_N)$ where $y_i = f(x_i)$, find a hypothesis function $h(x)$ that closely approximates the true underlying target function $f(x)$ for unseen inputs.
* **Fundamental Assumption of Inductive Learning:** *"Any hypothesis found to approximate the target function well over a sufficiently large set of training examples will also approximate the target function well over unobserved examples."*

```text
                 ┌──────────────────────────────────────┐
                 │       OBSERVED TRAINING DATA         │
                 │   (Specific Input-Output Pairs)      │
                 └──────────────────┬───────────────────┘
                                    │
                                    ▼
                         [ INDUCTIVE INFERENCE ]
                          (Generalization Process)
                                    │
                                    ▼
                 ┌──────────────────────────────────────┐
                 │           HYPOTHESIS h(x)            │
                 │   (Predictive Model for Unseen Data) │
                 └──────────────────────────────────────┘
```

> ⭐ **Must Remember:** **Inductive Bias** is the set of explicit or implicit assumptions a learning algorithm uses to predict outputs for unseen inputs. Without an inductive bias, a learner cannot generalize beyond the exact memorized training examples.

---

### 1.2 Conceptual Comparison of Machine Learning Paradigms

Machine Learning algorithms are categorized into three primary paradigms based on the nature of the feedback provided to the agent:

```text
                                  ┌─────────────────────────┐
                                  │    MACHINE LEARNING     │
                                  └────────────┬────────────┘
                                               │
         ┌─────────────────────────────────────┼─────────────────────────────────────┐
         ▼                                     ▼                                     ▼
┌─────────────────────────┐           ┌─────────────────────────┐           ┌─────────────────────────┐
│   SUPERVISED LEARNING   │           │  UNSUPERVISED LEARNING  │           │ REINFORCEMENT LEARNING  │
│ Labeled Data (Inputs+   │           │ Unlabeled Data (Inputs  │           │ Environment Interaction │
│ Desired Targets)        │           │ Only)                   │           │ Rewards & Punishments   │
└─────────────────────────┘           └─────────────────────────┘           └─────────────────────────┘
```

| Dimension | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
| :--- | :--- | :--- | :--- |
| **Input Data** | Labeled dataset: $\{(x_1, y_1), \dots, (x_N, y_N)\}$ containing features $x$ and explicit target labels $y$. | Unlabeled dataset: $\{x_1, x_2, \dots, x_N\}$ containing features only; no target labels. | State environment $S$, set of available actions $A$, and scalar reward signals $R$. |
| **Teacher / Feedback** | Direct supervision by a "teacher" providing correct answers. | No teacher; system discovers inherent structure autonomously. | Delayed reinforcement signals (rewards/penalties) resulting from trial-and-error actions. |
| **Primary Goal** | Learn a mapping function $h: X \to Y$ to predict correct labels for new, unseen inputs. | Discover hidden patterns, groupings, clusters, or probability distributions in data. | Learn an optimal policy $\pi: S \to A$ that maximizes cumulative long-term reward. |
| **Key Tasks** | Classification (discrete targets) and Regression (continuous targets). | Clustering (e.g., K-Means), Dimensionality Reduction, Association Rules. | Game playing (e.g., Chess, Go), Autonomous Navigation, Robotic Control. |
| **Concrete Example** | Predicting whether a patient has disease (Yes/No) based on clinical measurements. | Grouping online shoppers into distinct customer segments based on purchasing behavior. | Training a self-driving car to stay in lane using rewards for safety and penalties for drift. |

> 🧠 **Must Understand:** 
> * **Classification vs. Regression:** Both are supervised learning tasks. In **Classification**, the output label $y$ is categorical/discrete (e.g., `{Profit, Loss}` or `{Yes, No}`). In **Regression**, the output $y$ is continuous/numeric (e.g., house price in dollars).

---

## SECTION 2: SUPERVISED LEARNING & DECISION TREE CLASSIFICATION

### 2.1 Core Terminology

1. **Training Instance / Example ($x_i$):** A single record or data point described by a set of input attributes.
2. **Attributes / Features ($A_1, A_2, \dots, A_m$):** Properties or characteristics describing each instance (e.g., `Income`, `Age`, `Outlook`).
3. **Target Variable / Class Label ($Y$):** The output category to be predicted (e.g., `Own House`, `Return`, `PlayTennis`).
4. **Decision Tree:** A non-parametric supervised learning model that represents decisions and decision-making workflows as a hierarchical, directed tree graph.

---

### 2.2 Anatomic Anatomy of a Decision Tree

A Decision Tree represents a disjunction of conjunctions of constraints on the attribute values of instances.

```text
                     ┌────────────────────────┐
                     │       ROOT NODE        │  ◄── Topmost Decision Node
                     │  (Highest Info Gain)   │      (Evaluates First Feature)
                     └───────────┬────────────┘
                                 │
                     ┌───────────┴────────────┐
                     │         BRANCH         │  ◄── Attribute Value Split
                     └───────────┬────────────┘      (e.g., Feature == 'High')
                                 │
                     ┌───────────▼────────────┐
                     │ INTERNAL DECISION NODE │  ◄── Intermediate Decision Node
                     │ (Sub-attribute Test)   │      (Splits Subset Further)
                     └───────────┬────────────┘
                                 │
                     ┌───────────┴────────────┐
                     │         BRANCH         │  ◄── Attribute Value Split
                     └───────────┬────────────┘
                                 │
                     ┌───────────▼────────────┐
                     │       LEAF NODE        │  ◄── Terminal Output Node
                     │     [ CLASS LABEL ]    │      (Final Decision / Prediction)
                     └────────────────────────┘
```

* **Root Node:** The top-level node in the tree containing the full dataset. It evaluates the most informative attribute (highest Information Gain).
* **Internal Decision Nodes:** Intermediate nodes representing tests on specific input attributes.
* **Branches:** Edges representing the specific categorical values or outcomes of an attribute test.
* **Leaf / Terminal Nodes:** Final nodes that contain no child splits. Each leaf node is assigned a specific **Class Label** or outcome prediction.

---

### 2.3 Predicting the Class of an Unseen Example

To classify a new test instance using a learned decision tree:
1. Start at the **Root Node**.
2. Test the attribute specified by the root node on the test instance.
3. Move down the branch corresponding to the instance's specific value for that attribute.
4. Repeat this process at each subsequent internal decision node until a **Leaf Node** is reached.
5. Assign the class label at the leaf node as the predicted outcome for the test instance.

> ✍️ **Exam Focus:** Decision trees can represent **any Boolean function** over discrete attributes. In the worst case, a truth table with $n$ binary attributes can be converted into a decision tree of exponential size ($2^n$ leaves).

---

## SECTION 3: THE ID3 (ITERATIVE DICHOTOMISER 3) ALGORITHM

Developed by Ross Quinlan in 1986, **ID3** is a classic greedy, top-down decision tree construction algorithm for discrete/categorical features.

### 3.1 Core Strategy & Principles
* **Top-Down Induction:** Builds the tree top-down starting from the root node containing all training instances.
* **Greedy Choice:** At each step, selects the single best attribute that maximizes **Information Gain** (minimizes residual Entropy).
* **Recursive Partitioning:** Splits the dataset into non-overlapping subsets based on the chosen attribute's values and applies the same procedure recursively to each child subset.

---

### 3.2 Stopping Conditions (Base Cases)
The recursive tree-building process terminates at a node when any of the following conditions is met:

1. **Pure Node (All Instances Belong to Same Class):** All training examples at the current node belong to the exact same class label $c_k$. Create a leaf node with label $c_k$.
2. **No Attributes Remaining:** The candidate attribute list is empty (all input features have already been used along the current path). Create a leaf node with the **majority class label** among the examples at the node.
3. **No Examples Remaining:** The subset of examples for a particular branch is empty. Create a leaf node labeled with the **majority class label** of the parent node.

---

### 3.3 Formal ID3 Pseudocode

```python
def ID3(examples, target_attribute, attributes):
    # ID3 Decision Tree Induction Algorithm
    # Parameters:
    # - examples: Training dataset (subset of records at current node)
    # - target_attribute: Name of column to be predicted (Class Label)
    # - attributes: List of available input feature columns
    
    # Create a Root node for the tree
    root = Node()
    
    # Base Case 1: If all examples belong to the same target class
    if all_examples_same_class(examples, target_attribute):
        root.label = get_common_class(examples, target_attribute)
        return root
        
    # Base Case 2: If attributes list is empty
    if not attributes:
        root.label = majority_class(examples, target_attribute)
        return root
        
    # Step 1: Select the attribute with the maximum Information Gain
    best_attr = None
    max_gain = -1.0
    parent_entropy = compute_entropy(examples, target_attribute)
    
    for attr in attributes:
        gain = compute_information_gain(examples, attr, target_attribute, parent_entropy)
        if gain > max_gain:
            max_gain = gain
            best_attr = attr
            
    # Assign best attribute to root decision node
    root.attribute = best_attr
    
    # Step 2: For each possible value v_i of best_attr, grow a branch
    for value in get_possible_values(best_attr):
        # Subset of examples where best_attr == value
        examples_vi = [ex for ex in examples if ex[best_attr] == value]
        
        # Base Case 3: If subset is empty, add leaf with parent majority class
        if not examples_vi:
            leaf = Node()
            leaf.label = majority_class(examples, target_attribute)
            root.add_branch(value, leaf)
        else:
            # Recursive call with remaining attributes
            remaining_attrs = [a for a in attributes if a != best_attr]
            subtree = ID3(examples_vi, target_attribute, remaining_attrs)
            root.add_branch(value, subtree)
            
    return root
```

---

## SECTION 4: MATHEMATICAL CALCULATIONS (ENTROPY & INFORMATION GAIN)

ID3 relies on metrics from Information Theory (Claude Shannon) to quantify impurity and expected information reduction.

### 4.1 Entropy ($H(S)$)
**Entropy** measures the degree of impurity, disorder, or class uncertainty within a collection of examples $S$.

#### 1. General Formula for $k$ Classes:
$$H(S) = - \sum_{i=1}^{k} p_i \log_2 (p_i)$$

Where:
* $S$: Collection of training examples at the node.
* $k$: Total number of distinct target classes.
* $p_i$: Proportion/probability of examples in $S$ belonging to class $i$ ($p_i = \frac{|S_i|}{|S|}$).
* $\log_2$: Base-2 logarithm (measuring information in **bits**). Note: $0 \log_2(0) \equiv 0$.

#### 2. Binary Classification Formula ($+$ and $-$ classes):
$$H(S) = - p_{\oplus} \log_2 (p_{\oplus}) - p_{\ominus} \log_2 (p_{\ominus})$$

Where:
* $p_{\oplus} = \frac{p}{p + n}$: Ratio of positive examples.
* $p_{\ominus} = \frac{n}{p + n}$: Ratio of negative examples.

#### 3. Properties of Entropy:
* **Minimum Entropy ($H(S) = 0$):** Occurs when the node is completely **pure** (all examples belong to a single class, e.g., $p_{\oplus} = 1, p_{\ominus} = 0$).
* **Maximum Entropy ($H(S) = 1.0$ bit):** Occurs in binary classification when the classes are **equally distributed** ($p_{\oplus} = 0.5, p_{\ominus} = 0.5$).
* **Higher Entropy $\implies$ Higher Impurity $\implies$ Lower Homogeneity.**

```text
                     ENTROPY CURVE FOR BINARY CLASSIFICATION
      Entropy H(S)
        1.0 ┼───────────────────────(0.5, 1.0)
            │                     .  │  .
            │                   .    │    .
        0.5 ┼                  .     │     .
            │                 .      │      .
            │                .       │       .
        0.0 ┴───────────────┴────────┴────────┴────────
            0.0            0.5       │       1.0   p+ (Proportion)
          (Pure -)                 Maximum       (Pure +)
                                   Impurity
```

---

### 4.2 Information Gain ($\text{Gain}(S, A)$)
**Information Gain** is the expected reduction in entropy achieved by partitioning the dataset $S$ according to the candidate attribute $A$.

#### 1. Mathematical Formula:
$$\text{Gain}(S, A) = H(S) - \text{Weighted\_Entropy}(S, A)$$

$$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$

Where:
* $H(S)$: Parent entropy of dataset $S$ prior to splitting.
* $\text{Values}(A)$: Set of all distinct categorical values that attribute $A$ can assume.
* $S_v$: Subset of examples in $S$ where attribute $A$ has value $v$ ($S_v = \{ x \in S \mid A(x) = v \}$).
* $\frac{|S_v|}{|S|}$: Weight/fraction of instances falling into branch $v$.
* $H(S_v)$: Entropy of the child subset $S_v$.

> 🧠 **Must Understand:** ID3 evaluates $\text{Gain}(S, A)$ for every candidate feature $A$ and chooses the feature $A^*$ with the **largest Information Gain** to split the current node:
> $$A^* = \arg\max_{A} \text{Gain}(S, A)$$

---

## SECTION 5: RULE EXTRACTION FROM DECISION TREES

Decision Trees are fully transparent, interpretable "white-box" models. A decision tree can be directly converted into a set of **IF-THEN Classification Rules**.

### 5.1 Rule Extraction Method
1. Trace every complete path from the **Root Node** down to each **Leaf Node**.
2. Form the **IF** part (antecedent/condition) by joining all attribute-value branch tests along the path using logical **AND** ($\wedge$).
3. Form the **THEN** part (consequent/conclusion) by assigning the target **Class Label** at the leaf node.
4. The complete rule set represents an overall logical **OR** ($\vee$) over all extracted IF-THEN rules.

```text
                    Root Node [Outlook]
                    /        |        \
             Sunny /     Overcast      \ Rain
                  /          |          \
          [Humidity]      [YES]        [Wind]
          /        \                  /      \
    High /          \ Normal   Strong/        \ Weak
        /            \              /          \
      [NO]          [YES]        [NO]          [YES]
```

#### Extracted IF-THEN Rule Set:
* **Rule 1:** `IF (Outlook == Sunny) AND (Humidity == High) THEN PlayTennis = No`
* **Rule 2:** `IF (Outlook == Sunny) AND (Humidity == Normal) THEN PlayTennis = Yes`
* **Rule 3:** `IF (Outlook == Overcast) THEN PlayTennis = Yes`
* **Rule 4:** `IF (Outlook == Rain) AND (Wind == Strong) THEN PlayTennis = No`
* **Rule 5:** `IF (Outlook == Rain) AND (Wind == Weak) THEN PlayTennis = Yes`

---

## SECTION 6: WORKED EXAMPLES AND NUMERICALS (FULLY SOLVED PYQs)

> ⚠️ **Note on "PYQ" Source Labels:** The exam year, session, and question-number labels attached to the three worked examples below (e.g. "Re-Exam 2024-25 Q6.a") have **not** been verified against the original Unit 5 question papers. Treat these three problems as **practice numericals in a PYQ-style format**, not as confirmed past-paper citations, until checked against the actual papers.

---

### ✍️ **PYQ 1: Income, Age & Own House Classification Model**
*(Source: NMIMS B.Tech CE Re-Exam 2024-25 Q6.a / Final Exam 2024-25 Q5.b [15 Marks])*

#### **Problem Statement:**
Using the following training dataset, create a classification model using a decision tree algorithm (ID3) and draw the final tree.

| Tid | Income | Age | Own House |
| :---: | :--- | :--- | :---: |
| 1 | Very High | Young | Yes |
| 2 | High | Medium | Yes |
| 3 | Low | Young | Rented |
| 4 | High | Medium | Yes |
| 5 | Very High | Medium | Yes |
| 6 | Medium | Young | Yes |
| 7 | High | Old | Yes |
| 8 | Medium | Medium | Rented |
| 9 | Low | Medium | Rented |
| 10 | Low | Old | Rented |
| 11 | High | Young | Yes |
| 12 | Medium | Old | Rented |

* **Input Attributes:** `Income` `{Very High, High, Medium, Low}`, `Age` `{Young, Medium, Old}`
* **Target Variable / Class Label:** `Own House` `{Yes, Rented}`

---

#### **Step-by-Step Solution:**

##### **Step 1: Parent Dataset Entropy Calculation**
* Total examples ($N$) = $12$.
* Positive Class (`Own House = Yes`): $7$ instances (Tid: 1, 2, 4, 5, 6, 7, 11).
* Negative Class (`Own House = Rented`): $5$ instances (Tid: 3, 8, 9, 10, 12).

$$p_{\text{Yes}} = \frac{7}{12} \approx 0.5833, \quad p_{\text{Rented}} = \frac{5}{12} \approx 0.4167$$

$$H(D) = - \left( \frac{7}{12} \log_2 \frac{7}{12} \right) - \left( \frac{5}{12} \log_2 \frac{5}{12} \right)$$
$$H(D) = - (0.5833 \times -0.7781) - (0.4167 \times -1.2630) = 0.4539 + 0.5263 = \mathbf{0.9799 \text{ bits}}$$

---

##### **Step 2: Evaluate Information Gain for Candidate Root Attributes**

###### **A. Evaluating Candidate Attribute 1: `Income`**
Values: `{Very High, High, Medium, Low}`

1. **`Income = Very High` (2 instances: Tid 1, 5):**
   * Class distribution: `Yes` = 2, `Rented` = 0 (Pure)
   * $H(S_{\text{Very High}}) = 0.0$

2. **`Income = High` (4 instances: Tid 2, 4, 7, 11):**
   * Class distribution: `Yes` = 4, `Rented` = 0 (Pure)
   * $H(S_{\text{High}}) = 0.0$

3. **`Income = Low` (3 instances: Tid 3, 9, 10):**
   * Class distribution: `Yes` = 0, `Rented` = 3 (Pure)
   * $H(S_{\text{Low}}) = 0.0$

4. **`Income = Medium` (3 instances: Tid 6, 8, 12):**
   * Class distribution: `Yes` = 1 (Tid 6), `Rented` = 2 (Tid 8, 12)
   * $H(S_{\text{Medium}}) = - \left( \frac{1}{3} \log_2 \frac{1}{3} \right) - \left( \frac{2}{3} \log_2 \frac{2}{3} \right) = \mathbf{0.9183 \text{ bits}}$

* **Weighted Entropy for `Income`:**
  $$\text{Weighted\_Entropy}(D, \text{Income}) = \frac{2}{12}(0) + \frac{4}{12}(0) + \frac{3}{12}(0) + \frac{3}{12}(0.9183) = \frac{3}{12} \times 0.9183 = \mathbf{0.2296 \text{ bits}}$$

* **Information Gain for `Income`:**
  $$\text{Gain}(D, \text{Income}) = H(D) - \text{Weighted\_Entropy}(D, \text{Income}) = 0.9799 - 0.2296 = \mathbf{0.7503 \text{ bits}}$$

---

###### **B. Evaluating Candidate Attribute 2: `Age`**
Values: `{Young, Medium, Old}`

1. **`Age = Young` (4 instances: Tid 1, 3, 6, 11):**
   * Class distribution: `Yes` = 3 (Tid 1, 6, 11), `Rented` = 1 (Tid 3)
   * $H(S_{\text{Young}}) = - \left( \frac{3}{4} \log_2 \frac{3}{4} \right) - \left( \frac{1}{4} \log_2 \frac{1}{4} \right) = \mathbf{0.8113 \text{ bits}}$

2. **`Age = Medium` (5 instances: Tid 2, 4, 5, 8, 9):**
   * Class distribution: `Yes` = 3 (Tid 2, 4, 5), `Rented` = 2 (Tid 8, 9)
   * $H(S_{\text{Medium}}) = - \left( \frac{3}{5} \log_2 \frac{3}{5} \right) - \left( \frac{2}{5} \log_2 \frac{2}{5} \right) = \mathbf{0.9710 \text{ bits}}$

3. **`Age = Old` (3 instances: Tid 7, 10, 12):**
   * Class distribution: `Yes` = 1 (Tid 7), `Rented` = 2 (Tid 10, 12)
   * $H(S_{\text{Old}}) = - \left( \frac{1}{3} \log_2 \frac{1}{3} \right) - \left( \frac{2}{3} \log_2 \frac{2}{3} \right) = \mathbf{0.9183 \text{ bits}}$

* **Weighted Entropy for `Age`:**
  $$\text{Weighted\_Entropy}(D, \text{Age}) = \frac{4}{12}(0.8113) + \frac{5}{12}(0.9710) + \frac{3}{12}(0.9183) = 0.2704 + 0.4046 + 0.2296 = \mathbf{0.9046 \text{ bits}}$$

* **Information Gain for `Age`:**
  $$\text{Gain}(D, \text{Age}) = 0.9799 - 0.9046 = \mathbf{0.0753 \text{ bits}}$$

---

##### **Step 3: Root Node Selection**
* $\text{Gain}(D, \text{Income}) = \mathbf{0.7503 \text{ bits}}$
* $\text{Gain}(D, \text{Age}) = \mathbf{0.0753 \text{ bits}}$

Since **`Income`** provides the maximum Information Gain, it is selected as the **Root Node**.

---

##### **Step 4: Recursive Sub-Branch Evaluation**

Split dataset $D$ on `Income`:
* Branch `Income == Very High` $\to$ All 2 instances are `Yes`. **Leaf Node: Yes**.
* Branch `Income == High` $\to$ All 4 instances are `Yes`. **Leaf Node: Yes**.
* Branch `Income == Low` $\to$ All 3 instances are `Rented`. **Leaf Node: Rented**.
* Branch `Income == Medium` $\to$ Contains 3 instances (Tid 6, 8, 12):
  * Tid 6: Age = Young $\to$ `Yes`
  * Tid 8: Age = Medium $\to$ `Rented`
  * Tid 12: Age = Old $\to$ `Rented`

For the subset $D_{\text{Medium}}$, the remaining candidate attribute is **`Age`**:
* Sub-branch `Age == Young` $\to$ **Leaf Node: Yes**.
* Sub-branch `Age == Medium` $\to$ **Leaf Node: Rented**.
* Sub-branch `Age == Old` $\to$ **Leaf Node: Rented**.

---

##### **Step 5: Final Decision Tree Diagram**

```text
                       ┌─────────────────────────┐
                       │     ROOT: INCOME        │
                       └────────────┬────────────┘
                                    │
       ┌──────────────────┬─────────┴─────────┬──────────────────┐
       │ Very High        │ High              │ Medium           │ Low
       ▼                  ▼                   ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ LEAF: YES    │   │ LEAF: YES    │   │  NODE: AGE   │   │ LEAF: RENTED │
└──────────────┘   └──────────────┘   └──────┬───────┘   └──────────────┘
                                             │
                       ┌─────────────────────┼─────────────────────┐
                       │ Young               │ Medium              │ Old
                       ▼                     ▼                     ▼
               ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
               │ LEAF: YES    │      │ LEAF: RENTED │      │ LEAF: RENTED │
               └──────────────┘      └──────────────┘      └──────────────┘
```

---

##### **Step 6: Extracted IF-THEN Rules**
* **Rule 1:** `IF (Income == Very High) THEN Own House = Yes`
* **Rule 2:** `IF (Income == High) THEN Own House = Yes`
* **Rule 3:** `IF (Income == Low) THEN Own House = Rented`
* **Rule 4:** `IF (Income == Medium) AND (Age == Young) THEN Own House = Yes`
* **Rule 5:** `IF (Income == Medium) AND (Age == Medium) THEN Own House = Rented`
* **Rule 6:** `IF (Income == Medium) AND (Age == Old) THEN Own House = Rented`

---

### ✍️ **PYQ 2: Stock Market Return Prediction Model**
*(Source: SVKM's NMIMS B.Tech AI Final Exam 2025-26 Q6.a [15 Marks])*

#### **Problem Statement:**
Using the dataset, build a decision tree to predict `Return`. You may use any decision tree algorithm (ID3 or CART). Determine the root node and subsequent splits based on your chosen method. Define Inductive Learning and explain how it can be applied to this dataset. Generate IF-THEN rules from your decision tree for predicting `Return`.

| Record | Past Trend | Open Interest | Trading Volume | Return |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Up | High | High | Profit |
| 2 | Up | High | Low | Profit |
| 3 | Down | Low | High | Loss |
| 4 | Down | High | Low | Loss |
| 5 | Up | Low | High | Profit |

---

#### **Step-by-Step Solution:**

##### **Step 1: Dataset Class Counts & Parent Entropy**
* Total examples ($N$) = $5$.
* Target Variable: `Return` `{Profit, Loss}`
* Class Counts: `Profit` = 3 (Records 1, 2, 5), `Loss` = 2 (Records 3, 4).

$$H(D) = - \left( \frac{3}{5} \log_2 \frac{3}{5} \right) - \left( \frac{2}{5} \log_2 \frac{2}{5} \right) = - (0.6 \times -0.7370) - (0.4 \times -1.3219) = \mathbf{0.9710 \text{ bits}}$$

---

##### **Step 2: Calculate Information Gain for Candidate Attributes**

###### **A. Attribute 1: `Past Trend` `{Up, Down}`**
1. `Past Trend = Up` (3 instances: Rec 1, 2, 5) $\to$ `Profit` = 3, `Loss` = 0 $\implies H(S_{\text{Up}}) = \mathbf{0.0}$ (Pure)
2. `Past Trend = Down` (2 instances: Rec 3, 4) $\to$ `Profit` = 0, `Loss` = 2 $\implies H(S_{\text{Down}}) = \mathbf{0.0}$ (Pure)

$$\text{Weighted\_Entropy}(D, \text{Past Trend}) = \frac{3}{5}(0.0) + \frac{2}{5}(0.0) = \mathbf{0.0 \text{ bits}}$$
$$\text{Gain}(D, \text{Past Trend}) = 0.9710 - 0.0 = \mathbf{0.9710 \text{ bits}}$$

---

###### **B. Attribute 2: `Open Interest` `{High, Low}`**
1. `Open Interest = High` (3 instances: Rec 1, 2, 4) $\to$ `Profit` = 2, `Loss` = 1:
   $$H(S_{\text{High}}) = - \left( \frac{2}{3} \log_2 \frac{2}{3} \right) - \left( \frac{1}{3} \log_2 \frac{1}{3} \right) = \mathbf{0.9183 \text{ bits}}$$
2. `Open Interest = Low` (2 instances: Rec 3, 5) $\to$ `Profit` = 1, `Loss` = 1:
   $$H(S_{\text{Low}}) = \mathbf{1.0000 \text{ bit}}$$

$$\text{Weighted\_Entropy}(D, \text{Open Interest}) = \frac{3}{5}(0.9183) + \frac{2}{5}(1.0000) = 0.5510 + 0.4000 = \mathbf{0.9510 \text{ bits}}$$
$$\text{Gain}(D, \text{Open Interest}) = 0.9710 - 0.9510 = \mathbf{0.0200 \text{ bits}}$$

---

###### **C. Attribute 3: `Trading Volume` `{High, Low}`**
1. `Trading Volume = High` (3 instances: Rec 1, 3, 5) $\to$ `Profit` = 2, `Loss` = 1 $\implies H(S_{\text{High}}) = 0.9183$
2. `Trading Volume = Low` (2 instances: Rec 2, 4) $\to$ `Profit` = 1, `Loss` = 1 $\implies H(S_{\text{Low}}) = 1.0000$

$$\text{Gain}(D, \text{Trading Volume}) = 0.9710 - 0.9510 = \mathbf{0.0200 \text{ bits}}$$

---

##### **Step 3: Root Selection & Decision Tree**
* $\text{Gain}(D, \text{Past Trend}) = \mathbf{0.9710 \text{ bits}}$ (Maximum Possible Gain!)

Since `Past Trend` creates $100\%$ pure subsets on both branches, it is selected as the **Root Node**, and the tree construction terminates immediately.

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

---

##### **Step 4: Application of Inductive Learning & IF-THEN Rules**
* **Definition of Inductive Learning:** Inductive learning extracts general predictive rules from specific trading observations. Here, the learner induces that whenever `Past Trend` is `Up`, the return is `Profit`, regardless of open interest or trading volume.
* **Extracted IF-THEN Rules:**
  * **Rule 1:** `IF (Past Trend == Up) THEN Return = Profit`
  * **Rule 2:** `IF (Past Trend == Down) THEN Return = Loss`

---

### ✍️ **PYQ 3: Gini Index vs. Information Gain Comparison**
*(Source: SVKM's NMIMS Final Exam 2022-23 Q5.A [10 Marks] — source label unverified, see note above)*

> 🚧 **OUT OF SCOPE FLAG:** This problem's **Gini Index / CART** portion (Step 2's Gini and Gini-Gain columns, and the "Under Gini Impurity (CART)..." conclusion) goes beyond a syllabus defined strictly as *"up to ID3, entropy, and information gain."* Gini Impurity belongs to the **CART** algorithm, not ID3. Keep this problem for extra practice, but **do not treat the Gini/CART material as required Unit 5 revision** unless your syllabus explicitly includes CART. The **Information Gain / entropy** portion of this problem (used to pick the root node under ID3) *is* in scope and its listed values check out against the table above.

#### **Problem Statement:**
Calculate the following for the given dataset:
1. Compute the **Gini Index** for `Weather`, `Parents`, and `Money` w.r.t decision as output variable.
2. Which attribute is better (`Weather`, `Parents`, or `Money`) and why?
3. Evaluate the root node attribute using Information Gain and draw the decision tree.

| Record | Weather | Parents | Money | Decision |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Sunny | Yes | Rich | Cinema |
| 2 | Sunny | No | Rich | Tennis |
| 3 | Windy | Yes | Rich | Cinema |
| 4 | Rainy | Yes | Poor | Cinema |
| 5 | Rainy | No | Rich | Stay-In |
| 6 | Rainy | Yes | Poor | Cinema |
| 7 | Windy | No | Poor | Cinema |
| 8 | Windy | No | Rich | Shopping |
| 9 | Windy | Yes | Rich | Cinema |
| 10 | Sunny | No | Rich | Tennis |

* **Class Labels ($Y$):** `{Cinema, Tennis, Stay-In, Shopping}` ($4$ classes).
* **Total Instances ($N$):** $10$.
* **Class Frequencies:** `Cinema` = 6, `Tennis` = 2, `Stay-In` = 1, `Shopping` = 1.

---

#### **Formula Definitions:**
$$\text{Gini}(S) = 1 - \sum_{i=1}^{k} p_i^2, \quad \text{Gini\_Gain}(S, A) = \text{Gini}(S) - \sum_{v} \frac{|S_v|}{|S|} \text{Gini}(S_v)$$

---

#### **Step-by-Step Solution:**

##### **Step 1: Parent Gini & Parent Entropy**
* **Parent Gini:**
  $$\text{Gini}(D) = 1 - \left[ \left(\frac{6}{10}\right)^2 + \left(\frac{2}{10}\right)^2 + \left(\frac{1}{10}\right)^2 + \left(\frac{1}{10}\right)^2 \right] = 1 - [0.36 + 0.04 + 0.01 + 0.01] = \mathbf{0.5800}$$

* **Parent Entropy:**
  $$H(D) = - \left[ 0.6 \log_2 0.6 + 0.2 \log_2 0.2 + 0.1 \log_2 0.1 + 0.1 \log_2 0.1 \right] = \mathbf{1.5710 \text{ bits}}$$

---

##### **Step 2: Compute Gini Index and Information Gain for Each Attribute**

###### **1. Attribute `Parents` `{Yes, No}`**
* `Parents = Yes` (5 instances: Rec 1, 3, 4, 6, 9) $\to$ All 5 are `Cinema` (Pure):
  $$\text{Gini}(S_{\text{Yes}}) = 0.0, \quad H(S_{\text{Yes}}) = 0.0$$
* `Parents = No` (5 instances: Rec 2, 5, 7, 8, 10) $\to$ `Cinema`=1, `Tennis`=2, `Stay-In`=1, `Shopping`=1:
  $$\text{Gini}(S_{\text{No}}) = 1 - \left[ (0.2)^2 + (0.4)^2 + (0.2)^2 + (0.2)^2 \right] = 1 - [0.04 + 0.16 + 0.04 + 0.04] = \mathbf{0.7200}$$
  $$H(S_{\text{No}}) = - [0.2\log_2 0.2 + 0.4\log_2 0.4 + 0.2\log_2 0.2 + 0.2\log_2 0.2] = \mathbf{1.9219 \text{ bits}}$$

* **Weighted Metrics for `Parents`:**
  $$\text{Weighted\_Gini}(\text{Parents}) = \frac{5}{10}(0.0) + \frac{5}{10}(0.7200) = \mathbf{0.3600}$$
  $$\text{Gini\_Gain}(\text{Parents}) = 0.5800 - 0.3600 = \mathbf{0.2200}$$
  $$\text{Weighted\_Entropy}(\text{Parents}) = \frac{5}{10}(0) + \frac{5}{10}(1.9219) = \mathbf{0.9610 \text{ bits}}$$
  $$\text{Gain}(\text{Parents}) = 1.5710 - 0.9610 = \mathbf{0.6100 \text{ bits}}$$

---

###### **2. Attribute `Weather` `{Sunny, Windy, Rainy}`**
* `Sunny` (3 instances: Rec 1, 2, 10) $\to$ `Cinema`=1, `Tennis`=2:
  $$\text{Gini} = 1 - [(1/3)^2 + (2/3)^2] = 0.4444, \quad H = 0.9183 \text{ bits}$$
* `Windy` (4 instances: Rec 3, 7, 8, 9) $\to$ `Cinema`=3, `Shopping`=1:
  $$\text{Gini} = 1 - [(3/4)^2 + (1/4)^2] = 0.3750, \quad H = 0.8113 \text{ bits}$$
* `Rainy` (3 instances: Rec 4, 5, 6) $\to$ `Cinema`=2, `Stay-In`=1:
  $$\text{Gini} = 0.4444, \quad H = 0.9183 \text{ bits}$$

* **Weighted Metrics for `Weather`:**
  $$\text{Weighted\_Gini}(\text{Weather}) = \frac{3}{10}(0.4444) + \frac{4}{10}(0.3750) + \frac{3}{10}(0.4444) = \mathbf{0.4167}$$
  $$\text{Gini\_Gain}(\text{Weather}) = 0.5800 - 0.4167 = \mathbf{0.1633}$$
  $$\text{Weighted\_Entropy}(\text{Weather}) = \frac{3}{10}(0.9183) + \frac{4}{10}(0.8113) + \frac{3}{10}(0.9183) = \mathbf{0.8755 \text{ bits}}$$
  $$\text{Gain}(\text{Weather}) = 1.5710 - 0.8755 = \mathbf{0.6955 \text{ bits}}$$

---

###### **3. Attribute `Money` `{Rich, Poor}`**
* `Poor` (3 instances: Rec 4, 6, 7) $\to$ All 3 are `Cinema` (Pure): $\text{Gini} = 0.0, H = 0.0$
* `Rich` (7 instances: Rec 1, 2, 3, 5, 8, 9, 10) $\to$ `Cinema`=3, `Tennis`=2, `Stay-In`=1, `Shopping`=1:
  $$\text{Gini} = 1 - [(3/7)^2 + (2/7)^2 + (1/7)^2 + (1/7)^2] = 0.6939, \quad H = 1.8424 \text{ bits}$$

* **Weighted Metrics for `Money`:**
  $$\text{Weighted\_Gini}(\text{Money}) = \frac{3}{10}(0) + \frac{7}{10}(0.6939) = \mathbf{0.4857} \implies \text{Gini\_Gain} = \mathbf{0.0943}$$
  $$\text{Weighted\_Entropy}(\text{Money}) = \frac{7}{10}(1.8424) = \mathbf{1.2897 \text{ bits}} \implies \text{Gain} = \mathbf{0.2813 \text{ bits}}$$

---

##### **Step 3: Comparison Summary Table**

| Attribute | Weighted Gini | Gini Gain ($\uparrow$) | Weighted Entropy | Information Gain ($\uparrow$) |
| :--- | :---: | :---: | :---: | :---: |
| **`Parents`** | **0.3600** | **0.2200 (BEST GINI)** | 0.9610 bits | 0.6100 bits |
| **`Weather`** | 0.4167 | 0.1633 | **0.8755 bits** | **0.6955 bits (BEST IG)** |
| **`Money`** | 0.4857 | 0.0943 | 1.2897 bits | 0.2813 bits |

* **Conclusion:** 
  * Under **Gini Impurity (CART)**, **`Parents`** is chosen as the root node because it yields the lowest weighted impurity ($0.3600$) and isolates a completely pure branch (`Parents == Yes`).
  * Under **Information Gain (ID3)**, **`Weather`** is chosen as the root node because it yields the highest overall entropy reduction ($0.6955 \text{ bits}$).

---

### ✍️ **Worked Example 4: The Classic 14-Day PlayTennis Dataset**
*(Standard Reference Textbook Benchmark - Russell & Norvig / Quinlan)*

#### **Problem Statement:**
Construct the complete ID3 Decision Tree for the benchmark 14-day `PlayTennis` dataset.

| Day | Outlook | Temperature | Humidity | Wind | PlayTennis |
| :---: | :--- | :--- | :--- | :--- | :---: |
| D1 | Sunny | Hot | High | Weak | No |
| D2 | Sunny | Hot | High | Strong | No |
| D3 | Overcast | Hot | High | Weak | Yes |
| D4 | Rain | Mild | High | Weak | Yes |
| D5 | Rain | Cool | Normal | Weak | Yes |
| D6 | Rain | Cool | Normal | Strong | No |
| D7 | Overcast | Cool | Normal | Strong | Yes |
| D8 | Sunny | Mild | High | Weak | No |
| D9 | Sunny | Cool | Normal | Weak | Yes |
| D10 | Rain | Mild | Normal | Weak | Yes |
| D11 | Sunny | Mild | Normal | Strong | Yes |
| D12 | Overcast | Mild | High | Strong | Yes |
| D13 | Overcast | Hot | Normal | Weak | Yes |
| D14 | Rain | Mild | High | Strong | No |

---

#### **Full Tracing Solution:**

1. **Parent Dataset $D$ ($N = 14$):** `Yes` = 9, `No` = 5.
   $$H(D) = - \left( \frac{9}{14} \log_2 \frac{9}{14} \right) - \left( \frac{5}{14} \log_2 \frac{5}{14} \right) = \mathbf{0.940 \text{ bits}}$$

2. **Root Feature Selection (Gain Calculations):**
   * $\text{Gain}(D, \text{Outlook}) = 0.940 - \left[ \frac{5}{14}(0.971) + \frac{4}{14}(0) + \frac{5}{14}(0.971) \right] = \mathbf{0.246 \text{ bits}}$
   * $\text{Gain}(D, \text{Humidity}) = 0.940 - \left[ \frac{7}{14}(0.985) + \frac{7}{14}(0.592) \right] = \mathbf{0.151 \text{ bits}}$
   * $\text{Gain}(D, \text{Wind}) = 0.940 - \left[ \frac{6}{14}(1.000) + \frac{8}{14}(0.811) \right] = \mathbf{0.048 \text{ bits}}$
   * $\text{Gain}(D, \text{Temperature}) = 0.940 - 0.911 = \mathbf{0.029 \text{ bits}}$

   $\implies$ **Root Node Selected: `Outlook`**

3. **Sub-node Splits:**
   * **`Outlook == Overcast` (4 instances: D3, D7, D12, D13):** All 4 are `Yes`. **Pure Leaf: YES**.
   * **`Outlook == Sunny` (5 instances: D1, D2, D8, D9, D11 - 2 Yes, 3 No):**
     * Evaluate remaining features `{Humidity, Wind, Temperature}`.
     * $\text{Gain}(D_{\text{Sunny}}, \text{Humidity}) = \mathbf{0.971 \text{ bits}}$ (Splits perfectly into `High` $\to$ `No`, `Normal` $\to$ `Yes`).
   * **`Outlook == Rain` (5 instances: D4, D5, D6, D10, D14 - 3 Yes, 2 No):**
     * Evaluate remaining features.
     * $\text{Gain}(D_{\text{Rain}}, \text{Wind}) = \mathbf{0.971 \text{ bits}}$ (Splits perfectly into `Weak` $\to$ `Yes`, `Strong` $\to$ `No`).

---

## SECTION 7: SUMMARY & QUICK REVISION

### 7.1 ID3 Quick Steps
1. Calculate overall **Parent Entropy** $H(S)$ of target class labels.
2. For every unused input attribute $A$:
   * Partition dataset $S$ into subsets $S_v$ for each feature value $v$.
   * Calculate subset entropies $H(S_v)$.
   * Compute weighted average entropy and subtract from parent entropy to get $\text{Gain}(S, A)$.
3. Select attribute with **maximum Information Gain** as decision node.
4. Split dataset and recursively repeat for child branches until pure or stopping criteria met.

---

### 7.2 Entropy & Information Gain Formula Cheat Sheet

$$\text{Entropy: } H(S) = - \sum_{i=1}^{k} p_i \log_2 (p_i)$$

$$\text{Weighted Entropy: } \text{Remainder}(S, A) = \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$

$$\text{Information Gain: } \text{Gain}(S, A) = H(S) - \text{Remainder}(S, A)$$

$$\text{Gini Impurity: } \text{Gini}(S) = 1 - \sum_{i=1}^{k} p_i^2$$

---

### 7.3 Common Exam Pitfalls (`⚠️ COMMON MISTAKES`)
* ⚠️ **Base-2 Logarithm Errors:** Forgetting that entropy uses $\log_2$ (not $\log_{10}$ or natural $\ln$). Remember $\log_2(x) = \frac{\ln(x)}{\ln(2)}$.
* ⚠️ **Handling Pure Subsets:** Forgetting that $0 \log_2(0) = 0$. If a branch has $0$ examples for a class, its contribution to entropy is $0$.
* ⚠️ **Weighted Average Weights:** Forgetting to multiply each subset's entropy by its branch fraction $\frac{|S_v|}{|S|}$ when calculating weighted entropy.
* ⚠️ **Misinterpreting Information Gain:** Selecting the lowest weighted entropy is equivalent to selecting the highest Information Gain. Do not accidentally select the smallest gain!

---

## SECTION 8: LAST-MINUTE EXAM CHECKLIST

- [x] Can define Inductive Bias and explain why learning requires bias.
- [x] Can compare Supervised, Unsupervised, and Reinforcement Learning in a structured table.
- [x] Know the components of a Decision Tree (Root, Decision Node, Branch, Leaf).
- [x] Can state the 3 base case stopping conditions of the ID3 algorithm.
- [x] Can write the formal pseudocode for ID3 decision tree induction.
- [x] Can calculate $H(S)$ using $-\sum p_i \log_2(p_i)$ for any multi-class distribution.
- [x] Can calculate Weighted Entropy and Information Gain for candidate split attributes.
- [x] Can extract IF-THEN classification rules from any completed decision tree diagram.
- [x] Can solve full 10-15 mark numericals step-by-step with complete calculation traces.

---
