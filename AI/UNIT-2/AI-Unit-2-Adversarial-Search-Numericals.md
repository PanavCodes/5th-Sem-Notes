# ARTIFICIAL INTELLIGENCE (AI) — UNIT 2: ADVERSARIAL SEARCH (GAME PLAYING)
## NUMERICAL & PROBLEM-SOLVING MASTER WORKBOOK
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## WORKBOOK OVERVIEW

This document is a comprehensive, numericals-only master study workbook for **Artificial Intelligence (AI) — Unit 2: Adversarial Search (Game Playing)**. Every problem in this workbook is drawn directly from official SVKM's NMIMS B.Tech CE end-semester examinations, re-examinations, Mumbai University (MU) question papers, and official course laboratory manuals.

Every solved problem provides:
1. **Original PYQ Metadata:** Exact exam name, year, mark allocation, and question text.
2. **Given Game Tree Diagram:** Clear ASCII structural representation of the game tree.
3. **MAX/MIN Level Mapping:** Explicit identification of player turns at every depth level.
4. **Traversal Order & Evaluation Log:** DFS traversal order with step-by-step node evaluations.
5. **$(\alpha, \beta)$ Bounds Tracking:** Explicit tracking of lower bound $\alpha$ and upper bound $\beta$ at every node visit and update.
6. **Pruning Justification:** Mathematical proof ($\alpha \ge \beta$) for every pruned branch.
7. **Final Decision & Path:** Exact root minimax utility score, optimal move for MAX, and the winning strategy path.

---

## SECTION 1: IMPORTANT NUMERICAL RULES & MATHEMATICAL FOUNDATIONS

Before solving exam numericals, memorize these core mathematical principles and operational definitions:

```text
┌───────────────────────────────────────────────────────────────────────────┐
│                      CORE MINIMAX & ALPHA-BETA RULES                     │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. MAX Node:                                                              │
│    • Objective: Maximize utility score.                                   │
│    • Value Update: v = MAX(v, child_value)                                │
│    • Alpha Update:  α = MAX(α, v)                                         │
│    • Bound Passed to Child: Inherits current (α, β) bounds.               │
│                                                                           │
│ 2. MIN Node:                                                              │
│    • Objective: Minimize utility score (adversary's optimal move).        │
│    • Value Update: v = MIN(v, child_value)                                │
│    • Beta Update:   β = MIN(β, v)                                         │
│    • Bound Passed to Child: Inherits current (α, β) bounds.               │
│                                                                           │
│ 3. Initial Root Bounds:                                                   │
│    • α = -∞ (worst possible score MAX can guarantee)                      │
│    • β = +∞ (worst possible score MIN can guarantee)                      │
│                                                                           │
│ 4. Pruning Condition (Alpha-Beta Cutoff):                                 │
│    • Prune immediately when:  α ≥ β                                       │
│    • Reason: Player will never allow the game to reach this state         │
│      because a better (or equal) alternative already exists.              │
│                                                                           │
│ 5. Value Equivalence Guarantee:                                           │
│    • Alpha-Beta Pruning MUST produce the exact same final root minimax    │
│      value and optimal decision as standard unpruned Minimax.              │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 2: ALL MINIMAX NUMERICAL PYQS

---

### **PROBLEM 1.1 [SVKM's NMIMS Final Exam 2022-23, Q5.B - 6 Marks]**
#### **Question Text:**
*"Perform Minimax algorithm on the following game tree to determine the optimal decision for player MAX at the root node. Show all intermediate calculations and node utility values."*

#### **Given Game Tree Structure:**
```text
                       [ A ] (MAX)
                      /     \
                     /       \
             [ B ] (MIN)     [ C ] (MIN)
             /     \         /     \
            /       \       /       \
        [D](MAX)   [E](MAX)[F](MAX)  [G](MAX)
        /   \      /   \   /   \     /   \
       3     5    6     9 1     2   0    -1
