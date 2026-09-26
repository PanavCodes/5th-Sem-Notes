# Operating Systems: Unit 4 — Deadlock Exam-Oriented Numericals Workbook

This workbook provides a comprehensive, fully worked, and exam-oriented collection of **numerical problems and matrix algorithms** for **Unit 4: Deadlock** in Operating Systems. Every problem is presented in standard university examination format, featuring side-by-side snapshot tables, step-by-step matrix derivations, full Work/Finish algorithm execution traces, tentative resource request checks, and explicit discrepancy evaluations.

---

## 📋 Table of Contents
- [1. Document Structure & Source Verification](#1-document-structure-source-verification)
- [2. Source-Status & Verification Audit Matrix](#2-source-status-verification-audit-matrix)
- [3. SECTION I: BANKER'S ALGORITHM SAFETY & REQUEST NUMERICALS](#3-section-i-bankers-algorithm-safety-request-numericals)
  - [Problem 1: Standard 5-Process 3-Resource System (Silberschatz & SVKM NMIMS Final Exam)](#problem-1-standard-5-process-3-resource-system-silberschatz-svkm-nmims-final-exam)
  - [Problem 2: 3-Process 3-Resource System (Lab Manual Exp 7 Problem 1)](#problem-2-3-process-3-resource-system-lab-manual-exp-7-problem-1)
  - [Problem 3: 5-Process 4-Resource System (Lab Manual Exp 7 Problem 3)](#problem-3-5-process-4-resource-system-lab-manual-exp-7-problem-3)
  - [Problem 4: 4-Process 3-Resource System (Textbook / Technical Publications)](#problem-4-4-process-3-resource-system-textbook-technical-publications)
- [4. SECTION II: DEADLOCK DETECTION ALGORITHM NUMERICALS](#4-section-ii-deadlock-detection-algorithm-numericals)
  - [Problem 5: Multi-Instance Resource Deadlock Detection & Request Sensitivity](#problem-5-multi-instance-resource-deadlock-detection-request-sensitivity)
- [5. SECTION III: RESOURCE ALLOCATION GRAPH (RAG) ANALYSES](#5-section-iii-resource-allocation-graph-rag-analyses)
  - [Problem 6: RAG Matrix Conversion & Single vs. Multi-Instance Cycle Analysis](#problem-6-rag-matrix-conversion-single-vs-multi-instance-cycle-analysis)
- [6. SECTION IV: FORMULA RECAP & PRE-EXAM AUDIT CHECKLIST](#6-section-iv-formula-recap-pre-exam-audit-checklist)

---

## 1. Document Structure & Source Verification

To maintain complete academic rigor, every numerical in this workbook is labeled according to its source verification level:
1. **Verified PYQ:** Reserved for exact wording and data checked against an original university exam paper; no problem here is independently confirmed as a verified PYQ.
2. **Lab Exercise (attributed):** Lab-manual names and marks are retained from the supplied workbook, but original manuals were not independently checked.
3. **Textbook-style Example (attributed):** Named textbooks and course notes are source attributions, not proof of identical original wording or exam appearance.
4. **`Practice Question`**: Formulated to ensure complete coverage of edge cases and request evaluations.

---

## 2. Source-Status & Verification Audit Matrix

| Problem ID | Category | Source File / Examination | Verification Status | Primary Concept Tested |
| :--- | :--- | :--- | :---: | :--- |
| **Problem 1** | Banker's Algorithm | SVKM NMIMS Final Exam 2024-2025 (Q4c) / Silberschatz Ch. 8 | Exam attribution unverified | Safety Algorithm, Need Matrix, Resource Request, Source Discrepancy Evaluation |
| **Problem 2** | Banker's Algorithm | Attributed to SVKM NMIMS Lab Manual Exp 7 (Problem 1) | Lab exercise; manual unverified | 3-Process Safety Trace, Work/Finish Execution Sequence |
| **Problem 3** | Banker's Algorithm | Attributed to SVKM NMIMS Lab Manual Exp 7 (Problem 3) | Lab exercise; manual unverified | 4-Resource Type Vector Operations, Safe Sequence Derivation |
| **Problem 4** | Banker's Algorithm | Technical Publications / Course Notes (attributed) | Textbook-style example; source unverified | 4-Process Safety Analysis, Intermediate Work Tracking |
| **Problem 5** | Deadlock Detection | Silberschatz Ch. 8 / Mid-Sem Review (attributed) | Textbook-style example; exam status unverified | Multi-Instance Deadlock Detection Algorithm, Request Sensitivity |
| **Problem 6** | Graph & Matrix | Stallings Ch. 6 / GTU Examination | Reported question; original exam paper unverified | RAG to Matrix Conversion, Cycle vs. Deadlock Sufficiency |

---

## 3. SECTION I: BANKER'S ALGORITHM SAFETY & REQUEST NUMERICALS

### Problem 1: Standard 5-Process 3-Resource System (Silberschatz & SVKM NMIMS Final Exam)

#### Source Metadata & Grouped Questions
- **Question Source (exam attribution unverified):** *SVKM'S NMIMS Semester V Final Exam (2024-2025) [Q4c - 10 Marks] / Silberschatz Textbook (9th/10th Edition Ch. 8).*
- **Unverified variant attributions (wordings not reproduced or checked):** *SVKM'S NMIMS Special Re-Exam (2022-2023) [Q4a - 10 Marks] / GTU Dec 2014 [10 Marks].*

**Attribution note:** Exam year, question number, marks and other named exam variants above are unverified until their original papers are compared. The named variants are not separately transcribed questions. The chapter uses one-based $P_1$ for this workbook's zero-based $P_0$; the chapter's question $(1,0,0)$ and its answer-vector $(1,0,2)$ must be evaluated independently. The already worked zero-based $P_1:(1,0,2)$ case concerns a different process.

#### Question Statement
Consider a system with 5 processes ($P_0$ through $P_4$) and 3 resource types ($A, B, C$). 
Resource $A$ has 10 instances, $B$ has 5 instances, and $C$ has 7 instances.
The snapshot of the system at time $T_0$ is as follows:

```text
Snapshot at time T0:

             Allocation       Max          Available
               A B C         A B C          A B C
    P0         0 1 0         7 5 3          3 3 2
    P1         2 0 0         3 2 2
    P2         3 0 2         9 0 2
    P3         2 1 1         2 2 2
    P4         0 0 2         4 3 3
```

**Sub-Questions:**
1. What is the content of the matrix $\text{Need}$?
2. Is the system in a safe state? Show the complete step-by-step Work/Finish trace and derive a safe sequence.
3. If process $P_1$ requests $(1, 0, 2)$, can the request be granted immediately? Run the safety algorithm on the tentative state.
4. **Source Discrepancy & Sensitivity Analysis:**
   - **Case 4A:** If process $P_4$ requests $(3, 3, 0)$ from the original state $T_0$, can it be granted?
   - **Case 4B:** If process $P_0$ requests $(0, 2, 0)$ *after* $P_1$'s request $(1, 0, 2)$ has been granted, can it be granted?
   - **Source Flag:** In scanned textbook materials (*OS Chap 4 Deadlock.pdf* / Stallings), process indices appear as $P_1..P_5$ instead of $P_0..P_4$, and the question states a request of $(1, 0, 0)$ while the worked solution evaluates $(1, 0, 2)$. Here, $P_1..P_5$ is mapped to $P_0..P_4$ ($P_1 \to P_0, P_2 \to P_1$), and both request vectors are explicitly solved.

---

**Additional chapter sub-questions:** Starting independently from the original snapshot, test (i) source $P_1$ / workbook $P_0$ requesting $(1,0,0)$ and (ii) that same process requesting the chapter answer's changed vector $(1,0,2)$. Keep the separate workbook $P_1:(1,0,2)$ calculation as its own variant.

#### Complete Step-by-Step Solution

##### 1. Total Resource Invariant Verification
Before computing $\text{Need}$, verify that $\text{Total} = \text{Available} + \sum \text{Allocation}$:
$$\sum \text{Allocation}_A = 0 + 2 + 3 + 2 + 0 = 7, \quad \text{Available}_A = 3 \implies \text{Total}_A = 7 + 3 = 10$$
$$\sum \text{Allocation}_B = 1 + 0 + 0 + 1 + 0 = 2, \quad \text{Available}_B = 3 \implies \text{Total}_B = 2 + 3 = 5$$
$$\sum \text{Allocation}_C = 0 + 0 + 2 + 1 + 2 = 5, \quad \text{Available}_C = 2 \implies \text{Total}_C = 5 + 2 = 7$$
The input snapshot is fully consistent with total system resources $(10, 5, 7)$.

---

##### 2. Calculation of Need Matrix ($\text{Need} = \text{Max} - \text{Allocation}$)

For each process $P_i$, calculate $\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$ row by row:

$$\text{Need}[P_0] = (7, 5, 3) - (0, 1, 0) = (7, 4, 3)$$
$$\text{Need}[P_1] = (3, 2, 2) - (2, 0, 0) = (1, 2, 2)$$
$$\text{Need}[P_2] = (9, 0, 2) - (3, 0, 2) = (6, 0, 0)$$
$$\text{Need}[P_3] = (2, 2, 2) - (2, 1, 1) = (0, 1, 1)$$
$$\text{Need}[P_4] = (4, 3, 3) - (0, 0, 2) = (4, 3, 1)$$

```text
Calculated Need Matrix:

               Need
              A B C
    P0        7 4 3
    P1        1 2 2
    P2        6 0 0
    P3        0 1 1
    P4        4 3 1
```

---

##### 3. Safety Algorithm Trace at Time $T_0$

- **Initialization:**
  $$\text{Work} = \text{Available} = (3, 3, 2)$$
  $$\text{Finish} = [\text{False}, \text{False}, \text{False}, \text{False}, \text{False}]$$
  $$\text{Safe Sequence} = \langle \rangle$$

- **Step 1: Evaluate $P_0$**
  - $\text{Need}_0 = (7, 4, 3)$. Check $\text{Need}_0 \le \text{Work} \implies (7, 4, 3) \le (3, 3, 2) \implies$ **FALSE** ($7 > 3$). $P_0$ must wait.

- **Step 2: Evaluate $P_1$**
  - $\text{Need}_1 = (1, 2, 2)$. Check $\text{Need}_1 \le \text{Work} \implies (1, 2, 2) \le (3, 3, 2) \implies$ **TRUE**.
  - Execute $P_1$:
    $$\text{Work}_{\text{new}} = \text{Work} + \text{Allocation}_1 = (3, 3, 2) + (2, 0, 0) = (5, 3, 2)$$
    $$\text{Finish}[P_1] = \text{True}$$
    $$\text{Safe Sequence} = \langle P_1 \rangle$$

- **Step 3: Evaluate $P_3$** (scanning un-finished processes $P_0, P_2, P_3, P_4$)
  - $\text{Need}_3 = (0, 1, 1)$. Check $\text{Need}_3 \le \text{Work} \implies (0, 1, 1) \le (5, 3, 2) \implies$ **TRUE**.
  - Execute $P_3$:
    $$\text{Work}_{\text{new}} = \text{Work} + \text{Allocation}_3 = (5, 3, 2) + (2, 1, 1) = (7, 4, 3)$$
    $$\text{Finish}[P_3] = \text{True}$$
    $$\text{Safe Sequence} = \langle P_1, P_3 \rangle$$

- **Step 4: Evaluate $P_4$**
  - $\text{Need}_4 = (4, 3, 1)$. Check $\text{Need}_4 \le \text{Work} \implies (4, 3, 1) \le (7, 4, 3) \implies$ **TRUE**.
  - Execute $P_4$:
    $$\text{Work}_{\text{new}} = \text{Work} + \text{Allocation}_4 = (7, 4, 3) + (0, 0, 2) = (7, 4, 5)$$
    $$\text{Finish}[P_4] = \text{True}$$
    $$\text{Safe Sequence} = \langle P_1, P_3, P_4 \rangle$$

- **Step 5: Evaluate $P_0$**
  - $\text{Need}_0 = (7, 4, 3)$. Check $\text{Need}_0 \le \text{Work} \implies (7, 4, 3) \le (7, 4, 5) \implies$ **TRUE**.
  - Execute $P_0$:
    $$\text{Work}_{\text{new}} = \text{Work} + \text{Allocation}_0 = (7, 4, 5) + (0, 1, 0) = (7, 5, 5)$$
    $$\text{Finish}[P_0] = \text{True}$$
    $$\text{Safe Sequence} = \langle P_1, P_3, P_4, P_0 \rangle$$

- **Step 6: Evaluate $P_2$**
  - $\text{Need}_2 = (6, 0, 0)$. Check $\text{Need}_2 \le \text{Work} \implies (6, 0, 0) \le (7, 5, 5) \implies$ **TRUE**.
  - Execute $P_2$:
    $$\text{Work}_{\text{new}} = \text{Work} + \text{Allocation}_2 = (7, 5, 5) + (3, 0, 2) = (10, 5, 7)$$
    $$\text{Finish}[P_2] = \text{True}$$
    $$\text{Safe Sequence} = \langle P_1, P_3, P_4, P_0, P_2 \rangle$$

- **Conclusion for Sub-Question 2:**
  All processes finished ($\text{Finish}[i] = \text{True}$ for all $i$). **The system is in a SAFE state.**
  One valid safe sequence is **$\langle P_1, P_3, P_4, P_0, P_2 \rangle$** (another valid sequence is $\langle P_3, P_1, P_4, P_0, P_2 \rangle$).

---

##### 4. Separate zero-based $P_1$ variant: request $(1, 0, 2)$

- **Step A: Check Request Bounds**
  1. $\text{Request}_1 = (1, 0, 2) \le \text{Need}_1 (1, 2, 2) \implies$ **TRUE**.
  2. $\text{Request}_1 = (1, 0, 2) \le \text{Available} (3, 3, 2) \implies$ **TRUE**.

- **Step B: Tentative Allocation Update**
  Modify system state assuming $P_1$'s request is granted:
  $$\text{Available}_{\text{tentative}} = \text{Available} - \text{Request}_1 = (3, 3, 2) - (1, 0, 2) = (2, 3, 0)$$
  $$\text{Allocation}_{1, \text{tentative}} = \text{Allocation}_1 + \text{Request}_1 = (2, 0, 0) + (1, 0, 2) = (3, 0, 2)$$
  $$\text{Need}_{1, \text{tentative}} = \text{Need}_1 - \text{Request}_1 = (1, 2, 2) - (1, 0, 2) = (0, 2, 0)$$

```text
Tentative System Snapshot after granting P1's Request (1, 0, 2):

             Allocation       Need         Available
               A B C         A B C           A B C
    P0         0 1 0         7 4 3           2 3 0
    P1         3 0 2         0 2 0
    P2         3 0 2         6 0 0
    P3         2 1 1         0 1 1
    P4         0 0 2         4 3 1
```

- **Step C: Run Safety Algorithm on Tentative State**
  - $\text{Work} = (2, 3, 0)$, $\text{Finish} = [\text{False}, \text{False}, \text{False}, \text{False}, \text{False}]$
  1. **Check $P_1$:** $\text{Need}_1 = (0, 2, 0) \le \text{Work} (2, 3, 0) \implies$ **TRUE**.
     $$\text{Work} = (2, 3, 0) + (3, 0, 2) = (5, 3, 2), \quad \text{Finish}[P_1] = \text{True}$$
  2. **Check $P_3$:** $\text{Need}_3 = (0, 1, 1) \le \text{Work} (5, 3, 2) \implies$ **TRUE**.
     $$\text{Work} = (5, 3, 2) + (2, 1, 1) = (7, 4, 3), \quad \text{Finish}[P_3] = \text{True}$$
  3. **Check $P_4$:** $\text{Need}_4 = (4, 3, 1) \le \text{Work} (7, 4, 3) \implies$ **TRUE**.
     $$\text{Work} = (7, 4, 3) + (0, 0, 2) = (7, 4, 5), \quad \text{Finish}[P_4] = \text{True}$$
  4. **Check $P_0$:** $\text{Need}_0 = (7, 4, 3) \le \text{Work} (7, 4, 5) \implies$ **TRUE**.
     $$\text{Work} = (7, 4, 5) + (0, 1, 0) = (7, 5, 5), \quad \text{Finish}[P_0] = \text{True}$$
  5. **Check $P_2$:** $\text{Need}_2 = (6, 0, 0) \le \text{Work} (7, 5, 5) \implies$ **TRUE**.
     $$\text{Work} = (7, 5, 5) + (3, 0, 2) = (10, 5, 7), \quad \text{Finish}[P_2] = \text{True}$$

- **Conclusion for Sub-Question 3:**
  The tentative state is safe with sequence $\langle P_1, P_3, P_4, P_0, P_2 \rangle$. **The separate zero-based $P_1$ request $(1, 0, 2)$ can be GRANTED immediately; it is not the chapter question's source $P_1$.**

---

##### 4A. Chapter question: source $P_1$ = workbook $P_0$ requests $(1,0,0)$ from the original state

**Reset to $T_0$:** $\text{Available}=(3,3,2)$; $\text{Allocation}_0=(0,1,0)$; $\text{Need}_0=(7,4,3)$. This is independent of the already worked request by workbook $P_1$.

1. **Claim test:** $\text{Request}_0=(1,0,0)\le\text{Need}_0=(7,4,3)$.
2. **Availability test:** $\text{Request}_0=(1,0,0)\le\text{Available}=(3,3,2)$.
3. **Tentative update:** $\text{Available}^\prime=(2,3,2)$; $\text{Allocation}_0^\prime=(1,1,0)$; $\text{Need}_0^\prime=(6,4,3)$. All other rows are unchanged.
4. **Safety test:** Start $\text{Work}=(2,3,2)$ and $\text{Finish}=[F,F,F,F,F]$. At this point $P_0$ cannot finish yet, but $P_1$ can. The full componentwise trace follows.

| Step | Process | Need compared with Work before | Work before | Allocation released | Work after | Finish update |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | $P_1$ | $(1,2,2)\le(2,3,2)$ | $(2,3,2)$ | $(2,0,0)$ | $(4,3,2)$ | Finish[1] = T |
| 2 | $P_3$ | $(0,1,1)\le(4,3,2)$ | $(4,3,2)$ | $(2,1,1)$ | $(6,4,3)$ | Finish[3] = T |
| 3 | $P_0$ | $(6,4,3)\le(6,4,3)$ | $(6,4,3)$ | $(1,1,0)$ | $(7,5,3)$ | Finish[0] = T |
| 4 | $P_2$ | $(6,0,0)\le(7,5,3)$ | $(7,5,3)$ | $(3,0,2)$ | $(10,5,5)$ | Finish[2] = T |
| 5 | $P_4$ | $(4,3,1)\le(10,5,5)$ | $(10,5,5)$ | $(0,0,2)$ | $(10,5,7)$ | Finish[4] = T |

**Result:** All Finish values are true. The state is **safe**; grant the chapter-question request to workbook $P_0$. One safe sequence is $\langle P_1,P_3,P_0,P_2,P_4\rangle$.

##### 4B. Chapter answer-vector: the SAME source $P_1$ = workbook $P_0$ requests $(1,0,2)$ from the original state

**Reset again to $T_0$:** $\text{Available}=(3,3,2)$; $\text{Allocation}_0=(0,1,0)$; $\text{Need}_0=(7,4,3)$. Do not carry forward the grant in 4A or the grant to workbook $P_1$.

1. **Claim test:** $\text{Request}_0=(1,0,2)\le\text{Need}_0=(7,4,3)$.
2. **Availability test:** $\text{Request}_0=(1,0,2)\le\text{Available}=(3,3,2)$.
3. **Tentative update:** $\text{Available}^\prime=(2,3,0)$; $\text{Allocation}_0^\prime=(1,1,2)$; $\text{Need}_0^\prime=(6,4,1)$. All other rows are unchanged.
4. **Safety test:** $\text{Work}=(2,3,0)$; $\text{Finish}=[F,F,F,F,F]$. Check every process:

| Process | Tentative Need | Work | Blocking resource(s) |
|:--|:--|:--|:--|
| $P_0$ | $(6,4,1)$ | $(2,3,0)$ | A, B, C |
| $P_1$ | $(1,2,2)$ | $(2,3,0)$ | C |
| $P_2$ | $(6,0,0)$ | $(2,3,0)$ | A |
| $P_3$ | $(0,1,1)$ | $(2,3,0)$ | C |
| $P_4$ | $(4,3,1)$ | $(2,3,0)$ | A, C |

**Result:** No process can finish; Finish remains $[F,F,F,F,F]$. The tentative state is **unsafe**, so **defer** this request and roll back Available, Allocation and Need. The earlier *safe* $(1,0,2)$ calculation belongs to workbook $P_1$ (source $P_2$), a **different process**. An unsafe tentative state is not itself proof that the original state was deadlocked.

##### 5. Sensitivity & Source Discrepancy Analysis

###### Case 4A: $P_4$ requests $(3, 3, 0)$ from original state $T_0$
1. **Check Bounds:**
   - $\text{Request}_4 = (3, 3, 0) \le \text{Need}_4 (4, 3, 1) \implies$ **TRUE**.
   - $\text{Request}_4 = (3, 3, 0) \le \text{Available} (3, 3, 2) \implies$ **TRUE**.
2. **Tentative Allocation Update:**
   $$\text{Available}_{\text{tentative}} = (3, 3, 2) - (3, 3, 0) = (0, 0, 2)$$
   $$\text{Allocation}_{4, \text{tentative}} = (0, 0, 2) + (3, 3, 0) = (3, 3, 2)$$
   $$\text{Need}_{4, \text{tentative}} = (4, 3, 1) - (3, 3, 0) = (1, 0, 1)$$
3. **Safety Algorithm Check:**
   - $\text{Work} = (0, 0, 2)$. Scan all un-finished processes:
     - $P_0: \text{Need}_0 = (7, 4, 3) \le (0, 0, 2) \implies \text{FALSE}$
     - $P_1: \text{Need}_1 = (1, 2, 2) \le (0, 0, 2) \implies \text{FALSE}$
     - $P_2: \text{Need}_2 = (6, 0, 0) \le (0, 0, 2) \implies \text{FALSE}$
     - $P_3: \text{Need}_3 = (0, 1, 1) \le (0, 0, 2) \implies \text{FALSE}$ ($1 > 0$)
     - $P_4: \text{Need}_4 = (1, 0, 1) \le (0, 0, 2) \implies \text{FALSE}$ ($1 > 0$)
4. **Outcome:** No process can execute. The system enters an **UNSAFE state**. $P_4$'s request of $(3, 3, 0)$ must be **DEFERRED (BLOCKED)**.

###### Case 4B: $P_0$ requests $(0, 2, 0)$ AFTER $P_1$'s request $(1, 0, 2)$ is granted
1. **Current State:** $\text{Available} = (2, 3, 0)$, $\text{Need}_0 = (7, 4, 3)$.
2. **Check Bounds:**
   - $\text{Request}_0 = (0, 2, 0) \le \text{Need}_0 (7, 4, 3) \implies$ **TRUE**.
   - $\text{Request}_0 = (0, 2, 0) \le \text{Available} (2, 3, 0) \implies$ **TRUE**.
3. **Tentative Allocation Update:**
   $$\text{Available}_{\text{tentative}} = (2, 3, 0) - (0, 2, 0) = (2, 1, 0)$$
   $$\text{Allocation}_{0, \text{tentative}} = (0, 1, 0) + (0, 2, 0) = (0, 3, 0)$$
   $$\text{Need}_{0, \text{tentative}} = (7, 4, 3) - (0, 2, 0) = (7, 2, 3)$$
4. **Safety Algorithm Check:**
   - $\text{Work} = (2, 1, 0)$. Scan un-finished process needs:
     - $P_0: \text{Need}_0 = (7, 2, 3) \le (2, 1, 0) \implies \text{FALSE}$
     - $P_1: \text{Need}_1 = (0, 2, 0) \le (2, 1, 0) \implies \text{FALSE}$ ($2 > 1$)
     - $P_2: \text{Need}_2 = (6, 0, 0) \le (2, 1, 0) \implies \text{FALSE}$
     - $P_3: \text{Need}_3 = (0, 1, 1) \le (2, 1, 0) \implies \text{FALSE}$ ($1 > 0$)
     - $P_4: \text{Need}_4 = (4, 3, 1) \le (2, 1, 0) \implies \text{FALSE}$
5. **Outcome:** No process can execute. The system enters an **UNSAFE state**. $P_0$'s request of $(0, 2, 0)$ must be **DEFERRED**.

---

### Problem 2: 3-Process 3-Resource System (Lab Manual Exp 7 Problem 1)

#### Source Metadata & Grouped Questions
- **Question Source (Lab Exercise, original manual unverified):** *SVKM'S NMIMS Semester V Lab Manual Exp 7 [Problem 1 - 10 Marks].*

#### Question Statement
Consider a system with 3 processes ($P_0, P_1, P_2$) and 3 resource types ($X, Y, Z$).
The allocation matrix, maximum demand matrix, and available vector at time $T_0$ are given below:

```text
Snapshot at time T0:

             Allocation       Max          Available
               X Y Z         X Y Z          X Y Z
    P0         0 0 1         8 4 3          3 2 2
    P1         3 2 0         6 2 0
    P2         2 1 1         3 3 3
```

**Questions:**
1. Derive the $\text{Need}$ matrix for the processes.
2. Verify system safety by showing the step-by-step Work and Finish trace, and state the safe sequence.

---

#### Complete Step-by-Step Solution

##### 1. Need Matrix Calculation ($\text{Need} = \text{Max} - \text{Allocation}$)

$$\text{Need}[P_0] = (8, 4, 3) - (0, 0, 1) = (8, 4, 2)$$
$$\text{Need}[P_1] = (6, 2, 0) - (3, 2, 0) = (3, 0, 0)$$
$$\text{Need}[P_2] = (3, 3, 3) - (2, 1, 1) = (1, 2, 2)$$

```text
Calculated Need Matrix:

               Need
              X Y Z
    P0        8 4 2
    P1        3 0 0
    P2        1 2 2
```

---

##### 2. Safety Algorithm Trace

- **Initialization:**
  $$\text{Work} = \text{Available} = (3, 2, 2)$$
  $$\text{Finish} = [\text{False}, \text{False}, \text{False}], \quad \text{Safe Sequence} = \langle \rangle$$

- **Step 1: Evaluate $P_0$**
  - $\text{Need}_0 = (8, 4, 2)$. Check $\text{Need}_0 \le \text{Work} \implies (8, 4, 2) \le (3, 2, 2) \implies \text{FALSE}$. $P_0$ waits.

- **Step 2: Evaluate $P_1$**
  - $\text{Need}_1 = (3, 0, 0)$. Check $\text{Need}_1 \le \text{Work} \implies (3, 0, 0) \le (3, 2, 2) \implies$ **TRUE**.
  - Execute $P_1$:
    $$\text{Work}_{\text{new}} = (3, 2, 2) + \text{Allocation}_1 (3, 2, 0) = (6, 4, 2)$$
    $$\text{Finish}[P_1] = \text{True}, \quad \text{Safe Sequence} = \langle P_1 \rangle$$

- **Step 3: Evaluate $P_2$**
  - $\text{Need}_2 = (1, 2, 2)$. Check $\text{Need}_2 \le \text{Work} \implies (1, 2, 2) \le (6, 4, 2) \implies$ **TRUE**.
  - Execute $P_2$:
    $$\text{Work}_{\text{new}} = (6, 4, 2) + \text{Allocation}_2 (2, 1, 1) = (8, 5, 3)$$
    $$\text{Finish}[P_2] = \text{True}, \quad \text{Safe Sequence} = \langle P_1, P_2 \rangle$$

- **Step 4: Evaluate $P_0$**
  - $\text{Need}_0 = (8, 4, 2)$. Check $\text{Need}_0 \le \text{Work} \implies (8, 4, 2) \le (8, 5, 3) \implies$ **TRUE**.
  - Execute $P_0$:
    $$\text{Work}_{\text{new}} = (8, 5, 3) + \text{Allocation}_0 (0, 0, 1) = (8, 5, 4)$$
    $$\text{Finish}[P_0] = \text{True}, \quad \text{Safe Sequence} = \langle P_1, P_2, P_0 \rangle$$

- **Final Conclusion:**
  All processes finish successfully ($\text{Finish} = [\text{True}, \text{True}, \text{True}]$). **The system is in a SAFE state.**
  One valid safe sequence is **$\langle P_1, P_2, P_0 \rangle$**. Another valid sequence is **$\langle P_2,P_1,P_0\rangle$**: starting from Work $(3,2,2)$, $P_2$ releases $(2,1,1)$ giving $(5,3,3)$; $P_1$ releases $(3,2,0)$ giving $(8,5,3)$; and $P_0$ releases $(0,0,1)$ giving $(8,5,4)$.

---

### Problem 3: 5-Process 4-Resource System (Lab Manual Exp 7 Problem 3)

#### Source Metadata & Grouped Questions
- **Question Source (Lab Exercise, original manual unverified):** *SVKM'S NMIMS Semester V Lab Manual Exp 7 [Problem 3 - 10 Marks].*

#### Question Statement
Consider a system with 5 processes ($P_0$ through $P_4$) and 4 resource types ($A, B, C, D$).
The allocation matrix, maximum matrix, and available vector are given below:

```text
Snapshot at time T0:

             Allocation           Max              Available
              A B C D           A B C D             A B C D
    P0        0 0 1 2           0 0 1 2             1 5 2 0
    P1        1 0 0 0           1 7 5 0
    P2        1 3 5 4           2 3 5 6
    P3        0 6 3 2           0 6 5 2
    P4        0 0 1 4           0 6 5 6
```

**Questions:**
1. Compute the content of the $\text{Need}$ matrix.
2. Determine whether the system is in a safe state and state the safe sequence.

---

#### Complete Step-by-Step Solution

##### 1. Need Matrix Calculation ($\text{Need} = \text{Max} - \text{Allocation}$)

$$\text{Need}[P_0] = (0, 0, 1, 2) - (0, 0, 1, 2) = (0, 0, 0, 0)$$
$$\text{Need}[P_1] = (1, 7, 5, 0) - (1, 0, 0, 0) = (0, 7, 5, 0)$$
$$\text{Need}[P_2] = (2, 3, 5, 6) - (1, 3, 5, 4) = (1, 0, 0, 2)$$
$$\text{Need}[P_3] = (0, 6, 5, 2) - (0, 6, 3, 2) = (0, 0, 2, 0)$$
$$\text{Need}[P_4] = (0, 6, 5, 6) - (0, 0, 1, 4) = (0, 6, 4, 2)$$

```text
Calculated Need Matrix:

               Need
              A B C D
    P0        0 0 0 0
    P1        0 7 5 0
    P2        1 0 0 2
    P3        0 0 2 0
    P4        0 6 4 2
```

---

##### 2. Safety Algorithm Trace

- **Initialization:**
  $$\text{Work} = \text{Available} = (1, 5, 2, 0)$$
  $$\text{Finish} = [\text{False}, \text{False}, \text{False}, \text{False}, \text{False}], \quad \text{Safe Sequence} = \langle \rangle$$

- **Step 1: Evaluate $P_0$**
  - $\text{Need}_0 = (0, 0, 0, 0) \le \text{Work} (1, 5, 2, 0) \implies$ **TRUE**.
  - Execute $P_0$:
    $$\text{Work}_{\text{new}} = (1, 5, 2, 0) + (0, 0, 1, 2) = (1, 5, 3, 2)$$
    $$\text{Finish}[P_0] = \text{True}, \quad \text{Safe Sequence} = \langle P_0 \rangle$$

- **Step 2: Evaluate $P_2$**
  - $\text{Need}_2 = (1, 0, 0, 2) \le \text{Work} (1, 5, 3, 2) \implies$ **TRUE**.
  - Execute $P_2$:
    $$\text{Work}_{\text{new}} = (1, 5, 3, 2) + (1, 3, 5, 4) = (2, 8, 8, 6)$$
    $$\text{Finish}[P_2] = \text{True}, \quad \text{Safe Sequence} = \langle P_0, P_2 \rangle$$

- **Step 3: Evaluate $P_3$**
  - $\text{Need}_3 = (0, 0, 2, 0) \le \text{Work} (2, 8, 8, 6) \implies$ **TRUE**.
  - Execute $P_3$:
    $$\text{Work}_{\text{new}} = (2, 8, 8, 6) + (0, 6, 3, 2) = (2, 14, 11, 8)$$
    $$\text{Finish}[P_3] = \text{True}, \quad \text{Safe Sequence} = \langle P_0, P_2, P_3 \rangle$$

- **Step 4: Evaluate $P_4$**
  - $\text{Need}_4 = (0, 6, 4, 2) \le \text{Work} (2, 14, 11, 8) \implies$ **TRUE**.
  - Execute $P_4$:
    $$\text{Work}_{\text{new}} = (2, 14, 11, 8) + (0, 0, 1, 4) = (2, 14, 12, 12)$$
    $$\text{Finish}[P_4] = \text{True}, \quad \text{Safe Sequence} = \langle P_0, P_2, P_3, P_4 \rangle$$

- **Step 5: Evaluate $P_1$**
  - $\text{Need}_1 = (0, 7, 5, 0) \le \text{Work} (2, 14, 12, 12) \implies$ **TRUE**.
  - Execute $P_1$:
    $$\text{Work}_{\text{new}} = (2, 14, 12, 12) + (1, 0, 0, 0) = (3, 14, 12, 12)$$
    $$\text{Finish}[P_1] = \text{True}, \quad \text{Safe Sequence} = \langle P_0, P_2, P_3, P_4, P_1 \rangle$$

- **Final Conclusion:**
  All processes finish ($\text{Finish}[i] = \text{True}$). **The system is in a SAFE state.**
  The safe sequence is **$\langle P_0, P_2, P_3, P_4, P_1 \rangle$**.

---

### Problem 4: 4-Process 3-Resource System (Textbook / Technical Publications)

#### Source Metadata & Grouped Questions
- **Question Source (Textbook-style example, exact source unverified):** *Technical Publications / Standard Operating System Review Sets.*

#### Question Statement
A system has 4 processes ($P_1, P_2, P_3, P_4$) and 3 resource types ($A, B, C$). 
System snapshot at $T_0$ is as follows:

```text
Snapshot at time T0:

             Allocation       Max          Available
               A B C         A B C          A B C
    P1         1 0 1         4 2 2          4 2 3
    P2         1 1 0         2 2 2
    P3         1 0 2         3 1 3
    P4         0 1 0         2 1 2
```

**Questions:**
1. Compute the $\text{Need}$ matrix.
2. Determine if the system is safe and find a safe execution sequence.

---

#### Complete Step-by-Step Solution

##### 1. Need Matrix Calculation ($\text{Need} = \text{Max} - \text{Allocation}$)

$$\text{Need}[P_1] = (4, 2, 2) - (1, 0, 1) = (3, 2, 1)$$
$$\text{Need}[P_2] = (2, 2, 2) - (1, 1, 0) = (1, 1, 2)$$
$$\text{Need}[P_3] = (3, 1, 3) - (1, 0, 2) = (2, 1, 1)$$
$$\text{Need}[P_4] = (2, 1, 2) - (0, 1, 0) = (2, 0, 2)$$

```text
Calculated Need Matrix:

               Need
              A B C
    P1        3 2 1
    P2        1 1 2
    P3        2 1 1
    P4        2 0 2
```

---

##### 2. Safety Algorithm Trace

- **Initialization:** $\text{Work} = (4, 2, 3)$, $\text{Finish} = [\text{False}, \text{False}, \text{False}, \text{False}]$

1. **Evaluate $P_1$:** $\text{Need}_1 = (3, 2, 1) \le \text{Work} (4, 2, 3) \implies$ **TRUE**.
   $$\text{Work}_{\text{new}} = (4, 2, 3) + (1, 0, 1) = (5, 2, 4), \quad \text{Finish}[P_1] = \text{True}$$
2. **Evaluate $P_2$:** $\text{Need}_2 = (1, 1, 2) \le \text{Work} (5, 2, 4) \implies$ **TRUE**.
   $$\text{Work}_{\text{new}} = (5, 2, 4) + (1, 1, 0) = (6, 3, 4), \quad \text{Finish}[P_2] = \text{True}$$
3. **Evaluate $P_3$:** $\text{Need}_3 = (2, 1, 1) \le \text{Work} (6, 3, 4) \implies$ **TRUE**.
   $$\text{Work}_{\text{new}} = (6, 3, 4) + (1, 0, 2) = (7, 3, 6), \quad \text{Finish}[P_3] = \text{True}$$
4. **Evaluate $P_4$:** $\text{Need}_4 = (2, 0, 2) \le \text{Work} (7, 3, 6) \implies$ **TRUE**.
   $$\text{Work}_{\text{new}} = (7, 3, 6) + (0, 1, 0) = (7, 4, 6), \quad \text{Finish}[P_4] = \text{True}$$

- **Final Conclusion:**
  All processes finish. **The system is in a SAFE state.**
  The safe sequence is **$\langle P_1, P_2, P_3, P_4 \rangle$**.

---

## 4. SECTION II: DEADLOCK DETECTION ALGORITHM NUMERICALS

### Problem 5: Multi-Instance Resource Deadlock Detection & Request Sensitivity

#### Source Metadata & Grouped Questions
- **Question Source (Textbook-style example, exact source unverified):** *Silberschatz Textbook Ch. 8 / SVKM NMIMS Mid-Sem Review.*

#### Question Statement
Consider a system with 5 processes ($P_0..P_4$) and 3 resource types ($A, B, C$). 
Total resources are $A=7, B=2, C=6$.
At time $T_0$, the allocation matrix, current request matrix, and available vector are given below:

```text
Snapshot at time T0:

             Allocation      Request        Available
               A B C          A B C           A B C
    P0         0 1 0          0 0 0           0 0 0
    P1         2 0 0          2 0 2
    P2         3 0 3          0 0 0
    P3         2 1 1          1 0 0
    P4         0 0 2          0 0 2
```

**Questions:**
1. Execute the multi-instance deadlock detection algorithm to determine if the system is currently deadlocked.
2. **Sub-case 5B:** Suppose $P_2$ makes an additional request of $(0, 0, 1)$. Does this cause a deadlock? If so, identify the deadlocked processes.

---

#### Complete Step-by-Step Solution

##### 1. Part 1: Detection Algorithm Trace at $T_0$

- **Initialization:**
  $$\text{Work} = \text{Available} = (0, 0, 0)$$
  For all processes $i$, if $\text{Allocation}_i \neq \mathbf{0}$, set $\text{Finish}[i] = \text{False}$.
  $$\text{Finish} = [\text{False}, \text{False}, \text{False}, \text{False}, \text{False}]$$

- **Step 1: Evaluate $P_0$**
  - $\text{Request}_0 = (0, 0, 0) \le \text{Work} (0, 0, 0) \implies$ **TRUE**.
  - $P_0$ can finish and release its allocated resources:
    $$\text{Work}_{\text{new}} = \text{Work} + \text{Allocation}_0 = (0, 0, 0) + (0, 1, 0) = (0, 1, 0)$$
    $$\text{Finish}[P_0] = \text{True}$$

- **Step 2: Evaluate $P_2$**
  - $\text{Request}_2 = (0, 0, 0) \le \text{Work} (0, 1, 0) \implies$ **TRUE**.
  - Execute $P_2$:
    $$\text{Work}_{\text{new}} = (0, 1, 0) + \text{Allocation}_2 (3, 0, 3) = (3, 1, 3)$$
    $$\text{Finish}[P_2] = \text{True}$$

- **Step 3: Evaluate $P_3$**
  - $\text{Request}_3 = (1, 0, 0) \le \text{Work} (3, 1, 3) \implies$ **TRUE**.
  - Execute $P_3$:
    $$\text{Work}_{\text{new}} = (3, 1, 3) + \text{Allocation}_3 (2, 1, 1) = (5, 2, 4)$$
    $$\text{Finish}[P_3] = \text{True}$$

- **Step 4: Evaluate $P_4$**
  - $\text{Request}_4 = (0, 0, 2) \le \text{Work} (5, 2, 4) \implies$ **TRUE**.
  - Execute $P_4$:
    $$\text{Work}_{\text{new}} = (5, 2, 4) + \text{Allocation}_4 (0, 0, 2) = (5, 2, 6)$$
    $$\text{Finish}[P_4] = \text{True}$$

- **Step 5: Evaluate $P_1$**
  - $\text{Request}_1 = (2, 0, 2) \le \text{Work} (5, 2, 6) \implies$ **TRUE**.
  - Execute $P_1$:
    $$\text{Work}_{\text{new}} = (5, 2, 6) + \text{Allocation}_1 (2, 0, 0) = (7, 2, 6)$$
    $$\text{Finish}[P_1] = \text{True}$$

- **Conclusion for Part 1:**
  All processes finish ($\text{Finish}[i] = \text{True}$ for all $i$). **The system is NOT deadlocked.**
  The execution sequence is **$\langle P_0, P_2, P_3, P_4, P_1 \rangle$**.

---

##### 2. Part 2: Sub-case 5B ($P_2$ requests $(0, 0, 1)$)

- **Update Request Matrix:**
  $$\text{Request}_2 = (0, 0, 0) + (0, 0, 1) = (0, 0, 1)$$

- **Detection Algorithm Trace:**
  - $\text{Work} = (0, 0, 0)$, $\text{Finish} = [\text{False}, \text{False}, \text{False}, \text{False}, \text{False}]$
  1. **Check $P_0$:** $\text{Request}_0 = (0, 0, 0) \le \text{Work} (0, 0, 0) \implies$ **TRUE**.
     $$\text{Work} = (0, 0, 0) + (0, 1, 0) = (0, 1, 0), \quad \text{Finish}[P_0] = \text{True}$$
  2. **Scan remaining un-finished processes ($P_1, P_2, P_3, P_4$) against $\text{Work} = (0, 1, 0)$:**
     - $P_1: \text{Request}_1 = (2, 0, 2) \le (0, 1, 0) \implies \text{FALSE}$
     - $P_2: \text{Request}_2 = (0, 0, 1) \le (0, 1, 0) \implies \text{FALSE}$ ($1 > 0$)
     - $P_3: \text{Request}_3 = (1, 0, 0) \le (0, 1, 0) \implies \text{FALSE}$
     - $P_4: \text{Request}_4 = (0, 0, 2) \le (0, 1, 0) \implies \text{FALSE}$
  3. No other process can meet its request requirements.

- **Conclusion for Part 2:**
  $\text{Finish}[0] = \text{True}$, but $\text{Finish}[1..4] = \text{False}$.
  **A DEADLOCK EXISTS involving processes $\{P_1, P_2, P_3, P_4\}$.**

---

## 5. SECTION III: RESOURCE ALLOCATION GRAPH (RAG) ANALYSES

### Problem 6: RAG Matrix Conversion & Single vs. Multi-Instance Cycle Analysis

#### Source Metadata & Grouped Questions
- **Question Source (reported question, original paper unverified):** *Stallings Ch. 6 / GTU Examination.*

#### Question Statement
Given a system with processes $\{P_1, P_2, P_3\}$ and resource types $\{R_1, R_2\}$:
- $R_1$ has 2 instances, $R_2$ has 2 instances.
- Current Allocations: $P_1$ holds 1 instance of $R_1$; $P_2$ holds 1 instance of $R_1$ and 1 instance of $R_2$; $P_3$ holds 1 instance of $R_2$.
- Current Requests: $P_1$ requests 1 instance of $R_2$; $P_3$ requests 1 instance of $R_1$.

```text
Resource Allocation Graph Structure:

    P1 ---> R2 (Request)
    R1 ---> P1 (Assignment)
    R1 ---> P2 (Assignment)
    R2 ---> P2 (Assignment)
    R2 ---> P3 (Assignment)
    P3 ---> R1 (Request)
```

**Questions:**
1. Convert this Resource Allocation Graph into standard $\text{Allocation}$, $\text{Request}$, and $\text{Available}$ matrices.
2. Is there a cycle in the graph? Is the system deadlocked? Explain the relationship between cycles and deadlocks for multi-instance resources.

---

#### Complete Step-by-Step Solution

##### 1. Matrix Conversion from Graph

- **Total Resources:** $R_1 = 2, R_2 = 2$
- **Sum of Allocations:**
  $$\text{Allocated}_1 = 1 (P_1) + 1 (P_2) + 0 (P_3) = 2 \implies \text{Available}_1 = 2 - 2 = 0$$
  $$\text{Allocated}_2 = 0 (P_1) + 1 (P_2) + 1 (P_3) = 2 \implies \text{Available}_2 = 2 - 2 = 0$$

```text
Converted Matrix Representation:

             Allocation      Request        Available
               R1 R2          R1 R2           R1 R2
    P1         1  0           0  1            0  0
    P2         1  1           0  0
    P3         0  1           1  0
```

---

##### 2. Cycle Analysis & Deadlock Detection

- **Cycle Identification:**
  There is a directed cycle in the graph: $P_1 \to R_2 \to P_3 \to R_1 \to P_1$.

- **Detection Algorithm Execution:**
  - $\text{Work} = \text{Available} = (0, 0)$
  - $\text{Finish} = [\text{False}, \text{False}, \text{False}]$
  1. **Check $P_2$:** $\text{Request}_2 = (0, 0) \le \text{Work} (0, 0) \implies$ **TRUE**.
     $$\text{Work}_{\text{new}} = (0, 0) + \text{Allocation}_2 (1, 1) = (1, 1), \quad \text{Finish}[P_2] = \text{True}$$
  2. **Check $P_1$:** $\text{Request}_1 = (0, 1) \le \text{Work} (1, 1) \implies$ **TRUE**.
     $$\text{Work}_{\text{new}} = (1, 1) + \text{Allocation}_1 (1, 0) = (2, 1), \quad \text{Finish}[P_1] = \text{True}$$
  3. **Check $P_3$:** $\text{Request}_3 = (1, 0) \le \text{Work} (2, 1) \implies$ **TRUE**.
     $$\text{Work}_{\text{new}} = (2, 1) + \text{Allocation}_3 (0, 1) = (2, 2), \quad \text{Finish}[P_3] = \text{True}$$

- **Conclusion:**
  All processes finish ($\text{Finish} = [\text{True}, \text{True}, \text{True}]$). **The system is NOT deadlocked.**

- **Key Theoretical Rule:**
  - For **single-instance** resource types, a cycle in a Resource Allocation Graph is **necessary AND sufficient** for deadlock.
  - For **multiple-instance** resource types, a cycle is **necessary BUT NOT sufficient** for deadlock. Here, $P_2$ breaks the cycle by finishing and releasing its resources.

---

## 6. SECTION IV: FORMULA RECAP & PRE-EXAM AUDIT CHECKLIST

### 1. Fundamental Vector & Matrix Equations

1. **Need Matrix Equation:**
   $$\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$$

2. **System Total Resource Conservation Law:**
   $$\text{Total}[j] = \text{Available}[j] + \sum_{i=0}^{n-1} \text{Allocation}[i][j]$$

3. **Resource Request Safety Test Conditions:**
   $$\text{Request}_i \le \text{Need}_i \quad \text{AND} \quad \text{Request}_i \le \text{Available}$$

4. **Tentative State Update Formulas:**
   $$\text{Available}_{\text{new}} = \text{Available} - \text{Request}_i$$
   $$\text{Allocation}_{i, \text{new}} = \text{Allocation}_i + \text{Request}_i$$
   $$\text{Need}_{i, \text{new}} = \text{Need}_i - \text{Request}_i$$

---

### 2. Pre-Exam Quick Revision Audit Checklist

- [x] **Snapshot Alignment:** Is Available displayed as ONE vector for the whole system?
- [x] **Arithmetic Check:** Does $\text{Need} + \text{Allocation} = \text{Max}$ across all matrix entries?
- [x] **Total Check:** Does $\text{Available} + \sum \text{Allocation} = \text{Total}$ system instances?
- [x] **Safe Sequence Order:** Is each process's $\text{Need}_i \le \text{Work}$ verified before adding its $\text{Allocation}_i$ to $\text{Work}$?
- [x] **Tentative Reset:** If a tentative request leads to an unsafe state, is the request explicitly deferred and state restored?
- [x] **Discrepancy Notes:** Are source OCR typos or indexing differences ($P_1..P_5$ vs $P_0..P_4$) explicitly flagged?
- [x] **Deadlock vs Unsafe:** Is an unsafe state clearly distinguished from an actual deadlocked state?
