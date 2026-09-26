# Operating Systems: Unit 5 — Memory Management System Study Notes

> **Course Unit:** Unit 5: Memory Management System (06 Hours)  
> **Course Outcome:** CO3 — *Simulate memory management, I/O management, and file management strategies*  
> **Primary Reference Standard:** Silberschatz, Galvin & Gagne (*Operating System Concepts*, 10th Edition) & William Stallings (*Operating Systems: Internals and Design Principles*, 9th Edition)

---

## Table of Contents
- [1. Memory Management Requirements](#1-memory-management-requirements)
  - [1.1 Relocation](#11-relocation)
  - [1.2 Protection](#12-protection)
  - [1.3 Sharing](#13-sharing)
  - [1.4 Logical Organization](#14-logical-organization)
  - [1.5 Physical Organization](#15-physical-organization)
  - [1.6 Comparison Table of Memory Management Requirements](#16-comparison-table-of-memory-management-requirements)
- [2. Contiguous Memory Allocation & Memory Partitioning](#2-contiguous-memory-allocation-memory-partitioning)
  - [2.1 Fixed Partitioning vs. Variable/Dynamic Partitioning](#21-fixed-partitioning-vs-variabledynamic-partitioning)
  - [2.2 Internal vs. External Fragmentation](#22-internal-vs-external-fragmentation)
  - [2.3 Compaction](#23-compaction)
  - [2.4 Partition Allocation Strategies](#24-partition-allocation-strategies)
  - [2.5 Fully Worked Numerical: Partition Allocation Strategies](#25-fully-worked-numerical-partition-allocation-strategies)
  - [2.6 The Buddy System](#26-the-buddy-system)
  - [2.7 Fully Worked Numerical: The Buddy System](#27-fully-worked-numerical-the-buddy-system)
- [3. Paging](#3-paging)
  - [3.1 Principles of Operation: Pages and Frames](#31-principles-of-operation-pages-and-frames)
  - [3.2 Logical-to-Physical Address Translation](#32-logical-to-physical-address-translation)
  - [3.3 Page Table Structure & Hardware Support](#33-page-table-structure-hardware-support)
  - [3.4 Translation Lookaside Buffer (TLB) & Effective Access Time](#34-translation-lookaside-buffer-tlb-effective-access-time)
  - [3.5 Protection and Sharing in Paging](#35-protection-and-sharing-in-paging)
  - [3.6 Disadvantages of Paging](#36-disadvantages-of-paging)
  - [3.7 Fully Worked Numericals: Paging & TLB Calculations](#37-fully-worked-numericals-paging-tlb-calculations)
- [4. Segmentation](#4-segmentation)
  - [4.1 Concept of Segmentation](#41-concept-of-segmentation)
  - [4.2 Segment Table & Hardware Address Mapping](#42-segment-table-hardware-address-mapping)
  - [4.3 Comprehensive Comparison: Paging vs. Segmentation](#43-comprehensive-comparison-paging-vs-segmentation)
  - [4.4 Fully Worked Numerical: Segmentation Address Translation](#44-fully-worked-numerical-segmentation-address-translation)
- [5. Virtual Memory & Demand Paging](#5-virtual-memory-demand-paging)
  - [5.1 Principles of Virtual Memory](#51-principles-of-virtual-memory)
  - [5.2 Demand Paging & Valid/Invalid Bits](#52-demand-paging-validinvalid-bits)
  - [5.3 Page Fault Handling Mechanism](#53-page-fault-handling-mechanism)
  - [5.4 Effective Access Time (EAT) in Demand Paging](#54-effective-access-time-eat-in-demand-paging)
  - [5.5 Fully Worked Numerical: Demand Paging Effective Access Time](#55-fully-worked-numerical-demand-paging-effective-access-time)
- [6. Page Replacement Algorithms](#6-page-replacement-algorithms)
  - [6.1 First-In-First-Out (FIFO)](#61-first-in-first-out-fifo)
  - [6.2 Least Recently Used (LRU)](#62-least-recently-used-lru)
  - [6.3 Optimal Page Replacement (OPT)](#63-optimal-page-replacement-opt)
  - [6.4 Side-by-Side Comprehensive Comparison Numerical](#64-side-by-side-comprehensive-comparison-numerical)
- [7. University Exam Question Bank with Complete Model Answers](#7-university-exam-question-bank-with-complete-model-answers)
  - [7.1 Short-Answer Questions (5 Marks)](#71-short-answer-questions-5-marks)
  - [7.2 Long-Answer / Essay Questions (10 Marks)](#72-long-answer-essay-questions-10-marks)
- [8. Syllabus Coverage & Numerical Types Checklist](#8-syllabus-coverage-numerical-types-checklist)

---

## 1. Memory Management Requirements

Primary memory (RAM) is a critical, finite system resource that must be shared dynamically between the Operating System kernel and multiple executing user processes. An effective Memory Management Subsystem must satisfy five fundamental hardware and software requirements.

```
+-----------------------------------------------------------------------+
|                    MEMORY MANAGEMENT REQUIREMENTS                     |
+---------------+---------------+---------------+---------------+-------+
|  Relocation   |  Protection   |    Sharing    |  Logical Org. | Phys. |
| (Base/Limit)  | (Bounds Ck.)  | (Shared Code) | (Modules/Seg) | (RAM) |
+---------------+---------------+---------------+---------------+-------+
```

### 1.1 Relocation
- **Definition:** Relocation is the ability of the operating system to load and execute a process in any arbitrary region of physical memory, and to move a process from one area of main memory to another during its execution lifecycle.
- **Why It Is Necessary:** In a multiprogramming system, processes are frequently swapped out to secondary storage (disk) when blocked or preempted, and subsequently swapped back into main memory. It is highly improbable that the process will be restored to the exact same physical memory addresses it previously occupied.
- **Mechanism:**
  - **Static Relocation:** Done at load-time by adjusting absolute memory addresses before program execution begins. Once loaded, the process cannot be moved in RAM.
  - **Dynamic Relocation:** Supported by hardware Memory Management Units (MMU) at runtime using a **Relocation Register (Base Register)**. Every logical address generated by the CPU is automatically added to the contents of the Base Register to yield the physical RAM address:
    $$\text{Physical Address} = \text{Logical Address} + \text{Base Register Value}$$

### 1.2 Protection
- **Definition:** Protection ensures that no process can access or modify the memory space allocated to another process or the operating system kernel without explicit permission.
- **Why It Is Necessary:** Software bugs or malicious code in one user application must not corrupt the memory state of other concurrent applications or crash the operating system.
- **Mechanism:**
  - The CPU hardware compares every generated logical address against a **Limit Register** (or checks if $\text{Physical Address} < \text{Base} + \text{Limit}$).
  - If a process attempts to access an address outside its bounds ($\text{Logical Address} \ge \text{Limit}$), the MMU hardware triggers an execution trap to the OS kernel (**Segmentation Fault / Access Violation**).
  - *Note:* Protection MUST be satisfied at runtime by hardware, because dynamic relocation implies that program memory locations cannot be anticipated at compile-time.

### 1.3 Sharing
- **Definition:** Sharing allows multiple concurrent processes to access the exact same region of main memory safely without maintaining redundant duplicate copies.
- **Why It Is Necessary:** If multiple processes execute the same application code (e.g., multiple text editor instances, shared C library functions like `printf`), storing a single read-only copy of the code in main memory saves significant RAM.
- **Mechanism:** Memory protection mechanisms are configured to permit controlled, shared read-only access to specific memory regions, while maintaining strict isolation for write operations on process-private data spaces.

### 1.4 Logical Organization
- **Definition:** Logical organization refers to the way memory is perceived and structured by the programmer and operating system software—typically as a collection of modular units (main program, subroutines, arrays, stacks, data structures).
- **Why It Is Necessary:** Programmers do not view memory as a linear, unformatted array of bytes. Organizing memory into logical modules aligns physical storage with software design principles.
- **Mechanism:** Modern operating systems support logical organization through **Segmentation**, where distinct program entities are placed into separate memory segments with individual access control properties (e.g., read-only code segments, read-write data segments, execute-only routines).

### 1.5 Physical Organization
- **Definition:** Physical organization concerns the management of the flow of information between the two physical levels of system storage: volatile primary memory (RAM) and non-volatile secondary storage (disk/SSD).
- **Why It Is Necessary:** Main memory capacity is insufficient to hold all active system code and data simultaneously. System programmers cannot be expected to manually manage overlaying or data transfers between RAM and disk.
- **Mechanism:** The OS transparently automates memory-to-disk transfers via **Paging**, **Swapping**, and **Virtual Memory Management**.

---

### 1.6 Comparison Table of Memory Management Requirements

| Requirement | Primary Purpose | Enforced By | Runtime Overhead |
| :--- | :--- | :--- | :--- |
| **Relocation** | Allows programs to run at any RAM location after swapping. | Hardware MMU (Base Register) | Minimal (1 addition per memory cycle) |
| **Protection** | Prevents unauthorized cross-process memory access. | Hardware MMU (Limit Register) | Minimal (1 comparison per memory cycle) |
| **Sharing** | Conserves RAM by reusing read-only code modules. | OS Page/Segment Tables | Zero runtime penalty (shared hardware mappings) |
| **Logical Org.** | Maps software modules (functions, stacks) to memory structures. | Compiler, Linker & OS | Moderate (segment table lookup overhead) |
| **Physical Org.** | Handles transparent data flow between RAM and disk. | OS Kernel & Virtual Memory | High during page faults (disk I/O latency) |

---

## 2. Contiguous Memory Allocation & Memory Partitioning

Contiguous memory allocation requires each process to be loaded into a single, continuous block of physical memory addresses.

```
+-----------------------------------------------------------------------+
|                      CONTIGUOUS MEMORY ALLOCATION                     |
+-----------------------------------+-----------------------------------+
|         Fixed Partitioning        |   Variable / Dynamic Partitioning |
|  - Pre-divided memory blocks      |  - Dynamically carved blocks      |
|  - Suffers from Internal Frag.    |  - Suffers from External Frag.    |
+-----------------------------------+-----------------------------------+
```

### 2.1 Fixed Partitioning vs. Variable/Dynamic Partitioning

#### 1. Fixed (Static) Partitioning
- **Concept:** Main memory is divided into fixed-sized regions (partitions) at system initialization. Partitions may be equal in size or unequal in size.
- **Allocation Rule:** When a process arrives, it is allocated to any free partition that is large enough to hold it. Each partition can hold **exactly one process**.
- **Advantages:** Simple to implement; minimal management overhead.
- **Disadvantages:**
  1. Inflexible limit on process size (a process larger than the maximum partition size cannot run).
  2. Severe **Internal Fragmentation** when small processes occupy large fixed partitions.
  3. Degree of multiprogramming is strictly capped by the number of partitions.

#### 2. Variable (Dynamic) Partitioning
- **Concept:** Main memory is not pre-divided. Memory is allocated dynamically to arriving processes from a contiguous block of free memory (called a **Hole**) matching the exact memory size requested by the process.
- **Allocation Rule:** As processes arrive and terminate, memory becomes a alternate sequence of allocated process regions and variable-sized free holes.
- **Advantages:** Eliminates internal fragmentation completely; process size is limited only by total main memory capacity.
- **Disadvantages:** Leads to **External Fragmentation** over time as processes terminate and leave scattered free gaps.

---

### 2.2 Internal vs. External Fragmentation

```
INTERNAL FRAGMENTATION:               EXTERNAL FRAGMENTATION:
Allocated Partition (100 KB)          Main Memory (Total Free: 120 KB)
+------------------------+            +------------------------+
| Process Data (60 KB)   |            | Process A (200 KB)     |
+------------------------+            +------------------------+
| Unused Space (40 KB)   | <--- WAIST | Free Hole 1 (50 KB)    | <--- Scattered
| (Inside Partition)     |            +------------------------+      Free Holes
+------------------------+            | Process B (300 KB)     |      (Cannot fit
                                      +------------------------+      a 100 KB
                                      | Free Hole 2 (70 KB)    | <--- Request)
                                      +------------------------+
```

| Parameter | Internal Fragmentation | External Fragmentation |
| :--- | :--- | :--- |
| **Definition** | Unused memory space that exists **inside** an allocated partition boundary. | Unused memory space that exists **outside** allocated partitions, scattered across RAM. |
| **Primary Cause** | Occurs when fixed-size partitions are assigned to smaller processes. | Occurs when dynamic memory allocations and deallocations leave tiny, non-contiguous free holes. |
| **Total Memory Condition** | A single partition has more space than the process needs. | Total sum of all free holes is sufficient for a process, but no single hole is contiguous. |
| **Primary Occurrence** | Fixed Partitioning, Paging (last page of a process). | Variable Partitioning, Segmentation. |
| **Solution** | Use Variable Partitioning or smaller page sizes. | **Compaction** or non-contiguous allocation (Paging). |

---

### 2.3 Compaction
- **Definition:** Compaction is a technique used in dynamic partitioning to overcome external fragmentation. The operating system shifts all allocated process memory blocks toward one end of main memory, consolidating all scattered free holes into a single, large contiguous free block.
- **Requirements:** Compaction is only possible if program relocation is **dynamic** (supported at runtime via hardware base registers).
- **Drawback:** Compaction requires reading and rewriting vast amounts of physical RAM, incurring **massive CPU and memory bus overhead** that freezes process execution during the operation.

---

### 2.4 Partition Allocation Strategies

When a process requesting $S$ bytes arrives in a dynamic partitioning system, the OS searches the list of available free holes to place it. Four major placement strategies exist:

1. **First Fit:**
   - **Algorithm:** Scan the free hole list from the beginning and allocate the process to the **very first hole that is large enough** ($\text{Hole Size} \ge S$).
   - **Characteristics:** Fastest allocation speed; tends to clutter the beginning of memory with small leftover fragments.

2. **Best Fit:**
   - **Algorithm:** Scan the **entire** free hole list (or maintain a list sorted by size) and allocate the process to the **smallest hole that is large enough**.
   - **Characteristics:** Produces the smallest possible leftover fragment; extremely prone to producing tiny, unusable memory "dust" (severe external fragmentation). Requires searching the entire list.

3. **Worst Fit:**
   - **Algorithm:** Scan the **entire** free hole list and allocate the process to the **largest available hole**.
   - **Characteristics:** Leaves behind the largest possible leftover fragment, theoretical goal being that the leftover hole remains large enough for future jobs. In practice, it rapidly breaks down large free blocks, rendering the system incapable of serving large process requests.

4. **Next Fit:**
   - **Algorithm:** Similar to First Fit, but begins scanning the hole list from the **location of the last allocation search pointer** rather than starting from the beginning.
   - **Characteristics:** Distributes allocations evenly across memory; tends to break down the large free block located at the end of memory space.

---

### 2.5 Fully Worked Numerical: Partition Allocation Strategies

#### Problem Statement
Given a main memory layout with free memory holes in the following sequential order:
$$\text{Hole 1} = 200\text{ KB}, \quad \text{Hole 2} = 500\text{ KB}, \quad \text{Hole 3} = 300\text{ KB}, \quad \text{Hole 4} = 600\text{ KB}$$

Four process requests arrive in sequential order:
$$\text{P1} = 212\text{ KB}, \quad \text{P2} = 417\text{ KB}, \quad \text{P3} = 112\text{ KB}, \quad \text{P4} = 426\text{ KB}$$

Perform placement calculations for **First Fit**, **Best Fit**, **Worst Fit**, and **Next Fit**. For each algorithm, show:
1. The hole allocated to each process request.
2. The search position of the allocation pointer for Next Fit.
3. The remaining size of each hole after all requests are processed.
4. Total remaining unallocated free memory and external fragmentation status.

---

#### Step-by-Step Solution

##### 1. First Fit Allocation

Initial Holes: `[H1: 200 KB, H2: 500 KB, H3: 300 KB, H4: 600 KB]`

- **Process P1 (212 KB):**
  - Check H1 (200 KB): Too small ($200 < 212$).
  - Check H2 (500 KB): Fits ($500 \ge 212$). Allocate P1 in **H2**.
  - Leftover H2 = $500 - 212 = 288\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 288 KB, H3: 300 KB, H4: 600 KB]`

- **Process P2 (417 KB):**
  - Check H1 (200 KB): Too small.
  - Check H2 (288 KB): Too small.
  - Check H3 (300 KB): Too small.
  - Check H4 (600 KB): Fits ($600 \ge 417$). Allocate P2 in **H4**.
  - Leftover H4 = $600 - 417 = 183\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 288 KB, H3: 300 KB, H4: 183 KB]`

- **Process P3 (112 KB):**
  - Check H1 (200 KB): Fits ($200 \ge 112$). Allocate P3 in **H1**.
  - Leftover H1 = $200 - 112 = 88\text{ KB}$.
  - Current Holes: `[H1: 88 KB, H2: 288 KB, H3: 300 KB, H4: 183 KB]`

- **Process P4 (426 KB):**
  - Check H1 (88 KB): Too small.
  - Check H2 (288 KB): Too small.
  - Check H3 (300 KB): Too small.
  - Check H4 (183 KB): Too small.
  - **Result:** P4 **CANNOT** be allocated! P4 must wait.

**First Fit Final Memory Summary:**
- Allocated: P1 in H2, P2 in H4, P3 in H1.
- Unallocated Process: P4 (426 KB).
- Final Hole State: `H1 = 88 KB`, `H2 = 288 KB`, `H3 = 300 KB`, `H4 = 183 KB`.
- Total Free Memory Remaining = $88 + 288 + 300 + 183 = 859\text{ KB}$.
- *External Fragmentation Note:* Total free RAM ($859\text{ KB}$) is far greater than P4's request ($426\text{ KB}$), but no single hole is contiguous.

---

##### 2. Best Fit Allocation

Initial Holes: `[H1: 200 KB, H2: 500 KB, H3: 300 KB, H4: 600 KB]`

- **Process P1 (212 KB):**
  - Candidates ($\ge 212$): H2 (500), H3 (300), H4 (600).
  - Smallest candidate: **H3 (300 KB)**.
  - Allocate P1 in **H3**. Leftover H3 = $300 - 212 = 88\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 500 KB, H3: 88 KB, H4: 600 KB]`

- **Process P2 (417 KB):**
  - Candidates ($\ge 417$): H2 (500), H4 (600).
  - Smallest candidate: **H2 (500 KB)**.
  - Allocate P2 in **H2**. Leftover H2 = $500 - 417 = 83\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 83 KB, H3: 88 KB, H4: 600 KB]`

- **Process P3 (112 KB):**
  - Candidates ($\ge 112$): H1 (200), H4 (600).
  - Smallest candidate: **H1 (200 KB)**.
  - Allocate P3 in **H1**. Leftover H1 = $200 - 112 = 88\text{ KB}$.
  - Current Holes: `[H1: 88 KB, H2: 83 KB, H3: 88 KB, H4: 600 KB]`

- **Process P4 (426 KB):**
  - Candidates ($\ge 426$): H4 (600 KB).
  - Allocate P4 in **H4**. Leftover H4 = $600 - 426 = 174\text{ KB}$.
  - Current Holes: `[H1: 88 KB, H2: 83 KB, H3: 88 KB, H4: 174 KB]`

**Best Fit Final Memory Summary:**
- Allocated: **ALL processes allocated!** (P1 in H3, P2 in H2, P3 in H1, P4 in H4).
- Final Hole State: `H1 = 88 KB`, `H2 = 83 KB`, `H3 = 88 KB`, `H4 = 174 KB`.
- Total Free Memory Remaining = $88 + 83 + 88 + 174 = 433\text{ KB}$.

---

##### 3. Worst Fit Allocation

Initial Holes: `[H1: 200 KB, H2: 500 KB, H3: 300 KB, H4: 600 KB]`

- **Process P1 (212 KB):**
  - Largest available hole: **H4 (600 KB)**.
  - Allocate P1 in **H4**. Leftover H4 = $600 - 212 = 388\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 500 KB, H3: 300 KB, H4: 388 KB]`

- **Process P2 (417 KB):**
  - Largest available hole: **H2 (500 KB)**.
  - Allocate P2 in **H2**. Leftover H2 = $500 - 417 = 83\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 83 KB, H3: 300 KB, H4: 388 KB]`

- **Process P3 (112 KB):**
  - Largest available hole: **H4 (388 KB)**.
  - Allocate P3 in **H4**. Leftover H4 = $388 - 112 = 276\text{ KB}$.
  - Current Holes: `[H1: 200 KB, H2: 83 KB, H3: 300 KB, H4: 276 KB]`

- **Process P4 (426 KB):**
  - Largest available hole: H4 (276 KB).
  - All holes are smaller than 426 KB ($200, 83, 300, 276 < 426$).
  - **Result:** P4 **CANNOT** be allocated! P4 must wait.

**Worst Fit Final Memory Summary:**
- Allocated: P1 in H4, P2 in H2, P3 in H4.
- Unallocated Process: P4 (426 KB).
- Final Hole State: `H1 = 200 KB`, `H2 = 83 KB`, `H3 = 300 KB`, `H4 = 276 KB`.
- Total Free Memory Remaining = $200 + 83 + 300 + 276 = 859\text{ KB}$.

---

##### 4. Next Fit Allocation

Initial Holes: `[H1: 200 KB, H2: 500 KB, H3: 300 KB, H4: 600 KB]`  
Search Pointer Initial Position: **H1**

- **Process P1 (212 KB):**
  - Scan starts at H1. H1 (200) too small.
  - H2 (500) fits ($500 \ge 212$). Allocate P1 in **H2**.
  - Leftover H2 = $288\text{ KB}$.
  - **Search Pointer is now at H2.**
  - Current Holes: `[H1: 200 KB, H2: 288 KB, H3: 300 KB, H4: 600 KB]`

- **Process P2 (417 KB):**
  - Scan starts at H2 (288 KB). H2 (288) too small.
  - H3 (300 KB) too small.
  - H4 (600 KB) fits ($600 \ge 417$). Allocate P2 in **H4**.
  - Leftover H4 = $183\text{ KB}$.
  - **Search Pointer is now at H4.**
  - Current Holes: `[H1: 200 KB, H2: 288 KB, H3: 300 KB, H4: 183 KB]`

- **Process P3 (112 KB):**
  - Scan starts at H4 (183 KB). H4 (183) fits ($183 \ge 112$).
  - Allocate P3 in **H4**.
  - Leftover H4 = $183 - 112 = 71\text{ KB}$.
  - **Search Pointer remains at H4.**
  - Current Holes: `[H1: 200 KB, H2: 288 KB, H3: 300 KB, H4: 71 KB]`

- **Process P4 (426 KB):**
  - Scan starts at H4 (71 KB). H4 (71) too small.
  - Wrap around to start of list: H1 (200 KB) too small.
  - H2 (288 KB) too small.
  - H3 (300 KB) too small.
  - Reached starting point H4.
  - **Result:** P4 **CANNOT** be allocated! P4 must wait.

**Next Fit Final Memory Summary:**
- Allocated: P1 in H2, P2 in H4, P3 in H4.
- Unallocated Process: P4 (426 KB).
- Final Hole State: `H1 = 200 KB`, `H2 = 288 KB`, `H3 = 300 KB`, `H4 = 71 KB`.
- Total Free Memory Remaining = $200 + 288 + 300 + 71 = 859\text{ KB}$.

---

#### Comparative Summary of Placement Results

| Process | Requested | First Fit | Best Fit | Worst Fit | Next Fit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P1** | 212 KB | Allocated in H2 | Allocated in H3 | Allocated in H4 | Allocated in H2 |
| **P2** | 417 KB | Allocated in H4 | Allocated in H2 | Allocated in H2 | Allocated in H4 |
| **P3** | 112 KB | Allocated in H1 | Allocated in H1 | Allocated in H4 | Allocated in H4 |
| **P4** | 426 KB | **FAILED** | **Allocated in H4** | **FAILED** | **FAILED** |
| **Efficiency** | — | 3/4 Allocated | **4/4 Allocated (BEST)** | 3/4 Allocated | 3/4 Allocated |

*Conclusion:* In this specific memory configuration, **Best Fit** performed best by successfully accommodating all four processes.

---

### 2.6 The Buddy System

The Buddy System is a specialized memory allocation strategy that manages memory in powers-of-two block sizes ($2^k$), combining the speed of fixed partitioning with the flexibility of dynamic partitioning.

#### Operating Principles
1. **Memory Representation:** Memory is maintained as a single large contiguous block of size $2^U$ bytes.
2. **Allocation Rule:** When a memory request of size $s$ arrives:
   - Calculate integer $k$ such that: $2^{k-1} < s \le 2^k$.
   - If a free block of size $2^k$ is available, allocate it to the process.
   - If no block of size $2^k$ exists, split the smallest available free block of size $2^i$ ($i > k$) into two equal **buddies** of size $2^{i-1}$.
   - Continue recursively splitting until a block of size $2^k$ is produced, and allocate it.
3. **Deallocation and Merging Rule:**
   - When a process releases its allocated block of size $2^k$, the OS checks whether its corresponding adjacent **buddy** block is also free.
   - If the buddy is free, the two blocks are **coalesced (merged)** into a single larger block of size $2^{k+1}$.
   - Coalescing continues recursively up the binary tree as long as adjacent buddies are free.

---

### 2.7 Fully Worked Numerical: The Buddy System

#### Problem Statement
A system uses a Binary Buddy System with an initial memory block of size **1024 KB** ($1\text{ MB} = 2^{10}\text{ KB}$).
Process memory events occur in the following chronological sequence:
1. Process **A** requests **100 KB**
2. Process **B** requests **240 KB**
3. Process **C** requests **64 KB**
4. Process **D** requests **256 KB**
5. Process **A** releases **100 KB**
6. Process **C** releases **64 KB**
7. Process **B** releases **240 KB**
8. Process **D** releases **256 KB**

Show the memory layout, power-of-two block sizes allocated, splitting steps, internal fragmentation per block, and merging operations after every step.

---

#### Step-by-Step Solution

##### Initial State
- Entire memory is one single free block: `1024 KB` ($2^{10}$).

```
[1024 KB Free]
```

---

##### Step 1: Process A requests 100 KB
- Power-of-2 requirement: $2^{6} = 64 < 100 \le 128 = 2^7$. Requires a **128 KB** block.
- Split `1024 KB` $\rightarrow$ two `512 KB` buddies.
- Split first `512 KB` $\rightarrow$ two `256 KB` buddies.
- Split first `256 KB` $\rightarrow$ two `128 KB` buddies.
- Allocate **Process A** into the first `128 KB` block.
- **Internal Fragmentation for A:** $128 - 100 = 28\text{ KB}$.

**Memory Layout:**
```
[ A: 128 KB ] [ 128 KB Free ] [ 256 KB Free ] [ 512 KB Free ]
```

---

##### Step 2: Process B requests 240 KB
- Power-of-2 requirement: $2^7 = 128 < 240 \le 256 = 2^8$. Requires a **256 KB** block.
- A free `256 KB` block is available directly!
- Allocate **Process B** into the free `256 KB` block.
- **Internal Fragmentation for B:** $256 - 240 = 16\text{ KB}$.

**Memory Layout:**
```
[ A: 128 KB ] [ 128 KB Free ] [ B: 256 KB ] [ 512 KB Free ]
```

---

##### Step 3: Process C requests 64 KB
- Power-of-2 requirement: $2^5 = 32 < 64 \le 64 = 2^6$. Requires a **64 KB** block.
- Smallest available block is `128 KB Free`.
- Split `128 KB Free` $\rightarrow$ two `64 KB` buddies.
- Allocate **Process C** into the first `64 KB` block.
- **Internal Fragmentation for C:** $64 - 64 = 0\text{ KB}$ (Exact fit!).

**Memory Layout:**
```
[ A: 128 KB ] [ C: 64 KB ] [ 64 KB Free ] [ B: 256 KB ] [ 512 KB Free ]
```

---

##### Step 4: Process D requests 256 KB
- Power-of-2 requirement: Requires a **256 KB** block ($2^8$).
- Smallest available block is `512 KB Free`.
- Split `512 KB Free` $\rightarrow$ two `256 KB` buddies.
- Allocate **Process D** into the first `256 KB` block.
- **Internal Fragmentation for D:** $256 - 256 = 0\text{ KB}$.

**Memory Layout:**
```
[ A: 128 KB ] [ C: 64 KB ] [ 64 KB Free ] [ B: 256 KB ] [ D: 256 KB ] [ 256 KB Free ]
```

---

##### Step 5: Process A releases 100 KB (Frees 128 KB Block)
- The block `[128 KB]` occupied by A becomes free.
- Check A's buddy: Adjacent buddy is divided into `[ C: 64 KB ] [ 64 KB Free ]` (Not completely free!).
- **Coalescing Result:** Cannot merge yet.

**Memory Layout:**
```
[ 128 KB Free ] [ C: 64 KB ] [ 64 KB Free ] [ B: 256 KB ] [ D: 256 KB ] [ 256 KB Free ]
```

---

##### Step 6: Process C releases 64 KB (Frees 64 KB Block)
- The block `[64 KB]` occupied by C becomes free.
- **Merge 1:** C's adjacent `64 KB Free` buddy is free! Coalesce two `64 KB` blocks $\rightarrow$ single `128 KB Free` block.
- **Merge 2:** This new `128 KB Free` block's buddy is the left `128 KB Free` block (formerly A)! Coalesce two `128 KB` blocks $\rightarrow$ single `256 KB Free` block.
- **Merge 3:** Check buddy of `256 KB Free`: Adjacent block is `[ B: 256 KB ]` (Busy). Stopping merge.

**Memory Layout:**
```
[ 256 KB Free ] [ B: 256 KB ] [ D: 256 KB ] [ 256 KB Free ]
```

---

##### Step 7: Process B releases 240 KB (Frees 256 KB Block)
- The block `[256 KB]` occupied by B becomes free.
- **Merge 1:** Adjacent left buddy is `256 KB Free`! Coalesce two `256 KB` blocks $\rightarrow$ single `512 KB Free` block.
- Check buddy of `512 KB Free`: Adjacent right region is `[ D: 256 KB ] [ 256 KB Free ]` (Busy because D is allocated). Stopping merge.

**Memory Layout:**
```
[ 512 KB Free ] [ D: 256 KB ] [ 256 KB Free ]
```

---

##### Step 8: Process D releases 256 KB (Frees 256 KB Block)
- The block `[256 KB]` occupied by D becomes free.
- **Merge 1:** D's adjacent right buddy is `256 KB Free`! Coalesce two `256 KB` blocks $\rightarrow$ single `512 KB Free` block.
- **Merge 2:** This new `512 KB Free` block's left buddy is the `512 KB Free` block! Coalesce two `512 KB` blocks $\rightarrow$ single `1024 KB Free` block.

**Final Memory Layout:**
```
[ 1024 KB Free ]
```

*Conclusion:* Memory has fully returned to its initial coalesced state of **1024 KB Free**.

---

## 3. Paging

Paging is a non-contiguous memory management scheme that permits the physical address space of a process to be non-contiguous.

```
LOGICAL ADDRESS SPACE (Process)         PHYSICAL MEMORY (RAM)
+-----------------------+              +-----------------------+
|  Page 0               |              |  Frame 0              |
+-----------------------+              +-----------------------+
|  Page 1               | -----\       |  Frame 1 (Page 0)     |
+-----------------------+       \      +-----------------------+
|  Page 2               |        \---> |  Frame 2 (Page 1)     |
+-----------------------+              +-----------------------+
|  Page 3               |              |  Frame 3 (Page 3)     |
+-----------------------+              +-----------------------+
                                       |  Frame 4 (Page 2)     |
                                       +-----------------------+
```

### 3.1 Principles of Operation: Pages and Frames
1. **Frames:** Physical memory is divided into fixed-sized blocks called **Frames** (typically $4\text{ KB} = 4096\text{ bytes}$).
2. **Pages:** Logical address space of a process is divided into blocks of the exact same size called **Pages**.
3. **Allocation Rule:** When a process executes, its pages are loaded into any available free physical frames in RAM. Non-contiguous frame allocation eliminates External Fragmentation completely!
4. **Hardware Address Translation:** The CPU generates a **Logical Address** which is translated dynamically by the Memory Management Unit (MMU) into a **Physical Address** using a process **Page Table**.

---

### 3.2 Logical-to-Physical Address Translation

A Logical Address generated by the CPU consists of two parts:

```
+-----------------------------------+-----------------------------------+
|       Page Number (p)             |        Page Offset (d)            |
|       (m - n bits)                |           (n bits)                |
+-----------------------------------+-----------------------------------+
```

- **Page Number ($p$):** Used as an index into the process **Page Table**.
- **Page Offset ($d$):** Defines the exact byte offset within the page/frame.
- **Page Size ($S$):** Determined by hardware ($S = 2^n\text{ bytes}$). The offset requires $n$ bits.
- **Logical Address Space Size:** $2^m\text{ bytes}$. The page number requires $(m - n)$ bits.

```
Logical Address: (p, d)
        |
        v
  [ Page Table ]  ---> Maps Page Number p to Frame Number f
        |
        v
Physical Address: (f, d)  --->  Physical Location = (f * Page Size) + d
```

---

### 3.3 Page Table Structure & Hardware Support
- Each executing process has its own **Page Table** stored in physical RAM.
- **Page Table Base Register (PTBR):** A CPU register that points to the starting physical RAM address of the active process's page table.
- **Page Table Length Register (PTLR):** Indicates the size of the page table (for bounds checking).
- **Page Table Entry (PTE) Structure:**
  ```
  +---------------+---------------+---------------+---------------+---------------+
  | Frame No. (f) |  Valid/Invalid| Read/Write/Ex |  Modify/Dirty | Referenced Bit|
  +---------------+---------------+---------------+---------------+---------------+
  ```

---

### 3.4 Translation Lookaside Buffer (TLB) & Effective Access Time

Because the page table is stored in main memory, every standard logical memory reference requires **two physical RAM accesses**:
1. Access 1: Read the Page Table Entry from RAM to obtain the frame number $f$.
2. Access 2: Access the actual desired data byte at physical address $(f \cdot S) + d$.

To eliminate this $2\times$ memory access penalty, operating systems use a high-speed associative hardware cache called the **Translation Lookaside Buffer (TLB)** inside the MMU.

```
CPU Logical Address (p, d)
        |
        +---> [ Search TLB Associatively ]
                     |
         +-----------+-----------+
         |                       |
     [ TLB HIT ]             [ TLB MISS ]
         |                       |
Get Frame Number f        Read Page Table from RAM
         |                       |
         +-----------+-----------+
                     |
                     v
   Form Physical Address (f, d) & Access RAM
```

#### Effective Access Time (EAT) Formula

Let:
- $\alpha =$ TLB Hit Ratio (fraction of times page number is found in TLB, $0 \le \alpha \le 1$).
- $\epsilon =$ TLB Lookup Time (hardware associativity check delay, e.g., $20\text{ ns}$).
- $m =$ Main Memory Access Time (RAM latency, e.g., $100\text{ ns}$).

$$\text{EAT} = \alpha \cdot (\epsilon + m) + (1 - \alpha) \cdot (\epsilon + 2m)$$

Simplifying algebraically:
$$\text{EAT} = \epsilon + (2 - \alpha) \cdot m$$

---

### 3.5 Protection and Sharing in Paging
- **Protection Bits:** Attached to each Page Table Entry to enforce read-only (`R`), read-write (`RW`), or execute-only (`X`) access permissions.
- **Valid/Invalid Bit:**
  - `Valid (v)`: Indicates the page is part of the process's logical address space and is resident in physical RAM.
  - `Invalid (i)`: Indicates the page is either not in the process address space or currently resides on disk (virtual memory).
- **Sharing (Reentrant Code):** If two processes execute pure, non-modifying (reentrant) code (such as compilers or standard C libraries), their page tables simply map the logical pages to the identical physical frame numbers in RAM.

---

### 3.6 Disadvantages of Paging
1. **Internal Fragmentation:** While external fragmentation is eliminated, internal fragmentation occurs on the **last page of every process** (on average, $\frac{1}{2}\text{ Page Size}$ per process).
2. **Memory Overhead:** Page tables themselves consume significant physical RAM (e.g., a 32-bit system with 4 KB pages requires a 4 MB page table per process).
3. **Memory Access Delay:** Without a TLB hit, every memory access requires two physical RAM references.

---

### 3.7 Fully Worked Numericals: Paging & TLB Calculations

#### Numerical Type 1: Address Bits & Page Table Size Calculation

##### Problem Statement
A computer system has a **32-bit logical address space** and uses a page size of **4 KB** ($4096\text{ bytes}$).
Each Page Table Entry (PTE) takes **4 bytes** of memory.
Calculate:
1. The number of bits in the Page Offset ($d$).
2. The number of bits in the Page Number ($p$).
3. Total number of pages in the logical address space.
4. Total size of the Page Table for a single process in megabytes (MB).

##### Solution
1. **Page Offset Bits ($d$):**
   $$\text{Page Size } S = 4\text{ KB} = 4096\text{ bytes} = 2^{12}\text{ bytes}$$
   Therefore, offset bits $d = 12\text{ bits}$.

2. **Page Number Bits ($p$):**
   $$\text{Total Address Bits } m = 32\text{ bits}$$
   $$p = m - d = 32 - 12 = 20\text{ bits}$$

3. **Total Number of Pages:**
   $$\text{Number of Pages} = 2^p = 2^{20} = 1,048,576\text{ pages } (1\text{ Million Pages})$$

4. **Page Table Size:**
   $$\text{Page Table Size} = (\text{Number of Pages}) \times (\text{Size of 1 PTE})$$
   $$\text{Page Table Size} = 2^{20} \times 4\text{ bytes} = 1,048,576 \times 4\text{ bytes} = 4,194,304\text{ bytes}$$
   $$\text{Page Table Size in MB} = \frac{4,194,304}{1024 \times 1024} = 4\text{ MB}$$

*Answer:* The system uses **12 bits for offset**, **20 bits for page number**, has **$2^{20}$ pages**, and requires **4 MB** of RAM for each process page table.

---

#### Numerical Type 2: Logical-to-Physical Address Translation

##### Problem Statement
A paging system has a page size of **1 KB** ($1024\text{ bytes}$).
A process has the following Page Table mapping:

| Page Number ($p$) | Frame Number ($f$) |
| :---: | :---: |
| 0 | 5 |
| 1 | 2 |
| 2 | 9 |
| 3 | 1 |

Translate the following CPU logical addresses into physical addresses (in decimal):
1. **Logical Address = 1500**
2. **Logical Address = 3200**

##### Solution

###### Part 1: Translate Logical Address 1500
- **Step 1: Calculate Page Number ($p$) and Offset ($d$)**
  $$p = \lfloor \frac{\text{Logical Address}}{\text{Page Size}} \rfloor = \lfloor \frac{1500}{1024} \rfloor = 1$$
  $$d = \text{Logical Address} \pmod{\text{Page Size}} = 1500 \pmod{1024} = 476$$

- **Step 2: Look up Frame Number ($f$) in Page Table**
  For $p = 1$, Page Table gives Frame Number $f = 2$.

- **Step 3: Calculate Physical Address**
  $$\text{Physical Address} = (f \times \text{Page Size}) + d = (2 \times 1024) + 476 = 2048 + 476 = 2524$$

###### Part 2: Translate Logical Address 3200
- **Step 1: Calculate Page Number ($p$) and Offset ($d$)**
  $$p = \lfloor \frac{3200}{1024} \rfloor = 3$$
  $$d = 3200 \pmod{1024} = 3200 - (3 \times 1024) = 3200 - 3072 = 128$$

- **Step 2: Look up Frame Number ($f$) in Page Table**
  For $p = 3$, Page Table gives Frame Number $f = 1$.

- **Step 3: Calculate Physical Address**
  $$\text{Physical Address} = (f \times \text{Page Size}) + d = (1 \times 1024) + 128 = 1024 + 128 = 1152$$

*Answer:* Logical Address 1500 maps to **Physical Address 2524**. Logical Address 3200 maps to **Physical Address 1152**.

---

#### Numerical Type 3: TLB Effective Access Time (EAT)

##### Problem Statement
A paging system has a main memory access time of **100 nanoseconds (ns)** and a TLB lookup time of **20 ns**.
Calculate the Effective Access Time (EAT) for:
1. A TLB hit ratio of **80% ($\alpha = 0.80$)**.
2. A TLB hit ratio of **98% ($\alpha = 0.98$)**.

##### Solution

###### Part 1: For $\alpha = 0.80$
$$\text{EAT} = \alpha \cdot (\epsilon + m) + (1 - \alpha) \cdot (\epsilon + 2m)$$
$$\text{EAT} = 0.80 \cdot (20 + 100) + (1 - 0.80) \cdot (20 + 200)$$
$$\text{EAT} = 0.80 \cdot (120) + 0.20 \cdot (220) = 96 + 44 = 140\text{ ns}$$

###### Part 2: For $\alpha = 0.98$
$$\text{EAT} = 0.98 \cdot (20 + 100) + (1 - 0.98) \cdot (20 + 200)$$
$$\text{EAT} = 0.98 \cdot (120) + 0.02 \cdot (220) = 117.6 + 4.4 = 122\text{ ns}$$

*Answer:* EAT at 80% hit ratio is **140 ns**. Increasing TLB hit ratio to 98% improves EAT to **122 ns** (a reduction of 18 ns per memory reference).

---

## 4. Segmentation

### 4.1 Concept of Segmentation
Segmentation is a memory management scheme that supports the user's view of memory. Rather than dividing memory into fixed linear blocks, a program is viewed as a collection of variable-length **Segments** (e.g., Main Routine, Functions, Global Variables, Stack, Symbol Table).

```
PROGRAMMER'S LOGICAL VIEW               PHYSICAL MEMORY (RAM)
+-----------------------+              +-----------------------+
| Segment 0: Main Prog  |              | Segment 1 (Square)    |
+-----------------------+              +-----------------------+
| Segment 1: Square Func| -----\       | Segment 0 (Main)      |
+-----------------------+       \      +-----------------------+
| Segment 2: Stack      |        \---> | Segment 3 (Globals)   |
+-----------------------+              +-----------------------+
| Segment 3: Globals    |              | Segment 2 (Stack)     |
+-----------------------+              +-----------------------+
```

---

### 4.2 Segment Table & Hardware Address Mapping

A CPU logical address in segmentation consists of two components:
$$\text{Logical Address} = \langle \text{Segment Number } s, \text{ Segment Offset } d \rangle$$

- **Segment Table:** Each entry contains:
  1. **Base Address ($\text{base}$):** The starting physical RAM address where the segment resides.
  2. **Segment Limit ($\text{limit}$):** The length of the segment.

```
Logical Address: (s, d)
        |
        v
  [ Check Offset Bounds ] ---> Is d < Limit?
        |                           |
       YES                          NO
        |                           |
        v                           v
  Physical Address = Base + d   TRAP: Segmentation Fault!
```

---

### 4.3 Comprehensive Comparison: Paging vs. Segmentation

| Parameter | Paging | Segmentation |
| :--- | :--- | :--- |
| **User/Programmer View** | Linear, contiguous address space (invisible partitioning). | Modular, variable-length functional modules (matches programmer view). |
| **Block Size** | Fixed-size blocks (e.g., 4 KB). | Variable-size blocks. |
| **Hardware Division** | Implemented strictly by OS hardware (MMU). | Software-driven logical compiler/linker structure. |
| **Address Structure** | Single integer split into $p$ and $d$ by bit manipulation. | Two explicit components $\langle s, d \rangle$. |
| **Fragmentation** | Suffers from **Internal Fragmentation** (last page); no external fragmentation. | Suffers from **External Fragmentation**; no internal fragmentation. |
| **Table Entries** | Page Table contains Frame Number ($f$) + control bits. | Segment Table contains Base Address + Limit Length + control bits. |
| **Protection & Sharing** | Easy to protect/share fixed pages. | Natural alignment for sharing functional code modules. |

---

### 4.4 Fully Worked Numerical: Segmentation Address Translation

#### Problem Statement
Consider the following **Segment Table**:

| Segment Number ($s$) | Base Address ($\text{base}$) | Limit Length ($\text{limit}$) |
| :---: | :---: | :---: |
| 0 | 219 | 600 |
| 1 | 2300 | 140 |
| 2 | 90 | 100 |
| 3 | 1327 | 580 |
| 4 | 1952 | 96 |

Translate the following CPU logical addresses $\langle s, d \rangle$ into physical addresses, or state if a trap/segmentation fault occurs:
1. **$\langle 0, 430 \rangle$**
2. **$\langle 1, 150 \rangle$**
3. **$\langle 2, 90 \rangle$**
4. **$\langle 3, 580 \rangle$**

---

#### Step-by-Step Solution

##### Case 1: Logical Address $\langle 0, 430 \rangle$
- Segment $s = 0$, Offset $d = 430$.
- Look up Segment 0: $\text{Base} = 219$, $\text{Limit} = 600$.
- **Bounds Check:** Is $d < \text{Limit}$? $\implies 430 < 600$ (**VALID**).
- **Physical Address Calculation:**
  $$\text{Physical Address} = \text{Base} + d = 219 + 430 = 649$$

##### Case 2: Logical Address $\langle 1, 150 \rangle$
- Segment $s = 1$, Offset $d = 150$.
- Look up Segment 1: $\text{Base} = 2300$, $\text{Limit} = 140$.
- **Bounds Check:** Is $d < \text{Limit}$? $\implies 150 < 140$ (**INVALID!** $150 \ge 140$).
- **Result:** **TRAP: Segmentation Fault / Access Violation!** (Offset exceeds segment boundary).

##### Case 3: Logical Address $\langle 2, 90 \rangle$
- Segment $s = 2$, Offset $d = 90$.
- Look up Segment 2: $\text{Base} = 90$, $\text{Limit} = 100$.
- **Bounds Check:** Is $d < \text{Limit}$? $\implies 90 < 100$ (**VALID**).
- **Physical Address Calculation:**
  $$\text{Physical Address} = \text{Base} + d = 90 + 90 = 180$$

##### Case 4: Logical Address $\langle 3, 580 \rangle$
- Segment $s = 3$, Offset $d = 580$.
- Look up Segment 3: $\text{Base} = 1327$, $\text{Limit} = 580$.
- **Bounds Check:** Is $d < \text{Limit}$? $\implies 580 < 580$ (**INVALID!** Offset must be strictly less than limit).
- **Result:** **TRAP: Segmentation Fault!**

---

## 5. Virtual Memory & Demand Paging

### 5.1 Principles of Virtual Memory
Virtual Memory is a technique that allows the execution of processes that are **not completely resident in physical main memory**. The logical address space can be much larger than the physical RAM space.

---

### 5.2 Demand Paging & Valid/Invalid Bits
Demand paging combines paging with virtual memory. Pages are loaded into RAM **only when they are explicitly referenced during execution** ("on demand").
- **Valid/Invalid Bit in Page Table:**
  - `Valid (v)`: The page belongs to the process's logical address space **and** is currently resident in physical RAM.
  - `Invalid (i)`: This single bit setting actually covers **two distinct situations**, which the page-fault handler must tell apart:
    1. **Legitimate page, not yet loaded:** The page is a genuine part of the process's address space but currently resides only on secondary storage (disk/swap). Referencing it causes an ordinary **page fault**, and the OS simply loads it into a free frame and resumes execution.
    2. **Illegal reference:** The address falls **outside** the process's valid logical address space altogether (e.g., a bad pointer or array-bounds bug). Referencing it also triggers an invalid-bit trap, but the OS's fault handler recognizes it as an out-of-bounds access and **aborts the process** (segmentation fault) instead of fetching anything from disk.
  - *Key distinction:* "Not resident" (case 1) is a recoverable, expected event handled by loading the page; "outside the valid address space" (case 2) is a programming error handled by terminating the process. Both are marked `Invalid` at the hardware level, but the OS's page-fault handler distinguishes them by checking whether the referenced page number lies within the process's declared address space (e.g., against its page table limits) before deciding whether to service the fault or raise a segmentation violation.

---

### 5.3 Page Fault Handling Mechanism

When a process attempts to access a page marked `Invalid (i)` in the page table, the CPU triggers a hardware trap called a **Page Fault**.

```
                       PAGE FAULT HANDLING SEQUENCE
                       ============================

1. CPU Accesses Logical Addr  ---> 2. Check Page Table (Valid/Invalid Bit)
                                              |
                                     [ Page Fault Trap ]
                                              |
                                              v
5. Update Page Table (v) <--- 4. Read Page into <--- 3. OS Page Fault Handler
   & Restart Instruction      Free Frame from Disk      Locates Page on Disk
```

---

### 5.4 Effective Access Time (EAT) in Demand Paging

Let:
- $m =$ Normal Main Memory Access Time (e.g., $100\text{ ns}$).
- $p =$ Page Fault Rate / Probability ($0 \le p \le 1$).
- $p_{fault} =$ Page Fault Service Time (disk read latency, e.g., $8\text{ ms} = 8,000,000\text{ ns}$).

$$\text{EAT} = (1 - p) \cdot m + p \cdot p_{fault}$$

---

### 5.5 Fully Worked Numerical: Demand Paging Effective Access Time

#### Problem Statement
A computer system has a main memory access time of **100 nanoseconds**.
A page fault takes **8 milliseconds** ($8,000,000\text{ ns}$) to service.
1. Calculate the Effective Access Time (EAT) if 1 out of every 1,000 memory accesses causes a page fault ($p = 0.001$).
2. What must the page fault rate $p$ be to keep the Effective Access Time below **200 nanoseconds**?

#### Solution

##### Part 1: Calculate EAT for $p = 0.001$
$$\text{EAT} = (1 - p) \cdot m + p \cdot p_{fault}$$
$$\text{EAT} = (1 - 0.001) \cdot 100\text{ ns} + 0.001 \cdot 8,000,000\text{ ns}$$
$$\text{EAT} = (0.999 \times 100) + 8000 = 99.9 + 8000 = 8099.9\text{ ns } \approx 8.1\text{ microseconds}$$

*Observation:* Even a 0.1% page fault rate slows down execution by a factor of 80!

##### Part 2: Find Maximum $p$ for $\text{EAT} < 200\text{ ns}$
$$200 = (1 - p) \cdot 100 + p \cdot 8,000,000$$
$$200 = 100 - 100p + 8,000,000p$$
$$100 = 7,999,900p$$
$$p = \frac{100}{7,999,900} \approx 0.0000125 = 1.25 \times 10^{-5}$$

*Answer:* To keep EAT under 200 ns, less than **1 out of every 80,000 memory accesses** ($p < 0.0000125$) can be allowed to fault.

---

## 6. Page Replacement Algorithms

When a page fault occurs and physical memory is completely full, the OS must select a **Victim Page** to evict from RAM to make room for the incoming page.

```
+-----------------------------------------------------------------------+
|                      PAGE REPLACEMENT ALGORITHMS                      |
+-------------------+-------------------------------+-------------------+
|  FIFO (Earliest)  |    LRU (Past History/Recency) |  OPT (Future Spec)|
| - Replaces oldest |   - Replaces page unused for  | - Replaces page   |
| - Suffers from    |     longest past time.        |   unused longest  |
|   Belady Anomaly  |   - Stack Algorithm (Immune)  |   in future.      |
+-------------------+-------------------------------+-------------------+
```

---

### 6.1 First-In-First-Out (FIFO)
- **Rule:** Evicts the page that was loaded into physical memory earliest (oldest arrival time).
- **Implementation:** Uses a simple FIFO Queue.
- **Anomalous Behavior:** Suffers from **Belady's Anomaly** (increasing the number of physical frames can paradoxically increase the number of page faults!).

---

### 6.2 Least Recently Used (LRU)
- **Rule:** Evicts the page that has not been referenced for the longest period of time in the past (backward-looking).
- **Implementation:** Counters or Doubly Linked Lists (Stack).
- **Properties:** Belongs to the class of **Stack Algorithms** (immune to Belady's Anomaly). Excellent real-world performance by leveraging temporal locality.

---

### 6.3 Optimal Page Replacement (OPT)
- **Rule:** Evicts the page that will **not be used for the longest period of time in the future** (forward-looking).
- **Properties:** Guarantees the **minimum possible page fault rate** for any frame allocation.
- **Implementability:** Cannot be implemented in a real operating system because it requires perfect knowledge of future instruction execution. Used as an offline theoretical benchmark.

---

### 6.4 Side-by-Side Comprehensive Comparison Numerical

#### Problem Statement
Consider the following page reference string:
$$\text{Reference String: } 4, 7, 6, 1, 7, 6, 4, 2, 1, 7, 2, 3, 4, 3, 2$$

The system has **3 physical page frames**.
Simulate the step-by-step frame state for:
1. **FIFO (First-In-First-Out)**
2. **LRU (Least Recently Used)**
3. **Optimal (OPT)**

For each algorithm, provide:
- Frame-by-frame status table showing Hits, Faults, and Replacements.
- Total Page Faults and Total Page Hits.
- Hit Ratio (%) and Fault Ratio (%).
- Explicit victim selection rules and tie-handling explanations.

*Assumptions:*
- All 3 frames are initially empty.
- Initial page loads into empty frames count as Page Faults.

---

#### Step-by-Step Simulation Traces

##### 1. First-In-First-Out (FIFO) Simulation

FIFO Queue maintains arrival order. Oldest page is popped when full.

| Step | Page Ref | Frame 1 | Frame 2 | Frame 3 | Result | Victim / Note | Cumulative Faults |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **4** | **4** | - | - | **FAULT** | Initial load | 1 |
| 2 | **7** | 4 | **7** | - | **FAULT** | Initial load | 2 |
| 3 | **6** | 4 | 7 | **6** | **FAULT** | Initial load | 3 |
| 4 | **1** | **1** | 7 | 6 | **FAULT** | Evicts 4 (Oldest) | 4 |
| 5 | **7** | 1 | 7 | 6 | **HIT** | Resident | 4 |
| 6 | **6** | 1 | 7 | 6 | **HIT** | Resident | 4 |
| 7 | **4** | 1 | **4** | 6 | **FAULT** | Evicts 7 (Oldest) | 5 |
| 8 | **2** | 1 | 4 | **2** | **FAULT** | Evicts 6 (Oldest) | 6 |
| 9 | **1** | 1 | 4 | 2 | **HIT** | Resident | 6 |
| 10 | **7** | **7** | 4 | 2 | **FAULT** | Evicts 1 (Oldest) | 7 |
| 11 | **2** | 7 | 4 | 2 | **HIT** | Resident | 7 |
| 12 | **3** | 7 | **3** | 2 | **FAULT** | Evicts 4 (Oldest) | 8 |
| 13 | **4** | 7 | 3 | **4** | **FAULT** | Evicts 2 (Oldest) | 9 |
| 14 | **3** | 7 | 3 | 4 | **HIT** | Resident | 9 |
| 15 | **2** | **2** | 3 | 4 | **FAULT** | Evicts 7 (Oldest) | 10 |

**FIFO Summary Metrics:**
- **Total References:** 15
- **Page Faults:** 10
- **Page Hits:** 5
- **Hit Ratio:** $\frac{5}{15} \times 100 = 33.33\%$
- **Fault Ratio:** $\frac{10}{15} \times 100 = 66.67\%$

---

##### 2. Least Recently Used (LRU) Simulation

Evicts the page whose last access timestamp is farthest in the past.

| Step | Page Ref | Frame 1 | Frame 2 | Frame 3 | Result | Victim / Note | Cumulative Faults |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **4** | **4** | - | - | **FAULT** | Initial load | 1 |
| 2 | **7** | 4 | **7** | - | **FAULT** | Initial load | 2 |
| 3 | **6** | 4 | 7 | **6** | **FAULT** | Initial load | 3 |
| 4 | **1** | **1** | 7 | 6 | **FAULT** | Evicts 4 (Unused longest: last at step 1) | 4 |
| 5 | **7** | 1 | 7 | 6 | **HIT** | Resident (Refreshes 7) | 4 |
| 6 | **6** | 1 | 7 | 6 | **HIT** | Resident (Refreshes 6) | 4 |
| 7 | **4** | **4** | 7 | 6 | **FAULT** | Evicts 1 (Unused longest: last at step 4) | 5 |
| 8 | **2** | 4 | **2** | 6 | **FAULT** | Evicts 7 (Unused longest: last at step 5) | 6 |
| 9 | **1** | 4 | 2 | **1** | **FAULT** | Evicts 6 (Unused longest: last at step 6) | 7 |
| 10 | **7** | **7** | 2 | 1 | **FAULT** | Evicts 4 (Unused longest: last at step 7) | 8 |
| 11 | **2** | 7 | 2 | 1 | **HIT** | Resident (Refreshes 2) | 8 |
| 12 | **3** | 7 | 2 | **3** | **FAULT** | Evicts 1 (Unused longest: last at step 9) | 9 |
| 13 | **4** | **4** | 2 | 3 | **FAULT** | Evicts 7 (Unused longest: last at step 10) | 10 |
| 14 | **3** | 4 | 2 | 3 | **HIT** | Resident (Refreshes 3) | 10 |
| 15 | **2** | 4 | 2 | 3 | **HIT** | Resident (Refreshes 2) | 10 |

**LRU Summary Metrics:**
- **Total References:** 15
- **Page Faults:** 10
- **Page Hits:** 5
- **Hit Ratio:** $\frac{5}{15} \times 100 = 33.33\%$
- **Fault Ratio:** $\frac{10}{15} \times 100 = 66.67\%$

---

##### 3. Optimal (OPT) Simulation

Evicts the page that will not be used for the longest time in the future.

| Step | Page Ref | Frame 1 | Frame 2 | Frame 3 | Result | Victim Selection Explanation | Cumulative Faults |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | **4** | **4** | - | - | **FAULT** | Initial load | 1 |
| 2 | **7** | 4 | **7** | - | **FAULT** | Initial load | 2 |
| 3 | **6** | 4 | 7 | **6** | **FAULT** | Initial load | 3 |
| 4 | **1** | 1 | 7 | **4** | **FAULT** | Frames contain {4, 7, 6}. Future accesses: 7 (step 5), 6 (step 6), 4 (step 7). Page 4's next use (step 7) is later than both 7's (step 5) and 6's (step 6), so **OPT evicts 4** $\rightarrow$ frames become {1, 7, 6}. | 4 |
| 5 | **7** | 1 | 7 | 6 | **HIT** | Resident | 4 |
| 6 | **6** | 1 | 7 | 6 | **HIT** | Resident | 4 |
| 7 | **4** | 1 | 7 | **4** | **FAULT** | Frames contain {1, 7, 6}. Future accesses: 2(8), 1(9), 7(10). 6 is **never used again**! **Evicts 6**. | 5 |
| 8 | **2** | 1 | 7 | **2** | **FAULT** | Frames contain {1, 7, 4}. Future accesses: 1(9), 7(10), 2(11), 3(12), 4(13). 4 is used farthest at step 13. **Evicts 4**. | 6 |
| 9 | **1** | 1 | 7 | 2 | **HIT** | Resident | 6 |
| 10 | **7** | 1 | 7 | 2 | **HIT** | Resident | 6 |
| 11 | **2** | 1 | 7 | 2 | **HIT** | Resident | 6 |
| 12 | **3** | **3** | 7 | 2 | **FAULT** | Frames contain {1, 7, 2}. Future accesses: 4(13), 3(14), 2(15). 1 is **never used again**! **Evicts 1**. | 7 |
| 13 | **4** | 3 | **4** | 2 | **FAULT** | Frames contain {3, 7, 2}. Future accesses: 3(14), 2(15). 7 is **never used again**! **Evicts 7**. | 8 |
| 14 | **3** | 3 | 4 | 2 | **HIT** | Resident | 8 |
| 15 | **2** | 3 | 4 | 2 | **HIT** | Resident | 8 |

**Optimal Summary Metrics:**
- **Total References:** 15
- **Page Faults:** 8
- **Page Hits:** 7
- **Hit Ratio:** $\frac{7}{15} \times 100 = 46.67\%$
- **Fault Ratio:** $\frac{8}{15} \times 100 = 53.33\%$

---

#### Side-by-Side Algorithm Performance Matrix

| Metric | FIFO | LRU | Optimal (OPT) |
| :--- | :---: | :---: | :---: |
| **Total Page Accesses** | 15 | 15 | 15 |
| **Total Page Faults** | **10** | **10** | **8 (BEST)** |
| **Total Page Hits** | **5** | **5** | **7** |
| **Hit Ratio (%)** | **33.33%** | **33.33%** | **46.67%** |
| **Fault Ratio (%)** | **66.67%** | **66.67%** | **53.33%** |
| **Belady Anomaly Vulnerability** | YES | NO (Stack) | NO (Stack) |
| **Real OS Implementability** | YES | YES | NO (Theoretical) |

---

## 7. University Exam Question Bank with Complete Model Answers

### 7.1 Short-Answer Questions (5 Marks)

#### Q1. Explain the difference between Internal and External Fragmentation. How can each be resolved?
**Answer:**
1. **Internal Fragmentation:**
   - **Definition:** Unused memory space trapped inside an allocated partition.
   - **Cause:** Occurs when fixed-sized partitions are assigned to processes requesting less memory than the partition capacity.
   - **Solution:** Replaced by dynamic partitioning schemes or smaller page sizes in virtual memory.
2. **External Fragmentation:**
   - **Definition:** Unused memory space scattered outside allocated regions across physical RAM.
   - **Cause:** Occurs in dynamic partitioning when processes are allocated and deallocated over time, leaving scattered free holes that are individually too small for incoming jobs.
   - **Solution:** **Compaction** (shuffling RAM contents) or non-contiguous allocation via **Paging**.

---

#### Q2. Explain Belady's Anomaly. Which page replacement algorithm suffers from it?
**Answer:**
1. **Definition:** Belady's Anomaly is the counterintuitive phenomenon where increasing the number of physical memory frames allocated to a process causes an **increase in the total number of page faults** for a given page reference string.
2. **Vulnerable Algorithm:** **First-In-First-Out (FIFO)** suffers from Belady's Anomaly because it evicts pages purely based on arrival order without regard to reference recency or frequency.
3. **Immune Algorithms:** Algorithms that belong to the class of **Stack Algorithms** (such as **LRU** and **Optimal**) are mathematically immune to Belady's Anomaly because the set of pages resident in $N$ frames is always a strict subset of the pages resident in $N+1$ frames.

---

### 7.2 Long-Answer / Essay Questions (10 Marks)

#### Q3. Compare Paging and Segmentation in detail across structure, address translation, fragmentation, and user perception.
**Answer:**

**1. Basic Concept:**
- **Paging** divides physical memory into fixed-size **frames** and logical memory into equal-size **pages**, so a process's address space can be scattered across non-contiguous frames.
- **Segmentation** divides a program into **variable-size logical units** (code, data, stack, functions) called segments, each mapped to a contiguous block of physical memory.

**2. Address Translation:**
- Paging splits a logical address into $(p, d)$ — page number and offset — and uses a **Page Table** to map $p \to f$ (frame number), giving physical address $(f \times \text{Page Size}) + d$.
- Segmentation uses a two-part logical address $\langle s, d \rangle$ — segment number and offset — and a **Segment Table** storing $(\text{base}, \text{limit})$ per segment, giving physical address $\text{base} + d$ provided $d < \text{limit}$.

**3. Comprehensive Comparison Table:**

| Parameter | Paging | Segmentation |
| :--- | :--- | :--- |
| **User/Programmer View** | Linear, contiguous address space (invisible partitioning). | Modular, variable-length functional modules (matches programmer view). |
| **Block Size** | Fixed-size blocks (e.g., 4 KB). | Variable-size blocks. |
| **Hardware Division** | Implemented strictly by OS hardware (MMU). | Software-driven logical compiler/linker structure. |
| **Address Structure** | Single integer split into $p$ and $d$ by bit manipulation. | Two explicit components $\langle s, d \rangle$. |
| **Fragmentation** | Suffers from **Internal Fragmentation** (last page); no external fragmentation. | Suffers from **External Fragmentation**; no internal fragmentation. |
| **Table Entries** | Page Table contains Frame Number ($f$) + control bits. | Segment Table contains Base Address + Limit Length + control bits. |
| **Protection & Sharing** | Easy to protect/share fixed pages. | Natural alignment for sharing functional code modules. |

**4. Conclusion:** Paging is preferred for efficient, fragmentation-tolerant memory utilization at the hardware level, while segmentation is preferred when the logical structure of a program (functions, arrays, modules) needs to be reflected directly in memory protection and sharing. Many real systems (e.g., x86 protected mode) combine both, segmenting the address space first and then paging each segment.

---

## 8. Syllabus Coverage & Numerical Types Checklist

### Syllabus Topic Coverage Audit
- [x] Memory Management Requirements (Relocation, Protection, Sharing, Logical & Physical Org.)
- [x] Fixed vs. Variable/Dynamic Partitioning
- [x] Internal vs. External Fragmentation & Compaction
- [x] Partition Allocation Strategies (First Fit, Best Fit, Worst Fit, Next Fit)
- [x] The Buddy System (Binary splitting, allocation, deallocation, coalescing)
- [x] Paging Principles, Pages & Frames, Page Table Structure
- [x] Logical-to-Physical Address Translation ($p, d \rightarrow f, d$)
- [x] Hardware Support: TLB & Effective Access Time (EAT)
- [x] Protection, Valid/Invalid Bits, Shared Reentrant Code
- [x] Segmentation, Segment Table (Base, Limit), Hardware Bounds Checks
- [x] Virtual Memory, Demand Paging, Page Fault Handling Pipeline
- [x] Page Replacement Algorithms (FIFO, LRU, OPT)

---

### Numerical Problem Types Mastered
- [x] **Placement Strategies Numerical:** First Fit, Best Fit, Worst Fit, Next Fit memory layout & hole state traces.
- [x] **Buddy System Numerical:** Power-of-two block size allocation, recursive binary splitting, internal fragmentation, and recursive buddy coalescing.
- [x] **Paging Bit-Math Numerical:** Address bit splits ($m, p, d$), total pages $2^p$, and Page Table Size ($2^p \times \text{PTE}$).
- [x] **Paging Address Translation Numerical:** Logical-to-Physical translation using Division/Modulo ($p = \lfloor \frac{A}{S} \rfloor$, $d = A \pmod S$) and Page Table lookup.
- [x] **TLB Effective Access Time Numerical:** $\text{EAT} = \alpha(\epsilon + m) + (1-\alpha)(\epsilon + 2m)$ for varying hit ratios.
- [x] **Segmentation Bounds Check Numerical:** Physical address formation ($\text{Base} + d$) with explicit limit checks ($d < \text{Limit}$).
- [x] **Demand Paging EAT Numerical:** $\text{EAT} = (1-p)m + p \cdot p_{fault}$ and maximum allowable page fault probability.
- [x] **Side-by-Side Page Replacement Numerical:** 15-access reference string simulation for FIFO, LRU, and OPT with hit/fault ratios and victim explanations.

---