```

#### **Level Mapping:**
*   **Depth 0 (Root A):** MAX Player's turn ($\max$).
*   **Depth 1 (Nodes B, C):** MIN Player's turn ($\min$).
*   **Depth 2 (Nodes D, E, F, G):** MAX Player's turn ($\max$).
*   **Depth 3 (Leaves):** Terminal utility values.

#### **Step-by-Step Traversal & Value Propagation:**

1. **Evaluate Depth 2 MAX Nodes (Leaves to Depth 2):**
   * **Node D:** $\text{Utility}(D) = \max(3, 5) = \mathbf{5}$
   * **Node E:** $\text{Utility}(E) = \max(6, 9) = \mathbf{9}$
   * **Node F:** $\text{Utility}(F) = \max(1, 2) = \mathbf{2}$
   * **Node G:** $\text{Utility}(G) = \max(0, -1) = \mathbf{0}$

2. **Evaluate Depth 1 MIN Nodes (Depth 2 to Depth 1):**
   * **Node B:** Has children $D (5)$ and $E (9)$.  
     $$\text{Utility}(B) = \min(\text{Utility}(D), \text{Utility}(E)) = \min(5, 9) = \mathbf{5}$$
   * **Node C:** Has children $F (2)$ and $G (0)$.  
     $$\text{Utility}(C) = \min(\text{Utility}(F), \text{Utility}(G)) = \min(2, 0) = \mathbf{0}$$

3. **Evaluate Depth 0 MAX Root (Depth 1 to Root A):**
   * **Node A:** Has children $B (5)$ and $C (0)$.  
     $$\text{Utility}(A) = \max(\text{Utility}(B), \text{Utility}(C)) = \max(5, 0) = \mathbf{5}$$

#### **Final Solution Summary:**
*   **Final Root Utility Value:** $\mathbf{5}$
*   **Optimal Decision for MAX:** Move to **Node B** (Action $A \rightarrow B$).
*   **Optimal Game Path (Assuming Optimal Play):** $A \rightarrow B \rightarrow D \rightarrow \text{Leaf(5)}$.

---

### **PROBLEM 1.2 [SVKM's NMIMS Re-Exam 2022-23 / Class Notes - 10 Marks]**
#### **Question Text:**
*"Given the 4-ply game tree below, apply the Minimax procedure to calculate the minimax values for every node from leaves to root. Identify the winning strategy for player MAX."*

#### **Given Game Tree Structure:**
```text
                       [ A ] (MAX)
                      /     \
                     /       \
             [ B ] (MIN)     [ C ] (MIN)
             /     \         /     \
            /       \       /       \
        [D](MAX)   [E](MAX)[F](MAX)  [G](MAX)
        /   \      /   \   /   \     /   \
      -1     3    5     1 -6    -4  0     9
```

#### **Level Mapping:**
*   **Depth 0 (Root A):** MAX Player
*   **Depth 1 (Nodes B, C):** MIN Player
*   **Depth 2 (Nodes D, E, F, G):** MAX Player
*   **Depth 3 (Leaves):** Terminal Utility Scores

#### **Step-by-Step Calculations:**

1. **Depth 2 MAX Nodes:**
   * $\text{Utility}(D) = \max(-1, 3) = \mathbf{3}$
   * $\text{Utility}(E) = \max(5, 1) = \mathbf{5}$
   * $\text{Utility}(F) = \max(-6, -4) = \mathbf{-4}$
   * $\text{Utility}(G) = \max(0, 9) = \mathbf{9}$

2. **Depth 1 MIN Nodes:**
   * $\text{Utility}(B) = \min(\text{Utility}(D), \text{Utility}(E)) = \min(3, 5) = \mathbf{3}$
   * $\text{Utility}(C) = \min(\text{Utility}(F), \text{Utility}(G)) = \min(-4, 9) = \mathbf{-4}$

3. **Depth 0 Root MAX Node:**
   * $\text{Utility}(A) = \max(\text{Utility}(B), \text{Utility}(C)) = \max(3, -4) = \mathbf{3}$

#### **Final Solution Summary:**
*   **Root Minimax Value:** $\mathbf{3}$
*   **Optimal Action for MAX:** Choose left branch **$A \rightarrow B$**.
*   **Game Traversal Path:** $A \rightarrow B \rightarrow D \rightarrow 3$.

---

## SECTION 3: ALL ALPHA-BETA NUMERICAL PYQS

---

### **PROBLEM 2.1 [SVKM's NMIMS Final Exam 2024-25, Q2.c - 10 Marks]**
#### **Question Text:**
*"Apply Alpha-Beta Pruning on the following 4-level binary game tree. Show the step-by-step evaluation of each node, updated (α, β) values, pruned branches, justification for pruning, final root value, and the optimal move for MAX."*

#### **Given Game Tree Structure & Leaf Values:**
```text
                                        [ A ] (MAX)
                                       /           \
                                      /             \
                        [ B ] (MIN)                     [ C ] (MIN)
                       /           \                   /           \
                      /             \                 /             \
            [ D ] (MAX)             [ E ] (MAX)     [ F ] (MAX)     [ G ] (MAX)
           /           \           /         \     /         \     /         \
        [H](MIN)     [I](MIN)    [J](MIN)   [K](MIN)[L](MIN) [M](MIN)[N](MIN) [O](MIN)
        /   \        /   \       /   \      /   \   /   \    /   \   /   \    /   \
       8    23     -47   28    -30  -37    3   -41 -19   4 -49   4  43   45 -26  -14
