# ARTIFICIAL INTELLIGENCE (AI) STUDY NOTES
## UNIT 2: ADVERSARIAL SEARCH (GAME PLAYING)
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## UNIT OVERVIEW

Adversarial search (game playing) addresses environments where multiple competitive agents have conflicting goals. In a multi-agent environment, the actions of one agent directly impact the payoffs of other agents. This unit examines the formalization of two-player, zero-sum, perfect-information games, the optimal decision-making process via the **Minimax Algorithm**, and search-space optimization through **Alpha-Beta Pruning**.

---

## SECTION 1: GAME DOMAIN & PROBLEM FORMULATION

### 1.1 Fundamental Game Characteristics

An **Adversarial Search Problem** (or Game) is distinguished from standard single-agent state-space search by the presence of an active opponent attempting to minimize the agent's outcome while maximizing their own.

```text
                   ┌────────────────────────────────────────┐
                   │        ENVIRONMENT PROPERTIES          │
                   └───────────────────┬────────────────────┘
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐
│Two-Player System │          │ Zero-Sum Utility │          │Perfect Information│
│ MAX vs. MIN      │          │ Payoff(MAX)+     │          │ Fully Observable │
│ Alternating Turns│          │ Payoff(MIN) = 0  │          │ No Hidden State  │
└──────────────────┘          └──────────────────┘          └──────────────────┘
```

1. **Two-Player Games:**  
   Games involving exactly two opponents who take alternate turns to make moves. By convention, the players are designated as:
   * **MAX:** The maximizing player who attempts to reach a state with the highest possible utility.
   * **MIN:** The minimizing player (the adversary) who attempts to force the game to a state with the lowest possible utility for MAX.

2. **Zero-Sum Games:**  
   A game where the players' payoffs sum to zero for every outcome. More generally, a constant-sum game has the same total payoff across outcomes. In a two-player zero-sum game, any gain by MAX represents an equal loss for MIN:
   $\text{Utility}(\text{MAX}) + \text{Utility}(\text{MIN}) = 0$.
   * Pure competition: No possibility of cooperation, win-win outcomes, or mutual benefit.

3. **Perfect-Information Games:**  
   Games where the environment is **fully observable** by both players at all times. Neither player possesses hidden information (such as concealed playing cards or fog of war). Examples include Chess, Checkers, Tic-Tac-Toe, and Go.

4. **Deterministic Environment:**  
   Each action executed from a given state leads to a single, deterministic outcome without chance or random elements (like dice rolls).

---

### 1.2 Formal Game Problem Formulation

A game is formally defined as a specialized search problem consisting of **six components**:

1. **Initial State ($s_0$):**  
   The initial board configuration and an indication of which player moves first (e.g., an empty $3 \times 3$ grid in Tic-Tac-Toe with MAX playing 'X').

2. **Player Function ($\text{PLAYER}(s)$):**  
   Defines which player ($\text{MAX}$ or $\text{MIN}$) has the turn to move in state $s$.

3. **Actions Function ($\text{ACTIONS}(s)$):**  
   Returns the set of legal moves available to $\text{PLAYER}(s)$ in state $s$.

4. **Transition Model ($\text{RESULT}(s, a)$):**  
   A deterministic function returning the state that results from executing action $a$ in state $s$.

5. **Terminal Test ($\text{IS-TERMINAL}(s)$ or $\text{TERMINAL-TEST}(s)$):**  
   A boolean test that returns `True` if the game has ended in state $s$, and `False` otherwise. States where the game has ended are called **Terminal States** (leaf nodes).

6. **Utility / Payoff Function ($\text{UTILITY}(s, p)$):**  
   A numerical function defining the final value of a terminal state $s$ for player $p$. By universal AI convention, utility is measured relative to **MAX**:
   * $\text{UTILITY}(s, \text{MAX}) = +1$ (Win for MAX)
   * $\text{UTILITY}(s, \text{MAX}) = -1$ (Loss for MAX / Win for MIN)
   * $\text{UTILITY}(s, \text{MAX}) = 0$ (Draw / Tie)

---

### 1.3 Game States and Game Trees

