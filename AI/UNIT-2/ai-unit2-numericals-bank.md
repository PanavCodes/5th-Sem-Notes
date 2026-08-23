# UNIT 2 NUMERICAL & PROBLEM-SOLVING QUESTION BANK
## B.Tech (Computer Engineering) — SVKM's NMIMS (MPSTME)
### Subject: Artificial Intelligence (Course Code: 702CO0C076)

This document contains a comprehensive collection of solved numerical, computational, and step-by-step problem-solving questions for **AI Unit 2: Solving Problems by Searching**.

All problems are designed to align with the SVKM's NMIMS B.Tech CE curriculum guidelines, drawing directly from standard university exam patterns, NPTEL lecture sets, and the primary reference textbook, *Stuart Russell & Peter Norvig's Artificial Intelligence: A Modern Approach (4th Edition)*.

---

## SECTION 1: TOPIC-WISE PAST YEAR NUMERICAL QUESTIONS (PYQs)

---

###   [PYQ - 10 MARKS - HARD]
#### Q1. Apply Greedy Best-First Search and $A^*$ Search on the following directed, weighted graph to find the shortest path and path cost from the Start Node $A$ to the Goal Node $G$. Comment on the admissibility of the heuristic.

**Graph Structure and Attributes:**
*   **Nodes:** $A$ (Source), $B$, $C$, $D$, $G$ (Goal)
*   **Straight-line Heuristics to Goal Node ($h(n)$):**
    *   $h(A) = 3$
    *   $h(B) = 2$
    *   $h(C) = 3$
    *   $h(D) = 1$
    *   $h(G) = 0$
*   **Directed Edges with Path Weights ($g(n)$ step-costs):**
    *   $A \rightarrow B = 1$
    *   $A \rightarrow C = 4$
    *   $B \rightarrow D = 2$
    *   $C \rightarrow D = 5$
    *   $B \rightarrow G = 4$
    *   $D \rightarrow G = 1$

*Source: Compiled NMIMS B.Tech CE Re-Exam, Academic Year 2024-25, Q2.c [10 Marks]*

#### **Step-by-Step Solution:**

```text
       (h=3)  [A]
             /   \
          1 /     \ 4
           /       \
     (h=2)[B]     [C](h=3)
          | \     /
         2|  \4  /5
          |   \ /
     (h=1)[D]  V
           \  
          1 \ 
             v
            [G](h=0) [Goal]
```

---

### **Part 1: Greedy Best-First Search (GBFS) Execution**
In Greedy Best-First Search, the evaluation function is solely based on the heuristic estimate to the goal:
$$f(n) = h(n)$$
At each step, we expand the node in the frontier with the lowest $h(n)$ value.

#### **GBFS Search Trace Table:**

| Step | Current Node | Frontier / Open List (with $f(n)=h(n)$) | Selected Node | Reason |
| :---: | :---: | :--- | :---: | :--- |
| **0** | — | $\{ A(3) \}$ | $A$ | Initial state. |
| **1** | $A$ | $\{ B(2), C(3) \}$ | $B$ | Lowest heuristic value ($h(B) = 2 < h(C) = 3$). |
| **2** | $B$ | $\{ G(0), D(1), C(3) \}$ | $G$ | Goal reached ($h(G) = 0$). |

#### **GBFS Results:**
*   **Expansion Order:** $A \rightarrow B \rightarrow G$
*   **Path Found:** $A \rightarrow B \rightarrow G$
*   **Total Path Cost:** $g(G) = \text{cost}(A \rightarrow B) + \text{cost}(B \rightarrow G) = 1 + 4 = 5$

---

### **Part 2: $A^*$ Search Execution**
In $A^*$ Search, we evaluate nodes by combining the actual cost to reach them, $g(n)$, with the estimated cost to the goal, $h(n)$:
$$f(n) = g(n) + h(n)$$

#### **$A^*$ Search Trace Table:**

