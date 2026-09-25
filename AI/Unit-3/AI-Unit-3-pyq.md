# ARTIFICIAL INTELLIGENCE (AI) — UNIT 3: KNOWLEDGE REPRESENTATION & REASONING

## PAST YEAR QUESTION (PYQ) & EXAM-ORIENTED MASTER STUDY BANK

### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## DOCUMENT OVERVIEW & EXAM BLUEPRINT

This document is a comprehensive, exam-oriented Past Year Question (PYQ) study bank for **Artificial Intelligence (AI) — Unit 3: Knowledge Representation & Reasoning**. This file retains the question wording, year, exam, and mark labels supplied in the original draft. **Provenance warning:** The underlying Unit 3 question papers were not supplied for cross-checking, so the labels, recurrence claims, and mark allocations below are **unverified**, not confirmed official PYQs. Verify each against its paper before citing it as an exam question; the worked examples remain useful for practice.

### Unit 3 Topic Weightage & Question Frequency Matrix

> The weightage and priority estimates below are carried over from the original draft; they have not been independently verified from question papers or an official exam blueprint.

| Syllabus Sub-Topic | Typical Question Types | Exam Weightage | Priority Level |
| :--- | :--- | :---: | :---: |
| **1. Propositional Logic (PL)** | Truth Tables, Tautology vs Contradiction, Wumpus World PEAS & Rules | 5 – 10 Marks | 🔥 High |
| **2. First-Order Logic (FOL)** | English-to-FOL Translations, Quantifier Scope ($\forall, \exists$) | 5 – 10 Marks | 🔥 High |
| **3. CNF Conversion** | Ordered 7-Step Conversion of FOL Formulas to Clausal Form | 5 – 10 Marks | 🔥 High |
| **4. Unification Algorithm** | Substitutions, MGU Computation, Failure Cases, Occurs Check | 4 – 5 Marks | ⚡ Medium |
| **5. Inference (FC, BC, Resolution)**| Forward Chaining, Backward Chaining, Resolution Proof Trees | 10 – 12 Marks | 🔥 Very High |

---

## SECTION 1: TOPIC-WISE PAST YEAR QUESTIONS & MASTER MODEL ANSWERS

---

### TOPIC 1: PROPOSITIONAL LOGIC, TRUTH TABLES, & WUMPUS WORLD