A **Game Tree** is an explicit graphical representation of the search space:
* **Nodes:** Represent game states.
* **Edges (Branches):** Represent legal moves / actions ($\text{ACTIONS}(s)$).
* **Root Node:** Represents the initial state ($s_0$).
* **Leaf Nodes:** Represent terminal states where $\text{TERMINAL-TEST}(s)$ is `True`.
* **Ply:** A single move by one player. A full "round" consisting of one move by MAX and one move by MIN equals **2 plies**.

```text
Level 0 (root)            [MAX]            <- Initial state s0
                         /     \
Level 1                [MIN]   [MIN]         <- After MAX's first ply
                       /   \   /   \
Level 2 (leaves)      (3)  (12) (8)  (2)     <- After MIN's second ply
```

---

### Key Takeaways & Exam Highlights

> ⭐ **Must Remember**  
> Utility values are **ALWAYS measured from the perspective of MAX**. A high positive score benefits MAX, while a negative score benefits MIN.

> 🧠 **Must Understand**  
> In standard single-agent search (e.g., $A^*$, BFS, DFS), the agent finds a fixed path to a goal. In adversarial search, the agent must compute a **contingency strategy** (policy) because the opponent's actions cannot be controlled.

> ✍️ Exam Focus  
> Be prepared to list the 6 formal components of a game problem and contrast standard state-space search with game-tree search for a 5-mark question.

> ⚠️ Common Mistakes  
> * Confusing a **ply** with a full move (1 ply = 1 half-move by 1 player).
> * Assigning separate positive utility values to MIN (MIN's goal is to minimize MAX's utility).

---

## SECTION 2: OPTIMAL DECISIONS IN GAMES

### 2.1 The Concept of Optimal Strategy

An **optimal strategy** for MAX is a policy that leads to an outcome at least as good as any other strategy, **assuming that MIN also plays optimally** to minimize MAX's utility.

```text
                       MAX Node
                      /        \
            Move A1  /          \ Move A2
                    /            \
               MIN Node B       MIN Node C
               /   |   \         /   |   \
              3    12   8       2    14   2
              
           min(3,12,8) = 3     min(2,14,2) = 2
                    \            /
                     \          /
                 MAX chooses max(3, 2) = 3
```

---

### 2.2 Minimax Value Definition

The **Minimax Value** of a node $n$, denoted $\text{MINIMAX}(n)$, is the utility (for MAX) of being in state $n$, assuming both players play optimally from $n$ to the end of the game:

```math
\text{MINIMAX}(n) = \begin{cases} \text{UTILITY}(n) & \text{if } \text{IS-TERMINAL}(n) \\ \max_{a \in \text{ACTIONS}(n)} \text{MINIMAX}(\text{RESULT}(n, a)) & \text{if } \text{PLAYER}(n) = \text{MAX} \\ \min_{a \in \text{ACTIONS}(n)} \text{MINIMAX}(\text{RESULT}(n, a)) & \text{if } \text{PLAYER}(n) = \text{MIN} \end{cases}
```

---

### 2.3 Value Propagation Mechanics (Bottom-Up)

Value propagation in game trees operates strictly from the leaf nodes back to the root:

1. **Leaf Evaluation:** Evaluate all terminal states using the utility function.
2. **MIN Level Propagation:** A MIN node assigns itself the **minimum** value among all its child nodes:
   $\text{Value}(\text{MIN Node}) = \min(\text{Children Values})$.
3. **MAX Level Propagation:** A MAX node assigns itself the **maximum** value among all its child nodes:
   $\text{Value}(\text{MAX Node}) = \max(\text{Children Values})$.
4. **Root Decision:** The root node (MAX) selects the branch / action that yields the maximum propagated utility value.

---

### Key Takeaways & Exam Highlights

> ⭐ **Must Remember**  
> $\text{MINIMAX}(n)$ assumes **perfect rationality** from the opponent. If MIN plays sub-optimally, MAX will achieve a utility equal to or greater than the Minimax value.

> 🧠 **Must Understand**  
> Value propagation is a **bottom-up backtracking procedure**. You cannot calculate the value of an internal node without evaluating its descendants down to the terminal leaves.

> ✍️ Exam Focus  
> University exams often ask: *"Why does MAX assume MIN plays optimally?"* Answer: Assuming optimal play guarantees a lower bound on MAX's performance (pessimistic / safe decision-making).