```

#### **Level Mapping:**
*   **Depth 0 (Root A):** MAX Player ($\alpha = -\infty, \beta = +\infty$)
*   **Depth 1 (Nodes B, C):** MIN Player
*   **Depth 2 (Nodes D, E, F, G):** MAX Player
*   **Depth 3 (Nodes H, I, J, K, L, M, N, O):** MIN Player
*   **Depth 4 (Leaves):** 16 Terminal Utility Values

---

#### **Step-by-Step Execution Log with $(\alpha, \beta)$ Tracking:**

##### **Subtree Under Node B (Left Main Branch):**

1. **Node A (Root MAX):** Starts with $\alpha = -\infty, \beta = +\infty$. Calls `MIN-VALUE(B)`.
2. **Node B (MIN):** Inherits $\alpha = -\infty, \beta = +\infty$. Calls `MAX-VALUE(D)`.
3. **Node D (MAX):** Inherits $\alpha = -\infty, \beta = +\infty$. Calls `MIN-VALUE(H)`.
4. **Node H (MIN):** Inherits $\alpha = -\infty, \beta = +\infty$.
   * Evaluates leaf **8**: $v_H = \min(\infty, 8) = 8$. Updates $\beta = \min(\infty, 8) = 8$.
   * Evaluates leaf **23**: $v_H = \min(8, 23) = 8$.
   * Returns $v_H = \mathbf{8}$ to Node D.
5. **Node D (MAX):** Receives $v_H = 8$.
   * Updates $v_D = \max(-\infty, 8) = 8$.
   * Updates $\alpha = \max(-\infty, 8) = \mathbf{8}$.
   * Calls `MIN-VALUE(I)` with bounds **$\alpha = 8, \beta = +\infty$**.
6. **Node I (MIN):** Inherits $\alpha = 8, \beta = +\infty$.
   * Evaluates leaf **-47**: $v_I = \min(\infty, -47) = -47$.
   * Updates $\beta = \min(\infty, -47) = \mathbf{-47}$.
   * **PRUNING CHECK AT NODE I:**
     $$\text{Check: } \alpha \ge \beta \implies 8 \ge -47 \quad \mathbf{(TRUE!)}$$
   * ✂️ **PRUNING OCCURS AT NODE I!**
   * **Pruned Leaf:** **28** is **PRUNED** without evaluation!
   * Returns $v_I = \mathbf{-47}$ to Node D.
7. **Node D (MAX):** Receives $v_I = -47$. $v_D = \max(8, -47) = \mathbf{8}$.
   * Returns $v_D = \mathbf{8}$ to Node B.
8. **Node B (MIN):** Receives $v_D = 8$.
   * Updates $v_B = \min(\infty, 8) = 8$.
   * Updates $\beta = \min(\infty, 8) = \mathbf{8}$.
   * Calls `MAX-VALUE(E)` with bounds **$\alpha = -\infty, \beta = 8$**.

9. **Node E (MAX):** Inherits $\alpha = -\infty, \beta = 8$. Calls `MIN-VALUE(J)`.
10. **Node J (MIN):** Inherits $\alpha = -\infty, \beta = 8$.
    * Evaluates leaf **-30**: $v_J = -30, \beta = -30$.
    * Evaluates leaf **-37**: $v_J = \min(-30, -37) = -37$.
    * Returns $v_J = \mathbf{-37}$ to Node E.
11. **Node E (MAX):** Receives $v_J = -37$.
    * Updates $v_E = \max(-\infty, -37) = -37$.
    * Updates $\alpha = \max(-\infty, -37) = -37$. (Current bounds: $\alpha = -37, \beta = 8$).
    * Calls `MIN-VALUE(K)` with bounds **$\alpha = -37, \beta = 8$**.
12. **Node K (MIN):** Inherits $\alpha = -37, \beta = 8$.
    * Evaluates leaf **3**: $v_K = 3, \beta = \min(8, 3) = 3$. ($\alpha = -37 < \beta = 3 \implies$ No prune).
    * Evaluates leaf **-41**: $v_K = \min(3, -41) = -41, \beta = -41$.
    * Returns $v_K = \mathbf{-41}$ to Node E.
13. **Node E (MAX):** Receives $v_K = -41$. $v_E = \max(-37, -41) = \mathbf{-37}$.
    * Returns $v_E = \mathbf{-37}$ to Node B.
14. **Node B (MIN):** Receives $v_E = -37$.
    * Updates $v_B = \min(8, -37) = \mathbf{-37}$.
    * Returns $v_B = \mathbf{-37}$ to Root Node A.

---

##### **Subtree Under Node C (Right Main Branch):**

15. **Node A (Root MAX):** Receives $v_B = -37$.
    * Updates $v_A = \max(-\infty, -37) = -37$.
    * Updates $\alpha = \max(-\infty, -37) = \mathbf{-37}$.
    * Calls `MIN-VALUE(C)` with bounds **$\alpha = -37, \beta = +\infty$**.

16. **Node C (MIN):** Inherits $\alpha = -37, \beta = +\infty$. Calls `MAX-VALUE(F)`.
17. **Node F (MAX):** Inherits $\alpha = -37, \beta = +\infty$. Calls `MIN-VALUE(L)`.
18. **Node L (MIN):** Inherits $\alpha = -37, \beta = +\infty$.
    * Evaluates leaf **-19**: $v_L = -19, \beta = -19$.
    * Evaluates leaf **4**: $v_L = \min(-19, 4) = -19$.
    * Returns $v_L = \mathbf{-19}$ to Node F.
19. **Node F (MAX):** Receives $v_L = -19$.
    * Updates $v_F = \max(-\infty, -19) = -19$.
    * Updates $\alpha = \max(-37, -19) = \mathbf{-19}$.
    * Calls `MIN-VALUE(M)` with bounds **$\alpha = -19, \beta = +\infty$**.
20. **Node M (MIN):** Inherits $\alpha = -19, \beta = +\infty$.
    * Evaluates leaf **-49**: $v_M = -49$. Updates $\beta = \min(\infty, -49) = \mathbf{-49}$.
    * **PRUNING CHECK AT NODE M:**
      $$\text{Check: } \alpha \ge \beta \implies -19 \ge -49 \quad \mathbf{(TRUE!)}$$
    * ✂️ **PRUNING OCCURS AT NODE M!**
    * **Pruned Leaf:** **4** is **PRUNED** without evaluation!
    * Returns $v_M = \mathbf{-49}$ to Node F.
21. **Node F (MAX):** Receives $v_M = -49$. $v_F = \max(-19, -49) = \mathbf{-19}$.
    * Returns $v_F = \mathbf{-19}$ to Node C.

22. **Node C (MIN):** Receives $v_F = -19$.
    * Updates $v_C = \min(\infty, -19) = -19$.
    * Updates $\beta = \min(\infty, -19) = \mathbf{-19}$.
    * Current bounds at Node C: **$\alpha = -37, \beta = -19$**.
    * Calls `MAX-VALUE(G)` with bounds **$\alpha = -37, \beta = -19$**.

23. **Node G (MAX):** Inherits $\alpha = -37, \beta = -19$. Calls `MIN-VALUE(N)`.
24. **Node N (MIN):** Inherits $\alpha = -37, \beta = -19$.
    * Evaluates leaf **43**: $v_N = 43, \beta = \min(-19, 43) = -19$.
    * Evaluates leaf **45**: $v_N = \min(43, 45) = 43$.
    * Returns $v_N = \mathbf{43}$ to Node G.
25. **Node G (MAX):** Receives $v_N = 43$.
    * Updates $v_G = \max(-\infty, 43) = 43$.
    * Updates $\alpha = \max(-37, 43) = \mathbf{43}$.
    * **PRUNING CHECK AT NODE G:**
      $$\text{Check: } \alpha \ge \beta \implies 43 \ge -19 \quad \mathbf{(TRUE!)}$$
    * ✂️ **DEEP PRUNING OCCURS AT NODE G!**
    * **Pruned Subtree:** Entire Node **O** and its leaves (**-26, -14**) are **PRUNED** without evaluation!
    * Returns $v_G = \mathbf{43}$ to Node C.

26. **Node C (MIN):** Receives $v_G = 43$. $v_C = \min(-19, 43) = \mathbf{-19}$.
    * Returns $v_C = \mathbf{-19}$ to Root Node A.

27. **Node A (Root MAX):** Receives $v_C = -19$.
    * Updates $v_A = \max(-37, -19) = \mathbf{-19}$.

---

#### **Detailed Pruning Summary Table:**

| Cutoff # | Node Where Prune Occurred | Current Bounds $(\alpha, \beta)$ | Pruning Condition | Pruned Leaves / Subtrees | Reason |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Node I** (MIN) | $\alpha = 8, \beta = -47$ | $\alpha \ge \beta \ (8 \ge -47)$ | Leaf **28** | MIN will never allow a score $> -47$ here, but MAX can already achieve 8 via Node H. |
| **2** | **Node M** (MIN) | $\alpha = -19, \beta = -49$ | $\alpha \ge \beta \ (-19 \ge -49)$ | Leaf **4** | MIN will never allow a score $> -49$ here, but MAX can already achieve -19 via Node L. |
| **3** | **Node G** (MAX) | $\alpha = 43, \beta = -19$ | $\alpha \ge \beta \ (43 \ge -19)$ | Subtree **O** (Leaves **-26, -14**) | MAX guarantees at least 43 at Node G, but MIN at Node C will never choose G because C already has a score of -19. |

#### **Final Solution Summary:**
*   **Final Root Minimax Utility Value:** $\mathbf{-19}$
*   **Optimal Decision for MAX:** Choose right branch **$A \rightarrow C$**.
*   **Total Leaves Evaluated:** 12 out of 16 (4 leaves saved/pruned).
*   **Pruned Leaves List:** **`[28, 4, -26, -14]`**

---

### **PROBLEM 2.2 [Mumbai University Dec 2023 / Dec 2021 / AIMA Classic - 10 Marks]**
#### **Question Text:**
*"Trace the Alpha-Beta Pruning search process for the following game tree. Show the values of α and β at each step, list all pruned nodes, and state the final root value."*

#### **Given Game Tree Structure:**
```text
                          [ A ] (MAX)
                       /       |       \
                      /        |        \
              [ B ] (MIN)  [ C ] (MIN)  [ D ] (MIN)
              /   |   \    /   |   \    /   |   \
             3   12    8  2    4    6  14   5    2
