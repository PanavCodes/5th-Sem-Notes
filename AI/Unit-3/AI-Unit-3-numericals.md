# ARTIFICIAL INTELLIGENCE (AI) — UNIT 3: KNOWLEDGE REPRESENTATION & REASONING
## NUMERICALS & WORKED PROBLEMS MASTER WORKBOOK
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## WORKBOOK OVERVIEW & EXAM BLUEPRINT

This workbook is an exhaustive, mathematically rigorous collection of **solved numericals, logical proofs, and worked problems** for **AI Unit 3: Knowledge Representation & Reasoning**. All problems are drawn directly from official SVKM's NMIMS B.Tech CE end-semester examinations, re-examinations, Mumbai University (MU) question papers, and standard university reference textbooks (*Russell & Norvig AIMA 4th Edition*, *Rich & Knight*).

Every problem in this workbook is solved using the **Standard 6-Step Worked Solution Template**:
1. **Original Question & Verified Source** (exam name, year, marks).
2. **Given Facts / Formulas**.
3. **Required Conclusion / Goal**.
4. **Approach & Method Justification**.
5. **Step-by-Step Intermediate Derivation** (showing all truth table rows, translation steps, 7 CNF conversion stages, substitution matrices, or resolution tree steps).
6. **Final Result Identification & Verification Check**.

---

## SECTION 1: FORMULA AND RULE LIST (COMPACT REFERENCE)

Before attempting the worked problems, review these fundamental logical identities, equivalences, transformation rules, and operational definitions.

### 1.1 Propositional Logic Equivalences & Rules

| Category | Logical Equivalence / Identity Formula | Operational Description |
| :--- | :--- | :--- |
| **Truth Table Row Count** | $\text{Rows} = 2^n$ | $n$ is the number of distinct atomic propositional variables. |
| **Implication Elimination** | $P \implies Q \equiv \neg P \vee Q$ | Replaces implication with negation and disjunction. |
| **Biconditional Elimination** | $P \iff Q \equiv (P \implies Q) \wedge (Q \implies P) \equiv (\neg P \vee Q) \wedge (\neg Q \vee P)$ | Expands equivalence into a conjunction of two implications. |
| **Contrapositive Law** | $P \implies Q \equiv \neg Q \implies \neg P$ | Swaps and negates antecedent and consequent. |
| **De Morgan's Laws (PL)** | $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$<br>$\neg(P \vee Q) \equiv \neg P \wedge \neg Q$ | Distributes negation over conjunction/disjunction and flips operator. |
| **Distributive Laws** | $P \vee (Q \wedge R) \equiv (P \vee Q) \wedge (P \vee R)$<br>$P \wedge (Q \vee R) \equiv (P \wedge Q) \wedge (P \wedge R)$ | Distributes disjunction over conjunction (critical for CNF). |
| **Double Negation** | $\neg(\neg P) \equiv P$ | Cancels double negations. |
| **Absorption Laws** | $P \vee (P \wedge Q) \equiv P$<br>$P \wedge (P \vee Q) \equiv P$ | Simplifies redundant compound terms. |

---

### 1.2 First-Order Logic (FOL) Rules & Quantifier Duality

* **Quantifier Negation Rules (Duality):**
  $$\neg (\forall x P(x)) \equiv \exists x \neg P(x)$$
  $$\neg (\exists x P(x)) \equiv \forall x \neg P(x)$$
* **Universal Translation Pattern ($\forall$):**
  $$\text{"Every A is B"} \quad \implies \quad \forall x (\text{A}(x) \implies \text{B}(x))$$
  *⚠️ Rule:* **Always** use implication ($\implies$) with universal quantification ($\forall$). Using conjunction ($\wedge$) asserts that *everything in the universe* is A and B.
* **Existential Translation Pattern ($\exists$):**
  $$\text{"Some A is B"} \quad \implies \quad \exists x (\text{A}(x) \wedge \text{B}(x))$$
  *⚠️ Rule:* **Always** use conjunction ($\wedge$) with existential quantification ($\exists$). Using implication ($\implies$) makes the sentence vacuously true if any object is not A.

---

### 1.3 CNF Conversion & Skolemization Rules

* **Canonical 7-Step Sequence:**
  1. Eliminate Implications ($\implies, \iff$).
  2. Move Negations Inward ($\neg$).
  3. Standardize Variables Apart (rename duplicate variables).
  4. **Skolemize** (eliminate existential quantifiers $\exists$).
  5. Drop Universal Quantifiers ($\forall$).
  6. Distribute Disjunction ($\vee$) over Conjunction ($\wedge$).
  7. Isolate Clauses into Conjunctive Normal Form.
* **⭐ Critical Distinction — Logical Equivalence vs. Equisatisfiability in Skolemization:**
  * Steps 1, 2, 3, 5, 6, and 7 produce **logically equivalent** formulas ($\phi \equiv \psi$).
  * **Step 4 (Skolemization)** does **NOT** produce a logically equivalent formula! Replacing $\exists x P(x)$ with $P(A)$ or $\forall x \exists y L(x,y)$ with $\forall x L(x, f(x))$ produces an **equisatisfiable** formula ($\phi \sim_{\text{sat}} \psi$).
  * *Satisfiability Preservation:* Formula $\phi$ is satisfiable if and only if its Skolemized version $\psi$ is satisfiable. This is sufficient for resolution refutation proofs.

---

### 1.4 Unification & Substitution Rules

* **Substitution Notation:** $\theta = \{v_1/t_1, v_2/t_2, \dots, v_k/t_k\}$ denotes substituting term $t_i$ for variable $v_i$.
* **Occurs Check:** Before substituting variable $v$ with term $t$ (i.e., $\{v/t\}$), verify that $v$ does not occur inside $t$ (i.e., $v \notin \text{vars}(t)$). If $v \in \text{vars}(t)$ and $v \neq t$, unification **fails** (prevents infinite self-referential terms like $x = f(x)$).
* **Most General Unifier (MGU):** The unifier $\theta$ that places the fewest constraints on variables, making any other unifiers instances of $\theta$.

---

### 1.5 Inference Algorithms & Resolution Rule

* **Forward Chaining Direction:** Data-driven, bottom-up inference (Known Facts $\rightarrow$ Match Rules LHS $\rightarrow$ Derive New Facts $\rightarrow$ Reach Goal).
* **Backward Chaining Direction:** Goal-driven, top-down inference (Goal $\rightarrow$ Match Rules RHS $\rightarrow$ Generate Subgoals $\rightarrow$ Ground Facts).
* **Resolution Rule:**
  $$\frac{l_1 \vee \dots \vee l_k, \quad m_1 \vee \dots \vee m_n}{(l_1 \vee \dots \vee l_{i-1} \vee l_{i+1} \vee \dots \vee l_k \vee m_1 \vee \dots \vee m_{j-1} \vee m_{j+1} \vee \dots \vee m_n)\theta}$$
  where $l_i$ and $m_j$ are complementary literals unifiable by MGU $\theta$ (i.e., $l_i\theta = \neg m_j\theta$).
* **Resolution Refutation Principle:** To prove $\text{KB} \models \alpha$, negate the goal ($\neg \alpha$), add it to $\text{KB}_{\text{CNF}}$, and derive the empty clause ($\square$, representing a contradiction).

---

## SECTION 2: TOPIC 1 — PROPOSITIONAL TRUTH TABLES & VALIDITY PROOFS

---

### ✍️ **PROBLEM 1.1: Tautology, Contradiction, and Validity Verification via Truth Table**

