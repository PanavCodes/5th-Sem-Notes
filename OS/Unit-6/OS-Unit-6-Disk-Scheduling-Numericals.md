# Operating Systems (OS) - Unit 6: Disk Scheduling & I/O Numerical Master Guide

## Comprehensive Term-End Examination Numerical Solutions & Formula Guide
### Course Outcome: CO-3 (Simulate Memory Management, I/O Management, and File Management Strategies)

---

## 1. MASTER FORMULAS & TERM-END SOLUTION FRAMEWORK

Disk scheduling and I/O performance numericals form a major component of university term-end examinations, typically carrying 10 marks for scheduling algorithms and 5 marks for disk hardware metrics. Mastering these problems requires a clear understanding of fundamental formulas, systematic step-by-step presentation, and shortcuts for fast verification under exam conditions.

### 1.1 Disk Performance Parameter Formulas

Secondary storage performance is measured by the total time required to locate and transfer data from a physical disk surface into main memory.

#### A. Seek Time ($T_s$)
Seek time is the time required for the disk actuator arm to move the read/write head to the target cylinder or track.
$$T_s = (m \times n) + s$$
Where:
* $m$ = Constant hardware factor (ms per cylinder).
* $n$ = Number of cylinders traversed by the read/write head ($n = |\text{Target Cylinder} - \text{Current Cylinder}|$).
* $s$ = Startup time of the actuator arm.

#### B. Rotational Latency ($T_r$)
Rotational latency is the delay spent waiting for the requested sector to rotate under the read/write head once the head reaches the designated track.
* **Full Revolution Time ($T_{rev}$):** The time for one complete $360^\circ$ rotation.
$$T_{rev} = \frac{60}{\text{RPM}} \text{ seconds}$$
* **Average Rotational Latency ($T_{r,\text{avg}}$):** On average, the target sector is located half a revolution away from the head position upon arrival.
$$T_{r,\text{avg}} = \frac{1}{2} \times T_{rev} = \frac{30}{\text{RPM}} \text{ seconds} = \frac{30,000}{\text{RPM}} \text{ ms}$$

#### C. Transfer Time ($T_t$)
Transfer time is the duration required to read or write the data bytes as the sector passes beneath the read/write head.
$$T_t = \frac{b}{r \times N} = \frac{\text{Bytes to Transfer}}{\text{Data Transfer Rate}}$$
Where:
* $b$ = Number of bytes to transfer.
* $r$ = Rotational speed in revolutions per second ($r = \text{RPM} / 60$).
* $N$ = Number of bytes per track.

#### D. Total Access Time ($T_a$)
Total access time represents the sum of all individual delay components.
$$T_a = T_s + T_r + T_t$$

---

### 1.2 Disk Scheduling Algorithm Mechanics

When multiple I/O requests arrive, the operating system reorders them using scheduling algorithms to minimize total head movement (seek distance).

1. **FCFS (First-Come, First-Served):** Services requests strictly in arrival order. It is completely fair with zero starvation risk, but yields high seek times due to wild head swings.
2. **SSTF (Shortest Seek Time First):** Greedily selects the pending request closest to the current head position. It minimizes immediate seek distance, but can cause severe starvation for distant requests under heavy loads.
3. **SCAN (Elevator Algorithm):** Sweeps in one direction servicing all requests until it hits the physical disk boundary ($0$ or $\text{Max}$), then reverses direction to service remaining requests.
4. **C-SCAN (Circular SCAN):** Sweeps in one direction servicing requests to the physical disk boundary ($0$ or $\text{Max}$), then performs an immediate reset jump to the opposite boundary ($0$ or $\text{Max}$) without servicing requests on the return trip, and sweeps again.
5. **LOOK:** Sweeps in one direction servicing requests up to the furthest pending request in that direction, then reverses direction immediately without making an unnecessary trip to the physical disk boundary.
6. **C-LOOK (Circular LOOK):** Sweeps in one direction servicing requests to the furthest pending request, then jumps directly to the lowest/furthest pending request at the opposite end without hitting boundaries, and resumes scanning.

---

### 1.3 Term-End Exam Shortcuts & Verification Tricks

Using shortcut formulas allows you to verify your step-by-step arithmetic calculations within seconds during an exam.

