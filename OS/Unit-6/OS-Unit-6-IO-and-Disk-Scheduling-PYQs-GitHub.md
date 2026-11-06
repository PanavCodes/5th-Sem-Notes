# Operating Systems (OS) - Unit 6: I/O Management and Disk Scheduling
## Solved Previous Year Questions (PYQ) & Exam Preparation Guide
### Mapped to Course Outcome CO-3 | Semester End Examinations & Re-Examinations

---

## SECTION 1: UNIT 6 EXAM PATTERN & MARKS WEIGHTAGE

Unit 6 ("I/O Management and Disk Scheduling") carries a total weightage of **15 to 20 Marks** in end-semester examinations. The question paper structure consistently includes:

1. **Compulsory 10-Mark Disk Scheduling Numerical**: Solved using FCFS, SSTF, SCAN, C-SCAN, LOOK, or C-LOOK algorithms.
2. **10-Mark / 5-Mark Descriptive Questions**: Covering I/O Buffering (Single, Double, Circular), Organization of I/O Function, and Direct Memory Access (DMA).
3. **5-Mark Conceptual Short-Answer Questions**: Disk performance parameters (Seek Time, Rotational Latency, Access Time) and I/O operating modes (Blocking, Non-Blocking, Asynchronous).

---

## SECTION 2: 10-MARK MASTER PYQ QUESTIONS & SOLVED MODEL ANSWERS

### QUESTION 1 [10 MARKS] — (AY 2024–2025 Final Exam & AY 2023–2024 Final Exam)

**Question Statement:**
A disk drive has 5000 cylinders, numbered 0 to 4999. The disk request queue in FIFO order is:
`2069, 1212, 2296, 2800, 544, 1618, 356, 1523`
The read/write head is currently positioned at cylinder **2150**.

Calculate the total head movement (in cylinders) required to service all requests using the following disk scheduling algorithms:
1. **FCFS (First-Come, First-Served)**
2. **SCAN (Elevator Algorithm)**, assuming the head is initially moving towards the highest cylinder (4999).
3. **C-SCAN (Circular SCAN)**, assuming the head is initially moving towards the highest cylinder (4999).
4. **LOOK**, assuming the head is initially moving towards the highest cylinder (4999).

Compare the performance of the algorithms based on total head movement and discuss the major factor of comparison.

---

#### MODEL ANSWER & STEP-BY-STEP SOLUTION

##### Problem Parameters:
- Total Cylinders: 5000 (numbered 0 to 4999)
- Request Queue: [2069, 1212, 2296, 2800, 544, 1618, 356, 1523]
- Initial Head Position: 2150
- Initial Direction: Moving Right / Towards 4999 (Increasing)

---

#### PART I: FCFS (First-Come, First-Served) Algorithm

FCFS services I/O requests strictly in the order they arrive in the queue.

* **Service Sequence**: 2150 -> 2069 -> 1212 -> 2296 -> 2800 -> 544 -> 1618 -> 356 -> 1523

* **Step-by-Step Head Movements**:
  1. From 2150 to 2069: |2069 - 2150| = 81 cylinders
  2. From 2069 to 1212: |1212 - 2069| = 857 cylinders
  3. From 1212 to 2296: |2296 - 1212| = 1084 cylinders
  4. From 2296 to 2800: |2800 - 2296| = 504 cylinders
  5. From 2800 to 544:  |544 - 2800| = 2256 cylinders
  6. From 544 to 1618:  |1618 - 544| = 1074 cylinders
  7. From 1618 to 356:  |356 - 1618| = 1262 cylinders
  8. From 356 to 1523:  |1523 - 356| = 1167 cylinders

* **Total Head Movement (FCFS)** = 81 + 857 + 1084 + 504 + 2256 + 1074 + 1262 + 1167 = **7585 Cylinders**

---

#### PART II: SCAN Algorithm (Direction: Towards 4999)

The SCAN (Elevator) algorithm moves the head in the current direction servicing all requests until it reaches the physical disk boundary (4999), then reverses direction.

* **Sorting Requests Relative to Initial Head (2150)**:
  - Requests greater than 2150 (Right): 2296, 2800
  - Requests less than 2150 (Left): 2069, 1618, 1523, 1212, 544, 356

* **Service Sequence**: 2150 -> 2296 -> 2800 -> 4999 (Boundary) -> 2069 -> 1618 -> 1523 -> 1212 -> 544 -> 356