> ⚠️ Common Mistakes  
> Selecting the maximum leaf directly without propagating through the intermediate MIN levels!

---

## SECTION 3: MINIMAX ALGORITHM

### 3.1 Definition & Purpose

The **Minimax Algorithm** is a recursive depth-first search algorithm used to calculate the optimal move for MAX in a two-player, zero-sum, perfect-information game tree. DFS expands the tree as needed; it need not store the complete game tree in memory.

---

### 3.2 Step-by-Step Procedure

1. **Explore the Full Game Tree:** Perform a Depth-First Search (DFS) traversal down to terminal leaf states, generating successors as needed rather than storing the entire tree.
2. **Apply Utility Function:** Evaluate utility values at all leaf nodes.
3. **Back Up Values (Bottom-Up):**
   * At MIN levels, take the **minimum** child value.
   * At MAX levels, take the **maximum** child value.
4. **Select Optimal Move:** At the root node (level 0), select the action associated with the maximum backed-up utility value.

---

### 3.3 Pseudocode

The root procedure assumes it is MAX's turn and at least one legal move exists. With strict `>`, ties retain the first optimal action examined.

```text
function MINIMAX-DECISION(state) returns an action
    inputs: state, current state in game
    
    bestValue = -infinity
    bestAction = NONE
    for each a in ACTIONS(state) do
        value = MIN-VALUE(RESULT(state, a))
        if value > bestValue then
            bestValue = value
            bestAction = a
    return bestAction


function MAX-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    
    v = -infinity
    for each a in ACTIONS(state) do
        v = MAX(v, MIN-VALUE(RESULT(state, a)))
    return v


function MIN-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    
    v = +infinity
    for each a in ACTIONS(state) do
        v = MIN(v, MAX-VALUE(RESULT(state, a)))
    return v
```

---

### 3.4 Complexity Analysis

* **Time Complexity: $O(b^m)$**
  * $b$: Branching factor (number of legal moves per state).
  * $m$: Maximum depth of the game tree.
  * Minimax must examine every node in the game tree down to depth $m$.
  * *Example:* In Chess ($b \approx 35, m \approx 100$), $b^m \approx 35^{100} \approx 10^{154}$ nodes, making complete Minimax search computationally impossible.

* **Space Complexity: $O(b \cdot m)$**
  * Minimax performs a Depth-First Search (DFS), keeping the current path and generated sibling nodes in memory. With incremental successor generation that does not retain siblings, path bookkeeping can instead use $O(m)$ space.

---

### 3.5 Advantages & Limitations

| Aspect | Details |
| :--- | :--- |
| **Advantages** | • Guaranteed to find the optimal move against an optimal opponent.<br>• Complete for finite game trees.<br>• Linear space complexity $O(b \cdot m)$. |
| **Limitations** | • Exponential time complexity $O(b^m)$.<br>• Infeasible for games with large state spaces (e.g., Chess, Go).<br>• Assumes the opponent is strictly optimal (does not exploit opponent weaknesses). |

---

### 3.6 Fully Worked Minimax Numerical Example

#### Problem (10 Marks):
Consider the following 2-ply game tree where MAX moves first at the root node $A$. Calculate the Minimax values for all internal nodes and determine the optimal opening move for MAX.

```text
                  [ A ]  (MAX)
               /    |    \
             /      |      \
           [B]     [C]     [D]  (MIN)
          / | \    / \     / \
         3 12  8  2  14   5   2 (Leaves)
```

#### Step-by-Step Solution:

1. **Step 1 — Leaf Node Evaluation:**
   * Leaves under $B$: $\{3, 12, 8\}$
   * Leaves under $C$: $\{2, 14\}$
   * Leaves under $D$: $\{5, 2\}$

2. **Step 2 — Evaluate MIN Nodes (Level 1):**
   * $\text{Value}(B) = \min(3, 12, 8) = \mathbf{3}$
   * $\text{Value}(C) = \min(2, 14) = \mathbf{2}$
   * $\text{Value}(D) = \min(5, 2) = \mathbf{2}$

3. **Step 3 — Evaluate Root MAX Node (Level 0):**
   * $\text{Value}(A) = \max(\text{Value}(B), \text{Value}(C), \text{Value}(D)) = \max(3, 2, 2) = \mathbf{3}$