#### Shortcut 1: SCAN Total Seek Distance Formula
If the head is at $\text{Head}_{start}$ moving towards boundary $B_{start}$ (e.g., cylinder $0$ or $199$), and the furthest request in the opposite direction is $R_{opposite}$:
$$\text{Total Seek (SCAN)} = |B_{start} - \text{Head}_{start}| + |B_{start} - R_{opposite}|$$

#### Shortcut 2: LOOK Total Seek Distance Formula
If the head is at $\text{Head}_{start}$, moving towards $R_{same\_extreme}$ (the furthest request in the initial direction), and $R_{opposite\_extreme}$ is the furthest request in the reverse direction:
$$\text{Total Seek (LOOK)} = |R_{same\_extreme} - \text{Head}_{start}| + |R_{same\_extreme} - R_{opposite\_extreme}|$$

#### Shortcut 3: C-SCAN Total Seek Distance Formula
If the head is at $\text{Head}_{start}$ moving towards physical boundary $B_{max}$, resets to boundary $0$, and $R_{last}$ is the highest request before $\text{Head}_{start}$:
$$\text{Total Seek (C-SCAN)} = (B_{max} - \text{Head}_{start}) + (B_{max} - 0) + (R_{last} - 0)$$

#### Shortcut 4: C-LOOK Total Seek Distance Formula
If the head is at $\text{Head}_{start}$ moving towards $R_{highest\_right}$, jumps back to $R_{lowest\_left}$, and services up to $R_{last\_before\_head}$:
$$\text{Total Seek (C-LOOK)} = (R_{highest\_right} - \text{Head}_{start}) + (R_{highest\_right} - R_{lowest\_left}) + (R_{last\_before\_head} - R_{lowest\_left})$$

---

## 2. PYQ CATEGORY 1: 5000-CYLINDER LARGE DISK SYSTEMS (10 MARKS EACH)

Large disk systems featuring 5000 cylinders (numbered 0 to 4999) appear frequently in university final examinations. In these systems, boundary-traversing algorithms (SCAN/C-SCAN) show significant performance differences compared to request-bounded algorithms (LOOK/C-LOOK).

### 2.1 Problem 1A (Final Exam AY 2024–2025)

#### Problem Statement
A disk queue has requests on cylinders `2069, 1212, 2296, 2800, 544, 1618, 356, 1523`. The disk head is currently positioned at cylinder `2150`. The disk has 5000 cylinders numbered from `0 to 4999`. The initial head movement is towards higher-numbered cylinders (Right / Increasing). Calculate the total head movement (in cylinders) required to service all requests using **FCFS, SSTF, SCAN, C-SCAN, LOOK, and C-LOOK**.

#### Step 1: Initial Setup & Sorting
* **Disk Range:** $0 \text{ to } 4999$ (Total 5000 cylinders)
* **Initial Head Position:** $2150$
* **Initial Direction:** Moving Right / Increasing (towards $4999$)
* **Request Queue:** $[2069, 1212, 2296, 2800, 544, 1618, 356, 1523]$
* **Sorted Requests Less Than 2150 (Left):** $356, 544, 1212, 1523, 1618, 2069$
* **Sorted Requests Greater Than 2150 (Right):** $2296, 2800$

---

#### Step 2: Algorithm-by-Algorithm Execution

##### 1. FCFS (First-Come, First-Served)
Services requests strictly in arrival order.

* **Service Sequence:** $2150 \to 2069 \to 1212 \to 2296 \to 2800 \to 544 \to 1618 \to 356 \to 1523$
* **Step-by-Step Distance Calculations:**
  * Step 1: $|2069 - 2150| = 81$
  * Step 2: $|1212 - 2069| = 857$
  * Step 3: $|2296 - 1212| = 1084$
  * Step 4: $|2800 - 2296| = 504$
  * Step 5: $|544 - 2800| = 2256$
  * Step 6: $|1618 - 544| = 1074$
  * Step 7: $|356 - 1618| = 1262$
  * Step 8: $|1523 - 356| = 1167$
* **Total Seek Time Calculation:**
  $$\text{Total Seek} = 81 + 857 + 1084 + 504 + 2256 + 1074 + 1262 + 1167 = 8285 \text{ cylinders}$$

