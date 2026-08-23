# UNIT 2 PYQ & EXPECTED QUESTION BANK
## B.Tech (Computer Engineering) — SVKM's NMIMS (MPSTME)
### Subject: Artificial Intelligence (Course Code: 702CO0C076)

This document contains a comprehensive, technically rigorous collection of **Past Year Questions (PYQs)** from SVKM's NMIMS University and Mumbai University (MU), combined with high-yield **Expected and Probable Questions** compiled from the official course policy and prescribed textbooks (*Russell & Norvig AIMA 4th Edition*, *Dan Patterson*, and *Rich & Knight*).

All probability ratings, topic weightage percentages, and priority levels are approximate revision priorities based on a qualitative audit of available past papers and syllabus emphasis from 2013-2026.

---

## SECTION 1: TOPIC-WISE PYQ & EXPECTED ANALYSIS INDEX

To support structured revision, the questions in this bank are categorized by topic and priority level. Every question listed below is provided with a complete, exam-ready model answer in this document.

### 1.1 Past Year Questions (PYQs)

*   **Q1. Apply Greedy Best-First Search and A* Search on a weighted graph to find the shortest path and path cost, and comment on the admissibility of the heuristic.**  
    *   *Source:* Compiled NMIMS B.Tech CE Final Examination, Batch 2024-25, Q2.c [10 Marks]
    *   *Priority:* 🔥 **Very High Probability**
*   **Q2. Explain the Best-First Search algorithm and solve the 8-puzzle problem using Heuristic (h = Number of misplaced tiles) for a specific initial and goal configuration.**  
    *   *Source:* Compiled NMIMS B.Tech CE Final Examination, Academic Year 2023-24, Q4.a [10 Marks]
    *   *Priority:* 🔥 **Very High Probability**
*   **Q3. Explain A* Search in detail. What are the criteria for admissibility and consistency? Explain its drawbacks and show that A* is optimally efficient.**  
    *   *Source:* Compiled MU, May 2013 [10 Marks] | MU, Dec 2013 [10 Marks] | MU, May 2014 [10 Marks]
    *   *Priority:* 🔥 **Very High Probability**
*   **Q4. Give a comparative analysis of uninformed search strategies (BFS, DFS, UCS, DLS, IDS, Bidirectional) with respect to completeness, optimality, time complexity, and space complexity.**  
    *   *Source:* Compiled NMIMS D-24 [10 Marks] | MU, May 2013 [10 Marks] | MU, Dec 2014 [10 Marks]
    *   *Priority:* 🔥 **Very High Probability**
*   **Q5. Write a short note on the Hill Climbing search algorithm. Explain its core limitations (Local Maxima, Plateaus, Ridges) with the help of neat diagrams and suggest how to overcome them.**  
    *   *Source:* Compiled MU, Dec 2013 [5 Marks] | MDU BCA, 2015 / 2018 [10 Marks]
    *   *Priority:* ⭐ **High Probability**
*   **Q6. Explain the Depth-First Search (DFS) algorithm with a neat example tracing node expansion and state storage.**  
    *   *Source:* Compiled MU, Dec 2012 [4 Marks] | MU, May 2016 [10 Marks]
    *   *Priority:* ⭐ **High Probability**
*   **Q7. Explain the Breadth-First Search (BFS) algorithm with a neat example tracing node expansion.**  
    *   *Source:* Compiled MU, May 2014 [10 Marks]
    *   *Priority:* ⭐ **High Probability**

### 1.2 High-Yield Expected Practice Questions

*   **Q8. Explain the concept of a Problem-Solving Agent. Describe the formal 5-component problem formulation framework with a real-world example.**  
    *   *Type:* Expected Conceptual Question
    *   *Priority:* 🔥 **Very High Probability**
*   **Q9. Distinguish between Uninformed (Blind) Search and Informed (Heuristic) Search strategies. Provide a comprehensive comparison matrix.**  
    *   *Type:* Expected Conceptual Question
    *   *Priority:* 🔥 **Very High Probability**
*   **Q10. Explain the structural differences between Tree Search and Graph Search. Why is Graph Search critical for preventing infinite loops in cyclic search spaces?**  
    *   *Type:* Expected Theoretical Question
    *   *Priority:* ⭐ **High Probability**
*   **Q11. Mathematically derive the worst-case time and space complexities of BFS, DFS, and Uniform Cost Search (UCS).**  
    *   *Type:* Expected Mathematical Question
    *   *Priority:* ⭐ **High Probability**
*   **Q12. Prove that if an evaluation heuristic h(n) is consistent (monotone), it must also be admissible.**  
    *   *Type:* Expected Proof-Based Question
    *   *Priority:* 🟡 **Moderate Probability**

---

## SECTION 2: EXAM TRENDS & WEIGHTAGE DYNAMICS

Based on a qualitative audit of available SVKM's NMIMS and Mumbai University past question papers over the last decade, the distribution of exam marks for Unit 2 search topics is structured as follows:

```text
┌─────────────────────────────────────────────────────────────┐
│             UNIT 2 MARKS DISTRIBUTION (APPROX.)             │
├──────────────────────────────────────────────┬──────────────┤
│ Informed Search (A* & GBFS Solvers / Proofs) │ ▓▓▓▓▓▓ (40%) │
│ Uninformed Search (BFS, DFS, UCS Comparison) │ ▓▓▓▓   (30%) │
│ Local Search (Hill Climbing & Drawbacks)     │ ▓▓     (20%) │
│ Problem Formulation & Graph/Tree Theory      │ ▓      (10%) │
└──────────────────────────────────────────────┴──────────────┘
```

### Key Exam Trends to Memorize:
1.  **Strict Path Tracking:** When tracing step-by-step state space search problems, always maintain the explicit `OPEN` (frontier) and `CLOSED` (explored) sets in tabular format. Points are heavily deducted if the state queue tracking is absent.
2.  **Visual Graph Layouts:** Hand-drawn search trees must display both the path cost $g(n)$ and the heuristic estimate $h(n)$ alongside each expanded node to receive full marks.
3.  **Complexities and Edge Cases:** For Uniform Cost Search (UCS), remember that time and space complexities are expressed as $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$, where $\epsilon$ is the minimum positive step cost and $C^*$ is the optimal path cost.