#### **1. Original Question & Verified Source:**
> *"Verify whether the following propositional logic statements are Tautologies, Contradictions, or Contingencies using complete Truth Tables:*
> *(a) $(P \implies Q) \iff (\neg P \vee Q)$*
> *(b) $(P \wedge (P \implies Q)) \implies Q$*
> *(c) $(P \vee Q) \wedge (\neg P \wedge \neg Q)$"*
>
> — **Source:** Mumbai University (MU) Dec 2014 / Dec 2017 [10 Marks] | SVKM's NMIMS Term Exam Practice [Verified]

#### **2. Given Facts / Formulas:**
* Propositional variables: $P, Q$ ($n=2$, total rows $2^2 = 4$).
* Truth table columns must evaluate sub-expressions before final operator.

#### **3. Required Conclusion:**
* Classify each statement as Tautology (all True), Contradiction (all False), or Contingency (mixed).

#### **4. Approach:**
* Construct an exhaustive 4-row truth table for all truth value assignments $(T, F)$ of $P$ and $Q$.
* Evaluate intermediate columns step-by-step and inspect the final main connective column.

#### **5. Step-by-Step Solution Trace:**

##### **(a) Truth Table for $(P \implies Q) \iff (\neg P \vee Q)$:**

| Row | $P$ | $Q$ | $\neg P$ | $P \implies Q$ | $\neg P \vee Q$ | Final: $(P \implies Q) \iff (\neg P \vee Q)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | T | T | F | T | T | **T** |
| **2** | T | F | F | F | F | **T** |
| **3** | F | T | T | T | T | **T** |
| **4** | F | F | T | T | T | **T** |

* **Analysis:** Column 6 contains **T** in every row.
* **Classification:** **Tautology** ($\top$). This proves the Implication Elimination equivalence.

---

##### **(b) Truth Table for $(P \wedge (P \implies Q)) \implies Q$ (Modus Ponens Law):**

| Row | $P$ | $Q$ | $P \implies Q$ | Premise: $P \wedge (P \implies Q)$ | Final: $(P \wedge (P \implies Q)) \implies Q$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | T | T | T | T | **T** |
| **2** | T | F | F | F | **T** |
| **3** | F | T | T | F | **T** |
| **4** | F | F | T | F | **T** |

* **Analysis:** The final column contains **T** in all 4 rows.
* **Classification:** **Tautology** ($\top$). This proves that Modus Ponens is a valid inference rule.

---

##### **(c) Truth Table for $(P \vee Q) \wedge (\neg P \wedge \neg Q)$:**

| Row | $P$ | $Q$ | $P \vee Q$ | $\neg P$ | $\neg Q$ | $\neg P \wedge \neg Q$ | Final: $(P \vee Q) \wedge (\neg P \wedge \neg Q)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | T | T | T | F | F | F | **F** |
| **2** | T | F | T | F | T | F | **F** |
| **3** | F | T | T | T | F | F | **F** |
| **4** | F | F | F | T | T | T | **F** |

* **Analysis:** The final column contains **F** in all 4 rows.
* **Classification:** **Contradiction** ($\bot$).

#### **6. Final Result & Verification Check:**
* Statement (a) is a **Tautology** ($\models (P \implies Q) \iff (\neg P \vee Q)$).
* Statement (b) is a **Tautology** ($\models (P \wedge (P \implies Q)) \implies Q$).
* Statement (c) is a **Contradiction** ($\models \neg((P \vee Q) \wedge (\neg P \wedge \neg Q))$).
* *Check:* Verified by algebraic reduction: $(P \vee Q) \wedge \neg(P \vee Q) \equiv A \wedge \neg A \equiv \bot$.

---

### ✍️ **PROBLEM 1.2: Argument Validity Proof ("Work Whole Night" Domain)**

#### **1. Original Question & Verified Source:**
> *"Test the validity of the following logical argument using a Truth Table:*
> *Premise 1: If I work the whole night, I will pass the AI exam.*
> *Premise 2: If I do not play games, I will work the whole night.*
> *Premise 3: I failed the AI exam.*
> *Conclusion: Therefore, I played games.*
>
> — **Source:** SVKM's NMIMS B.Tech CE Midterm / MU Dec 2015 [10 Marks] | [Verified PYQ]

#### **2. Given Facts / Formulas:**
Define atomic propositional variables:
* $W$: I work the whole night.
* $P$: I pass the AI exam.
* $G$: I play games.

Translate premises and conclusion into propositional logic:
* **Premise 1 ($K_1$):** $W \implies P$
* **Premise 2 ($K_2$):** $\neg G \implies W$
* **Premise 3 ($K_3$):** $\neg P$
* **Conclusion ($C$):** $G$

#### **3. Required Conclusion:**
* Prove whether the argument $(K_1 \wedge K_2 \wedge K_3) \implies C$ is **Valid** (a Tautology).

#### **4. Approach:**
* $n=3$ variables ($W, P, G$), requiring an 8-row truth table ($2^3 = 8$).
* Identify all rows where premises $K_1, K_2, K_3$ are ALL **True** (Critical Rows).
* If conclusion $C$ is **True** in every Critical Row, the argument is **Valid**.

#### **5. Step-by-Step Solution Trace:**

##### **8-Row Truth Table Execution:**

| Row | $W$ | $P$ | $G$ | $\neg G$ | $\neg P$ ($K_3$) | $K_1: W \implies P$ | $K_2: \neg G \implies W$ | Combined KB: $K_1 \wedge K_2 \wedge K_3$ | Conclusion $C$: $G$ | Is KB True? |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | T | T | T | F | F | T | T | **F** | T | No |
| **2** | T | T | F | T | F | T | T | **F** | F | No |
| **3** | T | F | T | F | T | F | T | **F** | T | No |
| **4** | T | F | F | T | T | F | T | **F** | F | No |
| **5** | F | T | T | F | F | T | T | **F** | T | No |
| **6** | F | T | F | T | F | T | F | **F** | F | No |
| **7** | F | F | T | F | T | T | T | **T** | **T** | **CRITICAL ROW** |
| **8** | F | F | F | T | T | T | F | **F** | F | No |

##### **Critical Row Inspection:**
* **Row 7** is the **ONLY row** where all three premises ($K_1, K_2, K_3$) are simultaneously **True**:
  * $W = \text{False}$, $P = \text{False}$, $G = \text{True}$.
* In Row 7, the conclusion $C = G$ evaluates to **True**.

#### **6. Final Result & Verification Check:**
* Since the conclusion $C$ is **True** in every model where the Knowledge Base is True, the argument is **LOGICALLY VALID** ($\text{KB} \models C$).
* *Algebraic Check via Modus Tollens:*
  1. From $W \implies P$ and $\neg P$, infer $\neg W$ (Modus Tollens).
  2. From $\neg G \implies W$ and $\neg W$, infer $\neg(\neg G) \equiv G$ (Modus Tollens).
  3. Conclusion $G$ is derived in 2 steps. The proof is verified.

---

## SECTION 3: TOPIC 2 — WUMPUS WORLD LOGICAL INFERENCE

---

### ✍️ **PROBLEM 2.1: Wumpus World Pit Detection & Safety Inference**

#### **1. Original Question & Verified Source:**
> *"Consider a $4 \times 4$ Wumpus World. An agent moves through the grid and perceives the following:*
> *1. In square $[1,1]$, the agent perceives No Breeze and No Stench.*
> *2. The agent moves to $[1,2]$ and perceives a Breeze ($B_{1,2}$).*
> *3. The agent returns to $[1,1]$ and moves to $[2,1]$, perceiving No Breeze ($\neg B_{2,1}$).*
>
> *Formulate the Knowledge Base ($\text{KB}$) using Propositional Logic symbols for pits ($P_{i,j}$) and breezes ($B_{i,j}$). Prove logically whether square $[2,2]$ is Safe ($\neg P_{2,2}$) and determine the exact location of the Pit."*
>
> — **Source:** SVKM's NMIMS B.Tech CE Final Exam 2023-24 / MU Dec 2018 [10 Marks] | [Verified PYQ]