##### 2. SSTF (Shortest Seek Time First)
Always selects the pending request closest to the current head position.

* **Step-by-Step Decision Trace:**
  * Start at $2150$. Closest request is $2069$ (distance $|2069 - 2150| = 81$).
  * From $2069$: Closest is $2296$ (distance $|2296 - 2069| = 227$).
  * From $2296$: Closest is $2800$ (distance $|2800 - 2296| = 504$).
  * From $2800$: Closest is $1618$ (distance $|1618 - 2800| = 1182$).
  * From $1618$: Closest is $1523$ (distance $|1523 - 1618| = 95$).
  * From $1523$: Closest is $1212$ (distance $|1212 - 1523| = 311$).
  * From $1212$: Closest is $544$ (distance $|544 - 1212| = 668$).
  * From $544$: Closest is $356$ (distance $|356 - 544| = 188$).
* **Service Sequence:** $2150 \to 2069 \to 2296 \to 2800 \to 1618 \to 1523 \to 1212 \to 544 \to 356$
* **Total Seek Time Calculation:**
  $$\text{Total Seek} = 81 + 227 + 504 + 1182 + 95 + 311 + 668 + 188 = 3256 \text{ cylinders}$$

##### 3. SCAN Algorithm
Moves right towards cylinder $4999$, services all requests in path, hits boundary $4999$, then reverses left.

* **Service Sequence:** $2150 \to 2296 \to 2800 \to 4999 \text{ (Boundary)} \to 2069 \to 1618 \to 1523 \to 1212 \to 544 \to 356$
* **Step-by-Step Distance Calculations:**
  * Leg 1 (Right): $(4999 - 2150) = 2849$
  * Leg 2 (Left): $(4999 - 356) = 4643$
* **Total Seek Time Calculation:**
  $$\text{Total Seek} = 2849 + 4643 = 7492 \text{ cylinders}$$
* **Shortcut Verification:** $|4999 - 2150| + |4999 - 356| = 2849 + 4643 = 7492 \text{ cylinders}$. (Matches!)

##### 4. C-SCAN Algorithm
Moves right towards boundary $4999$, jumps to boundary $0$, then moves right servicing remaining requests.

* **Service Sequence:** $2150 \to 2296 \to 2800 \to 4999 \text{ (Boundary)} \to 0 \text{ (Boundary)} \to 356 \to 544 \to 1212 \to 1523 \to 1618 \to 2069$
* **Step-by-Step Distance Calculations:**
  * Right sweep to boundary: $|4999 - 2150| = 2849$
  * Boundary reset jump: $|0 - 4999| = 4999$
  * Right sweep to last request: $|2069 - 0| = 2069$
* **Total Seek Time Calculation:**
  $$\text{Total Seek} = 2849 + 4999 + 2069 = 9917 \text{ cylinders}$$

##### 5. LOOK Algorithm
Moves right to the highest request ($2800$), then reverses left to the lowest request ($356$) without hitting boundary $4999$.

* **Service Sequence:** $2150 \to 2296 \to 2800 \to 2069 \to 1618 \to 1523 \to 1212 \to 544 \to 356$
* **Step-by-Step Distance Calculations:**
  * Leg 1 (Right): $|2800 - 2150| = 650$
  * Leg 2 (Left): $|356 - 2800| = 2444$
* **Total Seek Time Calculation:**
  $$\text{Total Seek} = 650 + 2444 = 3094 \text{ cylinders}$$
* **Shortcut Verification:** $|2800 - 2150| + |2800 - 356| = 650 + 2444 = 3094 \text{ cylinders}$. (Matches!)

##### 6. C-LOOK Algorithm
Moves right to highest request ($2800$), jumps directly to lowest request ($356$), then moves right servicing remaining requests up to $2069$.

* **Service Sequence:** $2150 \to 2296 \to 2800 \to 356 \to 544 \to 1212 \to 1523 \to 1618 \to 2069$
* **Step-by-Step Distance Calculations:**
  * Right sweep: $|2800 - 2150| = 650$
  * Return jump: $|356 - 2800| = 2444$
  * Final right sweep: $|2069 - 356| = 1713$
* **Total Seek Time Calculation:**
  $$\text{Total Seek} = 650 + 2444 + 1713 = 4807 \text{ cylinders}$$