4. **Step 4 — Optimal Move Selection:**
   * $\text{MINIMAX}(A) = 3$.
   * The optimal move for MAX at root $A$ is to move to node **$B$** (Branch $A \rightarrow B$).

---

## SECTION 4: ALPHA-BETA PRUNING

### 4.1 Need for Pruning

Because Minimax has an exponential time complexity of $O(b^m)$, traversing the full game tree is impossible for non-trivial games. **Pruning** allows us to eliminate large subtrees from consideration **without altering the final Minimax decision**.

---

### 4.2 Definition and Parameters ($\alpha$ and $\beta$)

**Alpha-Beta Pruning** maintains two bounds along the DFS search path:

1. **Alpha ($\alpha$):**  
   The value of the **best (highest-value) choice** found so far at any choice point along the path for **MAX**.
   * Initial value: $\alpha = -\infty$
   * Updated ONLY at **MAX** nodes: $\alpha = \max(\alpha, v)$

2. **Beta ($\beta$):**  
   The value of the **best (lowest-value) choice** found so far at any choice point along the path for **MIN**.
   * Initial value: $\beta = +\infty$
   * Updated ONLY at **MIN** nodes: $\beta = \min(\beta, v)$

---

### 4.3 The Pruning Condition ($\alpha \ge \beta$)

Pruning occurs whenever a node's updated boundary satisfies:

```math
\mathbf{\alpha \ge \beta}
```

```text
                     MAX Node (alpha = 3)
                          /        \
                         /          \  (Search enters MIN Node)
                        /            \
        Selected Branch               MIN Node (beta <= 2)
        Yields 3                      /      \
                                     /        \
                                Leaf = 2    PRUNED!
                                
        Since MIN can guarantee <= 2, MAX (who already has 3) 
        will NEVER choose this branch! Further exploration is useless.
```

1. **Alpha Cutoff (at MIN Node):**  
   If a MIN node $n$ finds a child value $v \le \alpha$, its remaining unexplored children are pruned immediately.
   * *Reason:* MAX already has a guaranteed option of value $\alpha$ elsewhere. MAX will never select this branch because MIN can force a result $\le v \le \alpha$.

2. **Beta Cutoff (at MAX Node):**  
   If a MAX node $n$ finds a child value $v \ge \beta$, the search below $n$ is terminated immediately.
   * *Reason:* MIN already has a guaranteed option of value $\beta$ elsewhere. MIN will never allow play to reach this state because MAX can force a result $\ge v \ge \beta$.

---

### 4.4 Pseudocode

The root procedure assumes it is MAX's turn and at least one legal move exists. A cut-off node can return a bound sufficient for its ancestors rather than an exact standalone minimax value.

```text
function ALPHA-BETA-SEARCH(state) returns an action
    alpha = -infinity
    beta = +infinity
    bestValue = -infinity
    bestAction = NONE
    for each a in ACTIONS(state) do
        value = MIN-VALUE(RESULT(state, a), alpha, beta)
        if value > bestValue then
            bestValue = value
            bestAction = a
        alpha = MAX(alpha, bestValue)
    return bestAction


function MAX-VALUE(state, alpha, beta) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    
    v = -infinity
    for each a in ACTIONS(state) do
        v = MAX(v, MIN-VALUE(RESULT(state, a), alpha, beta))
        if v >= beta then return v  # Beta Cutoff (Prune)
        alpha = MAX(alpha, v)
    return v


function MIN-VALUE(state, alpha, beta) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    
    v = +infinity
    for each a in ACTIONS(state) do
        v = MIN(v, MAX-VALUE(RESULT(state, a), alpha, beta))
        if v <= alpha then return v  # Alpha Cutoff (Prune)
        beta = MIN(beta, v)
    return v
```

---

### 4.5 Move Ordering and Effectiveness

The efficiency of Alpha-Beta Pruning depends critically on the order in which child nodes are examined:

* **Worst-Case Move Ordering:**  
  * Nodes examined in worst-to-best order (no pruning occurs).
  * Time Complexity: **$O(b^m)$** (Same as standard Minimax).

* **Optimal Move Ordering:**  
  * Best moves examined first at every level.
  * Effective branching factor reduced from $b$ to **$\sqrt{b}$**.
  * Time Complexity: **$O(b^{m/2})$**
  * *Impact:* Allows searching **twice as deep** in the same amount of computation time!