---

## SECTION 3: EXAM-READY MODEL ANSWERS FOR PAST YEAR QUESTIONS (PYQs)

---

### 🔥 [PYQ - 10 MARKS]
#### Q1. Apply Greedy Best-First Search and A* Search on the following weighted graph to find the shortest path and path cost. Comment on the admissibility of the heuristic.

```text
               (A) [h=3]
              /   \
           2 /     \ 1
            v       v
     (B) [h=2]     (C) [h=2]
        / \           \
       2   \ 4       4 \ 5
      v     v           v
  (D) [h=2] \          (G) [Goal, h=0]
      \       \
     1 \       \ (B->G = 4)
        v       v
       (G)     (G)

Note: Edges — A->B=2, A->C=1, B->D=2, B->G=4, C->D=4, C->G=5, D->G=1
```

**Graph Specifications:**
*   **Nodes:** $A$ (Source), $B$, $C$, $D$, $G$ (Goal).
*   **Straight-Line Heuristic Distances $h(n)$ to Goal $G$:**
    *   $h(A) = 3$
    *   $h(B) = 2$
    *   $h(C) = 2$
    *   $h(D) = 2$
    *   $h(G) = 0$
*   **Weighted Directed Edges (with Step Costs):**
    *   $A \rightarrow B = 2$
    *   $A \rightarrow C = 1$
    *   $B \rightarrow D = 2$
    *   $B \rightarrow G = 4$
    *   $C \rightarrow D = 4$
    *   $C \rightarrow G = 5$
    *   $D \rightarrow G = 1$

*Source: Compiled NMIMS B.Tech CE Final Examination, Batch 2024-25, Q2.c [10 Marks]*

#### **Exam-Ready Answer:**

**1. Greedy Best-First Search (GBFS) Trace:**  
GBFS selects nodes strictly on the basis of the heuristic function: $f(n) = h(n)$. It prioritizes the node that appears closest to the goal.

*   **Step 1:** Start at Node $A$.  
    *   Fringe (Queue): $\{ [A, h=3] \}$
    *   Expand $A$. Generated Successors: $B$ and $C$.
    *   Fringe: $\{ [B, h=2], [C, h=2] \}$
*   **Step 2:** Resolve tie alphabetically: Select Node $B$ for expansion.
    *   Expand $B$. Generated Successors: $D$ and Goal $G$.
    *   Heuristics: $h(D) = 2$, $h(G) = 0$.
    *   Fringe: $\{ [G, h=0], [C, h=2], [D, h=2] \}$
*   **Step 3:** Select Node $G$ (minimum $h = 0$).  
    *   Goal reached!
    *   **GBFS Selected Path:** $A \rightarrow B \rightarrow G$
    *   **GBFS Path Cost:** $g(G) = cost(A \rightarrow B) + cost(B \rightarrow G) = 2 + 4 = 6$.

---

**2. $A^*$ Search Trace:**  
$A^*$ evaluates nodes using $f(n) = g(n) + h(n)$, where $g(n)$ is the exact path cost from start to $n$, and $h(n)$ is the heuristic estimate to the goal.

*   **Step 1:** Start at Node $A$.  
    *   $g(A) = 0, h(A) = 3 \Rightarrow f(A) = 3$.
    *   Fringe: $\{ [A, f=3] \}$
    *   Expand $A$. Successors:
        *   $B$: $g(B) = 2, h(B) = 2 \Rightarrow f(B) = 2 + 2 = 4$.
        *   $C$: $g(C) = 1, h(C) = 2 \Rightarrow f(C) = 1 + 2 = 3$.
    *   Fringe: $\{ [C, f=3], [B, f=4] \}$
*   **Step 2:** Select Node $C$ (minimum $f = 3$).
    *   Expand $C$. Successors:
        *   $D$: $g(D) = g(C) + cost(C \rightarrow D) = 1 + 4 = 5$. $h(D) = 2 \Rightarrow f(D) = 5 + 2 = 7$.
        *   $G$: $g(G) = g(C) + cost(C \rightarrow G) = 1 + 5 = 6$. $h(G) = 0 \Rightarrow f(G) = 6 + 0 = 6$.
    *   Fringe: $\{ [B, f=4], [G_{via C}, f=6], [D_{via C}, f=7] \}$
*   **Step 3:** Select Node $B$ (minimum $f = 4$).
    *   Expand $B$. Successors:
        *   $D$: $g(D) = g(B) + cost(B \rightarrow D) = 2 + 2 = 4$. (Shorter path to $D$ discovered). $h(D) = 2 \Rightarrow f(D) = 4 + 2 = 6$.
        *   $G$: $g(G) = g(B) + cost(B \rightarrow G) = 2 + 4 = 6$. $h(G) = 0 \Rightarrow f(G) = 6 + 0 = 6$.
    *   Fringe: $\{ [D_{via B}, f=6], [G_{via C}, f=6], [G_{via B}, f=6] \}$ (Discarding suboptimal $D_{via C}$).
*   **Step 4:** Resolve tie by expanding Node $D_{via B}$ (minimum $f = 6$).
    *   Expand $D_{via B}$. Successor:
        *   $G$: $g(G) = g(D_{via B}) + cost(D \rightarrow G) = 4 + 1 = 5$. $h(G) = 0 \Rightarrow f(G) = 5 + 0 = 5$.
    *   Fringe: $\{ [G_{via D}, f=5], [G_{via C}, f=6], [G_{via B}, f=6] \}$
*   **Step 5:** Select Node $G_{via D}$ (minimum $f = 5$). Goal reached!
    *   **$A^*$ Selected Path:** $A \rightarrow B \rightarrow D \rightarrow G$
    *   **$A^*$ Path Cost:** $5$ (Optimal Path).

---

**3. Evaluation of Heuristic Admissibility:**  
A heuristic $h(n)$ is **admissible** if it never overestimates the true remaining cost to reach the goal: $h(n) \le h^*(n)$ for all $n$, where $h^*(n)$ is the true optimal cost from $n$ to $G$.

