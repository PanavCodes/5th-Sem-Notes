# ARTIFICIAL INTELLIGENCE (AI) — UNIT 2: ADVERSARIAL SEARCH (GAME PLAYING)
## PAST YEAR QUESTION (PYQ) & EXAM-ORIENTED MASTER STUDY BANK
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## DOCUMENT OVERVIEW

This document is a comprehensive, exam-oriented Past Year Question (PYQ) study bank for **Artificial Intelligence (AI) — Unit 2: Adversarial Search (Game Playing)**. All questions are drawn directly from official SVKM's NMIMS B.Tech CE end-semester examinations, re-examinations, Mumbai University (MU) question papers, and official laboratory manuals.

Every section includes:
* **Genuine PYQs** with original wording and year/exam source metadata.
* **Grouped Repeated & Concept-Equivalent Questions** mapped to a single Adaptable Master Model Answer.
* **Step-by-Step Fully Solved Numerical PYQs** with complete tree structures, traversal logs, $(\alpha, \beta)$ bounds tracking, pruning justifications, root values, and optimal move decisions.
* **Final Revision & Exam-Day Checklist** formatted for quick review.

---

## SECTION 1: TOPIC-WISE PAST YEAR QUESTIONS & MASTER MODEL ANSWERS

---

### TOPIC 1: GAME DOMAIN & PROBLEM FORMULATION

#### **1.1 Grouped & Repeated PYQs**

* **Question 1.1a (Lab Exp 4 / Theory Paper):**  
  *"Differentiate between state space search (single-agent search) and adversarial search (game playing). What are the key characteristics of a two-player, zero-sum, perfect-information game?"*  
  — **Source:** SVKM's NMIMS Lab Manual Exp 4 | MU Dec 2014 [5 Marks] / May 2018 [5 Marks]