* **Step-by-Step Head Movements**:
  - Right Sweep (2150 to 4999): 4999 - 2150 = 2849 cylinders
  - Left Sweep (4999 to 356): 4999 - 356 = 4643 cylinders

* **Total Head Movement (SCAN)** = 2849 + 4643 = **7492 Cylinders**

---

#### PART III: C-SCAN Algorithm (Direction: Towards 4999)

C-SCAN moves the head servicing requests towards cylinder 4999. Upon reaching 4999, it jumps back to cylinder 0 without servicing requests during the return jump, then resumes scanning right.

* **Service Sequence**: 2150 -> 2296 -> 2800 -> 4999 (Boundary) -> 0 (Boundary) -> 356 -> 544 -> 1212 -> 1523 -> 1618 -> 2069

* **Step-by-Step Head Movements**:
  - Leg 1 (2150 to 4999): 4999 - 2150 = 2849 cylinders
  - Circular Jump (4999 to 0): 4999 - 0 = 4999 cylinders
  - Leg 2 (0 to 2069): 2069 - 0 = 2069 cylinders

* **Total Head Movement (C-SCAN)** = 2849 + 4999 + 2069 = **9917 Cylinders**

---

#### PART IV: LOOK Algorithm (Direction: Towards 4999)

LOOK functions like SCAN, but reverses direction immediately after servicing the highest pending request (2800), without traveling to physical boundary 4999.

* **Service Sequence**: 2150 -> 2296 -> 2800 -> 2069 -> 1618 -> 1523 -> 1212 -> 544 -> 356

* **Step-by-Step Head Movements**:
  - Right Leg (2150 to 2800): 2800 - 2150 = 650 cylinders
  - Left Leg (2800 to 356): 2800 - 356 = 2444 cylinders

* **Total Head Movement (LOOK)** = 650 + 2444 = **3094 Cylinders**

---

#### COMPARISON & PERFORMANCE DISCUSSION

| Algorithm | Service Path Trajectory | Total Head Movement | Efficiency Rank |
| :--- | :--- | :---: | :---: |
| **LOOK** | 2150 -> 2800 -> 356 | **3094 Cylinders** | **1st (Most Efficient)** |
| **SCAN** | 2150 -> 4999 -> 356 | **7492 Cylinders** | **2nd** |
| **FCFS** | 2150 -> 2069 -> ... -> 1523 | **7585 Cylinders** | **3rd** |
| **C-SCAN** | 2150 -> 4999 -> 0 -> 2069 | **9917 Cylinders** | **4th** |

##### Major Factors of Comparison:
1. **Boundary Traversal Overhead**: SCAN travels all the way to physical boundary 4999 even though no request exists beyond 2800. LOOK eliminates this wasted movement, saving 4398 cylinders compared to SCAN (3094 vs 7492).
2. **Circular Return Jump Cost**: C-SCAN incurs an extra 4999-cylinder reset jump to provide uniform wait times across all tracks, making its total head movement count higher in static batches.
3. **Fairness vs. Efficiency**: FCFS is completely fair and avoids starvation, but causes wild head swings (7585 cylinders). LOOK achieves optimal efficiency while maintaining bounded waiting time.

---

### QUESTION 2 [10 MARKS] — (Re-Exam 2022–2023 & 2023–2024 PYQ)

**Question Statement:**
Suppose that a disk drive has 200 cylinders numbered 0 to 199. The queue of pending requests in FIFO order is:
`98, 183, 37, 122, 14, 124, 65, 67`
The disk head is currently positioned at cylinder **53** and is moving towards cylinder **0** (Left).

Calculate the total head movement (in cylinders) for:
1. FCFS
2. SSTF
3. SCAN
4. C-SCAN
5. LOOK
6. C-LOOK

---

#### MODEL ANSWER & STEP-BY-STEP SOLUTION

##### Problem Parameters:
- Disk Range: 0 to 199 (200 cylinders total)
- Request Queue: [98, 183, 37, 122, 14, 124, 65, 67]
- Initial Head Position: 53
- Initial Direction: Moving Towards 0 (Left / Decreasing)

---

#### Detailed Calculations per Algorithm:

##### 1. FCFS Algorithm
- **Sequence**: 53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67
- **Movements**: |98-53| + |183-98| + |37-183| + |122-37| + |14-122| + |124-14| + |65-124| + |67-65|
- **Calculation**: 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = **640 Cylinders**

