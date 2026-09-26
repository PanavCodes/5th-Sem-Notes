# Operating Systems: Unit 3 — Process Concurrency Study Notes

---

## Table of Contents
- [Operating Systems: Unit 3 — Process Concurrency Study Notes](#operating-systems-unit-3--process-concurrency-study-notes)
  - [Table of Contents](#table-of-contents)
  - [1. Principles of Concurrency \& Critical Section Problem](#1-principles-of-concurrency--critical-section-problem)
    - [1.1 Fundamentals of Concurrent Execution](#11-fundamentals-of-concurrent-execution)
    - [1.2 Shared Resources \& Race Conditions](#12-shared-resources--race-conditions)
      - [Conceptual Explanation](#conceptual-explanation)
      - [Concrete Example 1: The Shared Counter Race Condition](#concrete-example-1-the-shared-counter-race-condition)
        - [Unsynchronized Execution Interleaving](#unsynchronized-execution-interleaving)
      - [Concrete Example 2: The Shared echo() Procedure Race Condition](#concrete-example-2-the-shared-echo-procedure-race-condition)
        - [Scenario A: Uniprocessor System (Interleaving Interruption)](#scenario-a-uniprocessor-system-interleaving-interruption)
        - [Scenario B: Multiprocessor System (Overlapping Execution)](#scenario-b-multiprocessor-system-overlapping-execution)
        - [Single Access Enforcement](#single-access-enforcement)
    - [1.3 Difficulties of Concurrency \& OS Concerns](#13-difficulties-of-concurrency--os-concerns)
      - [Difficulties of Concurrency](#difficulties-of-concurrency)
      - [OS Concerns and Responsibilities](#os-concerns-and-responsibilities)
    - [1.4 Critical Section Framework](#14-critical-section-framework)
      - [General Structure of a Concurrent Process](#general-structure-of-a-concurrent-process)
    - [1.5 Three Requirements for Critical-Section Solutions](#15-three-requirements-for-critical-section-solutions)
    - [1.6 Additional topics covered in the supplied PPT/PDF: Software Mutual Exclusion](#16-additional-topics-covered-in-the-supplied-pptpdf-software-mutual-exclusion)
      - [Attempt 1: Strict Alternation Using turn Variable](#attempt-1-strict-alternation-using-turn-variable)
        - [Pseudocode](#pseudocode)
        - [Evaluation](#evaluation)
      - [Attempt 2: Flag-Only Solution](#attempt-2-flag-only-solution)
        - [Pseudocode](#pseudocode-1)
        - [Evaluation](#evaluation-1)
      - [Dekker's Algorithm](#dekkers-algorithm)
        - [Shared Variables](#shared-variables)
        - [Pseudocode](#pseudocode-2)
        - [Evaluation](#evaluation-2)
      - [Peterson's Algorithm](#petersons-algorithm)
        - [Shared Variables](#shared-variables-1)
        - [Pseudocode (Process $P\_i$, where $j = 1 - i$)](#pseudocode-process-p_i-where-j--1---i)
        - [Verification of Criteria](#verification-of-criteria)
        - [Modern Limitation](#modern-limitation)
    - [1.7 Exam-Ready Brief \& Common Mistakes](#17-exam-ready-brief--common-mistakes)
      - [Concise Exam Definition](#concise-exam-definition)
      - [Common Student Mistakes](#common-student-mistakes)
  - [2. Mutual Exclusion: Hardware Approaches](#2-mutual-exclusion-hardware-approaches)
    - [2.1 Interrupt Disabling](#21-interrupt-disabling)
      - [Evaluation \& Limitations](#evaluation--limitations)
    - [2.2 Atomic Hardware Instructions](#22-atomic-hardware-instructions)
      - [2.2.1 TestAndSet Instruction](#221-testandset-instruction)
        - [C Definition (Executed Atomically by Hardware)](#c-definition-executed-atomically-by-hardware)
        - [Mutual Exclusion Implementation](#mutual-exclusion-implementation)
        - [Mechanism](#mechanism)
      - [2.2.2 CompareAndSwap / Swap Instruction](#222-compareandswap--swap-instruction)
        - [CompareAndSwap C Definition](#compareandswap-c-definition)
        - [Mutual Exclusion Implementation Using CompareAndSwap](#mutual-exclusion-implementation-using-compareandswap)
        - [Swap Instruction C Definition](#swap-instruction-c-definition)
        - [Mutual Exclusion Implementation Using Swap](#mutual-exclusion-implementation-using-swap)
    - [2.3 Comparison Table of Hardware Approaches](#23-comparison-table-of-hardware-approaches)
    - [2.4 Exam-Ready Brief \& Common Mistakes](#24-exam-ready-brief--common-mistakes)
      - [Concise Summary](#concise-summary)
      - [Common Student Mistakes](#common-student-mistakes-1)
  - [3. Semaphores](#3-semaphores)
    - [3.1 Definition \& Atomic Operations](#31-definition--atomic-operations)
      - [Standard Classic Definitions (Dijkstra)](#standard-classic-definitions-dijkstra)
      - [Non-Busy Waiting (Block-Queue) Kernel Implementation](#non-busy-waiting-block-queue-kernel-implementation)
        - [Physical Meaning of $S.\\text{value}$ in Block-Queue Implementation](#physical-meaning-of-stextvalue-in-block-queue-implementation)
    - [3.2 Types of Semaphores: Binary vs. Counting](#32-types-of-semaphores-binary-vs-counting)
    - [3.3 Strong vs. Weak Semaphores \& Process Queue Trace](#33-strong-vs-weak-semaphores--process-queue-trace)
      - [Strong vs. Weak Definitions](#strong-vs-weak-definitions)
      - [Step-by-Step Execution Trace of a Strong Semaphore](#step-by-step-execution-trace-of-a-strong-semaphore)
    - [3.4 Mutex Lock vs. Semaphore](#34-mutex-lock-vs-semaphore)
    - [3.5 Execution Trace: Incorrect Operation Order \& Deadlock](#35-execution-trace-incorrect-operation-order--deadlock)
      - [Example: Inverted Wait Locks in Bounded Buffer](#example-inverted-wait-locks-in-bounded-buffer)
        - [Correct Sequence](#correct-sequence)
        - [Erroneous Sequence (Inverted Waits)](#erroneous-sequence-inverted-waits)
      - [Step-by-Step Deadlock Trace (Buffer Full: `empty = 0`, `full = N`)](#step-by-step-deadlock-trace-buffer-full-empty--0-full--n)
    - [3.6 Exam-Ready Brief \& Common Mistakes](#36-exam-ready-brief--common-mistakes)
      - [Concise Summary](#concise-summary-1)
      - [Common Student Mistakes](#common-student-mistakes-2)
  - [4. Monitors](#4-monitors)
    - [4.1 Definition \& Structural Architecture](#41-definition--structural-architecture)
      - [Key Structural Characteristics](#key-structural-characteristics)
      - [Monitor Syntax Abstraction](#monitor-syntax-abstraction)
    - [4.2 Condition Variables \& Operations](#42-condition-variables--operations)
      - [Signal Semantics: Hoare vs. Mesa Architecture](#signal-semantics-hoare-vs-mesa-architecture)
    - [4.3 Bounded-Buffer Producer/Consumer Solution Using a Monitor](#43-bounded-buffer-producerconsumer-solution-using-a-monitor)
        - [External Producer and Consumer Threads](#external-producer-and-consumer-threads)
    - [4.4 Condition Variables vs. Semaphores](#44-condition-variables-vs-semaphores)
    - [4.5 Exam-Ready Brief \& Common Mistakes](#45-exam-ready-brief--common-mistakes)
      - [Concise Summary](#concise-summary-2)
      - [Common Student Mistakes](#common-student-mistakes-3)
  - [5. Message Passing](#5-message-passing)
    - [5.1 Direct vs. Indirect Addressing](#51-direct-vs-indirect-addressing)
      - [Addressing Schemes](#addressing-schemes)
        - [Indirect Mailbox Configurations](#indirect-mailbox-configurations)
    - [5.2 Synchronization Primitives: Blocking vs. Non-Blocking](#52-synchronization-primitives-blocking-vs-non-blocking)
    - [5.3 General Message Format (Header \& Body)](#53-general-message-format-header--body)
    - [5.4 Message Buffering Schemes](#54-message-buffering-schemes)
    - [5.5 Mutual Exclusion Using Message Passing](#55-mutual-exclusion-using-message-passing)
    - [5.6 Bounded-Buffer Producer/Consumer Solution Using Message Passing](#56-bounded-buffer-producerconsumer-solution-using-message-passing)
    - [5.7 Exam-Ready Brief \& Common Mistakes](#57-exam-ready-brief--common-mistakes)
      - [Concise Summary](#concise-summary-3)
      - [Common Student Mistakes](#common-student-mistakes-4)
  - [6. Classical IPC Problems](#6-classical-ipc-problems)
    - [6.1 Bounded-Buffer (Producer/Consumer) Problem](#61-bounded-buffer-producerconsumer-problem)
      - [Constraints to Enforce](#constraints-to-enforce)
      - [Complete Semaphore Solution](#complete-semaphore-solution)
        - [Variable Initializations](#variable-initializations)
        - [Producer and Consumer Implementation](#producer-and-consumer-implementation)
    - [6.2 Readers-Writers Problem](#62-readers-writers-problem)
      - [Constraints](#constraints)
      - [Policy: First Readers-Writers Problem (Reader Preference)](#policy-first-readers-writers-problem-reader-preference)
        - [Variable Initializations](#variable-initializations-1)
        - [Pseudocode Implementation](#pseudocode-implementation)
    - [6.3 Additional topics covered in the supplied PPT/PDF: Classical IPC Problems](#63-additional-topics-covered-in-the-supplied-pptpdf-classical-ipc-problems)
      - [The Sleeping Barber Problem](#the-sleeping-barber-problem)
        - [Scenario Description](#scenario-description)
        - [Complete Semaphore Pseudocode](#complete-semaphore-pseudocode)
    - [6.4 Exam-Ready Brief \& Common Mistakes](#64-exam-ready-brief--common-mistakes)
      - [Concise Summary](#concise-summary-4)
      - [Common Student Mistakes](#common-student-mistakes-5)
  - [7. Comprehensive Tool Comparison Table](#7-comprehensive-tool-comparison-table)
  - [8. Formula \& Pseudocode Quick Recap](#8-formula--pseudocode-quick-recap)
    - [1. Semaphore Queue State Equations](#1-semaphore-queue-state-equations)
    - [2. Bounded-Buffer Semaphore Variables](#2-bounded-buffer-semaphore-variables)
  - [9. Representative Exam Question Patterns \& Model Answers](#9-representative-exam-question-patterns--model-answers)
    - [Pattern 1: Conceptual Semaphore Trace \& Process Queue Transition (5/10 Marks)](#pattern-1-conceptual-semaphore-trace--process-queue-transition-510-marks)
    - [Pattern 2: Explain Producer-Consumer Problem Using Semaphores (10 Marks)](#pattern-2-explain-producer-consumer-problem-using-semaphores-10-marks)
    - [Pattern 3: Differentiate Between Monitors and Semaphores (5 Marks)](#pattern-3-differentiate-between-monitors-and-semaphores-5-marks)
  - [10. Quick Revision Checklist](#10-quick-revision-checklist)

---

## 1. Principles of Concurrency & Critical Section Problem

### 1.1 Fundamentals of Concurrent Execution
Concurrency refers to the ability of an operating system to execute multiple processes or threads in overlapping time intervals. *(Reference: Stallings Ch. 5; UNIT3-Process concurrency.pptx Slide 2-4)*

- **Uniprocessor Systems (Interleaving):** On a single-processor core, true simultaneous physical execution is impossible. Concurrency is achieved via **interleaving**, where the OS CPU scheduler rapidly switches execution among processes using time-slicing and interrupts.
- **Multiprocessor / Multicore Systems (Overlapping):** On multi-core architectures, processes achieve true physical **overlapping (parallel execution)**, running concurrently across distinct physical CPU cores.

Process concurrency arises in three primary execution contexts:
1. **Multiple Concurrent Applications:** Multiprogramming user processes competing for system resources.
2. **Structured Applications:** A single application structured as multiple cooperating parallel tasks or threads.
3. **OS Structure:** The operating system kernel itself implemented as a set of concurrent processes or threads handling system calls and interrupts.

---

### 1.2 Shared Resources & Race Conditions

#### Conceptual Explanation
When concurrent processes access and manipulate shared data structures (such as global memory variables, files, or database records) without synchronization, the final outcome depends unpredictably on the exact sequence and timing of instruction execution. This unsafe scenario is called a **Race Condition**. *(Reference: Silberschatz Ch. 5; Tanenbaum Ch. 2)*

---

#### Concrete Example 1: The Shared Counter Race Condition
Consider a shared global variable `count` initialized to `5`. Two concurrent processes execute the following operations:
- **Process P1:** `count = count + 1;`
- **Process P2:** `count = count - 1;`

At the machine assembly level, these high-level statements are compiled into three distinct hardware instructions:

```assembly
; Process P1 (Increment)
LOAD  R1, [count]   ; Step 1: Read count into register R1
ADD   R1, #1        ; Step 2: Increment R1
STORE [count], R1   ; Step 3: Write R1 back to memory

; Process P2 (Decrement)
LOAD  R2, [count]   ; Step 1: Read count into register R2
SUB   R2, #1        ; Step 2: Decrement R2
STORE [count], R2   ; Step 3: Write R2 back to memory
```

##### Unsynchronized Execution Interleaving
If CPU preemption interrupts Process P1 midway through execution, the memory state becomes corrupted:

1. **P1** executes `LOAD R1, [count]` $\rightarrow$ `R1 = 5`
2. **P1** executes `ADD R1, #1` $\rightarrow$ `R1 = 6`
3. *(Timer Interrupt occurs; CPU context switches to P2)*
4. **P2** executes `LOAD R2, [count]` $\rightarrow$ `R2 = 5` *(P2 reads stale value 5 from memory)*
5. **P2** executes `SUB R2, #1` $\rightarrow$ `R2 = 4`
6. **P2** executes `STORE [count], R2` $\rightarrow$ Memory `count` becomes `4`
7. *(Context switch back to P1)*
8. **P1** executes `STORE [count], R1` $\rightarrow$ Memory `count` becomes `6`

**Result:** The correct final value of `count` should be `5` ($5 + 1 - 1$). However, due to the interleaved execution, `count` erroneously ends up as `6` (or `4` if P2 stored last).

---

#### Concrete Example 2: The Shared echo() Procedure Race Condition
*(Reference: UNIT3-Process concurrency.pptx Slide 5-7; OS Chap-3 Process Concurrency.pdf Page 1-2; Stallings Ch. 5)*

Consider a shared utility procedure `echo()` loaded into global main memory to accept keyboard input and display characters on screen:

```c
void echo() {
    chin = getchar();   // Get character input from keyboard
    chout = chin;       // Transfer character from chin to chout
    putchar(chout);     // Display character on screen
}
```

##### Scenario A: Uniprocessor System (Interleaving Interruption)
1. **Process P1** invokes `echo()`. The user types character `'x'`. `getchar()` returns `'x'`, storing it in global variable `chin`.
2. Before P1 can copy `chin` to `chout`, P1 is interrupted by the CPU scheduler, and **Process P2** is dispatched.
3. **P2** invokes `echo()` and runs to completion. The user types character `'y'`. `chin` becomes `'y'`, `chout` becomes `'y'`, and `'y'` is printed on the screen.
4. **P1** resumes execution from where it was interrupted. It executes `chout = chin`. Because `chin` was overwritten by P2, `chout` receives `'y'`. P1 calls `putchar(chout)`, displaying `'y'`.

**Corruption Result:** Character `'x'` typed by User 1 is lost permanently, and character `'y'` typed by User 2 is printed twice.

##### Scenario B: Multiprocessor System (Overlapping Execution)
1. **Process P1** runs on CPU Core 1 and **Process P2** runs on CPU Core 2 simultaneously. Both invoke `echo()`.
2. P1 executes `chin = getchar()` getting `'x'`. Simultaneously, P2 executes `chin = getchar()` getting `'y'`, overwriting global variable `chin` before P1 reads it into `chout`.
3. Both processes read `chout = chin` (value `'y'`) and both output `'y'`.

##### Single Access Enforcement
To prevent this corruption, the OS must enforce **mutual exclusion**: only one process at a time may enter `echo()`. If P2 attempts to call `echo()` while P1 is inside, P2 must be suspended until P1 completes and exits `echo()`.

---

### 1.3 Difficulties of Concurrency & OS Concerns
*(Reference: UNIT3-Process concurrency.pptx Slide 4)*

#### Difficulties of Concurrency
1. **Sharing Global Resources:** Concurrent access to shared variables, memory tables, or files without proper synchronization leads to data corruption.
2. **Optimal Resource Allocation:** It is difficult for the OS to allocate resources optimally while preventing deadlock (where processes wait forever for each other) or starvation.
3. **Hard-to-Locate Programming Errors:** Debugging race conditions is extremely difficult because execution interleaving is non-deterministic and non-reproducible. A program may run correctly 99% of the time and fail randomly under specific timing conditions.

#### OS Concerns and Responsibilities
To support concurrent execution safely, the OS kernel must maintain:
1. **Process Tracking:** Track all active processes using Process Control Blocks (PCBs) and execution states.
2. **Resource Allocation & Management:** Dynamically allocate and deallocate CPU time, memory, files, and I/O devices to active processes.
3. **Data and Resource Protection:** Protect memory and resources of each process against unintentional or malicious interference by other processes.
4. **Independent Execution Guarantee:** Ensure that the results produced by a process are completely independent of its relative execution speed compared to other concurrent processes.

---

### 1.4 Critical Section Framework
To prevent race conditions, access to shared memory must be strictly controlled.

- **Critical Section (CS):** A segment of code in a process that accesses shared resources (such as shared variables, memory tables, or files) that must not be accessed concurrently by more than one process.
- **Remainder Section:** The portion of code preceding or following the critical section that operates on purely local variables.

#### General Structure of a Concurrent Process
```c
do {
    /* ENTRY SECTION */
    // Request permission to enter the critical section
    
    /* CRITICAL SECTION */
    // Access and modify shared variables/resources
    
    /* EXIT SECTION */
    // Release lock and notify waiting processes
    
    /* REMAINDER SECTION */
    // Perform local non-shared computations
} while (true);
```

---

### 1.5 Three Requirements for Critical-Section Solutions
Any valid software, hardware, or OS-level solution to the critical-section problem must satisfy three mandatory criteria: *(Reference: Silberschatz Ch. 5)*

1. **Mutual Exclusion:**
   - **Definition:** If process $P_i$ is executing in its critical section, no other process $P_j$ can be executing in its critical section for the same shared resource.
   - **Intuitive Example:** Only one car can safely occupy a narrow single-lane bridge intersection at a time.

2. **Progress:**
   - **Definition:** If no process is currently executing in its critical section and some processes wish to enter, only those processes that are not executing in their remainder section can participate in deciding which process will enter next. This decision cannot be postponed indefinitely.
   - **Intuitive Example:** If the bridge is completely empty, cars waiting at the bridge must be allowed to select one car to cross without being blocked by parked cars resting in the parking lot.

3. **Bounded Waiting:**
   - **Definition:** There must exist a bound or limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted.
   - **Intuitive Example:** No single waiting car should sit at a red light forever while an endless queue of incoming emergency trucks or high-priority cars continuously passes by (**prevents starvation**).

---

### 1.6 Additional topics covered in the supplied PPT/PDF: Software Mutual Exclusion
*(Reference: UNIT3-Process concurrency.pptx Slide 9-12; OS Chap-3 Process Concurrency.pdf Page 3-5; Stallings App. A)*

Software solutions attempt to achieve mutual exclusion without hardware lock instructions or OS kernel primitives, relying solely on atomic memory loads and stores shared between processes.

#### Attempt 1: Strict Alternation Using turn Variable
Processes $P_0$ and $P_1$ share a single integer variable `turn`, initialized to `0` or `1`.

##### Pseudocode
```c
// Process P0
while (true) {
    while (turn != 0); // Busy wait (spin)
    /* CRITICAL SECTION */
    turn = 1;          // Pass turn to P1
    /* REMAINDER SECTION */
}

// Process P1
while (true) {
    while (turn != 1); // Busy wait (spin)
    /* CRITICAL SECTION */
    turn = 0;          // Pass turn to P0
    /* REMAINDER SECTION */
}
```

##### Evaluation
- **Mutual Exclusion:** **Satisfied.** If `turn == 0`, only $P_0$ can enter; if `turn == 1`, only $P_1$ can enter.
- **Progress:** **VIOLATED.** Requires strict $P_0 \rightarrow P_1 \rightarrow P_0 \rightarrow P_1$ execution. If $P_0$ finishes its CS and enters a long remainder section while $P_1$ wants to enter its CS twice in a row, $P_1$ is blocked waiting for $P_0$ to change `turn = 1`. A process in its remainder section prevents another process from entering.

---

#### Attempt 2: Flag-Only Solution
To eliminate strict alternation, processes use a shared boolean array `boolean flag[2] = {false, false};` to signal their intent to enter.

##### Pseudocode
```c
// Process P0
while (true) {
    flag[0] = true;     // State intent to enter
    while (flag[1]);   // Wait if P1 wants to enter
    /* CRITICAL SECTION */
    flag[0] = false;    // Exit CS
    /* REMAINDER SECTION */
}

// Process P1
while (true) {
    flag[1] = true;     // State intent to enter
    while (flag[0]);   // Wait if P0 wants to enter
    /* CRITICAL SECTION */
    flag[1] = false;    // Exit CS
    /* REMAINDER SECTION */
}
```

##### Evaluation
- **Mutual Exclusion:** Satisfied if execution does not interleave at line 1.
- **Progress / Deadlock:** **VIOLATED.** If $P_0$ sets `flag[0] = true` and a context switch occurs before $P_0$ checks `while(flag[1])`, $P_1$ runs and sets `flag[1] = true`. Both flags are now `true`. $P_0$ loops on `while(flag[1])` and $P_1$ loops on `while(flag[0])`. Both processes spin forever in **deadlock**.

---

#### Dekker's Algorithm
Dekker's algorithm (1965) was the first known correct software solution for 2 processes. It combines `flag[2]` (intent) and `turn` (conflict resolution priority).

##### Shared Variables
```c
boolean flag[2] = {false, false};
int turn = 0; // 0 or 1
```

##### Pseudocode
```c
// Process P0
while (true) {
    flag[0] = true;
    while (flag[1]) {
        if (turn != 0) {
            flag[0] = false;      // Defer intent while turn belongs to P1
            while (turn != 0);    // Wait until turn becomes 0
            flag[0] = true;       // Re-assert intent
        }
    }
    /* CRITICAL SECTION */
    turn = 1;           // Transfer priority to P1
    flag[0] = false;    // Release CS
    /* REMAINDER SECTION */
}

// Process P1
while (true) {
    flag[1] = true;
    while (flag[0]) {
        if (turn != 1) {
            flag[1] = false;      // Defer intent while turn belongs to P0
            while (turn != 1);    // Wait until turn becomes 1
            flag[1] = true;       // Re-assert intent
        }
    }
    /* CRITICAL SECTION */
    turn = 0;           // Transfer priority to P0
    flag[1] = false;    // Release CS
    /* REMAINDER SECTION */
}
```

##### Evaluation
- **Guarantees:** Satisfies **Mutual Exclusion**, **Progress**, and **Bounded Waiting**. If both set flags simultaneously, `turn` decides who insists and who defers.

---

#### Peterson's Algorithm
Discovered by G.L. Peterson in 1981, this algorithm provides a much simpler and more elegant 2-process solution using `flag[2]` and `turn`.

##### Shared Variables
```c
boolean flag[2] = {false, false}; // flag[i] = true means Pi is ready to enter CS
int turn;                          // Indicates whose turn it is to wait
```

##### Pseudocode (Process $P_i$, where $j = 1 - i$)
```c
do {
    flag[i] = true;                 // 1. Declare intent to enter CS
    turn = j;                       // 2. Politely give turn to opponent
    while (flag[j] && turn == j);   // 3. Busy wait if opponent is ready AND it is opponent's turn
    
    /* CRITICAL SECTION */
    
    flag[i] = false;                // 4. Clear intent upon exit
    
    /* REMAINDER SECTION */
} while (true);
```

##### Verification of Criteria
1. **Mutual Exclusion:** $P_0$ enters CS only if `flag[1] == false` OR `turn == 0`. $P_1$ enters CS only if `flag[0] == false` OR `turn == 1`. If both try to enter simultaneously, both set `flag[0]=true` and `flag[1]=true`. However, `turn` can hold only one value ($0$ or $1$). Whichever process assigned `turn` last will overwrite `turn` and be forced to wait in the `while` loop, allowing the other process to enter CS.
2. **Progress:** A process $P_i$ exited from CS sets `flag[i] = false`, immediately unblocking $P_j$ waiting at `while(flag[j] && turn == j)`.
3. **Bounded Waiting:** $P_i$ gives `turn = j` before entering. $P_j$ is guaranteed to enter CS after at most one entry by $P_i$.

##### Modern Limitation
Peterson's algorithm assumes that machine instructions are executed strictly in program order. Modern out-of-order processors and optimizing compilers reorder memory reads and writes (`flag[i] = true` vs `turn = j`), breaking Peterson's algorithm unless explicit memory barriers (`mb()`) are inserted.

---

### 1.7 Exam-Ready Brief & Common Mistakes

#### Concise Exam Definition
> **Critical Section:** A block of code accessing shared resources that must be executed mutually exclusively. A valid solution must satisfy **Mutual Exclusion** (only 1 process in CS), **Progress** (no process outside CS blocks others), and **Bounded Waiting** (no process starves indefinitely).

#### Common Student Mistakes
- **Confusing Progress and Bounded Waiting:** Progress prevents deadlock when CS is empty; Bounded Waiting prevents starvation when processes repeatedly enter CS.
- **Assuming Peterson's Works Everywhere:** Forgetting to mention that Peterson's algorithm fails on modern out-of-order CPUs without memory barriers.

---

## 2. Mutual Exclusion: Hardware Approaches

### 2.1 Interrupt Disabling
On a uniprocessor system, concurrent processes cannot physically overlap; execution interleaving occurs only when a hardware interrupt (such as a timer tick) triggers a context switch. Disabling interrupts prevents the CPU scheduler from preempting the currently executing process. *(Reference: Stallings Ch. 5)*

```c
while (true) {
    /* DISABLE INTERRUPTS */;
    
    /* CRITICAL SECTION */
    
    /* ENABLE INTERRUPTS */;
    
    /* REMAINDER SECTION */
}
```

#### Evaluation & Limitations
- **Advantages:** Simple and effective for tiny uniprocessor OS kernels.
- **Multiprocessor Ineffectiveness:** Disabling interrupts on CPU Core 1 does not disable interrupts or stop execution on CPU Core 2. Processes on Core 2 can still access shared memory concurrently.
- **Kernel vs. User Restriction:** User-level applications must **never** be permitted to disable interrupts; a user process could disable interrupts and enter an infinite loop, freezing the entire system.

---

### 2.2 Atomic Hardware Instructions
Modern computer architectures provide special hardware instructions that execute **atomically** (as an indivisible, uninterrupted hardware bus transaction).

---

#### 2.2.1 TestAndSet Instruction

##### C Definition (Executed Atomically by Hardware)
```c
boolean TestAndSet(boolean *target) {
    boolean rv = *target; // Read original value
    *target = true;       // Set memory location to true
    return rv;            // Return original value
}
```

##### Mutual Exclusion Implementation
Shared variable `boolean lock = false;`

```c
do {
    while (TestAndSet(&lock)); // Spin (busy wait) while lock is true
    
    /* CRITICAL SECTION */
    
    lock = false;              // Release lock
    
    /* REMAINDER SECTION */
} while (true);
```

##### Mechanism
1. If `lock == false`, `TestAndSet(&lock)` returns `false` and sets `lock = true`. The `while` loop terminates, and the process enters CS.
2. If another process executes `TestAndSet(&lock)` while `lock == true`, it receives `true` and spins in the `while` loop until `lock` becomes `false`.

---

#### 2.2.2 CompareAndSwap / Swap Instruction

##### CompareAndSwap C Definition
```c
int CompareAndSwap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected) {
        *value = new_value;
    }
    return temp; // Returns original value
}
```

##### Mutual Exclusion Implementation Using CompareAndSwap
Shared variable `int lock = 0;`

```c
do {
    while (CompareAndSwap(&lock, 0, 1) != 0); // Spin while lock is 1
    
    /* CRITICAL SECTION */
    
    lock = 0; // Release lock
    
    /* REMAINDER SECTION */
} while (true);
```

##### Swap Instruction C Definition
```c
void Swap(boolean *a, boolean *b) {
    boolean temp = *a;
    *a = *b;
    *b = temp;
}
```

##### Mutual Exclusion Implementation Using Swap
Shared variable `boolean lock = false;`

```c
// Each process Pi maintains a local boolean variable key
do {
    key = true;
    while (key == true) {
        Swap(&lock, &key);
    }
    
    /* CRITICAL SECTION */
    
    lock = false;
    
    /* REMAINDER SECTION */
} while (true);
```

---

### 2.3 Comparison Table of Hardware Approaches

| Criteria | Interrupt Disabling | TestAndSet Instruction | CompareAndSwap / Swap |
| :--- | :--- | :--- | :--- |
| **Hardware Requirement** | CPU Interrupt Mask Register | Atomic `TestAndSet` Bus Lock | Atomic `CompareAndSwap` / `XCHG` |
| **Multiprocessor Support** | **No** (Uniprocessor only) | **Yes** (Bus-level lock) | **Yes** (Bus-level lock) |
| **Execution Mode** | Kernel Mode Only | User and Kernel Mode | User and Kernel Mode |
| **Waiting Mechanism** | No waiting (Preemption blocked) | **Busy Waiting (Spinlock)** | **Busy Waiting (Spinlock)** |
| **Starvation Risk** | No (Run to completion) | **Possible** (Unbounded spin) | **Possible** (Unbounded spin) |
| **CPU Efficiency** | High on uniprocessor | Low (Wastes CPU cycles spinning) | Low (Wastes CPU cycles spinning) |

---

### 2.4 Exam-Ready Brief & Common Mistakes

#### Concise Summary
> Hardware instructions like `TestAndSet` and `CompareAndSwap` guarantee atomic read-modify-write memory operations across multiprocessor cores. They provide simple spinlocks but suffer from **busy waiting** (wasting CPU cycles) and do not guarantee **bounded waiting** unless paired with a waiting queue.

#### Common Student Mistakes
- **Claiming Interrupt Disabling Works on Multicores:** Interrupt disabling only stops local CPU interrupts; other cores continue executing concurrently.
- **Forgetting Busy Waiting Cost:** Spinlocks consume 100% CPU on the waiting thread while looping.

---

## 3. Semaphores

### 3.1 Definition & Atomic Operations
A **Semaphore** $S$ is an OS integer variable that, apart from initialization, is accessed only through two standard atomic primitives: `wait()` (also known as $P()$, `semWait()`, or `down()`) and `signal()` (also known as $V()$, `semSignal()`, or `up()`). *(Reference: Silberschatz Ch. 5; Stallings Ch. 5)*

#### Standard Classic Definitions (Dijkstra)
```c
void wait(Semaphore S) {
    while (S <= 0); // Busy wait
    S--;
}

void signal(Semaphore S) {
    S++;
}
```

---

#### Non-Busy Waiting (Block-Queue) Kernel Implementation
To eliminate busy waiting, modern OS kernels represent a semaphore as a C structure containing an integer value and a pointer list of PCB structures:

```c
typedef struct {
    int value;
    struct PCB *list; // Queue of blocked processes
} Semaphore;

void wait(Semaphore *S) {
    S->value--;
    if (S->value < 0) {
        // Add currently running process to S->list
        // Block the process (state = WAITING)
        block(); 
    }
}

void signal(Semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        // Remove a process P from S->list
        // Wakeup process P (state = READY, move to Ready Queue)
        wakeup(P);
    }
}
```

##### Physical Meaning of $S.\text{value}$ in Block-Queue Implementation
- **$S.\text{value} \ge 0$:** Represents the number of available resource permits.
- **$S.\text{value} < 0$:** The absolute magnitude $|S.\text{value}|$ represents the exact number of processes currently blocked and waiting in $S.\text{list}$.

---

### 3.2 Types of Semaphores: Binary vs. Counting

| Feature / Type | Binary Semaphore | Counting Semaphore |
| :--- | :--- | :--- |
| **Value Range** | Restricted to **0 and 1**. | Can range over any integer value ($-\infty$ to $+\infty$). |
| **Primary Use Case** | Mutual exclusion (locking a single resource). | Resource allocation (managing $N$ identical resources). |
| **Initialization** | Initialized to `1` (unlocked). | Initialized to `N` (total available resource units). |
| **Ownership Property** | Any process can signal it, but typically used like a lock. | Signals increment resource count; waits decrement count. |

---

### 3.3 Strong vs. Weak Semaphores & Process Queue Trace
*(Reference: UNIT3-Process concurrency.pptx Slide 18; OS Chap-3 Process Concurrency.pdf Page 39; Stallings Ch. 5)*

#### Strong vs. Weak Definitions
When multiple processes are blocked on a semaphore's waiting queue, the order in which they are removed by `signal()` is critical:

- **Strong Semaphore:** Uses a **First-In-First-Out (FIFO)** queue. The process that has been blocked the longest is awakened first. **Guarantees freedom from starvation.**
- **Weak Semaphore:** Does not specify the order of process removal (e.g., random or priority-based). **Susceptible to starvation / indefinite postponement.**

---

#### Step-by-Step Execution Trace of a Strong Semaphore
*(Reference: Stallings Fig 5.5 / UNIT3-Process concurrency.pptx Slide 18)*

Consider processes $A, B, C$ that require results produced by process $D$. They synchronize using a strong counting semaphore `s` initialized to `1` (indicating one result from $D$ is available).

```
Initial State: s.count = 1; Ready Queue = [B, C, D]; Blocked Queue = []; Running = A
```

| Step | Active Process | Action Executed | Semaphore Value `s.count` | Blocked Queue | Ready Queue | Notes / State Transition |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **A** | Executes `semWait(s)` | `0` | `[]` | `[B, C, D]` | $s \ge 0$: $A$ consumes permit and continues execution; then $A$ rejoins Ready Queue. |
| **2** | **B** | Executes `semWait(s)` | `-1` | `[B]` | `[C, D, A]` | $s < 0$: Process $B$ is blocked and added to FIFO Blocked Queue. CPU switches to $D$. |
| **3** | **D** | Computes result | `-1` | `[B]` | `[C, A]` | $D$ runs and produces a result. |
| **4** | **D** | Executes `semSignal(s)` | `0` | `[]` | `[C, A, B]` | $s \le 0$: $B$ (longest blocked) is removed from FIFO Blocked Queue and moved to Ready Queue. $D$ rejoins Ready Queue. |
| **5** | **C** | Executes `semWait(s)` | `-1` | `[C]` | `[A, B, D]` | $s < 0$: $C$ is blocked and added to Blocked Queue. $A$ runs. |
| **6** | **A, B** | $A$ & $B$ execute `semWait(s)` | `-3` | `[C, A, B]` | `[D]` | $A$ and $B$ both issue `semWait(s)` and block. Blocked Queue = $[C, A, B]$. $D$ runs. |
| **7** | **D** | Executes `semSignal(s)` | `-2` | `[A, B]` | `[C]` | $s \le 0$: $C$ (head of FIFO queue) is unblocked and moved to Ready Queue. |

---

### 3.4 Mutex Lock vs. Semaphore

| Feature | Mutex Lock | Binary / Counting Semaphore |
| :--- | :--- | :--- |
| **Ownership** | **Strict Ownership:** The process that locks the mutex MUST be the one to unlock it. | **No Ownership:** Any process can execute `signal()` to wake up a process waiting on `wait()`. |
| **Primary Design** | Mutual Exclusion locking for a critical section. | Signaling / Coordination between processes. |
| **Recursive Locking** | Can support re-entrant / recursive locking. | Does not support re-entrant locking natively. |

---

### 3.5 Execution Trace: Incorrect Operation Order & Deadlock
*(Reference: Silberschatz Ch. 5; UNIT3-Process concurrency.pptx Slide 22)*

Semaphores are powerful, but subtle bugs in operation placement or ordering cause catastrophic system deadlocks.

#### Example: Inverted Wait Locks in Bounded Buffer
Consider two semaphores:
- `Semaphore mutex = 1;` (protects buffer access)
- `Semaphore empty = 0;` (counts empty slots; buffer is currently **FULL**)

##### Correct Sequence
```c
wait(empty); // 1. First check if empty space exists
wait(mutex); // 2. Then acquire exclusive lock
```

##### Erroneous Sequence (Inverted Waits)
```c
wait(mutex); // 1. Acquire exclusive lock FIRST
wait(empty); // 2. Then check if empty space exists
```

#### Step-by-Step Deadlock Trace (Buffer Full: `empty = 0`, `full = N`)

1. **Producer** executes `wait(mutex)`. `mutex` becomes `0`. Producer acquires exclusive buffer lock.
2. **Producer** executes `wait(empty)`. Because `empty == 0` (buffer full), Producer is **blocked** and placed in `empty->list`, holding `mutex = 0`.
3. CPU context switches to **Consumer**.
4. **Consumer** attempts to remove an item and executes `wait(mutex)`.
5. Because Producer holds `mutex = 0`, Consumer is **blocked** on `mutex->list`.

**Deadlock Result:** Producer is waiting for Consumer to execute `signal(empty)`, but Consumer is blocked waiting for Producer to execute `signal(mutex)`. Both processes are blocked forever.

---

### 3.6 Exam-Ready Brief & Common Mistakes

#### Concise Summary
> Semaphores provide OS-level synchronization via atomic `wait()` (decrements/blocks if $<0$) and `signal()` (increments/awakens if $\le 0$). **Strong semaphores** use FIFO queues to prevent starvation. Inverted `wait()` order causes deadlocks.

#### Common Student Mistakes
- **Confusing Signal Condition:** In block-queue semaphores, `signal()` wakes up a process if `value <= 0` (NOT if `value < 0`).
- **Executing Signal Before Wait:** Inverting `signal(mutex)` and `wait(mutex)` violates mutual exclusion completely.

---

## 4. Monitors

### 4.1 Definition & Structural Architecture
A **Monitor** is a high-level synchronization construct provided by programming languages (such as Concurrent Pascal, Java) that encapsulates shared data variables, mutex locks, and condition variables inside a protected module. *(Reference: Silberschatz Ch. 5; Stallings Ch. 5; Tanenbaum Ch. 2)*

#### Key Structural Characteristics
1. **Shared Data Encapsulation:** Shared variables are local to the monitor and accessible only via monitor procedures.
2. **Implicit Mutual Exclusion:** Only **one process at a time** can be active inside a monitor procedure. The compiler automatically inserts implicit lock and unlock primitives at procedure entry and exit.

#### Monitor Syntax Abstraction
```pascal
monitor monitor_name {
    // Shared variable declarations
    
    public procedure P1(...) {
        // Code
    }
    
    public procedure P2(...) {
        // Code
    }
    
    init {
        // Initialization code
    }
}
```

---

### 4.2 Condition Variables & Operations
To allow processes to wait inside a monitor when condition criteria are unmet, monitors provide explicit **Condition Variables** (declared as `condition x, y;`).

Condition variables do **not** have integer values; they only maintain queues of waiting processes and support two operations:
- `x.wait()`: The calling process is suspended and placed in condition `x`'s waiting queue. The process **releases its exclusive monitor lock** so other processes can enter the monitor.
- `x.signal()`: Awakens exactly one process blocked on `x.wait()`. If no process is waiting on `x`, `x.signal()` has **no effect** (unlike semaphore `signal()`, which increments a counter).

---

#### Signal Semantics: Hoare vs. Mesa Architecture

If process $P$ executes `x.signal()` inside a monitor and wakes up a suspended process $Q$, two processes are now ready to run inside the monitor. Two architectural signal policies exist:

```
 Hoare (Signal-and-Wait):      P (signaler) yields monitor immediately -> Q runs
 Mesa  (Signal-and-Continue):  P continues until procedure exit       -> Q re-checks condition (while loop)
```

1. **Hoare Semantics (Signal-and-Wait):**
   - **Mechanism:** The signaling process $P$ is immediately suspended and yields monitor access to woken process $Q$. $Q$ executes immediately. When $Q$ exits, $P$ resumes.
   - **Condition Check:** Woken process $Q$ uses an `if` statement: `if (condition) x.wait();`.

2. **Mesa Semantics (Signal-and-Continue):**
   - **Mechanism:** The signaling process $P$ continues executing inside the monitor until it finishes its procedure. $Q$ is moved to the monitor entry queue.
   - **Condition Check:** Woken process $Q$ MUST use a `while` loop: `while (condition) x.wait();` because another process may enter the monitor before $Q$ runs and alter the state.

---

### 4.3 Bounded-Buffer Producer/Consumer Solution Using a Monitor
*(Reference: UNIT3-Process concurrency.pptx Slide 32; Stallings Fig 5.16; Tanenbaum Ch. 2)*

The monitor module `boundedbuffer` encapsulates the buffer array, pointer indices, and condition variables `notfull` and `notempty`:

```c
monitor boundedbuffer {
    char buffer[N];          // Buffer space for N items
    int nextin, nextout;     // Buffer pointer indices
    int count;               // Current item count in buffer
    condition notfull;       // Signaled when space becomes available
    condition notempty;      // Signaled when item becomes available

    public void append(char x) {
        if (count == N) {
            cwait(notfull);  // Buffer is full; suspend producer
        }
        buffer[nextin] = x;
        nextin = (nextin + 1) % N;
        count++;
        csignal(notempty);   // Resume any waiting consumer
    }

    public void take(char *x) {
        if (count == 0) {
            cwait(notempty); // Buffer is empty; suspend consumer
        }
        *x = buffer[nextout];
        nextout = (nextout + 1) % N;
        count--;
        csignal(notfull);    // Resume any waiting producer
    }

    // Monitor Initialization
    boundedbuffer() {
        nextin = 0;
        nextout = 0;
        count = 0;
    }
}
```

##### External Producer and Consumer Threads
```c
void producer() {
    char x;
    while (true) {
        x = produce_item();
        boundedbuffer.append(x); // Calls monitor procedure
    }
}

void consumer() {
    char x;
    while (true) {
        boundedbuffer.take(&x);  // Calls monitor procedure
        consume_item(x);
    }
}
```

---

### 4.4 Condition Variables vs. Semaphores

| Feature | Condition Variable (Monitor) | Semaphore |
| :--- | :--- | :--- |
| **State Storage** | **Stateless:** Has no integer value or history counter. | **Stateful:** Stores an integer value / resource permit count. |
| **Signal Behavior** | `signal()` on an empty queue is **lost** (no effect). | `signal()` always increments counter value. |
| **Wait Behavior** | `wait()` **always blocks** the calling process unconditionally. | `wait()` blocks only if value $\le 0$; otherwise decrements value. |
| **Mutual Exclusion** | Provided **implicitly** by compiler / monitor wrapper. | Must be provided **explicitly** by programmer (`wait(mutex)`). |

---

### 4.5 Exam-Ready Brief & Common Mistakes

#### Concise Summary
> A **Monitor** is a language construct providing **implicit mutual exclusion** over encapsulated shared data. It uses **condition variables** (`cwait`, `csignal`) for synchronization. Unlike semaphores, condition variables are stateless: `csignal()` with no waiting processes is lost.

#### Common Student Mistakes
- **Assuming Condition Variables Store Values:** Condition variables only queue processes; they do NOT keep a count.
- **Forgetting Mesa While Loop:** Using `if` instead of `while` for `cwait()` in Mesa monitors causes race conditions when woken threads resume.

---

## 5. Message Passing

### 5.1 Direct vs. Indirect Addressing
Message passing achieves interprocess communication and synchronization without shared memory using two basic primitives: `send(destination, message)` and `receive(source, message)`. *(Reference: Silberschatz Ch. 3/5; Stallings Ch. 5)*

#### Addressing Schemes

1. **Direct Addressing:**
   - **Symmetric:** Sender explicitly names the receiver, and receiver explicitly names the sender.
     - `send(P, message)`: Send a message to process $P$.
     - `receive(Q, message)`: Receive a message from process $Q$.
   - **Asymmetric:** Sender names the destination process, but receiver uses a wildcard variable to accept messages from any process.
     - `receive(id, message)`: Receive from any sending process; `id` is populated with sender's identity.

2. **Indirect Addressing:**
   - Messages are sent to and received from shared intermediate queue structures called **Mailboxes** or **Ports**.
   - `send(mailbox_A, message)`: Send message to mailbox $A$.
   - `receive(mailbox_A, message)`: Receive message from mailbox $A$.

##### Indirect Mailbox Configurations
- **One-to-One:** Private communication channel between 2 processes.
- **Many-to-One (Port):** Multiple client processes send messages to a single server process port.
- **One-to-Many:** Single sender broadcasting to multiple receivers.
- **Many-to-Many:** Multiple senders and receivers sharing a common mailbox pool.

---

### 5.2 Synchronization Primitives: Blocking vs. Non-Blocking

The execution behavior of `send()` and `receive()` can be synchronous (blocking) or asynchronous (non-blocking):

| Combination | Send Behavior | Receive Behavior | System Property / Outcome |
| :--- | :--- | :--- | :--- |
| **Blocking Send + Blocking Receive** | Sender blocks until message is received. | Receiver blocks until a message arrives. | **Rendezvous:** Tight deterministic handoff between processes. |
| **Non-blocking Send + Blocking Receive** | Sender resumes execution immediately after sending. | Receiver blocks until a message arrives. | **Most Common Model:** Asynchronous production with synchronous consumption. |
| **Non-blocking Send + Non-blocking Receive** | Sender resumes execution immediately. | Receiver retrieves message or error code and continues. | **Fully Asynchronous:** Requires polling or callback handlers. |

---

### 5.3 General Message Format (Header & Body)
*(Reference: UNIT3-Process concurrency.pptx Slide 35; Stallings Fig 5.19; OS_UNIT_3_AND_4.docx Page 69)*

A message is formatted into a **Header** (metadata managed by OS) and a **Body** (payload):

```
+-------------------------------------------------------------+
|                        MESSAGE HEADER                       |
+-------------------------------------------------------------+
|  Message Type     | Categorizes data, control, or sync msg |
|  Destination ID   | Process ID, Mailbox ID, or Port address |
|  Source ID        | Sender Process ID (for reply routing)   |
|  Message Length   | Byte size of payload / message          |
|  Control Info     | Sequence number, priority, pointers     |
+-------------------------------------------------------------+
|                        MESSAGE BODY                         |
+-------------------------------------------------------------+
|  Message Contents | Actual data payload / file references   |
+-------------------------------------------------------------+
```

1. **Header Fields:**
   - **Message Type:** Distinguishes normal data messages from synchronization tokens or error reports.
   - **Destination ID & Source ID:** Addresses identifying sender and recipient.
   - **Message Length:** Indicates fixed or variable message length.
   - **Control Information:** Contains sequence numbers (for duplicate detection), priority flags, or link pointers.
2. **Body:** Contains actual data payload (text, structure, or array).

---

### 5.4 Message Buffering Schemes
Messages in transit are stored in OS kernel queues:

1. **Zero Capacity (No Buffering):** Queue length is `0`. Sender must block until receiver accepts message (**Rendezvous**).
2. **Bounded Capacity (Finite Queue):** Queue holds at most $N$ messages. Sender blocks only if queue is full ($N$ messages pending).
3. **Unbounded Capacity (Infinite Queue):** Queue length is infinite. Sender never blocks.

---

### 5.5 Mutual Exclusion Using Message Passing
Message passing can enforce mutual exclusion without shared memory by using a shared mailbox containing a single "token" message:

```c
// Shared Mailbox: box (initialized with 1 token message: send(box, "token"))

void Process_Pi() {
    message msg;
    while (true) {
        receive(box, msg); // Acquire token (blocks if token taken)
        
        /* CRITICAL SECTION */
        
        send(box, msg);    // Release token back to mailbox
        
        /* REMAINDER SECTION */
    }
}
```

---

### 5.6 Bounded-Buffer Producer/Consumer Solution Using Message Passing
*(Reference: UNIT3-Process concurrency.pptx Slide 36; Stallings Fig 5.21)*

Using two mailboxes: `mayproduce` (capacity $N$ null tokens) and `mayconsume` (initially empty):

```c
const int capacity = N; // Buffer size
const int null = 0;     // Empty token message

void producer() {
    message pmsg;
    while (true) {
        receive(mayproduce, pmsg); // Get an empty token (blocks if buffer full)
        pmsg = produce_item();
        send(mayconsume, pmsg);    // Send produced item to consumer
    }
}

void consumer() {
    message cmsg;
    while (true) {
        receive(mayconsume, cmsg); // Get filled item (blocks if buffer empty)
        consume_item(cmsg);
        send(mayproduce, null);    // Return empty token to producer
    }
}

void main() {
    create_mailbox(mayproduce);
    create_mailbox(mayconsume);
    
    // Initialize mayproduce with N null token messages
    for (int i = 1; i <= capacity; i++) {
        send(mayproduce, null);
    }
    
    parbegin(producer, consumer);
}
```

---

### 5.7 Exam-Ready Brief & Common Mistakes

#### Concise Summary
> **Message Passing** provides IPC via `send` and `receive`. It supports **direct** or **indirect (mailbox)** addressing and **blocking** or **non-blocking** semantics. A blocking `send` + blocking `receive` creates a **Rendezvous**.

#### Common Student Mistakes
- **Forgetting Initial Tokens in Mailbox Solution:** Omitting `send(box, msg)` during initialization causes all processes to block on first `receive()`.

---

## 6. Classical IPC Problems

### 6.1 Bounded-Buffer (Producer/Consumer) Problem
*(Reference: Silberschatz Ch. 5; Stallings Ch. 5; Tanenbaum Ch. 2)*

Producers generate data items and place them into a fixed-size shared buffer of $N$ slots. Consumers remove items from the buffer.

#### Constraints to Enforce
1. Producer must not insert items into a **full buffer**.
2. Consumer must not remove items from an **empty buffer**.
3. Mutual exclusion must be maintained during buffer pointer updates.

#### Complete Semaphore Solution

##### Variable Initializations
```c
#define N 5                 // Buffer size
typedef int item;
item buffer[N];
int in = 0;                  // Producer insertion index
int out = 0;                 // Consumer removal index

Semaphore mutex = 1;         // Protects buffer insertion/deletion
Semaphore empty = N;         // Counts empty buffer slots
Semaphore full = 0;          // Counts filled buffer slots
```

##### Producer and Consumer Implementation
```c
void producer(void) {
    item item_produced;
    while (true) {
        item_produced = produce_item();
        
        wait(empty);        // Decrement empty slots (block if buffer full)
        wait(mutex);        // Lock buffer access
        
        buffer[in] = item_produced;
        in = (in + 1) % N;
        
        signal(mutex);      // Unlock buffer access
        signal(full);       // Increment full slots (wake up consumer)
    }
}

void consumer(void) {
    item item_consumed;
    while (true) {
        wait(full);         // Decrement full slots (block if buffer empty)
        wait(mutex);        // Lock buffer access
        
        item_consumed = buffer[out];
        out = (out + 1) % N;
        
        signal(mutex);      // Unlock buffer access
        signal(empty);      // Increment empty slots (wake up producer)
        
        consume_item(item_consumed);
    }
}
```

---

### 6.2 Readers-Writers Problem
*(Reference: Silberschatz Ch. 5; Stallings Ch. 5)*

A shared database is accessed by multiple concurrent processes. **Readers** only read data; **Writers** modify data.

#### Constraints
1. Multiple readers can read simultaneously.
2. Only one writer can write at a time.
3. If a writer is writing, no reader can read.

#### Policy: First Readers-Writers Problem (Reader Preference)
Subsequent readers are granted immediate access if at least one reader is currently reading, even if a writer is waiting. **Writers may suffer starvation.**

##### Variable Initializations
```c
int readcount = 0;           // Number of active readers
Semaphore mutex = 1;         // Protects readcount update
Semaphore rw_mutex = 1;      // Controls database access for writers
```

##### Pseudocode Implementation
```c
void reader(void) {
    while (true) {
        wait(mutex);         // Lock readcount
        readcount++;
        if (readcount == 1) {
            wait(rw_mutex);  // First reader locks database from writers
        }
        signal(mutex);       // Unlock readcount
        
        /* READING IS PERFORMED */
        read_database();
        
        wait(mutex);         // Lock readcount
        readcount--;
        if (readcount == 0) {
            signal(rw_mutex);// Last reader unlocks database for writers
        }
        signal(mutex);       // Unlock readcount
        
        use_data_read();
    }
}

void writer(void) {
    while (true) {
        prepare_data();
        
        wait(rw_mutex);      // Lock database exclusively
        
        /* WRITING IS PERFORMED */
        write_database();
        
        signal(rw_mutex);    // Unlock database
    }
}
```

---

### 6.3 Additional topics covered in the supplied PPT/PDF: Classical IPC Problems
*(Reference: UNIT3-Process concurrency.pptx Slide 37-40; OS Chap-3 Process Concurrency.pdf Page 40-41; Tanenbaum Ch. 2)*

#### The Sleeping Barber Problem

##### Scenario Description
A barbershop consists of a waiting room with $N$ chairs and a barber room with 1 barber chair.
- If there are no customers, the barber sits in the barber chair and **goes to sleep**.
- When a customer arrives and finds the barber sleeping, the customer **wakes up the barber**.
- If a customer arrives while the barber is cutting hair:
  - If empty chairs exist in the waiting room ($numberOfFreeWRSeats > 0$), the customer sits in a chair.
  - If all $N$ chairs are occupied, the customer **leaves the shop without a haircut**.

##### Complete Semaphore Pseudocode
```c
#define N 5                       // Number of chairs in waiting room

Semaphore barberReady = 0;        // 1 if barber is ready to cut hair
Semaphore accessWRSeats = 1;      // Mutex protecting free seat count
Semaphore custReady = 0;          // Counts waiting customers ready for service
int numberOfFreeWRSeats = N;      // Free chairs in waiting room

void Barber() {
    while (true) {
        wait(custReady);          // Sleep if no customers; wake up when customer signals
        wait(accessWRSeats);      // Acquire lock on waiting room seats
        numberOfFreeWRSeats += 1; // Free one waiting chair
        signal(barberReady);      // Signal customer that barber is ready
        signal(accessWRSeats);    // Release seat count lock
        
        cut_hair();               // Cut hair (outside critical section)
    }
}

void Customer() {
    while (true) {
        wait(accessWRSeats);      // Acquire lock on waiting seats
        if (numberOfFreeWRSeats > 0) {
            numberOfFreeWRSeats -= 1; // Occupy one waiting chair
            signal(custReady);        // Wake up barber if sleeping
            signal(accessWRSeats);    // Release seat lock
            wait(barberReady);        // Wait until barber is ready in main chair
            
            get_haircut();            // Get haircut
        } else {
            signal(accessWRSeats);    // Shop full; release lock and leave
        }
    }
}
```

---

### 6.4 Exam-Ready Brief & Common Mistakes

#### Concise Summary
> - **Producer/Consumer:** Uses `empty` ($N$), `full` ($0$), and `mutex` ($1$). Always execute `wait(empty)` before `wait(mutex)`.
> - **Readers/Writers:** First reader locks `rw_mutex`; last reader unlocks `rw_mutex`. Readers can starve writers.
> - **Sleeping Barber:** Uses `custReady`, `barberReady`, and `accessWRSeats` mutex to manage waiting room capacity $N$.

#### Common Student Mistakes
- **Executing Mutex First in Bounded Buffer:** Causes immediate deadlock when buffer is full/empty.
- **Claiming First Readers-Writers Prevents Starvation:** Reader preference explicitly causes **writer starvation** if a continuous stream of readers arrives.

---

## 7. Comprehensive Tool Comparison Table

| Feature / Criteria | Hardware Instructions (TestAndSet) | Semaphores | Monitors | Message Passing |
| :--- | :--- | :--- | :--- | :--- |
| **Abstraction Level** | Low (Hardware level) | OS Primitive | High-Level Language Construct | OS / Network Primitive |
| **Memory Model** | Shared Memory | Shared Memory | Shared Memory | Shared or Distributed Memory |
| **Busy Waiting** | **Yes** (Spinlock) | **No** (Block-Queue) | **No** (Block-Queue) | **No** (Block-Queue) |
| **Mutual Exclusion** | Explicit (`while(TestAndSet)`) | Explicit (`wait(mutex)`) | **Implicit** (Compiler enforced) | Explicit (Token message) |
| **Data Synchronization** | None | Counter Primitives | Condition Variables | `send()` / `receive()` |
| **Starvation Risk** | High | Low (Strong FIFO) | Low | Low |
| **Distributed Systems**| No | No | No | **Yes** |

---

## 8. Formula & Pseudocode Quick Recap

### 1. Semaphore Queue State Equations
Given a semaphore $S$ with block-queue implementation:
$$\text{If } S.\text{value} \ge 0 \implies \text{Available Resource Permits} = S.\text{value}$$
$$\text{If } S.\text{value} < 0 \implies \text{Blocked Processes Count} = |S.\text{value}|$$

### 2. Bounded-Buffer Semaphore Variables
```c
Semaphore mutex = 1; // Binary semaphore for CS
Semaphore empty = N; // Counting semaphore for empty slots
Semaphore full  = 0; // Counting semaphore for full slots
```
$$\text{Invariant: } \text{empty} + \text{full} = N$$

---

## 9. Representative Exam Question Patterns & Model Answers

### Pattern 1: Conceptual Semaphore Trace & Process Queue Transition (5/10 Marks)
*(Based on Stallings / PPT Semaphore Mechanism)*

**Question:** Consider a strong counting semaphore $S$ initialized to `1`. Processes $P_1, P_2, P_3, P_4$ execute operations in the following order: $P_1$ calls `wait(S)`, $P_2$ calls `wait(S)`, $P_3$ calls `wait(S)`, $P_1$ calls `signal(S)`. Trace the value of $S$, the contents of the blocked queue, and state transitions.

**Model Answer:**
1. **Initial State:** $S = 1$, Blocked Queue = `[]`, Running = $P_1$.
2. **$P_1$ executes `wait(S)`:** $S$ becomes $1 - 1 = 0$. $S \ge 0$, so $P_1$ continues execution.
3. **$P_2$ executes `wait(S)`:** $S$ becomes $0 - 1 = -1$. $S < 0$, so $P_2$ is **blocked** and placed in FIFO Blocked Queue = `[P2]`.
4. **$P_3$ executes `wait(S)`:** $S$ becomes $-1 - 1 = -2$. $S < 0$, so $P_3$ is **blocked** and placed in FIFO Blocked Queue = `[P2, P3]`.
5. **$P_1$ executes `signal(S)`:** $S$ becomes $-2 + 1 = -1$. $S \le 0$, so the process at the head of the FIFO queue ($P_2$) is removed from Blocked Queue and moved to Ready Queue. Blocked Queue becomes `[P3]`.

---

### Pattern 2: Explain Producer-Consumer Problem Using Semaphores (10 Marks)

**Question:** Explain the Bounded-Buffer Producer-Consumer problem. Provide a complete C/pseudocode solution using semaphores and explain how deadlock is avoided.

**Model Answer:**
- Define bounded buffer constraints ($N$ slots, full/empty checks).
- Provide initializations: `mutex = 1`, `empty = N`, `full = 0`.
- Provide complete code blocks for `producer()` and `consumer()`.
- Explain why `wait(empty)` MUST precede `wait(mutex)` in producer to avoid holding `mutex` while waiting for empty slots.

---

### Pattern 3: Differentiate Between Monitors and Semaphores (5 Marks)

**Model Answer:**
- Highlight **Implicit vs Explicit Mutual Exclusion**: Monitors enforce mutual exclusion automatically; semaphores require explicit `wait(mutex)` and `signal(mutex)`.
- Highlight **Stateless Condition Variables vs Stateful Semaphores**: Condition variable `csignal()` has no effect if no process is waiting, whereas semaphore `signal()` increments the count value.

---

## 10. Quick Revision Checklist

- [x] Can you trace `echo()` shared procedure race conditions on uniprocessor vs multiprocessor?
- [x] Do you know Peterson's algorithm code and the 3 criteria (Mutual Exclusion, Progress, Bounded Waiting)?
- [x] Can you explain Dekker's algorithm and contrast Attempt 1 (turn) vs Attempt 2 (flag)?
- [x] Can you explain TestAndSet and CompareAndSwap assembly spinlocks?
- [x] Can you distinguish Strong (FIFO) vs Weak semaphores and trace $S.\text{value}$ negative queue counts?
- [x] Do you know why `wait(empty)` MUST precede `wait(mutex)` in Producer/Consumer?
- [x] Can you write Bounded-Buffer solutions in **Semaphores**, **Monitors**, and **Message Passing**?
- [x] Can you explain Hoare (Signal-and-Wait) vs Mesa (Signal-and-Continue) monitor semantics?
- [x] Do you know the General Message Format (Header & Body fields)?
- [x] Can you write the complete Sleeping Barber semaphore code?