```

#### **Step-by-Step Execution Log:**

1. **Root A (MAX):** Starts with $\alpha = -\infty, \beta = +\infty$. Calls `MIN-VALUE(B)`.
2. **Node B (MIN):** Inherits $\alpha = -\infty, \beta = +\infty$.
   * Evaluates leaf **3**: $v_B = 3, \beta = 3$.
   * Evaluates leaf **12**: $v_B = \min(3, 12) = 3$.
   * Evaluates leaf **8**: $v_B = \min(3, 8) = 3$.
   * Returns $v_B = \mathbf{3}$ to Root A.
3. **Root A (MAX):** Receives $v_B = 3$.
   * Updates $v_A = \max(-\infty, 3) = 3$.
   * Updates $\alpha = \max(-\infty, 3) = \mathbf{3}$.
   * Calls `MIN-VALUE(C)` with bounds **$\alpha = 3, \beta = +\infty$**.

4. **Node C (MIN):** Inherits $\alpha = 3, \beta = +\infty$.
   * Evaluates leaf **2**: $v_C = 2, \beta = \min(\infty, 2) = \mathbf{2}$.
   * **PRUNING CHECK AT NODE C:**
     $$\text{Check: } \alpha \ge \beta \implies 3 \ge 2 \quad \mathbf{(TRUE!)}$$
   * ✂️ **PRUNING OCCURS AT NODE C!**
   * **Pruned Leaves:** Leaves **4** and **6** are **PRUNED**!
   * Returns $v_C = \mathbf{2}$ to Root A.

5. **Root A (MAX):** Receives $v_C = 2$.
   * $v_A = \max(3, 2) = 3$. $\alpha$ remains **3**.
   * Calls `MIN-VALUE(D)` with bounds **$\alpha = 3, \beta = +\infty$**.

6. **Node D (MIN):** Inherits $\alpha = 3, \beta = +\infty$.
   * Evaluates leaf **14**: $v_D = 14, \beta = 14$. ($\alpha = 3 < \beta = 14 \implies$ No prune).
   * Evaluates leaf **5**: $v_D = \min(14, 5) = 5, \beta = 5$. ($\alpha = 3 < \beta = 5 \implies$ No prune).
   * Evaluates leaf **2**: $v_D = \min(5, 2) = 2, \beta = 2$.
   * **PRUNING CHECK AT NODE D:**
     $$\text{Check: } \alpha \ge \beta \implies 3 \ge 2 \quad \mathbf{(TRUE!)}$$
   * *(Note: All leaves of D were evaluated; pruning condition triggers at the boundary).*
   * Returns $v_D = \mathbf{2}$ to Root A.

7. **Root A (MAX):** Receives $v_D = 2$. $v_A = \max(3, 2) = \mathbf{3}$.

#### **Final Solution Summary:**
*   **Final Root Utility Score:** $\mathbf{3}$
*   **Optimal Decision for MAX:** Move to **Node B** ($A \rightarrow B$).
*   **Pruned Leaves:** Leaves **4** and **6** under Node C.
*   **Total Leaves Evaluated:** 7 out of 9 (2 leaves pruned).

---

### **PROBLEM 2.3 [Comparative Analysis: Left-to-Right vs Right-to-Left Traversal - 10 Marks]**
#### **Question Text:**
*"Demonstrate how the direction of tree traversal impacts the efficiency of Alpha-Beta Pruning using the game tree below. Compare the number of pruned nodes under (a) Left-to-Right Traversal vs. (b) Right-to-Left Traversal."*

```text
                       [ A ] (MAX)
                      /     \
                     /       \
             [ B ] (MIN)     [ C ] (MIN)
             /     \         /     \
            /       \       /       \
        [D](MAX)   [E](MAX)[F](MAX)  [G](MAX)
        /   \      /   \   /   \     /   \
       5     6    7     4 2     1   8     3