| Step | Current Node | Frontier / Open List (Node, $g$, $h$, $f$) | Selected Node | Reason |
| :---: | :---: | :--- | :---: | :--- |
| **0** | — | $\{ A(g=0, h=3, f=3) \}$ | $A$ | Initial state. |
| **1** | $A$ | $\{ B(g=1, h=2, f=3), C(g=4, h=3, f=7) \}$ | $B$ | Lowest $f$-cost ($f(B)=3 < f(C)=7$). |
| **2** | $B$ | $\{ D(g=3, h=1, f=4), G(g=5, h=0, f=5), C(g=4, h=3, f=7) \}$ | $D$ | Lowest $f$-cost ($f(D)=4$). |
| **3** | $D$ | $\{ G(g=4, h=0, f=4), C(g=4, h=3, f=7) \}$ | $G$ | Path to $G$ via $D$ ($g=4, f=4$) is cheaper than direct $B \rightarrow G$ ($g=5, f=5$). |

#### **$A^*$ Results:**
*   **Expansion Order:** $A \rightarrow B \rightarrow D \rightarrow G$
*   **Optimal Path:** $A \rightarrow B \rightarrow D \rightarrow G$
*   **Optimal Path Cost:** $g(G) = 1 \ (A\rightarrow B) + 2 \ (B\rightarrow D) + 1 \ (D\rightarrow G) = 4$

---

### **Part 3: Evaluation of Heuristic Admissibility**
A heuristic $h(n)$ is **admissible** if it never overestimates the actual cost to reach the goal state from node $n$. That is, for every node $n$:
$$h(n) \le h^*(n)$$
where $h^*(n)$ is the true shortest path cost from $n$ to $G$.

Let's calculate the true cost $h^*(n)$ for each node:
1.  **Node $G$:** $h^*(G) = 0$. Given $h(G) = 0 \le 0$ (Admissible).
2.  **Node $D$:** Only path is $D \rightarrow G$ (cost 1). $h^*(D) = 1$. Given $h(D) = 1 \le 1$ (Admissible).
3.  **Node $B$:** Paths are $B \rightarrow G$ (cost 4) and $B \rightarrow D \rightarrow G$ (cost $2+1=3$). Thus, $h^*(B) = 3$. Given $h(B) = 2 \le 3$ (Admissible).
4.  **Node $C$:** Path is $C \rightarrow D \rightarrow G$ (cost $5+1=6$). $h^*(C) = 6$. Given $h(C) = 3 \le 6$ (Admissible).
5.  **Node $A$:** Shortest path is $A \rightarrow B \rightarrow D \rightarrow G$ (cost 4). $h^*(A) = 4$. Given $h(A) = 3 \le 4$ (Admissible).

**Conclusion on Admissibility:**  
Since $h(n) \le h^*(n)$ holds true for all nodes, the heuristic is **strictly admissible**. This explains why the $A^*$ search successfully located the mathematically optimal path ($A \rightarrow B \rightarrow D \rightarrow G$ with cost 4), while the greedy search returned a suboptimal path (cost 5).

---

###   [PYQ - 10 MARKS - MEDIUM]
#### Q2. Solve the 8-Puzzle Problem from the given Initial State to the target Goal State using the Greedy Best-First Search (GBFS) algorithm. Use the "Number of Misplaced Tiles" as the heuristic function. Trace all states clearly.

**State Layouts:**
```text
Initial State:           Goal State:
   2   8   3                1   2   3
   1   6   4                8   _   4
   7   _   5                7   6   5
```
*(where "_" represents the blank space)*

*Source: Compiled NMIMS B.Tech CE Final Examination, Academic Year 2023-24, Q4.a [10 Marks]*

#### **Step-by-Step Solution:**

**1. Heuristic Definition ($h(n)$):**  
We count the number of misplaced tiles relative to their target positions in the Goal State, **excluding the blank space**.

**2. Step-by-Step Search Tree Tracing:**