---

### 2.2 Problem 1B (Final Exam AY 2023–2024)

#### Problem Statement
A disk drive has 5000 cylinders numbered `0 to 4999`. The drive is currently serving a request at cylinder `143`, and the previous request was at cylinder `125` (indicating rightward movement towards higher cylinders). The queue of pending requests is `86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130`. Calculate total seek distance for **FCFS, SSTF, SCAN, C-SCAN, LOOK, and C-LOOK**.

#### Step 1: Initial Setup & Sorting
* **Disk Range:** $0 \text{ to } 4999$
* **Initial Head Position:** $143$
* **Movement Direction:** Right / Increasing (since previous was $125 < 143$)
* **Request Queue:** $[86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130]$
* **Sorted Requests Less Than 143 (Left):** $86, 130$
* **Sorted Requests Greater Than 143 (Right):** $913, 948, 1022, 1470, 1509, 1750, 1774$

---

#### Step 2: Algorithm Execution & Summary Table

##### 1. FCFS
* **Sequence:** $143 \to 86 \to 1470 \to 913 \to 1774 \to 948 \to 1509 \to 1022 \to 1750 \to 130$
* **Calculation:** $57 + 1384 + 557 + 861 + 826 + 561 + 487 + 728 + 1620 = 7081 \text{ cylinders}$

##### 2. SSTF
* **Sequence:** $143 \to 130 \to 86 \to 913 \to 948 \to 1022 \to 1470 \to 1509 \to 1750 \to 1774$
* **Calculation:** $13 + 44 + 827 + 35 + 74 + 448 + 39 + 241 + 24 = 1745 \text{ cylinders}$

##### 3. SCAN
* **Sequence:** $143 \to 913 \to 948 \to 1022 \to 1470 \to 1509 \to 1750 \to 1774 \to 4999 \text{ (Boundary)} \to 130 \to 86$
* **Calculation:** $(4999 - 143) + (4999 - 86) = 4856 + 4913 = 9769 \text{ cylinders}$

##### 4. C-SCAN
* **Sequence:** $143 \to 913 \to 948 \to 1022 \to 1470 \to 1509 \to 1750 \to 1774 \to 4999 \to 0 \to 86 \to 130$
* **Calculation:** $(4999 - 143) + (4999 - 0) + (130 - 0) = 4856 + 4999 + 130 = 9985 \text{ cylinders}$

##### 5. LOOK
* **Sequence:** $143 \to 913 \to 948 \to 1022 \to 1470 \to 1509 \to 1750 \to 1774 \to 130 \to 86$
* **Calculation:** $(1774 - 143) + (1774 - 86) = 1631 + 1688 = 3319 \text{ cylinders}$

##### 6. C-LOOK
* **Sequence:** $143 \to 913 \to 948 \to 1022 \to 1470 \to 1509 \to 1750 \to 1774 \to 86 \to 130$
* **Calculation:** $(1774 - 143) + (1774 - 86) + (130 - 86) = 1631 + 1688 + 44 = 3363 \text{ cylinders}$

---

## 3. PYQ CATEGORY 2: 200-CYLINDER STANDARD SYSTEMS (10 MARKS EACH)

Standard 200-cylinder disk problems (numbered 0 to 199) are classic laboratory benchmarks and core re-examination problems.

### 3.1 Problem 2 (Standard Laboratory Benchmark)

#### Problem Statement
A disk drive contains 200 cylinders numbered `0 to 199`. The disk request queue in arrival order is `98, 183, 37, 122, 14, 124, 65, 67`. The disk head is initially positioned at cylinder `53` and is **moving towards cylinder 0 (Left / Decreasing)**. Calculate total seek time for all 6 algorithms.

#### Step 1: Initial Setup & Sorting
* **Disk Range:** $0 \text{ to } 199$
* **Initial Head Position:** $53$
* **Initial Direction:** Moving Left / Decreasing (towards $0$)
* **Request Queue:** $[98, 183, 37, 122, 14, 124, 65, 67]$
* **Sorted Requests Less Than 53 (Left):** $37, 14$
* **Sorted Requests Greater Than 53 (Right):** $65, 67, 98, 122, 124, 183$

---

#### Step 2: Algorithm Execution & Breakdown