#### 1.1 Grouped & Repeated PYQs
* **Question 1.1a (SVKM's NMIMS Re-Exam 2024-25, Q1.b):**  
  *"P, Q and R are logical propositions. Draw the Truth table and from that find out if anyone is Tautology (All True) and if anyone is Contradiction (All False).*  
  *Statement 1: $((P \vee Q) \wedge R) \iff ((P \wedge R) \vee (Q \wedge R))$*  
  *Statement 2: $(P \wedge (\neg Q \vee \neg R)) \implies (P \implies \neg Q)$"*  
  — **Source:** SVKM's NMIMS Re-Exam 2024-25, Q1.b [5 Marks]

* **Question 1.1b (SVKM's NMIMS Final Exam 2023-24, Q1.c):**  
  *"Determine whether the following argument is valid or not using propositional logic:*  
  *'If I work whole night on this problem, then I can solve it. If I solve the problem, then I will understand the topic. Therefore, if I work the whole night on this problem, then I will understand the topic.'"*  
  — **Source:** SVKM's NMIMS Final Exam 2023-24, Q1.c [5 Marks]

* **Question 1.1c (SVKM's NMIMS Final Exam 2022-23, Q6.B):**  
  *"Discuss Wumpus World problem with its PEAS properties in the context of Knowledge-Based Agents."*  
  — **Source:** SVKM's NMIMS Final Exam 2022-23, Q6.B [10 Marks] / R&N Chapter 7

---

#### Master Model Answer 1.1: Truth Table Analysis & Validity Proofs

##### 1. Statement 1 Analysis: Distributive Law Verification

```math
\text{Statement 1: } ((P \vee Q) \wedge R) \iff ((P \wedge R) \vee (Q \wedge R))
```
Let $L = (P \vee Q) \wedge R$ and $R_{hs} = (P \wedge R) \vee (Q \wedge R)$.

| $P$ | $Q$ | $R$ | $P \vee Q$ | $L = (P \vee Q) \wedge R$ | $P \wedge R$ | $Q \wedge R$ | $R_{hs} = (P \wedge R) \vee (Q \wedge R)$ | $L \iff R_{hs}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **T** | **T** | **T** | T | **T** | T | T | **T** | **T** |
| **T** | **T** | **F** | T | **F** | F | F | **F** | **T** |
| **T** | **F** | **T** | T | **T** | T | F | **T** | **T** |
| **T** | **F** | **F** | T | **F** | F | F | **F** | **T** |
| **F** | **T** | **T** | T | **T** | F | T | **T** | **T** |
| **F** | **T** | **F** | T | **F** | F | F | **F** | **T** |
| **F** | **F** | **T** | F | **F** | F | F | **F** | **T** |
| **F** | **F** | **F** | F | **F** | F | F | **F** | **T** |

* **Conclusion:** The final column $L \iff R_{hs}$ evaluates to **True (T) in all 8 rows**. Therefore, Statement 1 is a **TAUTOLOGY** (Valid). This confirms the Distributive Law of Conjunction over Disjunction.

---

##### 2. Statement 2 Analysis

```math
\text{Statement 2: } (P \wedge (\neg Q \vee \neg R)) \implies (P \implies \neg Q)
```
Let $A = P \wedge (\neg Q \vee \neg R)$ and $B = P \implies \neg Q$. We test $A \implies B$.

| $P$ | $Q$ | $R$ | $\neg Q$ | $\neg R$ | $\neg Q \vee \neg R$ | $A = P \wedge (\neg Q \vee \neg R)$ | $B = P \implies \neg Q$ | $A \implies B$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **T** | **T** | **T** | F | F | F | **F** | **F** | **T** |
| **T** | **T** | **F** | F | T | T | **T** | **F** | **F** |
| **T** | **F** | **T** | T | F | T | **T** | **T** | **T** |
| **T** | **F** | **F** | T | T | T | **T** | **T** | **T** |
| **F** | **T** | **T** | F | F | F | **F** | **T** | **T** |
| **F** | **T** | **F** | F | T | T | **F** | **T** | **T** |
| **F** | **F** | **T** | T | F | T | **F** | **T** | **T** |
| **F** | **F** | **F** | T | T | T | **F** | **T** | **T** |

* **Conclusion:** Line 2 evaluates to **False (F)** when $P=\text{T}, Q=\text{T}, R=\text{F}$. Because it contains both True and False values, Statement 2 is **NEITHER a Tautology NOR a Contradiction** (it is **Satisfiable but Not Valid**).

---

##### 3. Argument Validity Proof ("Work Whole Night")
Let the atomic propositions be:
* $P$: "I work the whole night on this problem."
* $Q$: "I can solve the problem."
* $R$: "I will understand the topic."

* **Premise 1:** $P \implies Q$
* **Premise 2:** $Q \implies R$
* **Conclusion:** $P \implies R$

The complete argument formula is: $[(P \implies Q) \wedge (Q \implies R)] \implies (P \implies R)$.

| $P$ | $Q$ | $R$ | $P \implies Q$ | $Q \implies R$ | Premises: $(P \implies Q) \wedge (Q \implies R)$ | Conclusion: $P \implies R$ | Complete Argument |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **T** | **T** | **T** | T | T | **T** | **T** | **T** |
| **T** | **T** | **F** | T | F | **F** | **F** | **T** |
| **T** | **F** | **T** | F | T | **F** | **T** | **T** |
| **T** | **F** | **F** | F | T | **F** | **F** | **T** |
| **F** | **T** | **T** | T | T | **T** | **T** | **T** |
| **F** | **T** | **F** | T | F | **F** | **T** | **T** |
| **F** | **F** | **T** | T | T | **T** | **T** | **T** |
| **F** | **F** | **F** | T | T | **T** | **T** | **T** |

* **Conclusion:** The argument is **VALID** because the implication evaluates to **True in all 8 rows** (Tautology). This logical pattern represents the classical inference rule **Hypothetical Syllogism**.

---

#### Master Model Answer 1.2: Wumpus World PEAS & Logical Formulation

##### 1. PEAS Description of Wumpus World
* **Performance Measure:**
  * $+1000$ points for escaping the cave with the Gold.
  * $-1000$ points for falling into a Pit or being eaten by the Wumpus.
  * $-1$ point per action taken.
  * $-10$ points for shooting the Arrow.
* **Environment:**
  * $4 \times 4$ grid of rooms surrounded by walls.
  * Agent starts at square $[1,1]$ facing East.
  * Locations of Gold and Wumpus are chosen randomly (uniform distribution, excluding $[1,1]$).
  * Each square (other than $[1,1]$) has a $0.2$ probability of containing a Pit.
* **Actuators:**
  * `TurnLeft`, `TurnRight`, `Forward`, `Grab` (gold), `Shoot` (arrow in facing direction), `Climb` (out of cave at $[1,1]$).
* **Sensors:**
  * Percepts represented as a 5-element tuple `[Stench, Breeze, Glitter, Bump, Scream]`:
    * `Stench`: Detected in squares directly adjacent (horizontally or vertically) to the Wumpus.
    * `Breeze`: Detected in squares directly adjacent to a Pit.
    * `Glitter`: Detected in the exact square containing the Gold.
    * `Bump`: Detected when walking into a wall.
    * `Scream`: Detected anywhere in the cave when the Wumpus is killed by an arrow.

```text
  +-------+-------+-------+-------+
4 |       |       |       |       |
  +-------+-------+-------+-------+
3 | Wumpus|       | Pits  |       |
  +-------+-------+-------+-------+
2 | Stench|       | Breeze|       |
  +-------+-------+-------+-------+
1 | Agent | Breeze| Pit   |       |
  | [1,1] | [2,1] | [3,1] |       |
  +-------+-------+-------+-------+
      1       2       3       4
```

##### 2. Propositional Rules for Wumpus World
Let $P_{i,j}$ be True if square $[i,j]$ contains a Pit, $B_{i,j}$ be True if square $[i,j]$ has a Breeze, $W_{i,j}$ be True if square $[i,j]$ contains a Wumpus, and $S_{i,j}$ be True if square $[i,j]$ has a Stench.

1. **Initial Safe Knowledge:**
   * $R_1: \neg P_{1,1}$ (No Pit in $[1,1]$)
   * $R_2: \neg W_{1,1}$ (No Wumpus in $[1,1]$)
2. **Breeze and Pit Relationships (Biconditionals):**
   * A square is breezy if and only if a neighboring square contains a pit:
   * $R_3: B_{1,1} \iff (P_{1,2} \vee P_{2,1})$
   * $R_4: B_{2,1} \iff (P_{1,1} \vee P_{2,2} \vee P_{3,1})$
3. **Stench and Wumpus Relationships:**
   * $R_5: S_{1,1} \iff (W_{1,2} \vee W_{2,1})$
   * $R_6: S_{2,1} \iff (W_{1,1} \vee W_{2,2} \vee W_{3,1})$

---

### TOPIC 2: FIRST-ORDER LOGIC (FOL) & TRANSLATIONS

#### 2.1 Grouped & Repeated PYQs
* **Question 2.1a (SVKM's NMIMS Re-Exam 2022-23, Q1.b):**  
  *"Convert the following English sentences into First-Order Logic (FOL):*  
  *1) There is a student who is loved by every other student.*  
  *2) Every student takes at least one course.*  
  *3) Bill takes either Analysis or Geometry (but not both).*  
  *4) Every student who takes Analysis also takes Geometry.*  
  *5) Anything which has a red nose is weird or is a clown."*  
  — **Source:** SVKM's NMIMS Re-Exam 2022-23, Q1.b [5 Marks]