##### 2. SSTF (Shortest Seek Time First) Algorithm
- **Closest Selection from Head (53)**:
  - 53 to 65 (diff 12)
  - 65 to 67 (diff 2)
  - 67 to 37 (diff 30)
  - 37 to 14 (diff 23)
  - 14 to 98 (diff 84)
  - 98 to 122 (diff 24)
  - 122 to 124 (diff 2)
  - 124 to 183 (diff 59)
- **Sequence**: 53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183
- **Calculation**: 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = **236 Cylinders**

##### 3. SCAN Algorithm (Direction: Left towards 0)
- Moves Left to 0, then reverses Right to 183.
- **Sequence**: 53 -> 37 -> 14 -> 0 (Boundary) -> 65 -> 67 -> 98 -> 122 -> 124 -> 183
- **Calculation**: (53 - 0) + (183 - 0) = 53 + 183 = **236 Cylinders**

##### 4. C-SCAN Algorithm (Direction: Left towards 0)
- Moves Left to 0, jumps to boundary 199, then moves Left servicing remaining requests.
- **Sequence**: 53 -> 37 -> 14 -> 0 (Boundary) -> 199 (Boundary) -> 183 -> 124 -> 122 -> 98 -> 67 -> 65
- **Calculation**: (53 - 0) + (199 - 0) + (199 - 65) = 53 + 199 + 134 = **386 Cylinders**

##### 5. LOOK Algorithm (Direction: Left towards 0)
- Moves Left to lowest request 14, then reverses Right to highest request 183.
- **Sequence**: 53 -> 37 -> 14 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183
- **Calculation**: (53 - 14) + (183 - 14) = 39 + 169 = **208 Cylinders**

##### 6. C-LOOK Algorithm (Direction: Left towards 0)
- Moves Left to 14, jumps directly to highest request 183, then moves Left to 65.
- **Sequence**: 53 -> 37 -> 14 -> 183 -> 124 -> 122 -> 98 -> 67 -> 65
- **Calculation**: (53 - 14) + (183 - 14) + (183 - 65) = 39 + 169 + 118 = **326 Cylinders**

---

#### SUMMARY COMPARISON TABLE

| Algorithm | Service Sequence | Total Seek Time | Performance Rank |
| :--- | :--- | :---: | :---: |
| **LOOK** | 53 -> 37 -> 14 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183 | **208 Cylinders** | **1st (Best)** |
| **SSTF** | 53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183 | **236 Cylinders** | **2nd** |
| **SCAN** | 53 -> 37 -> 14 -> 0 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183 | **236 Cylinders** | **2nd** |
| **C-LOOK** | 53 -> 37 -> 14 -> 183 -> 124 -> 122 -> 98 -> 67 -> 65 | **326 Cylinders** | **4th** |
| **C-SCAN** | 53 -> 37 -> 14 -> 0 -> 199 -> 183 -> 124 -> 122 -> 98 -> 67 -> 65 | **386 Cylinders** | **5th** |
| **FCFS** | 53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67 | **640 Cylinders** | **6th (Worst)** |

---

### QUESTION 3 [10 MARKS] — (December 2016 & Repeated in PYQ)

**Question Statement:**
What is I/O Buffering? Explain Single Buffering, Double Buffering (Buffer Swapping), and Circular Buffering in detail with neat diagrams, working mechanics, and execution time performance formulas.

---

#### MODEL ANSWER

##### 1. Definition and Purpose of I/O Buffering
I/O Buffering is the operating system technique of allocating a region of kernel main memory to temporarily store data transferred between I/O devices and user process memory.

**Primary Objectives of Buffering**:
1. **Speed Mismatch**: Bridges the execution speed gap between fast CPUs and slow peripheral hardware.
2. **Transfer Unit Mismatch**: Adapts between character-stream I/O (e.g., keyboards) and block-stream storage (e.g., disk sectors).
3. **Copy Semantics**: Prevents application race conditions by ensuring user memory can be modified without corrupting pending asynchronous background I/O writes.

---

##### 2. Classification of I/O Buffering Schemes & Mathematical Performance Analysis

Let:
- **T** = Time required to input a block of data from device into the kernel buffer.
- **C** = Time required by the CPU to process/compute the data block once in memory.
- **M** = Time required to copy/move the data block from kernel memory to user process memory.