---

### Key Takeaways & Exam Highlights

> ⭐ **Must Remember**  
> Alpha-Beta Pruning **returns the same exact root minimax value and an optimal move as Minimax**. It does NOT make approximations or compromise decision quality.

> 🧠 **Must Understand**  
> * $\alpha$ increases or stays constant. It NEVER decreases.
> * $\beta$ decreases or stays constant. It NEVER increases.
> * Pruning happens when **$\alpha \ge \beta$**.

> ✍️ Exam Focus  
> Expect a 10-mark numerical on Alpha-Beta pruning! You MUST write out the $(\alpha, \beta)$ values at every step and explicitly state the pruning condition ($\alpha \ge \beta$) whenever a branch is cut off.

> ⚠️ Common Mistakes  
> * Updating $\alpha$ at a MIN node or $\beta$ at a MAX node.
> * Forgetting to pass updated $(\alpha, \beta)$ bounds down to child nodes during DFS recursion.

---

## SECTION 5: FULLY SOLVED PYQ NUMERICALS

> **Provenance note:** The two original example headings identify a university PYQ and an AIMA example. These source attributions are preserved from the original notes but have not been independently verified; use the worked trees as practice problems unless you have the original question papers or textbook reference.

---

### 📄 PYQ NUMERICAL 1 (SVKM's NMIMS B.Tech CE Final Exam — 10 Marks)

#### Problem Statement:
Apply Alpha-Beta Pruning to the following 4-level game tree. The root node $A$ is a MAX node. Show all intermediate $(\alpha, \beta)$ updates, backed-up values, final root value, and list all pruned leaf nodes.

```text
                                      [A]  (MAX)
                                    /     \
                                  /         \
                                /             \
                        [B]                     [C]  (MIN)
                      /     \                 /     \
                    /         \             /         \
                 [D]           [E]       [F]           [G]  (MAX)
                /   \         /   \     /   \         /   \
              [H]   [I]     [J]   [K] [L]   [M]     [N]   [O]  (MIN)
              / \   / \     / \   / \ / \   / \     / \   / \
             8 23 -47 28  -30 -37 3 -41 -19 4 -49 4 43 45 -26 -14  (Leaves)
```

---

#### Step-by-Step Traversal & Pruning Trace:

##### 1. Left Subtree Exploration ($A \rightarrow B \rightarrow D \rightarrow H$):
1. **At Root A (MAX):** Initial $\alpha = -\infty, \beta = +\infty$.
2. **At Node B (MIN):** Inherits $\alpha = -\infty, \beta = +\infty$.
3. **At Node D (MAX):** Inherits $\alpha = -\infty, \beta = +\infty$.
4. **At Node H (MIN):** Inherits $\alpha = -\infty, \beta = +\infty$.
   * Evaluates child $8 \Rightarrow \beta = \min(+\infty, 8) = 8$.
   * Evaluates child $23 \Rightarrow \beta = \min(8, 23) = 8$.
   * **Node H Value = 8**.
5. **Back to Node D (MAX):**
   * $\alpha = \max(-\infty, 8) = \mathbf{8}$. Bounds at $D: (\alpha = 8, \beta = +\infty)$.
6. **At Node I (MIN):**
   * Inherits $\alpha = 8, \beta = +\infty$.
   * Evaluates first child **$-47$** $\Rightarrow \beta = \min(+\infty, -47) = \mathbf{-47}$.
   * **Check Pruning Condition at Node I:**
     $\alpha = 8, \quad \beta = -47 \implies \alpha \ge \beta \quad (8 \ge -47) \quad \text{TRUE}$
   * ✂️ **ALPHA CUTOFF AT NODE I!**
   * **The right child of I (Leaf 28) is PRUNED.**
   * **Node I returns -47 as an upper bound** (its exact value is also $-47$ for these supplied leaves).
7. **Back to Node D (MAX):**
   * $\text{Value}(D) = \max(8, -47) = \mathbf{8}$.
8. **Back to Node B (MIN):**
   * $\beta = \min(+\infty, 8) = \mathbf{8}$. Bounds at $B: (\alpha = -\infty, \beta = 8)$.