Let us check each node individually:
*   **Node $A$:** $h(A) = 3$. True optimal cost $h^*(A) = 5$ (path $A \rightarrow B \rightarrow D \rightarrow G$). Since $3 \le 5$, it is admissible.
*   **Node $B$:** $h(B) = 2$. True optimal cost $h^*(B) = 3$ (path $B \rightarrow D \rightarrow G$). Since $2 \le 3$, it is admissible.
*   **Node $C$:** $h(C) = 2$. True optimal cost $h^*(C) = 5$ (path $C \rightarrow D \rightarrow G$). Since $2 \le 5$, it is admissible.
*   **Node $D$:** $h(D) = 2$. True optimal cost $h^*(D) = 1$ (path $D \rightarrow G$).
    *   **Overestimation Check:** Here, $h(D) = 2 > h^*(D) = 1$.
    *   **Verdict:** The heuristic overestimates the remaining cost at Node $D$. Therefore, the heuristic is **NOT admissible**.

---

### 🔥 [PYQ - 10 MARKS]
#### Q2. Explain the Best-First Search algorithm. Solve the 8-puzzle problem using Best-First Search Technique. Assume h(n) = Number of misplaced tiles.

**Problem Configuration:**

```text
Initial State:        Goal State:
  2   8   3             1   2   3
  1   6   4             8   _   4
  7   _   5             7   6   5
```

*Source: Compiled NMIMS B.Tech CE Final Examination, Academic Year 2023-24, Q4.a [10 Marks]*

#### **Exam-Ready Answer:**

**1. Best-First Search (Greedy Best-First) Concept:**  
Best-First Search is an informed search strategy that selects the next node for expansion based on a heuristic evaluation function, $f(n) = h(n)$, where $h(n)$ is the estimated cost from node $n$ to the goal. It is implemented using a priority queue (fringe) ordered by ascending $h(n)$ values.

**2. Heuristic Definition (Misplaced Tiles):**  
The heuristic $h(n)$ counts the number of physical tiles that are currently not in their correct goal positions. The empty/blank space (denoted `_`) is excluded from this count.

**3. Step-by-Step State Space Trace:**

```text
  Step 0: Initial State [h = 4] (Misplaced: 2, 8, 1, 6)
             [ 2   8   3 ]
             [ 1   6   4 ]
             [ 7   _   5 ]
                     |
            (Move Blank UP)
                     v
  Step 1: Intermediate State [h = 3] (Misplaced: 2, 8, 1)
             [ 2   8   3 ]
             [ 1   _   4 ]
             [ 7   6   5 ]
                     |
            (Move Blank UP)
                     v
  Step 2: Intermediate State [h = 2] (Misplaced: 2, 8)
             [ 2   _   3 ]
             [ 1   8   4 ]
             [ 7   6   5 ]
                     |
           (Move Blank LEFT)
                     v
  Step 3: Intermediate State [h = 2] (Misplaced: 1, 8)
             [ _   2   3 ]
             [ 1   8   4 ]
             [ 7   6   5 ]
                     |
           (Move Blank DOWN)
                     v
  Step 4: Intermediate State [h = 1] (Misplaced: 8)
             [ 1   2   3 ]
             [ _   8   4 ]
             [ 7   6   5 ]
                     |
           (Move Blank RIGHT)
                     v
  Step 5: Goal State reached! [h = 0]
             [ 1   2   3 ]
             [ 8   _   4 ]
             [ 7   6   5 ]
```

*   **Step 0 (Start):** State $S_0$. Misplaced tiles: $2$ (should be 1), $8$ (should be center), $1$ (should be mid-left), $6$ (should be bottom-mid). Heuristic $h(S_0) = 4$.
    *   *Possible Moves:*
        1.  Move Blank Left: $h = 5$ (Tile 7 misplaced).
        2.  Move Blank Right: $h = 5$ (Tile 5 misplaced).
        3.  Move Blank Up: Resulting state has tiles 1, 2, 8 misplaced. $h = 3$.  
    *   *Decision:* Choose **Move Blank Up** (minimum $h = 3$).
*   **Step 1:** State $S_1$ ($2, 8, 3 / 1, \_, 4 / 7, 6, 5$). $h(S_1) = 3$.
    *   *Possible Moves:*
        1.  Move Blank Down: Loops back to $S_0$ (discarded).
        2.  Move Blank Left: $h = 3$ (tiles 2, 8, 1 misplaced).
        3.  Move Blank Right: $h = 4$.
        4.  Move Blank Up: Resulting state has tiles 2, 8 misplaced. $h = 2$.
    *   *Decision:* Choose **Move Blank Up** (minimum $h = 2$).
*   **Step 2:** State $S_2$ ($2, \_, 3 / 1, 8, 4 / 7, 6, 5$). $h(S_2) = 2$.
    *   *Possible Moves:*
        1.  Move Blank Down: Loops back (discarded).
        2.  Move Blank Left: Resulting state has tiles 1, 8 misplaced. $h = 2$.
        3.  Move Blank Right: $h = 3$.
    *   *Decision:* Choose **Move Blank Left** (minimum $h = 2$).
*   **Step 3:** State $S_3$ ($\_, 2, 3 / 1, 8, 4 / 7, 6, 5$). $h(S_3) = 2$.
    *   *Possible Moves:*
        1.  Move Blank Right: Loops back (discarded).
        2.  Move Blank Down: Resulting state has only tile 8 misplaced. $h = 1$.
    *   *Decision:* Choose **Move Blank Down** (minimum $h = 1$).
*   **Step 4:** State $S_4$ ($1, 2, 3 / \_, 8, 4 / 7, 6, 5$). $h(S_4) = 1$.
    *   *Possible Moves:*
        1.  Move Blank Up: Loops back (discarded).
        2.  Move Blank Right: Resulting state has all tiles in correct place. $h = 0$.
    *   *Decision:* Choose **Move Blank Right** (minimum $h = 0$).
*   **Step 5:** Goal State reached.
    *   **Solution Path found in 5 moves:** Up $\rightarrow$ Up $\rightarrow$ Left $\rightarrow$ Down $\rightarrow$ Right.

---