*   **Step 0: Initial State ($S_0$)**
    ```text
    2  8  3
    1  6  4
    7  _  5
    ```
    *   *Comparing against goal:*
        *   Tile 2 (at 1,1; goal is 1,2) $\rightarrow$ Misplaced.
        *   Tile 8 (at 1,2; goal is 2,1) $\rightarrow$ Misplaced.
        *   Tile 3 (at 1,3; goal is 1,3) $\rightarrow$ Correct.
        *   Tile 1 (at 2,1; goal is 1,1) $\rightarrow$ Misplaced.
        *   Tile 6 (at 2,2; goal is 3,2) $\rightarrow$ Misplaced.
        *   Tile 4 (at 2,3; goal is 2,3) $\rightarrow$ Correct.
        *   Tile 7 (at 3,1; goal is 3,1) $\rightarrow$ Correct.
        *   Tile 5 (at 3,3; goal is 3,3) $\rightarrow$ Correct.
    *   **Heuristic value $h(S_0) = 4$** (Misplaced tiles: 2, 8, 1, 6).

*   **Step 1: Expand $S_0$ (Blank at bottom-middle can move Up, Left, or Right):**
    *   **Option 1.1: Move Up (Swap blank with 6)**
        ```text
        2  8  3
        1  _  4
        7  6  5
        ```
        Misplaced tiles: 2, 8, 1. (Tiles 3, 4, 7, 6, 5 are correct).  
        **$h(\text{Option 1.1}) = 3$**
    *   **Option 1.2: Move Left (Swap blank with 7)**
        ```text
        2  8  3
        1  6  4
        _  7  5
        ```
        Misplaced tiles: 2, 8, 1, 6, 7.  
        **$h(\text{Option 1.2}) = 5$**
    *   **Option 1.3: Move Right (Swap blank with 5)**
        ```text
        2  8  3
        1  6  4
        7  5  _
        ```
        Misplaced tiles: 2, 8, 1, 6, 5.  
        **$h(\text{Option 1.3}) = 5$**

    *Selection:* Expand **Option 1.1** since it minimizes $h(n) = 3$.

*   **Step 2: Expand Option 1.1 (Blank at center can move Up, Down, Left, or Right):**
    *   *Note: Moving Down returns to Initial State (avoided via explored list).*
    *   **Option 2.1: Move Up (Swap blank with 8)**
        ```text
        2  _  3
        1  8  4
        7  6  5
        ```
        Misplaced tiles: 2, 1. (8, 3, 4, 7, 6, 5 are correct).  
        **$h(\text{Option 2.1}) = 2$**
    *   **Option 2.2: Move Left (Swap blank with 1)**
        ```text
        2  8  3
        _  1  4
        7  6  5
        ```
        Misplaced: 2, 8, 1.  
        **$h(\text{Option 2.2}) = 3$**
    *   **Option 2.3: Move Right (Swap blank with 4)**
        ```text
        2  8  3
        1  4  _
        7  6  5
        ```
        Misplaced: 2, 8, 1, 4.  
        **$h(\text{Option 2.3}) = 4$**

    *Selection:* Expand **Option 2.1** since it minimizes $h(n) = 2$.

*   **Step 3: Expand Option 2.1 (Blank at top-center can move Down, Left, or Right):**
    *   **Option 3.1: Move Left (Swap blank with 2)**
        ```text
        _  2  3
        1  8  4
        7  6  5
        ```
        Misplaced: 1, 8. (2, 3, 4, 7, 6, 5 are correct).  
        **$h(\text{Option 3.1}) = 2$** (Wait, is 1 misplaced? Yes, goal has 1 at 1,1; here 1 is at 2,1. 8 is misplaced).
    *   **Option 3.2: Move Right (Swap blank with 3)**
        ```text
        2  3  _
        1  8  4
        7  6  5
        ```
        Misplaced: 2, 3, 1, 8.  
        **$h(\text{Option 3.2}) = 4$**

    *Selection:* Expand **Option 3.1** (Heuristic $h = 2$).

*   **Step 4: Expand Option 3.1 (Blank at top-left can move Down or Right):**
    *   **Option 4.1: Move Down (Swap blank with 1)**
        ```text
        1  2  3
        _  8  4
        7  6  5
        ```
        Misplaced: 8. (1, 2, 3, 4, 7, 6, 5 are correct!).  
        **$h(\text{Option 4.1}) = 1$**

    *Selection:* Expand **Option 4.1** ($h = 1$).

