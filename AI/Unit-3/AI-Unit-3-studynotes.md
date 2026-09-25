# ARTIFICIAL INTELLIGENCE (AI) STUDY NOTES
## UNIT 3: KNOWLEDGE REPRESENTATION & REASONING
### Course Code: 702CO0C076 | B.Tech Computer Engineering (SVKM's NMIMS MPSTME / University Pattern)

---

## UNIT OVERVIEW

Knowledge Representation and Reasoning (KRR) is a foundational subfield of Artificial Intelligence focused on designing formal, mathematically precise languages to encode an agent's knowledge about the world, along with algorithmic mechanisms to draw sound logical conclusions from that knowledge. 

While classical search techniques (Unit 1 and Unit 2) navigate explicit state spaces or game trees, **knowledge-based agents** maintain an internal **Knowledge Base (KB)** containing sentences expressed in formal logic. This unit covers the full spectrum of symbolic logic representations:
1. **Propositional Logic (PL):** Syntax, semantics, truth tables, tautologies, model checking, and the Wumpus World environment.
2. **First-Order Logic (FOL / Predicate Logic):** Predicates, constants, variables, functions, quantifiers ($\forall, \exists$), quantifier scope, and English-to-FOL translations.
3. **Conjunctive Normal Form (CNF) Conversion:** The canonical 7-step transformation procedure from FOL formulas to clausal form.
4. **Unification:** Substitutions, Most General Unifier (MGU), failure conditions, and the Occurs Check.
5. **Inference Algorithms:** Forward Chaining (data-driven), Backward Chaining (goal-driven), and Resolution Refutation (proof by contradiction).

---

## SECTION 1: PROPOSITIONAL LOGIC (PL)

### 1.1 Knowledge-Based Agents & Logic Fundamentals

An intelligent agent requires more than raw data; it requires **knowledge** represented in a structured format that enables automated reasoning.

```
                           ┌─────────────────────────────────────┐
                           │        KNOWLEDGE-BASED AGENT        │
                           └──────────────────┬──────────────────┘
                                              │
                     ┌────────────────────────┴────────────────────────┐
                     ▼                                                 ▼
      ┌─────────────────────────────┐                   ┌─────────────────────────────┐
      │   Knowledge Base (KB)       │                   │      Inference Engine       │
      │   Domain-specific sentences │                   │ Domain-independent rules     │
      │   expressed in formal logic │                   │  (Modus Ponens, Resolution) │
      └─────────────────────────────┘                   └─────────────────────────────┘
```

#### **Core Terminology:**
* **Knowledge Base (KB):** A set of sentences expressed in a formal representation language. Each sentence represents an assertion about the world.
* **Sentence:** A syntactically well-formed formula in a logic language.
* **Syntax:** The formal rules specifying which combinations of symbols constitute valid sentences.
* **Semantics:** The set of rules defining the truth or meaning of sentences with respect to a **model** (a possible world assignment).
* **Model ($m$):** A mathematical abstraction representing a possible world state that assigns a truth value ($\text{True}$ or $\text{False}$) to every proposition symbol.
* **Entailment ($\text{KB} \models \alpha$):** Sentence $\alpha$ is logically entailed by $\text{KB}$ if and only if $\alpha$ is true in *every* model where $\text{KB}$ is true.
  $$\text{KB} \models \alpha \iff M(\text{KB}) \subseteq M(\alpha)$$
* **Inference ($\text{KB} \vdash_i \alpha$):** The process of deriving a new sentence $\alpha$ from $\text{KB}$ using an algorithm or proof procedure $i$.
* **Soundness:** An inference algorithm $i$ is **sound** if it derives only entailed sentences ($\text{KB} \vdash_i \alpha \implies \text{KB} \models \alpha$). No false conclusions are generated.
* **Completeness:** An inference algorithm $i$ is **complete** if it can derive *every* sentence that is entailed ($\text{KB} \models \alpha \implies \text{KB} \vdash_i \alpha$).

---

### 1.2 Syntax and Semantics of Propositional Logic

Propositional Logic (also called Boolean Logic or Propositional Calculus) is the simplest formal logic language.

#### **1. Syntax:**
* **Atomic Sentences:** Consist of a single proposition symbol (e.g., $P, Q, R, P_{1,2}$). Each symbol represents a proposition that can be either $\text{True}$ or $\text{False}$.
* **Complex Sentences:** Constructed from atomic sentences combined with parentheses and the **5 logical connectives**:

| Connective Name | Symbolic Notation | Technical Name | Meaning / Equivalent |
| :--- | :---: | :--- | :--- |
| **Negation** | $\neg P$ or $\sim P$ | NOT | Not $P$ |
| **Conjunction** | $P \wedge Q$ | AND | Both $P$ and $Q$ are True |
| **Disjunction** | $P \vee Q$ | OR | At least one of $P$ or $Q$ is True |
| **Implication** | $P \implies Q$ or $P \rightarrow Q$ | Conditional / IF-THEN | If $P$ is True, then $Q$ is True |
| **Biconditional** | $P \iff Q$ or $P \leftrightarrow Q$ | Equivalence / IF AND ONLY IF | $P$ and $Q$ have identical truth values |

#### **2. Complete Truth Table for Logical Connectives:**

| $P$ | $Q$ | $\neg P$ | $P \wedge Q$ | $P \vee Q$ | $P \implies Q$ | $P \iff Q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **False** | **False** | True | False | False | **True** | **True** |
| **False** | **True** | True | False | True | **True** | False |
| **True** | **False** | False | False | True | **False** | False |
| **True** | **True** | False | True | True | **True** | **True** |

> `⭐ MUST REMEMBER`: $P \implies Q$ is **False ONLY when $P$ is True and $Q$ is False**. If $P$ is False, $P \implies Q$ is **vacuously True** regardless of $Q$.

#### **3. Classifications of Sentences:**
* **Tautology (Valid Sentence):** A sentence that is $\text{True}$ in **all possible models** (e.g., $P \vee \neg P$).
* **Contradiction (Unsatisfiable Sentence):** A sentence that is $\text{False}$ in **all possible models** (e.g., $P \wedge \neg P$).
* **Satisfiable Sentence:** A sentence that is $\text{True}$ in **at least one model** (e.g., $P \vee Q$).

---