```

#### **Part (a): Left-to-Right Traversal Execution**

1. **Root A (MAX):** $\alpha = -\infty, \beta = +\infty$.
2. **Node B (MIN):** Calls D.
   * **Node D (MAX):** Leaves 5, 6 $\implies v_D = \max(5, 6) = 6$. Updates $\alpha = 6$.
   * **Node B (MIN):** Updates $\beta = 6$. Calls E with $\alpha = -\infty, \beta = 6$.
   * **Node E (MAX):** Leaf 7 $\implies v_E = 7, \alpha = 7$.
     $$\text{Check: } \alpha \ge \beta \implies 7 \ge 6 \quad \mathbf{(TRUE!)}$$
     ✂️ **Leaf 4 is PRUNED!** Returns $v_E = 7$.
   * **Node B (MIN):** $v_B = \min(6, 7) = 6$.
3. **Root A (MAX):** $v_A = 6, \alpha = 6$. Calls C with $\alpha = 6, \beta = +\infty$.
4. **Node C (MIN):** Calls F.
   * **Node F (MAX):** Leaves 2, 1 $\implies v_F = \max(2, 1) = 2$.
   * **Node C (MIN):** $v_C = 2, \beta = 2$.
     $$\text{Check: } \alpha \ge \beta \implies 6 \ge 2 \quad \mathbf{(TRUE!)}$$
     ✂️ **Node G and its leaves (8, 3) are PRUNED!**
5. **Root A (MAX):** $v_A = \max(6, 2) = \mathbf{6}$.

*   **Pruned Leaves (Left-to-Right):** **`[4, 8, 3]`** (3 leaves pruned).

---

#### **Part (b): Right-to-Left Traversal Execution**

1. **Root A (MAX):** $\alpha = -\infty, \beta = +\infty$.
2. **Node C (MIN):** Calls G first.
   * **Node G (MAX):** Leaves 3, 8 $\implies v_G = \max(3, 8) = 8$.
   * **Node C (MIN):** $v_C = 8, \beta = 8$. Calls F with $\alpha = -\infty, \beta = 8$.
   * **Node F (MAX):** Leaves 1, 2 $\implies v_F = \max(1, 2) = 2$.
   * **Node C (MIN):** $v_C = \min(8, 2) = 2$.
3. **Root A (MAX):** $v_A = 2, \alpha = 2$. Calls B with $\alpha = 2, \beta = +\infty$.
4. **Node B (MIN):** Calls E first.
   * **Node E (MAX):** Leaves 4, 7 $\implies v_E = \max(4, 7) = 7$.
   * **Node B (MIN):** $v_B = 7, \beta = 7$. Calls D with $\alpha = 2, \beta = 7$.
   * **Node D (MAX):** Leaves 6, 5 $\implies v_D = \max(6, 5) = 6$.
   * **Node B (MIN):** $v_B = \min(7, 6) = 6$.
5. **Root A (MAX):** $v_A = \max(2, 6) = \mathbf{6}$.

*   **Pruned Leaves (Right-to-Left):** **`[]`** (0 leaves pruned!).

---

#### **Comparison & Takeaway Table:**

| Metric | Left-to-Right Traversal | Right-to-Left Traversal | Impact / Analysis |
| :--- | :---: | :---: | :--- |
| **Final Root Value** | **6** | **6** | Identical minimax result guaranteed. |
| **Optimal Move** | Move to **Node B** | Move to **Node B** | Identical decision path. |
| **Leaves Evaluated** | **5** out of 8 | **8** out of 8 | Left-to-right is 37.5% faster. |
| **Pruned Leaves** | **3** (`4, 8, 3`) | **0** | Move ordering determines pruning efficiency! |

---

## SECTION 4: MOST REPEATED NUMERICAL PATTERNS

```text
┌───────────────────────────────────────────────────────────────────────────┐
│                    TOP 5 EXAM NUMERICAL PATTERNS                         │
├───────────────────────────────────────────────────────────────────────────┤
│ Pattern 1: 4-Level Deep Pruning Binary Tree (16 Leaves)                   │
│   • Frequency: SVKM's NMIMS Final Exam 2024-25, 2022-23 (10 Marks).      │
│   • Core Trick: Includes both shallow MIN cutoffs and deep MAX cutoffs.   │
│                                                                           │
│ Pattern 2: 3-Level Standard Minimax & Alpha-Beta Game Tree                │
│   • Frequency: SVKM's NMIMS Midterms & Re-Exams (6 to 10 Marks).         │
│   • Core Trick: Simple 2-ply or 3-ply tree testing basic propagation.     │
│                                                                           │
│ Pattern 3: AIMA Classic 3-Branch Tree                                     │
│   • Frequency: Mumbai University 2023, 2021, 2018 (10 Marks).             │
│   • Core Trick: Branch C gets pruned on the very first leaf!              │
│                                                                           │
│ Pattern 4: Minimax vs. Alpha-Beta Value Equivalence Proof                 │
│   • Frequency: Standard 10-mark university question pairing both methods. │
│   • Core Trick: Proving both methods arrive at the identical root score.  │
│                                                                           │
│ Pattern 5: Traversal Direction / Move Ordering Comparison                 │
│   • Frequency: Conceptual numericals (10 Marks).                          │
│   • Core Trick: Demonstrating how ordering best-first vs worst-first      │
│     changes leaf evaluation counts from O(b^{m/2}) to O(b^m).            │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 5: COMMON NUMERICAL MISTAKES & EXAM PITFALLS