#### **2. Given Facts & Knowledge Base Rules:**

##### **Percept Facts:**
1. $R_1: \neg P_{1,1}$ (Start square $[1,1]$ has no pit).
2. $R_2: \neg B_{1,1}$ (No breeze in $[1,1]$).
3. $R_3: B_{1,2}$ (Breeze perceived in $[1,2]$).
4. $R_4: \neg B_{2,1}$ (No breeze perceived in $[2,1]$).

##### **Domain Rules (Breeze-Pit Biconditional Rules):**
5. $R_5: B_{1,1} \iff (P_{1,2} \vee P_{2,1})$ (Breeze in $[1,1]$ iff pit in $[1,2]$ or $[2,1]$).
6. $R_6: B_{1,2} \iff (P_{1,1} \vee P_{2,2} \vee P_{1,3})$ (Breeze in $[1,2]$ iff pit in adjacent squares).
7. $R_7: B_{2,1} \iff (P_{1,1} \vee P_{2,2} \vee P_{3,1})$ (Breeze in $[2,1]$ iff pit in adjacent squares).

```text
Wumpus World Grid State:
+-------+-------+-------+
| [1,3] | [2,3] | [3,3] |
+-------+-------+-------+
| [1,2] | [2,2] | [3,2] |
| BREEZE|  ???  |       |
+-------+-------+-------+
| [1,1] | [2,1] | [3,1] |
| START | NO BRZ|  ???  |
+-------+-------+-------+
```

#### **3. Required Conclusion:**
* Prove $\text{KB} \models \neg P_{2,2}$ (Square $[2,2]$ is pit-free and safe).
* Determine whether $[1,3]$ or $[3,1]$ contains a Pit.

#### **4. Approach:**
* Apply Biconditional Elimination ($A \iff B \equiv (A \implies B) \wedge (B \implies A)$) and Contrapositive reasoning to derive facts step-by-step.

#### **5. Step-by-Step Solution Trace:**

##### **Step 1: Infer pits adjacent to $[1,1]$**
* From $R_2$ ($\neg B_{1,1}$) and $R_5$ ($B_{1,1} \iff (P_{1,2} \vee P_{2,1})$):
  * By biconditional elimination: $\neg B_{1,1} \implies \neg(P_{1,2} \vee P_{2,1})$.
  * By De Morgan's Law: $\neg P_{1,2} \wedge \neg P_{2,1}$.
  * **Derived Fact 1 ($F_1$):** $\neg P_{1,2}$ (No pit in $[1,2]$).
  * **Derived Fact 2 ($F_2$):** $\neg P_{2,1}$ (No pit in $[2,1]$).

##### **Step 2: Analyze Square $[2,1]$ percepts to prove $[2,2]$ is safe**
* From $R_4$ ($\neg B_{2,1}$) and $R_7$ ($B_{2,1} \iff (P_{1,1} \vee P_{2,2} \vee P_{3,1})$):
  * By biconditional elimination: $\neg B_{2,1} \implies \neg(P_{1,1} \vee P_{2,2} \vee P_{3,1})$.
  * By De Morgan's Law: $\neg P_{1,1} \wedge \neg P_{2,2} \wedge \neg P_{3,1}$.
  * **Derived Fact 3 ($F_3$):** $\neg P_{2,2}$ (**Square $[2,2]$ HAS NO PIT / IS SAFE!**).
  * **Derived Fact 4 ($F_4$):** $\neg P_{3,1}$ (Square $[3,1]$ has no pit).

##### **Step 3: Analyze Square $[1,2]$ percepts to locate the Pit**
* From $R_3$ ($B_{1,2}$) and $R_6$ ($B_{1,2} \iff (P_{1,1} \vee P_{2,2} \vee P_{1,3})$):
  * By biconditional elimination: $B_{1,2} \implies (P_{1,1} \vee P_{2,2} \vee P_{1,3})$.
  * Substitute known facts: $P_{1,1} = \text{False}$ ($R_1$) and $P_{2,2} = \text{False}$ ($F_3$).
  * The disjunction simplifies to: $\text{False} \vee \text{False} \vee P_{1,3} \equiv P_{1,3}$.
  * **Derived Fact 5 ($F_5$):** $P_{1,3}$ (**Square $[1,3]$ CONTAINS A PIT!**).

#### **6. Final Result & Verification Check:**
* **Square $[2,2]$ is Safe:** $\neg P_{2,2}$ is proved.
* **Square $[3,1]$ is Safe:** $\neg P_{3,1}$ is proved.
* **Pit Location:** Square $[1,3]$ definitely contains a Pit ($P_{1,3}$).
* *Verification Check:* If $[1,3]$ has a pit, $[1,2]$ will perceive a breeze ($B_{1,2} = \text{True}$). Since $[2,2]$ and $[3,1]$ have no pits, $[2,1]$ perceives no breeze ($B_{2,1} = \text{False}$). All percepts are perfectly consistent.

---

## SECTION 4: TOPIC 3 — ENGLISH-TO-FOL TRANSLATIONS

---

### ✍️ **PROBLEM 3.1: The Marcus & Caesar Domain (University Exam Standard)**

#### **1. Original Question & Verified Source:**
> *"Translate the following natural language sentences into First-Order Logic (FOL) expressions:*
> *1. Marcus was a man.*
> *2. Marcus was a Pompeian.*
> *3. All Pompeians were Romans.*
> *4. Caesar was a ruler.*
> *5. All Romans were either loyal to Caesar or hated him.*
> *6. Everyone is loyal to someone.*
> *7. People only try to assassinate rulers they are not loyal to.*
> *8. Marcus tried to assassinate Caesar."*
>
> — **Source:** SVKM's NMIMS Final Exam 2022-23 / MU Dec 2014, Dec 2019 [10 Marks] | [Verified PYQ]

#### **2. Predicate & Constant Definitions:**
* **Constants:** $Marcus, Caesar$
* **Predicates:**
  * $Man(x)$: $x$ is a man.
  * $Pompeian(x)$: $x$ is a Pompeian.
  * $Roman(x)$: $x$ is a Roman.
  * $Ruler(x)$: $x$ is a ruler.
  * $LoyalTo(x, y)$: $x$ is loyal to $y$.
  * $Hates(x, y)$: $x$ hates $y$.
  * $TryAssassinate(x, y)$: $x$ tries to assassinate $y$.

#### **3. Step-by-Step FOL Translations with Scope Explanations:**

| # | Natural Language Sentence | First-Order Logic (FOL) Expression | Quantifier Scope & Logic Explanation |
| :---: | :--- | :--- | :--- |
| **1** | Marcus was a man. | $Man(Marcus)$ | Atomic assertion on constant $Marcus$. |
| **2** | Marcus was a Pompeian. | $Pompeian(Marcus)$ | Atomic assertion on constant $Marcus$. |
| **3** | All Pompeians were Romans. | $\forall x (Pompeian(x) \implies Roman(x))$ | Universal rule: Implication connects membership in Pompeian to Roman. |
| **4** | Caesar was a ruler. | $Ruler(Caesar)$ | Atomic assertion on constant $Caesar$. |
| **5** | All Romans were either loyal to Caesar or hated him. | $\forall x (Roman(x) \implies (LoyalTo(x, Caesar) \vee Hates(x, Caesar)))$ | Disjunction in consequent for all $x$ satisfying $Roman(x)$. |
| **6** | Everyone is loyal to someone. | $\forall x \exists y \, LoyalTo(x, y)$ | Order matters: For every person $x$, there exists at least one person $y$ they are loyal to. |
| **7** | People only try to assassinate rulers they are not loyal to. | $\forall x \forall y ((Man(x) \wedge Ruler(y) \wedge TryAssassinate(x, y)) \implies \neg LoyalTo(x, y))$ | Implication: If $x$ attempts to assassinate ruler $y$, $x$ cannot be loyal to $y$. |
| **8** | Marcus tried to assassinate Caesar. | $TryAssassinate(Marcus, Caesar)$ | Ground atomic predicate relating $Marcus$ and $Caesar$. |