##### 1. FCFS Algorithm
* **Sequence:** $53 \to 98 \to 183 \to 37 \to 122 \to 14 \to 124 \to 65 \to 67$
* **Calculation:** $|98-53| + |183-98| + |37-183| + |122-37| + |14-122| + |124-14| + |65-124| + |67-65|$
  $$= 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 \text{ cylinders}$$

##### 2. SSTF Algorithm
* **Sequence:** $53 \to 65 \to 67 \to 37 \to 14 \to 98 \to 122 \to 124 \to 183$
* **Calculation:** $|65-53| + |67-65| + |37-67| + |14-37| + |98-14| + |122-98| + |124-122| + |183-124|$
  $$= 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 \text{ cylinders}$$

##### 3. SCAN Algorithm (Moving Left)
* **Sequence:** $53 \to 37 \to 14 \to 0 \text{ (Boundary)} \to 65 \to 67 \to 98 \to 122 \to 124 \to 183$
* **Calculation:** $(53 - 0) + (183 - 0) = 53 + 183 = 236 \text{ cylinders}$

##### 4. C-SCAN Algorithm (Moving Left)
* **Sequence:** $53 \to 37 \to 14 \to 0 \text{ (Boundary)} \to 199 \text{ (Boundary)} \to 183 \to 124 \to 122 \to 98 \to 67 \to 65$
* **Calculation:** $(53 - 0) + (199 - 0) + (199 - 65) = 53 + 199 + 134 = 386 \text{ cylinders}$

##### 5. LOOK Algorithm (Moving Left)
* **Sequence:** $53 \to 37 \to 14 \to 65 \to 67 \to 98 \to 122 \to 124 \to 183$
* **Calculation:** $(53 - 14) + (183 - 14) = 39 + 169 = 208 \text{ cylinders}$

##### 6. C-LOOK Algorithm (Moving Left)
* **Sequence:** $53 \to 37 \to 14 \to 183 \to 124 \to 122 \to 98 \to 67 \to 65$
* **Calculation:** $(53 - 14) + (183 - 14) + (183 - 65) = 39 + 169 + 118 = 326 \text{ cylinders}$

---

### 3.2 Problem 3 (Re-Exam 2022–2023)

#### Problem Statement
A disk drive has 200 cylinders (`0 to 199`). The request queue is `82, 170, 43, 140, 24, 16, 190`. Read/write head is at cylinder `50`, moving towards larger values (Right / Increasing). Calculate total seek distance for all 6 algorithms.

#### Step 1: Initial Setup
* **Disk Range:** $0 \text{ to } 199$
* **Initial Head:** $50$
* **Direction:** Right / Increasing
* **Queue:** $[82, 170, 43, 140, 24, 16, 190]$
* **Left Requests:** $16, 24, 43$
* **Right Requests:** $82, 140, 170, 190$

---

#### Step 2: Execution Results

##### 1. FCFS
* **Sequence:** $50 \to 82 \to 170 \to 43 \to 140 \to 24 \to 16 \to 190$
* **Calculation:** $32 + 88 + 127 + 97 + 116 + 8 + 174 = 642 \text{ cylinders}$

##### 2. SSTF
* **Sequence:** $50 \to 43 \to 24 \to 16 \to 82 \to 140 \to 170 \to 190$
* **Calculation:** $7 + 19 + 8 + 66 + 58 + 30 + 20 = 208 \text{ cylinders}$

##### 3. SCAN
* **Sequence:** $50 \to 82 \to 140 \to 170 \to 190 \to 199 \to 43 \to 24 \to 16$
* **Calculation:** $(199 - 50) + (199 - 16) = 149 + 183 = 332 \text{ cylinders}$

##### 4. C-SCAN
* **Sequence:** $50 \to 82 \to 140 \to 170 \to 190 \to 199 \to 0 \to 16 \to 24 \to 43$
* **Calculation:** $(199 - 50) + (199 - 0) + (43 - 0) = 149 + 199 + 43 = 391 \text{ cylinders}$

##### 5. LOOK
* **Sequence:** $50 \to 82 \to 140 \to 170 \to 190 \to 43 \to 24 \to 16$
* **Calculation:** $(190 - 50) + (190 - 16) = 140 + 174 = 314 \text{ cylinders}$

