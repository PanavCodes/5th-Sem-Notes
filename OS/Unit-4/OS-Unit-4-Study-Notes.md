# Operating Systems: Unit 4 — Deadlock Study Notes

## Table of Contents
- [1. Principles of Deadlock](#1-principles-of-deadlock)
  - [1.1 Definition of Deadlock & Simple Process-Resource Example](#11-definition-of-deadlock-simple-process-resource-example)
    - [Simple Process-Resource Example](#simple-process-resource-example)
  - [1.2 Reusable vs. Consumable Resources](#12-reusable-vs-consumable-resources)
    - [1. Reusable Resources](#1-reusable-resources)
    - [2. Consumable Resources](#2-consumable-resources)
  - [1.3 The Four Necessary Conditions for Deadlock](#13-the-four-necessary-conditions-for-deadlock)
  - [1.4 Resource-Allocation Graph (RAG) Framework](#14-resource-allocation-graph-rag-framework)
    - [Graph Vertices ($V$)](#graph-vertices-v)
    - [Graph Edges ($E$)](#graph-edges-e)
  - [1.5 Meaning of Cycles: Single-Instance vs. Multi-Instance Resources](#15-meaning-of-cycles-single-instance-vs-multi-instance-resources)
    - [1. Single Instance Per Resource Type](#1-single-instance-per-resource-type)
    - [2. Multiple Instances Per Resource Type](#2-multiple-instances-per-resource-type)
  - [1.6 Deadlock vs. Starvation](#16-deadlock-vs-starvation)
  - [1.7 Safe States, Unsafe States, and Deadlocked States](#17-safe-states-unsafe-states-and-deadlocked-states)
    - [State Definitions](#state-definitions)
    - [State Hierarchy Relationship](#state-hierarchy-relationship)
  - [1.8 Exam Summary & Common Mistakes](#18-exam-summary-common-mistakes)
- [2. Deadlock Prevention](#2-deadlock-prevention)
  - [2.1 Overview & Core Strategy](#21-overview-core-strategy)
  - [2.2 Invalidation of Mutual Exclusion](#22-invalidation-of-mutual-exclusion)
  - [2.3 Invalidation of Hold and Wait](#23-invalidation-of-hold-and-wait)
  - [2.4 Invalidation of No Preemption](#24-invalidation-of-no-preemption)
  - [2.5 Invalidation of Circular Wait](#25-invalidation-of-circular-wait)
    - [Mathematical Proof of Prevention](#mathematical-proof-of-prevention)
  - [2.6 Comprehensive Prevention Comparison Table](#26-comprehensive-prevention-comparison-table)
  - [2.7 Exam Summary & Common Mistakes](#27-exam-summary-common-mistakes)
- [3. Deadlock Avoidance & Banker's Algorithm](#3-deadlock-avoidance-bankers-algorithm)
  - [3.1 Principles of Deadlock Avoidance](#31-principles-of-deadlock-avoidance)
    - [Required Information](#required-information)
  - [3.2 Safe State & Safe Sequence Concepts](#32-safe-state-safe-sequence-concepts)
  - [3.3 Data Structures for Banker's Algorithm](#33-data-structures-for-bankers-algorithm)
  - [3.4 The Safety Algorithm (Complete Pseudocode)](#34-the-safety-algorithm-complete-pseudocode)
  - [3.5 The Resource-Request Algorithm (Complete Pseudocode)](#35-the-resource-request-algorithm-complete-pseudocode)
  - [3.6 Fully Worked Step-by-Step Numerical Example](#36-fully-worked-step-by-step-numerical-example)
    - [3.6.1 Initial System Snapshot & Need Matrix Calculation](#361-initial-system-snapshot-need-matrix-calculation)
    - [3.6.2 Safety Check at T0 & Safe Sequence Derivation](#362-safety-check-at-t0-safe-sequence-derivation)
    - [3.6.3 Processing Tentative Resource Requests](#363-processing-tentative-resource-requests)
    - [3.6.4 Discrepancy Flag & Source Resolution](#364-discrepancy-flag-source-resolution)
  - [3.7 Limitations of Banker's Algorithm](#37-limitations-of-bankers-algorithm)
  - [3.8 Exam Summary & Common Mistakes](#38-exam-summary-common-mistakes)
- [4. Deadlock Detection and Recovery](#4-deadlock-detection-and-recovery)
  - [4.1 Deadlock Detection Strategy](#41-deadlock-detection-strategy)
  - [4.2 Detection for Single-Instance Resources (Wait-For Graph)](#42-detection-for-single-instance-resources-wait-for-graph)
    - [Wait-For Graph Construction](#wait-for-graph-construction)
  - [4.3 Detection for Multiple-Instance Resources](#43-detection-for-multiple-instance-resources)
    - [Data Structures](#data-structures)
    - [Detection Algorithm Pseudocode](#detection-algorithm-pseudocode)
  - [4.4 Detection Frequency & System Overhead](#44-detection-frequency-system-overhead)
  - [4.5 Recovery Strategies](#45-recovery-strategies)
    - [4.5.1 Process Termination Approaches](#451-process-termination-approaches)
    - [4.5.2 Resource Preemption & Issues](#452-resource-preemption-issues)
  - [4.6 Exam Summary & Common Mistakes](#46-exam-summary-common-mistakes)
- [5. The Dining Philosophers Problem](#5-the-dining-philosophers-problem)
  - [5.1 Problem Statement & Resource Constraints](#51-problem-statement-resource-constraints)
    - [Problem Rules](#problem-rules)
  - [5.2 Naive Semaphore Implementation & Deadlock Analysis](#52-naive-semaphore-implementation-deadlock-analysis)
    - [Why the Naive Solution Fails (Deadlock Scenario)](#why-the-naive-solution-fails-deadlock-scenario)
  - [5.3 Deadlock-Free Solutions Using Semaphores](#53-deadlock-free-solutions-using-semaphores)
    - [Option 1: Limit Seated Philosophers (Table Attendant)](#option-1-limit-seated-philosophers-table-attendant)
    - [Option 2: Asymmetric Chopstick Pickup](#option-2-asymmetric-chopstick-pickup)
  - [5.4 Deadlock-Free Solution Using Monitors](#54-deadlock-free-solution-using-monitors)
  - [5.5 Deadlock Freedom vs. Starvation Freedom Analysis](#55-deadlock-freedom-vs-starvation-freedom-analysis)
  - [5.6 Exam Summary & Common Mistakes](#56-exam-summary-common-mistakes)
- [6. Comprehensive Unit 4 Comparison Table](#6-comprehensive-unit-4-comparison-table)
- [7. Formula & Algorithm Pseudocode Quick Recap](#7-formula-algorithm-pseudocode-quick-recap)
  - [1. Need Matrix Equation](#1-need-matrix-equation)
  - [2. Available Vector Calculation](#2-available-vector-calculation)
  - [3. Safety Algorithm Invariant](#3-safety-algorithm-invariant)
  - [4. Resource-Request Conditions](#4-resource-request-conditions)
- [8. Representative Exam Question Patterns & Model Answers](#8-representative-exam-question-patterns-model-answers)
  - [Pattern 1: Four Necessary Conditions & Prevention Strategies (10 Marks)](#pattern-1-four-necessary-conditions-prevention-strategies-10-marks)
  - [Pattern 2: Banker's Algorithm Numerical Problem (10 Marks)](#pattern-2-bankers-algorithm-numerical-problem-10-marks)
  - [Pattern 3: Dining Philosophers Monitor Solution (10 Marks)](#pattern-3-dining-philosophers-monitor-solution-10-marks)
- [9. Quick Revision Checklist](#9-quick-revision-checklist)

---

## 1. Principles of Deadlock

### 1.1 Definition of Deadlock & Simple Process-Resource Example
**Definition:** A **deadlock** is a permanent system state in which a set of concurrent processes is completely blocked because every process in the set holds one or more non-shareable resources while waiting to acquire another resource currently held by another blocked process in the same set. Since no waiting process can proceed or release its held resources without external intervention, execution grinds to a total halt *(Silberschatz et al., Chap. 7; OS Chap 4 Deadlock.pdf, p. 1)*.

#### Simple Process-Resource Example
Consider two processes, $P_1$ and $P_2$, and two exclusive system resources, a **Printer ($R_1$)** and a **Disk Drive ($R_2$)**:
1. $P_1$ requests and is allocated the Printer ($R_1$).
2. $P_2$ requests and is allocated the Disk Drive ($R_2$).
3. $P_1$ requests the Disk Drive ($R_2$), but must wait because $R_2$ is currently held by $P_2$.
4. $P_2$ requests the Printer ($R_1$), but must wait because $R_1$ is currently held by $P_1$.

```text
  [Process P1]  --- Holds --->  [Printer (R1)]  <--- Requests ---  [Process P2]
       |                                                                |
   Requests                                                           Holds
       |                                                                |
       v                                                                v
[Disk Drive (R2)] <----------------------------------------------- [Process P2]
```

**Result:** $P_1$ is waiting for $P_2$, and $P_2$ is waiting for $P_1$. Neither process can ever release its resource, resulting in a circular wait deadlock.

---

### 1.2 Reusable vs. Consumable Resources
Operating systems manage resources that fall into two broad structural categories *(Stallings, Chap. 6; Nutt, Chap. 10)*:

#### 1. Reusable Resources
- **Definition:** A reusable resource is a physical or logical unit that can be safely used by one process at a time and is **not consumed or destroyed** by that usage. Once a process completes its task, it releases the resource back to the system pool for reassignment to other processes.
- **Examples:** CPU time slices, main memory partitions, secondary storage space, magnetic tape drives, I/O devices (printers, scanners), semaphores, and database file locks.
- **Deadlock Context:** Deadlocks with reusable resources typically arise when processes hold a subset of required resources and demand additional units held by competitors.

#### 2. Consumable Resources
- **Definition:** A consumable resource is a dynamic entity created (produced) by one process and destroyed (consumed) by another process upon receipt. There is no fixed total quantity of consumable resources in the system.
- **Examples:** Hardware interrupts, IPC signals, messages in message-passing mailboxes, network packets, and data buffers.
- **Deadlock Context:** Deadlock occurs when a consumer process blocks waiting for a message/signal that will never be produced because the producer process is itself blocked waiting for another resource or signal *(Stallings, Sec. 6.1)*.

---

### 1.3 The Four Necessary Conditions for Deadlock
According to **Edward G. Coffman Jr. (1971)**, the following **four conditions are necessary for deadlock and must hold simultaneously** in a system *(Silberschatz et al., Sec. 7.2)*:

1. **Mutual Exclusion:**
   - At least one resource must be held in a non-shareable mode. Only one process can use an instance of the resource at any given time. If another process requests that resource, the requesting process must be delayed until the resource is released.
2. **Hold and Wait:**
   - A process must currently hold at least one resource while simultaneously waiting to acquire additional resources that are currently being held by other processes.
3. **No Preemption:**
   - Resources cannot be forcibly preempted from a process. A resource can be released only voluntarily by the process holding it after that process has completed its task.
4. **Circular Wait:**
   - A closed chain of processes $\{P_0, P_1, \dots, P_n\}$ exists such that $P_0$ is waiting for a resource held by $P_1$, $P_1$ is waiting for a resource held by $P_2$, $\dots$, $P_{n-1}$ is waiting for a resource held by $P_n$, and $P_n$ is waiting for a resource held by $P_0$.

> **Exam Note:** All four are necessary; their presence alone does not prove that the current allocation is deadlocked, especially with multiple resource instances.

---

### 1.4 Resource-Allocation Graph (RAG) Framework
A **Resource-Allocation Graph (RAG)** is a directed graph $G = (V, E)$ used to formally model system states, process requests, and resource assignments *(Silberschatz et al., Sec. 7.2.2)*.

#### Graph Vertices ($V$)
The vertex set $V$ is partitioned into two distinct node types:
- **Process Nodes ($P = \{P_1, P_2, \dots, P_n\}$):** Drawn as circles `(O)`. Represents active processes.
- **Resource Nodes ($R = \{R_1, R_2, \dots, R_m\}$):** Drawn as rectangles `[ ]`. Inside each rectangle, individual resource instances are represented as dots `•`.

#### Graph Edges ($E$)
- **Request Edge ($P_i 	o R_j$):** A directed arrow from process $P_i$ to resource $R_j$. Indicates that $P_i$ has requested an instance of $R_j$ and is currently waiting.
- **Assignment Edge ($R_j 	o P_i$):** A directed arrow from an instance dot inside resource $R_j$ to process $P_i$. Indicates that an instance of $R_j$ has been allocated to $P_i$.

```text
  Request Edge:    (P1) ---------> [ R1 ]     (P1 is waiting for R1)
  Assignment Edge: [ R2 • ] ------> (P2)     (Instance of R2 is held by P2)
```

---

### 1.5 Meaning of Cycles: Single-Instance vs. Multi-Instance Resources
The relationship between a cycle in a Resource-Allocation Graph and the presence of a deadlock depends strictly on the number of instances available per resource type:

#### 1. Single Instance Per Resource Type
- **Rule:** A cycle in a single-instance RAG is a **necessary AND sufficient** condition for deadlock.
- **Explanation:** If every resource node contains exactly one instance, every cycle directly represents an unbreakable circular wait.
- **Theorem:**
$$	ext{Cycle in Single-Instance RAG} \iff 	ext{System is Deadlocked}$$

```text
(P1) ----> [R1 •] ----> (P2)
 ^                        |
 |                        v
 +-------- [R2 •] <-------+      <-- CYCLE EXISTS = DEADLOCK!
```

#### 2. Multiple Instances Per Resource Type
- **Rule:** A cycle in a multi-instance RAG is a **necessary BUT NOT sufficient** condition for deadlock.
- **Explanation:** A cycle indicates the *possibility* of a deadlock. However, if an instance of a resource involved in the cycle is also assigned to an outside process that is not part of the cycle, that outside process may finish, release its resource instance, break the cycle, and allow waiting processes to proceed.
- **Theorem:**
$$	ext{Cycle in Multi-Instance RAG} \implies 	ext{Possible Deadlock (Not Guaranteed)}$$

---

### 1.6 Deadlock vs. Starvation
While both conditions cause execution delays, they represent fundamentally different system pathologies:

| Aspect / Property | Deadlock | Starvation (Indefinite Blocking) |
| :--- | :--- | :--- |
| **Definition** | Two or more processes are permanently blocked waiting for resources held by each other. | A runnable process is indefinitely delayed from acquiring a needed resource due to scheduling biases. |
| **Cause** | Circular dependency among competing processes. | Unfair scheduling algorithms (e.g., strict priority or unconstrained reader preference). |
| **Process State** | Processes are in a **Blocked / Waiting** state; zero progress can be made. | Process is in a **Ready / Waiting** state, but continually bypassed by higher-priority tasks. |
| **Resolution** | Requires explicit OS intervention (process termination or resource preemption). | Resolved automatically when higher-priority workload decreases or aging is applied. |
| **System Scope** | Involves a closed set of mutually dependent processes. | Can affect a single isolated process while the rest of the system runs efficiently. |

---

### 1.7 Safe States, Unsafe States, and Deadlocked States
Deadlock avoidance algorithms monitor state transitions to ensure the system never enters an unsafe state *(Silberschatz et al., Sec. 7.5.1; Tanenbaum, Sec. 6.4)*:

#### State Definitions
1. **Safe State:**
   - A state is **safe** if there exists at least one **safe sequence** $\langle P_1, P_2, \dots, P_n 
angle$ of processes such that, for each process $P_i$, the maximum additional resources that $P_i$ may request can be satisfied by the currently available resources plus the resources already held by all preceding processes $P_j$ (where $j < i$).
2. **Unsafe State:**
   - A state is **unsafe** if no safe sequence exists. In an unsafe state, the operating system cannot guarantee that all processes will eventually finish without a deadlock occurring if every process suddenly requests its declared maximum resource needs.
3. **Deadlocked State:**
   - A state where a subset of processes is actively deadlocked (a subset of unsafe states).

#### State Hierarchy Relationship
$$	ext{Safe State} \subset 	ext{Unsafe State} \supset 	ext{Deadlocked State}$$

```text
All resource-allocation states
+----------------------+   +-------------------------------------+
| SAFE STATES          |   | UNSAFE STATES                       |
| At least one safe    |   | No safe sequence                    |
| sequence exists      |   | +-------------------------------+   |
|                      |   | | DEADLOCKED STATES             |   |
|                      |   | | Processes cannot progress     |   |
|                      |   | +-------------------------------+   |
+----------------------+   +-------------------------------------+
Safe and unsafe are disjoint; deadlocked is a subset of unsafe.
```

> **CRITICAL DISTINCTION:** An **unsafe state is NOT necessarily a deadlocked state**. An unsafe state simply means the OS has lost the ability to *guarantee* deadlock avoidance under worst-case process behavior. The system may still avoid deadlock if processes do not request their full maximum claims simultaneously.

---

### 1.8 Exam Summary & Common Mistakes
- **Concise Summary:** Deadlock is a permanent blockage caused by circular resource dependencies among processes. It requires four concurrent conditions: Mutual Exclusion, Hold & Wait, No Preemption, and Circular Wait.
- **Common Student Mistakes:**
  - *Mistake 1:* Claiming that a cycle in a Resource-Allocation Graph always implies a deadlock. *(Correction: Cycles guarantee deadlock ONLY in single-instance resource systems; in multi-instance systems, a cycle is merely a necessary condition).*
  - *Mistake 2:* Equating an unsafe state directly to a deadlocked state. *(Correction: An unsafe state is a state from which deadlock CAN occur if worst-case requests arrive, but execution is not yet deadlocked).*

---

## 2. Deadlock Prevention

### 2.1 Overview & Core Strategy
**Deadlock Prevention** is a static design-time strategy that prevents deadlocks by establishing system constraints that **eliminate at least one of the four necessary Coffman conditions** *(Silberschatz et al., Sec. 7.4)*. By ensuring that at least one condition can never hold, deadlocks become structurally impossible.

---

### 2.2 Invalidation of Mutual Exclusion
- **Strategy:** Make all system resources completely shareable so that no process ever requires exclusive access.
- **Implementation:** Read-only files, shared memory segments, or virtualizing non-shareable hardware using spooling (e.g., a print spooler converts a physical printer into a shareable daemon).
- **Limitations & Disadvantages:**
  - **Inapplicable to most intrinsic hardware:** Many physical resources (e.g., tape drives, writeable files, CPU registers) are inherently non-shareable and cannot be virtualized without introducing race conditions.

---

### 2.3 Invalidation of Hold and Wait
- **Strategy:** Ensure that whenever a process requests resources, it does not currently hold any other resources.
- **Implementation Options:**
  1. **Protocol 1 (All-at-Once Allocation):** A process must declare and request all its required resources simultaneously before commencing execution. If even one resource is unavailable, none are granted, and the process waits.
  2. **Protocol 2 (Incremental Release-and-Request):** A process can request additional resources only after it has completely released all currently allocated resources.
- **Limitations & Disadvantages:**
  - **Severe Resource Underutilization:** Resources allocated for an entire run may be used for only a fraction of execution time (e.g., a process holding a tape drive for 2 hours but using it for 5 minutes).
  - **High Risk of Starvation:** Processes requiring multiple popular resources may wait indefinitely because all requested units are rarely free at the same instant.

---

### 2.4 Invalidation of No Preemption
- **Strategy:** Allow the operating system to forcibly preempt resources currently allocated to a process.
- **Implementation Protocols:**
  - If a process $P_1$ holding resources requests an additional resource $R_x$ that is currently unavailable, $P_1$ enters a waiting state and **all its currently held resources are implicitly preempted** and added to the free pool.
  - Alternatively, if $R_x$ is held by another waiting process $P_2$, $R_x$ is preempted from $P_2$ and allocated to $P_1$.
- **Limitations & Disadvantages:**
  - **Limited Application Scope:** Preemption can only be applied to resources whose state can be easily saved and restored later without corruption (e.g., CPU registers, main memory pages).
  - **Inapplicable to State-Full Hardware:** Cannot be applied to resources like printers, tape drives, or database transactions without invalidating execution integrity.

---

### 2.5 Invalidation of Circular Wait
- **Strategy:** Enforce a strict global linear ordering on all system resource types.
- **Implementation:**
  - Define a global 1-to-1 indexing function $F: R 	o \mathbb{N}$ that maps every resource type $R_i$ to a unique integer (e.g., $F(	ext{Tape Drive}) = 1$, $F(	ext{Disk}) = 2$, $F(	ext{Printer}) = 3$).
  - **Rule:** A process can request resource $R_j$ if and only if $F(R_j) > F(R_i)$ for all resources $R_i$ currently held by that process. Alternatively, if a process needs a lower-numbered resource, it must first release all higher-numbered resources.

#### Mathematical Proof of Prevention
Suppose a circular wait exists involving processes $\{P_0, P_1, \dots, P_n\}$ and resources $\{R_0, R_1, \dots, R_n\}$ where $P_i$ holds $R_i$ and requests $R_{i+1}$. Under the ordering rule:
$$F(R_0) < F(R_1) < F(R_2) < \dots < F(R_n) < F(R_0)$$
This implies $F(R_0) < F(R_0)$, which is a logical contradiction. Therefore, no circular wait can ever form.

- **Limitations & Disadvantages:**
  - **Restricts Application Flexibility:** Forces developers to acquire resources in an arbitrary global order that may not align with natural program logic, leading to artificial delays.

---

### 2.6 Comprehensive Prevention Comparison Table

| Condition Targeted | Prevention Mechanism | System Impact & Disadvantages |
| :--- | :--- | :--- |
| **Mutual Exclusion** | Virtualize non-shareable resources via spooling/sharing. | Inapplicable to inherently exclusive hardware (tape drives, mutexes). |
| **Hold and Wait** | Require process to request all resources upfront OR release all before requesting. | Severe resource underutilization; high starvation risk for multi-resource tasks. |
| **No Preemption** | Forcibly preempt held resources if new request cannot be satisfied. | Applicable only to saveable/restorable state resources (CPU, Memory). |
| **Circular Wait** | Enforce global linear numerical ordering $F(R_i)$ on resource requests. | Restricts programming flexibility; potential efficiency loss if ordering differs from usage order. |

---

### 2.7 Exam Summary & Common Mistakes
- **Concise Summary:** Deadlock prevention eliminates deadlocks by invalidating at least one of Coffman's four conditions. Preventing Circular Wait via global linear resource ordering is the most practical strategy.
- **Common Student Mistakes:**
  - *Mistake:* Recommending "disabling interrupts" as a general deadlock prevention technique. *(Correction: Disabling interrupts provides mutual exclusion for kernel data structures, but does NOT prevent resource deadlocks in user-level applications).*

---

## 3. Deadlock Avoidance & Banker's Algorithm

### 3.1 Principles of Deadlock Avoidance
Unlike static prevention, **Deadlock Avoidance** is a dynamic runtime strategy that allows the four necessary conditions to exist, but carefully examines every resource request before granting it. The OS grants a request **only if the resulting system state remains in a safe state** *(Silberschatz et al., Sec. 7.5)*.

#### Required Information
To perform deadlock avoidance, the operating system requires prior information:
- Each process must declare its **maximum resource claim** upfront upon entering the system.
- The OS tracks current resource allocations, available units, and maximum potential future demands.

---

### 3.2 Safe State & Safe Sequence Concepts
- **Safe State:** There exists a sequence $\langle P_{i_1},P_{i_2},\ldots,P_{i_n}\rangle$ in which every process can obtain its remaining maximum need from currently available resources plus resources released by preceding processes.
- **Safe Sequence:** This ordering is a constructive proof that all processes *could* finish, even if each requests its full remaining need.
- **Unsafe does not imply already deadlocked:** It means that such a completion guarantee is absent.

### 3.3 Data Structures for Banker's Algorithm
Let $n$ be the number of processes and $m$ be the number of resource types *(Silberschatz et al., Sec. 7.5.3; OS Chap 4 Deadlock.pdf, PDF pp. 14-16)*:

1. **`Available` (Vector of length $m$):**
   - `Available[j] = k` indicates that $k$ instances of resource type $R_j$ are currently free.
2. **`Max` ($n 	imes m$ Matrix):**
   - `Max[i][j] = k` defines the maximum claim of process $P_i$ for resource type $R_j$.
3. **`Allocation` ($n 	imes m$ Matrix):**
   - `Allocation[i][j] = k` defines the number of instances of resource type $R_j$ currently allocated to process $P_i$.
4. **`Need` ($n 	imes m$ Matrix):**
   - `Need[i][j] = k` indicates the remaining resource claim of process $P_i$ for resource type $R_j$.
   - **Fundamental Relationship:**
$$	ext{Need}[i][j] = 	ext{Max}[i][j] - 	ext{Allocation}[i][j]$$

---

### 3.4 The Safety Algorithm (Complete Pseudocode)
This algorithm determines whether a system state is safe and constructs a safe sequence:

```c
// Step 1: Initialize working vectors
int Work[m];
bool Finish[n];

for (int j = 0; j < m; j++) {
    Work[j] = Available[j];
}
for (int i = 0; i < n; i++) {
    Finish[i] = false;
}

// Step 2: Find an unfinished process whose remaining needs can be satisfied
int count = 0;
while (count < n) {
    bool found = false;
    for (int i = 0; i < n; i++) {
        if (Finish[i] == false) {
            bool can_allocate = true;
            for (int j = 0; j < m; j++) {
                if (Need[i][j] > Work[j]) {
                    can_allocate = false;
                    break;
                }
            }
            
            // Step 3: Simulate process completion and resource reclamation
            if (can_allocate) {
                for (int j = 0; j < m; j++) {
                    Work[j] += Allocation[i][j];
                }
                Finish[i] = true;
                found = true;
                count++;
            }
        }
    }
    
    // If no process could be found in a full pass, the system is unsafe
    if (!found) {
        break;
    }
}

// Step 4: System is safe if all processes finished
if (count == n) {
    // SYSTEM IS IN A SAFE STATE (record the selected process order as a safe sequence)
} else {
    // SYSTEM IS IN AN UNSAFE STATE
}
```

---

### 3.5 The Resource-Request Algorithm (Complete Pseudocode)
Let $	ext{Request}_i$ be the request vector for process $P_i$ where $	ext{Request}_i[j] = k$ means $P_i$ wants $k$ instances of $R_j$:

```c
// Step 1: Check if request exceeds declared maximum claim
for (int j = 0; j < m; j++) {
    if (Request[i][j] > Need[i][j]) {
        // ERROR: Process exceeded its declared maximum claim!
        return ERROR_MAX_EXCEEDED;
    }
}

// Step 2: Check if resources are currently available
for (int j = 0; j < m; j++) {
    if (Request[i][j] > Available[j]) {
        // Process Pi must WAIT since resources are not currently available
        return PROCESS_MUST_WAIT;
    }
}

// Step 3: Tentatively allocate resources to Pi (Pretend allocation)
for (int j = 0; j < m; j++) {
    Available[j] -= Request[i][j];
    Allocation[i][j] += Request[i][j];
    Need[i][j] -= Request[i][j];
}

// Step 4: Run Safety Algorithm on tentative state
if (is_system_safe()) {
    // Grant resources permanently to Pi
    return REQUEST_GRANTED;
} else {
    // UNSAFE! Roll back tentative state and force Pi to wait
    for (int j = 0; j < m; j++) {
        Available[j] += Request[i][j];
        Allocation[i][j] -= Request[i][j];
        Need[i][j] += Request[i][j];
    }
    return REQUEST_DENIED_UNSAFE;
}
```

---

### 3.6 Fully Worked Step-by-Step Numerical Example

#### 3.6.1 Initial System Snapshot & Need Matrix Calculation
The scanned chapter supplies five processes, called $P_1$ through $P_5$ (PDF pp. 21-25). For consistency with the standard zero-based textbook notation, the **same rows** are named $P_0$ through $P_4$ here; thus source $P_1$ is $P_0$ here, and source $P_2$ is $P_1$ here. The three resource totals are $(10,5,7)$.

Allocation, Max and their elementwise difference are:

```math
\mathrm{Allocation} = \begin{bmatrix}
0 & 1 & 0 \\
2 & 0 & 0 \\
3 & 0 & 2 \\
2 & 1 & 1 \\
0 & 0 & 2
\end{bmatrix}
```

```math
\mathrm{Max} = \begin{bmatrix}
7 & 5 & 3 \\
3 & 2 & 2 \\
9 & 0 & 2 \\
2 & 2 & 2 \\
4 & 3 & 3
\end{bmatrix}
```

- **Total Allocated Resources:** $(0+2+3+2+0,\;1+0+0+1+0,\;0+0+2+1+2)=(7,2,5)$.
- **Calculated Available Vector:** $(10,5,7)-(7,2,5)=(3,3,2)$.
- **Calculated Need Matrix:** $\mathrm{Need}=\mathrm{Max}-\mathrm{Allocation}$, row by row: $(7-0,5-1,3-0)$; $(3-2,2-0,2-0)$; $(9-3,0-0,2-2)$; $(2-2,2-1,2-1)$; $(4-0,3-0,3-2)$.

```math
\mathrm{Need} = \begin{bmatrix}
7 & 4 & 3 \\
1 & 2 & 2 \\
6 & 0 & 0 \\
0 & 1 & 1 \\
4 & 3 & 1
\end{bmatrix}
```

#### 3.6.2 Safety Check at T0 & Safe Sequence Derivation
Initialize $\mathrm{Work}=\mathrm{Available}=(3,3,2)$ and $\mathrm{Finish}=[\mathrm{false},\mathrm{false},\mathrm{false},\mathrm{false},\mathrm{false}]$. Compare vectors componentwise; a completed process returns its *currently allocated* resources.

| Step | Process | Need | Work before | Work after completion | Finish update |
|:--|:--|:--|:--|:--|:--|
| Initial check | $P_0$ | $(7,4,3)$ | $(3,3,2)$ | Not eligible | Unchanged |
| 1 | $P_1$ | $(1,2,2)$ | $(3,3,2)$ | $(3,3,2)+(2,0,0)=(5,3,2)$ | $\mathrm{Finish}[1]=\mathrm{true}$ |
| 2 | $P_3$ | $(0,1,1)$ | $(5,3,2)$ | $(5,3,2)+(2,1,1)=(7,4,3)$ | $\mathrm{Finish}[3]=\mathrm{true}$ |
| 3 | $P_4$ | $(4,3,1)$ | $(7,4,3)$ | $(7,4,3)+(0,0,2)=(7,4,5)$ | $\mathrm{Finish}[4]=\mathrm{true}$ |
| 4 | $P_0$ | $(7,4,3)$ | $(7,4,5)$ | $(7,4,5)+(0,1,0)=(7,5,5)$ | $\mathrm{Finish}[0]=\mathrm{true}$ |
| 5 | $P_2$ | $(6,0,0)$ | $(7,5,5)$ | $(7,5,5)+(3,0,2)=(10,5,7)$ | $\mathrm{Finish}[2]=\mathrm{true}$ |

**Conclusion:** The original state is safe. One safe sequence is $\langle P_1,P_3,P_4,P_0,P_2\rangle$ (source notation: $\langle P_2,P_4,P_5,P_1,P_3\rangle$).

#### 3.6.3 Processing Tentative Resource Requests
**Independent-test rule:** Every case below starts afresh from the **same original state**: Available $(3,3,2)$ and the Allocation/Need matrices printed above. A grant in one case is **not** carried into another case. Each request must pass $\mathrm{Request}_i\le\mathrm{Need}_i$ and $\mathrm{Request}_i\le\mathrm{Available}$ before a *temporary* allocation and safety test.

##### Request 1A: Source-question $P_1$ (our $P_0$) requests $(1,0,0)$
- Check: $(1,0,0)\le(7,4,3)$ and $(1,0,0)\le(3,3,2)$.
- Tentative Available $=(2,3,2)$; Allocation$_0=(1,1,0)$; Need$_0=(6,4,3)$.
- Safety trace: $P_1:(2,3,2)\to(4,3,2)$; $P_3:\to(6,4,3)$; $P_4:\to(6,4,5)$; $P_0:\to(7,5,5)$; $P_2:\to(10,5,7)$.
- **Decision: Grant.** Safe sequence $\langle P_1,P_3,P_4,P_0,P_2\rangle$.

##### Request 1B: Source-answer vector $(1,0,2)$ for source $P_1$ (our $P_0$)
- Check: $(1,0,2)\le(7,4,3)$ and $(1,0,2)\le(3,3,2)$.
- Tentative Available $=(2,3,0)$; Allocation$_0=(1,1,2)$; Need$_0=(6,4,1)$.
- Safety trace: $P_1:(2,3,0)\to(4,3,0)$; $P_3$ needs $(0,1,1)$ and **cannot** finish yet; $P_4$ needs $(4,3,1)$ and **cannot** finish yet; $P_2$ needs $(6,0,0)$ and **cannot** finish yet; $P_0$ needs $(6,4,1)$ and **cannot** finish yet.
- **Decision: Deny/defer as unsafe.** No process is eligible after $P_1$ finishes. This differs from a separate standard textbook example in which $(1,0,2)$ is requested by **$P_1$ in zero-based notation** (source $P_2$), which *is* safe. Never transfer the request to another row without saying so.

##### Request 1C: Standard textbook variant, our $P_1$ (source $P_2$) requests $(1,0,2)$
- Check: $(1,0,2)\le(1,2,2)$ and $(1,0,2)\le(3,3,2)$.
- Tentative Available $=(2,3,0)$; Allocation$_1=(3,0,2)$; Need$_1=(0,2,0)$.
- Safety trace: $P_1:(2,3,0)\to(5,3,2)$; $P_3:\to(7,4,3)$; $P_4:\to(7,4,5)$; $P_0:\to(7,5,5)$; $P_2:\to(10,5,7)$.
- **Decision: Grant.** Safe sequence $\langle P_1,P_3,P_4,P_0,P_2\rangle$.

##### Request 2: Our $P_0$ requests $(0,2,0)$
- Check: $(0,2,0)\le(7,4,3)$ and $(0,2,0)\le(3,3,2)$.
- Tentative Available $=(3,1,2)$; Allocation$_0=(0,3,0)$; Need$_0=(7,2,3)$.
- Safety trace: $P_3:(3,1,2)\to(5,2,3)$; $P_1:\to(7,2,3)$; $P_0:\to(7,5,3)$; $P_2:\to(10,5,5)$; $P_4:\to(10,5,7)$.
- **Decision: Grant.** Safe sequence $\langle P_3,P_1,P_0,P_2,P_4\rangle$. Another valid safe sequence is $\langle P_3,P_1,P_2,P_0,P_4\rangle$.

##### Request 3: Our $P_4$ requests $(3,3,0)$
- From the **original state**, the request passes Need $(4,3,1)$ and Available $(3,3,2)$ checks.
- Tentative Available $=(0,0,2)$; Allocation$_4=(3,3,2)$; Need$_4=(1,0,1)$.
- No unfinished process has Need $\le(0,0,2)$, so the tentative state is unsafe.
- **Decision: Deny/defer as unsafe**, not for insufficient initial availability. (After granting Request 1C, a *new* $(3,3,0)$ request would instead fail the availability test because Available would be $(2,3,0)$.)

#### 3.6.4 Discrepancy Flag & Source Resolution
> **Source discrepancy (OS Chap 4 Deadlock.pdf, PDF pp. 21 and 25):** The question on p. 21 prints $(1,0,0)$ for source $P_1$; the answer on p. 25 switches to $(1,0,2)$ without a matching safety check. The scanned answer also uses a first-step availability check alone to claim an immediate grant; availability is necessary but **not sufficient** under Banker's algorithm. Request 1A tests the question's vector. Request 1B tests the answer's vector for the same source process. Request 1C is an explicitly separate textbook-style request by another process. All cases above use the original state independently. The PDF is scanned, so verify ambiguous characters against the original page image before quoting them as exact source text.

### 3.7 Limitations of Banker's Algorithm
1. **Requires Fixed Resource Pool:** Cannot handle dynamic addition/removal of physical hardware resources.
2. **Requires Static Process Population:** The algorithm must track the processes currently admitted and their maximum claims; process arrivals and completions require updating the state, rather than a permanently fixed process population.
3. **Requires Advance Declaration of Max Need:** Impossible for interactive, open-ended applications to predict their maximum future resource claims.
4. **Incurs High Performance Overhead:** Running an $O(m \cdot n^2)$ safety algorithm on every single resource request causes severe CPU degradation.
5. **Enforces Unrealistic Process Independence:** Assumes processes run to completion without releasing resources incrementally.

---

### 3.8 Exam Summary & Common Mistakes
- **Concise Summary:** Banker's algorithm avoids deadlocks by granting resource requests only if the resulting state maintains a safe sequence $\langle P_0, \dots, P_{n-1} 
angle$.
- **Common Student Mistakes:**
  - *Mistake:* Forgetting to calculate the Need matrix ($	ext{Need} = 	ext{Max} - 	ext{Allocation}$) before running the safety check.
  - *Mistake:* Adding $	ext{Max}$ instead of $	ext{Allocation}$ to $	ext{Work}$ when a process finishes in the safety algorithm. *(Correction: When $P_i$ finishes, it releases what it currently holds, so $	ext{Work} = 	ext{Work} + 	ext{Allocation}_i$).*

---

## 4. Deadlock Detection and Recovery

### 4.1 Deadlock Detection Strategy
If a system does not employ deadlock prevention or avoidance, deadlocks may occur. **Deadlock Detection** allows the system to enter an unsafe or deadlocked state, periodically runs an algorithm to detect deadlocked processes, and invokes a recovery scheme *(Silberschatz et al., Sec. 7.6)*.

---

### 4.2 Detection for Single-Instance Resources (Wait-For Graph)
For systems where every resource type has exactly **one instance**, deadlock detection uses a simplified data structure called a **Wait-For Graph (WFG)** *(Silberschatz et al., Sec. 7.6.1)*.

#### Wait-For Graph Construction
- Derived directly from a Resource-Allocation Graph by removing resource nodes and collapsing edges.
- An edge $P_i 	o P_j$ exists in a Wait-For Graph if and only if process $P_i$ is waiting for a resource currently held by process $P_j$.

```text
Resource Allocation Graph:             Corresponding Wait-For Graph:
(P1) ---> [R1] ---> (P2)                     (P1) ---------> (P2)
  ^                  |                         ^               |
  |                  v                         |               v
[R2] <-------------- (P2)                    (P3) <---------- (P2)  (Wait-For Cycle)
```

- **Algorithm:** The OS maintains the Wait-For Graph and periodically runs a cycle-detection algorithm (such as Depth-First Search).
- **Time Complexity:** $O(|V|+|E|)$ with adjacency lists and DFS (or $O(n^2)$ with an adjacency matrix), where $n$ is the number of processes.
- **Rule:** **A cycle in a Wait-For Graph indicates a DEADLOCK.**

---

### 4.3 Detection for Multiple-Instance Resources
For systems with multiple instances per resource type, a detection algorithm similar to Banker's safety algorithm is used *(Silberschatz et al., Sec. 7.6.2)*:

#### Data Structures
- $	ext{Available}$ (length $m$), $	ext{Allocation}$ ($n 	imes m$), $	ext{Request}$ ($n 	imes m$).

#### Detection Algorithm Pseudocode
```c
int Work[m];
bool Finish[n];

// Step 1: Initialize Work and Finish
for (int j = 0; j < m; j++) {
    Work[j] = Available[j];
}

for (int i = 0; i < n; i++) {
    if (Allocation[i] != 0) {
        Finish[i] = false;
    } else {
        Finish[i] = true; // Processes holding 0 resources are not deadlocked
    }
}

// Step 2: Find an unfinished process whose current requests can be satisfied
while (true) {
    bool found = false;
    for (int i = 0; i < n; i++) {
        if (Finish[i] == false) {
            bool can_satisfy = true;
            for (int j = 0; j < m; j++) {
                if (Request[i][j] > Work[j]) {
                    can_satisfy = false;
                    break;
                }
            }
            
            // Step 3: Reclaim allocated resources
            if (can_satisfy) {
                for (int j = 0; j < m; j++) {
                    Work[j] += Allocation[i][j];
                }
                Finish[i] = true;
                found = true;
            }
        }
    }
    if (!found) break;
}

// Step 4: Identify deadlocked processes
for (int i = 0; i < n; i++) {
    if (Finish[i] == false) {
        // Process Pi is DEADLOCKED!
    }
}
```

---

### 4.4 Detection Frequency & System Overhead
The OS must balance detection thoroughness against CPU overhead:
1. **On Every Unserviceable Request:** Invoking detection whenever a request blocks provides immediate detection but consumes excessive CPU time.
2. **Periodic Interval:** Running detection at fixed intervals (e.g., every $X$ minutes) or when CPU utilization drops below a threshold (e.g., $< 30\%$).

---

### 4.5 Recovery Strategies

#### 4.5.1 Process Termination Approaches
When a deadlock is detected, the OS can break it by terminating processes *(Silberschatz et al., Sec. 7.7.1)*:
1. **Abort All Deadlocked Processes:**
   - Immediately breaks the deadlock, but destroys partial computation results for all aborted jobs (very costly).
2. **Abort One Process at a Time:**
   - Abort one process, re-run the detection algorithm, and repeat until the deadlock cycle is broken. Incurs high overhead due to repeated detection passes.

##### Victim Selection Criteria for Termination
When deciding which process to terminate, the OS evaluates:
- Process priority.
- Computation time already expended and time remaining to completion.
- Types and quantities of resources held.
- Resources needed to complete execution.
- Process type (Interactive vs. Batch).

#### 4.5.2 Resource Preemption & Issues
Instead of aborting processes, the OS can preempt resources *(Silberschatz et al., Sec. 7.7.2)*:
1. **Selecting a Victim:** Determine which resources and processes to preempt to minimize overall cost.
2. **Rollback:** Return the victim process to a safe checkpointed state and restart it from that point. Requires checkpoint/logging mechanisms.
3. **Starvation Prevention:** If victim selection is based strictly on cost, the same process may be repeatedly chosen as a victim and starve.
   - **Solution:** Include the number of prior preemptions in the process's cost function.

---

### 4.6 Exam Summary & Common Mistakes
- **Concise Summary:** Detection uses Wait-For Graphs ($O(n^2)$) for single-instance resources or Work-Finish matrices for multi-instance resources. Recovery involves process termination or resource preemption with starvation controls.
- **Common Student Mistakes:**
  - *Mistake:* Assuming that finding a cycle in a multi-instance detection algorithm immediately means all processes in the graph are deadlocked. *(Correction: Only processes with `Finish[i] == false` at the end of the algorithm are deadlocked).*

---

## 5. The Dining Philosophers Problem

### 5.1 Problem Statement & Resource Constraints
The **Dining Philosophers Problem** (Edsger Dijkstra, 1965) is a classic synchronization benchmark representing the challenge of allocating multiple limited resources among concurrent processes without causing deadlock or starvation *(Silberschatz et al., Sec. 6.7; Stallings, Sec. 6.6)*.

```text
                        [Philosopher 0]
                      /                             (Fork 0)                       (Fork 4)
            /                                   [Philosopher 1]                           [Philosopher 4]
        |                                         |
     (Fork 1)                                  (Fork 3)
         \                                       /
          [Philosopher 2] ------- (Fork 2) ------- [Philosopher 3]
```

#### Problem Rules
- Five philosophers sit around a circular table with 5 chopsticks/forks (`chopstick[0..4]`) and a central bowl of rice.
- A philosopher alternates between **Thinking** and **Eating**.
- To eat, a philosopher requires **both adjacent forks** (left fork `chopstick[i]` and right fork `chopstick[(i+1)%5]`).
- A philosopher can pick up only one fork at a time and cannot take a fork held by a neighbor.

---

### 5.2 Naive Semaphore Implementation & Deadlock Analysis

```c
// Naive Semaphore Solution
semaphore chopstick[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    while (true) {
        think();
        
        wait(chopstick[i]);                 // Pick up left chopstick
        wait(chopstick[(i + 1) % 5]);       // Pick up right chopstick
        
        eat();
        
        signal(chopstick[i]);               // Release left chopstick
        signal(chopstick[(i + 1) % 5]);     // Release right chopstick
    }
}
```

#### Why the Naive Solution Fails (Deadlock Scenario)
Suppose all 5 philosophers become hungry simultaneously and every philosopher executes `wait(chopstick[i])`.
- Every philosopher successfully acquires their left chopstick.
- All `chopstick` semaphores decrement to `0`.
- Next, every philosopher executes `wait(chopstick[(i+1)%5])` to acquire their right chopstick.
- Since every right chopstick is held by a neighboring philosopher, **all 5 philosophers block permanently**.
- This is a classic **Circular Wait Deadlock**.

---

### 5.3 Deadlock-Free Solutions Using Semaphores
To eliminate deadlock, one of the following structural modifications can be applied *(Silberschatz et al., Sec. 6.7)*:

#### Option 1: Limit Seated Philosophers (Table Attendant)
Allow at most 4 philosophers to sit at the table simultaneously using a counting semaphore `room` initialized to `4`. Each fork has a binary semaphore initialized to `1`:

```c
semaphore room = 4;
semaphore chopstick[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    while (true) {
        think();
        wait(room);                       // Admit at most four contenders
        wait(chopstick[i]);               // Acquire left fork
        wait(chopstick[(i + 1) % 5]);     // Acquire right fork
        eat();
        signal(chopstick[(i + 1) % 5]);   // Release right fork
        signal(chopstick[i]);             // Release left fork
        signal(room);                     // Free table place
    }
}
```

With at most four contenders, at least one fork remains unheld when each contender has taken a first fork; hence the all-five circular-wait configuration cannot arise. This guarantees deadlock freedom, **not** starvation freedom unless admission/fork scheduling is fair.

#### Option 2: Asymmetric Chopstick Pickup
An odd philosopher picks up their left chopstick first, then right. An even philosopher picks up their right chopstick first, then left.

```c
// Asymmetric Deadlock-Free Semaphore Solution
semaphore chopstick[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    while (true) {
        think();
        
        if (i % 2 == 0) { // Even philosopher: Right then Left
            wait(chopstick[(i + 1) % 5]);
            wait(chopstick[i]);
        } else {         // Odd philosopher: Left then Right
            wait(chopstick[i]);
            wait(chopstick[(i + 1) % 5]);
        }
        
        eat();
        
        signal(chopstick[i]);
        signal(chopstick[(i + 1) % 5]);
    }
}
```

---

### 5.4 Deadlock-Free Solution Using Monitors
**Assume Mesa-style condition variables (signal-and-continue).** A philosopher is allowed to pick up chopsticks **only if both adjacent chopsticks are simultaneously available** *(Silberschatz et al., dining-philosophers monitor section; supplemental explanation, not attributed to an unattached PDF)*:

```c
monitor DiningPhilosophers {
    enum { THINKING, HUNGRY, EATING } state[5];
    condition self[5];

    void pickup(int i) {
        state[i] = HUNGRY;
        test(i); // Attempt to acquire both chopsticks
        
        while (state[i] != EATING) {
            self[i].wait(); // Mesa-style: recheck after waking
        }
    }

    void putdown(int i) {
        state[i] = THINKING;
        
        // Test if left and right neighbors can now eat
        test((i + 4) % 5);
        test((i + 1) % 5);
    }

    void test(int i) {
        if ((state[(i + 4) % 5] != EATING) && 
            (state[i] == HUNGRY) && 
            (state[(i + 1) % 5] != EATING)) {
            
            state[i] = EATING;
            self[i].signal(); // Wake up philosopher i if waiting
        }
    }

    initialization_code() {
        for (int i = 0; i < 5; i++) {
            state[i] = THINKING;
        }
    }
}

// Philosopher Process Execution:
void philosopher(int i) {
    while (true) {
        think();
        DiningPhilosophers.pickup(i);
        eat();
        DiningPhilosophers.putdown(i);
    }
}
```

---

### 5.5 Deadlock Freedom vs. Starvation Freedom Analysis
> **CRITICAL EXAM WARNING:** **Deadlock-Free DOES NOT Mean Starvation-Free!**
> While the monitor and asymmetric semaphore solutions strictly eliminate deadlocks, **they do not guarantee freedom from starvation**.
>
> **Starvation Scenario:** A philosopher $P_1$ can starve to death if their left neighbor $P_0$ and right neighbor $P_2$ alternate eating in such a way that at least one neighbor is always in the `EATING` state whenever $P_1$ attempts to execute `pickup(1)`. $P_1$ remains perpetually blocked in the `HUNGRY` state.

---

### 5.6 Exam Summary & Common Mistakes
- **Concise Summary:** Naive chopstick acquisition causes circular wait deadlocks. Asymmetric pickup or monitor-based state testing guarantees deadlock freedom, but additional queueing logic is required to prevent starvation.
- **Common Student Mistakes:**
  - *Mistake:* Stating that the monitor solution to Dining Philosophers eliminates both deadlocks and starvation. *(Correction: It eliminates deadlocks, but starvation remains possible if neighbors alternate eating).*

---

## 6. Comprehensive Unit 4 Comparison Table

| Metric / Feature | Deadlock Prevention | Deadlock Avoidance (Banker's) | Deadlock Detection & Recovery |
| :--- | :--- | :--- | :--- |
| **Basic Strategy** | Eliminates one of Coffman's 4 conditions statically at design time. | Dynamically checks resource requests to maintain a safe state. | Allows deadlocks to occur, detects them periodically, and recovers. |
| **Advance Info Needed** | None required. | Maximum resource claims declared upfront by every process. | None required (uses current allocations and requests). |
| **Resource Utilization** | **Low** (due to conservative allocation restrictions). | **Medium to High** (allows flexible requests within safe bounds). | **High** (resources allocated freely until deadlock occurs). |
| **System Overhead** | Minimal runtime overhead; restrictions enforced by design. | High runtime overhead ($O(m \cdot n^2)$ safety check on every request). | Low overhead until detection/recovery is triggered. |
| **Process Autonomy** | Restricted (forced request order or total allocation). | Moderate (processes must state max claims). | High (unrestricted process requests). |

---

## 7. Formula & Algorithm Pseudocode Quick Recap

### 1. Need Matrix Equation
$$	ext{Need}[i][j] = 	ext{Max}[i][j] - 	ext{Allocation}[i][j]$$

### 2. Available Vector Calculation
$$	ext{Available}[j] = 	ext{Total}[j] - \sum_{i=0}^{n-1} 	ext{Allocation}[i][j]$$

### 3. Safety Algorithm Invariant
$$	ext{Need}_i \le 	ext{Work} \implies 	ext{Work}_{	ext{new}} = 	ext{Work}_{	ext{old}} + 	ext{Allocation}_i$$

### 4. Resource-Request Conditions
$$	ext{Request}_i \le 	ext{Need}_i \quad 	ext{AND} \quad 	ext{Request}_i \le 	ext{Available}$$

---

## 8. Representative Exam Question Patterns & Model Answers

### Pattern 1: Four Necessary Conditions & Prevention Strategies (10 Marks)
- **Question:** Explain Coffman's four necessary conditions for deadlock. Discuss how invalidating Circular Wait prevents deadlocks, providing a mathematical proof.
- **Model Answer:** Detail Mutual Exclusion, Hold & Wait, No Preemption, and Circular Wait. Present the linear indexing function $F: R 	o \mathbb{N}$ and reproduce the proof ($F(R_0) < F(R_0)$ contradiction).

### Pattern 2: Banker's Algorithm Numerical Problem (10 Marks)
- **Question:** Given 5 processes ($P_0..P_4$) and 3 resources ($A=10, B=5, C=7$), with Allocation and Max matrices provided: (i) Compute Need matrix, (ii) Prove system is in a safe state and give safe sequence, (iii) Test the source question's $(1,0,0)$ request by source $P_1$ (our $P_0$); separately evaluate the inconsistent $(1,0,2)$ answer vector for that same process.
- **Model Answer:** Calculate $	ext{Need} = 	ext{Max} - 	ext{Allocation}$. Trace Safety Algorithm steps to derive $\langle P_1, P_3, P_4, P_0, P_2 
angle$. Apply the Resource-Request algorithm to each independently reset state; $(1,0,0)$ for source $P_1$ is safe, but $(1,0,2)$ for source $P_1$ is unsafe. A $(1,0,2)$ request by source $P_2$ (our $P_1$) is a separate safe variant.

### Pattern 3: Dining Philosophers Monitor Solution (10 Marks)
- **Question:** Explain the Dining Philosophers problem. Show why the naive semaphore solution leads to deadlock and provide a monitor-based deadlock-free solution.
- **Model Answer:** State problem rules, trace naive circular wait deadlock, provide complete `DiningPhilosophers` monitor C pseudocode (`pickup`, `putdown`, `test`), and explain starvation risk.

---

## 9. Quick Revision Checklist

- [ ] Can you list and define Coffman's 4 necessary conditions for deadlock?
- [ ] Do you understand why a cycle in a RAG guarantees deadlock ONLY for single-instance resources?
- [ ] Can you state the difference between a Safe State, an Unsafe State, and a Deadlocked State?
- [ ] Do you know how to calculate $	ext{Need} = 	ext{Max} - 	ext{Allocation}$?
- [ ] Can you trace Banker's Safety Algorithm step-by-step to find a Safe Sequence?
- [ ] Do you know how to process a tentative resource request using the Resource-Request Algorithm?
- [ ] Can you distinguish the attached PDF's question vector $(1,0,0)$ from its answer vector $(1,0,2)$, keeping the process row explicit?
- [ ] Can you explain Wait-For Graph (WFG) cycle detection for single-instance deadlock detection?
- [ ] Can you explain victim selection criteria and starvation issues in deadlock recovery?
- [ ] Can you write the complete Monitor pseudocode for the Dining Philosophers problem?
- [ ] Do you remember that deadlock-free solutions to Dining Philosophers do NOT automatically prevent starvation?