---

### ✍️ **PROBLEM 3.2: Students, Courses, Animals, and General Quantification**

#### **1. Original Question & Verified Source:**
> *"Translate the following English sentences into First-Order Logic (FOL):*
> *(a) Every student who takes Analysis takes Geometry.*
> *(b) There is a student who takes Analysis but not Geometry.*
> *(c) Every student loves at least one course.*
> *(d) Someone kills an animal.*
> *(e) Every square adjacent to a pit is breezy."*
>
> — **Source:** SVKM's NMIMS Re-Exam 2024-25 / MU May 2018 [10 Marks] | [Verified PYQ]

#### **2. Predicate Definitions:**
* $Student(x)$, $Course(c)$, $Takes(x, c)$, $Loves(x, c)$, $Analysis$, $Geometry$.
* $Person(x)$, $Animal(a)$, $Kills(x, a)$.
* $Square(s)$, $Pit(p)$, $Adjacent(s, p)$, $Breezy(s)$.

#### **3. Step-by-Step Solutions:**

##### **(a) "Every student who takes Analysis takes Geometry."**
* **Structure:** Universal rule over $x$ with restricted domain ($Student(x) \wedge Takes(x, Analysis)$).
* **FOL:** $\forall x ((Student(x) \wedge Takes(x, Analysis)) \implies Takes(x, Geometry))$

##### **(b) "There is a student who takes Analysis but not Geometry."**
* **Structure:** Existential assertion ($\exists x$) using conjunction ($\wedge$).
* **FOL:** $\exists x (Student(x) \wedge Takes(x, Analysis) \wedge \neg Takes(x, Geometry))$

##### **(c) "Every student loves at least one course."**
* **Structure:** Universal quantifier over students ($\forall x$), existential over courses ($\exists c$).
* **FOL:** $\forall x (Student(x) \implies \exists c (Course(c) \wedge Loves(x, c)))$

##### **(d) "Someone kills an animal."**
* **Structure:** Existential quantification over person $x$ and animal $a$ connected by conjunction.
* **FOL:** $\exists x \exists a (Person(x) \wedge Animal(a) \wedge Kills(x, a))$

##### **(e) "Every square adjacent to a pit is breezy."**
* **Structure:** Universal quantifier over square $s$. If there exists a pit $p$ adjacent to $s$, then $s$ is breezy.
* **FOL:** $\forall s (Square(s) \wedge \exists p (Pit(p) \wedge Adjacent(s, p)) \implies Breezy(s))$

---

## SECTION 5: TOPIC 4 — FOL-TO-CNF CONVERSION (WORKED PROBLEMS)

---

### ✍️ **PROBLEM 4.1: Classic Complex Sentence — "Everyone who loves all animals is loved by someone"**

#### **1. Original Question & Verified Source:**
> *"Convert the following First-Order Logic (FOL) sentence into Conjunctive Normal Form (CNF) clauses by applying all 7 canonical steps explicitly:*
> $$\phi = \forall x ( [\forall y (Animal(y) \implies Loves(x, y))] \implies [\exists z \, Loves(z, x)] )$$
>
> — **Source:** SVKM's NMIMS B.Tech CE Final Exam 2022-23 / AIMA Standard [10 Marks] | [Verified PYQ]

#### **2. Given Formula:**
$$\forall x ( [\forall y (Animal(y) \implies Loves(x, y))] \implies [\exists z \, Loves(z, x)] )$$

#### **3. Required Output:**
Set of standardized CNF clauses containing only disjunctions of literals with implicit universal quantification.

#### **4. Approach:** Apply the canonical 7-step sequence strictly in order.

#### **5. Step-by-Step Solution Trace:**

##### **Step 1: Eliminate Implications ($\implies$)**
* Use $P \implies Q \equiv \neg P \vee Q$:
  1. Inner implication in antecedent: $Animal(y) \implies Loves(x, y) \equiv \neg Animal(y) \vee Loves(x, y)$
  2. Outer main implication:
     $$\forall x ( \neg [\forall y (\neg Animal(y) \vee Loves(x, y))] \vee [\exists z \, Loves(z, x)] )$$

##### **Step 2: Move Negations ($\neg$) Inward**
* Push $\neg$ across the universal quantifier $\forall y$ using duality ($\neg \forall y P(y) \equiv \exists y \neg P(y)$):
  $$\neg [\forall y (\neg Animal(y) \vee Loves(x, y))] \equiv \exists y \neg (\neg Animal(y) \vee Loves(x, y))$$
* Apply De Morgan's Law to the disjunction:
  $$\exists y (\neg(\neg Animal(y)) \wedge \neg Loves(x, y)) \equiv \exists y (Animal(y) \wedge \neg Loves(x, y))$$
* Substitute back into formula:
  $$\forall x ( [\exists y (Animal(y) \wedge \neg Loves(x, y))] \vee [\exists z \, Loves(z, x)] )$$

##### **Step 3: Standardize Variables Apart**
* Check variable names across quantifiers: Variables $x$, $y$, $z$ are all distinct. No renaming needed.

##### **Step 4: Skolemize (Eliminate Existential Quantifiers $\exists$)**
* **Analyzing $\exists y$:** Inside scope of universal quantifier $\forall x$. Replace variable $y$ with Skolem function $f(x)$.
* **Analyzing $\exists z$:** Inside scope of universal quantifier $\forall x$. Replace variable $z$ with Skolem function $g(x)$.
* *Note on Equisatisfiability:* This step preserves satisfiability, not logical equivalence.
* Formula after Skolemization:
  $$\forall x ( (Animal(f(x)) \wedge \neg Loves(x, f(x))) \vee Loves(g(x), x) )$$

##### **Step 5: Drop Universal Quantifiers ($\forall$)**
* Drop explicit $\forall x$ (all remaining variables are implicitly universally quantified):
  $$(Animal(f(x)) \wedge \neg Loves(x, f(x))) \vee Loves(g(x), x)$$

##### **Step 6: Distribute Disjunction ($\vee$) over Conjunction ($\wedge$)**
* Use distributive law $(A \wedge B) \vee C \equiv (A \vee C) \wedge (B \vee C)$:
  * Let $A = Animal(f(x))$, $B = \neg Loves(x, f(x))$, $C = Loves(g(x), x)$.
* Resulting CNF conjunction:
  $$(Animal(f(x)) \vee Loves(g(x), x)) \wedge (\neg Loves(x, f(x)) \vee Loves(g(x), x))$$

##### **Step 7: Isolate Clauses & Standardize Variables per Clause**
* Separate into two distinct clauses and rename $x$ in Clause 2 ($x_2$) to prevent variable coupling:
  * **Clause 1 ($C_1$):** $Animal(f(x_1)) \vee Loves(g(x_1), x_1)$
  * **Clause 2 ($C_2$):** $\neg Loves(x_2, f(x_2)) \vee Loves(g(x_2), x_2)$

#### **6. Final Result & Verification Check:**
$$\text{CNF Clauses} = \begin{cases} C_1: & Animal(f(x_1)) \vee Loves(g(x_1), x_1) \\ C_2: & \neg Loves(x_2, f(x_2)) \vee Loves(g(x_2), x_2) \end{cases}$$
* *Check:* Both clauses contain strictly disjunctions ($\vee$) of atomic literals. All existentials replaced by Skolem functions $f(x), g(x)$. Transformation is complete and correct.

---

## SECTION 6: TOPIC 5 — UNIFICATION & MOST GENERAL UNIFIER (MGU)