* **Question 2.1b (Mumbai University Dec 2015):**  
  *"Represent the following in First-Order Predicate Logic (FOPL):*  
  *1) Anyone who kills an animal is loved by no one.*  
  *2) A square is breezy if there is a pit in the neighbouring squares."*  
  — **Source:** Mumbai University (MU) Dec 2015 [5 Marks]

---

#### Master Model Answer 2.1: Formal FOL Translations

##### 1. Predicate Definitions
* $\text{Student}(x)$: $x$ is a student.
* $\text{Loves}(x, y)$: $x$ loves $y$.
* $\text{Course}(x)$: $x$ is a course.
* $\text{Takes}(x, y)$: $x$ takes course $y$.
* $\text{RedNose}(x)$: $x$ has a red nose.
* $\text{Weird}(x)$: $x$ is weird.
* $\text{Clown}(x)$: $x$ is a clown.
* $\text{Kills}(x, y)$: $x$ kills $y$.
* $\text{Animal}(x)$: $x$ is an animal.
* $\text{Pit}(x)$: Square $x$ contains a pit.
* $\text{Breezy}(x)$: Square $x$ is breezy.
* $\text{Adjacent}(x, y)$: Square $x$ is adjacent to square $y$.

---

##### 2. Step-by-Step FOL Expressions
1. **"There is a student who is loved by every other student."**
   * **FOL:** $\exists x (\text{Student}(x) \wedge \forall y ((\text{Student}(y) \wedge y \neq x) \implies \text{Loves}(y, x)))$
   * *Explanation:* $\exists x$ anchors the specific student loved by all distinct student peers $y$.

2. **"Every student takes at least one course."**
   * **FOL:** $\forall x (\text{Student}(x) \implies \exists y (\text{Course}(y) \wedge \text{Takes}(x, y)))$
   * *Explanation:* Universal quantifier $\forall x$ maps to existential quantifier $\exists y$ using implication $\implies$.

3. **"Bill takes either Analysis or Geometry (but not both)."**
   * **FOL:** $(\text{Takes}(\text{Bill}, \text{Analysis}) \vee \text{Takes}(\text{Bill}, \text{Geometry})) \wedge \neg(\text{Takes}(\text{Bill}, \text{Analysis}) \wedge \text{Takes}(\text{Bill}, \text{Geometry}))$
   * *Alternative (XOR):* $\text{Takes}(\text{Bill}, \text{Analysis}) \oplus \text{Takes}(\text{Bill}, \text{Geometry})$

4. **"Every student who takes Analysis also takes Geometry."**
   * **FOL:** $\forall x ((\text{Student}(x) \wedge \text{Takes}(x, \text{Analysis})) \implies \text{Takes}(x, \text{Geometry}))$

5. **"Anything which has a red nose is weird or is a clown."**
   * **FOL:** $\forall x (\text{RedNose}(x) \implies (\text{Weird}(x) \vee \text{Clown}(x)))$

6. **"Anyone who kills an animal is loved by no one."**
   * **FOL:** $\forall x \forall y ((\exists z (\text{Animal}(z) \wedge \text{Kills}(x, z))) \implies \neg \text{Loves}(y, x))$
   * *Equivalent Form:* $\neg \exists x \exists y \exists z (\text{Animal}(z) \wedge \text{Kills}(x, z) \wedge \text{Loves}(y, x))$

7. **"A square is breezy if there is a pit in the neighbouring squares."**
   * **FOL:** $\forall s ((\exists n (\text{Adjacent}(n, s) \wedge \text{Pit}(n))) \implies \text{Breezy}(s))$

---

### TOPIC 3: CNF CONVERSION PROCEDURE & WORKED EXAMPLES

#### 3.1 Grouped & Repeated PYQs
* **Question 3.1a (Mumbai University May 2016 / May 2018 / May 2023):**  
  *"Explain the step-by-step procedure involved in converting a First-Order Logic (FOL) statement into Conjunctive Normal Form (CNF) with a suitable example."*  
  — **Source:** MU May 16 [10 Marks], May 18 [10 Marks], May 23 [10 Marks]

---

#### Master Model Answer 3.1: Canonical 7-Step CNF Conversion Procedure
A formula is in **Conjunctive Normal Form (CNF)** if it is a conjunction ($\wedge$) of clauses, where each clause is a disjunction ($\vee$) of literals.

```text
  [ FOL Formula ]
         │
         ▼ 1. Eliminate Biconditionals (⇔) and Implications (⇒)
  [ Implication-Free Formula ]
         │
         ▼ 2. Move Negations (¬) Inward (De Morgan's & Quantifier Duality)
  [ Negation Normal Form (NNF) ]
         │
         ▼ 3. Standardize Variables (Rename bound variables)
  [ Standardized Formula ]
         │
         ▼ 4. Skolemization (Replace ∃ with Skolem Constants / Functions)
  [ Skolemized Formula ] (Equisatisfiable!)
         │
         ▼ 5. Drop Universal Quantifiers (∀)
  [ Prenex Outer Form ]
         │
         ▼ 6. Distribute Disjunctions (∨) over Conjunctions (∧)
  [ CNF Formula (Conjunction of Clauses) ]
         │
         ▼ 7. Isolate Clauses into Knowledge Base
  [ Final Clause Set {C1, C2, ..., Cn} ]
```

##### The 7 Ordered Steps:
1. **Eliminate Implications ($\implies$) and Biconditionals ($\iff$):**
   * $A \iff B \equiv (A \implies B) \wedge (B \implies A)$
   * $A \implies B \equiv \neg A \vee B$
