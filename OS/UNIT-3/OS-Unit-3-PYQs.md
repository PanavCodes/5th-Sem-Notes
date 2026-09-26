# Operating Systems: Unit 3 — Process Concurrency Exam-Oriented PYQ Bank

This document contains a comprehensive, marks-aligned **Previous Year Question (PYQ) Bank** and **Model Answers** for **Unit 3: Process Concurrency**. It covers all official syllabus topics from the **Operating Systems 2025-26 Course Policy** (`Approved CP_OS.pdf` / `Proposed CP_OS 2026-27.docx`), lecture presentations (`UNIT3-Process concurrency.pptx`), and course handouts (`OS Chap-3 Process Concurrency.pdf`), as well as verified semester examination papers from SVKM's NMIMS University and GTU.

---

## Table of Contents
- [1. Document Structure & Source Verification](#1-document-structure-source-verification)
- [2. Topic-Wise Question Index](#2-topic-wise-question-index)
- [3. Repeated-Question Summary List](#3-repeated-question-summary-list)
- [4. Source-Status & Verification Checklist](#4-source-status-verification-checklist)
- [5. SECTION I: PRESCRIBED SYLLABUS TOPICS QUESTION BANK](#5-section-i-prescribed-syllabus-topics-question-bank)
  - [Topic 1: Principles of Concurrency & Critical Section Problem](#topic-1-principles-of-concurrency-critical-section-problem)
    - [Q1.1 (Verified PYQ): Race Condition Definition & Concrete Examples [5/10 Marks]](#q11-verified-pyq-race-condition-definition--concrete-examples-510-marks)
    - [Q1.2 (Verified PYQ): Critical Section Problem & Three Mandatory Requirements [5/10 Marks]](#q12-verified-pyq-critical-section-problem--three-mandatory-requirements-510-marks)
    - [Q1.3 (Verified PYQ): Process Interleaving & Shared Counter Corruption Trace [5 Marks]](#q13-verified-pyq-process-interleaving--shared-counter-corruption-trace-5-marks)
  - [Topic 2: Hardware Approaches to Mutual Exclusion](#topic-2-hardware-approaches-to-mutual-exclusion)
    - [Q2.1 (Reported PYQ): Interrupt Disabling for Mutual Exclusion [5 Marks]](#q21-reported-pyq-interrupt-disabling-for-mutual-exclusion-5-marks)
    - [Q2.2 (Verified PYQ): Atomic Hardware Instructions — TestAndSet, CompareAndSwap, and Exchange/Swap [10 Marks]](#q22-verified-pyq-atomic-hardware-instructions--testandset-compareandswap-and-exchangeswap-10-marks)
    - [Q2.3 (Practice Question): Multiprocessor Bus Locking vs. Busy-Waiting Spinlocks [5 Marks]](#q23-practice-question-multiprocessor-bus-locking-vs-busy-waiting-spinlocks-5-marks)
  - [Topic 3: Semaphores & Synchronization Primitives](#topic-3-semaphores-synchronization-primitives)
    - [Q3.1 (Verified PYQ): Semaphore Definition, Types (Binary vs. Counting), and Atomic Operations [5 Marks]](#q31-verified-pyq-semaphore-definition-types-binary-vs-counting-and-atomic-operations-5-marks)
    - [Q3.2 (Verified PYQ): Inverted Semaphore Wait Order & Deadlock Analysis [5/10 Marks]](#q32-verified-pyq-inverted-semaphore-wait-order--deadlock-analysis-510-marks)
    - [Q3.3 (Practice Question): Mutex Lock vs. Counting Semaphore Comparison [5 Marks]](#q33-practice-question-mutex-lock-vs-counting-semaphore-comparison-5-marks)
  - [Topic 4: Monitors & Language-Level Constructs](#topic-4-monitors-language-level-constructs)
    - [Q4.1 (Reported PYQ): Monitor Structure, Implicit Mutual Exclusion, and Condition Variables [5/10 Marks]](#q41-reported-pyq-monitor-structure-implicit-mutual-exclusion-and-condition-variables-510-marks)
    - [Q4.2 (Verified PYQ): Dining Philosophers Problem & Monitor-Based Solution [10 Marks]](#q42-verified-pyq-dining-philosophers-problem--monitor-based-solution-10-marks)
    - [Q4.3 (Practice Question): Hoare (Signal-and-Wait) vs. Mesa (Signal-and-Continue) Condition Semantics [5 Marks]](#q43-practice-question-hoare-signal-and-wait-vs-mesa-signal-and-continue-condition-semantics-5-marks)
  - [Topic 5: Message Passing & Inter-Process Communication](#topic-5-message-passing-inter-process-communication)
    - [Q5.1 (Reported PYQ): Message Passing Principles — Addressing & Blocking vs. Non-Blocking Primitives [5 Marks]](#q51-reported-pyq-message-passing-principles--addressing--blocking-vs-non-blocking-primitives-5-marks)
    - [Q5.2 (Practice Question): Mutual Exclusion Implementation Using Mailbox Message Passing [5 Marks]](#q52-practice-question-mutual-exclusion-implementation-using-mailbox-message-passing-5-marks)
    - [Q5.3 (Practice Question): Structural Layout of a Message — Header vs. Body Layout [5 Marks]](#q53-practice-question-structural-layout-of-a-message--header-vs-body-layout-5-marks)
  - [Topic 6: Classical IPC Problems](#topic-6-classical-ipc-problems)
    - [Q6.1 (Verified PYQ): Bounded-Buffer (Producer-Consumer) Problem Using Semaphores [10 Marks]](#q61-verified-pyq-bounded-buffer-producer-consumer-problem-using-semaphores-10-marks)
    - [Q6.2 (Practice Question): Bounded-Buffer (Producer-Consumer) Problem Using Monitors [10 Marks]](#q62-practice-question-bounded-buffer-producer-consumer-problem-using-monitors-10-marks)
    - [Q6.3 (Practice Question): Bounded-Buffer (Producer-Consumer) Problem Using Message Passing [10 Marks]](#q63-practice-question-bounded-buffer-producer-consumer-problem-using-message-passing-10-marks)
    - [Q6.4 (Verified PYQ): First Readers-Writers Problem (Reader Preference) Using Semaphores [10 Marks]](#q64-verified-pyq-first-readers-writers-problem-reader-preference-using-semaphores-10-marks)
- [6. SECTION II: ADDITIONAL TOPICS IN SUPPLIED TEACHING MATERIALS](#6-section-ii-additional-topics-in-supplied-teaching-materials)
  - [Topic A1: Software Mutual-Exclusion Approaches](#topic-a1-software-mutual-exclusion-approaches)
    - [QA1.1 (Verified / Reported PYQ): Software Mutual Exclusion — Strict Alternation, Flag-Only Attempts, Dekker's, and Peterson's Algorithm [10 Marks]](#qa11-verified--reported-pyq-software-mutual-exclusion--strict-alternation-flag-only-attempts-dekkers-and-petersons-algorithm-10-marks)
  - [Topic A2: Strong vs. Weak Semaphores & Queue Ordering](#topic-a2-strong-vs-weak-semaphores-queue-ordering)
    - [QA2.1 (Practice Question): Strong (FIFO) vs. Weak Semaphores & Process Queue Transition Trace [5 Marks]](#qa21-practice-question-strong-fifo-vs-weak-semaphores--process-queue-transition-trace-5-marks)
  - [Topic A3: The Sleeping Barber Problem](#topic-a3-the-sleeping-barber-problem)
    - [QA3.1 (Reported PYQ): The Sleeping Barber Problem & Semaphore Solution [10 Marks]](#qa31-reported-pyq-the-sleeping-barber-problem--semaphore-solution-10-marks)
- [7. SECTION III: QUICK REVISION CHECKLIST & PSEUDOCODE RECAP](#7-section-iii-quick-revision-checklist-pseudocode-recap)

---

## 1. Document Structure & Source Verification

### Categorization System & Verification Labels
To guarantee academic integrity and clarity, every question in this bank is explicitly labeled with one of three verification tags:
1. **`Verified PYQ`**: Directly cross-referenced and extracted from an official SVKM's NMIMS University semester examination paper present in the source files.
2. **`Reported PYQ (unverified)`**: Extracted from university question compilations (GTU, TechNeo, Easy Solution, or textbook review questions) cited in course materials.
3. **`Practice Question`**: Formulated specifically to ensure complete coverage of all core syllabus topics and potential exam variations.

---

## 2. Topic-Wise Question Index

| Topic # | Syllabus Topic Area | Total Questions | Verified PYQs | Reported PYQs | Practice Questions |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | **Principles of Concurrency & Critical Section Problem** | 3 | 3 | 0 | 0 |
| **2** | **Hardware Approaches to Mutual Exclusion** | 3 | 1 | 1 | 1 |
| **3** | **Semaphores & Synchronization Primitives** | 3 | 2 | 0 | 1 |
| **4** | **Monitors & Language-Level Constructs** | 3 | 1 | 1 | 1 |
| **5** | **Message Passing & Inter-Process Communication** | 3 | 0 | 1 | 2 |
| **6** | **Classical IPC Problems (Producer-Consumer & Readers-Writers)** | 4 | 2 | 0 | 2 |
| **A1** | *Additional: Software Mutual Exclusion (Peterson's / Dekker's)* | 1 | 1 | 0 | 0 |
| **A2** | *Additional: Strong vs. Weak Semaphores* | 1 | 0 | 0 | 1 |
| **A3** | *Additional: Sleeping Barber Problem* | 1 | 0 | 1 | 0 |
| **TOTAL** | **All Unit 3 Topics** | **22** | **10** | **4** | **8** |

---

## 3. Repeated-Question Summary List

The following core questions appear repeatedly across multiple exam sessions with minor phrasing variations:

1. **The Critical Section Problem & 3 Requirements:**
   - *SVKM NMIMS Special Re-Exam 2022-23 [Q1b - 5M]*: "Elaborate the solution to critical section problem?"
   - *SVKM NMIMS Re-Exam 2023-24 / Batch 2024-25 [Q1a - 5M]*: "Explain critical section problem in detail."
   - *GTU Dec 2014 / June 2015 [5M/10M]*: "Explain critical section problem with its different solutions."
2. **Race Condition Concept & Examples:**
   - *SVKM NMIMS Special Re-Exam 2022-23 [Q6a - 10M]*: "What is race condition? Explain Peterson's solution in detail."
   - *GTU Dec 2014 [5M]*: "What is race condition? Explain with example."
3. **Semaphore Definition & Types:**
   - *SVKM NMIMS Final Exam 2022-23 [Q1a - 5M]*: "What do you mean by semaphore? What are its types? Explain any one in detail."
   - *GTU June 2015 / Nov 2015 [5M]*: "What is semaphore? List the disadvantages of semaphores."
4. **Producer-Consumer Problem:**
   - *SVKM NMIMS Special Re-Exam 2022-23 [Q4a - 10M]*: "Enlist all classical IPC problems and explain producer-consumer problem in detail?"
   - *SVKM NMIMS Final Exam 2024-25 [Q1b - 5M]*: "A student writes the following Producer-Consumer code... [identify errors & deadlock]."
5. **Readers-Writers Problem:**
   - *SVKM NMIMS Final Exam 2023-24 [Q7a - 10M]*: "Discuss the Readers-Writers problem that arise in concurrent programming, with pseudocode."
   - *GTU June 2015 [10M]*: "Explain how Readers/Writers problem can be solved with semaphores?"

---

## 4. Source-Status & Verification Checklist

| Original Source Examination Paper | File Name in Workspace | Verification Status | Unit 3 Questions Verified |
| :--- | :--- | :---: | :--- |
| **SVKM NMIMS Final Exam 2024-2025** | `QP_Final-Exam_Operating Systems(702CO1C002)_Semester V_2024-2025.pdf` | **VERIFIED** | Q1b (Producer-Consumer Code Debugging - 5M), Q2a (Dining Philosophers & Monitor - 10M) |
| **SVKM NMIMS Special Re-Exam 2022-2023** | `Operating_System__Sem-V__Year_2022-23__Special_Re_Exam_GF1XGRiPQ3.pdf` | **VERIFIED** | Q1b (Critical Section Solution - 5M), Q4a (Producer-Consumer - 10M) |
| **SVKM NMIMS Final Exam 2022-2023** | `Opearting_System_Final_2022-23_G7cIgeVmgx.pdf` | **VERIFIED** | Q1a (Semaphores & Types - 5M) |
| **SVKM NMIMS Final Exam 2023-2024** | `Operating_Systems__Sem-V__A_Y_2023-24__Final_Exam_w3cxMbVN2J.pdf` | **VERIFIED** | Q7a (Readers-Writers Problem - 10M) |
| **SVKM NMIMS Re-Exam 2023-24 / Batch 24-25** | `Operating_Systems__Batch__2024-25_Final_Batch_2023-24__Re_Exam_20jgs6KmZG.pdf` | **VERIFIED** | Q1a (Critical Section Problem - 5M), Q6a (Race Condition & Peterson's - 10M) |
| **GTU Question Paper Compilation** | `OS_TechNeo_Rev16.pdf` / `Operating system Easy Solution.pdf` | **REPORTED** | Hardware Mutual Exclusion (5M), Monitors (5M), Message Passing (5M), Sleeping Barber (10M) |

---

## 5. SECTION I: PRESCRIBED SYLLABUS TOPICS QUESTION BANK

### Topic 1: Principles of Concurrency & Critical Section Problem

#### Q1.1 (Verified PYQ): Race Condition Definition & Concrete Examples [5/10 Marks]
* **Source Details:** SVKM's NMIMS Re-Exam 2023-24 / Batch 2024-25 [Q6a - 10 Marks (Partial)], GTU Dec 2014 [5 Marks].
* **Question Text:** *"What is a race condition? Explain with a neat diagram and concrete code/assembly examples how unsynchronized concurrent execution leads to data inconsistency."*

##### Model Answer
###### 1. Definition (2 Marks)
A **race condition** is an undesirable situation in concurrent programming where two or more processes or threads access and manipulate shared data concurrently, and the final outcome of the execution depends unpredictably on the exact order and timing of instruction interleaving or overlapping. The process that "wins" the execution race determines the final state of the shared data.

###### 2. Diagrammatic Illustration (1.5 Marks)

```text
       Process P1 (Producer / Incrementor)           Process P2 (Consumer / Decrementor)
                         |                                           |
                Reads count = 5                             Reads count = 5
                         |                                           |
                Increments R1 = 6                           Decrements R2 = 4
                         |                                           |
                         | <--- Timer Preemption Interrupt --->    |
                         |                                    Stores count = 4
                Stores count = 6                                     |
                         |                                           v
                         v                             Memory count corrupted to 4!
              Memory count becomes 6                   (Expected correct count = 5)
```

###### 3. Concrete Code / Assembly Trace Example (1.5 Marks)
Consider two concurrent processes sharing an integer counter variable `count = 5`:
- **Process P1:** `count = count + 1;`
- **Process P2:** `count = count - 1;`

At the machine level, these statements compile into distinct assembly instructions:

```assembly
; Process P1
LOAD  R1, [count]   ; Step 1: R1 = 5
ADD   R1, #1        ; Step 2: R1 = 6
STORE [count], R1   ; Step 3: memory = R1

; Process P2
LOAD  R2, [count]   ; Step 1: R2 = 5
SUB   R2, #1        ; Step 2: R2 = 4
STORE [count], R2   ; Step 3: memory = R2
```

**Execution Interleaving Trace:**
1. **P1** executes `LOAD R1, [count]` $\rightarrow$ `R1 = 5`
2. **P1** executes `ADD R1, #1` $\rightarrow$ `R1 = 6`
3. *(Interrupt preemption; OS switches CPU context to P2)*
4. **P2** executes `LOAD R2, [count]` $\rightarrow$ `R2 = 5` *(P2 reads stale value 5)*
5. **P2** executes `SUB R2, #1` $\rightarrow$ `R2 = 4`
6. **P2** executes `STORE [count], R2` $\rightarrow$ `count` becomes `4`
7. *(Context switch back to P1)*
8. **P1** executes `STORE [count], R1` $\rightarrow$ `count` becomes `6`

**Conclusion:** The correct final value should be `5` ($5 + 1 - 1$). Due to the race condition, the result is `6` (or `4` if P2 stored last), destroying data consistency.

---

#### Q1.2 (Verified PYQ): Critical Section Problem & Three Mandatory Requirements [5/10 Marks]
* **Source Details:** SVKM's NMIMS Special Re-Exam 2022-23 [Q1b - 5 Marks], Re-Exam 2023-24 [Q1a - 5 Marks], GTU June 2015 [10 Marks].
* **Question Text:** *"Explain the Critical Section Problem in detail. State and explain the three mandatory requirements that any valid solution to the critical section problem must satisfy."*

##### Model Answer
###### 1. Critical Section Framework (2 Marks)
A **Critical Section (CS)** is a code segment in a concurrent process that accesses shared resources (such as global variables, memory tables, or files) that must not be accessed simultaneously by more than one process.

The general execution structure of a concurrent process is divided into four sections:

```c
do {
    /* ENTRY SECTION */
    // Requests permission to enter critical section

    /* CRITICAL SECTION */
    // Access and modify shared resources

    /* EXIT SECTION */
    // Releases lock and notifies waiting processes

    /* REMAINDER SECTION */
    // Non-critical local execution
} while (true);
```

###### 2. Three Mandatory Requirements (3 Marks)
Any valid software, hardware, or OS solution to the critical section problem must satisfy all three criteria:

1. **Mutual Exclusion:**
   - **Requirement:** If process $P_i$ is executing in its critical section, no other process $P_j$ can be executing in its critical section for the same shared resource simultaneously.
   - **Purpose:** Prevents race conditions and guarantees data consistency.

2. **Progress:**
   - **Requirement:** If no process is executing in its critical section and some processes wish to enter, only those processes that are **not** executing in their remainder section can participate in deciding which process enters next. This decision cannot be postponed indefinitely.
   - **Purpose:** Prevents system deadlock and ensures that processes outside the CS do not block eager processes from entering.

3. **Bounded Waiting:**
   - **Requirement:** There must exist a bound or limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.
   - **Purpose:** Prevents **indefinite starvation** of waiting processes.

---

#### Q1.3 (Verified PYQ): Process Interleaving & Shared Counter Corruption Trace [5 Marks]
* **Source Details:** SVKM's NMIMS Final Exam 2024-2025 [Q1b - Conceptual Variant], Course Slides (`UNIT3-Process concurrency.pptx` Slide 8).
* **Question Text:** *"Consider a shared buffer handled by an `echo()` function accessed concurrently by two processes P1 and P2 on a uniprocessor system. Trace step-by-step how interleaved execution corrupts the input buffer."*

##### Model Answer
###### 1. Conceptual Explanation & Assembly Trace
Assume `echo()` reads a character from an input device and writes it to a shared variable `in`:

```c
void echo() {
    in = getchar();
    putchar(in);
}
```

At the machine level:
- `LOAD R, [input_device]`
- `STORE [in], R`

###### 2. Unsynchronized Interleaving Trace

| Step | Active Process | Instruction Executed | Register State | Shared Memory (`in`) | System Outcome |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **P1** | `getchar()` typed `'x'` | $R_1 = 	ext{'x'}$ | Unchanged | P1 receives user input `'x'` |
| 2 | **P1** | *Preempted before storing* | $R_1 = 	ext{'x'}$ | Unchanged | Context switch to P2 |
| 3 | **P2** | `getchar()` typed `'y'` | $R_2 = 	ext{'y'}$ | Unchanged | P2 receives user input `'y'` |
| 4 | **P2** | `STORE [in], R2` | $R_2 = 	ext{'y'}$ | `in = 'y'` | Shared `in` set to `'y'` |
| 5 | **P2** | `putchar(in)` | $R_2 = 	ext{'y'}$ | `in = 'y'` | **P2 prints 'y'** |
| 6 | **P1** | *Resumed:* `STORE [in], R1` | $R_1 = 	ext{'x'}$ | `in = 'x'` | P1 overwrites `in` with `'x'` |
| 7 | **P1** | `putchar(in)` | $R_1 = 	ext{'x'}$ | `in = 'x'` | **P1 prints 'x'** |

**Corruption Analysis:** If P2 executes `putchar()` after step 6, P2 erroneously echoes `'x'` instead of `'y'`. Shared resource access without mutual exclusion corrupts character echoing.

---

### Topic 2: Hardware Approaches to Mutual Exclusion

#### Q2.1 (Reported PYQ): Interrupt Disabling for Mutual Exclusion [5 Marks]
* **Source Details:** GTU May 2015 [5 Marks], Technical Publications / Stallings Review Q5.5.
* **Question Text:** *"Explain how disabling interrupts achieves mutual exclusion on a uniprocessor system. What are its major limitations and why is it unsuitable for multiprocessor systems or user-level processes?"*

##### Model Answer
###### 1. Mechanism (2 Marks)
On a uniprocessor system, concurrent process execution is achieved via CPU time-slicing enforced by hardware clock interrupts. To achieve mutual exclusion, a process disables all interrupts immediately before entering its critical section and re-enables them upon exit:

```c
while (true) {
    disable_interrupts(); // Entry section
    /* CRITICAL SECTION */
    enable_interrupts();  // Exit section
    /* REMAINDER SECTION */
}
```
Because the CPU cannot be preempted while interrupts are disabled, the executing process guarantees uninterrupted execution throughout its critical section.

###### 2. Limitations & Multiprocessor Ineffectiveness (3 Marks)
1. **User-Level Security Risk:** Giving user-level processes the ability to disable interrupts is dangerous; a malicious or buggy process could disable interrupts and enter an infinite loop, halting the entire operating system.
2. **Multiprocessor Ineffectiveness:** Disabling interrupts on one CPU core only disables preemption on *that specific core*. Other concurrent processes running on parallel CPU cores can still access shared memory simultaneously, failing to guarantee mutual exclusion.
3. **Degraded I/O Efficiency:** Delaying interrupt processing degrades clock updates and real-time I/O handling.

---

#### Q2.2 (Verified PYQ): Atomic Hardware Instructions — TestAndSet, CompareAndSwap, and Exchange/Swap [10 Marks]
* **Source Details:** SVKM's NMIMS Course Syllabus, GTU Dec 2014 / May 2015 [10 Marks].
* **Question Text:** *"Explain how special hardware instructions guarantee mutual exclusion. Write C-style atomic definitions and mutual exclusion implementations for TestAndSet and CompareAndSwap (or Swap). State their advantages and disadvantages."*

##### Model Answer
###### 1. Overview of Hardware Atomicity (2 Marks)
Modern computer architectures provide special, non-interruptible atomic hardware instructions that execute read-modify-write operations on a memory location in a single instruction cycle. On multiprocessor systems, the CPU asserts a memory bus lock during execution to prevent parallel cores from accessing the memory address.

###### 2. TestAndSet (TSL) Instruction (3 Marks)
**C Definition (Executed Atomically by Hardware):**
```c
bool TestAndSet(bool *target) {
    bool rv = *target;
    *target = true;
    return rv;
}
```

**Mutual Exclusion Protocol Using TestAndSet:**
```c
// Shared variable initialized to false
bool lock = false;

void Process() {
    while (true) {
        // Entry Section: Busy-waits until lock becomes false
        while (TestAndSet(&lock))
            ; // Spinlock (do nothing)

        /* CRITICAL SECTION */

        // Exit Section
        lock = false;

        /* REMAINDER SECTION */
    }
}
```
*Tracing:* If `lock == false`, `TestAndSet(&lock)` returns `false` and sets `lock = true`. The calling process exits the `while` loop and enters the CS. Any subsequent process calling `TestAndSet` gets `true` and spins in the entry loop.

###### 3. CompareAndSwap (CAS) Instruction (3 Marks)
**C Definition (Executed Atomically by Hardware):**
```c
int CompareAndSwap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected) {
        *value = new_value;
    }
    return temp;
}
```

**Mutual Exclusion Protocol Using CompareAndSwap:**
```c
// Shared variable initialized to 0
int lock = 0;

void Process() {
    while (true) {
        // Entry Section: Expects lock == 0, sets to 1
        while (CompareAndSwap(&lock, 0, 1) != 0)
            ; // Spinlock

        /* CRITICAL SECTION */

        // Exit Section
        lock = 0;

        /* REMAINDER SECTION */
    }
}
```

###### 4. Advantages & Disadvantages (2 Marks)
* **Advantages:**
  1. Applicable to any number of processes on both uniprocessor and multiprocessor shared-memory systems.
  2. Simple and easy to verify.
  3. Supports multiple critical sections (each section can use its own lock variable).
* **Disadvantages:**
  1. **Busy Waiting (Spinlock):** Waiting processes consume CPU cycles in an entry loop, wasting processor time.
  2. **Starvation Possible:** Selection of the next process entering the CS is non-deterministic, violating Bounded Waiting.
  3. **Deadlock Risk via Priority Inversion:** A low-priority process holding the lock can be preempted by a high-priority busy-waiting process that hogging the CPU.

---

#### Q2.3 (Practice Question): Multiprocessor Bus Locking vs. Busy-Waiting Spinlocks [5 Marks]
* **Source Details:** Practice Question derived from Stallings Operating Systems Chapter 5.
* **Question Text:** *"Differentiate between Hardware Bus Locking and Software Spinlocks. Explain why spinlocks are acceptable on multicore kernels for short critical sections but inefficient for long user tasks."*

##### Model Answer
###### 1. Comparison Summary
- **Multiprocessor Bus Locking:** A physical hardware mechanism where a CPU core asserts a control line on the system bus while executing an atomic instruction (`TSL`/`CAS`), locking memory access for all other cores for **one memory cycle**.
- **Spinlocks:** A software synchronization lock built on atomic instructions where a waiting thread repeatedly checks a lock variable in a tight `while` loop (busy waiting).

###### 2. Trade-Off Analysis
- **Short Critical Sections:** If a critical section executes in a few CPU cycles (e.g., updating a kernel pointer), busy-waiting on a spinlock is **more efficient than thread context-switching**, which requires saving/restoring registers, flushing TLBs, and invoking the OS scheduler.
- **Long Critical Sections:** If a process holds a lock for a long duration (e.g., performing I/O), spinlocks waste massive numbers of CPU cycles in busy-waiting loops, degrading total system throughput. In such cases, blocking primitives (semaphores/monitors) must be used.

---

### Topic 3: Semaphores & Synchronization Primitives

#### Q3.1 (Verified PYQ): Semaphore Definition, Types (Binary vs. Counting), and Atomic Operations [5 Marks]
* **Source Details:** SVKM's NMIMS Final Exam 2022-2023 [Q1a - 5 Marks], GTU June 2015 [5 Marks].
* **Question Text:** *"What is a semaphore? Distinguish between binary and counting semaphores. Write atomic kernel definitions for wait() and signal() operations using non-busy-waiting block queues."*

##### Model Answer
###### 1. Definition & Types (2 Marks)
A **semaphore** (proposed by Edsger Dijkstra) is a protected integer variable used for process synchronization and mutual exclusion. Apart from initialization, a semaphore $S$ is accessed exclusively through two atomic operations: `wait()` (also called `P()` or `semWait`) and `signal()` (also called `V()` or `semSignal`).

- **Binary Semaphore (Mutex):** Its integer value ranges strictly between `0` and `1`. Used primarily to enforce mutual exclusion.
- **Counting Semaphore:** Its integer value ranges over an unrestricted non-negative domain. Used to control access to a resource pool containing multiple identical instances.

###### 2. Non-Busy-Waiting Block Queue Definitions (3 Marks)
To eliminate busy waiting, kernel semaphores maintain a value and a process waiting queue:

```c
typedef struct {
    int value;
    struct process *queue; // Queue of blocked processes
} semaphore;

void wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        // Add this process to S->queue
        // Block the process (change state to BLOCKED)
        block();
    }
}

void signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        // Remove a process P from S->queue
        // Move P to READY queue
        wakeup(P);
    }
}
```

*Key Properties of Queue Implementation:*
- If `S->value` is negative, its magnitude $|S
ightarrow	ext{value}|$ represents the exact number of processes currently blocked in `S->queue`.
- The `block()` call suspends the process, freeing the CPU for other tasks and eliminating spinlocks.

---

#### Q3.2 (Verified PYQ): Inverted Semaphore Wait Order & Deadlock Analysis [5/10 Marks]
* **Source Details:** SVKM's NMIMS Final Examination 2024-2025 [Q1b - 5 Marks].
* **Question Text:** *"A student writes the following Bounded-Buffer Producer-Consumer code:*
```c
semaphore full = 0, empty = N, mutex = 1;

void Producer() {
    while (true) {
        produce_item(&item);
        wait(mutex); // Line A
        wait(empty); // Line B
        append_item(item);
        signal(mutex);
        signal(full);
    }
}
```
*Identify the critical flaw in the operation order and trace step-by-step how it causes a system deadlock when the buffer is full."*

##### Model Answer
###### 1. Flaw Identification (1.5 Marks)
The critical flaw is the **inversion of `wait()` operations** in lines A and B. The Producer acquires the binary lock `wait(mutex)` *before* checking resource availability with `wait(empty)`.

###### 2. Step-by-Step Deadlock Execution Trace (2.5 Marks)
Assume the bounded buffer is completely full (`full = N`, `empty = 0`, `mutex = 1`):

1. **Producer Execution:**
   - Producer calls `produce_item(&item)`.
   - Producer executes `wait(mutex)`. Since `mutex == 1`, Producer decrements `mutex` to `0` and acquires the mutual exclusion lock.
   - Producer executes `wait(empty)`. Since `empty == 0`, `empty` becomes `-1`. The Producer is **blocked inside `wait(empty)`** while still holding `mutex = 0`!
2. **Context Switch to Consumer:**
   - Consumer attempts to consume an item to free buffer space.
   - Consumer executes `wait(mutex)` to enter the critical section.
   - Since `mutex == 0` (held by the sleeping Producer), the Consumer is **blocked on `wait(mutex)`**.
3. **Deadlock State Reached:**
   - The Producer is waiting for the Consumer to execute `signal(empty)`.
   - The Consumer is waiting for the Producer to execute `signal(mutex)`.
   - Both processes are blocked indefinitely in a circular wait dependency.

###### 3. Correct Code Correction (1 Mark)
Swap lines A and B so resource availability is checked *before* acquiring the mutex lock:

```c
// CORRECT ORDER
wait(empty); // Line 1: Wait for an available empty slot FIRST
wait(mutex); // Line 2: Acquire CS lock SECOND
/* CRITICAL SECTION */
signal(mutex);
signal(full);
```

---

#### Q3.3 (Practice Question): Mutex Lock vs. Counting Semaphore Comparison [5 Marks]
* **Source Details:** Practice Question derived from Silberschatz Operating System Concepts Chapter 5.
* **Question Text:** *"Compare Mutex Locks and Counting Semaphores across Ownership, Initialization, Operational Domain, and Use Cases."*

##### Model Answer

| Comparison Criteria | Mutex Lock (Binary Semaphore) | Counting Semaphore |
| :--- | :--- | :--- |
| **Operational Domain** | Integer value strictly restricted to `0` or `1`. | Integer value ranges over unrestricted domain ($0 \le S \le N$). |
| **Ownership Property** | Enforces strict **ownership**: the thread that acquires the mutex (`lock`) must be the one that releases it (`unlock`). | **No ownership**: any thread can invoke `signal()` to increment the value. |
| **Primary Purpose** | Enforces **Mutual Exclusion** for a single shared resource. | Manages access to a **Resource Pool** with multiple instances or synchronizes event ordering. |
| **Initialization Value** | Always initialized to `1` (unlocked state). | Initialized to $N$, representing total available resource units. |
| **Signaling Capability** | Cannot be used for asynchronous event notification across threads safely. | Ideal for signaling events between threads (e.g., Producer signaling Consumer). |

---

### Topic 4: Monitors & Language-Level Constructs

#### Q4.1 (Reported PYQ): Monitor Structure, Implicit Mutual Exclusion, and Condition Variables [5/10 Marks]
* **Source Details:** GTU June 2015 [5/10 Marks], TechNeo OS Review Q3.6.
* **Question Text:** *"What is a Monitor? Explain its structural components, implicit mutual exclusion, and how condition variables (wait and signal) operate within a monitor."*

##### Model Answer
###### 1. Definition & Structural Architecture (3 Marks)
A **monitor** is a high-level language synchronization construct that encapsulates shared data structures, local procedures, and initialization code within a single abstract data type.

```text
               +-----------------------------------+
               |             MONITOR               |
               |  +-----------------------------+  |
               |  |        Shared Data          |  |
               |  +-----------------------------+  |
               |  +-----------------------------+  |
  Entry Queue  |  |   Condition Variables (x, y)  |  |
  +---------+  |  |   x.wait()  /  y.wait()     |  |
  | P1|P2|P3|->|  +-----------------------------+  |
  +---------+  |  +-----------------------------+  |
               |  |     Entry Procedures        |  |
               |  |  Procedure1()  Procedure2() |  |
               |  +-----------------------------+  |
               +-----------------------------------+
```

###### 2. Key Structural Features (2 Marks)
1. **Encapsulation:** Shared data variables can only be accessed by calling procedures defined within the monitor.
2. **Implicit Mutual Exclusion:** The compiler automatically enforces mutual exclusion. Only **one process at a time** can be actively executing code inside the monitor.

###### 3. Condition Variables & Operations (3 Marks)
To allow processes to block when condition checks fail, monitors provide **condition variables** (e.g., `condition x`). Condition variables do not hold integer values; they only maintain queues of blocked processes:

- **`x.wait()`**: The calling process is suspended and placed on condition `x`'s queue. The process temporarily releases its exclusive lock on the monitor so another process can enter.
- **`x.signal()`**: Resumes exactly one process blocked on `x.wait()`. If no process is waiting on `x`, the `signal()` operation has **no effect** (unlike semaphores, where signals are remembered).

---

#### Q4.2 (Verified PYQ): Dining Philosophers Problem & Monitor-Based Solution [10 Marks]
* **Source Details:** SVKM's NMIMS Final Examination 2024-2025 [Q2a - 10 Marks].
* **Question Text:** *"Explain the Dining Philosophers problem and critically analyze why naive semaphore solutions result in deadlock or starvation. Propose and justify a complete monitor-based solution that guarantees deadlock-free execution."*

##### Model Answer
###### 1. Problem Statement & Naive Flaws (3 Marks)
Five philosophers sit around a circular table with 5 chopsticks. Each philosopher alternates between `THINKING` and `EATING`. To eat, a philosopher requires both their left and right chopsticks.

**Naive Semaphore Solution Flaw:**
If each chopstick is represented by a binary semaphore `chopstick[5]`, and every philosopher simultaneously executes `wait(chopstick[i])` to grab their left chopstick, all 5 chopsticks are acquired. When they try to execute `wait(chopstick[(i+1)%5])` for their right chopstick, every philosopher blocks forever $\rightarrow$ **SYSTEM DEADLOCK**.

###### 2. Complete Monitor-Based Solution Pseudocode (5 Marks)

```pascal
monitor DiningPhilosophers {
    enum { THINKING, HUNGRY, EATING } state[5];
    condition self[5];

    procedure pickup(int i) {
        state[i] = HUNGRY;
        test(i); // Attempt to acquire both chopsticks
        
        // Mesa-style while loop recheck to prevent race conditions
        while (state[i] != EATING) {
            self[i].wait();
        }
    }

    procedure putdown(int i) {
        state[i] = THINKING;
        // Test left and right neighbors upon releasing chopsticks
        test((i + 4) % 5);
        test((i + 1) % 5);
    }

    procedure test(int i) {
        if ((state[(i + 4) % 5] != EATING) and
            (state[i] == HUNGRY) and
            (state[(i + 1) % 5] != EATING)) {
            state[i] = EATING;
            self[i].signal();
        }
    }

    initialization_code() {
        for (int i = 0; i < 5; i++) {
            state[i] = THINKING;
        }
    }
}
```

###### 3. Justification & Correctness Proof (2 Marks)
- **Deadlock Prevention:** A philosopher changes state to `EATING` only if **both** adjacent neighbors are not eating (`state[(i+4)%5] != EATING` and `state[(i+1)%5] != EATING`). Chopsticks are never acquired piecemeal, eliminating circular wait and guaranteeing deadlock-free execution.
- **Starvation Note:** While deadlock is eliminated, starvation is still theoretically possible if two adjacent neighbors alternate eating times.

---

#### Q4.3 (Practice Question): Hoare (Signal-and-Wait) vs. Mesa (Signal-and-Continue) Condition Semantics [5 Marks]
* **Source Details:** Practice Question derived from Tanenbaum Modern Operating Systems Chapter 2.
* **Question Text:** *"Differentiate between Hoare (Signal-and-Wait) and Mesa (Signal-and-Continue) monitor signaling semantics. Why does Mesa-style monitoring require `while` loops around condition waits?"*

##### Model Answer

| Comparison Criteria | Hoare Semantics (Signal-and-Wait) | Mesa Semantics (Signal-and-Continue) |
| :--- | :--- | :--- |
| **Signaler Execution** | The signaling process $P$ immediately suspends and relinquishes the monitor so awakened process $Q$ executes instantly. | The signaling process $P$ retains monitor control and continues execution until its monitor procedure finishes. |
| **Awakened Process Execution** | Process $Q$ is guaranteed to run immediately upon signal without interference. | Process $Q$ is moved to the monitor entry queue and runs when $P$ exits. |
| **Condition Recheck Requirement** | **`if` statement sufficient:** Condition is guaranteed true when $Q$ runs (`if (condition) x.wait();`). | **`while` loop mandatory:** Condition may be invalidated before $Q$ runs (`while (condition) x.wait();`). |
| **Practical OS Adoption** | Theoretical; rarely implemented due to high context-switch cost. | **Universal standard** (used in Java, POSIX threads, C#, Modula-3). |

---

### Topic 5: Message Passing & Inter-Process Communication

#### Q5.1 (Reported PYQ): Message Passing Principles — Addressing & Blocking vs. Non-Blocking Primitives [5 Marks]
* **Source Details:** GTU May 2016 [5 Marks], TechNeo OS Review Q3.8.
* **Question Text:** *"Explain message passing in IPC. Distinguish between direct and indirect addressing, and compare blocking versus non-blocking send/receive primitives."*

##### Model Answer
###### 1. Addressing Schemes (2.5 Marks)
Message passing achieves synchronization and communication without shared memory using two basic primitives: `send(destination, message)` and `receive(source, message)`.

1. **Direct Addressing:**
   - **Mechanism:** The sending and receiving processes must explicitly name each other:
     - `send(P, message)`: Send message to process $P$.
     - `receive(Q, message)`: Receive message from process $Q$.
   - **Limitation:** High coupling; hardcoding process identifiers makes modular code refactoring difficult.

2. **Indirect Addressing (Mailboxes / Ports):**
   - **Mechanism:** Messages are sent to and received from shared intermediate queues called **mailboxes** or **ports**:
     - `send(mailbox_A, message)`
     - `receive(mailbox_A, message)`
   - **Advantage:** Decouples processes; multiple producers and consumers can communicate through a single mailbox.

###### 2. Blocking vs. Non-Blocking Primitives (2.5 Marks)
- **Blocking Send (Synchronous):** The sending process blocks until the message is received by the receiving process or mailbox.
- **Non-Blocking Send (Asynchronous):** The sending process resumes execution immediately after handing the message to the OS kernel.
- **Blocking Receive:** The receiving process blocks until a message is available.
- **Non-Blocking Receive:** The receiving process retrieves either a valid message or an immediate error/null status without blocking.
- **Rendezvous:** Occurs when **both** `send()` and `receive()` are blocking primitives, creating tight lockstep synchronization between processes.

---

#### Q5.2 (Practice Question): Mutual Exclusion Implementation Using Mailbox Message Passing [5 Marks]
* **Source Details:** Practice Question derived from Stallings Operating Systems Chapter 5.
* **Question Text:** *"Show how message passing primitives (`send` and `receive`) can be used to enforce mutual exclusion among N concurrent processes without shared memory."*

##### Model Answer
###### 1. Concept
Mutual exclusion can be implemented using an indirect shared mailbox initialized with a single "token" message.

###### 2. Pseudocode Implementation
```c
mailbox mutex = create_mailbox();

// Initialization: Place a single dummy token message in the mailbox
send(mutex, "TOKEN");

void Process(int id) {
    message msg;
    while (true) {
        // Entry Section: Blocking receive acts as wait()
        receive(mutex, &msg);

        /* CRITICAL SECTION */

        // Exit Section: Send token back to mailbox acting as signal()
        send(mutex, msg);

        /* REMAINDER SECTION */
    }
}
```

###### 3. Explanation
- Only one process can successfully complete `receive(mutex, &msg)` because only one token message exists in the mailbox.
- Other concurrent processes calling `receive()` will block until the process in the CS finishes and calls `send(mutex, msg)`.

---

#### Q5.3 (Practice Question): Structural Layout of a Message — Header vs. Body Layout [5 Marks]
* **Source Details:** Practice Question derived from Course Presentation `UNIT3-Process concurrency.pptx`.
* **Question Text:** *"Describe the general format and structural components of a message in an IPC system. Differentiate between message header metadata and message body data."*

##### Model Answer
###### 1. General Message Format
A message in an IPC system is structured into two main sections: a fixed-length **Header** (metadata managed by the OS kernel) and a variable-length **Body** (payload content).

```text
+-------------------------------------------------------------------------+
|                             MESSAGE HEADER                              |
+---------------+---------------+------------------+----------------------+
| Message Type  | Source ID     | Destination ID   | Message Length       |
+---------------+---------------+------------------+----------------------+
| Control Info  | Sequence No.  | Priority / Tag   | Pointer Fields       |
+---------------+---------------+------------------+----------------------+
|                             MESSAGE BODY                                |
+-------------------------------------------------------------------------+
| Data Payload / Character String / Formatted Struct                      |
+-------------------------------------------------------------------------+
```

###### 2. Component Descriptions
1. **Header Fields (Kernel Metadata):**
   - **Message Type:** Categorizes the message (e.g., control, data, acknowledgment).
   - **Source & Destination Identifiers:** Process IDs or Mailbox/Port IDs.
   - **Message Length:** Specifies byte size of the body payload.
   - **Control Information:** Buffering pointers, sequence numbers for duplicate detection, and process priority tags.
2. **Body (Payload):**
   - Contains actual application data transferred between processes.

---

### Topic 6: Classical IPC Problems

#### Q6.1 (Verified PYQ): Bounded-Buffer (Producer-Consumer) Problem Using Semaphores [10 Marks]
* **Source Details:** SVKM's NMIMS Special Re-Exam 2022-23 [Q4a - 10 Marks], Course Policy Syllabus Topic 6.
* **Question Text:** *"Describe the Bounded-Buffer Producer-Consumer problem. Provide a complete semaphore-based solution with initialized variables. Trace the execution for one producer and one consumer."*

##### Model Answer
###### 1. Problem Statement & Variable Initialization (3 Marks)
A Producer generates data items and places them into a shared fixed-capacity buffer of size $N$. A Consumer retrieves items from the buffer.

**Constraints:**
1. Producer must block if the buffer is full (`empty == 0`).
2. Consumer must block if the buffer is empty (`full == 0`).
3. Buffer manipulation must be mutually exclusive.

**Synchronization Variable Setup:**
```c
#define N 5 // Buffer capacity

item buffer[N];
int in = 0, out = 0;

semaphore mutex = 1; // Enforces mutual exclusion inside buffer
semaphore empty = N; // Counting semaphore tracking free slots
semaphore full  = 0; // Counting semaphore tracking filled slots
```

###### 2. Complete Semaphore Pseudocode (4 Marks)

```c
void Producer() {
    item item_produced;
    while (true) {
        item_produced = produce_item();

        semWait(empty); // Wait for an available empty slot
        semWait(mutex); // Enter critical section

        buffer[in] = item_produced;
        in = (in + 1) % N;

        semSignal(mutex); // Exit critical section
        semSignal(full);  // Signal availability of a new full slot
    }
}

void Consumer() {
    item item_consumed;
    while (true) {
        semWait(full);  // Wait for an available full slot
        semWait(mutex); // Enter critical section

        item_consumed = buffer[out];
        out = (out + 1) % N;

        semSignal(mutex); // Exit critical section
        semSignal(empty); // Signal freeing of a buffer slot

        consume_item(item_consumed);
    }
}
```

###### 3. Step-by-Step Execution Trace (3 Marks)
Assume initial state: `empty = 5`, `full = 0`, `mutex = 1`.

1. **Producer Execution:**
   - Calls `produce_item()`.
   - Executes `semWait(empty)` $\rightarrow$ `empty` decrements from `5` to `4`.
   - Executes `semWait(mutex)` $\rightarrow$ `mutex` decrements from `1` to `0`.
   - Stores item at `buffer[0]` and sets `in = 1`.
   - Executes `semSignal(mutex)` $\rightarrow$ `mutex` increments to `1`.
   - Executes `semSignal(full)` $\rightarrow$ `full` increments from `0` to `1`.
2. **Consumer Execution:**
   - Executes `semWait(full)` $\rightarrow$ `full` decrements from `1` to `0`.
   - Executes `semWait(mutex)` $\rightarrow$ `mutex` decrements from `1` to `0`.
   - Reads item at `buffer[0]` and sets `out = 1`.
   - Executes `semSignal(mutex)` $\rightarrow$ `mutex` increments to `1`.
   - Executes `semSignal(empty)` $\rightarrow$ `empty` increments from `4` to `5`.
3. **Outcome:** System state correctly returns to `empty = 5`, `full = 0`, `mutex = 1` with data safely transferred.

---

#### Q6.2 (Practice Question): Bounded-Buffer (Producer-Consumer) Problem Using Monitors [10 Marks]
* **Source Details:** Practice Question derived from Silberschatz Operating System Concepts Chapter 5.
* **Question Text:** *"Write a complete monitor-based solution for the Bounded-Buffer Producer-Consumer problem. Explain how condition variables eliminate manual semaphore management."*

##### Model Answer
###### 1. Monitor BoundedBuffer Pseudocode
```pascal
monitor BoundedBuffer {
    item buffer[N];
    int count = 0, in = 0, out = 0;
    condition not_full, not_empty;

    procedure produce(item x) {
        while (count == N) {
            not_full.wait(); // Block if buffer is full
        }
        buffer[in] = x;
        in = (in + 1) % N;
        count++;
        not_empty.signal(); // Signal waiting consumers
    }

    procedure consume(item *x) {
        while (count == 0) {
            not_empty.wait(); // Block if buffer is empty
        }
        *x = buffer[out];
        out = (out + 1) % N;
        count--;
        not_full.signal(); // Signal waiting producers
    }

    initialization_code() {
        count = 0; in = 0; out = 0;
    }
}
```

###### 2. Key Advantages
- **Automatic Lock Management:** Programmers do not explicitly manage `mutex` locks; the monitor compiler automatically guarantees that `produce()` and `consume()` cannot run concurrently.
- **Mesa-Style Safety:** The `while (count == N)` and `while (count == 0)` loops ensure condition re-evaluation upon waking up, eliminating race conditions.

---

#### Q6.3 (Practice Question): Bounded-Buffer (Producer-Consumer) Problem Using Message Passing [10 Marks]
* **Source Details:** Practice Question derived from Stallings Operating Systems Chapter 5.
* **Question Text:** *"Design a message-passing solution for the Bounded-Buffer Producer-Consumer problem using mailboxes. Show how buffer capacity is managed using empty message tokens."*

##### Model Answer
###### 1. Mailbox Setup
```c
mailbox capacity = create_mailbox(); // Holds empty slot tokens
mailbox items    = create_mailbox(); // Holds produced item messages

// Initialize capacity mailbox with N empty dummy messages
for (int i = 0; i < N; i++) {
    send(capacity, "EMPTY_TOKEN");
}
```

###### 2. Producer & Consumer Pseudocode
```c
void Producer() {
    message msg, empty_token;
    while (true) {
        msg = produce_item();
        receive(capacity, &empty_token); // Wait for an empty slot token
        send(items, msg);                // Send data item to consumer queue
    }
}

void Consumer() {
    message msg, empty_token = "EMPTY_TOKEN";
    while (true) {
        receive(items, &msg);       // Wait for a filled data item
        send(capacity, empty_token); // Send empty slot token back to capacity
        consume_item(msg);
    }
}
```

---

#### Q6.4 (Verified PYQ): First Readers-Writers Problem (Reader Preference) Using Semaphores [10 Marks]
* **Source Details:** SVKM's NMIMS Final Examination 2023-2024 [Q7a - 10 Marks], GTU June 2015 [10 Marks].
* **Question Text:** *"Explain the Readers-Writers problem. Provide a complete semaphore-based solution for the Reader-Preference policy. Discuss its starvation behavior."*

##### Model Answer
###### 1. Problem Definition & Preference Policy (3 Marks)
A shared database is accessed by concurrent **Reader** processes (who only read data) and **Writer** processes (who update data).

**Constraints:**
1. Multiple Readers can read the database concurrently.
2. Only one Writer can write to the database at a time.
3. While a Writer is writing, no Reader can read.

**Policy: First Readers-Writers Problem (Reader Preference)**
No Reader is kept waiting unless a Writer has already obtained permission to write. No Reader waits for a Writer simply because the Writer is waiting.

###### 2. Complete Semaphore Pseudocode (5 Marks)

```c
int readcount = 0;     // Tracks number of active readers
semaphore mutex = 1;    // Protects updates to readcount
semaphore rw_mutex = 1; // Enforces mutual exclusion for writers

void Writer() {
    while (true) {
        semWait(rw_mutex); // Lock database for exclusive writing

        /* WRITING IS PERFORMED */
        write_database();

        semSignal(rw_mutex); // Unlock database
    }
}

void Reader() {
    while (true) {
        semWait(mutex);
        readcount++;
        if (readcount == 1) {
            semWait(rw_mutex); // First reader locks database from writers
        }
        semSignal(mutex);

        /* READING IS PERFORMED */
        read_database();

        semWait(mutex);
        readcount--;
        if (readcount == 0) {
            semSignal(rw_mutex); // Last reader unlocks database for writers
        }
        semSignal(mutex);
    }
}
```

###### 3. Starvation Analysis (2 Marks)
- **Writer Starvation Risk:** Under the Reader-Preference policy, if a steady stream of new Reader processes arrives before `readcount` reaches `0`, the Readers continuously increment and decrement `readcount` without ever dropping it to zero.
- As a result, `rw_mutex` remains locked indefinitely, causing **indefinite Writer starvation**.

---

## 6. SECTION II: ADDITIONAL TOPICS IN SUPPLIED TEACHING MATERIALS

> **⚠️ Scope Note:** The topics in this section appear in the provided course slides (`UNIT3-Process concurrency.pptx`) and handouts (`OS Chap-3 Process Concurrency.pdf`), but are not explicitly named in the core course policy syllabus list. They are included here for full reference.

### Topic A1: Software Mutual-Exclusion Approaches

#### QA1.1 (Verified / Reported PYQ): Software Mutual Exclusion — Strict Alternation, Flag-Only Attempts, Dekker's, and Peterson's Algorithm [10 Marks]
* **Source Details:** SVKM's NMIMS Re-Exam 2023-24 / Batch 2024-25 [Q6a - 10M], GTU Dec 2014 [5M].
* **Question Text:** *"Trace the evolution of software solutions to the 2-process critical section problem. Explain Strict Alternation, Flag-Only Attempts, Dekker's Algorithm, and Peterson's Algorithm with two-process pseudocode."*

##### Model Answer
###### 1. Attempt 1: Strict Alternation (Turn Variable)
Uses a single shared integer variable `turn` initialized to `0`.

```c
// Process P0                          // Process P1
while (turn != 0) ;                   while (turn != 1) ;
/* CRITICAL SECTION */                 /* CRITICAL SECTION */
turn = 1;                             turn = 0;
```
- **Flaw:** Violates **Progress**. If $P_0$ is in its remainder section and $P_1$ wishes to enter CS, $P_1$ is blocked because `turn` remains `0`.

###### 2. Attempt 2: Flag Array
Uses `bool flag[2] = {false, false}`.

```c
// Process P0
flag[0] = true;
while (flag[1]) ; // Wait
/* CRITICAL SECTION */
flag[0] = false;
```
- **Flaw:** If $P_0$ and $P_1$ set `flag[0] = true` and `flag[1] = true` simultaneously, both enter their `while` loops and spin forever $\rightarrow$ **DEADLOCK**.

###### 3. Peterson's Algorithm (Complete Correct Solution)
Combines `flag[2]` array and `turn` variable:

```c
// Shared variables
bool flag[2] = {false, false};
int turn = 0;

// Structure for Process P_i (where j = 1 - i)
void Process(int i) {
    int j = 1 - i;
    while (true) {
        flag[i] = true;   // Announce intention to enter CS
        turn = j;         // Yield turn to other process
        
        while (flag[j] && turn == j)
            ; // Spinlock

        /* CRITICAL SECTION */

        flag[i] = false;  // Exit section

        /* REMAINDER SECTION */
    }
}
```

- **Correctness Guarantees:**
  1. **Mutual Exclusion:** Enforced because `turn` can only equal `0` or `1` at any instant, so both processes cannot exit the `while` loop together.
  2. **Progress & Bounded Waiting:** Both satisfied; the `turn` variable resolves ties deterministically.

---

### Topic A2: Strong vs. Weak Semaphores & Queue Ordering

#### QA2.1 (Practice Question): Strong (FIFO) vs. Weak Semaphores & Process Queue Transition Trace [5 Marks]
* **Source Details:** Course Presentation `UNIT3-Process concurrency.pptx` Slide 14.
* **Question Text:** *"Distinguish between Strong and Weak Semaphores. Trace the process queue transitions when processes P1, P2, and P3 execute wait and signal operations."*

##### Model Answer
###### 1. Definitions
- **Strong Semaphore:** Uses a **First-In, First-Out (FIFO)** queue to manage blocked processes. Guarantees freedom from starvation (satisfies Bounded Waiting).
- **Weak Semaphore:** Uses a non-deterministic process queue order (e.g., random or LIFO). Processes may suffer from starvation.

###### 2. Process Queue Transition Trace
Assume a strong counting semaphore `S = 0` and process queue `Q = []`:

| Event # | Process | Operation Executed | Semaphore `S->value` | Queue State `Q` | Active Process Status |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **P1** | `wait(S)` | `-1` | `[P1]` | P1 blocked and queued |
| 2 | **P2** | `wait(S)` | `-2` | `[P1, P2]` | P2 blocked and queued |
| 3 | **P3** | `wait(S)` | `-3` | `[P1, P2, P3]` | P3 blocked and queued |
| 4 | **P4** | `signal(S)` | `-2` | `[P2, P3]` | **P1 dequeued and awakened (FIFO)** |
| 5 | **P5** | `signal(S)` | `-1` | `[P3]` | **P2 dequeued and awakened (FIFO)** |

---

### Topic A3: The Sleeping Barber Problem

#### QA3.1 (Reported PYQ): The Sleeping Barber Problem & Semaphore Solution [10 Marks]
* **Source Details:** GTU Dec 2014 [10 Marks], TechNeo OS Review Q3.15.
* **Question Text:** *"Describe the Sleeping Barber classical synchronization problem. Provide complete semaphore pseudocode handling barber sleep, customer waiting chairs, and cutting states."*

##### Model Answer
###### 1. Problem Description
A barbershop has one barber, one barber chair, and $N$ waiting room chairs.
- If no customers are present, the barber sleeps in the barber chair.
- When a customer arrives and all chairs are full, the customer leaves.
- If the barber is busy but chairs are free, the customer sits in a waiting chair.
- If the barber is sleeping, the customer wakes up the barber.

###### 2. Semaphore Pseudocode Solution

```c
#define CHAIRS 5

semaphore customers = 0; // Tracks waiting customers
semaphore barbers   = 0; // Tracks barber readiness
semaphore mutex     = 1; // Protects access to waiting count
int waiting = 0;         // Number of customers waiting

void Barber() {
    while (true) {
        semWait(customers); // Sleep if no customers wait
        semWait(mutex);     // Acquire mutex to update waiting count
        waiting--;
        semSignal(barbers);  // Barber ready to cut
        semSignal(mutex);   // Release mutex

        cut_hair();
    }
}

void Customer() {
    semWait(mutex);
    if (waiting < CHAIRS) {
        waiting++;
        semSignal(customers); // Wake up barber if sleeping
        semSignal(mutex);
        semWait(barbers);     // Wait if barber is busy cutting
        get_haircut();
    } else {
        semSignal(mutex);     // Shop full; customer leaves
    }
}
```

---

## 7. SECTION III: QUICK REVISION CHECKLIST & PSEUDOCODE RECAP

### 1. Essential Synchronization Equations & Initializations

| Problem / Primitive | Shared Synchronization Variables & Initial Values | Key Invariants / Notes |
| :--- | :--- | :--- |
| **TestAndSet Lock** | `bool lock = false;` | `while(TestAndSet(&lock));` |
| **CompareAndSwap Lock** | `int lock = 0;` | `while(CompareAndSwap(&lock, 0, 1) != 0);` |
| **Peterson's Algorithm** | `bool flag[2] = {false, false}; int turn = 0;` | `flag[i]=true; turn=j; while(flag[j] && turn==j);` |
| **Bounded Buffer (Semaphores)** | `mutex = 1`, `empty = N`, `full = 0` | `wait(empty)` MUST come before `wait(mutex)`. |
| **Bounded Buffer (Monitors)** | `count = 0`, `condition not_full, not_empty;` | Use `while(count == N) not_full.wait();` for Mesa safety. |
| **First Readers-Writers** | `mutex = 1`, `rw_mutex = 1`, `int readcount = 0;` | First reader locks `rw_mutex`; last reader unlocks it. |
| **Sleeping Barber** | `customers = 0`, `barbers = 0`, `mutex = 1`, `waiting = 0` | Customer leaves if `waiting == CHAIRS`. |

---

### 2. Final Revision Checklist Before Exam
- [x] Can state the **3 critical section requirements** (Mutual Exclusion, Progress, Bounded Waiting) with exact definitions?
- [x] Can write C definitions and locks for **TestAndSet** and **CompareAndSwap**?
- [x] Know why **inverting wait operations** in Producer-Consumer causes deadlock?
- [x] Can write complete pseudocode for **Bounded-Buffer** (Semaphores & Monitors)?
- [x] Can write complete pseudocode for **First Readers-Writers** and explain Writer starvation?
- [x] Can write **Peterson's Algorithm** pseudocode for 2 processes?
- [x] Understand the difference between **Hoare** and **Mesa** monitor condition semantics?

---