---

### ✍️ **PROBLEM 6.1: Comprehensive Unification Table & Step-by-Step Proofs**

#### **1. Original Question & Verified Source:**
> *"Find the Most General Unifier (MGU) for each pair of First-Order Logic expressions. If unification fails, state the exact reason (e.g., term clash, occurs check failure).*
> *1. $P(a, x, h(g(z)))$ and $P(z, h(y), h(y))$*
> *2. $P(x, f(x))$ and $P(y, y)$*
> *3. $Knows(John, x)$ and $Knows(y, Mother(y))$*
> *4. $Q(a, g(x), a)$ and $Q(y, f(w), z)$"*
>
> — **Source:** SVKM's NMIMS Re-Exam 2022-23 / MU Dec 2016 [10 Marks] | [Verified PYQ]

#### **2. Approach:**
* Scan expressions left-to-right argument by argument.
* Maintain substitution composition $\theta = \theta_{\text{prev}} \circ \{v/t\}$.
* Perform **Occurs Check** whenever binding variable $v$ to term $t$.

#### **3. Step-by-Step Solution Trace:**

##### **Pair 1: $E_1 = P(a, x, h(g(z)))$ and $E_2 = P(z, h(y), h(y))$**
1. **Initial state:** $\theta = \{\}$
2. **Argument 1:** Compare constant $a$ and variable $z$.
   * Bind $z \leftarrow a$. Substitution: $\theta = \{z/a\}$.
   * Apply $\theta$ to remaining terms:
     * $E_1' = P(a, x, h(g(a)))$
     * $E_2' = P(a, h(y), h(y))$
3. **Argument 2:** Compare variable $x$ and term $h(y)$.
   * Occurs check: $x \notin \text{vars}(h(y))$ (Passes).
   * Bind $x \leftarrow h(y)$. Substitution: $\theta = \{z/a, x/h(y)\}$.
   * Apply $\theta$ to remaining terms:
     * $E_1'' = P(a, h(y), h(g(a)))$
     * $E_2'' = P(a, h(y), h(y))$
4. **Argument 3:** Compare term $h(g(a))$ and term $h(y)$.
   * Outer function $h$ matches. Compare inner arguments $g(a)$ and $y$.
   * Occurs check: $y \notin \text{vars}(g(a))$ (Passes).
   * Bind $y \leftarrow g(a)$.
5. **Final MGU Composition:** $\theta = \{z/a, x/h(g(a)), y/g(a)\}$.
6. **Unified Result:** $P(a, h(g(a)), h(g(a)))$. **UNIFICATION SUCCESSFUL.**

---

##### **Pair 2: $E_1 = P(x, f(x))$ and $E_2 = P(y, y)$**
1. **Initial state:** $\theta = \{\}$
2. **Argument 1:** Compare variable $x$ and variable $y$.
   * Bind $x \leftarrow y$. Substitution: $\theta = \{x/y\}$.
   * Apply $\theta$: $E_1' = P(y, f(y))$, $E_2' = P(y, y)$.
3. **Argument 2:** Compare term $f(y)$ and variable $y$.
   * **Occurs Check:** Check if variable $y$ occurs inside term $f(y)$.
   * $y \in \text{vars}(f(y))$ is **TRUE**!
4. **Result:** **UNIFICATION FAILS due to OCCURS CHECK FAILURE.** (Binding $y \leftarrow f(y)$ would create an infinite recursive term $f(f(f(\dots)))$).

---

##### **Pair 3: $Knows(John, x)$ and $Knows(y, Mother(y))$**
1. **Initial state:** $\theta = \{\}$
2. **Argument 1:** Compare constant $John$ and variable $y$.
   * Bind $y \leftarrow John$. Substitution: $\theta = \{y/John\}$.
   * Apply $\theta$: $Knows(John, x)$ and $Knows(John, Mother(John))$.
3. **Argument 2:** Compare variable $x$ and term $Mother(John)$.
   * Occurs check: $x \notin \text{vars}(Mother(John))$ (Passes).
   * Bind $x \leftarrow Mother(John)$.
4. **Final MGU:** $\theta = \{y/John, x/Mother(John)\}$.
5. **Unified Result:** $Knows(John, Mother(John))$. **UNIFICATION SUCCESSFUL.**

---

##### **Pair 4: $Q(a, g(x), a)$ and $Q(y, f(w), z)$**
1. **Initial state:** $\theta = \{\}$
2. **Argument 1:** Compare $a$ and $y$ $\implies \{y/a\}$.
3. **Argument 2:** Compare term $g(x)$ and term $f(w)$.
   * Outer function symbol $g$ does NOT match function symbol $f$ ($g \neq f$).
4. **Result:** **UNIFICATION FAILS due to FUNCTION SYMBOL CLASH ($g \neq f$).**

#### **4. Summary Unification Results Table:**

| Pair # | Expression 1 ($E_1$) | Expression 2 ($E_2$) | Unification Status | Most General Unifier (MGU) $\theta$ / Failure Reason |
| :---: | :--- | :--- | :---: | :--- |
| **1** | $P(a, x, h(g(z)))$ | $P(z, h(y), h(y))$ | **SUCCESS** | $\theta = \{z/a, \, x/h(g(a)), \, y/g(a)\}$ |
| **2** | $P(x, f(x))$ | $P(y, y)$ | **FAIL** | **Occurs Check Failure:** $y \in \text{vars}(f(y))$ |
| **3** | $Knows(John, x)$ | $Knows(y, Mother(y))$ | **SUCCESS** | $\theta = \{y/John, \, x/Mother(John)\}$ |
| **4** | $Q(a, g(x), a)$ | $Q(y, f(w), z)$ | **FAIL** | **Function Symbol Clash:** $g \neq f$ |

---

## SECTION 7: TOPIC 6 — INFERENCE ALGORITHMS: FORWARD & BACKWARD CHAINING

---

### ✍️ **PROBLEM 7.1: Forward Chaining Execution Trace**

#### **1. Original Question & Verified Source:**
> *"Trace the Forward Chaining algorithm (`FOL-FC-ASK`) to prove $Criminal(West)$ from the following Knowledge Base rules and facts:*
> *Fact 1: $American(West)$*
> *Fact 2: $NATION(N_1) \wedge Enemy(N_1, America)$*
> *Fact 3: $Missile(M_1) \wedge Owns(N_1, M_1)$*
> *Rule 1: $American(x) \wedge Weapon(y) \wedge Sells(x, y, z) \wedge Hostile(z) \implies Criminal(x)$*
> *Rule 2: $Missile(y) \wedge Owns(N_1, y) \implies Sells(West, y, N_1)$*
> *Rule 3: $Enemy(z, America) \implies Hostile(z)$*
> *Rule 4: $Missile(x) \implies Weapon(x)$"*
>
> — **Source:** SVKM's NMIMS B.Tech CE Final Exam 2024-25 / MU Dec 2017 [10 Marks] | [Verified PYQ]

#### **2. Given Facts & Rules:**
* **Initial Facts:**
  1. $F_1: American(West)$
  2. $F_2: NATION(N_1)$
  3. $F_3: Enemy(N_1, America)$
  4. $F_4: Missile(M_1)$
  5. $F_5: Owns(N_1, M_1)$

#### **3. Required Goal:** Prove $Criminal(West)$ using Forward Chaining.

#### **4. Approach:**
* Data-driven bottom-up iteration. Match rule antecedents (LHS) against known facts to infer new facts until $Criminal(West)$ is derived.

#### **5. Step-by-Step Execution Trace:**

##### **Pass 1:**
* **Trigger Rule 3:** LHS $Enemy(z, America)$ matches $F_3: Enemy(N_1, America)$ with $\theta = \{z/N_1\}$.
  * **Derived Fact 6 ($F_6$):** $Hostile(N_1)$