2. **Move Negations ($\neg$) Inward (Negation Normal Form):**
   * $\neg(\neg A) \equiv A$
   * $\neg(A \wedge B) \equiv \neg A \vee \neg B$ (De Morgan's)
   * $\neg(A \vee B) \equiv \neg A \wedge \neg B$ (De Morgan's)
   * $\neg \forall x P(x) \equiv \exists x \neg P(x)$
   * $\neg \exists x P(x) \equiv \forall x \neg P(x)$
3. **Standardize Variables:**
   * Rename duplicate variable names so each quantifier binds a unique variable symbol:
   * $(\forall x P(x)) \vee (\exists x Q(x)) \longrightarrow (\forall x P(x)) \vee (\exists y Q(y))$
4. **Skolemization (Eliminate Existential Quantifiers $\exists$):**
   * Replace existentially quantified variables with **Skolem Constants** (if outside the scope of any $\forall$) or **Skolem Functions** (if inside the scope of universal quantifiers $\forall$).
   * *Equisatisfiability:* Skolemization preserves satisfiability, but not strict logical equivalence.
5. **Drop Universal Quantifiers ($\forall$):**
   * All remaining variables are implicitly universally quantified. Remove explicit $\forall$ symbols.
6. **Distribute Disjunction ($\vee$) over Conjunction ($\wedge$):**
   * $A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)$
7. **Isolate Clauses:**
   * Break the conjunction into independent clauses separated by commas.

---

##### Fully Worked Complex Conversion Example
**Statement:** *"Everyone who loves all animals is loved by someone."*

```math
\text{FOL: } \forall x (\forall y (\text{Animal}(y) \implies \text{Loves}(x, y)) \implies \exists z \text{Loves}(z, x))
```
* **Step 1: Eliminate Implications ($\implies$)**
  * Inner implication: $\text{Animal}(y) \implies \text{Loves}(x, y) \equiv \neg \text{Animal}(y) \vee \text{Loves}(x, y)$
  * Outer implication: $\neg (\forall y (\neg \text{Animal}(y) \vee \text{Loves}(x, y))) \vee \exists z \text{Loves}(z, x)$
* **Step 2: Move Negations Inward**
  * $\forall y \longrightarrow \exists y$ and negate disjunction:
  * $\exists y \neg(\neg \text{Animal}(y) \vee \text{Loves}(x, y)) \vee \exists z \text{Loves}(z, x)$
  * $\exists y (\text{Animal}(y) \wedge \neg \text{Loves}(x, y)) \vee \exists z \text{Loves}(z, x)$
  * Pull quantifiers outward: $\forall x \exists y \exists z ((\text{Animal}(y) \wedge \neg \text{Loves}(x, y)) \vee \text{Loves}(z, x))$
* **Step 3: Standardize Variables**
  * Variables $x, y, z$ are already distinct.
* **Step 4: Skolemization**
  * Both $\exists y$ and $\exists z$ fall within the scope of universal quantifier $\forall x$.
  * Replace $y$ with Skolem function $f(x)$ and $z$ with Skolem function $g(x)$:
  * $\forall x ((\text{Animal}(f(x)) \wedge \neg \text{Loves}(x, f(x))) \vee \text{Loves}(g(x), x))$
* **Step 5: Drop Universal Quantifiers**
  * $(\text{Animal}(f(x)) \wedge \neg \text{Loves}(x, f(x))) \vee \text{Loves}(g(x), x)$
* **Step 6: Distribute $\vee$ over $\wedge$**
  * Apply $(A \wedge B) \vee C \equiv (A \vee C) \wedge (B \vee C)$:
  * Clause 1: $\text{Animal}(f(x)) \vee \text{Loves}(g(x), x)$
  * Clause 2: $\neg \text{Loves}(x, f(x)) \vee \text{Loves}(g(x), x)$
* **Step 7: Final CNF Clause Set**
  * $C_1 = \{\text{Animal}(f(x)) \vee \text{Loves}(g(x), x)\}$
  * $C_2 = \{\neg \text{Loves}(x, f(x)) \vee \text{Loves}(g(x), x)\}$

---

### TOPIC 4: UNIFICATION ALGORITHM, MGU, & OCCURS CHECK

#### 4.1 Grouped & Repeated PYQs
* **Question 4.1a (SVKM's NMIMS Final Exam 2022-23, Q7.C):**  
  *"Write a short note on Unification Algorithm."*  
  — **Source:** SVKM's NMIMS Final Exam 2022-23, Q7.C [4 Marks]

* **Question 4.1b (Mumbai University / GTU Question Bank):**  
  *"What is Unification? Find the Most General Unifier (MGU) for the expressions $P(x, g(f(a)), x)$ and $P(f(y), z, g(y))$."* **As written in the draft; these terms have no MGU. The appropriate answer is that unification fails, not an invented substitution. Check the original question paper for possible transcription errors.**  
  — **Source:** MU / Technical Question Bank [5 Marks]

---

#### Master Model Answer 4.1: Unification & Substitution Theory

##### 1. Definition & Purpose
**Unification** is an algorithmic process that takes two logical expressions containing variables and computes a **substitution matrix $\theta$** that makes the two expressions syntactically identical.
* **Substitution ($\theta$):** A set of bindings $\{v_1 / t_1, v_2 / t_2, \dots, v_n / t_n\}$ where variable $v_i$ is replaced by term $t_i$.
* **Most General Unifier (MGU):** The simplest substitution $\theta$ that unifies two expressions without making unnecessary variable assignments.

---

##### 2. The Occurs Check
The **Occurs Check** prevents a variable $x$ from being unified with a complex term $f(x)$ containing $x$ itself (e.g., unifying $x$ with $S(x)$). 
* Without the occurs check, the algorithm creates an infinite cyclic structure $x = S(S(S(\dots)))$, causing unsound logical inferences.

---

##### 3. Unification Algorithm (exam-ready pseudocode)

```text
UNIFY(s, t, theta = {})
    apply theta to both s and t
    if s and t are identical: return theta
    if s is a variable:
        if s occurs in t: return FAIL
        return COMPOSE({s -> t}, theta)
    if t is a variable:
        if t occurs in s: return FAIL
        return COMPOSE({t -> s}, theta)
    if s and t have different function/predicate symbols or arities: return FAIL
    for each corresponding argument pair (si, ti), from left to right:
        theta = UNIFY(si, ti, theta)
        if theta is FAIL: return FAIL
    return theta
```

Here `COMPOSE` applies the new binding to earlier bindings so the resulting substitution remains consistent; the occurs check rejects cyclic terms. The first example below demonstrates a structural failure rather than a successful MGU.

##### 3. Step-by-Step MGU Problem Solving
**Given Terms:**

```math
E_1 = P(x, g(f(a)), x), \quad E_2 = P(f(y), z, g(y))
```

| Step | Argument Pair | Current Substitution $\theta$ | Action / Result | Updated Terms |
| :---: | :---: | :---: | :--- | :--- |
| **0** | $E_1, E_2$ | $\emptyset$ | Compare predicates: Both are $P$ (Match). | — |
| **1** | $x, f(y)$ | $\{x / f(y)\}$ | Bind variable $x$ to term $f(y)$ (Occurs check passes: $x \notin f(y)$). | $E_1' = P(f(y), g(f(a)), f(y))$<br>$E_2' = P(f(y), z, g(y))$ |
| **2** | $g(f(a)), z$ | $\{x / f(y), z / g(f(a))\}$ | Bind variable $z$ to term $g(f(a))$. | $E_1'' = P(f(y), g(f(a)), f(y))$<br>$E_2'' = P(f(y), g(f(a)), g(y))$ |
| **3** | $f(y), g(y)$ | **FAIL** | Compare functors: $f$ vs. $g$ **Clash!** Function symbols do not match. | **UNIFICATION FAILS** |

* **Final Result:** Unification **FAILS** because $f(y)$ and $g(y)$ have conflicting function heads. Hence **no MGU exists for these exact expressions**; do not fabricate one. A successful contrasting example is $P(x,a)$ and $P(b,y)$, with MGU $\{x\mapsto b,\ y\mapsto a\}$.

---

### TOPIC 5: FOL INFERENCE: FORWARD CHAINING, BACKWARD CHAINING, & RESOLUTION

#### 5.1 Grouped & Repeated PYQs
* **Question 5.1a (SVKM's NMIMS Final Exam 2022-23, Q3.B / Final Exam 2024-25 / MU Dec 12, May 14, Dec 19):**  
  *"As per the law, it is a crime for an American to sell weapons to hostile nations. Country A (Nono), an enemy of America, has some missiles, and all of its missiles were sold to it by Colonel West, who is an American."*  
  *(i) Translate sentences into FOL.*  
  *(ii) Convert FOL sentences into CNF clauses.*  
  *(iii) Prove that Colonel West is a Criminal using Resolution Refutation and Forward Chaining.*  
  — **Source:** SVKM's NMIMS Final Exam 2022-23, Q3.B [10 Marks] / Re-Exam 2024-25 [10 Marks]

* **Question 5.1b (SVKM's NMIMS Final Exam 2022-23 Q1.b / Final Exam 2025-26 Q1.b):**  
  *"Differentiate between Forward Chaining and Backward Chaining with suitable examples."*  
  — **Source:** SVKM's NMIMS Final Exam 2022-23 [5 Marks], 2025-26 [5 Marks]

* **Question 5.1c (Mumbai University Dec 2015):**  
  *"Consider facts: 1) Rimi is hungry. 2) If Rimi is hungry she barks. 3) If Rimi is barking then Raja is angry. Prove that Raja is angry using resolution."*  
  — **Source:** MU Dec 2015 [10 Marks]

* **Question 5.1d (Mumbai University Dec 2015):**  
  *"Consider axioms: All people who are graduating are happy. All happy people smile. Someone is graduating. Prove that someone is smiling using resolution technique."*  
  — **Source:** MU Dec 2015 [12 Marks]

---

#### Master Model Answer 5.1: Forward Chaining vs. Backward Chaining Comparison

| Feature / Dimension | Forward Chaining (Data-Driven) | Backward Chaining (Goal-Driven) |
| :--- | :--- | :--- |
| **Direction of Search** | Starts from known initial facts $\longrightarrow$ moves forward to derive goals. | Starts from goal query $\longrightarrow$ moves backward to find supporting facts. |
| **Search Strategy** | Often iterates over known facts and applicable rules; not inherently BFS. | Often explores goal/subgoals depth-first; strategy depends on implementation. |
| **Matching Technique** | Left-Hand Side (IF-part / Premise) matching. | Right-Hand Side (THEN-part / Conclusion) matching. |
| **Application Domain** | Planning, monitoring, control systems, data synthesis. | Medical diagnosis, system troubleshooting, PROLOG interpreters. |
| **Efficiency** | Can generate irrelevant conclusions if KB is large. | Highly targeted; only explores rules relevant to proving the goal. |

**Suitable example for both methods (same facts and rules):**

- Facts: `Hungry(Rimi)`. Rules: `Hungry(Rimi) => Barks(Rimi)` and `Barks(Rimi) => Angry(Raja)`. Query: `Angry(Raja)`.
- **Forward chaining:** Start with `Hungry(Rimi)`; apply the first rule to add `Barks(Rimi)`; apply the second to add `Angry(Raja)`. The query is established.
- **Backward chaining:** Start with goal `Angry(Raja)`; the second rule makes `Barks(Rimi)` a subgoal; the first rule makes `Hungry(Rimi)` a subgoal; the known fact satisfies it, so both earlier goals follow.
- These are two directions of reasoning over the **same** knowledge base, not two different proofs of unrelated claims.

---

## SECTION 2: MOST IMPORTANT / RECURRENT PYQ CONCEPTS

> The concepts are important for revision; the recurrence and source-year claims in this section require verification against the original papers.

1. **Resolution Refutation Proofs (10 – 12 Marks):**
   * Constructing resolution trees down to the empty clause ($\square$ / $\text{NIL}$) by assuming the negated query $\neg \text{Goal}$.
   * *Primary Exam Domains:* American Weapon Crime (Colonel West), Rimi Hungry / Raja Angry, Graduating Happy People, and Marcus Caesar.
2. **FOL-to-CNF Conversion Rules (10 Marks):**
   * Systematic application of the 7-step conversion, especially **Skolemization** (distinguishing Skolem constants vs. Skolem functions) and **distributing $\vee$ over $\wedge$**.
3. **English-to-FOL Sentence Translation (5 – 10 Marks):**
   * Correct quantifier usage ($\forall$ with $\implies$, $\exists$ with $\wedge$). Avoid mixing $\forall$ with $\wedge$.
4. **Truth Table Validity & Tautology Checks (5 Marks):**
   * Evaluating $2^n$-row truth tables for equivalence ($\iff$), implication ($\implies$), and identifying tautologies vs. contradictions.
5. **Forward Chaining vs. Backward Chaining (5 Marks):**
   * Tabular differences, AND-OR search trees, data-driven vs. goal-driven execution.

---

## SECTION 3: REPEATED PYQ MATCHING MATRIX

> These source-year matches are retained from the draft, **not verified**. Do not treat this matrix as proof that a question appeared in a listed exam.

| Question Theme | Matched Exam Years & Papers | Master Answer Location |
| :--- | :--- | :--- |
| **American Weapon Crime (Colonel West)** | NMIMS Final Exam 2022-23 (Q3.B)<br>NMIMS Final Exam 2024-25 (Q3)<br>MU Dec 2012, May 2014, Dec 2019 | **Section 7: Solved PYQ 1** |
| **Rimi Hungry / Raja Angry Resolution** | MU Dec 2015 (Ex 3.11.4)<br>AI&SC TechKnowledge Question Bank | **Section 7: Solved PYQ 2** |
| **Graduating Happy Smiling People** | MU Dec 2015 (Ex 3.11.6) | **Section 7: Solved PYQ 3** |
| **Truth Tables & Tautology Check** | NMIMS Re-Exam 2024-25 (Q1.b) | **Section 1: Master Answer 1.1** |
| **Wumpus World PEAS & Logical Rules** | NMIMS Final Exam 2022-23 (Q6.B) | **Section 1: Master Answer 1.2** |
| **Forward vs Backward Chaining** | NMIMS Final Exam 2022-23 (Q1.b)<br>NMIMS Final Exam 2025-26 (Q1.b)<br>MU Dec 2012, May 2014 | **Section 1: Master Answer 5.1** |
| **English to FOL Translations** | NMIMS Re-Exam 2022-23 (Q1.b)<br>MU Dec 2015 (Ex 3.10.2) | **Section 1: Master Answer 2.1** |

---

## SECTION 4: IMPORTANT LOGIC & FOL QUESTIONS

### Q4.1: Explain the Architecture of a Knowledge-Based Agent
* **Answer:**  
  A Knowledge-Based (KB) agent consists of two core components:
  1. **Knowledge Base (KB):** A set of sentences expressed in a formal representation language representing facts about the world.
  2. **Inference Engine:** Domain-independent algorithms that derive new sentences from existing ones via entailment ($\text{KB} \models \alpha$).

```text
                +---------------------------+
  Percepts ---> |   Knowledge-Based Agent   | ---> Actions
                |                           |
                |  +---------------------+  |
                |  |   Inference Engine  |  |
                |  +----------+----------+  |
                |             | TELL/ASK    |
                |  +----------v----------+  |
                |  |    Knowledge Base   |  |
                |  |        (KB)         |  |
                |  +---------------------+  |
                +---------------------------+
```

* **Core Interface Operations:**
  * $\text{TELL}(\text{KB}, \text{sentence})$: Adds new information to the KB.
  * $\text{ASK}(\text{KB}, \text{query})$: Queries the KB to check if a sentence is entailed by the current KB.

---

## SECTION 5: IMPORTANT CNF & UNIFICATION QUESTIONS

### Q5.1: Differentiate between Logical Equivalence and Equisatisfiability in Skolemization
* **Answer:**
  * **Logical Equivalence ($\equiv$):** Two formulas $A$ and $B$ have identical truth values in *every possible model*. Example: $P \implies Q \equiv \neg P \vee Q$.
  * **Equisatisfiability ($\sim_{sat}$):** Two formulas $A$ and $B$ are equisatisfiable if $A$ is satisfiable if and only if $B$ is satisfiable (though their models may differ).
  * *Context in Skolemization:* Replacing $\exists x P(x)$ with $P(A)$ introduces a new constant symbol $A$. The resulting formula is **equisatisfiable**, not strictly logically equivalent, because the truth value depends on the interpretation of $A$.

---

## SECTION 6: IMPORTANT INFERENCE QUESTIONS

### Q6.1: Explain the Soundness and Completeness of Resolution Refutation
* **Answer:**
  * **Soundness:** A proof system is sound if every sentence derived using the inference rules is logically entailed by the KB ($\text{KB} \vdash \alpha \implies \text{KB} \models \alpha$). Resolution is strictly sound.
  * **Completeness:** A proof system is complete if it can derive any sentence that is entailed by the KB ($\text{KB} \models \alpha \implies \text{KB} \vdash \alpha$).
  * **Refutation Completeness:** Propositional and First-Order Resolution refutation is **Refutation Complete**. While resolution cannot generate all entailed sentences directly, it is guaranteed to derive an empty clause ($\square$) from $\text{KB} \wedge \neg \alpha$ if $\text{KB} \models \alpha$.

---

## SECTION 7: SOLVED PAST YEAR PROBLEMS (DETAILED STEP-BY-STEP PROOFS)

> The proof exercises and their exam labels are preserved from the draft. Their logical solutions are checked here, but the exact PYQ provenance remains unverified without the original papers.

---

### ✍️ SOLVED PYQ 1: "Is Colonel West a Criminal?" (American Weapon Crime)
*(Source: SVKM's NMIMS B.Tech CE Final Exam 2022-23 Q3.B / Re-Exam 2024-25 / MU Dec 12, May 14, Dec 19 [10 Marks])*

#### Given Problem Statement:
1. It is a crime for an American to sell weapons to hostile nations.
2. The country Nono, an enemy of America, has some missiles.
3. All of Nono's missiles were sold to it by Colonel West.
4. Colonel West is an American.
5. Nono is an enemy of America.
6. Missiles are weapons.

**Goal:** Prove that **Colonel West is a Criminal** using **(A) First-Order Logic to CNF Conversion** and **(B) Resolution Refutation**.

---

#### Step 1: Translate Sentences into First-Order Logic (FOL)
1. $\forall x \forall y \forall z ((\text{American}(x) \wedge \text{Weapon}(y) \wedge \text{Sells}(x, y, z) \wedge \text{Hostile}(z)) \implies \text{Criminal}(x))$
2. $\exists x (\text{Owns}(\text{Nono}, x) \wedge \text{Missile}(x))$
3. $\forall x ((\text{Missile}(x) \wedge \text{Owns}(\text{Nono}, x)) \implies \text{Sells}(\text{West}, x, \text{Nono}))$
4. $\text{American}(\text{West})$
5. $\text{Enemy}(\text{Nono}, \text{America})$
6. $\forall x (\text{Missile}(x) \implies \text{Weapon}(x))$
7. $\forall x (\text{Enemy}(x, \text{America}) \implies \text{Hostile}(x))$  *(Background Knowledge)*

---

#### Step 2: Convert FOL Knowledge Base into CNF Clauses
* **From Axiom 1:**
  * $C_1: \neg \text{American}(x) \vee \neg \text{Weapon}(y) \vee \neg \text{Sells}(x, y, z) \vee \neg \text{Hostile}(z) \vee \text{Criminal}(x)$
* **From Axiom 2 (Skolemize with Skolem Constant $M_1$):**
  * $C_2: \text{Owns}(\text{Nono}, M_1)$
  * $C_3: \text{Missile}(M_1)$
* **From Axiom 3:**
  * $C_4: \neg \text{Missile}(x) \vee \neg \text{Owns}(\text{Nono}, x) \vee \text{Sells}(\text{West}, x, \text{Nono})$
* **From Axiom 4:**
  * $C_5: \text{American}(\text{West})$
* **From Axiom 5:**
  * $C_6: \text{Enemy}(\text{Nono}, \text{America})$
* **From Axiom 6:**
  * $C_7: \neg \text{Missile}(x) \vee \text{Weapon}(x)$
* **From Axiom 7:**
  * $C_8: \neg \text{Enemy}(x, \text{America}) \vee \text{Hostile}(x)$

---

#### Step 3: Negate the Query (Proof by Refutation)
* **Negated Goal Query:**
  * $C_0: \neg \text{Criminal}(\text{West})$

---

#### Step 4: Complete Resolution Refutation Tree

```text
               [ C0: ¬Criminal(West) ]       [ C1: ¬American(x) ∨ ¬Weapon(y) ∨ ¬Sells(x,y,z) ∨ ¬Hostile(z) ∨ Criminal(x) ]
                                  \             /
                                   \           / { x -> West }
                                    \         /
             [ C9: ¬American(West) ∨ ¬Weapon(y) ∨ ¬Sells(West, y, z) ∨ ¬Hostile(z) ]      [ C5: American(West) ]
                                               \                                            /
                                                \                                          /
                                                 \                                        /
                  [ C10: ¬Weapon(y) ∨ ¬Sells(West, y, z) ∨ ¬Hostile(z) ]      [ C8: ¬Enemy(v, America) ∨ Hostile(v) ]
                                                   \                           /
                                                    \                         / { v -> z }
                                                     \                       /
             [ C11: ¬Weapon(y) ∨ ¬Sells(West, y, z) ∨ ¬Enemy(z, America) ]      [ C6: Enemy(Nono, America) ]
                                                   \                                 /
                                                    \                               /
                                                     \                             / { z -> Nono }
                        [ C12: ¬Weapon(y) ∨ ¬Sells(West, y, Nono) ]      [ C7: ¬Missile(u) ∨ Weapon(u) ]
                                                    \                       /
                                                     \                     /
                                                      \                   /
                         [ C13: ¬Missile(y) ∨ ¬Sells(West, y, Nono) ]      [ C4: ¬Missile(w) ∨ ¬Owns(Nono, w) ∨ Sells(West, w, Nono) ]
                                                     \                       /
                                                      \                     / { y -> w }
                                                       \                   /
                           [ C14: ¬Missile(w) ∨ ¬Owns(Nono, w) ]      [ C3: Missile(M1) ]
                                        \                            /
                                         \                          / { w -> M1 }
                                          \                        /
                                 [ C15: ¬Owns(Nono, M1) ]      [ C2: Owns(Nono, M1) ]
                                            \                     /
                                             \                   /
                                              \                 /
                                           [ EMPTY CLAUSE: □ / NIL ]
```

**Resolution substitutions, checked:** $C_{10}$ with standardized-apart $C_8$ unifies $v\mapsto z$, producing $C_{11}$ with $z$ still free. Resolve $C_{11}$ with $C_6$ using $z\mapsto\text{Nono}$ to obtain $C_{12}$. Resolve with $C_7$ using $u\mapsto y$ to obtain $C_{13}$. Standardize $C_4$ apart with variable $w$; unify $y\mapsto w$ to derive $\neg\text{Missile}(w)\vee\neg\text{Owns}(\text{Nono},w)$ (duplicate missile literal removed). Use $w\mapsto M_1$, then $C_3$ and $C_2$, to obtain the empty clause.

**Forward-chaining answer requested in Question 5.1a:** Start with $\text{Owns}(\text{Nono},M_1)$, $\text{Missile}(M_1)$, $\text{American}(\text{West})$, and $\text{Enemy}(\text{Nono},\text{America})$. Apply $\text{Missile}(x)\Rightarrow\text{Weapon}(x)$ with $x\mapsto M_1$ to infer $\text{Weapon}(M_1)$. Apply the selling rule with $x\mapsto M_1$ to infer $\text{Sells}(\text{West},M_1,\text{Nono})$. Apply the enemy rule with $x\mapsto\text{Nono}$ to infer $\text{Hostile}(\text{Nono})$. Finally, the crime rule with $x\mapsto\text{West}$, $y\mapsto M_1$, $z\mapsto\text{Nono}$ infers $\text{Criminal}(\text{West})$.

* **Conclusion:** The derivation of the **Empty Clause ($\square$)** confirms that the assumption $\neg \text{Criminal}(\text{West})$ creates a logical contradiction. Therefore, **Colonel West is a Criminal**.

---

### ✍️ SOLVED PYQ 2: "Is Raja Angry?" (Rimi Hungry & Barking Domain)
*(Source: Mumbai University Dec 2015 [10 Marks])*

#### Given Facts:
1. Rimi is hungry.
2. If Rimi is hungry, she barks.
3. If Rimi is barking, then Raja is angry.

**Goal:** Prove that **Raja is angry** using **Resolution Refutation**.

---

#### Step 1: Convert Facts to Predicate Logic (FOL)
1. $\text{Hungry}(\text{Rimi})$
2. $\text{Hungry}(\text{Rimi}) \implies \text{Barks}(\text{Rimi})$
3. $\text{Barks}(\text{Rimi}) \implies \text{Angry}(\text{Raja})$

---

#### Step 2: Convert FOL to CNF Clauses
* $C_1: \text{Hungry}(\text{Rimi})$
* $C_2: \neg \text{Hungry}(\text{Rimi}) \vee \text{Barks}(\text{Rimi})$
* $C_3: \neg \text{Barks}(\text{Rimi}) \vee \text{Angry}(\text{Raja})$

---

#### Step 3: Negate Query & Resolve
* **Negated Goal ($C_0$):** $\neg \text{Angry}(\text{Raja})$

```text
    [ C0: ¬Angry(Raja) ]       [ C3: ¬Barks(Rimi) ∨ Angry(Raja) ]
                     \           /
                      \         /
                 [ C4: ¬Barks(Rimi) ]       [ C2: ¬Hungry(Rimi) ∨ Barks(Rimi) ]
                                  \           /
                                   \         /
                              [ C5: ¬Hungry(Rimi) ]       [ C1: Hungry(Rimi) ]
                                                \           /
                                                 \         /
                                              [ EMPTY CLAUSE: □ ]
```

* **Conclusion:** Deriving $\square$ proves that **Raja is Angry**.

---

### ✍️ SOLVED PYQ 3: "Is Someone Smiling?" (Graduating & Happy People)
*(Source: Mumbai University Dec 2015 [12 Marks])*

#### Given Axioms:
1. All people who are graduating are happy. ($\forall x (\text{Graduating}(x) \implies \text{Happy}(x))$)
2. All happy people smile. ($\forall x (\text{Happy}(x) \implies \text{Smile}(x))$)
3. Someone is graduating. ($\exists x \text{Graduating}(x)$)

**Goal:** Prove that **someone is smiling** ($\exists x \text{Smile}(x)$) using Resolution.

---

#### Step 1: Convert Axioms to CNF Clauses
* $C_1: \neg \text{Graduating}(x_1) \vee \text{Happy}(x_1)$
* $C_2: \neg \text{Happy}(x_2) \vee \text{Smile}(x_2)$
* $C_3: \text{Graduating}(\text{Jack})$  *(Skolem constant $\text{Jack}$ for $\exists x$)*

---

#### Step 2: Negate Query & Resolve
* **Negated Goal ($C_0$):** $\neg \exists x \text{Smile}(x) \equiv \forall x \neg \text{Smile}(x) \longrightarrow C_0 = \{\neg \text{Smile}(x_3)\}$

```text
    [ C0: ¬Smile(x3) ]       [ C2: ¬Happy(x2) ∨ Smile(x2) ]
                   \           /
                    \         / { x3 -> x2 }
                     \       /
               [ C4: ¬Happy(x2) ]       [ C1: ¬Graduating(x1) ∨ Happy(x1) ]
                                \           /
                                 \         / { x2 -> x1 }
                                  \       /
                           [ C5: ¬Graduating(x1) ]       [ C3: Graduating(Jack) ]
                                             \           /
                                              \         / { x1 -> Jack }
                                               \       /
                                           [ EMPTY CLAUSE: □ ]
```

* **Conclusion:** Deriving $\square$ proves that **Someone is Smiling**.

---

## SECTION 8: LAST-MINUTE REVISION & KEY RULES

1. **Resolution Step Checklist:**
   * Step 1: Translate English to FOL.
   * Step 2: Convert FOL to CNF (7 steps).
   * Step 3: Add **Negated Goal Clause** $\neg \text{Goal}$ to KB.
   * Step 4: Resolve complementary literals $(L \vee A) \wedge (\neg L \vee B) \implies (A \vee B)$ until $\square$ is produced.
2. **Quantifier Rules:**
   * Never translate *"All $A$ are $B$"* using $\wedge$: $\forall x (A(x) \wedge B(x))$ is WRONG! Use $\implies$: $\forall x (A(x) \implies B(x))$.
   * Never translate *"Some $A$ is $B$"* using $\implies$: $\exists x (A(x) \implies B(x))$ is WRONG! Use $\wedge$: $\exists x (A(x) \wedge B(x))$.
3. **Skolemization Rules:**
   * $\exists x P(x) \longrightarrow P(A)$ (Skolem Constant).
   * $\forall x \exists y P(x, y) \longrightarrow P(x, f(x))$ (Skolem Function dependent on $x$).

---

## SECTION 9: COMPLETE PYQ COVERAGE CHECKLIST

> This checks topic coverage within the draft, **not** verification that each listed item appeared in an official exam.

- [x] **Propositional Logic Truth Tables & Tautology Checks**
- [x] **Wumpus World PEAS & Propositional Knowledge Base Rules**
- [x] **First-Order Logic (FOL) Syntax, Quantifiers, and Translations**
- [x] **Canonical 7-Step FOL-to-CNF Conversion Algorithm**
- [x] **Skolemization (Constants vs Functions) & Equisatisfiability**
- [x] **Unification Algorithm, Substitution Matrices, MGU, & Occurs Check**
- [x] **Forward Chaining vs Backward Chaining Detailed Comparison**
- [x] **Resolution Refutation Proof Trees (American Weapon Crime - West)**
- [x] **Resolution Refutation Proof Trees (Rimi Hungry & Raja Angry)**
- [x] **Resolution Refutation Proof Trees (Graduating Happy Smiling People)**

---