##### 6. C-LOOK
* **Sequence:** $50 \to 82 \to 140 \to 170 \to 190 \to 16 \to 24 \to 43$
* **Calculation:** $(190 - 50) + (190 - 16) + (43 - 16) = 140 + 174 + 27 = 341 \text{ cylinders}$

---

### 3.3 Problem 4 (Special Re-Exam 2022–2023)

#### Problem Statement
Disk requests: `85, 160, 33, 150, 27, 16, 190`. Read/write head is at cylinder `50`, moving towards larger values (Right). Disk range: `0 to 199`. Calculate seek distance for all 6 algorithms.

#### Step 1: Initial Setup
* **Disk Range:** $0 \text{ to } 199$
* **Initial Head:** $50$, Direction: Right
* **Queue:** $[85, 160, 33, 150, 27, 16, 190]$
* **Left Requests:** $16, 27, 33$
* **Right Requests:** $85, 150, 160, 190$

---

#### Step 2: Execution Results

##### 1. FCFS
* **Sequence:** $50 \to 85 \to 160 \to 33 \to 150 \to 27 \to 16 \to 190$
* **Calculation:** $35 + 75 + 127 + 117 + 123 + 11 + 174 = 662 \text{ cylinders}$

##### 2. SSTF
* **Sequence:** $50 \to 33 \to 27 \to 16 \to 85 \to 150 \to 160 \to 190$
* **Calculation:** $17 + 6 + 11 + 69 + 65 + 10 + 30 = 208 \text{ cylinders}$

##### 3. SCAN
* **Sequence:** $50 \to 85 \to 150 \to 160 \to 190 \to 199 \to 33 \to 27 \to 16$
* **Calculation:** $(199 - 50) + (199 - 16) = 149 + 183 = 332 \text{ cylinders}$

##### 4. C-SCAN
* **Sequence:** $50 \to 85 \to 150 \to 160 \to 190 \to 199 \to 0 \to 16 \to 27 \to 33$
* **Calculation:** $(199 - 50) + (199 - 0) + (33 - 0) = 149 + 199 + 33 = 381 \text{ cylinders}$

##### 5. LOOK
* **Sequence:** $50 \to 85 \to 150 \to 160 \to 190 \to 33 \to 27 \to 16$
* **Calculation:** $(190 - 50) + (190 - 16) = 140 + 174 = 314 \text{ cylinders}$

##### 6. C-LOOK
* **Sequence:** $50 \to 85 \to 150 \to 160 \to 190 \to 16 \to 27 \to 33$
* **Calculation:** $(190 - 50) + (190 - 16) + (33 - 16) = 140 + 174 + 17 = 331 \text{ cylinders}$

---

## 4. PYQ CATEGORY 3: DISK HARDWARE PERFORMANCE METRICS (5 MARKS EACH)

Hardware latency numericals test your ability to convert rotational speeds (RPM) and data sizes into precise millisecond delays.

### 4.1 Problem 5A: Rotational Latency Calculation Across Drive Speeds

#### Problem Statement
Calculate the average rotational latency in milliseconds for hard drives spinning at the following rotational speeds:
1. $5400 \text{ RPM}$
2. $7200 \text{ RPM}$
3. $10000 \text{ RPM}$
4. $15000 \text{ RPM}$

#### Step-by-Step Solution

##### Formula Derivation
The time required for one full $360^\circ$ rotation is $T_{rev} = \frac{60}{\text{RPM}} \text{ seconds}$.
On average, the disk rotates half a revolution ($180^\circ$) before reaching the target sector:
$$T_{r,\text{avg}} = \frac{1}{2} \times \frac{60}{\text{RPM}} \text{ seconds} = \frac{30}{\text{RPM}} \text{ seconds} = \frac{30,000}{\text{RPM}} \text{ ms}$$

##### Calculations
1. **5400 RPM:**
   $$T_{r,\text{avg}} = \frac{30,000}{5400} = 5.555... \text{ ms} \approx 5.56 \text{ ms}$$
2. **7200 RPM:**
   $$T_{r,\text{avg}} = \frac{30,000}{7200} = 4.166... \text{ ms} \approx 4.17 \text{ ms}$$
3. **10000 RPM:**
   $$T_{r,\text{avg}} = \frac{30,000}{10000} = 3.00 \text{ ms}$$