### 1.3 Establishing Meaning & Validity via Truth Tables

To check whether a Knowledge Base entails a sentence $\alpha$ ($\text{KB} \models \alpha$) using model checking:
1. Identify all $n$ proposition symbols appearing in $\text{KB}$ and $\alpha$.
2. Construct a truth table with $2^n$ rows representing all possible models.
3. Evaluate the truth value of every sentence in $\text{KB}$ and the target query $\alpha$ for each row.
4. Verify that in **every row where $\text{KB}$ is True**, $\alpha$ is also **True**. If so, $\text{KB} \models \alpha$.

#### **Model Checking Truth Table Example:**
For 3 proposition symbols $P_{1,1}, P_{1,2}, P_{2,1}$, there are $2^3 = 8$ models:

```
Models (2^n = 8) ───► Evaluate KB ───► Filter models where KB == True ───► Check if Query α == True in all filtered models
```

---

### 1.4 The Wumpus World Environment

The **Wumpus World** is the standard benchmark environment used in AI textbooks (Russell & Norvig) to illustrate logical agents.

```
┌───────┬───────┬───────┬───────┐
│ 1,4   │ 2,4   │ 3,4   │ 4,4   │
├───────┼───────┼───────┼───────┤
│ 1,3   │ 2,3   │ 3,3   │ 4,3   │
│ W!    │       │       │       │
├───────┼───────┼───────┼───────┤
│ 1,2   │ 2,2   │ 3,2   │ 4,2   │
│ A     │       │       │       │
│ S, OK │ OK    │       │       │
├───────┼───────┼───────┼───────┤
│ 1,1   │ 2,1   │ 3,1   │ 4,1   │
│ V, OK │ B, V  │ P!    │       │
└───────┴───────┴───────┴───────┘
```

#### **PEAS Description of Wumpus World:**
* **Performance Measure:** $+1000$ for picking up gold, $-1000$ for falling into a pit or being eaten by Wumpus, $-1$ per action taken, $-10$ for shooting arrow.
* **Environment:** $4 \times 4$ grid of rooms. Agent starts at $[1,1]$ facing Right. Gold and Wumpus are placed randomly. Pits are placed in each cell with probability $0.2$.
* **Actuators:** `Forward`, `TurnLeft`, `TurnRight`, `Grab`, `Shoot`, `Climb`.
* **Sensors:**
  * **Stench:** Perceived in squares directly adjacent to the Wumpus.
  * **Breeze:** Perceived in squares directly adjacent to a Pit.
  * **Glitter:** Perceived in the square where Gold is located.
  * **Bump:** Perceived when bumping into a wall.
  * **Scream:** Perceived when Wumpus is killed.

#### **Propositional Representation Symbols:**
* $P_{i,j}$: True if square $[i,j]$ contains a **Pit**.
* $B_{i,j}$: True if square $[i,j]$ contains a **Breeze**.
* $W_{i,j}$: True if square $[i,j]$ contains a **Wumpus**.
* $S_{i,j}$: True if square $[i,j]$ contains a **Stench**.

#### **Immutable Rules in Knowledge Base ($\text{KB}$):**
* $R_1: \neg P_{1,1}$ (Start square has no pit)
* $R_2: B_{1,1} \iff (P_{1,2} \vee P_{2,1})$ (Breeze at $[1,1]$ iff pit at $[1,2]$ or $[2,1]$)
* $R_3: B_{2,1} \iff (P_{1,1} \vee P_{2,2} \vee P_{3,1})$ (Breeze at $[2,1]$ iff pit adjacent)
* $R_4: S_{1,1} \iff (W_{1,2} \vee W_{2,1})$ (Stench at $[1,1]$ iff Wumpus adjacent)

#### **Step-by-Step Wumpus Reasoning Example:**
1. **Percept at $[1,1]$:** No breeze, no stench ($\neg B_{1,1}, \neg S_{1,1}$).
2. **Apply $R_2$:** Since $\neg B_{1,1}$ is True, $P_{1,2} \vee P_{2,1}$ must be False $\implies \neg P_{1,2} \wedge \neg P_{2,1}$. Squares $[1,2]$ and $[2,1]$ are **Safe (OK)**.
3. **Agent moves to $[2,1]$:** Perceives a Breeze ($B_{2,1}$).
4. **Apply $R_3$:** $B_{2,1} \implies (P_{1,1} \vee P_{2,2} \vee P_{3,1})$. Since $P_{1,1}$ is False ($\neg P_{1,1}$), pit is either at $[2,2]$ or $[3,1]$.
5. **Agent backtracks to $[1,1]$ and moves to $[1,2]$:** Perceives a Stench ($S_{1,2}$), but NO Breeze ($\neg B_{1,2}$).
6. **Inference:** Since $\neg B_{1,2}$, square $[2,2]$ CANNOT have a pit. Therefore, the pit MUST be at **$[3,1]$** ($P_{3,1}$ is True)! Furthermore, since $S_{1,2}$ is True and $[1,1]$ had no stench, the Wumpus MUST be at **$[1,3]$** ($W_{1,3}$ is True)!

#### **Limitations of Propositional Logic:**
1. **Lack of Variables / Generality:** Cannot write a single general rule like *"Pits cause breezes in adjacent squares"*. Instead, we must write a separate rule for every single square on the $4 \times 4$ board (e.g., $R_2, R_3, R_4 \dots$).
2. **Combinatorial Explosion:** For a $10 \times 10$ board, hundreds of propositional rules are required.
3. **Handling Change over Time:** Representing temporal states requires creating duplicate symbols for every time step ($P_{i,j}^t$), causing massive KB growth.

---

## SECTION 2: FIRST-ORDER LOGIC (FOL / PREDICATE LOGIC)

### 2.1 Syntax and Semantics of FOL