### 🔥 [PYQ - 10 MARKS]
#### Q3. Explain A* Search in detail. What are the criteria for admissibility and consistency? Explain its drawbacks and show that A* is optimally efficient.

*Source: Compiled MU, May 2013 [10 Marks] | MU, Dec 2013 [10 Marks] | MU, May 2014 [10 Marks]*

#### **Exam-Ready Answer:**

**1. Definition of A* Search:**  
$A^*$ Search is an informed graph-navigation algorithm that evaluates nodes by combining the path cost $g(n)$ (cost from the start node to node $n$) with the heuristic estimate $h(n)$ (estimated cost from $n$ to the goal):
$$f(n) = g(n) + h(n)$$
where $f(n)$ represents the estimated total cost of the cheapest solution passing through node $n$.

---

**2. Criteria for Optimality:**

*   **Admissibility (Required for Tree Search):**  
    A heuristic $h(n)$ is **admissible** if it never overestimates the true remaining cost to reach the goal. That is:
    $$0 \le h(n) \le h^*(n)$$
    for all nodes $n$, where $h^*(n)$ is the actual cheapest cost from $n$ to the goal. Admissibility ensures that the first goal node selected for expansion is optimal, as any suboptimal goal node $G_2$ would have $f(G_2) = g(G_2) > g(G) = f(G)$.
*   **Consistency/Monotonicity (Required for Graph Search):**  
    A heuristic $h(n)$ is **consistent** if, for every node $n$ and every successor $n'$ generated by an action $a$, the estimated cost of reaching the goal from $n$ is no greater than the step cost $c(n, a, n')$ plus the estimated cost of reaching the goal from $n'$:
    $$h(n) \le c(n, a, n') + h(n')$$
    Consistency ensures that the path cost $f(n)$ along any path is non-decreasing (monotonic). Under consistency, once $A^*$ expands a node, the path to that node is guaranteed to be optimal, eliminating the need to re-open closed nodes.

---

**3. Drawbacks of A* Search:**
*   **Exponential Space Complexity:** $A^*$ keeps all generated nodes in memory (in the `OPEN` and `CLOSED` sets) to perform duplicate checking and path tracking. Its space complexity is $O(b^d)$, making it highly impractical for large problems, where it typically runs out of RAM long before it runs out of CPU time.
*   **Heuristic Sensitivity:** The performance of $A^*$ is heavily dependent on the quality of $h(n)$. If the heuristic is uninformative, the search degrades into a blind Uniform Cost Search.

---

**4. Optimally Efficient Proof (Concept):**  
$A^*$ is **optimally efficient** for any given consistent heuristic. This means that no other optimal algorithm is guaranteed to expand fewer nodes than $A^*$ (except for tie-breaking cases). 

*   *Justification:* Any algorithm that does not expand all nodes with $f(n) < C^*$ (where $C^*$ is the optimal path cost) runs the risk of missing the optimal solution. Since $A^*$ must expand every node with $f(n) < C^*$ to guarantee optimality, it expands the absolute minimal set of nodes necessary to verify that a path is indeed the optimal path.

---

### 🔥 [PYQ - 10 MARKS]
#### Q4. Give a comparative analysis of uninformed search strategies (BFS, DFS, UCS, DLS, IDS, Bidirectional) with respect to completeness, optimality, time complexity, and space complexity.

*Source: Compiled NMIMS D-24 [10 Marks] | MU, May 2013 [10 Marks] | MU, Dec 2014 [10 Marks]*

#### **Exam-Ready Answer:**

**1. Comparative Analysis Matrix:**  
The table below evaluates tree-search strategies using standard performance criteria, where:
*   $b$: Branching factor of the search tree.
*   $d$: Depth of the shallowest goal node.
*   $m$: Maximum depth of the state space (can be $\infty$).
*   $l$: User-defined depth limit.
*   $C^*$: Cost of the optimal solution.
*   $\epsilon$: Minimum positive step cost (each step cost must exceed $\epsilon > 0$).

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity | Search Direction |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **BFS** | **Yes** (if $b$ is finite) | **Yes** (if step costs are equal) | $O(b^d)$ | $O(b^d)$ (High) | Forward |
| **DFS** | **No** (fails in infinite paths) | **No** | $O(b^m)$ | $O(bm)$ (Low) | Forward |
| **UCS (Uniform Cost)**| **Yes** (if cost $\ge \epsilon$) | **Yes** (any step cost) | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | Forward (Priority) |
| **DLS (Depth-Limit)** | **No** (if $l < d$) | **No** | $O(b^l)$ | $O(bl)$ | Forward |
| **IDS (Iterative Deep)**| **Yes** (if $b$ is finite) | **Yes** (if step costs are equal) | $O(b^d)$ | $O(bd)$ (Low) | Forward (Iterative)|
| **Bidirectional** | **Yes** (if $b$ finite, reversible) | **Yes** (if step costs equal) | $O(b^{d/2})$ | $O(b^{d/2})$ | Forward & Backward |

**2. Key Technical Takeaways:**
1.  **Memory Bottleneck of BFS:** BFS stores all generated nodes in the frontier. This results in an exponential space complexity of $O(b^d)$. For example, at depth $d=10$ with branching factor $b=10$, BFS requires storing $10^{10}$ nodes, which easily exhausts standard computer memory.
2.  **Iterative Deepening Search (IDS) as the Optimal Choice:** IDS combines the completeness and optimality of BFS with the low memory footprint of DFS (storing only the active search path). It systematically runs Depth-Limited Search with increasing limits: $l = 0, 1, 2, \dots, d$. Although it regenerates nodes at upper levels, the overhead is mathematically negligible since the majority of nodes lie at the bottom level:
    $$\frac{N(IDS)}{N(BFS)} \approx \frac{b}{b-1}$$
3.  **UCS Optimality Criterion:** Uniform Cost Search is optimal because it expands nodes strictly in order of ascending path cost $g(n)$ using a priority queue. It is guaranteed to be complete only if the step cost of every action is bounded below by a small positive constant $\epsilon > 0$, which prevents infinite paths of infinitely decreasing costs (e.g., $1 + 1/2 + 1/4 + 1/8 \dots \rightarrow 2$).