---

##### 2. Subtree E ($B \rightarrow E$):
9. **At Node E (MAX):**
   * Inherits bounds from $B: (\alpha = -\infty, \beta = 8)$.
10. **At Node J (MIN):**
    * Inherits $(\alpha = -\infty, \beta = 8)$.
    * Evaluated children: $-30$ and $-37 \Rightarrow \text{Value}(J) = \min(-30, -37) = \mathbf{-37}$.
11. **Back to Node E (MAX):**
    * $\alpha = \max(-\infty, -37) = -37$. Bounds at $E: (\alpha = -37, \beta = 8)$.
12. **At Node K (MIN):**
    * Inherits $(\alpha = -37, \beta = 8)$.
    * Evaluated children: $3$ and $-41 \Rightarrow \text{Value}(K) = \min(3, -41) = \mathbf{-41}$.
13. **Back to Node E (MAX):**
    * $\text{Value}(E) = \max(-37, -41) = \mathbf{-37}$.
14. **Back to Node B (MIN):**
    * $\beta = \min(8, -37) = \mathbf{-37}$.
    * **Node B Value = -37**.
15. **Back to Root A (MAX):**
    * $\alpha = \max(-\infty, -37) = \mathbf{-37}$. Bounds at Root $A: (\alpha = -37, \beta = +\infty)$.

---

##### 3. Right Subtree Exploration ($A \rightarrow C \rightarrow F \rightarrow L$):
16. **At Node C (MIN):**
    * Inherits bounds from Root $A: (\alpha = -37, \beta = +\infty)$.
17. **At Node F (MAX):**
    * Inherits $(\alpha = -37, \beta = +\infty)$.
18. **At Node L (MIN):**
    * Inherits $(\alpha = -37, \beta = +\infty)$.
    * Evaluated children: $-19$ and $4 \Rightarrow \text{Value}(L) = \min(-19, 4) = \mathbf{-19}$.
19. **Back to Node F (MAX):**
    * $\alpha = \max(-37, -19) = \mathbf{-19}$. Bounds at $F: (\alpha = -19, \beta = +\infty)$.
20. **At Node M (MIN):**
    * Inherits $(\alpha = -19, \beta = +\infty)$.
    * Evaluates first child **$-49$** $\Rightarrow \beta = \min(+\infty, -49) = \mathbf{-49}$.
    * **Check Pruning Condition at Node M:**
      $\alpha = -19, \quad \beta = -49 \implies \alpha \ge \beta \quad (-19 \ge -49) \quad \text{TRUE}$
    * ✂️ **ALPHA CUTOFF AT NODE M!**
    * **The right child of M (Leaf 4) is PRUNED.**
    * **Node M returns -49 as an upper bound** (its exact value is also $-49$ for these supplied leaves).
21. **Back to Node F (MAX):**
    * $\text{Value}(F) = \max(-19, -49) = \mathbf{-19}$.
22. **Back to Node C (MIN):**
    * $\beta = \min(+\infty, -19) = \mathbf{-19}$. Bounds at $C: (\alpha = -37, \beta = -19)$.

---

##### 4. Subtree G ($C \rightarrow G$):
23. **At Node G (MAX):**
    * Inherits bounds from $C: (\alpha = -37, \beta = -19)$.
24. **At Node N (MIN):**
    * Inherits $(\alpha = -37, \beta = -19)$.
    * Evaluates children: $43$ and $45 \Rightarrow \text{Value}(N) = \min(43, 45) = \mathbf{43}$.
25. **Back to Node G (MAX):**
    * $\alpha = \max(-37, 43) = \mathbf{43}$.
    * Bounds at $G$: $(\alpha = 43, \beta = -19)$.
    * **Check Pruning Condition at Node G:**
      $\alpha = 43, \quad \beta = -19 \implies \alpha \ge \beta \quad (43 \ge -19) \quad \text{TRUE}$
    * ✂️ **BETA CUTOFF AT NODE G!**
    * **The entire subtree at Node O (containing leaves -26 and -14) is PRUNED.**
    * **Node G returns 43 as a lower bound** (its exact value is also $43$ for these supplied leaves).
26. **Back to Node C (MIN):**
    * $\text{Value}(C) = \min(-19, 43) = \mathbf{-19}$.