First-Order Logic (FOL) extends Propositional Logic by adopting an ontology of **Objects, Relations, and Functions**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                      FIRST-ORDER LOGIC SYNTAX                          │
├──────────────────┬─────────────────────────────────────────────────────┤
│ Terminology      │ Elements & Examples                                 │
├──────────────────┼─────────────────────────────────────────────────────┤
│ Constants        │ John, Caesar, America, Nono, 2, Apple                │
│ Variables        │ x, y, z, w                                          │
│ Functions        │ Mother(x), Plus(x, y), FatherOf(John)               │
│ Predicates       │ King(x), Loves(x, y), GreaterThan(x, y), Criminal(x)│
│ Quantifiers      │ Universal (∀), Existential (∃)                      │
│ Connectives      │ ¬, ∧, ∨, ⇒, ⇔                                       │
└──────────────────┴─────────────────────────────────────────────────────┘
```

#### **1. Terms & Atomic Sentences:**
* **Term:** A logical expression referring to an object. Can be a constant, variable, or $k$-ary function applied to terms (e.g., $\text{Mother}(\text{John})$).
* **Atomic Sentence:** Formed by a predicate symbol applied to terms (e.g., $\text{Loves}(\text{John}, \text{Mother}(\text{John}))$ or $\text{Brother}(\text{Richard}, \text{John})$).

#### **2. Quantifiers & Their Semantics:**

##### **A. Universal Quantifier ($\forall x$):**
* Means *"for all $x$"* or *"for every object $x$ in the domain"*.
* $ \forall x \, P(x) $ is True if $P(x)$ is True for *every* object $x$ in the model.
* `⭐ MUST REMEMBER`: The main connective used with $\forall$ is **Implication ($\implies$)**.

##### **B. Existential Quantifier ($\exists x$):**
* Means *"there exists an $x$"* or *"for at least one object $x$ in the domain"*.
* $ \exists x \, P(x) $ is True if $P(x)$ is True for *at least one* object $x$ in the model.
* `⭐ MUST REMEMBER`: The main connective used with $\exists$ is **Conjunction ($\wedge$)**.

---

### 2.2 Quantifier Scope & Duality

#### **Quantifier Duality (De Morgan's Laws for Quantifiers):**
Universal and Existential quantifiers are mathematical duals. Negating a quantified expression swaps the quantifier and moves negation inside:

1. $\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$ ("Not everyone likes spinach $\iff$ Someone dislikes spinach")
2. $\neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$ ("There is no one who likes poison $\iff$ Everyone dislikes poison")
3. $\forall x \, P(x) \equiv \neg \exists x \, \neg P(x)$
4. $\exists x \, P(x) \equiv \neg \forall x \, \neg P(x)$

---

### 2.3 English-to-FOL Translation Rules & Worked Examples

```
┌────────────────────────────────────────────────────────────────────────┐
│                      COMMON TRANSLATION PATTERNS                       │
├─────────────────────────────────────┬──────────────────────────────────┤
│ English Sentence Pattern            │ FOL Formula Structure            │
├─────────────────────────────────────┼──────────────────────────────────┤
│ "Every A is a B"                    │ ∀x (A(x) ⇒ B(x))                 │
│ "Some A is a B"                     │ ∃x (A(x) ∧ B(x))                 │
│ "No A is a B"                       │ ∀x (A(x) ⇒ ¬B(x)) or ¬∃x (A(x) ∧ B(x))│
│ "Only A are B"                      │ ∀x (B(x) ⇒ A(x))                 │
└─────────────────────────────────────┴──────────────────────────────────┘
```

#### ⚠️ **Common Translation Errors (`⚠️ COMMON MISTAKES`):**

1. **Using $\implies$ with $\exists$:**
   * ❌ *Incorrect:* $\exists x \, (\text{Person}(x) \implies \text{Smart}(x))$
   * *Why it's wrong:* This sentence is vacuously True if there exists ANY object in the universe that is NOT a Person (e.g., a chair)!
   * ✅ *Correct:* $\exists x \, (\text{Person}(x) \wedge \text{Smart}(x))$ ("There exists a person who is smart").

2. **Using $\wedge$ with $\forall$:**
   * ❌ *Incorrect:* $\forall x \, (\text{Person}(x) \wedge \text{Smart}(x))$
   * *Why it's wrong:* This asserts that EVERY object in the entire universe is both a Person AND Smart!
   * ✅ *Correct:* $\forall x \, (\text{Person}(x) \implies \text{Smart}(x))$ ("Every person is smart").

---

#### **Comprehensive University Exam Translation Examples:**

##### **Example 1: The Marcus & Caesar Domain**
*(Source: Lab Exp 4 / University Past Papers)*
1. *"Marcus was a man."*
   $$\text{man}(\text{marcus})$$
2. *"Marcus was a Roman."*
   $$\text{roman}(\text{marcus})$$
3. *"All men are people."*
   $$\forall x \, (\text{man}(x) \implies \text{person}(x))$$
4. *"Caesar was a ruler."*
   $$\text{ruler}(\text{caesar})$$
5. *"All Romans were either loyal to Caesar or hated him."*
   $$\forall x \, (\text{roman}(x) \implies (\text{loyal}(x, \text{caesar}) \vee \text{hate}(x, \text{caesar})))$$
6. *"Everyone is loyal to someone."*
   $$\forall x \exists y \, \text{loyal}(x, y)$$
7. *"People only try to assassinate rulers they are not loyal to."*
   $$\forall x \forall y \, ((\text{person}(x) \wedge \text{ruler}(y) \wedge \text{tryassassinate}(x, y)) \implies \neg \text{loyal}(x, y))$$
8. *"Marcus tried to assassinate Caesar."*
   $$\text{tryassassinate}(\text{marcus}, \text{caesar})$$

##### **Example 2: American Weapon Crime Domain**
*(Source: SVKM's NMIMS Final Exam 2024-25 / MU Dec 15 [10 Marks])*
1. *"It is a crime for an American to sell weapons to hostile nations."*
   $$\forall x \forall y \forall z \forall w \, ((\text{American}(x) \wedge \text{Weapon}(y) \wedge \text{Sells}(x, y, z) \wedge \text{Hostile}(z)) \implies \text{Criminal}(x))$$
2. *"Country Nono has some missiles."*
   $$\exists x \, (\text{Owns}(\text{Nono}, x) \wedge \text{Missile}(x))$$
3. *"All of its missiles were sold to Nono by Colonel West."*
   $$\forall x \, ((\text{Missile}(x) \wedge \text{Owns}(\text{Nono}, x)) \implies \text{Sells}(\text{West}, x, \text{Nono}))$$
4. *"Missiles are weapons."*
   $$\forall x \, (\text{Missile}(x) \implies \text{Weapon}(x))$$
5. *"An enemy of America is known as hostile."*
   $$\forall x \, (\text{Enemy}(x, \text{America}) \implies \text{Hostile}(x))$$
6. *"West is an American."*
   $$\text{American}(\text{West})$$
7. *"Nono is an enemy of America."*
   $$\text{Enemy}(\text{Nono}, \text{America})$$

---

## SECTION 3: CONJUNCTIVE NORMAL FORM (CNF) CONVERSION

To enable automated theorem proving via **Resolution Refutation**, all First-Order Logic formulas must be transformed into **Conjunctive Normal Form (CNF)** (also called **Clausal Form**).

### 3.1 Definition of CNF
* **Literal:** An atomic predicate or its negation (e.g., $P(x)$ or $\neg P(x)$).
* **Clause:** A disjunction ($\vee$) of literals (e.g., $\neg \text{Man}(x) \vee \text{Person}(x)$).
* **CNF Formula:** A conjunction ($\wedge$) of clauses.

$$\text{CNF Formula} = C_1 \wedge C_2 \wedge C_3 \dots \wedge C_k = \bigwedge_{i=1}^k \left( \bigvee_{j=1}^{m_i} L_{i,j} \right)$$

---

### 3.2 The Ordered 7-Step Algorithm for FOL to CNF

```
┌────────────────────────────────────────────────────────────────────────┐
│                   7-STEP FOL TO CNF CONVERSION FLOW                    │
├──────┬────────────────────────────┬────────────────────────────────────┤
│ Step │ Operation Description      │ Substitution Equivalence Rules     │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  1   │ Eliminate Implications     │ A ⇒ B ≡ ¬A ∨ B                     │
│      │ and Biconditionals         │ A ⇔ B ≡ (¬A ∨ B) ∧ (¬B ∨ A)        │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  2   │ Move Negation (¬) Inward   │ ¬(A ∧ B) ≡ ¬A ∨ ¬B                 │
│      │ (De Morgan's Laws)         │ ¬(A ∨ B) ≡ ¬A ∧ ¬B                 │
│      │                            │ ¬∀x P(x) ≡ ∃x ¬P(x)                │
│      │                            │ ¬∃x P(x) ≡ ∀x ¬P(x)                │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  3   │ Standardize Variables      │ Rename duplicate variable names    │
│      │                            │ across different quantifiers       │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  4   │ Skolemize (Eliminate ∃)    │ ∃x P(x) ──► P(A) (Skolem Constant) │
│      │                            │ ∀x ∃y P(x,y) ──► P(x, F(x))        │
│      │                            │ (Skolem Function)                  │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  5   │ Drop Universal Quantifiers │ Move all ∀ to prefix & drop symbol │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  6   │ Distribute ∨ over ∧        │ A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)    │
├──────┼────────────────────────────┼────────────────────────────────────┤
│  7   │ Isolate Clauses            │ Separate conjunctions into distinct│
│      │                            │ clause sets with new variables     │
└──────┴────────────────────────────┴────────────────────────────────────┘
```

> `🧠 MUST UNDERSTAND`: **Skolemization vs Logical Equivalence:**
> Steps 1, 2, 3, 5, and 6 preserve **strict logical equivalence**. However, Step 4 (Skolemization) preserves **SATISFIABILITY**, NOT strict logical equivalence ($\alpha$ and $\text{Skolem}(\alpha)$ are equisatisfiable).

---

### 3.3 Fully Worked CNF Conversion Examples

#### **Worked Example 1: Classic Textbook Sentence**
*(Source: Russell & Norvig AIMA 4th Ed / University Paper)*

**Sentence:** *"Everyone who loves all animals is loved by someone."*
$$\forall x \, [\forall y \, (\text{Animal}(y) \implies \text{Loves}(x, y)) \implies \exists y \, \text{Loves}(y, x)]$$

##### **Step 1: Eliminate Implications ($\implies$)**
Apply $A \implies B \equiv \neg A \vee B$ twice:
1. Inner implication: $\forall y \, (\text{Animal}(y) \implies \text{Loves}(x, y)) \equiv \forall y \, (\neg \text{Animal}(y) \vee \text{Loves}(x, y))$
2. Outer implication:
   $$\forall x \, [\neg (\forall y \, (\neg \text{Animal}(y) \vee \text{Loves}(x, y))) \vee \exists y \, \text{Loves}(y, x)]$$

##### **Step 2: Move Negation ($\neg$) Inward**
1. Move $\neg$ across quantifier $\forall y$: $\neg \forall y \, P(y) \equiv \exists y \, \neg P(y)$
   $$\forall x \, [\exists y \, \neg (\neg \text{Animal}(y) \vee \text{Loves}(x, y)) \vee \exists y \, \text{Loves}(y, x)]$$
2. Apply De Morgan's Law $\neg (A \vee B) \equiv \neg A \wedge \neg B$ and double negation:
   $$\forall x \, [\exists y \, (\text{Animal}(y) \wedge \neg \text{Loves}(x, y)) \vee \exists y \, \text{Loves}(y, x)]$$

##### **Step 3: Standardize Variables Apart**
Notice that $y$ is used in two different existential quantifiers. Rename the second $y$ to $z$:
$$\forall x \, [\exists y \, (\text{Animal}(y) \wedge \neg \text{Loves}(x, y)) \vee \exists z \, \text{Loves}(z, x)]$$

##### **Step 4: Skolemize (Eliminate Existential Quantifiers $\exists$)**
* $\exists y$ is within the scope of universal quantifier $\forall x$. Replace $y$ with Skolem function $F(x)$.
* $\exists z$ is also within the scope of universal quantifier $\forall x$. Replace $z$ with Skolem function $G(x)$.

$$\forall x \, [(\text{Animal}(F(x)) \wedge \neg \text{Loves}(x, F(x))) \vee \text{Loves}(G(x), x)]$$

##### **Step 5: Drop Universal Quantifiers ($\forall$)**
Drop $\forall x$:
$$(\text{Animal}(F(x)) \wedge \neg \text{Loves}(x, F(x))) \vee \text{Loves}(G(x), x)$$

##### **Step 6: Distribute Disjunction ($\vee$) over Conjunction ($\wedge$)**
Apply $(A \wedge B) \vee C \equiv (A \vee C) \wedge (B \vee C)$:
$$[\text{Animal}(F(x)) \vee \text{Loves}(G(x), x)] \wedge [\neg \text{Loves}(x, F(x)) \vee \text{Loves}(G(x), x)]$$

##### **Step 7: Isolate Clauses & Standardize Variables per Clause**
Separate into two distinct clauses and rename $x$ in Clause 2 to $x_2$:
* **Clause 1:** $\text{Animal}(F(x_1)) \vee \text{Loves}(G(x_1), x_1)$
* **Clause 2:** $\neg \text{Loves}(x_2, F(x_2)) \vee \text{Loves}(G(x_2), x_2)$

---

#### **Worked Example 2: Propositional Logic CNF Conversion**
*(Source: Mumbai University Dec 2015 [4 Marks])*

**Convert the propositional logic statement into CNF:** $A \implies (B \iff C)$

##### **Solution Trace:**
1. **Eliminate Biconditional ($\iff$):**
   $$A \implies ((B \implies C) \wedge (C \implies B))$$
2. **Eliminate Inner Implications ($\implies$):**
   $$A \implies ((\neg B \vee C) \wedge (\neg C \vee B))$$
3. **Eliminate Outer Implication ($\implies$):**
   $$\neg A \vee ((\neg B \vee C) \wedge (\neg C \vee B))$$
4. **Distribute Disjunction ($\vee$) over Conjunction ($\wedge$):**
   Apply $X \vee (Y \wedge Z) \equiv (X \vee Y) \wedge (X \vee Z)$ where $X = \neg A$:
   $$(\neg A \vee \neg B \vee C) \wedge (\neg A \vee \neg C \vee B)$$
5. **Final CNF Clauses:**
   * **Clause 1:** $\neg A \vee \neg B \vee C$
   * **Clause 2:** $\neg A \vee \neg C \vee B$

---

## SECTION 4: UNIFICATION

### 4.1 Concept and Purpose of Unification

In First-Order Logic, inference rules like Generalized Modus Ponens require matching atomic sentences containing variables. **Unification** is the algorithmic procedure of finding a substitution $\theta$ that makes two logical expressions syntactically identical.

* **Substitution ($\theta$):** A set of variable bindings written as:
  $$\theta = \{ t_1 / v_1, t_2 / v_2, \dots, t_k / v_k \}$$
  which means variable $v_i$ is replaced by term $t_i$.
* **Unifier:** A substitution $\theta$ is a unifier for expressions $\alpha$ and $\beta$ if:
  $$\alpha \theta = \beta \theta$$

---

### 4.2 Most General Unifier (MGU)

For any unifiable pair of expressions, there can be multiple unifiers. The **Most General Unifier (MGU)** is the unique substitution (up to variable renaming) that places the **fewest constraints** on the variables.

#### **MGU Comparison Example:**
Unify $P(\text{John}, x)$ and $P(y, z)$:
* **Unifier 1 ($\theta_1$):** $\{ \text{John}/y, \text{John}/x, \text{John}/z \} \implies P(\text{John}, \text{John})$ (Too specific!)
* **Unifier 2 ($\theta_2$ - MGU):** $\{ \text{John}/y, z/x \} \implies P(\text{John}, z)$ (**Most General!**)

---

### 4.3 Unification Failures & The Occurs Check

Unification returns **`FAIL`** under 4 distinct structural mismatch conditions:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      UNIFICATION FAILURE CONDITIONS                    │
├───────────────────────────────┬────────────────────────────────────────┤
│ Failure Condition             │ Concrete Example                       │
├───────────────────────────────┼────────────────────────────────────────┤
│ 1. Predicate Symbol Mismatch  │ King(x) vs Queen(y)                    │
│ 2. Arity (Argument Count) Diff│ P(x, y) vs P(z)                        │
│ 3. Constant Mismatch          │ Knows(John, x) vs Knows(Jane, y)       │
│ 4. Occurs Check Failure       │ Unify variable x with term f(x)        │
└───────────────────────────────┴────────────────────────────────────────┘
```