---

### 🔥 [PYQ - 5 MARKS]
#### Q5. Write a short note on Hill Climbing search algorithm. Explain its core limitations (Local Maxima, Plateaus, Ridges) with the help of neat diagrams and suggest how to overcome them.

*Source: Compiled MU, Dec 2013 [5 Marks] | MDU BCA, 2015 / 2018 [10 Marks]*

#### **Exam-Ready Answer:**

**1. Concept of Hill Climbing:**  
Hill climbing is an uninformed, greedy local search algorithm that continuously moves in the direction of increasing value (elevation) to find the peak of a state-space landscape. It does not maintain a search tree or track past paths; it only stores the current state and its immediate neighbors. It is described as "climbing Mount Everest in thick fog with amnesia."

**2. Core Limitations (Anomalies):**

*   **A. Local Maxima (Foothills):**  
    A local maximum is a state that is higher than all of its immediate neighbors but is lower than the global maximum. Since any move from a local maximum leads to a lower elevation, the greedy algorithm terminates prematurely, returning a suboptimal solution.
    *   *Diagram representation:*
        ```text
               Local Peak (Terminates here!)
                 /\
                /  \
               /    \     Global Peak
              /      \       /\
             /        \     /  \
            /          \___/    \
        ```
*   **B. Plateaus (Flat Regions & Shoulders):**  
    A plateau is a flat area of the state-space landscape where all neighboring states have the exact same evaluation score. On a plateau, the algorithm cannot determine an uphill direction using local comparisons, causing it to wander aimlessly or get lost. 
    *   *Shoulder:* A flat region from which progress is possible.
    *   *Flat Local Maximum:* A flat region from which no uphill path exists.
    *   *Diagram representation:*
        ```text
                    Flat Plateau (Wanders / Gets Lost)
                   ┌─────────────┐
                  /              \
                 /                \
                /                  \
        ```
*   **C. Ridges (Diagonal Slopes):**  
    A ridge is a long, narrow strip of elevated land with steep slopes falling off on either side. The top of the ridge slope is oriented diagonally to the search actions (North, South, East, West). A simple, single-coordinate step in any cardinal direction results in a lower elevation, causing the algorithm to terminate on the ridge, even though a diagonal uphill path exists.
    *   *Diagram representation:*
        ```text
                     /\ (Ridge Line)
                    /  \
                   /    \  <-- Steep slopes on both sides.
                  /      \
        ```

---

**3. Solutions to Overcome Limitations:**
1.  **Backtracking:** Maintain a list of recently visited paths. If stuck at a local maximum, backtrack to a previous decision point and try an alternative branch.
2.  **Random-Restart Hill Climbing:** If the search gets stuck, randomly generate a completely new starting state and restart the search. This is highly effective; if the success probability of a single run is $p$, the probability of finding the global maximum after $k$ restarts is $1 - (1-p)^k$, which approaches $1$ as $k$ increases.
3.  **Sideways Moves:** Allow the algorithm to execute moves to neighboring states with the same evaluation score (for a limited number of steps, e.g., max 100 sideways steps) to escape shoulders.
4.  **Diagonal/Vector Steps:** Execute multiple actions or rules simultaneously before evaluating the state, allowing diagonal navigation up a ridge.

---

### ⭐ [PYQ - 10 MARKS]
#### Q6. Explain the Depth-First Search (DFS) algorithm with a neat example tracing node expansion and state storage.

*Source: Compiled MU, Dec 2012 [4 Marks] | MU, May 2016 [10 Marks]*

#### **Exam-Ready Answer:**

**1. DFS Algorithm Working Principle:**  
Depth-First Search is an uninformed search strategy that expands the deepest unexpanded node first. It is implemented using a Last-In-First-Out (LIFO) stack (or recursively). When a branch reaches a dead end, the algorithm backtracks to expand the next deepest sibling node.

**2. Trace Example on a Graph:**  
Let us trace DFS on the following directed graph. Start Node is $A$, and Goal Node is $G$. Alphabetical tie-breaking is applied.

```text
               (A)
              /   \
            (B)   (C)
           /   \     \
         (D)   (E)   (G) [Goal]
         /
       (F)
       /
     (H)
```

*   **Step 1:** Push Start Node $A$ onto the Stack.  
    *   Stack: $ [A] $. Explored: $ \emptyset $.
*   **Step 2:** Pop $A$. Expand $A$. Push successors $C$ and $B$ (such that $B$ is on top of the stack).  
    *   Stack: $ [B, C] $. Explored: $ \{A\} $.
*   **Step 3:** Pop $B$ (deepest). Expand $B$. Push successors $E$ and $D$ (such that $D$ is on top).  
    *   Stack: $ [D, E, C] $. Explored: $ \{A, B\} $.
*   **Step 4:** Pop $D$. Expand $D$. Push successor $F$.  
    *   Stack: $ [F, E, C] $. Explored: $ \{A, B, D\} $.
*   **Step 5:** Pop $F$. Expand $F$. Push successor $H$.  
    *   Stack: $ [H, E, C] $. Explored: $ \{A, B, D, F\} $.
*   **Step 6:** Pop $H$. Dead end (no successors). Backtrack.  
    *   Stack: $ [E, C] $. Explored: $ \{A, B, D, F, H\} $.
*   **Step 7:** Pop $E$. Dead end. Backtrack.  
    *   Stack: $ [C] $. Explored: $ \{A, B, D, F, H, E\} $.
*   **Step 8:** Pop $C$. Expand $C$. Push successor Goal $G$.  
    *   Stack: $ [G] $. Explored: $ \{A, B, D, F, H, E, C\} $.
*   **Step 9:** Pop $G$. Goal detected! Search terminates.

*   **Node Expansion Order:** $A \rightarrow B \rightarrow D \rightarrow F \rightarrow H \rightarrow E \rightarrow C \rightarrow G$.
*   **Inherent Limitation:** DFS found a very long path and did not explore the direct path $A \rightarrow C \rightarrow G$ because it blindly pursued the deep branch under $B$. DFS is **not optimal**.

---

### ⭐ [PYQ - 10 MARKS]
#### Q7. Explain the Breadth-First Search (BFS) algorithm with a neat example tracing node expansion.