---

###### Scheme A: No Buffering
Data is transferred directly between the peripheral device and user process memory space. The process blocks completely during both input transfer and computation.

- **Total Execution Time per Block** = **T + C**

---

###### Scheme B: Single Buffering
The OS allocates a single kernel memory buffer for the I/O request. The device fills the kernel buffer (time T). The OS moves the block to user space (time M), and the CPU processes it (time C) while the device concurrently reads the next block (time T).

- **Total Execution Time per Block** = **max(T, C) + M**

---

###### Scheme C: Double Buffering (Dual Buffering / Buffer Swapping)
The OS assigns two kernel buffers (Buffer 1 and Buffer 2). While the I/O device fills Buffer 1 (time T), the user process reads and computes data from Buffer 2 (time C + M). Once both operations finish, the two buffers swap roles.

- **Total Execution Time per Block** = **max(T, C + M)**
- *Note*: If memory transfer time M is negligible, Execution Time = **max(T, C)**.
- **Key Advantage**: If T <= C, the I/O device runs continuously at full hardware speed without pausing.

---

###### Scheme D: Circular Buffering
When an application generates heavy, unpredictable bursts of I/O, two buffers may be insufficient. The OS allocates a bounded queue of **N kernel buffers** arranged in a circular ring buffer (producer-consumer architecture).

- **Performance**: Smooths out bursty traffic as long as the average processing rate exceeds the average arrival rate.

---

##### 3. Master Summary Comparison Table

| Buffering Scheme | Kernel Buffers Allocated | Parallel Processing Capability | Execution Time per Block Formula | Primary Use Case |
| :--- | :---: | :--- | :---: | :--- |
| **No Buffering** | 0 | None (Sequential) | **T + C** | Direct hardware control, dedicated real-time tasks |
| **Single Buffering** | 1 | Overlaps input T with process computation C | **max(T, C) + M** | Standard character devices, line printers |
| **Double Buffering** | 2 | Overlaps input T with process computation C and memory move M | **max(T, C + M)** | High-speed block devices, sequential file processing |
| **Circular Buffering** | N (Ring queue) | Handles rapid I/O bursts across N buffers | Bounded queue smoothing | Streaming media, network packet processing |

---

### QUESTION 4 [10 MARKS] — (AY 2023–2024 & TechNeo PYQ)

**Question Statement:**
Explain the three fundamental techniques for performing I/O operations: Programmed I/O, Interrupt-Driven I/O, and Direct Memory Access (DMA). Discuss the evolutionary steps of the I/O function.

---

#### MODEL ANSWER

##### 1. Three Fundamental I/O Techniques

###### A. Programmed I/O (Polling / Busy-Waiting)
In Programmed I/O, the CPU issues an I/O command to the device controller and enters a busy-wait polling loop, constantly checking the controller's Status Register until the device completes the operation.

- **Working**: CPU writes command -> Loops checking Status Register -> Reads data byte into CPU register -> Writes byte to RAM.
- **Drawback**: Extremely inefficient. Wastes millions of CPU clock cycles spinning in polling loops.

---

###### B. Interrupt-Driven I/O
The CPU issues an I/O command, saves process state, and switches to executing other processes. When data is ready, the device controller asserts a hardware Interrupt Request (IRQ) line. The CPU catches the interrupt, executes the Interrupt Service Routine (ISR) to transfer the byte to RAM, and resumes the process.

- **Working**: CPU issues command -> Switches process -> IRQ asserted -> ISR transfers byte -> Returns context.
- **Drawback**: Generating a hardware interrupt for every single byte creates excessive context-switch overhead for high-speed devices.

---

###### C. Direct Memory Access (DMA)
DMA offloads bulk data transfers to an independent hardware controller: the DMA Controller (DMAC). The CPU programs the DMAC with the physical RAM address, byte count, and control mode, then resumes work. The DMAC transfers the entire block of data directly between the device and RAM over the system bus, issuing a **single interrupt** upon completion.

---

##### 2. Comprehensive Comparison Table