27. **Back to Root A (MAX):**
    * $\text{Value}(A) = \max(-37, -19) = \mathbf{-19}$.

---

#### Summary Table of Results:

| Node | Type | Final Value | Bounds ($\alpha, \beta$) | Pruning / Action |
| :---: | :---: | :---: | :---: | :--- |
| **A** | MAX | **-19** | $\alpha = -19, \beta = +\infty$ | Root Node. Optimal Move: Branch $A \rightarrow C$. |
| **B** | MIN | -37 | $\alpha = -\infty, \beta = -37$ | Fully evaluated. |
| **C** | MIN | **-19** | $\alpha = -37, \beta = -19$ | Optimal branch for MAX at root. |
| **D** | MAX | 8 | $\alpha = 8, \beta = +\infty$ | Child of B. |
| **E** | MAX | -37 | $\alpha = -37, \beta = 8$ | Child of B. |
| **F** | MAX | -19 | $\alpha = -19, \beta = +\infty$ | Child of C. |
| **G** | MAX | 43 | $\alpha = 43, \beta = -19$ | **Pruned child subtree O ($\alpha \ge \beta$); returned value is a lower bound.** |
| **I** | MIN | -47 | $\alpha = 8, \beta = -47$ | **Pruned right leaf 28 ($\alpha \ge \beta$).** |
| **M** | MIN | -49 | $\alpha = -19, \beta = -49$ | **Pruned right leaf 4 ($\alpha \ge \beta$).** |

* **Final Minimax Value at Root $A$:** **-19**
* **Optimal Decision for MAX:** Move to **Node $C$** (Path $A \rightarrow C \rightarrow F \rightarrow L$).
* **List of Pruned Leaves:** **`28`**, **`4`**, **`-26`**, **`-14`** (4 leaf nodes pruned in total).

---

### 📄 PYQ NUMERICAL 2 (Standard AIMA 2-Ply Alpha-Beta Pruning Example — 10 Marks)

#### Problem Statement:
Trace Alpha-Beta Pruning on the 2-ply game tree shown below (Root $A$ is MAX). List all $(\alpha, \beta)$ updates, backed-up values, and pruned branches.

```text
                  [ A ]  (MAX)
               /    |    \
             /      |      \
           [B]     [C]     [D]  (MIN)
          / | \    / \     /|\
         3 12  8  2   x   14 5 2  (Leaves)
```

#### Step-by-Step Solution:

1. **Root A (MAX):** $\alpha = -\infty, \beta = +\infty$.
2. **Subtree B (MIN):**
   * Inherits $(\alpha = -\infty, \beta = +\infty)$.
   * Evaluates leaves $3, 12, 8 \Rightarrow \text{Value}(B) = \min(3, 12, 8) = \mathbf{3}$.
   * Back to Root $A \Rightarrow \alpha = \max(-\infty, 3) = \mathbf{3}$. Bounds at $A: (\alpha = 3, \beta = +\infty)$.
3. **Subtree C (MIN):**
   * Inherits $(\alpha = 3, \beta = +\infty)$.
   * Evaluates first leaf **$2$** $\Rightarrow \beta = \min(+\infty, 2) = \mathbf{2}$.
   * **Check Pruning Condition at Node C:**
     $\alpha = 3, \quad \beta = 2 \implies \alpha \ge \beta \quad (3 \ge 2) \quad \text{TRUE}$
   * ✂️ **ALPHA CUTOFF AT NODE C!**
   * **The remaining child of C (leaf $x$) is PRUNED.**
   * $\text{Value}(C) \le 2$; the returned $2$ is an upper bound, not necessarily C's exact value, because $x$ was not evaluated.
4. **Subtree D (MIN):**
   * Inherits $(\alpha = 3, \beta = +\infty)$.
   * Evaluates leaf $14 \Rightarrow \beta = 14$ (No pruning, $3 < 14$).
   * Evaluates leaf $5 \Rightarrow \beta = 5$ (No pruning, $3 < 5$).
   * Evaluates leaf $2 \Rightarrow \beta = 2$ (All leaves evaluated, $\text{Value}(D) = \mathbf{2}$).