*Source: Compiled MU, May 2014 [10 Marks]*

#### **Exam-Ready Answer:**

**1. BFS Algorithm Working Principle:**  
Breadth-First Search is an uninformed search strategy that expands the shallowest unexpanded node first, exploring the state space level-by-level. It is implemented using a First-In-First-Out (FIFO) queue. It guarantees finding the shortest path (optimal) if all edge costs are uniform.

**2. Trace Example on the same Graph:**  
Let us trace BFS on the graph used in Q6. Start Node is $A$, and Goal Node is $G$.

*   **Step 1:** Initialize FIFO Queue with Start Node $A$.  
    *   Queue: $ [A] $. Explored: $ \emptyset $.
*   **Step 2:** Dequeue $A$. Goal check fails. Expand $A$. Enqueue successors $B$ and $C$.  
    *   Queue: $ [B, C] $. Explored: $ \{A\} $.
*   **Step 3:** Dequeue $B$. Goal check fails. Expand $B$. Enqueue successors $D$ and $E$.  
    *   Queue: $ [C, D, E] $. Explored: $ \{A, B\} $.
*   **Step 4:** Dequeue $C$. Goal check fails. Expand $C$. Enqueue successor Goal $G$.  
    *   Queue: $ [D, E, G] $. Explored: $ \{A, B, C\} $.
*   **Step 5:** Dequeue $D$. Goal check fails. Expand $D$. Enqueue successor $F$.  
    *   Queue: $ [E, G, F] $. Explored: $ \{A, B, C, D\} $.
*   **Step 6:** Dequeue $E$. Dead end.  
    *   Queue: $ [G, F] $. Explored: $ \{A, B, C, D, E\} $.
*   **Step 7:** Dequeue $G$. Goal detected! Search terminates.

*   **Node Expansion Order:** $A \rightarrow B \rightarrow C \rightarrow D \rightarrow E \rightarrow G$.
*   **Selected Optimal Path:** $A \rightarrow C \rightarrow G$.
*   **Conclusion:** BFS successfully found the optimal, minimum-step path (length 2) compared to DFS which found a path of length 7.

---

## SECTION 4: HIGH-YIELD EXPECTED PRACTICE QUESTIONS

---

### ⭐ [EXPECTED - 5 MARKS]
#### Q8. Explain the concept of a Problem-Solving Agent. Describe the formal 5-component problem formulation framework with a real-world example.

#### **Answer:**

**1. Concept of a Problem-Solving Agent:**  
A problem-solving agent is a goal-based agent that uses mathematical models and search algorithms to plan sequences of actions that lead to a desirable goal state. It operates under a "Formulate, Search, Execute" paradigm:
1.  **Formulate Goal:** Define the target state-space criteria.
2.  **Formulate Problem:** Define the states and actions necessary to achieve the goal.
3.  **Search:** Run a search algorithm in a simulated environment to find an action sequence.
4.  **Execute:** Execute the action sequence in the physical world.

---

**2. The 5 Formal Components of Problem Formulation:**  
To formalize any problem as a search task, we must specify five components:

1.  **Initial State:** The state the agent starts in (e.g., in a navigation task: `At(Arad)`).
2.  **Actions:** The set of actions available to the agent at a given state $s$, denoted by $Actions(s)$ (e.g., `Go(Sibiu)`, `Go(Timisoara)`).
3.  **Transition Model:** A formal description of what each action does, represented as a function $Result(s, a)$ that returns the state reached by executing action $a$ in state $s$.
4.  **Goal Test:** A function that determines whether a given state is a goal state. This can be an explicit match (e.g., `s == At(Bucharest)`) or an abstract condition check.
5.  **Path Cost:** A function that assigns a numeric cost to a path. The step cost of executing action $a$ to transition from $s$ to $s'$ is denoted by $c(s, a, s')$.

---

**3. Example (8-Puzzle Problem Formulation):**
*   **Initial State:** A specific grid configuration of 8 numbered tiles and a blank space (e.g., $2, 8, 3 / 1, 6, 4 / 7, \_, 5$).
*   **Actions:** Move the blank space `Left`, `Right`, `Up`, or `Down`.
*   **Transition Model:** Swaps the coordinates of the blank space with the adjacent tile in the selected direction.
*   **Goal Test:** Checks if the current grid configuration matches the target goal state ($1, 2, 3 / 8, \_, 4 / 7, 6, 5$).
*   **Path Cost:** Each individual tile movement has a uniform cost of $1$. Total path cost is the total number of moves.

---

### ⭐ [EXPECTED - 5 MARKS]
#### Q9. Distinguish between Uninformed (Blind) Search and Informed (Heuristic) Search strategies. Provide a comprehensive comparison matrix.

#### **Answer:**

**1. Core Conceptual Distinctions:**
*   **Uninformed (Blind) Search:** The agent has no information about the state space other than the formal problem definition. It can only generate successor states, transition between states, and perform the goal test. It cannot estimate how close a non-goal state is to the target goal, resulting in systematic but blind exploration (e.g., BFS, DFS, UCS).
*   **Informed (Heuristic) Search:** The agent utilizes domain-specific knowledge represented as a **heuristic function** $h(n)$, which estimates the cost of the cheapest path from node $n$ to the goal. This guidance allows the search algorithm to selectively expand promising branches, reducing the number of nodes expanded (e.g., GBFS, $A^*$).

**2. Detailed Comparison Matrix:**

| Comparison Parameter | **Uninformed (Blind) Search** | **Informed (Heuristic) Search** |
| :--- | :--- | :--- |
| **Domain Knowledge** | Requires zero domain-specific knowledge; only uses the goal test and transition rules. | Employs domain-specific heuristics (e.g., straight-line distance, Manhattan distance). |
| **Search Guidance** | Explores states blindly in a fixed, structured order regardless of goal location. | Guides the search frontier actively towards the goal state. |
| **Search Efficiency** | **Low**: High number of node expansions; suffers from exponential state explosion. | **High**: Prunes unpromising branches early; fewer node expansions. |
| **Time/Space Complexity** | Strictly exponential: typically $O(b^d)$ or $O(b^m)$. | Sub-exponential or linear in the best case when the heuristic is highly accurate. |
| **Optimality** | Optimal only for uniform step costs (BFS) or simple cheapest-first priority (UCS). | Optimal for any step cost when the heuristic is admissible (for trees) or consistent (for graphs). |
| **Primary Examples** | BFS, DFS, Uniform Cost Search, Iterative Deepening. | Greedy Best-First Search, $A^*$ Search, SMA*. |