#### 🧠 **The Occurs Check:**
When attempting to unify a variable $x$ with a complex term $t$, the algorithm must check whether $x$ **occurs inside $t$**. If $x$ occurs in $t$, unification MUST fail.
* **Example:** Unify $x$ with $S(x)$ or $f(x)$.
* If permitted, this creates an infinite circular structure $x = f(f(f(\dots)))$, leading to non-termination in theorem provers.

---

### 4.4 Unification Algorithm & Step-by-Step Examples

#### **Complete Unification Pseudocode:**

```python
function UNIFY(x, y, theta) returns a substitution or failure
    inputs: x, a variable, constant, list, or compound expression
            y, a variable, constant, list, or compound expression
            theta, the substitution built up so far (default: empty {})

    if theta == failure then return failure
    else if x == y then return theta
    else if VARIABLE?(x) then return UNIFY-VAR(x, y, theta)
    else if VARIABLE?(y) then return UNIFY-VAR(y, x, theta)
    else if COMPOUND?(x) and COMPOUND?(y) then
        return UNIFY(ARGS[x], ARGS[y], UNIFY(OP[x], OP[y], theta))
    else if LIST?(x) and LIST?(y) then
        return UNIFY(REST[x], REST[y], UNIFY(FIRST[x], FIRST[y], theta))
    else return failure

function UNIFY-VAR(var, x, theta) returns a substitution
    if {var/val} in theta then return UNIFY(val, x, theta)
    else if {x/val} in theta then return UNIFY(var, val, theta)
    else if OCCUR-CHECK?(var, x) then return failure
    else return theta U {x/var}
```