*   **Step 5: Expand Option 4.1 (Blank at middle-left can move Up, Down, or Right):**
    *   **Option 5.1: Move Right (Swap blank with 8)**
        ```text
        1  2  3
        8  _  4
        7  6  5
        ```
        *All tiles are in their correct goal positions.*  
        **$h(\text{Option 5.1}) = 0$** (Goal State Reached!)

#### **Final Traced Path and Heuristics:**
$$\text{Initial } [h=4] \xrightarrow{\text{Up}} \text{State 1 } [h=3] \xrightarrow{\text{Up}} \text{State 2 } [h=2] \xrightarrow{\text{Left}} \text{State 3 } [h=2] \xrightarrow{\text{Down}} \text{State 4 } [h=1] \xrightarrow{\text{Right}} \text{Goal State } [h=0]$$

---

###   [PYQ - 5 MARKS - EASY]
#### Q3. Trace the execution of Depth-First Search (DFS) on the following cyclic graph starting from Node $A$ with Goal Node $G$. Assume that alphabetically smaller nodes are expanded first to break ties. Show the complete expansion order.

**Graph Adjacency List:**
*   $A \rightarrow B, C$
*   $B \rightarrow D, E$
*   $C \rightarrow D, G$
*   $D \rightarrow A$ (back edge)

```text
       [A]
      /   \
    [B]   [C]
    / \   / \
  [D]-[E][D][G] (Goal)
```

*Source: Compiled MU, May 2016 [10 Marks] / Dec 2014 [5 Marks]*

#### **Step-by-Step Solution:**

In Depth-First Search, we explore the graph using a Last-In-First-Out (LIFO) stack. Alphabetically smaller neighbors are pushed last so they are popped first, or alternatively, we expand alphabetically smaller nodes first.

#### **DFS Search Trace Table:**

| Step | Current Node | Stack / Frontier (with Parents) | Expanded / Visited Set | Reason |
| :---: | :---: | :--- | :---: | :--- |
| **0** | — | $[ A ]$ | $\emptyset$ | Start Search. |
| **1** | $A$ | $[ B, C ]$ | $\{ A \}$ | Pop $A$. Alphabetically, $B$ is expanded before $C$. |
| **2** | $B$ | $[ D, E, C ]$ | $\{ A, B \}$ | Pop $B$. Neighbors $D, E$ added to top of stack. |
| **3** | $D$ | $[ E, C ]$ | $\{ A, B, D \}$ | Pop $D$. Neighbor $A$ is already visited; backtrack. |
| **4** | $E$ | $[ C ]$ | $\{ A, B, D, E \}$ | Pop $E$. No unvisited neighbors; backtrack. |
| **5** | $C$ | $[ F, G ]$ (represented as $D, G$) | $\{ A, B, D, E, C \}$ | Pop $C$. Neighbors $D$ (visited) and $G$ added. |
| **6** | $G$ | — | $\{ A, B, D, E, C, G \}$ | Pop $G$ (Goal). Goal state met! |

#### **DFS Results:**
*   **Expansion Order:** $A \rightarrow B \rightarrow D \rightarrow E \rightarrow C \rightarrow G$
*   **Path Found:** $A \rightarrow C \rightarrow G$

---

###   [PYQ - 10 MARKS - HARD]
#### Q4. Trace the execution of $A^*$ Search on the following directed, weighted graph to find the shortest path from the Start Node $S$ to the Goal Node $G$. Show the complete open list calculations at each step.

**Graph Attributes:**
*   **Start Node:** $S$, **Goal Node:** $G$
*   **Heuristic Values ($h(n)$):**
    *   $h(S) = 14$
    *   $h(B) = 12$
    *   $h(C) = 11$
    *   $h(d) = 6$
    *   $h(e) = 4$
    *   $h(f) = 11$
    *   $h(G) = 0$
*   **Directed Edge Weights:**
    *   $S \rightarrow B = 4$
    *   $S \rightarrow C = 3$
    *   $B \rightarrow f = 5$
    *   $B \rightarrow e = 12$
    *   $C \rightarrow e = 10$
    *   $C \rightarrow d = 7$
    *   $d \rightarrow e = 2$
    *   $f \rightarrow G = 6$
    *   $e \rightarrow G = 5$