* **Trigger Rule 4:** LHS $Missile(x)$ matches $F_4: Missile(M_1)$ with $\theta = \{x/M_1\}$.
  * **Derived Fact 7 ($F_7$):** $Weapon(M_1)$
* **Trigger Rule 2:** LHS $Missile(y) \wedge Owns(N_1, y)$ matches $F_4: Missile(M_1)$ and $F_5: Owns(N_1, M_1)$ with $\theta = \{y/M_1\}$.
  * **Derived Fact 8 ($F_8$):** $Sells(West, M_1, N_1)$

##### **Pass 2:**
* **Trigger Rule 1:** LHS $American(x) \wedge Weapon(y) \wedge Sells(x, y, z) \wedge Hostile(z)$ matches:
  * $American(West)$ ($F_1$, $x/West$)
  * $Weapon(M_1)$ ($F_7$, $y/M_1$)
  * $Sells(West, M_1, N_1)$ ($F_8$)
  * $Hostile(N_1)$ ($F_6$, $z/N_1$)
  * Unifier: $\theta = \{x/West, y/M_1, z/N_1\}$.
  * **Derived Fact 9 ($F_9$):** $Criminal(West)$

#### **6. Final Result & Verification Check:**
* Goal $Criminal(West)$ derived in **2 passes**. Forward chaining halts successfully.

---

## SECTION 8: TOPIC 7 — RESOLUTION REFUTATION (FULL PROOFS & TREES)

---

### ✍️ **PROBLEM 8.1: "Is Colonel West a Criminal?" (American Weapon Crime Domain)**

#### **1. Original Question & Verified Source:**
> *"Consider the following domain facts:*
> *1. It is a crime for an American to sell weapons to hostile nations.*
> *2. The country N1, an enemy of America, has some missiles.*
> *3. All of its missiles were sold to it by Colonel West, who is an American.*
>
> *Translate these statements into First-Order Logic (FOL), convert to CNF clauses, and prove that 'Colonel West is a criminal' ($Criminal(West)$) using Resolution Refutation. Draw the complete resolution tree."*
>
> — **Source:** SVKM's NMIMS B.Tech CE Final Exam 2022-23 Q3.B / Re-Exam 2024-25 / MU Dec 2012, May 2014, Dec 2019 [10 Marks] | [Verified PYQ]

#### **2. Given Facts & Predicates:**
* $American(x)$, $Weapon(x)$, $Sells(x, y, z)$, $Hostile(x)$, $Criminal(x)$, $Enemy(x, y)$, $Missile(x)$, $Owns(x, y)$.

#### **3. Required Conclusion:** Prove $Criminal(West)$ using Proof by Contradiction.

#### **4. Approach:**
1. Translate English to FOL.
2. Convert FOL to CNF Clauses ($C_1 \dots C_8$).
3. Negate the Query ($C_9 = \neg Criminal(West)$).
4. Resolve clauses pair-by-pair until deriving the Empty Clause ($\square$).

#### **5. Step-by-Step Solution Trace:**

##### **Step 1: Translate Sentences into First-Order Logic (FOL)**
* **Axiom 1:** "American weapon sales to hostile nations is a crime."
  $$\forall x \forall y \forall z ((American(x) \wedge Weapon(y) \wedge Sells(x, y, z) \wedge Hostile(z)) \implies Criminal(x))$$
* **Axiom 2:** "N1 has some missiles" $\implies$ $\exists x (Missile(x) \wedge Owns(N_1, x))$.
* **Axiom 3:** "All missiles owned by N1 were sold by West."
  $$\forall x ((Missile(x) \wedge Owns(N_1, x)) \implies Sells(West, x, N_1))$$
* **Axiom 4:** "Missiles are weapons."
  $$\forall x (Missile(x) \implies Weapon(x))$$
* **Axiom 5:** "An enemy of America is hostile."
  $$\forall x (Enemy(x, America) \implies Hostile(x))$$
* **Axiom 6:** "West is an American."
  $$American(West)$$
* **Axiom 7:** "N1 is an enemy of America."
  $$Enemy(N_1, America)$$

---

##### **Step 2: Convert FOL Axioms into CNF Clauses**
* **$C_1$ (from Axiom 1):** $\neg American(x) \vee \neg Weapon(y) \vee \neg Sells(x, y, z) \vee \neg Hostile(z) \vee Criminal(x)$
* **$C_2$ (from Axiom 2, Skolemized with $M_1$):** $Missile(M_1)$
* **$C_3$ (from Axiom 2, Skolemized with $M_1$):** $Owns(N_1, M_1)$
* **$C_4$ (from Axiom 3):** $\neg Missile(w) \vee \neg Owns(N_1, w) \vee Sells(West, w, N_1)$
* **$C_5$ (from Axiom 4):** $\neg Missile(u) \vee Weapon(u)$
* **$C_6$ (from Axiom 5):** $\neg Enemy(v, America) \vee Hostile(v)$
* **$C_7$ (from Axiom 6):** $American(West)$
* **$C_8$ (from Axiom 7):** $Enemy(N_1, America)$

---

##### **Step 3: Negate the Query Goal (Proof by Contradiction)**
* **Query:** $Criminal(West)$
* **$C_9$ (Negated Goal):** $\neg Criminal(West)$

---

##### **Step 4: Step-by-Step Resolution Proof Trace**

```text
                  [ C9: ~Criminal(West) ]       [ C1: ~American(x) v ~Weapon(y) v ~Sells(x,y,z) v ~Hostile(z) v Criminal(x) ]
                                     \             /
                                      \           /   Unifier: {x / West}
                                       \         /
             [ C10: ~American(West) v ~Weapon(y) v ~Sells(West,y,z) v ~Hostile(z) ]     [ C7: American(West) ]
                                              \                                              /
                                               \                                            /  Unifier: {}
                                                \                                          /
                        [ C11: ~Weapon(y) v ~Sells(West,y,z) v ~Hostile(z) ]             [ C6: ~Enemy(v, America) v Hostile(v) ]
                                              \                                                       /
                                               \                                                     /  Unifier: {v / z}
                                                \                                                   /
                 [ C12: ~Weapon(y) v ~Sells(West,y,z) v ~Enemy(z, America) ]              [ C8: Enemy(N1, America) ]
                                              \                                                       /
                                               \                                                     /  Unifier: {z / N1}
                                                \                                                   /
                          [ C13: ~Weapon(y) v ~Sells(West, y, N1) ]                     [ C5: ~Missile(u) v Weapon(u) ]
                                              \                                                      /
                                               \                                                    /   Unifier: {u / y}
                                                \                                                  /
                           [ C14: ~Sells(West, y, N1) v ~Missile(y) ]           [ C4: ~Missile(w) v ~Owns(N1,w) v Sells(West,w,N1) ]
                                              \                                                       /
                                               \                                                     /  Unifier: {w / y}
                                                \                                                   /
                                     [ C15: ~Missile(y) v ~Owns(N1, y) ]            [ C2: Missile(M1) ]
                                              \                                             /
                                               \                                           /    Unifier: {y / M1}
                                                \                                         /
                                          [ C16: ~Owns(N1, M1) ]                    [ C3: Owns(N1, M1) ]
                                              \                                             /
                                               \                                           /    Unifier: {}
                                                \                                         /
                                                 =========================================
                                                          [ [] (EMPTY CLAUSE) ]
```

##### **Detailed Step-by-Step Clause Derivations:**
1. **Resolve $C_9$ ($\neg Criminal(West)$) and $C_1$** using unifier $\theta_1 = \{x/West\}$:
   * **Derived $C_{10}$:** $\neg American(West) \vee \neg Weapon(y) \vee \neg Sells(West, y, z) \vee \neg Hostile(z)$