5. **Root A (MAX):**
   * $\text{Value}(A) = \max(\text{Value}(B), \text{Value}(C), \text{Value}(D)) = \max(3, \le 2, 2) = \mathbf{3}$.

* **Final Minimax Value:** **3**
* **Optimal Move:** Move to **Node $B$**.
* **Pruned Nodes:** The unevaluated leaf $x$ under $C$.

---

## SECTION 6: FINAL REVISION & EXAM CHECKLIST

### 6.1 Quick Revision Summary
* **Adversarial Search:** Search in a multi-agent, competitive environment.
* **Game Types:** Two-player, zero-sum, perfect-information, deterministic games.
* **Minimax:** Computes optimal strategy via depth-first complete tree search. Time $O(b^m)$, Space $O(bm)$.
* **Alpha ($\alpha$):** MAX's best choice so far ($-\infty \to \text{increases}$). Updated at MAX nodes.
* **Beta ($\beta$):** MIN's best choice so far ($+\infty \to \text{decreases}$). Updated at MIN nodes.
* **Pruning Rule:** Cut off search whenever **$\alpha \ge \beta$**.
* **Alpha-Beta Complexity:** Best case $O(b^{m/2})$ with optimal move ordering.

---

### 6.2 Key Definitions

| Term | Exam Definition |
| :--- | :--- |
| **Zero-Sum Game** | A game where the sum of utilities across all players is zero for every outcome. |
| **Ply** | One half-move in a game (a single move by one player). |
| **Minimax Value** | The utility of a state assuming both players play perfectly rationally. |
| **Alpha ($\alpha$)** | Lower bound on the utility value MAX is guaranteed to achieve along the path. |
| **Beta ($\beta$)** | Upper bound on the utility value MIN is guaranteed to allow along the path. |
| **Alpha Cutoff** | Pruning of branches below a MIN node when $\beta \le \alpha$. |
| **Beta Cutoff** | Pruning of branches below a MAX node when $\alpha \ge \beta$. |

---

### 6.3 Minimax vs. Alpha-Beta Comparison

| Feature | Minimax Algorithm | Alpha-Beta Pruning |
| :--- | :--- | :--- |
| **Search Scope** | Examines entire game tree. | Examines only relevant subtrees (prunes suboptimal ones). |
| **Time Complexity (Worst)** | $O(b^m)$ | $O(b^m)$ |
| **Time Complexity (Best)** | $O(b^m)$ | **$O(b^{m/2})$** |
| **Space Complexity** | $O(bm)$ | $O(bm)$ |
| **Decision Quality** | Exact optimal decision. | **Same exact root value; an optimal move (ties can yield different optimal moves).** |
| **Parameters** | None. | Uses $\alpha$ and $\beta$ bounds. |

---

### 6.4 Common Exam Mistakes to Avoid

1. ❌ **Mistake:** Changing $\alpha$ at a MIN node or $\beta$ at a MAX node.  
   * **Correction:** $\alpha$ is updated ONLY at MAX nodes; $\beta$ is updated ONLY at MIN nodes.

2. ❌ **Mistake:** Forgetting to pass updated $\alpha$ and $\beta$ values down to child nodes.  
   * **Correction:** Always pass the current $(\alpha, \beta)$ bounds down during DFS calls.

3. ❌ **Mistake:** Pruning when $\alpha < \beta$.  
   * **Correction:** Prune ONLY when **$\alpha \ge \beta$**.

4. ❌ **Mistake:** Thinking Alpha-Beta gives an approximate or different answer than Minimax.  
   * **Correction:** Alpha-Beta returns the exact same root value and an optimal move; when moves tie, the particular optimal move may differ.

---

### 6.5 Complete Syllabus Coverage Checklist

- [x] Two-player, zero-sum, perfect-information game formulation
- [x] Game state, game tree, player objectives, utility values, terminal states
- [x] Optimal decisions in games & bottom-up value propagation
- [x] Minimax algorithm, working principle, pseudocode, time/space complexity
- [x] Alpha-Beta pruning, $\alpha$ and $\beta$ definitions, initial values, update rules
- [x] Pruning condition $\alpha \ge \beta$, move ordering, best-case time complexity $O(b^{m/2})$
- [x] Fully solved 10-mark PYQ numericals with step-by-step traces
- [x] Final revision summary, definitions, comparisons, and exam checklist
