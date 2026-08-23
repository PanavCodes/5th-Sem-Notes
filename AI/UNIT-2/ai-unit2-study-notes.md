# UNIT 2 STUDY NOTES: PROBLEM SOLVING AND SEARCH
## B.Tech (Computer Engineering) — SVKM's NMIMS (MPSTME)
### Subject: Artificial Intelligence (Course Code: 702CO0C076)

---

## SECTION 1: PROBLEM FORMULATION & FOUNDATIONS (LECTURE 5)

*Mapped Bloom's Taxonomy Level: **Understand** (CO2)*

### 1.1 Problem-Solving Agents

🧠 **Must Understand**  
A **problem-solving agent** is a goal-based agent that decides what to do by finding sequences of actions that lead to desirable states [175, 195]. When the correct action to take is not immediately obvious, the agent must plan ahead by simulating action sequences in an abstract model before acting in the real world [195, 197].

#### The "Formulate, Search, Execute" Paradigm [55, 180, 197]:
1.  **Formulate Goal:** Based on the current situation and performance measure, the agent defines a goal, which is a set of world states where the goal is satisfied [15, 16, 51, 116, 177].
2.  **Formulate Problem:** The agent decides what actions and states to consider given the goal [16, 52, 117, 178]. This is the process of abstraction.
3.  **Search:** The agent simulates sequences of actions in its model, searching until it finds a sequence of actions that reaches the goal [197]. This sequence is the **solution** [197].
4.  **Execute:** The agent executes the actions in the solution, one at a time, ignoring external percepts during execution (running "open-loop") [180, 197]. Once executed, it formulates a new goal [55, 180].

```text
                  ┌─────────────────────────────────┐
                  │          Formulate Goal         │
                  └────────────────┬────────────────┘
                                   │
                                   ▼
                  ┌─────────────────────────────────┐
                  │        Formulate Problem        │
                  └────────────────┬────────────────┘
                                   │
                                   ▼
                  ┌─────────────────────────────────┐
                  │      Search for a Solution      │
                  └────────────────┬────────────────┘
                                   │
                                   ▼
                  ┌─────────────────────────────────┐
                  │    Execute Solution (Actions)   │
                  └─────────────────────────────────┘
```

#### Simple Problem-Solving Agent Pseudocode [18, 19, 56, 57, 119, 120, 139, 140, 159, 160, 179, 180]:
```python
def SIMPLE-PROBLEM-SOLVING-AGENT(percept):
    persistent: seq = []       # Action sequence, initially empty
    persistent: state = None   # Description of the current world state
    persistent: goal = None    # A goal, initially null
    persistent: problem = None # A problem formulation

    state = UPDATE-STATE(state, percept)
    if not seq:
        goal = FORMULATE-GOAL(state)
        problem = FORMULATE-PROBLEM(state, goal)
        seq = SEARCH(problem)
        if seq == "failure":
            return "NoOp"
    action = seq[0]
    seq = seq[1:]
    return action
```

#### Underlying Environmental Assumptions [181]:

For a simple problem-solving agent to operate successfully with its "eyes closed" (ignoring percepts during execution), the environment must be [181]:
*   **Static:** The environment does not change during planning or execution [181].
*   **Observable / Known:** The initial state is fully known [181].
*   **Discrete:** States and actions are clearly distinct and countable [181].
*   **Deterministic:** Each action has exactly one guaranteed outcome, meaning no unexpected events can occur [181].

---

### 1.2 Formal Problem Formulation

⭐ **Must Remember**  
A search problem is formally defined by **five components** in the modern AIMA framework [18, 56, 119, 139, 159, 198, 209]:

1.  **Initial State:** The state the agent starts in [18, 56, 119, 139, 159]. Represented as $s_0 \in S$ (e.g., $In(Arad)$) [18, 56, 119, 139, 159].
2.  **Actions:** A description of the possible actions available to the agent in a state $s$ [18, 19, 120, 140, 160]. Denoted as $Actions(s)$ (e.g., $Actions(Arad) = \{Go(Sibiu), Go(Timisoara), Go(Zerind)\}$).
3.  **Transition Model:** A formal description of what each action does [209]. Represented as a function $Result(s, a)$ that returns the state reached by executing action $a$ in state $s$ (e.g., $Result(In(Arad), Go(Sibiu)) = In(Sibiu)$).
    *   **State Space:** The set of all states reachable from the initial state by executing any sequence of actions [10, 39, 198]. It forms a directed graph [10].