*Source: Compiled NMIMS B.Tech CE Final Exam, Academic Year 2025-2026, Q3.a [10 Marks]*

#### **Step-by-Step Solution:**

We compute $f(n) = g(n) + h(n)$ at each level of expansion.

#### **$A^*$ Search Trace Table:**

| Step | Current Node | Frontier / Open List (Node, $g$, $h$, $f$) | Selected Node | Reason |
| :---: | :---: | :--- | :---: | :--- |
| **0** | — | $\{ S(0, 14, 14) \}$ | $S$ | Start at root node. |
| **1** | $S$ | $\{ C(3, 11, 14), B(4, 12, 16) \}$ | $C$ | Lowest $f$-cost ($f(C) = 14$). |
| **2** | $C$ | $\{ B(4, 12, 16), d(10, 6, 16), e_1(13, 4, 17) \}$ | $B$ | Lowest $f$-cost (Tied $B$ vs $d$; break alphabetically). |
| **3** | $B$ | $\{ d(10, 6, 16), e_1(13, 4, 17), f(9, 11, 20) \}$ | $d$ | Lowest $f$-cost ($f(d) = 16$). |
| **4** | $d$ | $\{ e_2(12, 4, 16), f(9, 11, 20) \}$ | $e_2$ | Path cost to $e$ via $d$ is $12$ ($f(e)=16$), cheaper than $e_1$ ($13$). |
| **5** | $e$ | $\{ G(17, 0, 17), f(9, 11, 20) \}$ | $G$ | Lowest $f$-cost ($f(G) = 17$). |

#### **$A^*$ Results:**
*   **Expansion Order:** $S \rightarrow C \rightarrow B \rightarrow d \rightarrow e \rightarrow G$
*   **Optimal Path Found:** $S \rightarrow C \rightarrow d \rightarrow e \rightarrow G$
*   **Optimal Path Cost:** $g(G) = 3 \ (S\rightarrow C) + 7 \ (C\rightarrow d) + 2 \ (d\rightarrow e) + 5 \ (e\rightarrow G) = 17$

---

## SECTION 2: HIGH-YIELD EXPECTED NUMERICAL PROBLEMS

---

###   [EXPECTED - 6 MARKS - MEDIUM]
#### Q5. Perform Uniform Cost Search (UCS) on the following weighted graph. Find the shortest path from start node $S$ to goal node $G$.

**Graph Connectivity:**
*   $S \rightarrow A$ (cost 2), $S \rightarrow B$ (cost 5)
*   $A \rightarrow C$ (cost 3), $A \rightarrow D$ (cost 8)
*   $B \rightarrow D$ (cost 4), $B \rightarrow G$ (cost 9)
*   $C \rightarrow G$ (cost 6)
*   $D \rightarrow G$ (cost 2)

#### **Step-by-Step Solution:**

Uniform Cost Search is equivalent to Dijkstra's algorithm. It expands nodes in order of non-decreasing path cost $g(n)$ from the start node.

#### **UCS Search Trace Table:**

| Step | Current Node | Frontier / Open List (Node, $g(n)$) | Selected Node | Reason |
| :---: | :---: | :--- | :---: | :--- |
| **0** | — | $\{ S(0) \}$ | $S$ | Start node. |
| **1** | $S$ | $\{ A(2), B(5) \}$ | $A$ | Lowest path cost ($2 < 5$). |
| **2** | $A$ | $\{ B(5), C(5), D(10) \}$ | $B$ | Lowest path cost (Tied $B$ vs $C$; break alphabetically). |
| **3** | $B$ | $\{ C(5), D_2(9), G_1(14) \}$ | $C$ | $D$ updated via $B$ since $g(D)=5+4=9 < 10$. |
| **4** | $C$ | $\{ D_2(9), G_2(11) \}$ | $D_2$ | $G$ updated via $C$ since $g(G)=5+6=11 < 14$. |
| **5** | $D_2$ | $\{ G_3(11) \}$ | $G$ | $G$ updated via $D$ since $g(G)=9+2=11$ (equal to $G_2$). |
| **6** | $G$ | — | $G$ | Goal expanded. |