---

### ⭐ [EXPECTED - 5 MARKS]
#### Q10. Explain the structural differences between Tree Search and Graph Search. Why is Graph Search critical for preventing infinite loops in cyclic search spaces?

#### **Answer:**

**1. Core Structural Differences:**
*   **Tree Search:** Evaluates paths in the state space by systematically generating a **Search Tree** of paths from the root. It does not track whether a physical state has been visited before along a different branch, allowing the same physical state to be represented as multiple distinct nodes in the search tree.
*   **Graph Search:** Extends tree search by adding a **closed list** (also known as the **explored set**) that records all unique physical states that have already been expanded. Before expanding a node from the frontier (open list), the algorithm checks if its state is in the closed list; if so, it is discarded.

---

**2. Tabular Comparison:**

| Feature Parameter | **Tree Search** | **Graph Search** |
| :--- | :--- | :--- |
| **Frontier Tracking** | Maintains `OPEN` (frontier) queue. | Maintains both `OPEN` (frontier) and `CLOSED` (explored) sets. |
| **State Duplication** | Allows redundant paths and duplicate states across branches. | Strictly forbids duplicate state expansions. |
| **Memory Overhead** | **Low**: Only stores the frontier. | **High**: Must store every expanded state in RAM. |
| **Loop Vulnerability** | Highly vulnerable to infinite loops in cyclic graphs. | Immune to infinite loops in cyclic graphs. |

---

**3. Why Graph Search Prevents Infinite Loops (Vulnerability Analysis):**  
In many state spaces (e.g., the 8-puzzle or grid-world routing), actions are completely reversible. For example, moving a vacuum agent `Left` followed by `Right` returns it to the original state.
*   In a **Tree Search**, the algorithm will repeatedly expand these reversible states, creating an infinite, cyclic tree of redundant states, causing algorithms like DFS to enter infinite loops and fail.
*   In a **Graph Search**, once the initial state is expanded and added to the closed list, any attempt to return to it is detected during the closed list check. The duplicate node is discarded, breaking the cycle and guaranteeing termination in finite state spaces.

---

### ⭐ [EXPECTED - 5 MARKS]
#### Q11. Mathematically derive the worst-case time and space complexities of BFS, DFS, and Uniform Cost Search (UCS).

#### **Answer:**

**1. Breadth-First Search (BFS):**  
*   **Time Complexity Derivation:** Let $b$ be the branching factor and $d$ be the depth of the shallowest goal. At level 0, there is 1 node. At level 1, there are $b$ nodes. At level $d$, there are $b^d$ nodes. In the worst case, the goal is the last node checked at level $d$. The total number of nodes generated is:
    $$T(b, d) = 1 + b + b^2 + b^3 + \dots + b^d = O(b^d)$$
*   **Space Complexity Derivation:** BFS must store every generated node in memory to maintain the FIFO queue. Since the frontier at depth $d$ contains $b^d$ nodes, and the explored set contains $O(b^{d-1})$ nodes, the space complexity is dominated by the size of the frontier:
    $$S(b, d) = O(b^d)$$

---

**2. Depth-First Search (DFS):**  
*   **Time Complexity Derivation:** Let $m$ be the maximum depth of any path in the state space. In the worst case, DFS explores the entire search tree to its maximum depth $m$ before backtracking to find the goal at the bottom of the last branch. The worst-case time complexity is:
    $$T(b, m) = O(b^m)$$
    If $m$ is much larger than the goal depth $d$, DFS can be extremely slow.
*   **Space Complexity Derivation:** DFS only needs to store the single path currently being traversed, along with any unexpanded sibling nodes for each node on the path. For a tree with branching factor $b$ and maximum depth $m$, the stack contains at most $b$ nodes at each of the $m$ levels:
    $$S(b, m) = O(bm)$$
    This linear space requirement is the primary advantage of DFS over BFS.

---

**3. Uniform Cost Search (UCS):**  
*   **Complexity Derivation:** UCS expands nodes based on path cost rather than depth. Let $C^*$ be the cost of the optimal solution. We assume that every individual action costs at least $\epsilon > 0$.
    *   The maximum number of steps along any optimal path is bounded by $\lfloor C^* / \epsilon \rfloor$.
    *   Therefore, the worst-case depth at which the search operates is $1 + \lfloor C^* / \epsilon \rfloor$.
    *   The worst-case time and space complexities are determined by the number of nodes within this cost boundary:
        $$T(UCS) = S(UCS) = O\!\left(b^{1 + \lfloor C^*/\epsilon \rfloor}\right)$$
    *   *Significance:* If all step costs are equal ($c = 1$), then $\epsilon = 1$ and $C^* = d$, reducing the complexity to the standard BFS complexity: $O(b^{d})$.

---

### 🟡 [EXPECTED - 5 MARKS]
#### Q12. Prove that if an evaluation heuristic h(n) is consistent (monotone), it must also be admissible.

#### **Answer:**

**1. Mathematical Definitions:**
*   **Consistency (Monotonicity):** For any node $n$ and any successor $n'$ generated by action $a$:
    $$h(n) \le c(n, a, n') + h(n')$$
*   **Admissibility:** For any node $n$:
    $$h(n) \le h^*(n)$$
    where $h^*(n)$ is the true optimal cost to reach the goal $G$ from $n$, and $h(G) = 0$.

---

**2. Proof by Mathematical Induction:**  
Let $n = n_0, n_1, n_2, \dots, n_k = G$ be the sequence of nodes along the true optimal path from node $n$ to the goal $G$.
*   By the definition of consistency, for any adjacent pair of nodes $n_i$ and $n_{i+1}$ along this path:
    $$h(n_i) \le c(n_i, a_i, n_{i+1}) + h(n_{i+1})$$
    which can be rewritten as:
    $$h(n_i) - h(n_{i+1}) \le c(n_i, a_i, n_{i+1})$$