4.  **Goal Test:** A function that determines whether a given state is a goal state [11]. It can be:
    *   *Explicit:* Checking against a specific set of goal states (e.g., state == $In(Bucharest)$).
    *   *Implicit:* Checking if a state satisfies a condition (e.g., $CheckMate(s)$ or $NoQueensClashing(s)$).
5.  **Path Cost (Action Cost Function):** A function that assigns a numeric cost to each action [11, 209]. Denoted as $c(s, a, s')$.
    *   The path cost of a sequence of actions is the sum of the step costs along the path [11].
    *   **Optimal Solution:** A solution with the lowest path cost among all possible solutions [12].

---

### 1.3 Searching for Solutions

🧠 **Must Understand**  
Search algorithms take a formulated problem as input and construct an abstract **Search Tree** superimposed over the underlying **State Space Graph** [11, 55].

#### Distinguishing State Space Graph vs. Search Tree:

*   **State Space Graph:** Represents the physical structure of the world. Nodes in this graph are unique physical states, and edges represent transitions. For $ Romania $, there are exactly 20 cities (20 unique states).
*   **Search Tree:** Represents the paths explored by the search algorithm. Nodes in the search tree represent *paths* from the root to that state. A single physical state can appear multiple times in a search tree as different nodes (representing different paths to reach that state) [207].

#### Core Nodes and Data Structures [199]:

*   **Tree Node:** A data structure used to build the search tree. A node $n$ typically contains:
    *   `state`: The state in the state space corresponding to the node [20].
    *   `parent`: The node in the search tree that generated this node.
    *   `action`: The action that was applied to the parent to generate this node.
    *   `path-cost` ($g(n)$): The total cost of the path from the root to this node [25, 49, 125, 146, 165].
*   **Frontier:** The set of all leaf nodes available for expansion at any given point [20, 199]. Also called the *open list*.
*   **Reached Set / Explored Set:** A set tracking all states that have already been visited/expanded to avoid infinite loops and redundant search paths [199]. Also called the *closed list*.
*   **Expansion:** Applying the transition model to a selected node from the frontier to generate its child nodes [199].

---

## SECTION 2: UNINFORMED SEARCH STRATEGIES (LECTURE 6)

*Mapped Bloom's Taxonomy Level: **Apply** (CO2)*

Uninformed (blind) search strategies have no information about the distance from the current state to the goal [176]. They only know how to generate successors and distinguish goal states from non-goal states [176].

```text
                               ┌─────────────────────────────┐
                               │  UNINFORMED SEARCH METHODS  │
                               └──────────────┬──────────────┘
                    ┌─────────────────────────┼─────────────────────────┐
                    ▼                         ▼                         ▼
         ┌───────────────────┐     ┌───────────────────┐     ┌───────────────────┐
         │   BREADTH-FIRST   │     │    DEPTH-FIRST    │     │   UNIFORM COST    │
         │   SEARCH (BFS)    │     │   SEARCH (DFS)    │     │   SEARCH (UCS)    │
         └───────────────────┘     └───────────────────┘     └───────────────────┘
         • Expands shallowest      • Expands deepest         • Expands lowest
           nodes first               nodes first               path cost g(n)
         • FIFO Queue              • LIFO Stack              • Priority Queue
```

### 2.1 Breadth-First Search (BFS)

⭐ **Must Remember**  
BFS expands the shallowest unexpanded node first [20, 21, 30, 66, 130, 141, 142, 151, 170].

*   **Frontier Implementation:** First-In-First-Out (FIFO) queue [20].
*   **Goal Test Timing:** Applied to a node **when the node is generated** (added to the frontier), rather than when it is selected for expansion [20, 58]. This optimization saves substantial computational steps.
*   **Completeness:** **Yes**, if the branching factor $b$ is finite and a solution exists [203].
*   **Optimality:** **Yes**, if and only if all action step costs are identical (or a nondecreasing function of depth) [20, 203].
*   **Complexities:**
    *   **Time Complexity:** $O(b^d)$, where $b$ is the branching factor and $d$ is the depth of the shallowest solution [40, 184, 203].
    *   **Space Complexity:** $O(b^d)$, because all explored and frontier nodes must be retained in memory [40, 184, 203].
*   **Major Drawback:** Exponential space requirements. Space is the primary bottleneck of BFS.

---

### 2.2 Depth-First Search (DFS)

⭐ **Must Remember**  
DFS always expands the deepest unexpanded node in the current frontier [23, 30, 66, 123, 130, 144, 151, 170, 202].

*   **Frontier Implementation:** Last-In-First-Out (LIFO) stack [123, 144, 202].
*   **Goal Test Timing:** Applied to a node **when it is selected for expansion**.
*   **Completeness:**
    *   *Tree-search version:* **No** [5, 184, 202]. It can get trapped going down an infinite path (even if a solution exists elsewhere) [5, 202].
    *   *Graph-search version:* **Yes** in finite state spaces with loop checking [203].
*   **Optimality:** **No** [203]. It may return a highly suboptimal path without exploring shorter alternatives.
*   **Complexities:**
    *   **Time Complexity:** $O(b^m)$, where $m$ is the maximum depth of the search tree [184, 203]. If $m$ is much larger than $d$, DFS is extremely slow compared to BFS [184, 203].
    *   **Space Complexity:** $O(b \cdot m)$ (Linear space!) [30, 66, 130, 151, 170, 184, 203]. Once a branch is fully explored, it is pruned from memory.
*   **Major Advantage:** Linear memory efficiency.

---

### 2.3 Uniform Cost Search (UCS)

⭐ **Must Remember**  
UCS (equivalent to **Dijkstra's Algorithm** in computer science) expands the node $n$ with the **lowest path cost** $g(n)$ [14, 21, 30, 58, 66, 122, 130, 142, 143, 151, 170, 200].

*   **Frontier Implementation:** Priority Queue, sorted in ascending order of path cost $g(n)$ [14, 58, 200].
*   **Goal Test Timing:** Applied **when the node is selected for expansion**, NOT when generated [58, 200].
    *   *Reasoning:* A shorter path to a generated goal node might be discovered later. Testing on expansion guarantees that the first goal expanded is indeed the cheapest path [58, 182, 202].
*   **Completeness:** **Yes**, provided that every action cost is strictly greater than a small positive constant $\epsilon$ ($\epsilon > 0$) [22, 59, 122, 143, 162, 183, 201]. This prevents infinite loops of zero-cost actions [59].
*   **Optimality:** **Yes**, cost-optimal for general step costs [30, 66, 130, 151, 170, 202, 203].
*   **Complexities:**
    *   **Time & Space Complexity:** $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$, where $C^*$ is the cost of the optimal solution and $\epsilon$ is the minimum action cost [22, 59, 122, 143, 162, 183, 201]. This can be much larger than $b^d$ if step costs are highly non-uniform [22, 59, 122, 143, 162, 183, 201].

---

### 2.4 Uninformed Search Comparison Table

✍️ **Exam Focus**  
*Memorize this complete comparison matrix, highly favored as a 10-mark university question:*

| Metric | **Breadth-First Search (BFS)** | **Depth-First Search (DFS)** | **Uniform Cost Search (UCS)** |
| :--- | :--- | :--- | :--- |
| **Frontier Queue** | FIFO Queue [20] | LIFO Stack [123, 144, 202] | Priority Queue, sorted by $g(n)$ [14, 58, 200] |
| **Goal Test Timing** | On generation [20, 58] | On expansion | On expansion [58, 200] |
| **Completeness** | Yes (if branching factor $b$ is finite) [203] | No (unless graph search in finite space) [5, 184, 202, 203] | Yes (if step costs $\ge \epsilon > 0$) [22, 59, 122, 143, 162, 183, 201] |
| **Optimality** | Yes (for uniform step costs) [20, 203] | No [203] | Yes (cost-optimal for general step costs) [30, 66, 130, 151, 170, 202, 203] |
| **Time Complexity** | $O(b^d)$ [40, 184, 203] | $O(b^m)$ [184, 203] | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ [22, 59, 122, 143, 162, 183, 201] |
| **Space Complexity** | $O(b^d)$ [40, 184, 203] | $O(b \cdot m)$ [30, 66, 130, 151, 170, 184, 203] | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ [22, 59, 122, 143, 162, 183, 201] |
| **Primary Drawback** | Exponential memory bottleneck [40, 184, 203]. | Prone to infinite cycles; non-optimal [5, 202, 203]. | Explores large trees of low-cost paths unnecessarily [22, 59, 122, 143, 162, 183, 201]. |

---

### 2.5 Worked Example: Uninformed Search Trace

Consider the following state space graph where the start state is **S** and the goal state is **G**:

```text
       [B] ──(5)──> [F]
      /   ▲          │
    (4)   │          │
    /    (12)       (16)
   /      │          │
 [S] ───> [C] ──(10)─> [E] ──(5)──> [G]
   \      │          ▲
   (3)   (7)         │
     \    ▼          │
       [D] ──(2)─────┘
```

#### Step-by-Step Expansion Trace:

#### **A. Breadth-First Search (BFS):**
1.  **Initialize:** Frontier = `[S]`
2.  **Expand S:** Goal test is run on children on generation.
    *   Neighbors generated: B, C, D. None are goal.
    *   Frontier = `[B, C, D]`. Explored = `{S}`.
3.  **Expand B:** 
    *   Neighbor generated: F (not goal).
    *   Frontier = `[C, D, F]`. Explored = `{S, B}`.
4.  **Expand C:**
    *   Neighbors generated: D, E (not goal).
    *   Frontier = `[D, F, E]`. Explored = `{S, B, C}`.
5.  **Expand D:**
    *   Neighbor generated: E (already reached).
    *   Frontier = `[F, E]`. Explored = `{S, B, C, D}`.
6.  **Expand F:**
    *   Neighbor generated: E, G. **Goal G is generated!** Stop immediately.
7.  **BFS Path Returned:** $S \rightarrow B \rightarrow F \rightarrow G$ (Step Count = 3).
8.  **BFS Path Cost:** $4 + 5 + 16 = 25$.

#### **B. Uniform Cost Search (UCS):**

Nodes are expanded based on minimal $g(n)$ path cost. Goal test is run only on expansion.
1.  **Initialize:** Frontier = `[(0, S)]`
2.  **Pop (0, S):** Goal test fails ($S 
e G$).
    *   Expand S: Add neighbors to frontier with cumulative costs.
    *   Frontier = `[(3, D), (4, B), (12, C)]` (since $g(C)=12$, $g(B)=4$, $g(D)=3$).
3.  **Pop (3, D):** Goal test fails.
    *   Expand D: Generates E with cost $3 + 2 = 5$.
    *   Frontier = `[(4, B), (5, E), (12, C)]`.
4.  **Pop (4, B):** Goal test fails.
    *   Expand B: Generates F with cost $4 + 5 = 9$.
    *   Frontier = `[(5, E), (9, F), (12, C)]`.
5.  **Pop (5, E):** Goal test fails.
    *   Expand E: Generates G with cost $5 + 5 = 10$.
    *   Frontier = `[(9, F), (10, G), (12, C)]`.
6.  **Pop (9, F):** Goal test fails.
    *   Expand F: Generates G with cost $9 + 16 = 25$. Since $25 > 10$ (already in frontier), ignore.
    *   Frontier = `[(10, G), (12, C)]`.
7.  **Pop (10, G):** **Goal test passes!** Return path.
8.  **UCS Path Returned:** $S \rightarrow D \rightarrow E \rightarrow G$.
9.  **UCS Optimal Path Cost:** 10. (Optimal!)

---

## SECTION 3: INFORMED HEURISTIC SEARCH METHODS (LECTURE 7)

*Mapped Bloom's Taxonomy Level: **Apply** (CO2)*

Informed search strategies use domain-specific knowledge to select the most promising path. This knowledge is formalized as a **Heuristic Function** $h(n)$ [2, 16, 25, 49, 125, 146, 165, 204]:
\[h(n) = 	ext{Estimated cost of the cheapest path from the current node } n 	ext{ to a goal state.}\]
*   If $n$ is a goal state, then $h(n) = 0$ [26, 147, 166].

---

### 3.1 Greedy Best-First Search (GBFS)

⭐ **Must Remember**  
GBFS expands the node that is estimated to be closest to the goal, evaluating nodes strictly by their heuristic values [2, 3, 38, 42, 60, 99, 100, 194, 204, 210, 218]:
$$f(n) = h(n)$$

*   **Frontier Implementation:** Priority Queue sorted in ascending order of $h(n)$.
*   **Completeness:**
    *   *Tree-search version:* **No** [91]. It can fall into infinite loops (e.g., getting stuck shuttling back and forth between two nodes if the heuristic values are misleading) [90, 91].
    *   *Graph-search version:* **Yes** in finite state spaces with repeated-state checking [3, 204].
*   **Optimality:** **No** [5, 194, 210, 218]. It ignores path cost $g(n)$ entirely, selecting paths that seem short locally but are highly suboptimal globally [77, 194].
*   **Complexities:**
    *   **Time & Space Complexity:** $O(b^m)$ in the worst case [3, 5, 48, 204]. However, a highly informative heuristic can dramatically reduce complexity to $O(b \cdot m)$ [3, 204].

#### Romania Route-Finding Example (Arad to Bucharest) [2, 3, 26, 60, 126, 147, 166, 196, 207]:

Straight-line distance heuristic to Bucharest ($h_{SLD}$):
*   $h_{SLD}(Arad) = 366$ [126, 147, 166]
*   $h_{SLD}(Sibiu) = 253$ [26, 61, 147, 166]
*   $h_{SLD}(Fagaras) = 176$ [26, 126, 147, 166]
*   $h_{SLD}(Bucharest) = 0$ [26, 147, 166]

**Progress:** Arad ($366$) $\rightarrow$ Sibiu ($253$) $\rightarrow$ Fagaras ($176$) $\rightarrow$ Bucharest ($0$) [2, 3, 60]. Finds path without expanding any other branch, but the path is not optimal if the actual roads are circuitous.

---

### 3.2 A\* Search

⭐ **Must Remember**  
$A^*$ Search minimizes the total estimated solution cost by combining the path cost so far $g(n)$ and the estimated cost to the goal $h(n)$ [5, 6, 25, 42, 48, 49, 125, 146, 165, 194, 204, 210, 218]:
$$f(n) = g(n) + h(n)$$
*   $f(n) = 	ext{Estimated cost of the cheapest solution passing through node } n$ [25, 125, 146, 165, 204].

#### Conditions for Optimality: Admissibility and Consistency

Whether $A^*$ is cost-optimal depends on two mathematical properties of its heuristic:

1.  **Admissible Heuristic:** A heuristic is admissible if it **never overestimates** the true cost to reach a goal state [7, 26, 77, 112, 126, 147, 166, 205]. It is optimistic [205]. Let $h^*(n)$ be the true minimum cost to reach the goal from $n$:
    \[h(n) \le h^*(n) \quad 	ext{and} \quad h(n) \ge 0\]
    *   *Theorem:* **Tree-search $A^*$ is optimal if $h(n)$ is admissible** [27, 62, 127, 148, 167, 194, 207].
2.  **Consistent Heuristic (Monotonicity):** A heuristic is consistent if, for every node $n$ and every successor $n'$ generated by an action $a$, the estimated cost of reaching the goal from $n$ is no greater than the step cost of moving from $n$ to $n'$ plus the estimated cost of reaching the goal from $n'$ [27, 28, 62, 63, 127, 128, 148, 149, 167, 168, 206, 207]:
    $$h(n) \le c(n, a, n') + h(n')$$
    *   This is a form of the **triangle inequality** [207].
    *   *Theorem:* **Graph-search $A^*$ is optimal if $h(n)$ is consistent** [27, 62, 92, 127, 148, 167, 207].
    *   *Important Property:* **Every consistent heuristic is also admissible** (consistency $\implies$ admissibility) [92, 207].

```text
              n ──────────── h(n) ──────────> Goal
             /                                  ▲
  c(n,a,n') /                                  /
           /                    h(n')          /
          n' ─────────────────────────────────
```

#### Key Properties of A\* Search:

*   **Completeness:** **Yes**, provided action costs are bounded below by a small positive constant $\epsilon$ ($\epsilon > 0$) [205].
*   **Optimality:** **Yes**, cost-optimal (under admissibility/consistency) [42, 194, 207, 210, 218].
*   **Optimal Efficiency:** For a given heuristic, no other optimal algorithm is guaranteed to expand fewer nodes than $A^*$ [7, 112].
*   **Space Bottleneck:** Since $A^*$ must retain all generated nodes in memory to maintain the frontier and explored sets, it usually runs out of space long before it runs out of time [185, 210].

---

### 3.3 Heuristic Search Comparison Table

✍️ **Exam Focus**  
*Highly tested in NMIMS exams. Contrast these two algorithms:*

| Feature Metric | **Greedy Best-First Search (GBFS)** | **$A^*$ Search** |
| :--- | :--- | :--- |
| **Evaluation Function** | $f(n) = h(n)$ [2, 38, 204, 210] | $f(n) = g(n) + h(n)$ [5, 25, 42, 49, 125, 146, 165, 204, 210] |
| **Primary Focus** | Speed; minimizes estimated remaining path [194, 218]. | Optimality; minimizes total estimated solution cost [194, 218]. |
| **Completeness** | No (can get stuck in loops in Tree Search) [90, 91]. | Yes (if branching factor is finite) [205]. |
| **Optimality** | No [5, 194, 210, 218]. | Yes (if heuristic is admissible/consistent) [42, 194, 207, 210, 218]. |
| **Memory Retention** | High (must store frontier) [5, 48]. | High (primary bottleneck of the algorithm) [185, 210]. |
| **Romania Progress** | Fast, but ignores actual road distances [194]. | Balanced; uses road weights and straight-line heuristics [204]. |

---

### 3.4 Worked Example: Informed Search Trace ($S \rightarrow G$)

Using the same graph from Section 2.5, we introduce the following heuristic estimates $h(n)$ to the goal $G$:
*   $h(S) = 14$
*   $h(B) = 12$
*   $h(C) = 11$
*   $h(D) = 6$
*   $h(E) = 4$
*   $h(F) = 16$
*   $h(G) = 0$

#### **A. Greedy Best-First Search (GBFS):**

Nodes sorted strictly by $f(n) = h(n)$.
1.  **Initialize:** Frontier = `[(14, S)]`
2.  **Pop S:** Expand S. Neighbors added:
    *   B: $h(B) = 12$
    *   C: $h(C) = 11$
    *   D: $h(D) = 6$
    *   Frontier = `[(6, D), (11, C), (12, B)]`.
3.  **Pop D:** Expand D. Neighbor added:
    *   E: $h(E) = 4$.
    *   Frontier = `[(4, E), (11, C), (12, B)]`.
4.  **Pop E:** Expand E. Neighbor added:
    *   G: $h(G) = 0$.
    *   Frontier = `[(0, G), (11, C), (12, B)]`.
5.  **Pop G:** **Goal reached!**
6.  **GBFS Path Returned:** $S \rightarrow D \rightarrow E \rightarrow G$ (Moves = 3).
7.  **Actual Path Cost:** $3 + 2 + 5 = 10$.

#### **B. $A^*$ Search:**

Nodes sorted by $f(n) = g(n) + h(n)$.
1.  **Initialize:** Frontier = `[(14, S)]` ($g(S)=0, h(S)=14$)
2.  **Pop S:** Expand S.
    *   B: $g(B)=4, h(B)=12 \implies f(B) = 4+12=16$
    *   C: $g(C)=3, h(C)=11 \implies f(C) = 3+11=14$
    *   D: $g(D)=3, h(D)=6 \implies f(D) = 3+6=9$
    *   Frontier = `[(9, D), (14, C), (16, B)]`.
3.  **Pop D:** Expand D.
    *   E: $g(E) = g(D)+c(D,E) = 3+2=5$. $h(E)=4 \implies f(E) = 5+4=9$.
    *   Frontier = `[(9, E), (14, C), (16, B)]`.
4.  **Pop E:** Expand E.
    *   G: $g(G) = g(E)+c(E,G) = 5+5=10$. $h(G)=0 \implies f(G) = 10+0=10$.
    *   Frontier = `[(10, G), (14, C), (16, B)]`.
5.  **Pop G:** **Goal reached!**
6.  **$A^*$ Path Returned:** $S \rightarrow D \rightarrow E \rightarrow G$.
7.  **Actual Path Cost:** 10. (Optimal!)

---

## SECTION 4: LOCAL SEARCH & OPTIMIZATION (LECTURES 8 & 9)

*Mapped Bloom's Taxonomy Level: **Apply** (CO2)*

Local search algorithms evaluate and modify one or more **current states** rather than systematically exploring paths from a root node [211]. They use very little memory (usually $O(1)$ constant memory) because they do not maintain a search tree [46, 211].

---

### 4.1 Hill Climbing Search

🧠 **Must Understand**  
Hill climbing is a simple loop that continually moves in the direction of increasing value (or decreasing cost), head-to-head with its immediate neighbors [186, 211]. It is often called **greedy local search** [186, 211].

#### The AIMA Metaphor:

> *"Hill climbing is like climbing Mount Everest in a thick fog with amnesia."* [105, 186]
> * You can only observe your immediate surroundings (thick fog) [105, 186].
> * You have no memory of the path you took to get there (amnesia) [105, 186].

#### Steepest-Ascent Hill Climbing Algorithm [75]:
```python
def HILL-CLIMBING(problem):
    current = MAKE-NODE(problem.INITIAL-STATE)
    while True:
        neighbor = a state with the highest VALUE among current's neighbors
        if neighbor.VALUE <= current.VALUE:
            return current.STATE
        current = neighbor
```

---

### 4.2 Drawbacks of Hill Climbing Search

✍️ **Exam Focus**  
*Hill climbing is incomplete and easily gets trapped by three famous terrestrial anomalies:*

```text
     Value
       │         GLOBAL MAXIMUM
       │              /\
       │             /  \
       │  LOCAL     /    \      PLATEAU (Flat)
       │  MAXIMUM  /      \    ┌───────────┐    /\
       │     /\   /        \  /             \  /  \
       │    /  \ /          \/               \/    \
       │   /    X                                   \
       └──────────────────────────────────────────── (State Space)
```

#### 1. Local Maxima (Foothills) [31, 43, 68, 73, 131, 152, 171, 187, 216]:

*   **Concept:** A peak that is higher than all its immediate neighbors, but lower than the global maximum [31, 43, 68, 73, 131, 152, 171, 187, 216].
*   **Trap:** Because all neighboring states go downhill, the algorithm thinks it has reached the global optimum and terminates prematurely [31, 68, 73, 131, 152, 171, 187, 216].
*   **Solution:** **Backtracking** to an earlier decision node or executing **Random-Restart Hill Climbing** [45, 75, 103, 104, 216].

#### 2. Plateaus [32, 44, 69, 74, 132, 153, 172, 188, 213, 216]:

*   **Concept:** A flat region of the state space landscape where all neighboring states have the identical evaluation score [32, 44, 69, 74, 132, 153, 172, 188, 213, 216].
*   **Trap:** The algorithm cannot determine which direction to move because no neighbor is better than the current state [44, 74, 188, 213]. It gets lost wandering aimlessly [32, 69, 74, 132, 153, 172, 188, 213].
    *   *Flat Local Maximum:* No uphill exit exists [32, 69, 132, 153, 172, 188, 213].
    *   *Shoulder:* Uphill progress is possible if the agent moves sideways [32, 69, 103, 132, 153, 172, 188, 213, 214].
*   **Solution:** Allow **Sideways Moves** (moving to a neighbor of equal value) but limit consecutive sideways moves (e.g., max 100) to prevent infinite loops [103, 214].

#### 3. Ridges [32, 44, 45, 69, 70, 75, 132, 133, 153, 154, 172, 173, 188, 189, 212]:

*   **Concept:** A long, narrow region of high land with steep slopes falling away on either side [75, 212].
*   **Trap:** The ridge rises from left to right, but the grid of available moves is aligned with cardinal directions (North, South, East, West) [75, 133, 154, 173, 189, 212]. Moving in any single cardinal direction goes downhill, so the search terminates even though an diagonal path leads uphill [75, 133, 154, 173, 189, 212].
*   **Solution:** Moving in multiple directions at once (vector step combinations), using **Random-Restart**, or applying a sequence of rules before evaluating the state [45, 46, 75].

---

## SECTION 5: COMPREHENSIVE SUMMARY & EXAM TOOLKIT

### 5.1 Important Definitions & Formulas

*   **Heuristic Function ($h(n)$):** Estimated cost of the cheapest path from node $n$ to a goal [25, 49, 125, 146, 165, 204].
*   **Admissible Heuristic:** $h(n) \le h^*(n)$ for all nodes, where $h^*(n)$ is the true optimal cost [7, 112].
*   **Consistent Heuristic:** $h(n) \le c(n, a, n') + h(n')$ for all transitions [27, 28, 62, 63, 127, 128, 148, 149, 167, 168, 206, 207].
*   **Expected Utility (A\* Sort):** $f(n) = g(n) + h(n)$ [5, 25, 42, 49, 125, 146, 165, 204, 210].
*   **UCS/BFS Time/Space Complexities:** BFS $= O(b^d)$ [40, 184, 203], UCS $= O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ [22, 59, 122, 143, 162, 183, 201].

---

### 5.2 Solved Exam-Style Problems

#### **Problem 1 (True/False Theory):**

*   *Question:* Is it possible for a heuristic to be consistent but not admissible? Explain with proof.
*   *Answer:* **No, it is mathematically impossible.** Every consistent heuristic is guaranteed to be admissible. We prove this by induction on the path length to the goal.
    *   Let $n_k \rightarrow n_{k-1} \rightarrow \dots \rightarrow n_0$ be the optimal path from node $n_k$ to the goal $n_0$ (where $h(n_0)=0$).
    *   By consistency: $h(n_i) - h(n_{i-1}) \le c(n_i, a, n_{i-1})$.
    *   Summing these inequalities from $i=1$ to $k$:
        $$\sum_{i=1}^k (h(n_i) - h(n_{i-1})) \le \sum_{i=1}^k c(n_i, a, n_{i-1})$$
    *   The left-hand side telescopes to $h(n_k) - h(n_0) = h(n_k)$.
    *   The right-hand side is exactly the true optimal path cost $h^*(n_k)$.
    *   Therefore, $h(n_k) \le h^*(n_k)$, proving admissibility [92, 207].

#### **Problem 2 (8-Puzzle Heuristic Check):**

*   *Question:* Contrast the "Misplaced Tiles" heuristic ($h_1$) and the "Manhattan Distance" heuristic ($h_2$) for the 8-puzzle. Which is superior and why?
*   *Answer:*
    *   **Misplaced Tiles ($h_1$):** Counts the number of tiles out of their goal positions [76]. It is admissible since each misplaced tile must be moved at least once.
    *   **Manhattan Distance ($h_2$):** Sum of the vertical and horizontal distances of each tile from its goal position [22]. It is admissible because a tile must move at least that many times to reach its goal.
    *   **Comparison:** $h_2$ is strictly superior because it **dominates** $h_1$ (for every node $n$, $h_2(n) \ge h_1(n)$). In $A^*$ search, a dominating admissible heuristic is guaranteed to expand fewer nodes, making the search computationally more efficient.

---

### 5.3 Quick last-minute revision checklist

*   [ ] Can I write the 5 components of a formal search problem from memory? [18, 56, 119, 139, 159, 198, 209]
*   [ ] Do I know when to apply the goal test in BFS vs. UCS? (BFS = on generation [20, 58], UCS = on expansion [58, 200]).
*   [ ] Can I write the definitions of admissibility [7, 26, 77, 112, 126, 147, 166, 205] and consistency from memory? [27, 28, 62, 63, 127, 128, 148, 149, 167, 168, 206, 207]
*   [ ] Do I understand the "Everest in a fog" metaphor for Hill Climbing? [105, 186]
*   [ ] Can I sketch the visual diagrams for Local Maxima, Plateaus, and Ridges? [31, 32, 43, 44, 45, 68, 69, 70, 73, 74, 75, 131, 132, 133, 152, 153, 154, 171, 172, 173, 187, 188, 189, 212, 213]

---

## SECTION 6: COURSE POLICY AUDIT & EXCLUSIONS

### 6.1 Course Policy Checklist (Unit 2)

| Topic | Status | Detailed Location | Prescribed Source |
| :--- | :---: | :--- | :--- |
| **Problem-solving agents** | ✅ Fully Covered | Section 1.1 | *AIMA Chapter 3* [175, 195] |
| **Problem formulation** | ✅ Fully Covered | Section 1.2 | *AIMA Chapter 3* [18, 56, 119, 139, 159, 198, 209] |
| **Searching for solutions** | ✅ Fully Covered | Section 1.3 | *AIMA Chapter 3* [11, 55, 199] |
| **Breadth-First Search (BFS)** | ✅ Fully Covered | Section 2.1 | *AIMA Chapter 3* [20, 141] |
| **Depth-First Search (DFS)** | ✅ Fully Covered | Section 2.2 | *AIMA Chapter 3* [23, 144] |
| **Uniform Cost Search (UCS)** | ✅ Fully Covered | Section 2.3 | *AIMA Chapter 3* [14, 58, 200] |
| **Informed search strategies** | ✅ Fully Covered | Section 3 | *AIMA Chapter 3* [176, 204] |
| **Greedy Best-First Search** | ✅ Fully Covered | Section 3.1 | *AIMA Chapter 3* [2, 3, 204] |
| **$A^*$ Search & Optimality** | ✅ Fully Covered | Section 3.2 | *AIMA Chapter 3* [5, 27, 62, 125, 204] |
| **Hill Climbing Search** | ✅ Fully Covered | Section 4.1 | *AIMA Chapter 4* [186, 211] |
| **Hill Climbing Drawbacks** | ✅ Fully Covered | Section 4.2 | *AIMA Chapter 4* [31, 32, 72, 187] |

---

### 6.2 Out-of-Syllabus Exclusion Checklist

| Excluded Topic | Status | Exclusion Verification |
| :--- | :---: | :--- |
| **Genetic Algorithms (GA)** | 🚫 Excluded | Checked. No population-based optimization, selection, crossover, or mutation. |
| **Adversarial Search / Game Playing** | 🚫 Excluded | Checked. No Minimax, Alpha-Beta Pruning, or multi-agent game rules. |

---

### 6.3 Source Coverage Checklist

| Syllabus Topic | Primary Source(s) Used | Relevant Passages / Figures |
| :--- | :--- | :--- |
| **Agent / Problem Formulation** | `efdd4d1d4c2087fe1cbe03d9ced67f34.pdf` | Chapter 3, pp. 81-87 [195, 198, 209] |
| **Uninformed Search Methods** | `Artificial-Intelligence-A-Modern-Approach-3rd-Edition.pdf` | Section 3.4, BFS vs DFS vs UCS [182, 184] |
| **Informed Search Methods** | `Sem 5 aids_ AIML AI pyq Solutions .l.pdf` | Tabulated trace equations & Romanian examples [135, 195] |
| **Hill Climbing Drawbacks** | `Artificial Intelligence and Soft Computing.pdf` | Section 2.17, Foothills/Plateau/Ridge traps [43, 44, 45] |
| **A* Optimization Proofs** | `NPTEL Lecture.pdf` | NPTEL Slide 12, Admissibility and Consistency bounds [92, 93] |

---
*End of Study Notes.*