* **Question 1.1b (SVKM's NMIMS Re-Exam 2022-23, Q2.A):**  
  *"Explain different types of environments with suitable examples in the context of game playing and adversarial search."*  
  — **Source:** SVKM's NMIMS Re-Exam 2022-23, Q2.A [10 Marks]

* **Question 1.1c (MU May 2023 / Dec 2023):**  
  *"Define Game Playing in AI. What are the formal components required to formulate a game as a search problem? Explain with Tic-Tac-Toe."*  
  — **Source:** Mumbai University (MU), May 2023 [5 Marks], Dec 2023 [5 Marks]

---

#### **Master Model Answer (Topic 1)**

##### **1. Concept & Definition**
An **Adversarial Search Problem** (Game) is a search environment involving multiple competitive agents with conflicting goals. Unlike single-agent state-space search (where the agent plans a path in a passive environment), adversarial search must account for an active opponent who makes moves to minimize the agent's success.

##### **2. Key Characteristics of Classical Game Domains**
1. **Two-Player System:** The game involves exactly two opponents who alternate turns:
   * **MAX:** The maximizing player who attempts to maximize the final utility.
   * **MIN:** The minimizing player (the adversary) who attempts to minimize MAX's final utility.
2. **Zero-Sum Property:** The total utility payoff across both players is constant for any final state:
   $$\text{Utility}(\text{MAX}) + \text{Utility}(\text{MIN}) = 0$$
   Any gain by MAX represents an equal and opposite loss for MIN. No cooperation or win-win outcome is possible.
3. **Perfect Information:** The game environment is **fully observable**. Both players have complete visibility of the entire state space at all times (no hidden cards, fog of war, or concealed information).
4. **Deterministic Transitions:** Every legal action from a state leads to a single, deterministic outcome with zero randomness (no dice rolls or chance elements).

##### **3. Comparison: State-Space Search vs. Adversarial Search**

| Feature / Dimension | Single-Agent State-Space Search (e.g., $A^*$, BFS) | Adversarial Search (Game Playing) |
| :--- | :--- | :--- |
| **Environment Type** | Passive, static, non-competitive | Active, competitive, adversarial |
| **Agent Goal** | Find an optimal path from Start to Goal | Choose optimal move against an optimal adversary |
| **Control / Turn** | Single agent executes consecutive steps | Alternating turns between MAX and MIN |
| **Solution Type** | Sequence of actions (a path) | Strategy / Contingency Policy (response to any opponent move) |
| **Time Constraint** | Offline planning before execution | Real-time decision making per turn (strict move clock) |

##### **4. Formal 6-Tuple Game Problem Formulation**
A game is formally defined as a search problem using a 6-tuple $\langle s_0, \text{PLAYER}, \text{ACTIONS}, \text{RESULT}, \text{TERMINAL-TEST}, \text{UTILITY}\rangle$:

1. **Initial State ($s_0$):** Specifies the initial board setup and identifies which player moves first (e.g., empty $3 \times 3$ grid in Tic-Tac-Toe with MAX playing 'X').
2. **$\text{PLAYER}(s)$:** Identifies whose turn it is to move in state $s$ ($\text{MAX}$ or $\text{MIN}$).
3. **$\text{ACTIONS}(s)$:** Returns the set of all legal moves available to $\text{PLAYER}(s)$ in state $s$.
4. **$\text{RESULT}(s, a)$:** The transition model returning the new state $s'$ resulting from executing action $a$ in state $s$.
5. **$\text{TERMINAL-TEST}(s)$:** A boolean function returning `True` if the game has ended (win, loss, or draw), and `False` otherwise. States where the game ends are called **terminal states**.
6. **$\text{UTILITY}(s, p)$:** The objective/payoff function that assigns a numeric value to a terminal state $s$ for player $p$:
   * In Tic-Tac-Toe: $+1$ (MAX wins), $-1$ (MIN wins), $0$ (Draw).

```
                      [ Initial State s0 ] (MAX's Turn: 'X')
                      /        |        \
                     /         |         \
                 [Move 1]   [Move 2]   [Move 3]
                   /           |           \
            (MIN: 'O')     (MIN: 'O')    (MIN: 'O')
               /               |              \
             ...              ...             ...
            /                  |                \
    [Terminal: +1]      [Terminal: 0]     [Terminal: -1]
     (MAX Wins)           (Draw)           (MIN Wins)
```

---

### TOPIC 2: OPTIMAL DECISIONS IN GAMES & MINIMAX ALGORITHM

#### **2.1 Grouped & Repeated PYQs**

* **Question 2.1a (SVKM's NMIMS Final Exam 2022-23, Q5.B):**  
  *"Perform Minimax on following tree. Write Mini-Max algorithm."*  
  — **Source:** SVKM's NMIMS Final Exam 2022-23, Q5.B [6+4 = 10 Marks]

* **Question 2.1b (MU May 2024, Q.10):**  
  *"What Do You Understand By Min Max Search ? Explain in Detail With Example."*  
  — **Source:** Mumbai University (MU), May 2024 [10 Marks]

* **Question 2.1c (GTU / MU Previous Years):**  
  *"Explain the MiniMax search procedure for Game Playing using a suitable example. State its time and space complexity."*  
  — **Source:** University Examination Question Bank [7/10 Marks]

---

#### **Master Model Answer (Topic 2)**

##### **1. Definition & Purpose**
The **Minimax Algorithm** is a recursive depth-first backtracking algorithm used in two-player, turn-based, zero-sum, perfect-information games. Its purpose is to determine the **optimal move** for the MAX player by working backward from terminal states, under the assumption that the adversary (MIN player) also plays perfectly to minimize MAX's score.

##### **2. Working Principle & Value Propagation**
Minimax constructs a game tree from the current board position down to terminal states (or a fixed depth limit). 
Values are computed bottom-up according to the following recursive definition:

$$\text{MINIMAX}(n) = \begin{cases} 
\text{UTILITY}(n) & \text{if } \text{TERMINAL-TEST}(n) \text{ is True} \\[6pt]
\max_{s \in \text{SUCCESSORS}(n)} \text{MINIMAX}(s) & \text{if } \text{PLAYER}(n) = \text{MAX} \\[6pt]
\min_{s \in \text{SUCCESSORS}(n)} \text{MINIMAX}(s) & \text{if } \text{PLAYER}(n) = \text{MIN}
\end{cases}$$

* **MAX Levels:** Select the **maximum** utility value among all child nodes ($\max$).
* **MIN Levels:** Select the **minimum** utility value among all child nodes ($\min$).

##### **3. Complete Minimax Pseudocode**

```python
function MINIMAX-DECISION(state) returns an action
    # Returns the action that leads to the child with the highest minimax value
    best_score = -infinity
    best_action = None
    for each action in ACTIONS(state):
        v = MIN-VALUE(RESULT(state, action))
        if v > best_score:
            best_score = v
            best_action = action
    return best_action

function MAX-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v = -infinity
    for each s in SUCCESSORS(state) do
        v = MAX(v, MIN-VALUE(s))
    return v

function MIN-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v = +infinity
    for each s in SUCCESSORS(state) do
        v = MIN(v, MAX-VALUE(s))
    return v
```

##### **4. Complexity Analysis**
* **Time Complexity:** $\mathcal{O}(b^m)$, where $b$ is the legal branching factor and $m$ is the maximum depth of the game tree. Minimax must explore every node in the game tree down to leaf nodes.
* **Space Complexity:** $\mathcal{O}(b \cdot m)$, because search is performed depth-first, requiring storage only for the current active search path and unexpanded siblings.

##### **5. Advantages & Limitations**
* **Advantages:**
  * Guaranteed to find the mathematically optimal move against an optimal opponent.
  * Simple to implement using recursive depth-first search.
* **Limitations:**
  * **Exponential Time Complexity:** Complete tree traversal is computationally impossible for complex games like Chess ($b \approx 35, m \approx 80 \implies 35^{80}$ states) or Go.
  * **Requires Optimization:** Must be paired with depth-limited cutoffs, heuristic evaluation functions, or pruning techniques (Alpha-Beta Pruning).

---

### TOPIC 3: ALPHA-BETA PRUNING

#### **3.1 Grouped & Repeated PYQs**

* **Question 3.1a (MU May-23, Dec-23, May-24, May-25):**  
  *"Explain Alpha Beta Pruning With Example. Write the Alpha Beta Search Algorithm."*  
  — **Source:** Mumbai University (MU), May 2023, Dec 2023, May 2024, May 2025 [10 Marks]

* **Question 3.1b (SVKM's NMIMS Re-Exam 2022-23, Q3.B):**  
  *"Write alpha - beta pruning algorithm. Solve following using alpha - beta pruning."*  
  — **Source:** SVKM's NMIMS Re-Exam 2022-23, Q3.B [4+6 = 10 Marks]

* **Question 3.1c (Lab Exp 4 / Reference Question):**  
  *"What is the significance of Alpha and Beta cut-offs? How does Alpha-Beta Pruning improve the time complexity of Minimax search?"*  
  — **Source:** SVKM's NMIMS Lab Manual Exp 4 | MU Dec 2017 [5 Marks]

---

#### **Master Model Answer (Topic 3)**

##### **1. Definition & Need for Pruning**
**Alpha-Beta Pruning** is an optimization technique applied to the Minimax algorithm that eliminates (prunes) branches of the game tree that are guaranteed not to affect the final decision at the root.

By ignoring irrelevant subtrees, Alpha-Beta Pruning returns the **exact same optimal decision as standard Minimax**, but in a fraction of the time.

##### **2. Meaning of Alpha ($\alpha$) and Beta ($\beta$) Parameters**
During the depth-first search traversal, two bounds are passed down and updated:
* **$\alpha$ (Alpha):** The value of the **best (highest) choice** found so far along the search path for **MAX**. 
  * Initial value: $\alpha = -\infty$.
  * Updated **only at MAX nodes**. MAX will never accept a move yielding less than $\alpha$.
* **$\beta$ (Beta):** The value of the **best (lowest) choice** found so far along the search path for **MIN**.
  * Initial value: $\beta = +\infty$.
  * Updated **only at MIN nodes**. MIN will never accept a move yielding more than $\beta$.

##### **3. Pruning Conditions & Cutoffs**
At any node in the game tree, if the following condition holds:
$$\alpha \ge \beta$$

Search below the current node is **stopped immediately** (pruned).

1. **Alpha Cutoff (at MIN Node):** Occurs when a MIN node finds a child value $v \le \alpha$. Since MAX already has a guaranteed path yielding $\alpha$ elsewhere, MAX will never allow the game to enter this MIN branch.
2. **Beta Cutoff (at MAX Node):** Occurs when a MAX node finds a child value $v \ge \beta$. Since MIN already has a guaranteed path yielding $\beta$ elsewhere, MIN will never allow MAX to reach this state.

```
            [ MAX Node ]  (Alpha = 5)
                 /  \
                /    \
  (Guaranteed 5)    [ MIN Node ]  (Beta = 3)
                          \
                         [ Child = 3 ]  ==> PRUNE REMAINING SIBLINGS!
                                            Because Alpha (5) >= Beta (3)
```

##### **4. Complete Alpha-Beta Pruning Pseudocode**

```python
function ALPHA-BETA-SEARCH(state) returns an action
    v = MAX-VALUE(state, -infinity, +infinity)
    return action in ACTIONS(state) with value v

function MAX-VALUE(state, alpha, beta) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v = -infinity
    for each action in ACTIONS(state) do
        v = MAX(v, MIN-VALUE(RESULT(state, action), alpha, beta))
        if v >= beta then return v  # Beta Cutoff (Prune remaining children)
        alpha = MAX(alpha, v)
    return v

function MIN-VALUE(state, alpha, beta) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v = +infinity
    for each action in ACTIONS(state) do
        v = MIN(v, MAX-VALUE(RESULT(state, action), alpha, beta))
        if v <= alpha then return v  # Alpha Cutoff (Prune remaining children)
        beta = MIN(beta, v)
    return v
```

##### **5. Time & Space Complexity Comparison**

| Feature | Standard Minimax Algorithm | Alpha-Beta Pruning (Optimal Move Ordering) | Alpha-Beta Pruning (Worst-Case Ordering) |
| :--- | :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(b^m)$ | $\mathcal{O}(b^{m/2}) = \mathcal{O}(\sqrt{b^m})$ | $\mathcal{O}(b^m)$ |
| **Effective Branching Factor** | $b$ | $\sqrt{b}$ | $b$ |
| **Space Complexity** | $\mathcal{O}(b \cdot m)$ | $\mathcal{O}(b \cdot m)$ | $\mathcal{O}(b \cdot m)$ |
| **Final Decision Quality** | Exact Optimal Decision | Exact Optimal Decision (Identical to Minimax) | Exact Optimal Decision |

* **Impact of Move Ordering:** If the best moves are evaluated first (move ordering heuristic), Alpha-Beta Pruning effectively doubles the searchable depth of the game tree within the same time budget.

---

## SECTION 2: FULLY SOLVED NUMERICAL PAST YEAR QUESTIONS (PYQs)

---

### **NUMERICAL PYQ 1 (10 MARKS — HARD)**
#### **Source:** SVKM's NMIMS B.Tech CE Final Examination, Batch 2024-25, Q3.a [10 Marks]

#### **Question:**
> **Apply the steps of Alpha-Beta pruning to the following Tree and find out the pruned nodes.**
> 
> The game tree is a 4-level full binary tree with 16 leaf nodes. Root node $A$ is a MAX node at Level 0.
> 
> **Leaf Values (Left to Right):**  
> `8, 23, -47, 28, -30, -37, 3, -41, -19, 4, -49, 4, 43, 45, -26, -14`

---

#### **Step-by-Step Complete Solution:**

##### **1. Game Tree Structure & Node Naming**
* **Level 0 (MAX):** Root $A$
* **Level 1 (MIN):** $B$ (left child of $A$), $C$ (right child of $A$)
* **Level 2 (MAX):** 
  * Under $B$: $D, E$
  * Under $C$: $F, G$
* **Level 3 (MIN):**
  * Under $D$: $H, I$
  * Under $E$: $J, K$
  * Under $F$: $L, M$
  * Under $G$: $N, O$
* **Level 4 (Leaves / Utility Values):**
  * Under $H$: `8, 23`
  * Under $I$: `-47, 28`
  * Under $J$: `-30, -37`
  * Under $K$: `3, -41`
  * Under $L$: `-19, 4`
  * Under $M$: `-49, 4`
  * Under $N$: `43, 45`
  * Under $O$: `-26, -14`

---

##### **2. Step-by-Step Traversal & ($\alpha, \beta$) Tracking Log**

###### **Step 1: Traverse Left Subtree under $B$**
1. **Initialize Root $A$ (MAX):** $\alpha = -\infty, \beta = +\infty$. Pass down to $B$ (MIN), $D$ (MAX), and $H$ (MIN).
2. **Evaluate Node $H$ (MIN):**
   * Left leaf = `8` $\implies \beta = \min(+\infty, 8) = 8$.
   * Right leaf = `23` $\implies \beta = \min(8, 23) = 8$.
   * Node $H$ returns value $v = 8$.
3. **Update Node $D$ (MAX):**
   * Receives $v = 8$ from $H$.
   * Updates $\alpha = \max(-\infty, 8) = 8$. Current bounds at $D$: $\alpha = 8, \beta = +\infty$.
4. **Evaluate Node $I$ (MIN):**
   * Passes $\alpha = 8, \beta = +\infty$ down to $I$.
   * Left leaf = `-47` $\implies \beta = \min(+\infty, -47) = -47$.
   * **Check Pruning Condition at $I$:**
     $$\alpha \ge \beta \iff 8 \ge -47 \quad \text{(TRUE!)}$$
   * **PRUNING DECISION 1:** Prune the right child of $I$ (leaf value **`28`**).
   * Node $I$ returns value $v = -47$.
5. **Complete Node $D$ (MAX):**
   * $v = \max(8, -47) = 8$. Node $D$ value = $8$.
6. **Update Node $B$ (MIN):**
   * Receives $v = 8$ from $D$.
   * Updates $\beta = \min(+\infty, 8) = 8$. Current bounds at $B$: $\alpha = -\infty, \beta = 8$.

###### **Step 2: Traverse Subtree under $E$**
7. **Evaluate Node $J$ (MIN):**
   * Passes $\alpha = -\infty, \beta = 8$ down to $E$ (MAX) and $J$ (MIN).
   * Left leaf = `-30` $\implies \beta = \min(8, -30) = -30$.
   * Right leaf = `-37` $\implies \beta = \min(-30, -37) = -37$.
   * Node $J$ returns value $v = -37$.
8. **Update Node $E$ (MAX):**
   * Receives $v = -37$ from $J$.
   * Updates $\alpha = \max(-\infty, -37) = -37$. Current bounds at $E$: $\alpha = -37, \beta = 8$.
9. **Evaluate Node $K$ (MIN):**
   * Left leaf = `3` $\implies \beta = \min(8, 3) = 3$.
   * Right leaf = `-41` $\implies \beta = \min(3, -41) = -41$.
   * Node $K$ returns value $v = -41$.
10. **Complete Node $E$ (MAX) & $B$ (MIN):**
    * At $E$: $v = \max(-37, -41) = -37$. Node $E$ value = $-37$.
    * At $B$: Receives $v = -37$ from $E$. Updates $\beta = \min(8, -37) = -37$.
    * Node $B$ returns value $v = -37$.

###### **Step 3: Update Root $A$ & Traverse Right Subtree under $C$**
11. **Update Root $A$ (MAX):**
    * Receives $v = -37$ from $B$.
    * Updates $\alpha = \max(-\infty, -37) = -37$. Current bounds at $A$: $\alpha = -37, \beta = +\infty$.
12. **Pass Bounds to $C$ (MIN):**
    * Passes $\alpha = -37, \beta = +\infty$ down to $C$ (MIN), $F$ (MAX), and $L$ (MIN).
13. **Evaluate Node $L$ (MIN):**
    * Left leaf = `-19` $\implies \beta = \min(+\infty, -19) = -19$.
    * Right leaf = `4` $\implies \beta = \min(-19, 4) = -19$.
    * Node $L$ returns value $v = -19$.
14. **Update Node $F$ (MAX):**
    * Receives $v = -19$ from $L$.
    * Updates $\alpha = \max(-37, -19) = -19$. Current bounds at $F$: $\alpha = -19, \beta = +\infty$.
15. **Evaluate Node $M$ (MIN):**
    * Passes $\alpha = -19, \beta = +\infty$ down to $M$.
    * Left leaf = `-49` $\implies \beta = \min(+\infty, -49) = -49$.
    * **Check Pruning Condition at $M$:**
      $$\alpha \ge \beta \iff -19 \ge -49 \quad \text{(TRUE!)}$$
    * **PRUNING DECISION 2:** Prune the right child of $M$ (leaf value **`4`**).
    * Node $M$ returns value $v = -49$.
16. **Complete Node $F$ (MAX) & Update $C$ (MIN):**
    * At $F$: $v = \max(-19, -49) = -19$. Node $F$ value = $-19$.
    * At $C$: Receives $v = -19$ from $F$. Updates $\beta = \min(+\infty, -19) = -19$. Current bounds at $C$: $\alpha = -37, \beta = -19$.

###### **Step 4: Evaluate $G$ & Final Pruning**
17. **Pass Bounds to $G$ (MAX):**
    * Passes $\alpha = -37, \beta = -19$ down to $G$ (MAX) and $N$ (MIN).
18. **Evaluate Node $N$ (MIN):**
    * Left leaf = `43` $\implies \beta = \min(+\infty, 43) = 43$.
    * Right leaf = `45` $\implies \beta = \min(43, 45) = 43$.
    * Node $N$ returns value $v = 43$.
19. **Update Node $G$ (MAX):**
    * Receives $v = 43$ from $N$.
    * Updates $\alpha = \max(-37, 43) = 43$. Current bounds at $G$: $\alpha = 43, \beta = -19$.
    * **Check Pruning Condition at $G$:**
      $$\alpha \ge \beta \iff 43 \ge -19 \quad \text{(TRUE!)}$$
    * **PRUNING DECISION 3:** Prune the entire right subtree under $G$ (Node **`O`** and its leaves **`-26, -14`**).
20. **Complete Game Tree Evaluation:**
    * Node $G$ value = $43$.
    * Node $C$ (MIN): $v = \min(-19, 43) = -19$.
    * Root $A$ (MAX): $v = \max(-37, -19) = -19$.

---

##### **3. Summary Table of Computed Values**

| Node | Type | Children / Leaves | Evaluated Value ($v$) | Final Bounds ($\alpha, \beta$) | Status |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **H** | MIN | 8, 23 | 8 | $\alpha=-\infty, \beta=8$ | Fully Evaluated |
| **I** | MIN | -47, [28] | -47 | $\alpha=8, \beta=-47$ | **Right Leaf 28 Pruned** |
| **D** | MAX | H(8), I(-47) | 8 | $\alpha=8, \beta=+\infty$ | Fully Evaluated |
| **J** | MIN | -30, -37 | -37 | $\alpha=-\infty, \beta=-37$ | Fully Evaluated |
| **K** | MIN | 3, -41 | -41 | $\alpha=-37, \beta=-41$ | Fully Evaluated |
| **E** | MAX | J(-37), K(-41) | -37 | $\alpha=-37, \beta=8$ | Fully Evaluated |
| **B** | MIN | D(8), E(-37) | -37 | $\alpha=-\infty, \beta=-37$ | Fully Evaluated |
| **L** | MIN | -19, 4 | -19 | $\alpha=-37, \beta=-19$ | Fully Evaluated |
| **M** | MIN | -49, [4] | -49 | $\alpha=-19, \beta=-49$ | **Right Leaf 4 Pruned** |
| **F** | MAX | L(-19), M(-49) | -19 | $\alpha=-19, \beta=+\infty$ | Fully Evaluated |
| **N** | MIN | 43, 45 | 43 | $\alpha=-37, \beta=43$ | Fully Evaluated |
| **O** | MIN | [-26, -14] | — | — | **Entire Node O Pruned** |
| **G** | MAX | N(43), [O] | 43 | $\alpha=43, \beta=-19$ | **Right Branch Pruned** |
| **C** | MIN | F(-19), G(43) | -19 | $\alpha=-37, \beta=-19$ | Fully Evaluated |
| **A** | MAX | B(-37), C(-19) | **-19** | $\alpha=-19, \beta=+\infty$ | **Root Node** |

---

##### **4. Final Exam Summary Results**
* **Final Root Value:** **$-19$**
* **Optimal Move Choice at Root $A$:** Move to **Right Child $C$** (Path: $A \rightarrow C \rightarrow F \rightarrow L \rightarrow -19$).
* **List of Pruned Nodes / Leaves (Total 4 Leaves Pruned):**
  1. Leaf **`28`** (under MIN node $I$)
  2. Leaf **`4`** (under MIN node $M$)
  3. Leaves **`-26`** and **`-14`** (under MAX node $G$ / MIN node $O$)

---

### **NUMERICAL PYQ 2 (10 MARKS — MEDIUM)**
#### **Source:** SVKM's NMIMS Re-Exam 2022-23, Q3.B [10 Marks] / AI_UNIT2_NUMERICALTOPICS.pdf

#### **Question:**
> **Apply Alpha-Beta Pruning on the following 3-level game tree. Show all $(\alpha, \beta)$ updates and identify the pruned branches.**
> 
> * Root $A$ is a MAX node.
> * Level 1 (MIN): Children $B, C$.
> * Level 2 (MAX): $D, E$ (under $B$); $F, G$ (under $C$).
> * Level 3 (Leaves):
>   * Under $D$: `-1, 8`
>   * Under $E$: `-3, -1`
>   * Under $F$: `2, -1`
>   * Under $G$: `-3, 4`

---

#### **Step-by-Step Solution:**

```
                  [ A ] (MAX)
                 /     \
                /       \
         [ B ] (MIN)     [ C ] (MIN)
         /    \           /    \
        /      \         /      \
     [D] (MAX) [E] (MAX) [F] (MAX) [G] (MAX)
     / \       / \       / \       / \
   -1   8    -3  -1     2  -1    -3   4
```

1. **Evaluate $D$ (MAX):**
   * Left child = `-1` $\implies \alpha = -1$.
   * Right child = `8` $\implies \alpha = \max(-1, 8) = 8$.
   * Node $D$ value = $8$.
2. **Evaluate $E$ (MAX):**
   * Passes $\alpha = -\infty, \beta = 8$ down to $E$ from $B$.
   * Left child = `-3` $\implies \alpha = -3$.
   * Right child = `-1` $\implies \alpha = \max(-3, -1) = -1$.
   * Node $E$ value = $-1$.
3. **Evaluate $B$ (MIN):**
   * $v = \min(8, -1) = -1$.
   * Node $B$ value = $-1$.
4. **Update Root $A$ (MAX):**
   * Receives $v = -1$ from $B$.
   * Updates $\alpha = \max(-\infty, -1) = -1$. Current bounds at $A$: $\alpha = -1, \beta = +\infty$.
5. **Evaluate $F$ (MAX):**
   * Passes $\alpha = -1, \beta = +\infty$ down to $C$ (MIN) and $F$ (MAX).
   * Left child = `2` $\implies \alpha = \max(-1, 2) = 2$.
   * Right child = `-1` $\implies \alpha = \max(2, -1) = 2$.
   * Node $F$ value = $2$.
6. **Update Node $C$ (MIN):**
   * Receives $v = 2$ from $F$.
   * Updates $\beta = \min(+\infty, 2) = 2$. Current bounds at $C$: $\alpha = -1, \beta = 2$.
7. **Evaluate $G$ (MAX):**
   * Passes $\alpha = -1, \beta = 2$ down to $G$.
   * Left child = `-3` $\implies \alpha = \max(-1, -3) = -1$.
   * Right child = `4` $\implies \alpha = \max(-1, 4) = 4$.
   * At $G$, $\alpha$ becomes $4$. Check condition: $\alpha \ge \beta \iff 4 \ge 2$ (TRUE at completion of $G$).
   * Node $G$ value = $4$.
8. **Complete $C$ (MIN) & Root $A$ (MAX):**
   * At $C$: $v = \min(2, 4) = 2$. Node $C$ value = $2$.
   * At Root $A$: $v = \max(-1, 2) = 2$.

#### **Results:**
* **Final Root Value:** **`2`**
* **Optimal Decision Path:** Move to **Right Child $C$** ($A \rightarrow C \rightarrow F \rightarrow 2$).
* **Pruned Branches:** None in this specific leaf order (demonstrates that poor move ordering requires full tree exploration).

---

## SECTION 3: RECEPTACLE OF COMMON EXAM MISTAKES

```
┌───────────────────────────────────────────────────────────────────────────┐
│                       ⚠️ COMMON EXAM MISTAKES TO AVOID                    │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. MISUPDATING ALPHA AND BETA:                                            │
│    • Mistake: Updating Alpha at a MIN node or Beta at a MAX node.          │
│    • Correction: Alpha ONLY updates at MAX nodes; Beta ONLY updates at    │
│      MIN nodes.                                                           │
│                                                                           │
│ 2. CONFUSING PRUNING CONDITIONS:                                          │
│    • Mistake: Writing Alpha > Beta or Alpha <= Beta as the cut-off rule.   │
│    • Correction: The exact pruning condition is ALWAYS Alpha >= Beta.     │
│                                                                           │
│ 3. FORGETTING TO INHERIT PARENT BOUNDS:                                   │
│    • Mistake: Resetting Alpha = -inf and Beta = +inf at every sub-node.   │
│    • Correction: Child nodes ALWAYS inherit the current (Alpha, Beta)     │
│      bounds from their direct parent node before starting evaluation.     │
│                                                                           │
│ 4. WEAK ROOT-VALUE PROPAGATION:                                          │
│    • Mistake: Giving only final values without showing intermediate        │
│      sub-node values on the tree diagram.                                 │
│    • Correction: Annotate EVERY node with its final computed value (v)    │
│      and mark pruned branches clearly with double slashes (//).           │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 4: LAST-MINUTE REVISION & CHECKLIST

### **Quick Definition Flashcards**
* **Game Tree:** A directed graph where nodes represent game states and edges represent legal moves between players.
* **Ply:** Half a full turn (a single move executed by one player). Two plies equal one complete turn.
* **Zero-Sum Game:** A competitive game where the total sum of utilities across all players is zero.
* **Alpha ($\alpha$):** The lower bound on MAX's utility (best option MAX has guaranteed so far).
* **Beta ($\beta$):** The upper bound on MIN's utility (best option MIN has guaranteed so far).
* **Alpha Cutoff:** Search termination below a MIN node when $\beta \le \alpha$.
* **Beta Cutoff:** Search termination below a MAX node when $\alpha \ge \beta$.

---

### **Complete Syllabus Coverage Checklist**

- [x] **Game Domain & Problem Formulation**
  - [x] Two-player games (MAX vs. MIN)
  - [x] Zero-sum games definition and formula
  - [x] Perfect-information games
  - [x] Game states and game trees
  - [x] Players, objectives, and utility values
  - [x] Initial state, legal moves, terminal states
  - [x] 6-tuple formal game formulation

- [x] **Optimal Decisions in Games**
  - [x] Game trees representation
  - [x] MAX player strategy ($\max$)
  - [x] MIN player strategy ($\min$)
  - [x] Leaf-node utility evaluation
  - [x] Value propagation from leaves to root
  - [x] Optimal decision-making assuming rational play

- [x] **Minimax Algorithm**
  - [x] Definition and working principle
  - [x] MAX and MIN level behavior
  - [x] Bottom-up value propagation
  - [x] DFS traversal order
  - [x] Complete Python/pseudo-code implementation
  - [x] Time complexity $\mathcal{O}(b^m)$ and Space complexity $\mathcal{O}(b \cdot m)$
  - [x] Advantages and limitations
  - [x] Fully worked Minimax tree numericals

- [x] **Alpha-Beta Pruning**
  - [x] Need for pruning and search space reduction
  - [x] Definition of Alpha ($\alpha$) and Beta ($\beta$)
  - [x] Initial values: $\alpha = -\infty, \beta = +\infty$
  - [x] Alpha/Beta update rules (MAX updates $\alpha$, MIN updates $\beta$)
  - [x] Pruning condition: $\alpha \ge \beta$
  - [x] Alpha and Beta cutoffs explained with diagrams
  - [x] DFS traversal order
  - [x] Best-case time complexity $\mathcal{O}(b^{m/2})$ vs worst-case $\mathcal{O}(b^m)$
  - [x] Fully solved 10-mark past year exam numericals

---