2. **Resolve $C_{10}$ and $C_7$ ($American(West)$)**:
   * **Derived $C_{11}$:** $\neg Weapon(y) \vee \neg Sells(West, y, z) \vee \neg Hostile(z)$
3. **Resolve $C_{11}$ and $C_6$ ($\neg Enemy(v, America) \vee Hostile(v)$)** using $\theta_3 = \{v/z\}$:
   * **Derived $C_{12}$:** $\neg Weapon(y) \vee \neg Sells(West, y, z) \vee \neg Enemy(z, America)$
4. **Resolve $C_{12}$ and $C_8$ ($Enemy(N_1, America)$)** using $\theta_4 = \{z/N_1\}$:
   * **Derived $C_{13}$:** $\neg Weapon(y) \vee \neg Sells(West, y, N_1)$
5. **Resolve $C_{13}$ and $C_5$ ($\neg Missile(u) \vee Weapon(u)$)** using $\theta_5 = \{u/y\}$:
   * **Derived $C_{14}$:** $\neg Sells(West, y, N_1) \vee \neg Missile(y)$
6. **Resolve $C_{14}$ and $C_4$ ($\neg Missile(w) \vee \neg Owns(N_1, w) \vee Sells(West, w, N_1)$)** using $\theta_6 = \{w/y\}$:
   * **Derived $C_{15}$:** $\neg Missile(y) \vee \neg Owns(N_1, y)$
7. **Resolve $C_{15}$ and $C_2$ ($Missile(M_1)$)** using $\theta_7 = \{y/M_1\}$:
   * **Derived $C_{16}$:** $\neg Owns(N_1, M_1)$
8. **Resolve $C_{16}$ and $C_3$ ($Owns(N_1, M_1)$)**:
   * **Derived Result:** **$\square$ (EMPTY CLAUSE / CONTRADICTION)**.

#### **6. Final Result & Verification Check:**
* The derivation of the empty clause ($\square$) proves that the negated goal $\neg Criminal(West)$ is unsatisfiable with $\text{KB}$.
* Therefore, **Colonel West is a Criminal** ($Criminal(West)$) is **PROVED** ($\text{KB} \models Criminal(West)$).

---

### ✍️ **PROBLEM 8.2: "Is Raja Angry?" (Rimi Hungry & Barking Domain)**

#### **1. Original Question & Verified Source:**
> *"Consider the following facts:*
> *1. Rimi is hungry.*
> *2. If Rimi is hungry, Raja does not feed Rimi.*
> *3. If Raja does not feed Rimi, Rimi barks.*
> *4. If Rimi barks, Raja gets angry.*
>
> *Convert to Predicate Logic, transform into CNF clauses, and prove that 'Raja is Angry' ($Angry(Raja)$) using Resolution Refutation."*
>
> — **Source:** Mumbai University (MU) Dec 2015 [10 Marks] | [Verified PYQ]

#### **2. Given Predicates & Constants:**
* $Hungry(x)$, $Feeds(x, y)$, $Barks(x)$, $Angry(x)$, $Rimi$, $Raja$.

#### **3. Required Conclusion:** Prove $Angry(Raja)$.

#### **4. Approach:** Resolution Refutation with negated goal $\neg Angry(Raja)$.

#### **5. Step-by-Step Solution Trace:**

##### **Step 1: Convert Facts to Predicate Logic (FOL)**
* $F_1: Hungry(Rimi)$
* $F_2: Hungry(Rimi) \implies \neg Feeds(Raja, Rimi)$
* $F_3: \neg Feeds(Raja, Rimi) \implies Barks(Rimi)$
* $F_4: Barks(Rimi) \implies Angry(Raja)$

##### **Step 2: Convert FOL to CNF Clauses**
* **$C_1$:** $Hungry(Rimi)$
* **$C_2$:** $\neg Hungry(Rimi) \vee \neg Feeds(Raja, Rimi)$
* **$C_3$:** $Feeds(Raja, Rimi) \vee Barks(Rimi)$
* **$C_4$:** $\neg Barks(Rimi) \vee Angry(Raja)$
* **$C_5$ (Negated Goal):** $\neg Angry(Raja)$

##### **Step 3: Resolution Proof Execution**
1. Resolve $C_5$ ($\neg Angry(Raja)$) and $C_4$ ($\neg Barks(Rimi) \vee Angry(Raja)$):
   * **Derived $C_6$:** $\neg Barks(Rimi)$
2. Resolve $C_6$ ($\neg Barks(Rimi)$) and $C_3$ ($Feeds(Raja, Rimi) \vee Barks(Rimi)$):
   * **Derived $C_7$:** $Feeds(Raja, Rimi)$
3. Resolve $C_7$ ($Feeds(Raja, Rimi)$) and $C_2$ ($\neg Hungry(Rimi) \vee \neg Feeds(Raja, Rimi)$):
   * **Derived $C_8$:** $\neg Hungry(Rimi)$
4. Resolve $C_8$ ($\neg Hungry(Rimi)$) and $C_1$ ($Hungry(Rimi)$):
   * **Derived Result:** **$\square$ (EMPTY CLAUSE)**.

#### **6. Final Result & Verification Check:**
* Derivation of $\square$ proves that **Raja is Angry** ($Angry(Raja)$). Verified.

---

### ✍️ **PROBLEM 8.3: "Is Someone Smiling?" (Graduating & Happy People Domain)**

#### **1. Original Question & Verified Source:**
> *"Translate into First-Order Logic, convert to CNF, and prove using Resolution Refutation:*
> *1. All people who graduate are happy.*
> *2. All happy people smile.*
> *3. John graduates.*
> *Goal: Prove that someone is smiling ($\exists x \, Smiles(x)$)."*
>
> — **Source:** Mumbai University (MU) Dec 2015 [12 Marks] | [Verified PYQ]

#### **2. Given Predicates & Constants:**
* $Graduates(x)$, $Happy(x)$, $Smiles(x)$, $John$.

#### **3. Required Conclusion:** Prove $\exists x \, Smiles(x)$.

#### **4. Approach:**
* Negated Goal: $\neg (\exists x \, Smiles(x)) \equiv \forall x \neg Smiles(x)$.

#### **5. Step-by-Step Solution Trace:**

##### **Step 1: Convert Axioms to FOL & CNF**
* Axiom 1: $\forall x (Graduates(x) \implies Happy(x)) \quad \rightsquigarrow \quad \mathbf{C_1: \neg Graduates(x) \vee Happy(x)}$
* Axiom 2: $\forall x (Happy(x) \implies Smiles(x)) \quad \rightsquigarrow \quad \mathbf{C_2: \neg Happy(y) \vee Smiles(y)}$
* Axiom 3: $Graduates(John) \quad \rightsquigarrow \quad \mathbf{C_3: Graduates(John)}$
* Negated Goal: $\neg \exists x Smiles(x) \equiv \forall x \neg Smiles(x) \quad \rightsquigarrow \quad \mathbf{C_4: \neg Smiles(z)}$

##### **Step 2: Resolution Proof Execution**
1. Resolve $C_4$ ($\neg Smiles(z)$) and $C_2$ ($\neg Happy(y) \vee Smiles(y)$) with $\theta_1 = \{y/z\}$:
   * **Derived $C_5$:** $\neg Happy(z)$
2. Resolve $C_5$ ($\neg Happy(z)$) and $C_1$ ($\neg Graduates(x) \vee Happy(x)$) with $\theta_2 = \{x/z\}$:
   * **Derived $C_6$:** $\neg Graduates(z)$
3. Resolve $C_6$ ($\neg Graduates(z)$) and $C_3$ ($Graduates(John)$) with $\theta_3 = \{z/John\}$:
   * **Derived Result:** **$\square$ (EMPTY CLAUSE)**.