4. **15000 RPM:**
   $$T_{r,\text{avg}} = \frac{30,000}{15000} = 2.00 \text{ ms}$$

---

### 4.2 Problem 5B: Comprehensive Total Disk Access Time

#### Problem Statement
A hard disk has the following specifications:
* Rotational speed = $7200 \text{ RPM}$
* Average seek time = $8 \text{ ms}$
* Controller overhead = $1 \text{ ms}$
* Sector size = $512 \text{ bytes}$
* Sectors per track = $400$

Calculate:
1. Average rotational latency ($T_r$)
2. Data transfer rate in MB/s
3. Total access time to read a file of size $1.6 \text{ MB}$ ($1,638,400 \text{ bytes}$) stored in contiguous sectors on the same cylinder.

#### Step-by-Step Solution

##### Step 1: Average Rotational Latency ($T_r$)
$$T_r = \frac{30,000}{7200} = 4.17 \text{ ms}$$

##### Step 2: Track Capacity & Data Transfer Rate
* **Bytes per track ($N$):** $400 \text{ sectors} \times 512 \text{ bytes/sector} = 204,800 \text{ bytes/track}$.
* **Rotational speed per second ($r$):** $7200 / 60 = 120 \text{ revolutions/sec}$.
* **Data Transfer Rate:**
  $$\text{Transfer Rate} = 120 \text{ rev/sec} \times 204,800 \text{ bytes/rev} = 24,576,000 \text{ bytes/sec} \approx 24.58 \text{ MB/s}$$

##### Step 3: Transfer Time for 1.6 MB ($T_t$)
$$T_t = \frac{1,638,400 \text{ bytes}}{24,576,000 \text{ bytes/sec}} = 0.06667 \text{ seconds} = 66.67 \text{ ms}$$

##### Step 4: Total Access Time ($T_a$)
$$\text{Total } T_a = \text{Controller Overhead} + \text{Seek Time} + \text{Rotational Latency} + \text{Transfer Time}$$
$$\text{Total } T_a = 1.00 + 8.00 + 4.17 + 66.67 = 79.84 \text{ ms}$$

---

## 5. MASTER COMPARISON MATRIX & TERM-END EXAM STRATEGY

### 5.1 Side-by-Side Efficiency Comparison Across All PYQs

The following table summarizes total head movement (in cylinders) across all solved university examination problems.

| Numerical Problem | Disk Range & Initial Head | Direction | FCFS | SSTF | SCAN | C-SCAN | LOOK | C-LOOK | Best Algorithm |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Problem 1A** (AY 2024–25) | 0–4999, Head = 2150 | Right | 8285 | 3256 | 7492 | 9917 | **3094** | 4807 | **LOOK** |
| **Problem 1B** (AY 2023–24) | 0–4999, Head = 143 | Right | 7081 | **1745** | 9769 | 9985 | 3319 | 3363 | **SSTF** |
| **Problem 2** (Lab Benchmark) | 0–199, Head = 53 | Left | 640 | 236 | 236 | 386 | **208** | 326 | **LOOK** |
| **Problem 3** (Re-Exam 22–23) | 0–199, Head = 50 | Right | 642 | **208** | 332 | 391 | 314 | 341 | **SSTF** |
| **Problem 4** (Sp. Re-Exam 22–23)| 0–199, Head = 50 | Right | 662 | **208** | 332 | 381 | 314 | 331 | **SSTF** |

---

### 5.2 Term-End Exam Checklist for 10/10 Marks

To score full marks on disk scheduling numericals in term-end exams:
1. **Always state the initial parameters clearly:** Write down the disk boundaries ($0$ to $B_{max}$), initial head position, and initial direction.
2. **Sort the request queue:** Separate pending requests into those less than the initial head and those greater than the initial head.
3. **Show step-by-step arithmetic:** Write down every individual head jump distance $|R_{i} - R_{i-1}|$ explicitly rather than just writing the final sum.
4. **Draw a simple trajectory line:** Include a horizontal number line showing the path of the head for SCAN, C-SCAN, LOOK, and C-LOOK.
5. **Use shortcut formulas to verify:** Use the shortcut equations during the last 2 minutes of the exam to double-check your total seek time!