#### **UCS Results:**
*   **Optimal Path:** $S \rightarrow A \rightarrow C \rightarrow G$ (or $S \rightarrow B \rightarrow D \rightarrow G$)
*   **Optimal Path Cost:** 11

---

###   [EXPECTED - 6 MARKS - MEDIUM]
#### Q6. Trace the behavior of Steepest-Ascent Hill Climbing on a 1D state-space landscape where the state is represented by an integer $x \in \{1, 2, \dots, 10\}$. Analyze two different start states and determine if they reach the global maximum.

**Objective Function Values ($f(x)$):**
*   $f(1) = 12$
*   $f(2) = 15$
*   $f(3) = 18$
*   $f(4) = 16$ (Local Maximum / Foothill)
*   $f(5) = 14$
*   $f(6) = 15$
*   $f(7) = 18$
*   $f(8) = 22$
*   $f(9) = 25$ (Global Maximum)
*   $f(10) = 20$

#### **Step-by-Step Solution:**

In Steepest-Ascent Hill Climbing, the transition rule allows the agent to move to a neighbor state only if that neighbor has a strictly higher objective value than the current state: $f(\text{neighbor}) > f(\text{current})$. Neighbors of state $x$ are $x-1$ and $x+1$ (boundary states have only one neighbor).

#### **Scenario A: Start State $x_0 = 2$**
1.  **Step 1:** Current state is $2$ ($f(2) = 15$). Neighbors are $\{1, 3\}$.
    *   $f(1) = 12$, $f(3) = 18$.
    *   Best neighbor is $3$ ($18 > 15$). Move to $3$.
2.  **Step 2:** Current state is $3$ ($f(3) = 18$). Neighbors are $\{2, 4\}$.
    *   $f(2) = 15$, $f(4) = 16$.
    *   Both neighbor values are strictly less than current $f(3) = 18$.
    *   **Result:** Algorithm terminates at $x = 3$.
    *   **Verdict:** Stuck at a **Local Maximum** ($f(3) = 18$) and fails to reach the global maximum.

#### **Scenario B: Start State $x_0 = 7$**
1.  **Step 1:** Current state is $7$ ($f(7) = 18$). Neighbors are $\{6, 8\}$.
    *   $f(6) = 15$, $f(8) = 22$.
    *   Best neighbor is $8$ ($22 > 18$). Move to $8$.
2.  **Step 2:** Current state is $8$ ($f(8) = 22$). Neighbors are $\{7, 9\}$.
    *   $f(7) = 18$, $f(9) = 25$.
    *   Best neighbor is $9$ ($25 > 22$). Move to $9$.
3.  **Step 3:** Current state is $9$ ($f(9) = 25$). Neighbors are $\{8, 10\}$.
    *   $f(8) = 22$, $f(10) = 20$.
    *   Both neighbor values are less than current $f(9) = 25$.
    *   **Result:** Algorithm terminates at $x = 9$.
    *   **Verdict:** Successfully reaches the **Global Maximum** ($f(9) = 25$).

---

## SECTION 3: TOPIC-WISE PYQ FREQUENCY ANALYSIS

The following chart outlines the approximate revision priority levels of key Unit 2 search topics based on their historical occurrence in SVKM's NMIMS and Mumbai University examinations from 2013-2026:

```text
┌─────────────────────────────────────────────────────────────┐
│             UNIT 2 TOPIC FREQUENCY IN EXAMS               │
├──────────────────────────────────────────────┬──────────────┤
│ A* Search Graph/Heuristic Tracing            │ ▓▓▓▓▓▓ (40%) │
│ 8-Puzzle Misplaced/Manhattan Calculations   │ ▓▓▓▓   (30%) │
│ Hill Climbing Problems & Traps               │ ▓▓     (15%) │
│ Uninformed Search Traversals (BFS/DFS/UCS)   │ ▓▓     (15%) │
└─────────────────────────────────────────────────────────────┘
```

---

## SECTION 4: EASY / MEDIUM / HARD NUMERICAL CLASSIFICATION

To plan your study schedule effectively, practice problems in order of increasing cognitive complexity:

### **1. Easy Numericals (2 to 4 Marks)**
*   **Heuristic Computations:** Calculating the misplaced tiles heuristic $h_1(n)$ and Manhattan distance heuristic $h_2(n)$ for arbitrary 8-puzzle configurations.
*   **Simple Search Trees:** Drawing the search frontier step-by-step for standard DFS and BFS graphs.

### **2. Medium Numericals (5 to 6 Marks)**
*   **Steepest-Ascent Traces:** Step-by-step state optimization traces for Hill Climbing under local traps.
*   **Uniform Cost Search:** Tracing nodes on complex cyclic graphs using path cost $g(n)$ tracking.
*   **Greedy Best-First Search:** Routing over spatial grids with Euclidean/Straight-line distances.

### **3. Hard Numericals (8 to 10 Marks)**
*   **Combined Graph Solvers:** Routing over weighted directed graphs using both $A^*$ and GBFS and analyzing heuristic admissibility.
*   **Consistent vs. Admissible Proofs:** Mathematical induction proofs demonstrating why consistency guarantees admissibility but the converse is not true.

---

## SECTION 5: MOST IMPORTANT EXAM NUMERICALS

Prioritize these three specific categories of numericals for Class Test-1 and your Term End Exams:
1.  **Weighted Graph $A^*$ Tracing:** Memorize the formula $f(n) = g(n) + h(n)$. Ensure you update path costs in the frontier if a cheaper path is found to an unexpanded node.
2.  **8-Puzzle Manhattan Distances:** Understand that the Manhattan distance of a tile is $|x_1 - x_2| + |y_1 - y_2|$. The total heuristic is the sum of these values across all 8 tiles, **ignoring the blank space**.
3.  **Hill Climbing Anomalies:** Be ready to draw the 3-dimensional diagrams for a Local Maximum, Plateau, and Ridge, explaining how sideways-move limits and random restarts resolve them.

---

## SECTION 6: MIXED-ALGORITHM GRAPH COMPARISONS

---

###   [EXPECTED - 10 MARKS - HARD]
#### Q7. Differentiate between Uninformed and Informed Search strategies. Show how BFS, DFS, UCS, GBFS, and $A^*$ Search expand nodes differently by running them on the following cyclic weighted graph.

**Graph Connectivity and Values:**
*   **Nodes:** $S$ (Start), $A$, $B$, $G$ (Goal)
*   **Heuristics ($h(n)$):** $h(S)=4, \ h(A)=2, \ h(B)=3, \ h(G)=0$.
*   **Edges:** $S \rightarrow A = 2, \ S \rightarrow B = 1, \ A \rightarrow G = 3, \ B \rightarrow A = 1, \ B \rightarrow G = 6$.

#### **Step-by-Step Comparative Solutions:**

#### **1. Breadth-First Search (BFS) Trace:**
*   *Strategy:* Expand layer-by-layer (FIFO).
*   *Trace:*
    1.  Expand $S$. Frontier: $[ A, B ]$.
    2.  Expand $A$. Goal $G$ is generated as a child. In standard BFS, we goal-test on generation, so the search terminates immediately.
*   *Path Found:* $S \rightarrow A \rightarrow G$
*   *Path Cost:* $2 + 3 = 5$.

#### **2. Depth-First Search (DFS) Trace:**
*   *Strategy:* Explore deepest branch first (LIFO). Tie-break alphabetically.
*   *Trace:*
    1.  Expand $S$. Frontier: $[ A, B ]$.
    2.  Expand $A$ (alphabetically smaller). Children: $G$.
    3.  Expand $G$ (Goal). Goal reached.
*   *Path Found:* $S \rightarrow A \rightarrow G$
*   *Path Cost:* $2 + 3 = 5$.

#### **3. Uniform Cost Search (UCS) Trace:**
*   *Strategy:* Expand node with lowest path cost $g(n)$ (FIFO queue sorted by cost).
*   *Trace:*
    1.  Expand $S$. Frontier: $\{ B(1), A(2) \}$.
    2.  Expand $B$ (cost 1). Children: $A$ (cost $1+1=2$), $G$ (cost $1+6=7$). Frontier: $\{ A(2), G(7) \}$.
    3.  Expand $A$ (cost 2). Children: $G$ (cost $2+3=5$). Frontier: $\{ G(5), G(7) \}$.
    4.  Expand $G$ (cost 5). Goal reached.