| Criterion | Programmed I/O | Interrupt-Driven I/O | Direct Memory Access (DMA) |
| :--- | :--- | :--- | :--- |
| **CPU Involvement** | Continuous CPU polling loop | CPU handles every byte/word via ISR | CPU setup & single completion interrupt |
| **Hardware Required** | Basic Controller Registers | Interrupt Controller (PIC/APIC) | DMA Controller (DMAC) |
| **Data Transfer Path** | Device -> CPU -> Memory | Device -> CPU -> Memory | Device -> System Bus -> Memory (Direct) |
| **Context Switching Overhead** | None (Busy-waits) | Very High (1 interrupt per byte/word) | Minimal (1 interrupt per block) |
| **Target Devices** | Very simple, slow peripherals | Character devices (Keyboard, Mouse) | High-speed block devices (Disk, SSD, NIC) |

---

##### 3. Evolutionary Steps of the I/O Function
1. **Direct CPU Control**: Processor directly controls physical hardware lines.
2. **Programmed I/O Added**: Device controller added; CPU uses polling.
3. **Interrupt-Driven I/O Added**: Controller uses IRQ lines; CPU avoids polling.
4. **Direct Memory Access (DMA)**: DMAC takes over block memory transfers.
5. **I/O Channel**: Specialized I/O processor executes I/O programs stored in RAM.
6. **I/O Processor**: Independent computer module with dedicated local memory manages I/O tasks.

---

## SECTION 3: 5-MARK CORE PYQ QUESTIONS & SOLVED MODEL ANSWERS

### QUESTION 5 [5 MARKS] — (AY 2024–2025 & FYIT PYQ)

**Question Statement:**
Write a detailed short note on Direct Memory Access (DMA). Explain its hardware registers, handshaking mechanism, and transfer modes.

---

#### MODEL ANSWER

##### 1. Definition and DMAC Structure
Direct Memory Access (DMA) allows high-speed peripheral controllers to transfer blocks of data directly to or from main memory without routing data through CPU registers.

**DMAC Registers**:
1. **Address Register**: Holds physical memory starting location.
2. **Byte / Word Count Register (C)**: Tracks remaining bytes to transfer.
3. **Control Register**: Specifies transfer direction (Read/Write) and mode.

---

##### 2. Handshaking Lines & Transfer Steps
- **DRQ (DMA Request)**: Asserted by device controller when a data word is ready in its local buffer.
- **DACK (DMA Acknowledge)**: Asserted by DMAC to signal that the system bus is acquired and data transfer is occurring.

**Step Sequence**:
1. CPU writes Address, Count, and Control bits into DMAC registers.
2. Device fills buffer and asserts **DRQ** to DMAC.
3. DMAC requests System Bus from CPU.
4. DMAC asserts **DACK** and transfers word directly to RAM.
5. DMAC increments Address and decrements Count C.
6. Once C = 0, DMAC releases bus and issues **completion interrupt** to CPU.

---

##### 3. DMA Transfer Modes

| Mode | Mechanism | Trade-Off |
| :--- | :--- | :--- |
| **Cycle Stealing** | DMAC transfers 1 word per bus request, then returns bus to CPU. | Does not lock CPU out of RAM; higher arbitration overhead. |
| **Burst Mode** | DMAC holds system bus continuously until the entire block is transferred. | Maximum throughput; locks CPU out of RAM during burst. |
| **Fly-By Mode** | Data moves directly between device and RAM over bus without passing through DMAC. | Requires 1 bus cycle per word; needs hardware support. |

---

### QUESTION 6 [5 MARKS] — (AY 2024–2025 Final Exam Q1d)

**Question Statement:**
Compare blocking, non-blocking, and asynchronous I/O operations by explaining how each works in practice, providing examples to illustrate the differences.

---

#### MODEL ANSWER

| I/O Operating Mode | Execution Mechanics | Practical Application / Example |
| :--- | :--- | :--- |
| **Blocking I/O** | The user process execution is completely suspended (moved to Waiting state) until the I/O system call completes and returns data. | Reading keyboard input via `scanf()` or reading disk files via standard `read()`. |
| **Non-Blocking I/O** | The system call returns immediately with whatever data is ready or returns an error code (e.g., `EWOULDBLOCK`). Process continues running and polls. | Network socket reads using `recv()` with `O_NONBLOCK` flag set. |
| **Asynchronous I/O** | The system call initiates I/O and returns immediately. The process continues execution. OS notifies the process via signal or callback upon full completion. | POSIX Asynchronous I/O (`aio_read()`, `aio_write()`) used in high-performance web servers (Node.js, NGINX). |

---