```text
❌ MISTAKE 1: Confusing MAX and MIN Levels during Propagation
   • Error: Taking max() at a MIN level or min() at a MAX level.
   • Fix: Always write "MAX" or "MIN" next to every level before starting!

❌ MISTAKE 2: Forgetting to Inherit Parent Bounds (α, β)
   • Error: Resetting α = -∞ and β = +∞ at every child node.
   • Fix: Child nodes ALWAYS inherit their parent's current (α, β) values!

❌ MISTAKE 3: Using Strict Inequality for Pruning Cutoff
   • Error: Pruning only when α > β instead of α ≥ β.
   • Fix: Prune immediately when α EQUALS β (α ≥ β)!

❌ MISTAKE 4: Updating the Wrong Bound Variable
   • Error: Updating α at a MIN node or updating β at a MAX node.
   • Fix: Remember: MAX nodes ONLY update α; MIN nodes ONLY update β!

❌ MISTAKE 5: Expecting Alpha-Beta to Yield a Different Root Value
   • Error: Changing the root score because pruning occurred.
   • Fix: Alpha-Beta MUST yield the EXACT same root value as Minimax!
```

---

## SECTION 6: QUICK SOLVING PROCEDURE FOR EXAM PAPER

```text
┌───────────────────────────────────────────────────────────────────────────┐
│              STEP-BY-STEP EXAM SOLVING ALGORITHM FOR NUMERICALS           │
├───────────────────────────────────────────────────────────────────────────┤
│ STEP 1: Label All Levels                                                  │
│   • Mark Level 0 = MAX, Level 1 = MIN, Level 2 = MAX, etc.                │
│                                                                           │
│ STEP 2: Write Initial Bounds at Root                                      │
│   • Set α = -∞ and β = +∞ at Root Node A.                                 │
│                                                                           │
│ STEP 3: Traverse Depth-First (Left-to-Right by Default)                   │
│   • Pass (α, β) bounds downward to children.                              │
│                                                                           │
│ STEP 4: Evaluate Leaf Nodes & Return Utility Upward                       │
│   • At MIN node: v = MIN(v, leaf_val), β = MIN(β, v).                     │
│   • At MAX node: v = MAX(v, leaf_val), α = MAX(α, v).                     │
│                                                                           │
│ STEP 5: Perform Cutoff Check at EVERY Value Update                        │
│   • If α ≥ β: STOP evaluating remaining children of this node!            │
│   • Draw a clear 'X' or dashed line across pruned subtrees.               │
│   • Write pruning reason: "Pruned at Node X because α (val1) ≥ β (val2)". │
│                                                                           │
│ STEP 6: Summarize Final Results                                           │
│   • Final Root Minimax Score = X.                                         │
│   • Optimal Move for MAX = Action A → Y.                                  │
│   • List of Pruned Leaves/Subtrees = [...].                               │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 7: LAST-MINUTE NUMERICAL CHECKLIST

- [ ] **Level Check:** Did I correctly alternate MAX and MIN levels from root to leaves?
- [ ] **Inheritance Check:** Did child nodes inherit their parent's active $(\alpha, \beta)$ bounds?
- [ ] **Update Check:** Did MAX nodes update *only* $\alpha$, and MIN nodes update *only* $\beta$?
- [ ] **Pruning Check:** Did I apply the cutoff as soon as $\alpha \ge \beta$?
- [ ] **Pruning Justification:** Did I write the explicit numeric inequality $(\alpha \ge \beta)$ for every cutoff?
- [ ] **Root Equivalence:** Does my Alpha-Beta root value match unpruned Minimax?
- [ ] **Optimal Move:** Did I clearly state which move MAX should select at the root?

---

## SECTION 8: COMPLETE PYQ COVERAGE CHECKLIST

- [x] **Problem 1.1:** SVKM's NMIMS Final Exam 2022-23 Minimax Numerical (6 Marks)
- [x] **Problem 1.2:** SVKM's NMIMS Re-Exam 2022-23 / Class Notes 4-Ply Minimax (10 Marks)
- [x] **Problem 2.1:** SVKM's NMIMS Final Exam 2024-25 Alpha-Beta Pruning 16-Leaf Tree (10 Marks)
- [x] **Problem 2.2:** Mumbai University Dec 2023 / AIMA Classic 3-Branch Tree (10 Marks)
- [x] **Problem 2.3:** Left-to-Right vs Right-to-Left Move Ordering Numerical (10 Marks)
- [x] **Minimax tree evaluation:** Fully covered with step-by-step MAX/MIN calculations.
- [x] **MAX/MIN propagation:** Fully demonstrated with mathematical formulas.
- [x] **DFS traversal:** Detailed log provided for every node expansion.
- [x] **Alpha-Beta values:** $(\alpha, \beta)$ bounds tracked at every step.
- [x] **Pruning condition:** $\alpha \ge \beta$ verified at every cutoff.
- [x] **Pruned branches:** Every pruned leaf explicitly listed with reasons.
- [x] **Final optimal move:** Selected root action identified for every problem.