*   *Path Found:* $S \rightarrow B \rightarrow A \rightarrow G$
*   *Path Cost:* $1 \ (S\rightarrow B) + 1 \ (B\rightarrow A) + 3 \ (A\rightarrow G) = 5$ (Optimal).

#### **4. Greedy Best-First Search (GBFS) Trace:**
*   *Strategy:* Expand node with lowest $h(n)$.
*   *Trace:*
    1.  Expand $S$. Frontier: $\{ A(h=2), B(h=3) \}$.
    2.  Expand $A$. Children: $G(h=0)$.
    3.  Expand $G$. Goal reached.
*   *Path Found:* $S \rightarrow A \rightarrow G$
*   *Path Cost:* $2 + 3 = 5$.

#### **5. $A^*$ Search Trace:**
*   *Strategy:* Expand node with lowest $f(n) = g(n) + h(n)$.
*   *Trace:*
    1.  Expand $S$. Frontier: $\{ B(g=1, f=1+3=4), A(g=2, f=2+2=4) \}$.
    2.  Expand $B$ (Lowest $f$, tie-break alphabetically). Children: $A(g=2, f=2+2=4)$, $G(g=7, f=7+0=7)$. Frontier: $\{ A(2, 2, 4), G(7, 0, 7) \}$.
    3.  Expand $A$. Children: $G(g=5, f=5+0=5)$. Frontier: $\{ G(5, 0, 5), G(7, 0, 7) \}$.
    4.  Expand $G$. Goal reached.
*   *Path Found:* $S \rightarrow B \rightarrow A \rightarrow G$
*   *Path Cost:* 5 (Optimal).

---

## SECTION 7: FORMULA & CALCULATION QUICK SHEET

Maximize your revision efficiency by practicing with these quick formulas:

*   **$A^*$ Evaluation Function:**
    $$f(n) = g(n) + h(n)$$
*   **Admissibility Condition:**
    $$h(n) \le h^*(n) \quad \forall n \in S$$
*   **Consistency (Monotonicity) Condition:**
    $$h(n) \le c(n, a, n') + h(n') \quad \forall \text{ successor } n' \text{ of } n$$
*   **Manhattan Distance Formula for a single tile $i$:**
    $$d_{\text{Manhattan}}(i) = |x_{\text{current}} - x_{\text{goal}}| + |y_{\text{current}} - y_{\text{goal}}|$$
*   **Total Heuristic $h_2(n)$:**
    $$h_2(n) = \sum_{i=1}^8 d_{\text{Manhattan}}(i)$$

---

## SECTION 8: COMPLETE UNIT 2 NUMERICAL COVERAGE CHECKLIST

Use this checklist to track your numerical problem-solving readiness before the exam:

*   [x] Traced directed graph routing using $A^*$ Search and $f(n) = g(n) + h(n)$.
*   [x] Calculated 8-puzzle misplaced tiles heuristic $h_1(n)$ step-by-step.
*   [x] Calculated 8-puzzle Manhattan distances $h_2(n)$ step-by-step.
*   [x] Analyzed heuristic admissibility and consistency conditions.
*   [x] Traced Steepest-Ascent Hill Climbing and recognized local optima traps.
*   [x] Compared node expansion orders for BFS, DFS, UCS, GBFS, and $A^*$ on a cyclic graph.

---

## SECTION 9: OUT-OF-SYLLABUS VERIFICATION LOG

To keep your study focus fully optimized, we have verified that the following non-examinable topics have been **completely excluded** from this question bank:
*   **Genetic Algorithms (GA):** No calculations regarding crossover rates, roulette-wheel selection, or mutations.
*   **Adversarial Search / Game Playing:** No Minimax search trees, Alpha-Beta evaluation values, or game state updates.

---
*End of Question Bank. Practice these solutions on paper to ensure high performance in your exam!*