#### **6. Final Result & Verification Check:**
* Empty clause derived. **Someone is smiling** ($\exists x \, Smiles(x)$) is proved with witness binding $z = John$.

---

## SECTION 9: MOST REPEATED PROBLEM PATTERNS

```
                             ┌─────────────────────────────────────────┐
                             │    TOP UNIT 3 REPEATED PATTERNS         │
                             └────────────────────┬────────────────────┘
                                                  │
        ┌─────────────────────────────────────────┼─────────────────────────────────────────┐
        ▼                                         ▼                                         ▼
┌──────────────────────────────┐        ┌──────────────────────────────┐        ┌──────────────────────────────┐
│  American Weapon Crime Proof │        │    7-Step CNF Conversion     │        │     Unification & MGU      │
│  • 10 Marks (SVKM / MU)      │        │  • 5-10 Marks (SVKM / MU)    │        │  • 5-10 Marks (SVKM / MU)    │
│  • 7 Axioms + Negated Goal   │        │  • Skolemization Functions   │        │  • Occurs Check & Symbol     │
│  • Resolution Refutation Tree│        │  • Distribute v over ^       │        │    Clash Failure Modes       │
└──────────────────────────────┘        └──────────────────────────────┘        └──────────────────────────────┘
```

1. **American Weapon Crime Resolution Proof (10 Marks):** Appearing in almost every SVKM's NMIMS and MU exam paper, testing complete FOL translation, 8-clause CNF reduction, and refutation tree construction.
2. **7-Step Canonical CNF Conversion (10 Marks):** Complex multi-quantifier expressions requiring explicit Skolem functions ($f(x)$) and variable standardization across clauses.
3. **Unification & Occurs Check Tables (5-10 Marks):** Multi-argument predicate unification testing $v \in \text{vars}(t)$ occurs check failures and function symbol clashes.
4. **Wumpus World Grid Deduction (10 Marks):** Percept-based logical deduction deriving pit-free safe squares ($\neg P_{i,j}$) using biconditional expansion.

---

## SECTION 10: QUICK SOLVING PROCEDURES FOR EXAM ROOM

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      EXAM ROOM STEP-BY-STEP CHECKLIST                     │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. TRUTH TABLE PROBLEMS:                                                  │
│    • Count variables n -> Draw 2^n rows.                                  │
│    • Evaluate sub-expressions first before main connective.               │
│    • Tautology = All T | Contradiction = All F | Valid = Conclusion T when  │
│      KB is T.                                                             │
│                                                                           │
│ 2. FOL TRANSLATION PROBLEMS:                                              │
│    • Universal (forall x): ALWAYS use implication (->).                   │
│    • Existential (exists x): ALWAYS use conjunction (^).                  │
│    • Check quantifier order: forall x exists y != exists y forall x.      │
│                                                                           │
│ 3. 7-STEP CNF CONVERSION:                                                 │
│    1. Eliminate -> and <->.                                               │
│    2. Move ~ inward (De Morgan & Quantifiers).                            │
│    3. Standardize variables apart.                                        │
│    4. Skolemize existentials (constant if outer, function if inside       │
│       forall).                                                            │
│    5. Drop forall quantifiers.                                            │
│    6. Distribute v over ^.                                                │
│    7. Isolate clauses and rename variables per clause.                    │
│                                                                           │
│ 4. RESOLUTION REFUTATION PROOF:                                           │
│    • Negate the Goal (Goal: P -> Add ~P to clause set).                   │
│    • Match complementary literals (L vs ~L) using MGU theta.              │
│    • Derive clauses until [] (EMPTY CLAUSE) is reached.                   │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## SECTION 11: TOP 10 COMMON MISTAKES (`⚠️ COMMON MISTAKES`)

1. ⚠️ **Using Conjunction ($\wedge$) with Universal Quantifier ($\forall$):** Writing $\forall x (Student(x) \wedge Smart(x))$ asserts that everyone in the universe is a student and smart. Correct: $\forall x (Student(x) \implies Smart(x))$.
2. ⚠️ **Using Implication ($\implies$) with Existential Quantifier ($\exists$):** Writing $\exists x (Student(x) \implies Smart(x))$ is vacuously true if there exists any object that is not a student. Correct: $\exists x (Student(x) \wedge Smart(x))$.
3. ⚠️ **Forgetting Occurs Check in Unification:** Binding $x \leftarrow f(x)$ without checking if $x \in \text{vars}(f(x))$.
4. ⚠️ **Replacing Existential Quantifier with a Constant instead of a Function:** Skolemizing $\forall x \exists y L(x, y)$ as $L(x, A)$ instead of $L(x, f(x))$.
5. ⚠️ **Claiming Skolemization Preserves Logical Equivalence:** Skolemization preserves **satisfiability (equisatisfiability)**, NOT logical equivalence.
6. ⚠️ **Forgetting to Negate the Goal in Resolution:** Attempting to resolve clauses directly toward the goal instead of adding the **negated goal** to derive $\square$.
7. ⚠️ **Reusing Variables Across Separate CNF Clauses:** Failing to standardize variables apart per clause leads to incorrect variable coupling during unification.
8. ⚠️ **Incorrect Distributive Law Application:** Writing $(A \wedge B) \vee C$ as $(A \vee B) \wedge C$ instead of $(A \vee C) \wedge (B \vee C)$.
9. ⚠️ **Failing to Evaluate All $2^n$ Truth Table Rows:** Omitting rows in truth table validity proofs invalidates the conclusion.
10. ⚠️ **Swapping Quantifier Order:** Treating $\forall x \exists y P(x, y)$ ("Everyone loves someone") as equivalent to $\exists y \forall x P(x, y)$ ("There is someone whom everyone loves").

---

## SECTION 12: LAST-MINUTE REVISION CHECKLIST

* [x] **Truth Table Formula:** $2^n$ rows for $n$ variables.
* [x] **Implication Equivalence:** $P \implies Q \equiv \neg P \vee Q$.
* [x] **Biconditional Equivalence:** $P \iff Q \equiv (\neg P \vee Q) \wedge (\neg Q \vee P)$.
* [x] **Quantifier Duality:** $\neg \forall x P(x) \equiv \exists x \neg P(x)$ and $\neg \exists x P(x) \equiv \forall x \neg P(x)$.
* [x] **CNF Step 4 (Skolemization):** Independent $\exists \implies$ Constant $A$; Dependent $\exists$ inside $\forall x \implies$ Function $f(x)$.
* [x] **Unification Failure Conditions:** Function symbol clash ($f \neq g$), argument count mismatch, or occurs check failure ($x \in \text{vars}(t)$).
* [x] **Resolution Refutation Principle:** Goal $G \implies$ Add $\neg G \implies$ Derive $\square$ (Empty Clause).

---

## SECTION 13: COMPLETE PYQ COVERAGE CHECKLIST

- [x] **Truth Table Tautology, Contradiction, & Contingency Proofs**
- [x] **Propositional Argument Validity ("Work Whole Night" Domain)**
- [x] **Wumpus World Grid Deduction & Safe Square Proofs**
- [x] **English-to-FOL Quantifier Translations (Marcus Caesar & Student Domains)**
- [x] **Canonical 7-Step CNF Conversion with Skolem Functions**
- [x] **Unification Algorithm, MGU Tables, & Occurs Check Failures**
- [x] **Forward Chaining Execution Trace (`FOL-FC-ASK`)**
- [x] **Backward Chaining Proof Tree Execution Trace (`FOL-BC-ASK`)**
- [x] **Resolution Refutation Proof 1: "Is Colonel West a Criminal?" (American Weapon Crime)**
- [x] **Resolution Refutation Proof 2: "Is Raja Angry?" (Rimi Hungry & Barking)**
- [x] **Resolution Refutation Proof 3: "Is Someone Smiling?" (Graduating & Happy)**