### QUESTION 7 [5 MARKS] — (Special Re-Exam 2022–2023 Q5b)

**Question Statement:**
Define the following disk performance parameters and write their mathematical formulas: Seek Time, Rotational Latency, Transfer Time, and Total Access Time.

---

#### MODEL ANSWER

##### 1. Seek Time (Ts)
The time required for the disk actuator arm to move the read/write head to the specified cylinder/track.
- **Formula**: `Ts = (m * n) + s`
  - `m` = Hardware constant factor
  - `n` = Number of tracks traversed
  - `s` = Arm startup time

##### 2. Rotational Latency (Tr)
The time required for the target sector to rotate underneath the read/write head once positioned over the track.
- **Formula (Average)**: `Average Tr = 0.5 * (60 / RPM) seconds = (30 / RPM) seconds`
  - *Example for 7200 RPM*: `Tr = 30 / 7200 = 0.004167 seconds = 4.17 ms`.

##### 3. Transfer Time (Tt)
The time required to transfer data to or from the disk surface as it rotates under the head.
- **Formula**: `Tt = b / (r * N)`
  - `b` = Bytes to transfer
  - `N` = Bytes per track
  - `r` = Rotational speed in revolutions per second (`RPM / 60`)

##### 4. Total Access Time (Ta)
- **Formula**: `Total Access Time (Ta) = Seek Time (Ts) + Rotational Latency (Tr) + Transfer Time (Tt)`

---

### QUESTION 8 [5 MARKS] — (Lab Manual & Exam Assessment Questions)

**Question Statement:**
Answer the following conceptual assessment questions regarding disk scheduling algorithms:
1. What is the key difference between SCAN and LOOK?
2. Which algorithm provides the most uniform wait time for requests?
3. What is the main disadvantage of C-SCAN?
4. Which algorithm is best suited for real-time systems and why?

---

#### MODEL ANSWER

1. **Key Difference between SCAN and LOOK**:
   - **SCAN** moves the head all the way to the physical disk boundary (cylinder 0 or 199/4999), even if no pending requests exist at those boundary tracks.
   - **LOOK** "looks ahead" and reverses direction immediately after servicing the last pending request in that direction, saving unnecessary boundary traversal.

2. **Algorithm with Most Uniform Wait Time**:
   - **C-SCAN (and C-LOOK)**. By scanning in one direction only and resetting to cylinder 0 without servicing on the return trip, C-SCAN treats cylinders as a circular loop, offering equal response frequency to all tracks.

3. **Main Disadvantage of C-SCAN**:
   - Extra head movement distance incurred during the full-span reset jump from cylinder Max back to 0, which inflates total seek time in static request batches.

4. **Best Algorithm for Real-Time Systems**:
   - **Deadline Scheduling / Priority C-SCAN**. Real-time systems require guaranteed upper bounds on latency. Standard SSTF can cause indefinite starvation for distant tracks, whereas C-SCAN queues with strict deadlines guarantee bounded response times.

---

## SECTION 4: PYQ RAPID REVISION MATRIX & FORMULA SHEET

### 1. Disk Scheduling Algorithms Quick Comparison

| Algorithm | Trajectory Behavior | Boundary Trip? | Starvation Risk? | Overall Efficiency Rank |
| :--- | :--- | :---: | :---: | :---: |
| **LOOK** | Sweeps to furthest pending request, then reverses | **No** | Low | **1st (Most Efficient)** |
| **SSTF** | Always chooses closest pending request | **No** | **HIGH** | **2nd** |
| **SCAN** | Sweeps to physical disk boundary (0/Max), then reverses | **Yes** | None | **3rd** |
| **C-LOOK** | Sweeps to furthest request, jumps to lowest request | **No** | None | **4th** |
| **C-SCAN** | Sweeps to Max boundary, jumps to 0 boundary | **Yes** | None | **5th** |
| **FCFS** | Services requests strictly in arrival order | **No** | None | **6th (Worst)** |

---

### 2. Key Master Formulas

```
1. Single Buffering Execution Time = max(T, C) + M
2. Double Buffering Execution Time = max(T, C + M)
3. Seek Time (Ts) = (m * n) + s
4. Average Rotational Latency (Tr) = (30 / RPM) seconds
5. Transfer Time (Tt) = b / (r * N)
6. Total Access Time (Ta) = Ts + Tr + Tt
```