---

#### **Worked Unification Examples Table:**

| Pair No. | Expression 1 ($\alpha$) | Expression 2 ($\beta$) | MGU ($\theta$) | Resulting Unified Expression | Status / Explanation |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **1** | $\text{Knows}(\text{John}, x)$ | $\text{Knows}(\text{John}, \text{Jane})$ | $\{ \text{Jane}/x \}$ | $\text{Knows}(\text{John}, \text{Jane})$ | **Success** |
| **2** | $\text{Knows}(\text{John}, x)$ | $\text{Knows}(y, \text{OJ})$ | $\{ \text{John}/y, \text{OJ}/x \}$ | $\text{Knows}(\text{John}, \text{OJ})$ | **Success** |
| **3** | $\text{Knows}(\text{John}, x)$ | $\text{Knows}(y, \text{Mother}(y))$ | $\{ \text{John}/y, \text{Mother}(\text{John})/x \}$ | $\text{Knows}(\text{John}, \text{Mother}(\text{John}))$ | **Success** |
| **4** | $\text{Knows}(\text{John}, x)$ | $\text{Knows}(x, \text{OJ})$ | — | — | **`FAIL`** (Variable $x$ cannot bind to both $\text{John}$ and $\text{OJ}$. Standardize apart first!) |
| **5** | $P(a, x, y, z)$ | $P(x, y, z, w)$ | $\{ a/x, a/y, a/z, a/w \}$ | $P(a, a, a, a)$ | **Success** (Sequential variable cascade) |

