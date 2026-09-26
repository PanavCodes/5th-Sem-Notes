# Operating Systems: Unit 4 — Deadlock Exam-Oriented PYQ Bank

## Table of Contents
- [1. Document Structure & Source Verification](#1-document-structure-source-verification)
- [2. Topic-Wise Question Index](#2-topic-wise-question-index)
- [3. Repeated-Question Summary List](#3-repeated-question-summary-list)
- [4. Source-Status & Verification Checklist](#4-source-status-verification-checklist)
- [5. SECTION I: PRESCRIBED SYLLABUS TOPICS QUESTION BANK](#5-section-i-prescribed-syllabus-topics-question-bank)
  - [Topic 1: Principles of Deadlock & Resource-Allocation Graphs](#topic-1-principles-of-deadlock-resource-allocation-graphs)
    - [Q1.1: Definition of Deadlock, Necessary Conditions & RAGs (Grouped)](#q11-definition-of-deadlock-necessary-conditions-rags-grouped)
    - [Q1.2: Resource Types: Reusable vs. Consumable Resources](#q12-resource-types-reusable-vs-consumable-resources)
    - [Q1.3: Resource-Allocation Graphs (RAGs) & Cycles vs. Deadlock](#q13-resource-allocation-graphs-rags-cycles-vs-deadlock)
    - [Q1.4: State Classifications: Deadlock vs. Starvation vs. Safe vs. Unsafe](#q14-state-classifications-deadlock-vs-starvation-vs-safe-vs-unsafe)
  - [Topic 2: Deadlock Prevention](#topic-2-deadlock-prevention)
    - [Q2.1: Deadlock Prevention Strategies & Invalidation Methods (Grouped)](#q21-deadlock-prevention-strategies-invalidation-methods-grouped)
    - [Q2.2: Circular Wait Prevention & Formal Linear Ordering Proof](#q22-circular-wait-prevention-formal-linear-ordering-proof)
  - [Topic 3: Deadlock Avoidance & Banker's Algorithm](#topic-3-deadlock-avoidance-bankers-algorithm)
    - [Q3.1: Deadlock Avoidance Concepts & Safe State Analysis](#q31-deadlock-avoidance-concepts-safe-state-analysis)
    - [Q3.2: Banker's Algorithm Data Structures & Operations](#q32-bankers-algorithm-data-structures-operations)
    - [Q3.3: Banker's Algorithm Numerical Problem 1 (Standard 5-Process 3-Resource)](#q33-bankers-algorithm-numerical-problem-1-standard-5-process-3-resource)
    - [Q3.4: Banker's Algorithm Numerical Problem 2 (Lab Exp 7 Problem 1 - 3-Process)](#q34-bankers-algorithm-numerical-problem-2-lab-exp-7-problem-1---3-process)
    - [Q3.5: Banker's Algorithm Numerical Problem 3 (Lab Exp 7 Problem 3 - 4-Resource)](#q35-bankers-algorithm-numerical-problem-3-lab-exp-7-problem-3---4-resource)
  - [Topic 4: Deadlock Detection & Recovery](#topic-4-deadlock-detection-recovery)
    - [Q4.1: Deadlock Detection Algorithms: Wait-For Graph vs. Multi-Instance](#q41-deadlock-detection-algorithms-wait-for-graph-vs-multi-instance)
    - [Q4.2: Deadlock Recovery Strategies: Termination & Preemption](#q42-deadlock-recovery-strategies-termination-preemption)
  - [Topic 5: The Dining Philosophers Problem](#topic-5-the-dining-philosophers-problem)
    - [Q5.1: Dining Philosophers Problem & Naive Semaphore Failure](#q51-dining-philosophers-problem-naive-semaphore-failure)
    - [Q5.2: Deadlock-Free Semaphore & Monitor Solutions](#q52-deadlock-free-semaphore-monitor-solutions)
- [6. SECTION II: ADDITIONAL TOPICS IN SUPPLIED TEACHING MATERIALS](#6-section-ii-additional-topics-in-supplied-teaching-materials)
  - [Topic A1: Ostrich Algorithm & Trade-offs in Modern Operating Systems](#topic-a1-ostrich-algorithm-trade-offs-in-modern-operating-systems)
- [7. SECTION III: QUICK REVISION CHECKLIST & ALGORITHM RECAP](#7-section-iii-quick-revision-checklist-algorithm-recap)

---

## 1. Document Structure & Source Verification

This **Exam-Oriented Previous Year Question (PYQ) Bank** covers **Unit 4: Deadlock** (05 Hours) as prescribed by the SVKM NMIMS University Operating Systems curriculum (`Approved CP_OS.pdf`). It preserves the questions and source attributions found in the supplied bank, together with textbook-style and lab-manual exercises. The cited original examination papers and lab manual were not attached here, so their exact wording, marks and question numbers are not independently verified.

### Classification & Labeling Standards
- **Claimed exam PYQ (unverified):** Questions attributed in the original bank to SVKM's NMIMS University Semester V examination question papers (`QP_Final-Exam_Operating Systems(702CO1C002)_Semester V_2024-2025.pdf`, `Operating_System__Sem-V__Year_2022-23__Special_Re_Exam_GF1XGRiPQ3.pdf`, `Operating_System___Re-exam_2022-23_DyWjtzaYi3.pdf`, `Operating_Systems__Sem-V__A_Y_2023-24__Final_Exam_w3cxMbVN2J.pdf`, `Operating_Systems__Batch__2024-25_Final_Batch_2023-24__Re_Exam_20jgs6KmZG.pdf`).
- **Reported question (unverified):** Questions extracted from university compilations (GTU, TechNeo, Easy Solution, Technical Publications) or chapter review sets.
- **Practice Question:** Newly written questions designed to ensure complete, syllabus-aligned exam preparation.

---

## 2. Topic-Wise Question Index

A **question section** is one numbered answer group; a **question wording** is one individually printed source/practice question within that group. The two totals are different because related wordings share answers. A reported question is not a verified past-paper question.

| Topic | Answer-group IDs | Sections | Question wordings |
|:--|:--|--:|--:|
| Principles of deadlock | Q1.1, Q1.2, Q1.3, Q1.4 | 4 | 7 |
| Deadlock prevention | Q2.1, Q2.2 | 2 | 3 |
| Deadlock avoidance and Banker's | Q3.1, Q3.2, Q3.3, Q3.4, Q3.5 | 5 | 6 |
| Detection and recovery | Q4.1, Q4.2 | 2 | 3 |
| Dining Philosophers | Q5.1, Q5.2 | 2 | 2 |
| Additional material | QA1.1 | 1 | 1 |
| **TOTAL** | **16 groups** | **16** | **22** |

**Counting note:** The original index claimed 29 questions, but only the individual question wordings printed in this file are counted above. The original 29/13/14/2 status breakdown was not auditable from the text and has been removed. The three Banker's source problems are each counted once; their differing request vectors are worked interpretations, not invented additional PYQs.

## 3. Repeated-Question Summary List

| Core Concept | Frequently Asked Question Patterns | Grouped Under | Primary Target Answer |
| :--- | :--- | :--- | :--- |
| **4 Necessary Conditions** | "Explain four necessary conditions for deadlock." / "Define Coffman's conditions." | **Q1.1** | Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait definitions and mechanics. |
| **Deadlock Prevention** | "How can deadlock be prevented?" / "Explain methods to break Coffman conditions." | **Q2.1** | Invalidation protocols for all 4 conditions with trade-off analysis. |
| **Banker's Safety Check** | "State and explain Banker's algorithm." / "Check system safety and find safe sequence." | **Q3.2 & Q3.3** | Matrices ($\text{Need} = \text{Max} - \text{Allocation}$), Work/Finish trace, request safety evaluations. |
| **Resource-Allocation Graphs** | "Explain Resource Allocation Graph with cycle." / "Does a cycle always mean deadlock?" | **Q1.3** | RAG components, single-instance vs. multi-instance cycle significance. |
| **Dining Philosophers** | "Explain Dining Philosophers problem and its solution using semaphores/monitors." | **Q5.1 & Q5.2** | Naive deadlock trace, asymmetric/capacity solutions, monitor implementation, starvation analysis. |

---

## 4. Source-Status & Verification Checklist

| Source File / Paper ID | Institution / Session | Scope Included | Verification Status |
| :--- | :--- | :--- | :--- |
| `QP_Final-Exam_Operating Systems(702CO1C002)_Semester V_2024-2025.pdf` | SVKM's NMIMS (2024-2025) | Unit 4 Questions | **Unverified attribution** |
| `Operating_System__Sem-V__Year_2022-23__Special_Re_Exam_GF1XGRiPQ3.pdf` | SVKM's NMIMS (2022-2023) | Unit 4 Questions | **Unverified attribution** |
| `Operating_System___Re-exam_2022-23_DyWjtzaYi3.pdf` | SVKM's NMIMS (2022-2023) | Unit 4 Questions | **Unverified attribution** |
| `Operating_Systems__Sem-V__A_Y_2023-24__Final_Exam_w3cxMbVN2J.pdf` | SVKM's NMIMS (2023-2024) | Unit 4 Questions | **Unverified attribution** |
| `Operating_Systems__Batch__2024-25_Final_Batch_2023-24__Re_Exam_20jgs6KmZG.pdf` | SVKM's NMIMS (2024-2025) | Unit 4 Questions | **Unverified attribution** |
| `OS Chap 4 Deadlock.pdf` | Textbook Chapter / Handout | Unit 4 Theory & Examples | **`Reported PYQ (unverified)`** |
| `OS Notes HM.pdf` / `3140702-OS-Techanical Publications.pdf` | Course Notes / GTU | Unit 4 Exercises | **`Reported PYQ (unverified)`** |

---

## 5. SECTION I: PRESCRIBED SYLLABUS TOPICS QUESTION BANK

### Topic 1: Principles of Deadlock & Resource-Allocation Graphs

#### Q1.1: Definition of Deadlock, Necessary Conditions & RAGs (Grouped)
- **Original Question 1 (exam attribution unverified):** *SVKM'S NMIMS Semester V Final Exam (2024-2025) [Q4a - 10 Marks]:* "Define deadlock. Explain the four necessary conditions for a deadlock to occur. Draw and explain a Resource Allocation Graph (RAG) illustrating a deadlocked state."
- **Original Question 2 (exam attribution unverified):** *SVKM'S NMIMS Semester V Special Re-Exam (2022-2023) [Q4a - 5 Marks]:* "What is deadlock? State and explain four necessary conditions for deadlock occurrence."
- **Reported question 3 (unverified):** *GTU Dec 2014 / TechNeo [Marks 7]:* "Define deadlock. Describe the four conditions proposed by Coffman for deadlock with appropriate real-world or computer system examples."

##### Shared Answer (Complete 10-Mark Answer):

###### 1. Definition of Deadlock (2 Marks)
A **deadlock** is an undesirable system state in a multiprogramming environment where two or more processes are permanently blocked because each process waits for a resource or event that can be provided only by another blocked process in the set. Since no process can release its held resources without executing, none of the processes can proceed without external intervention.

```text
  Process P1 ------------ (Holds R1, Waits for R2) ------------> Resource R2
      ^                                                             |
      |                                                             |
  Resource R1 <------------ (Holds R2, Waits for R1) ------------ Process P2
```

###### 2. The Four Necessary Conditions for Deadlock (Coffman Conditions) (4 Marks)
The following four conditions are necessary for a resource deadlock and must hold simultaneously; their presence alone does not prove a particular multi-instance allocation is already deadlocked:

1. **Mutual Exclusion:**
   - **Mechanism:** At least one resource must be held in a non-shareable mode. Only one process can use the resource at any given instant. If another process requests that resource, the requesting process must be delayed until the resource is released.
   - **Example:** A physical tape drive, printer, or a write-lock on a database record.

2. **Hold and Wait:**
   - **Mechanism:** A process must currently hold at least one allocated resource while simultaneously waiting to acquire additional resources that are currently being held by other active processes.
   - **Example:** Process $P_1$ holds Resource $R_1$ and requests Resource $R_2$ without releasing $R_1$.

3. **No Preemption:**
   - **Mechanism:** Resources cannot be forcibly preempted or taken away from a process while it is using them. A resource can only be released voluntarily by the holding process after it has completed its task.
   - **Example:** The OS kernel cannot forcibly snatch an open optical drive or a locked memory mutex from an active process.

4. **Circular Wait:**
   - **Mechanism:** A closed chain or circular set of processes $\{P_0, P_1, \dots, P_n\}$ exists such that $P_0$ is waiting for a resource held by $P_1$, $P_1$ is waiting for a resource held by $P_2$, ..., $P_{n-1}$ is waiting for a resource held by $P_n$, and $P_n$ is waiting for a resource held by $P_0$.
   - **Mathematical Formulation:**
     $$P_0     o R_1     o P_1     o R_2     o \dots     o P_n     o R_0     o P_0$$

###### 3. Resource-Allocation Graph (RAG) Illustrating Deadlock (4 Marks)
A **Resource-Allocation Graph (RAG)** is a directed graph $G = (V, E)$ used to model system resource allocations and process wait dependencies.
- **Vertices ($V$):** Divided into two classes:
  - Process Nodes $P = \{P_1, P_2, \dots, P_n\}$ (drawn as circles).
  - Resource Nodes $R = \{R_1, R_2, \dots, R_m\}$ (drawn as rectangles containing small dots representing resource instances).
- **Edges ($E$):**
  - **Request Edge ($P_i     o R_j$):** Directed edge from process $P_i$ to resource $R_j$, indicating $P_i$ is currently waiting for an instance of $R_j$.
  - **Assignment Edge ($R_j     o P_i$):** Directed edge from a specific instance dot in $R_j$ to process $P_i$, indicating that instance of $R_j$ is allocated to $P_i$.

```text
        +------------+                   +------------+
        | Resource R1|                   | Resource R2|
        |   [ * ]    |                   |   [ * ]    |
        +-----+------+                   +-----+------+
              |                                ^
        Assignment                             | Request
              |                                |
              v                                |
        ( Process P1 ) --- Request --------> ( Process P2 )
              ^                                |
              |                                |
              +----------- Assignment ---------+
```

- **Graph Analysis:** In the graph above, Process $P_1$ holds $R_1$ and requests $R_2$. Process $P_2$ holds $R_2$ and requests $R_1$. The directed cycle $P_1     o R_2     o P_2     o R_1     o P_1$ contains single-instance resources, representing a **permanent deadlocked state**.

---

#### Q1.2: Resource Types: Reusable vs. Consumable Resources
- **Reported question (unverified):** *Stallings OS Textbook / Course Notes [Marks 5]:* "Differentiate between reusable resources and consumable resources. Give two examples for each and explain how deadlock can occur with consumable resources."

##### Answer (5 Marks):

###### 1. Differentiating Reusable vs. Consumable Resources

| Feature / Metric | Reusable Resources | Consumable Resources |
| :--- | :--- | :--- |
| **Definition** | A resource that can be safely used by one process at a time and is **not consumed or destroyed** by that use. | A resource that is **created (produced) and destroyed (consumed)** dynamically during execution. |
| **Life Cycle** | Process requests, acquires, uses, and **releases** the resource back to the system pool. | Producer process creates the resource; Consumer process acquires and **destroys** it. |
| **Quantity Constraint** | Fixed total count maintained by the system. | Unbounded or dynamic count dependent on process activity. |
| **Primary Examples** | CPU cores, RAM blocks, Disk space, Printers, Mutex locks. | Signals, IPC messages, Network packets, Interrupts. |

###### 2. Deadlock Involving Consumable Resources
Deadlock occurs with consumable resources when a receiving process blocks waiting for a message/signal from a sending process, but the sending process is itself blocked waiting for a signal from the receiver (or another process).

```text
Process P1 (Consumer of Msg2, Producer of Msg1):
    Receive(P2, Msg2);   // BLOCKED waiting for Msg2 from P2
    Send(P2, Msg1);

Process P2 (Consumer of Msg1, Producer of Msg2):
    Receive(P1, Msg1);   // BLOCKED waiting for Msg1 from P1
    Send(P1, Msg2);
```
- **Deadlock Analysis:** Both processes execute `Receive()` first. Neither process can reach its `Send()` operation to produce the expected message, resulting in a **consumable resource deadlock**.

---

#### Q1.3: Resource-Allocation Graphs (RAGs) & Cycles vs. Deadlock
- **Original Question 1 (exam attribution unverified):** *SVKM'S NMIMS Semester V Re-Exam (2022-2023) [Q4b - 5 Marks]:* "Explain Resource Allocation Graph (RAG). Is the presence of a cycle in a RAG a necessary and sufficient condition for deadlock? Justify."
- **Reported question 2 (unverified):** *GTU June 2015 [Marks 5]:* "Does a cycle in a Resource Allocation Graph always indicate deadlock? Explain with suitable single-instance and multi-instance diagrams."

##### Answer (5 Marks):

###### 1. RAG Cycle Rule
The presence of a directed cycle in a Resource-Allocation Graph is **always a NECESSARY condition** for deadlock, but whether it is **SUFFICIENT** depends entirely on the instance count of the resources in the cycle:

1. **Single-Instance Resources:** A cycle in a RAG is **both a Necessary AND Sufficient condition** for deadlock. If a cycle exists, deadlock is guaranteed.
2. **Multiple-Instance Resources:** A cycle in a RAG is a **Necessary BUT NOT Sufficient condition** for deadlock. A cycle may exist without the system being deadlocked if processes outside the cycle can release resource instances.

###### 2. Illustrative Comparison Diagrams

```text
Case A: Single-Instance Cycle (DEADLOCK)      Case B: Multi-Instance Cycle (NO DEADLOCK)

      +------+                                      +------+
      |  R1  |                                      |  R1  |  [ * ] [ * ]
      | [*]  |                                      +--+---+
      +--+---+                                         |      ^
         |      ^                                      |      |
     Assign    Req                                 Assign    Req
         |      |                                      |      |
         v      |                                      v      |
       (P1)----+                                     (P1)----+
         |                                             |
        Req                                           Req
         |                                             |
         v                                             v
      +--+---+                                      +--+---+
      |  R2  |                                      |  R2  |  [ * ] [ * ]
      | [*]  |                                      +--+---+
      +--+---+                                         ^      |
         |      ^                                      |      |
     Assign    Req                                 Assign   Assign
         |      |                                      |      |
         v      |                                      |      v
       (P2)----+                                     (P3)    (P2)
```

###### 3. Justification
- **In Case A (Single-Instance):** $P_1$ holds $R_1$ and waits for $R_2$. $P_2$ holds $R_2$ and waits for $R_1$. Neither can proceed. **System is Deadlocked.**
- **In Case B (Multi-Instance):** $R_1$ and $R_2$ each have 2 instances. Process $P_3$ holds an instance of $R_1$ without waiting for anything. When $P_3$ finishes, it releases $R_1$, breaking the cycle and allowing $P_1$ or $P_2$ to complete. **System is NOT Deadlocked.**

---

#### Q1.4: State Classifications: Deadlock vs. Starvation vs. Safe vs. Unsafe
- **Practice Question:** *Exam Scope Integration [Marks 5]:* "Compare and contrast the following terms: (a) Deadlock vs. Starvation, (b) Safe State vs. Unsafe State vs. Deadlocked State."

##### Answer (5 Marks):

###### 1. Deadlock vs. Starvation

| Attribute | Deadlock | Starvation (Indefinite Blocking) |
| :--- | :--- | :--- |
| **Definition** | Two or more processes are permanently blocked waiting for resources held by each other. | A process is indefinitely delayed waiting for a resource because other processes are repeatedly given priority. |
| **Process State** | Processes are in a **Blocked / Waiting** state; zero CPU progress. | Process may be in a **Ready** or **Waiting** state; system as a whole makes progress. |
| **Cause** | Circular dependency among non-shareable resources. | Unfair scheduling or greedy allocation algorithms (e.g., LJF, Priority). |
| **Resolution** | Requires external intervention (killing processes, preempting resources). | Resolved by adding aging mechanisms or fair queuing (e.g., Round Robin). |

###### 2. Safe State vs. Unsafe State vs. Deadlocked State

```text
+-------------------------------------------------------+
|                 ALL SYSTEM STATES                     |
|  +-------------------------------------------------+  |
|  |                 UNSAFE STATES                   |  |
|  |  +-------------------------------------------+  |  |
|  |  |            DEADLOCKED STATES              |  |  |
|  |  +-------------------------------------------+  |  |
|  +-------------------------------------------------+  |
|  +-------------------------------------------------+  |
|  |                  SAFE STATES                    |  |
|  +-------------------------------------------------+  |
+-------------------------------------------------------+
```

1. **Safe State:** A state is safe if there exists a **safe sequence** $\langle P_1, P_2, \dots, P_n \rangle$ of process executions such that for each $P_i$, the resources that $P_i$ still needs can be satisfied by currently available resources plus the resources held by all preceding processes $P_j$ ($j < i$). **Guarantees no deadlock.**
2. **Unsafe State:** A state from which the operating system cannot guarantee that all processes will finish. **An unsafe state is NOT necessarily a deadlock**, but it creates the potential for a deadlock if process demands reach maximum limits.
3. **Deadlocked State:** A subset of unsafe states where processes are actively stuck in a circular wait dependency and cannot proceed.

---

### Topic 2: Deadlock Prevention

#### Q2.1: Deadlock Prevention Strategies & Invalidation Methods (Grouped)
- **Original Question 1 (exam attribution unverified):** *SVKM'S NMIMS Semester V Final Exam (2023-2024) [Q3a - 10 Marks]:* "What is deadlock prevention? Discuss how a system can prevent deadlock by invalidating each of the four Coffman conditions."
- **Reported question 2 (unverified):** *GTU Dec 2014 [Marks 7]:* "Explain deadlock prevention methods for each necessary condition. What are the disadvantages of each approach?"

##### Answer (Complete 10-Mark Answer):

###### 1. Overview of Deadlock Prevention (2 Marks)
**Deadlock Prevention** is a set of conservative static methods designed to ensure that a system **can never enter a deadlocked state**. It works by constraining resource requests such that **at least one of the four Coffman necessary conditions is structurally invalidated** at design time.

###### 2. Invalidating the Four Conditions (8 Marks)

###### A. Invalidating Mutual Exclusion
- **Strategy:** Make all system resources shareable so that no process ever needs exclusive access.
- **Implementation:** Read-only files can be shared simultaneously among multiple processes. Non-shareable devices (like printers) can be **spooled** through a daemon process.
- **Limitations & Disadvantages:** Many hardware resources (e.g., tape drives, write mutexes, memory buffers) are fundamentally non-shareable. Spooling requires substantial disk space and introduces daemon management overhead.

###### B. Invalidating Hold and Wait
- **Strategy:** Guarantee that whenever a process requests resources, it does not currently hold any other resources.
- **Implementation Methods:**
  1. **Protocol 1 (All-at-Once Allocation):** A process must request and be allocated all its required resources at once before beginning execution.
  2. **Protocol 2 (Release-Before-Request):** A process can request additional resources only after releasing all currently allocated resources.
- **Limitations & Disadvantages:**
  - **Severe Resource Underutilization:** A process that needs a tape drive at the end of its 10-hour execution must lock it for the full 10 hours.
  - **Starvation Risk:** Processes requiring many popular resources may be delayed indefinitely while waiting for all resources to be free simultaneously.

###### C. Invalidating No Preemption
- **Strategy:** If a process holding resources requests another resource that cannot be immediately allocated, all currently held resources are forcibly preempted.
- **Implementation:**
  - When $P_i$ requests $R_j$ and $R_j$ is unavailable, $P_i$'s held resources are implicitly released and added to the pool of free resources. $P_i$ is restarted only when it regains both its old and new resources.
- **Limitations & Disadvantages:**
  - Applied easily to state-saveable resources (like CPU registers or memory pages via context switches).
  - Cannot be applied to non-state-saveable resources (like printers or database write transactions) without destroying task integrity.

###### D. Invalidating Circular Wait
- **Strategy:** Imposes a strict global linear ordering on all system resource types.
- **Implementation:** Define a one-to-one mapping function $F: R \to \mathbb{N}$ that assigns a unique integer index to each resource type (e.g., $F(\text{Tape}) = 1$, $F(\text{Disk}) = 2$, $F(\text{Printer}) = 3$). A process can request resources only in strictly increasing order of enumeration.
- **Limitations & Disadvantages:** Prevents circular wait completely, but restricts programming flexibility and requires dynamic resource access needs to be mapped to static indices.

---

#### Q2.2: Circular Wait Prevention & Formal Linear Ordering Proof
- **Original Question (exam attribution unverified):** *SVKM'S NMIMS Semester V Batch Re-Exam (2024-2025) [Q2b - 5 Marks]:* "Explain how imposing a global linear ordering on resources prevents circular wait. Provide a formal proof by contradiction."

##### Answer (5 Marks):

###### 1. Global Linear Ordering Mechanism
Let $R = \{R_1, R_2, \dots, R_m\}$ be the set of all resource types in the system. Assign a global integer index function $F: R \to \mathbb{N}$.

**Rule:** A process $P_i$ can request a resource $R_b$ if and only if:
1. $P_i$ holds no resources, OR
2. $F(R_b) > F(R_a)$ for all resources $R_a$ currently held by $P_i$.

If $P_i$ needs a resource $R_c$ where $F(R_c) < F(R_a)$, $P_i$ must first release all resources $R_a$ such that $F(R_a) \ge F(R_c)$.

###### 2. Proof by Contradiction
Assume that a circular wait state exists despite strict enforcement of the linear ordering rule.

1. Let the circular wait chain be represented by processes $\{P_0, P_1, \dots, P_n\}$ and resources $\{R_{\pi 0}, R_{\pi 1}, \dots, R_{\pi n}\}$:
   - $P_0$ holds $R_{\pi 0}$ and requests $R_{\pi 1}$.
   - $P_1$ holds $R_{\pi 1}$ and requests $R_{\pi 2}$.
   - ...
   - $P_{n-1}$ holds $R_{\pi(n-1)}$ and requests $R_{\pi n}$.
   - $P_n$ holds $R_{\pi n}$ and requests $R_{\pi 0}$.

2. According to the linear ordering rule, a process holding $R_a$ can request $R_b$ only if $F(R_b) > F(R_a)$. Therefore, the allocation chain yields the strict inequality chain:
   $$F(R_{\pi 0}) < F(R_{\pi 1}) < F(R_{\pi 2}) < \dots < F(R_{\pi n}) < F(R_{\pi 0})$$

3. Transitivity of the strictly-less-than relation ($<$) implies that:
   $$F(R_{\pi 0}) < F(R_{\pi 0})$$

4. **Conclusion:** $F(R_{\pi 0}) < F(R_{\pi 0})$ is an impossible mathematical contradiction. Thus, a circular wait chain **cannot exist** under strict global linear ordering. $\square$

---

### Topic 3: Deadlock Avoidance & Banker's Algorithm

#### Q3.1: Deadlock Avoidance Concepts & Safe State Analysis
- **Original Question 1 (exam attribution unverified):** *SVKM'S NMIMS Semester V Final Exam (2024-2025) [Q4b - 5 Marks]:* "Differentiate between deadlock prevention and deadlock avoidance. Explain the concept of a safe state."
- **Reported question 2 (unverified):** *GTU June 2015 [Marks 5]:* "Define safe state and safe sequence in deadlock avoidance. Why is an unsafe state not necessarily a deadlocked state?"

##### Answer (5 Marks):

###### 1. Differentiating Deadlock Prevention vs. Avoidance

| Attribute | Deadlock Prevention | Deadlock Avoidance |
| :--- | :--- | :--- |
| **Core Approach** | Static design-time constraints that eliminate one of Coffman's 4 conditions. | Dynamic runtime monitoring that evaluates resource requests before granting them. |
| **System Knowledge** | Requires no advance information about future process resource demands. | Requires process to declare its **maximum resource needs upfront**. |
| **Resource Utilization** | Low utilization due to rigid allocation constraints. | **Higher utilization**; resources granted dynamically if state remains safe. |
| **Overhead** | Low runtime overhead (static rules). | High runtime overhead due to executing safety algorithms on every request. |

###### 2. Safe State & Safe Sequence
- **Safe State:** A state is safe if the operating system can allocate resources to each process (up to its declared maximum) in some order without creating a deadlock.
- **Safe Sequence:** An ordered sequence of processes $\langle P_1, P_2, \dots, P_n \rangle$ is safe if, for each $P_i$, the additional resources that $P_i$ still needs can be satisfied by the **currently available resources plus the resources already held by all preceding processes $P_j$ ($j < i$)**.

```text
       +---------------------------------------------------------+
       |                     UNSAFE STATE                        |
       |  (Deadlock is possible if max demands are requested)   |
       |                                                         |
       |     +---------------------------------------------+     |
       |     |              DEADLOCKED STATE               |     |
       |     +---------------------------------------------+     |
       +---------------------------------------------------------+
                                    ^
                                    | Dynamic Request
                                    | (Pushes System Across Boundary)
       +----------------------------+----------------------------+
       |                     SAFE STATE                          |
       |     (Guaranteed safe sequence exists; No deadlock)      |
       +---------------------------------------------------------+
```

---

#### Q3.2: Banker's Algorithm Data Structures & Operations
- **Reported question (unverified):** *Textbook Review / TechNeo [Marks 5]:* "Describe the data structures and steps involved in Dijkstra's Banker's Algorithm for deadlock avoidance."

##### Answer (5 Marks):

###### 1. Core Data Structures
Let $n$ be the number of processes and $m$ be the number of resource types.

1. **`Available[m]` (Vector):** Length $m$. If `Available[j] = k`, there are $k$ instances of resource type $R_j$ currently unallocated and available.
2. **`Max[n][m]` (Matrix):** $n     imes m$. If `Max[i][j] = k`, process $P_i$ may request at most $k$ instances of resource type $R_j$.
3. **`Allocation[n][m]` (Matrix):** $n     imes m$. If `Allocation[i][j] = k`, process $P_i$ is currently allocated $k$ instances of resource type $R_j$.
4. **`Need[n][m]` (Matrix):** $n     imes m$. Indicates remaining resource needs of each process:
```math
\mathrm{Need}[i][j]=\mathrm{Max}[i][j]-\mathrm{Allocation}[i][j]
```

###### 2. Safety Algorithm Pseudocode

```c
// Step 1: Initialize Work and Finish
int Work[m];
bool Finish[n];

for (int j = 0; j < m; j++) {
    Work[j] = Available[j];
}
for (int i = 0; i < n; i++) {
    Finish[i] = false;
}

// Step 2: Find an index i such that both:
//   (a) Finish[i] == false
//   (b) Need[i][j] <= Work[j] for all j = 0..m-1
while (true) {
    int i = find_executable_process(Finish, Need, Work);
    if (i != -1) {
        // Step 3: Simulate process completion and resource release
        for (int j = 0; j < m; j++) {
            Work[j] += Allocation[i][j];
        }
        Finish[i] = true;
    } else {
        break; // No more executable processes found
    }
}

// Step 4: Check if all processes finished
bool system_is_safe = true;
for (int i = 0; i < n; i++) {
    if (!Finish[i]) {
        system_is_safe = false;
        break;
    }
}
```

###### 3. Resource-Request Algorithm Pseudocode
When process $P_i$ makes a request vector $\text{Request}_i$:

```c
// Step 1: Check if Request <= Need
if (Request_i <= Need[i]) {
    // Step 2: Check if Request <= Available
    if (Request_i <= Available) {
        // Step 3: Tentatively allocate resources to P_i
        Available = Available - Request_i;
        Allocation[i] = Allocation[i] + Request_i;
        Need[i] = Need[i] - Request_i;
        
        // Step 4: Run Safety Algorithm on tentative state
        if (is_system_safe()) {
            grant_request_permanently();
        } else {
            rollback_tentative_allocation();
            P_i_must_wait();
        }
    } else {
        P_i_must_wait(); // Insufficient available resources
    }
} else {
    raise_error("Process exceeded its maximum declared claim!");
}
```

---

#### Q3.3: Banker's Algorithm Numerical Problem 1 (Standard 5-Process 3-Resource)
- **Question as printed in this bank (exam attribution unverified):** *SVKM's NMIMS Semester V Final Exam (2024-2025), claimed Q4c, 10 marks; original paper not supplied for verification.* The numerical snapshot is also in `OS Chap 4 Deadlock.pdf`, PDF pp. 21-25. The chapter labels its rows P1-P5, while this table uses P0-P4. The question below is a **normalized transcription**, not a claim of verbatim exam wording.
- **Problem:** Given five processes P0-P4, three resource types A, B, C, and totals (10, 5, 7), determine Need, check whether the state at T0 is safe, and decide whether the request printed in the chapter's question, **(1, 0, 0) by source P1 (our P0)**, can be granted. Analyze the chapter's conflicting answer vector separately.

**Snapshot at T0 (Available is a single vector, displayed in the first row only):**

| Process | Allocation (A, B, C) | Max (A, B, C) | Available (A, B, C) |
|:--|:--|:--|:--|
| P0 | 0, 1, 0 | 7, 5, 3 | 3, 3, 2 |
| P1 | 2, 0, 0 | 3, 2, 2 | - |
| P2 | 3, 0, 2 | 9, 0, 2 | - |
| P3 | 2, 1, 1 | 2, 2, 2 | - |
| P4 | 0, 0, 2 | 4, 3, 3 | - |

**Tasks:** (a) Compute Need = Max - Allocation. (b) Show the Work/Finish safety trace and one safe sequence. (c) Test the question's request. (d) Clearly separate the conflicting answer vector and any textbook-style variants.

##### Complete solution

###### 1. Need matrix and available resources
| Process | Allocation | Max | Need = Max - Allocation |
|:--|:--|:--|:--|
| P0 | (0, 1, 0) | (7, 5, 3) | (7, 4, 3) |
| P1 | (2, 0, 0) | (3, 2, 2) | (1, 2, 2) |
| P2 | (3, 0, 2) | (9, 0, 2) | (6, 0, 0) |
| P3 | (2, 1, 1) | (2, 2, 2) | (0, 1, 1) |
| P4 | (0, 0, 2) | (4, 3, 3) | (4, 3, 1) |

Total Allocation = (7, 2, 5), so Available = (10, 5, 7) - (7, 2, 5) = **(3, 3, 2)**, matching the snapshot. The row-by-row differences are (7-0, 5-1, 3-0) = (7, 4, 3); (3-2, 2-0, 2-0) = (1, 2, 2); (9-3, 0-0, 2-2) = (6, 0, 0); (2-2, 2-1, 2-1) = (0, 1, 1); (4-0, 3-0, 3-2) = (4, 3, 1).

```math
\mathrm{Need}=\begin{bmatrix}
7&4&3\\
1&2&2\\
6&0&0\\
0&1&1\\
4&3&1
\end{bmatrix}
```

###### 2. Original-state safety check
Initialize Work = (3, 3, 2) and Finish = [false, false, false, false, false]. P0 cannot finish initially because Need0 = (7, 4, 3) exceeds Work; P1 can finish first.

| Step | Process | Need <= Work? | Work before | Allocation released | Work after | Finish |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | P1 | (1, 2, 2) <= (3, 3, 2) | (3, 3, 2) | (2, 0, 0) | (5, 3, 2) | Finish[1] = true |
| 2 | P3 | (0, 1, 1) <= (5, 3, 2) | (5, 3, 2) | (2, 1, 1) | (7, 4, 3) | Finish[3] = true |
| 3 | P4 | (4, 3, 1) <= (7, 4, 3) | (7, 4, 3) | (0, 0, 2) | (7, 4, 5) | Finish[4] = true |
| 4 | P0 | (7, 4, 3) <= (7, 4, 5) | (7, 4, 5) | (0, 1, 0) | (7, 5, 5) | Finish[0] = true |
| 5 | P2 | (6, 0, 0) <= (7, 5, 5) | (7, 5, 5) | (3, 0, 2) | (10, 5, 7) | Finish[2] = true |

All Finish entries become true; **the original state is safe**, with sequence **P1, P3, P4, P0, P2** (source labels: P2, P4, P5, P1, P3). Other sequences can also be valid.

###### 3. Requests tested independently from the ORIGINAL state
Each row below starts again from the original Available = (3, 3, 2) and original Allocation and Need. A grant in one case is **not** carried into another. First check Request <= Need and Request <= Available componentwise; then tentatively update the matrices and run the safety test.

| Interpretation | Process (zero-based; chapter label) | Request | Request <= Need? | Request <= Available? | Tentative Available | Decision |
|:--|:--|:--|:--|:--|:--|:--|
| Chapter question | P0; source P1 | (1, 0, 0) | Yes: <= (7, 4, 3) | Yes | (2, 3, 2) | **Grant: safe** |
| Chapter answer vector, same source process | P0; source P1 | (1, 0, 2) | Yes: <= (7, 4, 3) | Yes | (2, 3, 0) | **Defer: unsafe** |
| Separate textbook-style variant | P1; source P2 | (1, 0, 2) | Yes: <= (1, 2, 2) | Yes | (2, 3, 0) | **Grant: safe** |
| Independent supplementary test | P4; source P5 | (3, 3, 0) | Yes: <= (4, 3, 1) | Yes | (0, 0, 2) | **Defer: unsafe** |
| Independent supplementary test | P0; source P1 | (0, 2, 0) | Yes: <= (7, 4, 3) | Yes | (3, 1, 2) | **Grant: safe** |

**Chapter-question case, P0 requests (1, 0, 0):** Tentative Allocation0 = (1, 1, 0); Need0 = (6, 4, 3); Work starts at (2, 3, 2). A complete safe trace is:

| Step | Process | Need <= Work? | Work before | Allocation released | Work after | Finish |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | P1 | (1, 2, 2) <= (2, 3, 2) | (2, 3, 2) | (2, 0, 0) | (4, 3, 2) | Finish[1] = true |
| 2 | P3 | (0, 1, 1) <= (4, 3, 2) | (4, 3, 2) | (2, 1, 1) | (6, 4, 3) | Finish[3] = true |
| 3 | P4 | (4, 3, 1) <= (6, 4, 3) | (6, 4, 3) | (0, 0, 2) | (6, 4, 5) | Finish[4] = true |
| 4 | P0 | (6, 4, 3) <= (6, 4, 5) | (6, 4, 5) | (1, 1, 0) | (7, 5, 5) | Finish[0] = true |
| 5 | P2 | (6, 0, 0) <= (7, 5, 5) | (7, 5, 5) | (3, 0, 2) | (10, 5, 7) | Finish[2] = true |

**Chapter-answer case, the SAME P0 requests (1, 0, 2):** Tentative Allocation0 = (1, 1, 2), Need0 = (6, 4, 1), Work = (2, 3, 0). P1 can finish, releasing (2, 0, 0), so Work becomes (4, 3, 0). P0 still needs (6, 4, 1), P2 needs (6, 0, 0), P3 needs (0, 1, 1), and P4 needs (4, 3, 1). **None can finish**; the tentative state is unsafe. Roll back the allocation and defer the request. This is **not** the same as a request by P1 in the zero-based table.

**Separate P1 variant, P1 requests (1, 0, 2):** Tentative Allocation1 = (3, 0, 2); Need1 = (0, 2, 0); Work = (2, 3, 0). The trace P1: (2, 3, 0) -> (5, 3, 2), P3 -> (7, 4, 3), P4 -> (7, 4, 5), P0 -> (7, 5, 5), P2 -> (10, 5, 7) proves safety. Grant this **different process's** request.

**P4 requests (3, 3, 0) from the original state:** Tentative Allocation4 = (3, 3, 2), Need4 = (1, 0, 1), Work = (0, 0, 2). No unfinished process can finish. Defer because the tentative state is **unsafe**, not because initial availability is insufficient.

**P0 requests (0, 2, 0) from the original state:** Tentative Allocation0 = (0, 3, 0), Need0 = (7, 2, 3), Work = (3, 1, 2). P3 -> Work (5, 2, 3), P1 -> (7, 2, 3), P2 -> (10, 2, 5), P0 -> (10, 5, 5), P4 -> (10, 5, 7). Thus **P3, P1, P2, P0, P4** is a valid safe sequence; grant. If instead this request occurs **after** granting the separate P1 (1, 0, 2) variant, Available = (2, 3, 0); a tentative P0 (0, 2, 0) leaves (2, 1, 0) and is unsafe. These are distinct starting states.

> **Source discrepancy:** `OS Chap 4 Deadlock.pdf`, PDF p. 21, asks about (1, 0, 0) for its P1; the worked answer on p. 25 changes the vector to (1, 0, 2) without the necessary safety demonstration. Its P1 corresponds to this table's P0. Preserve both printed vectors, and never attribute the safe textbook P1 (zero-based) variant to the chapter's P1.

#### Q3.4: Banker's Algorithm Numerical Problem 2 (Lab Exp 7 Problem 1 - 3-Process)
- **Lab-manual exercise (not a verified PYQ):** *Described in the supplied bank as SVKM's NMIMS Semester V Lab Manual, Experiment 7, Problem 1, 10 marks; original lab manual not supplied for checking.* The following is a normalized transcription of the bank's data.
- **Question:** Given the following Allocation, Max and Available data, calculate Need and determine whether the system is safe. Show the Work/Finish trace and a safe sequence.

**Snapshot at T0:**

| Process | Allocation (A, B, C) | Max (A, B, C) | Available (A, B, C) |
|:--|:--|:--|:--|
| P0 | 0, 0, 1 | 8, 4, 3 | 3, 2, 2 |
| P1 | 3, 2, 0 | 6, 2, 0 | - |
| P2 | 2, 1, 1 | 3, 3, 3 | - |

##### Complete solution

###### 1. Need = Max - Allocation
| Process | Allocation | Max | Need = Max - Allocation |
|:--|:--|:--|:--|
| P0 | (0, 0, 1) | (8, 4, 3) | (8, 4, 2) |
| P1 | (3, 2, 0) | (6, 2, 0) | (3, 0, 0) |
| P2 | (2, 1, 1) | (3, 3, 3) | (1, 2, 2) |

Row calculations: P0 (8, 4, 3) - (0, 0, 1) = (8, 4, 2); P1 (6, 2, 0) - (3, 2, 0) = (3, 0, 0); P2 (3, 3, 3) - (2, 1, 1) = (1, 2, 2).

```math
\mathrm{Need}=\begin{bmatrix}
8&4&2\\
3&0&0\\
1&2&2
\end{bmatrix}
```

###### 2. Safety check
Initialize Work = (3, 2, 2), Finish = [false, false, false].

| Step | Process | Need <= Work? | Work before | Allocation released | Work after | Finish |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | P1 | (3, 0, 0) <= (3, 2, 2) | (3, 2, 2) | (3, 2, 0) | (6, 4, 2) | Finish[1] = true |
| 2 | P2 | (1, 2, 2) <= (6, 4, 2) | (6, 4, 2) | (2, 1, 1) | (8, 5, 3) | Finish[2] = true |
| 3 | P0 | (8, 4, 2) <= (8, 5, 3) | (8, 5, 3) | (0, 0, 1) | (8, 5, 4) | Finish[0] = true |

All processes finish; the system is **safe**. One safe sequence is **P1, P2, P0**. Final Work = (8, 5, 4), consistent with Available + total Allocation.

#### Q3.5: Banker's Algorithm Numerical Problem 3 (Lab Exp 7 Problem 3 - 4-Resource)
- **Lab-manual exercise (not a verified PYQ):** *Described in the supplied bank as SVKM's NMIMS Semester V Lab Manual, Experiment 7, Problem 3, 10 marks; original lab manual not supplied for checking.* The following is a normalized transcription of the bank's data.
- **Question:** Calculate the Need matrix and derive a safe sequence from this four-resource snapshot.

**Snapshot at T0 (A, B, C, D):**

| Process | Allocation (A, B, C, D) | Max (A, B, C, D) | Available (A, B, C, D) |
|:--|:--|:--|:--|
| P0 | 0, 0, 1, 2 | 0, 0, 1, 2 | 1, 5, 2, 0 |
| P1 | 1, 0, 0, 0 | 1, 7, 5, 0 | - |
| P2 | 1, 3, 5, 4 | 2, 3, 5, 6 | - |
| P3 | 0, 6, 3, 2 | 0, 6, 5, 2 | - |
| P4 | 0, 0, 1, 4 | 0, 6, 5, 6 | - |

##### Complete solution

###### 1. Need = Max - Allocation
| Process | Allocation | Max | Need = Max - Allocation |
|:--|:--|:--|:--|
| P0 | (0, 0, 1, 2) | (0, 0, 1, 2) | (0, 0, 0, 0) |
| P1 | (1, 0, 0, 0) | (1, 7, 5, 0) | (0, 7, 5, 0) |
| P2 | (1, 3, 5, 4) | (2, 3, 5, 6) | (1, 0, 0, 2) |
| P3 | (0, 6, 3, 2) | (0, 6, 5, 2) | (0, 0, 2, 0) |
| P4 | (0, 0, 1, 4) | (0, 6, 5, 6) | (0, 6, 4, 2) |

Row calculations: P0 (0, 0, 1, 2) - (0, 0, 1, 2) = (0, 0, 0, 0); P1 (1, 7, 5, 0) - (1, 0, 0, 0) = (0, 7, 5, 0); P2 (2, 3, 5, 6) - (1, 3, 5, 4) = (1, 0, 0, 2); P3 (0, 6, 5, 2) - (0, 6, 3, 2) = (0, 0, 2, 0); P4 (0, 6, 5, 6) - (0, 0, 1, 4) = (0, 6, 4, 2).

```math
\mathrm{Need}=\begin{bmatrix}
0&0&0&0\\
0&7&5&0\\
1&0&0&2\\
0&0&2&0\\
0&6&4&2
\end{bmatrix}
```

###### 2. Safety check
Initialize Work = (1, 5, 2, 0), Finish = [false, false, false, false, false].

| Step | Process | Need <= Work? | Work before | Allocation released | Work after | Finish |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | P0 | (0, 0, 0, 0) <= (1, 5, 2, 0) | (1, 5, 2, 0) | (0, 0, 1, 2) | (1, 5, 3, 2) | Finish[0] = true |
| 2 | P2 | (1, 0, 0, 2) <= (1, 5, 3, 2) | (1, 5, 3, 2) | (1, 3, 5, 4) | (2, 8, 8, 6) | Finish[2] = true |
| 3 | P3 | (0, 0, 2, 0) <= (2, 8, 8, 6) | (2, 8, 8, 6) | (0, 6, 3, 2) | (2, 14, 11, 8) | Finish[3] = true |
| 4 | P4 | (0, 6, 4, 2) <= (2, 14, 11, 8) | (2, 14, 11, 8) | (0, 0, 1, 4) | (2, 14, 12, 12) | Finish[4] = true |
| 5 | P1 | (0, 7, 5, 0) <= (2, 14, 12, 12) | (2, 14, 12, 12) | (1, 0, 0, 0) | (3, 14, 12, 12) | Finish[1] = true |

All processes finish; the system is **safe**. One safe sequence is **P0, P2, P3, P4, P1**. Final Work = (3, 14, 12, 12), consistent with Available + total Allocation.

### Topic 4: Deadlock Detection & Recovery

#### Q4.1: Deadlock Detection Algorithms: Wait-For Graph vs. Multi-Instance
- **Original Question 1 (exam attribution unverified):** *SVKM'S NMIMS Semester V Special Re-Exam (2022-2023) [Q4b - 5 Marks]:* "Explain deadlock detection algorithm for multiple resource instances."
- **Reported question 2 (unverified):** *GTU June 2015 [Marks 5]:* "How is deadlock detected in a system with single-instance resource types versus multiple-instance resource types?"

##### Answer (5 Marks):

###### 1. Single-Instance Resources: Wait-For Graph (WFG) Algorithm
- **Mechanism:** If all resources have a single instance, the Resource-Allocation Graph is collapsed into a **Wait-For Graph (WFG)** by removing resource nodes $R_j$. An edge $P_i     o P_j$ exists in a WFG if process $P_i$ is waiting for process $P_j$ to release a resource.
- **Detection Protocol:** The OS periodically runs a cycle-detection algorithm (e.g., Depth-First Search) on the WFG. An edge cycle in a WFG indicates **deadlock**. Time complexity: $O(n^2)$ for $n$ vertices.

```text
Resource Allocation Graph (RAG)           Collapsed Wait-For Graph (WFG)

   (P1) ---> [R1] ---> (P2)                     (P1) ---------> (P2)
    ^                   |                        ^               |
    |                   v                        |               |
   [R2] <--------------(P2)                      +--------------(P2)
```

###### 2. Multiple-Instance Resources: Detection Algorithm
For multiple-instance resources, the detection algorithm uses data structures similar to Banker's algorithm (`Available[m]`, `Allocation[n][m]`, `Request[n][m]`), but evaluates **actual current Requests** instead of declared maximum demands (`Need`).

###### Algorithm Steps:
1. Initialize $\text{Work} = \text{Available}$.
2. For $i = 0 \dots n-1$:
   - If $\text{Allocation}[i] 
eq \mathbf{0}$, set $\text{Finish}[i] = \text{False}$; else set $\text{Finish}[i] = \text{True}$.
3. Find an index $i$ such that $\text{Finish}[i] == \text{False}$ and $\text{Request}_i \le \text{Work}$.
   - If found, update $\text{Work} = \text{Work} + \text{Allocation}_i$, set $\text{Finish}[i] = \text{True}$, and repeat Step 3.
4. If $\text{Finish}[i] == \text{False}$ for any $i$, **the system is DEADLOCKED**, and process $P_i$ is deadlocked.

---

#### Q4.2: Deadlock Recovery Strategies: Termination & Preemption
- **Original Question (exam attribution unverified):** *SVKM'S NMIMS Semester V Re-Exam (2022-2023) [Q4c - 5 Marks]:* "Describe the methods for recovering from a deadlock state. Discuss the issues involved in resource preemption."

##### Answer (5 Marks):

###### 1. Recovery Methods Overview
When a detection algorithm identifies a deadlocked state, the system must recover using one of two primary strategies:

###### Option A: Process Termination
1. **Abort All Deadlocked Processes:** Completely clears the deadlock, but incurs high computation loss as completed work in all aborted processes is destroyed.
2. **Abort One Process at a Time:** Abort one deadlocked process, rerun deadlock detection, and repeat until the deadlock cycle is broken.
   - *Victim Selection Criteria:* Choose process with lowest priority, lowest runtime so far, lowest held resources, or non-interactive batch process.

###### Option B: Resource Preemption
Progressively preempt resources from processes and allocate them to other processes until the deadlock cycle is broken.

###### 2. Three Critical Issues in Resource Preemption
1. **Selecting a Victim:**
   - Which resources and processes should be preempted? Must evaluate cost factors such as process runtime, holding resource counts, and priority to minimize cost.
2. **Rollback:**
   - Once a resource is preempted from a process, what should be done with that process?
   - **Total Rollback:** Abort the process and restart it from the beginning.
   - **Partial Rollback (Checkpointing):** Roll back the process to its last saved safe checkpoint state and resume from there.
3. **Starvation Prevention:**
   - How to ensure that the same process is not repeatedly picked as a victim?
   - If victim selection is strictly cost-based, a process holding heavy resources may be repeatedly preempted and starve indefinitely.
   - **Solution:** Include a **preemption count** in the process cost factor. As preemption count increases, its priority for being picked as a victim decreases.

---

### Topic 5: The Dining Philosophers Problem

#### Q5.1: Dining Philosophers Problem & Naive Semaphore Failure
- **Original Question (exam attribution unverified):** *SVKM'S NMIMS Semester V Final Exam (2023-2024) [Q3b - 5 Marks]:* "Explain the Dining Philosophers problem. Show how a naive semaphore implementation causes deadlock."

##### Answer (5 Marks):

###### 1. Problem Statement & Constraints
The **Dining Philosophers Problem** is a classical synchronization problem modeling resource allocation among concurrent processes:
- 5 Philosophers sit around a circular table with one central bowl of rice.
- 5 single chopsticks (`chopstick[0..4]`) are placed between adjacent philosophers.
- A philosopher alternates between **Thinking** and **Eating**.
- To eat, a philosopher must acquire **both adjacent chopsticks** (left chopstick and right chopstick).

```text
                   Philosopher 0
                     (P0)
                 /          \
         Chopstick 4      Chopstick 0
               /              \
  Philosopher 4                Philosopher 1
      (P4)                          (P1)
        |                            |
  Chopstick 3                      Chopstick 1
        \                          /
         Philosopher 3    Philosopher 2
             (P3) ------Chopstick 2------ (P2)
```

###### 2. Naive Semaphore Solution & Deadlock Trace

```c
// Shared Initialization
semaphore chopstick[5] = {1, 1, 1, 1, 1};

// Philosopher i Code
void philosopher(int i) {
    while (true) {
        think();
        
        semWait(chopstick[i]);             // Pick up left chopstick
        semWait(chopstick[(i + 1) % 5]);   // Pick up right chopstick
        
        eat();
        
        semSignal(chopstick[i]);           // Release left chopstick
        semSignal(chopstick[(i + 1) % 5]); // Release right chopstick
    }
}
```

###### Deadlock Trace:
1. All 5 philosophers ($P_0, P_1, P_2, P_3, P_4$) become hungry at the exact same time.
2. Each philosopher $P_i$ executes `semWait(chopstick[i])` concurrently.
3. Every philosopher successfully acquires their left chopstick. All `chopstick` semaphores drop to `0`.
4. Next, every philosopher $P_i$ executes `semWait(chopstick[(i + 1) % 5])` to pick up their right chopstick.
5. Since every right chopstick is already held as a left chopstick by its neighbor, **all 5 philosophers block permanently**.
6. **Result:** A circular wait state $P_0     o P_1     o P_2     o P_3     o P_4     o P_0$ is created. **System is Deadlocked.**

---

#### Q5.2: Deadlock-Free Semaphore & Monitor Solutions
- **Original Question (exam attribution unverified):** *SVKM'S NMIMS Semester V Special Re-Exam (2022-2023) [Q3b - 10 Marks]:* "Provide a deadlock-free monitor solution for the Dining Philosophers problem. Explain its working and discuss whether it guarantees freedom from starvation."

##### Answer (Complete 10-Mark Answer):

###### 1. Deadlock Prevention Strategies for Dining Philosophers (2 Marks)
Deadlock can be prevented using three main architectural modifications:
1. **Capacity Limit:** Allow at most 4 philosophers to sit at the table simultaneously.
2. **Asymmetric Pickup:** Odd-numbered philosophers pick up left chopstick first, then right. Even-numbered philosophers pick up right chopstick first, then left.
3. **Atomic Both-or-Nothing Acquisition (Monitor Approach):** Allow a philosopher to pick up chopsticks only if **both chopsticks are available simultaneously**.

###### 2. Deadlock-Free Monitor Pseudocode (Mesa-Style) (6 Marks)

```c
monitor DiningPhilosophers {
    enum {THINKING, HUNGRY, EATING} state[5];
    condition self[5]; // Condition variable per philosopher

    void pickup(int i) {
        state[i] = HUNGRY;
        test(i); // Attempt to acquire both chopsticks
        
        // Mesa-style recheck loop: wait if state is not EATING
        while (state[i] != EATING) {
            self[i].wait();
        }
    }

    void putdown(int i) {
        state[i] = THINKING;
        
        // Test left and right neighbors to signal them if hungry
        test((i + 4) % 5); // Left neighbor
        test((i + 1) % 5); // Right neighbor
    }

    void test(int i) {
        // Philosopher i can eat ONLY if hungry AND both neighbors are NOT eating
        if ((state[i] == HUNGRY) &&
            (state[(i + 4) % 5] != EATING) &&
            (state[(i + 1) % 5] != EATING)) {
            
            state[i] = EATING;
            self[i].signal(); // Unblock philosopher i
        }
    }

    // Monitor Initialization
    initialization_code() {
        for (int i = 0; i < 5; i++) {
            state[i] = THINKING;
        }
    }
}
```

**Philosopher calling loop (required to complete the monitor solution):**

```c
void philosopher(int i) {
    while (true) {
        think();
        DiningPhilosophers.pickup(i);
        eat();
        DiningPhilosophers.putdown(i);
    }
}
```

###### 3. Deadlock Freedom vs. Starvation Freedom Analysis (2 Marks)
- **Deadlock Freedom:** **GUARANTEED.** Because a philosopher transitions to `EATING` only if both adjacent chopsticks are free simultaneously in an atomic monitor test, no philosopher can hold one chopstick while waiting for another. Circular wait is impossible.
- **Starvation Freedom:** **NOT GUARANTEED.** A deadlock-free solution does **not** automatically prevent starvation. A hungry philosopher $P_i$ can starve indefinitely if its left neighbor $P_{i-1}$ and right neighbor $P_{i+1}$ alternate eating in an overlapping sequence such that at least one neighbor is always in the `EATING` state whenever $P_i$ executes `test()`.

---

## 6. SECTION II: ADDITIONAL TOPICS IN SUPPLIED TEACHING MATERIALS

### Topic A1: Ostrich Algorithm & Trade-offs in Modern Operating Systems

#### QA1.1: The Ostrich Algorithm
- **Reported question (unverified):** *Tanenbaum OS Textbook / Course Notes [Marks 5]:* "Explain the Ostrich Algorithm for deadlock handling. Why do commercial OS like UNIX and Windows adopt this approach?"

##### Answer (5 Marks):

###### 1. Definition
The **Ostrich Algorithm** is a deadlock handling strategy where the operating system simply **ignores the deadlock problem entirely**—sticking its head in the sand like an ostrich and pretending deadlocks never occur.

###### 2. Justification & Trade-offs in Commercial OS
1. **Rarity vs. Prevention Cost:** In general-purpose operating systems (like Linux, Windows, macOS), deadlocks occur very rarely.
2. **Performance Overhead:** Operating systems could eliminate deadlocks using Banker's algorithm or strict linear ordering, but the continuous runtime CPU and memory overhead of these algorithms would severely slow down daily system operations.
3. **Pragmatic Engineering Trade-off:** OS designers trade off a rare deadlock occurrence (which can be resolved by terminating a stuck user application or rebooting) for **significantly higher everyday system performance and execution speed**.
4. **Safety-Critical Exception:** Real-time embedded systems (e.g., flight controls, medical devices, automotive controllers) must assess deadlock risks explicitly; this text does not establish a universal policy for every safety-critical system.

---

## 7. SECTION III: QUICK REVISION CHECKLIST & ALGORITHM RECAP

### 1. Matrix & Vector Invariants in Banker's Algorithm
```math
\mathrm{Need}[i][j]=\mathrm{Max}[i][j]-\mathrm{Allocation}[i][j]
```
```math
\mathrm{Total}(R_j)=\mathrm{Available}[j]+\sum_{i=0}^{n-1}\mathrm{Allocation}[i][j]
```

### 2. Quick Revision Checklist
- [ ] **Coffman 4 Conditions:** Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait.
- [ ] **RAG Cycles:** Cycle $\implies$ Deadlock (Single-instance); Cycle $
eq$ Deadlock (Multi-instance).
- [ ] **Prevention:** Invalidate 1 condition. Circular wait invalidated via global linear ordering $F(R_i)$.
- [ ] **Avoidance:** Banker's Algorithm requires upfront Max demand declarations; stays in Safe State.
- [ ] **Need Matrix:** Always verify $\text{Need} = \text{Max} - \text{Allocation}$.
- [ ] **Request Checks:** Verify $\text{Request} \le \text{Need}$ AND $\text{Request} \le \text{Available}$.
- [ ] **Detection:** WFG cycle check for single instance; Work-Finish algorithm for multi-instance.
- [ ] **Recovery:** Process termination (abort all vs. abort 1-by-1) or resource preemption (victim selection, rollback, starvation prevention).
- [ ] **Dining Philosophers:** Naive semaphore deadlocks; monitor solution guarantees deadlock freedom BUT NOT starvation freedom.