*   Let us sum this inequality along the entire optimal path from $i = 0$ to $k-1$:
    $$\sum_{i=0}^{k-1} [h(n_i) - h(n_{i+1})] \le \sum_{i=0}^{k-1} c(n_i, a_i, n_{i+1})$$

*   The left side of the summation is a telescoping series:
    $$\sum_{i=0}^{k-1} [h(n_i) - h(n_{i+1})] = [h(n_0) - h(n_1)] + [h(n_1) - h(n_2)] + \dots + [h(n_{k-1}) - h(n_k)] = h(n_0) - h(n_k)$$
    Since $n_0 = n$ and $n_k = G$, the series simplifies to:
    $$h(n) - h(G)$$

*   The right side of the summation is the sum of step costs along the optimal path, which by definition equals the true optimal path cost $h^*(n)$:
    $$\sum_{i=0}^{k-1} c(n_i, a_i, n_{i+1}) = h^*(n)$$

*   Substituting these back into our summed inequality:
    $$h(n) - h(G) \le h^*(n)$$

*   Since the heuristic at any goal node is zero ($h(G) = 0$):
    $$h(n) \le h^*(n)$$

---

**3. Conclusion:**  
This mathematically proves that any consistent heuristic is guaranteed to be admissible. *(Note: The converse is not always true; an admissible heuristic can be inconsistent).*

---

## SECTION 5: COMPREHENSIVE REVISION METRICS

### 5.1 Unit 2 Syllabus Coverage Audit

| Syllabus Topic | Status | Detailed Location | Verified Reference |
| :--- | :---: | :--- | :--- |
| **1. Problem Formulation** | ✅ Fully Covered | Section 4, Expected Q8 | *AIMA Chapter 3* |
| **2. Problem-Solving Agents** | ✅ Fully Covered | Section 4, Expected Q8 | *AIMA Chapter 3* |
| **3. Searching for Solutions** | ✅ Fully Covered | Section 4, Expected Q10 | *AIMA Chapter 3* |
| **4. Breadth-First Search (BFS)** | ✅ Fully Covered | Section 3, PYQ Q7 | *AIMA Chapter 3* |
| **5. Depth-First Search (DFS)** | ✅ Fully Covered | Section 3, PYQ Q6 | *AIMA Chapter 3* |
| **6. Uniform Cost Search (UCS)** | ✅ Fully Covered | Section 3, PYQ Q4, Section 4 Q11 | *AIMA Chapter 3* |
| **7. Heuristic Functions** | ✅ Fully Covered | Section 3, PYQ Q2, Q3 | *AIMA Chapter 3* |
| **8. Greedy Best-First Search** | ✅ Fully Covered | Section 3, PYQ Q1, Q2 | *AIMA Chapter 3* |
| **9. A* Search** | ✅ Fully Covered | Section 3, PYQ Q1, Q3 | *AIMA Chapter 3* |
| **10. Hill Climbing Search** | ✅ Fully Covered | Section 3, PYQ Q5 | *AIMA Chapter 4* |
| **11. Local Maxima drawback** | ✅ Fully Covered | Section 3, PYQ Q5 | *AIMA Chapter 4* |
| **12. Plateaus drawback** | ✅ Fully Covered | Section 3, PYQ Q5 | *AIMA Chapter 4* |
| **13. Ridges drawback** | ✅ Fully Covered | Section 3, PYQ Q5 | *AIMA Chapter 4* |

---

### 5.2 Out-of-Syllabus Exclusion Checklist

*   [x] **Genetic Algorithms (GA):** Completely excluded. No mentions of populations, selection, crossover, or mutation.
*   [x] **Adversarial Search / Game Playing:** Completely excluded. No mentions of Minimax, Alpha-Beta Pruning, or game-playing agents.

---

### 5.3 Answer-Availability Checklist

*   [x] Q1 Model Answer (Trace Graph for GBFS and A*)
*   [x] Q2 Model Answer (Solve 8-puzzle using BFS with misplaced tiles)
*   [x] Q3 Model Answer (Criteria for Admissibility and Consistency)
*   [x] Q4 Model Answer (Comparative Analysis Table of Uninformed Strategies)
*   [x] Q5 Model Answer (Hill Climbing Drawbacks and Solutions)
*   [x] Q6 Model Answer (DFS Trace on Directed Graph)
*   [x] Q7 Model Answer (BFS Trace on Directed Graph)
*   [x] Q8 Model Answer (Concept of Problem-Solving Agent & 5 Formulation Components)
*   [x] Q9 Model Answer (Blind Search vs Heuristic Search Comparison)
*   [x] Q10 Model Answer (Tree Search vs Graph Search Comparison)
*   [x] Q11 Model Answer (Complexities Derivation)
*   [x] Q12 Model Answer (Proof of Consistency implying Admissibility)

---

### 5.4 Correction Log

*   **UCS Complexity Formulation:** Bounded space complexity using step-cost lower bounds: $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$.
*   **Admissibility Comment:** Corrected heuristic analysis at node $D$ to show that $h(D) = 2 > h^*(D) = 1$ constitutes an overestimation, rendering the heuristic inadmissible.
*   **8-Puzzle Goal Alignment:** Checked and mapped the exact misplaced tiles (excluding blank) at each step to align with the goal state.

---

### 5.5 Prioritized Last-Minute Revision Plan
1.  **Phase 1 (Heuristic Traces):** Re-draw the step-by-step $A^*$ trace tree in Q1. Ensure you show how the path cost $g(n)$ updates dynamically.
2.  **Phase 2 (Drawbacks of Local Search):** Sketch the Local Maxima, Plateau, and Ridge hills. Memorize the 4 methods to resolve them (backtracking, random-restarts, sideways moves, multiple simultaneous rules).
3.  **Phase 3 (Theory Proofs):** Re-write the consistent-implies-admissible algebraic telescoping series induction in Q12.

---
*End of Question Bank. Download this file directly from your Studio panel for last-minute exam revision!*