---

## SECTION 5: INFERENCE IN FIRST-ORDER LOGIC

Inference is the process of computing new entailed sentences from a Knowledge Base.

### 5.1 Inference Rules

1. **Generalized Modus Ponens (GMP):**
   For atomic sentences $p_i, p_i', q$ and substitution $\theta$ such that $\text{UNIFY}(p_i, p_i') = \theta$ for all $i$:
   $$\frac{p_1', p_2', \dots, p_n', \quad (p_1 \wedge p_2 \wedge \dots \wedge p_n \implies q)}{q\theta}$$

2. **Unit Resolution:**
   $$\frac{l_1 \vee l_2 \vee \dots \vee l_k, \quad \neg l_1}{l_2 \vee \dots \vee l_k}$$

3. **General First-Order Resolution:**
   $$\frac{l_1 \vee \dots \vee l_k, \quad m_1 \vee \dots \vee m_n}{(l_1 \vee \dots \vee l_{i-1} \vee l_{i+1} \vee \dots \vee l_k \vee m_1 \vee \dots \vee m_{j-1} \vee m_{j+1} \vee \dots \vee m_n)\theta}$$
   where $\text{UNIFY}(l_i, \neg m_j) = \theta$.

---

### 5.2 Forward Chaining (Data-Driven Inference)

* **Concept:** Starts from known facts in the Knowledge Base and repeatedly applies Modus Ponens to derive new facts until the query goal is derived or no new inferences can be made.
* **Property:** Complete for First-Order Definite Clauses (Horn Clauses).

```
Known Facts in KB ───► Match Rule Antecedents ───► Infer Rule Consequent ───► Add to KB ───► Repeat until Goal found
```

#### **Forward Chaining Algorithm (`FOL-FC-ASK`):**

```python
function FOL-FC-ASK(KB, alpha) returns a substitution or false
    inputs: KB, a knowledge base of definite clauses
            alpha, the query, an atomic sentence

    loop until no new sentences are added:
        new = {}
        for each rule (p1 ^ ... ^ pn => q) in KB:
            for each theta such that UNIFY(pi, pi') = theta for all i (where pi' in KB):
                q_prime = SUBST(theta, q)
                if q_prime is not in KB and new:
                    add q_prime to new
                    phi = UNIFY(q_prime, alpha)
                    if phi != failure then return phi
        if new is empty then return false
        add new to KB
```

---

### 5.3 Backward Chaining (Goal-Driven Inference)

* **Concept:** Starts from the query goal $q$, searches for rules in $\text{KB}$ whose head (consequent) unifies with $q$, and recursively attempts to prove all premises of those rules as subgoals.
* **Traversal:** Executes a **Depth-First Search (DFS)** backwards through the rule space.

```
Query Goal (q) ◄─── Find Rule Head matching q ◄─── Generate Subgoals for Premises ◄─── Recurse until Facts hit
```

#### **Backward Chaining Proof Tree (American Weapon Crime Domain):**

```
                             ┌───────────────────────┐
                             │ Criminal(West) [GOAL] │
                             └───────────┬───────────┘
                                         │ Rule 1: {x/West}
            ┌────────────────────────────┼────────────────────────────┐
            │                            │                            │
 ┌──────────┴──────────┐      ┌──────────┴──────────┐      ┌──────────┴──────────┐      ┌──────────┴──────────┐
 │   American(West)    │      │      Weapon(y)      │      │  Sells(West, y, z)  │      │    Hostile(z)       │
 └──────────┬──────────┘      └──────────┬──────────┘      └──────────┬──────────┘      └──────────┬──────────┘
            │ Fact 6                     │ {y/M1}                     │ {z/Nono}                   │ Fact 5: {z/Nono}
        [  TRUE  ]            ┌──────────┴──────────┐      ┌──────────┴──────────┐      ┌──────────┴──────────┐
                              │     Missile(M1)     │      │ Sells(West,M1,Nono) │      │ Enemy(Nono,America) │
                              └──────────┬──────────┘      └──────────┬──────────┘      └──────────┬──────────┘
                                         │ Fact 4                     │ Rule 3                     │ Fact 2
                                     [ TRUE ]               ┌─────────┴─────────┐              [ TRUE ]
                                                            │ Owns(Nono, M1)    │
                                                            └─────────┬─────────┘
                                                                      │ Fact 3
                                                                  [ TRUE ]
```

---

### 5.4 Resolution Refutation (Proof by Contradiction)

Resolution refutation is the primary sound and complete inference technique for First-Order Logic.

#### **Algorithm Steps:**
1. **Negate the Query ($\neg \alpha$):** Add the negated goal sentence to the Knowledge Base.
2. **Convert all KB sentences and $\neg \alpha$ to CNF (Clausal Form).**
3. **Repeatedly Resolve Clauses:** Find pairs of clauses containing complementary literals ($L$ and $\neg L$), unify them using MGU $\theta$, and produce a new resolvent clause.
4. **Termination:**
   * If the **empty clause ($\emptyset$ or falsum)** is derived, a contradiction is reached $\implies$ Query $\alpha$ is **PROVED TRUE**!
   * If no new clauses can be generated, the query cannot be proved.

---

## SECTION 6: SOLVED PAST YEAR QUESTIONS (PYQs) & WORKED PROBLEMS

---

### ✍️ **PYQ 1: "Is Colonel West a Criminal?" (American Weapon Crime)**
*(Source: SVKM's NMIMS B.Tech CE Final Exam 2024-25 / MU Dec 15 [10 Marks])*

#### **Problem Statement:**
Consider the following axioms:
1. It is a crime for an American to sell weapons to hostile nations.
2. Country Nono is an enemy of America.
3. Nono has some missiles.
4. All of its missiles were sold to Nono by Colonel West.
5. Missiles are weapons.
6. An enemy of America is known as hostile.
7. West is an American.

**Task:** Express axioms in FOL, convert to CNF, and prove that **West is a Criminal** using Resolution Refutation.

---

#### **Step-by-Step Solution:**

##### **Step 1: Translate Axioms to FOL**
1. $\forall x \forall y \forall z \forall w \, ((\text{American}(x) \wedge \text{Weapon}(y) \wedge \text{Sells}(x, y, z) \wedge \text{Hostile}(z)) \implies \text{Criminal}(x))$
2. $\text{Enemy}(\text{Nono}, \text{America})$
3. $\exists x \, (\text{Owns}(\text{Nono}, x) \wedge \text{Missile}(x))$
4. $\forall x \, ((\text{Missile}(x) \wedge \text{Owns}(\text{Nono}, x)) \implies \text{Sells}(\text{West}, x, \text{Nono}))$
5. $\forall x \, (\text{Missile}(x) \implies \text{Weapon}(x))$
6. $\forall x \, (\text{Enemy}(x, \text{America}) \implies \text{Hostile}(x))$
7. $\text{American}(\text{West})$

##### **Step 2: Convert FOL Axioms to CNF Clauses**
* **Clause 1:** $\neg \text{American}(x) \vee \neg \text{Weapon}(y) \vee \neg \text{Sells}(x, y, z) \vee \neg \text{Hostile}(z) \vee \text{Criminal}(x)$
* **Clause 2:** $\text{Enemy}(\text{Nono}, \text{America})$
* **Clause 3a:** $\text{Owns}(\text{Nono}, M_1)$ *(Skolem constant $M_1$ for $\exists x$)*
* **Clause 3b:** $\text{Missile}(M_1)$
* **Clause 4:** $\neg \text{Missile}(w) \vee \neg \text{Owns}(\text{Nono}, w) \vee \text{Sells}(\text{West}, w, \text{Nono})$
* **Clause 5:** $\neg \text{Missile}(u) \vee \text{Weapon}(u)$
* **Clause 6:** $\neg \text{Enemy}(v, \text{America}) \vee \text{Hostile}(v)$
* **Clause 7:** $\text{American}(\text{West})$

##### **Step 3: Negate Query Goal**
* **Query Goal:** $\text{Criminal}(\text{West})$
* **Negated Goal (Clause 8):** $\neg \text{Criminal}(\text{West})$

##### **Step 4: Resolution Refutation Proof Trace**

```
[Clause 8: ¬Criminal(West)]              [Clause 1: ¬American(x) ∨ ¬Weapon(y) ∨ ¬Sells(x,y,z) ∨ ¬Hostile(z) ∨ Criminal(x)]
            └─────────────────────────┬──────────────────────────┘
                                      │ Unify {West/x}
                                      ▼
             [Clause 9: ¬American(West) ∨ ¬Weapon(y) ∨ ¬Sells(West,y,z) ∨ ¬Hostile(z)]
            └─────────────────────────┬──────────────────────────┘
                                      │ Resolve with [Clause 7: American(West)]
                                      ▼
                      [Clause 10: ¬Weapon(y) ∨ ¬Sells(West,y,z) ∨ ¬Hostile(z)]
            └─────────────────────────┬──────────────────────────┘
                                      │ Resolve with [Clause 5: ¬Missile(u) ∨ Weapon(u)], Unify {u/y}
                                      ▼
                      [Clause 11: ¬Missile(y) ∨ ¬Sells(West,y,z) ∨ ¬Hostile(z)]
            └─────────────────────────┬──────────────────────────┘
                                      │ Resolve with [Clause 3b: Missile(M1)], Unify {M1/y}
                                      ▼
                              [Clause 12: ¬Sells(West,M1,z) ∨ ¬Hostile(z)]
            └─────────────────────────┬──────────────────────────┘
                                      │ Resolve with [Clause 4: ¬Missile(w) ∨ ¬Owns(Nono,w) ∨ Sells(West,w,Nono)]
                                      │ Unify {M1/w, Nono/z}
                                      ▼
                      [Clause 13: ¬Missile(M1) ∨ ¬Owns(Nono,M1) ∨ ¬Hostile(Nono)]
            └─────────────────────────┬──────────────────────────┘
                                      │ Resolve sequentially with Clause 3b, Clause 3a, Clause 6, Clause 2
                                      ▼
                                  [ EMPTY CLAUSE: ∅ ]  (Contradiction!)
```

**Conclusion:** Deriving the empty clause $\emptyset$ proves that **West is indeed a Criminal**!

---

### ✍️ **PYQ 2: "Is Raja Angry?"**
*(Source: Mumbai University Dec 2015 [10 Marks])*

#### **Problem Statement:**
1. Rimi is hungry.
2. If Rimi is hungry, she barks.
3. If Rimi is barking, then Raja is angry.

**Task:** Express in predicate logic, convert to CNF, and prove that **Raja is angry** using Resolution.

---

#### **Step-by-Step Solution:**

##### **Step 1: Translate to Logic**
1. $\text{Hungry}(\text{Rimi})$
2. $\text{Hungry}(\text{Rimi}) \implies \text{Barks}(\text{Rimi})$
3. $\text{Barks}(\text{Rimi}) \implies \text{Angry}(\text{Raja})$

##### **Step 2: Convert to CNF Clauses**
* **Clause 1:** $\text{Hungry}(\text{Rimi})$
* **Clause 2:** $\neg \text{Hungry}(\text{Rimi}) \vee \text{Barks}(\text{Rimi})$
* **Clause 3:** $\neg \text{Barks}(\text{Rimi}) \vee \text{Angry}(\text{Raja})$

##### **Step 3: Negate Query Goal & Resolve**
* **Negated Goal (Clause 4):** $\neg \text{Angry}(\text{Raja})$

```
    [Clause 4: ¬Angry(Raja)]         [Clause 3: ¬Barks(Rimi) ∨ Angry(Raja)]
               └─────────────────┬─────────────────┘
                                 ▼
                      [Clause 5: ¬Barks(Rimi)]       [Clause 2: ¬Hungry(Rimi) ∨ Barks(Rimi)]
                                 └──────────────┬──────────────┘
                                                ▼
                                     [Clause 6: ¬Hungry(Rimi)]       [Clause 1: Hungry(Rimi)]
                                                └──────────────┬──────────────┘
                                                               ▼
                                                           [  ∅  ]  (Contradiction!)
```

**Conclusion:** Deriving $\emptyset$ proves that **Raja is Angry**!

---

### ✍️ **PYQ 3: "Is Someone Smiling?"**
*(Source: Mumbai University Dec 2015 [12 Marks])*

#### **Problem Statement:**
1. All people who are graduating are happy.
2. All happy people smile.
3. Someone is graduating.

**Task:** Represent in FOL, convert to CNF, and prove that **someone is smiling** using Resolution Refutation. Draw the resolution tree.

---

#### **Step-by-Step Solution:**

##### **Step 1: Convert Axioms to FOL**
1. $\forall x \, (\text{Graduating}(x) \implies \text{Happy}(x))$
2. $\forall x \, (\text{Happy}(x) \implies \text{Smile}(x))$
3. $\exists x \, \text{Graduating}(x)$

##### **Step 2: Convert FOL to CNF Clauses**
* **Clause 1:** $\neg \text{Graduating}(x) \vee \text{Happy}(x)$
* **Clause 2:** $\neg \text{Happy}(y) \vee \text{Smile}(y)$
* **Clause 3:** $\text{Graduating}(A)$ *(Skolem constant $A$ for $\exists x$)*

##### **Step 3: Negate Query Goal**
* **Query:** $\exists x \, \text{Smile}(x)$
* **Negated Query:** $\neg \exists x \, \text{Smile}(x) \equiv \forall x \, \neg \text{Smile}(x)$
* **Clause 4:** $\neg \text{Smile}(z)$

##### **Step 4: Resolution Tree Proof**

```
    [Clause 4: ¬Smile(z)]        [Clause 2: ¬Happy(y) ∨ Smile(y)]
               └───────────┬───────────┘
                           │ Unify {y/z}
                           ▼
               [Clause 5: ¬Happy(y)]        [Clause 1: ¬Graduating(x) ∨ Happy(x)]
                           └───────────┬───────────┘
                                       │ Unify {x/y}
                                       ▼
                          [Clause 6: ¬Graduating(x)]        [Clause 3: Graduating(A)]
                                       └───────────┬───────────┘
                                                   │ Unify {A/x}
                                                   ▼
                                               [  ∅  ]  (Contradiction!)
```

**Conclusion:** Proved! Someone is smiling.

---

## SECTION 7: SUMMARY & FINAL REVISION

### 7.1 Quick Revision Summary
* **Propositional Logic:** Simple truth-functional logic using 5 connectives ($\neg, \wedge, \vee, \implies, \iff$). Incapable of expressing general domain rules across multiple objects.
* **First-Order Logic:** Expressive logic containing Constants, Variables, Functions, Predicates, and Quantifiers ($\forall, \exists$).
* **CNF Conversion:** 7-step process required for resolution: Eliminate Implications $\rightarrow$ Negations Inward $\rightarrow$ Standardize Variables $\rightarrow$ Skolemize $\exists \rightarrow$ Drop $\forall \rightarrow$ Distribute $\vee$ over $\wedge \rightarrow$ Isolate Clauses.
* **Unification:** Finding MGU $\theta$ to make two literals identical. Must execute Occurs Check to prevent infinite terms.
* **Resolution Refutation:** Sound and complete proof technique that negates the goal and derives the empty clause $\emptyset$.

---

### 7.2 Important Definitions
1. **Knowledge Base (KB):** Set of sentences in a formal representation language.
2. **Entailment ($\text{KB} \models \alpha$):** $\alpha$ is True in all models where $\text{KB}$ is True.
3. **Soundness:** Derives only entailed sentences (no false derivations).
4. **Completeness:** Can derive all entailed sentences.
5. **Tautology:** A sentence True in all possible models.
6. **Skolemization:** Process of eliminating $\exists$ by replacing variables with Skolem constants or Skolem functions. Preserves satisfiability.
7. **Most General Unifier (MGU):** The most general substitution that unifies two expressions.
8. **Occurs Check:** Verification step in unification ensuring a variable does not occur within the term it is being unified with.
9. **Forward Chaining:** Data-driven inference starting from facts to derive goals.
10. **Backward Chaining:** Goal-driven inference starting from queries to find supporting facts.

---

### 7.3 Common Exam Pitfalls (`⚠️ COMMON MISTAKES`)
* ❌ **Pitfall 1:** Using $\implies$ with $\exists$ in FOL translations. Always use $\wedge$ with $\exists$.
* ❌ **Pitfall 2:** Using $\wedge$ with $\forall$ in FOL translations. Always use $\implies$ with $\forall$.
* ❌ **Pitfall 3:** Forgetting to negate the query goal when starting a Resolution Refutation proof!
* ❌ **Pitfall 4:** Re-using variable names across clauses when applying Resolution. Always standardize variables apart!
* ❌ **Pitfall 5:** Assuming Skolemization preserves logical equivalence. It only preserves **satisfiability**!

---

### 7.4 Complete Syllabus Coverage Checklist

- [x] **Propositional Logic Syntax & Semantics**
- [x] **5 Logical Connectives & Complete Truth Tables**
- [x] **Tautology, Contradiction, Satisfiability**
- [x] **Wumpus World Formalization & Propositional Proofs**
- [x] **First-Order Logic (FOL) Syntax & Semantics**
- [x] **Quantifiers ($\forall, \exists$), Scope, and Duality**
- [x] **English-to-FOL Translation Rules & Examples**
- [x] **Ordered 7-Step CNF Conversion Procedure**
- [x] **Skolem Constants vs Skolem Functions**
- [x] **Unification Algorithm, MGU, & Occurs Check**
- [x] **Forward Chaining (Data-Driven Inference)**
- [x] **Backward Chaining (Goal-Driven Inference & Proof Trees)**
- [x] **Resolution Refutation (Proof by Contradiction)**
- [x] **Solved Past Year Questions (American Weapon Crime, Rimi Hungry, Graduating Happy)**
