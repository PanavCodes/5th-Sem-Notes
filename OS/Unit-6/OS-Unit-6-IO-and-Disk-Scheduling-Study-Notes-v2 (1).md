# Operating Systems (OS) - Unit 6: I/O Management and Disk Scheduling
## Comprehensive Master Study Notes & Term-End Exam Guide
### Course Outcome: CO-3 (Simulate Memory Management, I/O Management, and File Management Strategies)

> **IMPORTANT SYLLABUS BOUNDARY NOTICE:**
> Per the official university curriculum and course lecture slides (`UNIT6-IO.pptx` up to Slide 57), **Unit 6 strictly covers I/O Hardware, I/O Function Organization, I/O Buffering, Physical Disk Geometry, Disk Performance Parameters, and Disk Scheduling Algorithms**.
> Topics from **RAID (Redundant Array of Independent Disks) onwards** belong to Unit 7 / Advanced Mass-Storage Systems and are **excluded** from Unit 6.

---

## SECTION 1: I/O HARDWARE & DEVICE OVERVIEW

### 1.1 Categories of I/O Devices
Operating systems manage a vast diversity of Input/Output (I/O) hardware devices. These devices are classified into three primary categories based on their target interaction partner, transfer unit, and data transfer rates:

| Device Category | Target Interaction | Primary Characteristics | Common Examples | Data Transfer Rate Range |
| :--- | :--- | :--- | :--- | :--- |
| **Human-Readable Devices** | Suitable for direct communication with human users. | Character-oriented or graphics-oriented, low speed, complex visual encoding. | Keyboard, Mouse, Display Monitor, Printer, Touchscreen | 10 Bytes/sec to 10 MB/sec |
| **Machine-Readable Devices** | Suitable for communication with electronic equipment and storage media. | Block-oriented or stream-oriented, high speed, fixed block transfers with error detection. | Hard Disk Drive (HDD), Solid State Drive (SSD), Optical Disc, USB Flash Drive | 100 KB/sec to several GB/sec |
| **Communication Devices** | Suitable for communicating with remote computers and network nodes. | Packet/stream-oriented, variable speed, protocol-driven. | Network Interface Card (NIC), Wi-Fi Adapter, Modem, Bluetooth Module | 56 Kbps to 100 Gbps |

#### Critical Metrics Distinguishing I/O Devices:
1. **Data Rate:** Varies over many orders of magnitude (from a keyboard generating ~10 bytes/sec to a Gigabit Ethernet NIC handling 1 Gbps+).
2. **Unit of Transfer:** Character-stream (transferred byte-by-byte, e.g., terminal, mouse) versus Block-stream (transferred in fixed-size blocks of bytes, e.g., disk, tape).
3. **Data Representation:** Differing character encoding schemes, parity check bits, block structures, and control signals.
4. **Access Speed & Error Conditions:** Synchronous vs. asynchronous timing, error types, error reporting, and recovery mechanics.

---

### 1.2 Role of the Operating System in I/O Management
The primary objectives of the OS I/O subsystem are to:
1. **Provide Abstraction & Device Independence:** Hide hardware-specific details behind uniform system calls (`read()`, `write()`, `open()`, `close()`), allowing user applications to access any storage or communication device without knowing its physical register layout.
2. **Optimize Performance:** Use buffering, caching, spooling, and request scheduling to bridge the massive speed gap between fast CPUs/RAM and slow secondary I/O devices.
3. **Ensure Fair Allocation & Protection:** Manage shared access to devices, enforce permissions, and prevent race conditions or unauthorized hardware access.
4. **Error Handling:** Catch hardware errors (e.g., CRC check failure, bad sectors, timeout) and attempt recovery without crashing application software.

```
+-----------------------------------------------------------------+
|                      USER APPLICATIONS                          |
+-----------------------------------------------------------------+
                               |  System Calls (read, write, open)
                               v
+-----------------------------------------------------------------+
|                  KERNEL I/O SUBSYSTEM                           |
|  - Device Independence   - Buffering & Caching                   |
|  - I/O Scheduling        - Spooling & Device Reservation         |
+-----------------------------------------------------------------+
                               |  Uniform Driver Interface
                               v
+-----------------------------------------------------------------+
|                     DEVICE DRIVERS                              |
|  (Translates generic requests into hardware control commands)   |
+-----------------------------------------------------------------+
                               |  Register I/O (Ports/MMIO)
                               v
+-----------------------------------------------------------------+
|                    DEVICE CONTROLLER                            |
|  - Status Register       - Control Register                     |
|  - Data-In Register      - Data-Out Register                    |
+-----------------------------------------------------------------+
                               |  Physical Signals / Busses
                               v
+-----------------------------------------------------------------+
|                     PHYSICAL I/O DEVICE                         |
+-----------------------------------------------------------------+
```

---

### 1.3 Device Controllers & Device Drivers

#### A. Device Controller (Hardware Layer)
A **Device Controller** is an electronic component (a chip or expansion card) attached to the system bus that controls the physical I/O device. It acts as a bridge between the system bus and the physical mechanics of the device.

The Controller exposes a set of **Interface Registers**:
* **Data-In Register:** Read by the CPU to receive input data from the device.
* **Data-Out Register:** Written by the CPU to send data/commands to the device.
* **Status Register:** Read by the CPU to check state flags (e.g., BUSY, READY, ERROR, DATA_AVAILABLE).
* **Control Register:** Written by the CPU to initiate operations, select transfer modes, or enable interrupts.

#### B. Memory-Mapped I/O vs. Port-Mapped (Isolated) I/O

```
Port-Mapped (Isolated) I/O:
  CPU Registers <---> Special IN / OUT Instructions <---> Dedicated I/O Ports

Memory-Mapped I/O (MMIO):
  CPU Registers <---> Standard Memory Instructions (MOV) <---> Shared Physical Address Space
```

| Feature | Port-Mapped I/O (Isolated I/O) | Memory-Mapped I/O (MMIO) |
| :--- | :--- | :--- |
| **Address Space** | Separate, dedicated I/O port address space (e.g., ports 0x0000 to 0xFFFF). | Device registers are mapped directly into the main memory address space. |
| **CPU Instructions** | Requires special CPU instructions (`IN`, `OUT` in x86). | Uses standard memory assembly instructions (`MOV`, `LDR`, `STR`). |
| **Bus Control** | Requires dedicated `I/OR` and `I/OW` hardware control lines. | Uses standard `MEMR` and `MEMW` bus lines. |
| **Protection & Caching** | OS protects ports using CPU privilege levels (IOPL). | OS uses Virtual Memory Page Tables to control protection and disable caching (`uncached`). |

#### C. Device Driver (Software Layer)
A **Device Driver** is a kernel software module custom-written for a specific device controller. It encapsulates device-specific register operations and presents a standard interface (e.g., Block Device or Character Device interface) to the OS Kernel I/O subsystem.

---

## SECTION 2: ORGANIZATION OF THE I/O FUNCTION

The evolution of the I/O function reflects the historical drive to minimize CPU involvement in slow peripheral data transfers.

```
+-----------------------------------------------------------------------------------+
|                           EVOLUTION OF THE I/O FUNCTION                            |
+-----------------------------------------------------------------------------------+
| 1. Direct Software Control: CPU directly controls hardware bits (Polling/PIO)     |
| 2. Controller Added: CPU uses Programmed I/O without interrupts                   |
| 3. Interrupt-Driven I/O: Controller issues hardware IRQ when ready                |
| 4. Direct Memory Access (DMA): DMAC handles block transfer, interrupts CPU once   |
| 5. I/O Channel: Dedicated specialized processor executes I/O programs in RAM      |
| 6. I/O Processor: Independent computer with local memory dedicated to I/O tasks  |
+-----------------------------------------------------------------------------------+
```

---

### 2.1 Programmed I/O (Polling / Busy-Waiting)
In **Programmed I/O**, the CPU issues an I/O command on behalf of a process to the device controller and then **polls (busy-waits)** on the Status Register in a tight loop until the I/O operation completes.

```
CPU Loop:
  1. Issue I/O Command -> Device Controller
  2. LOOP: Read Controller Status Register
  3. IF Status == BUSY -> GOTO Step 2 (CPU Spin-Wait)
  4. IF Status == READY -> Read Data Register -> Store in RAM
  5. Repeat for next byte/word
```

* **Advantage:** Very simple hardware design; no interrupt lines or special control logic needed.
* **Disadvantage:** Extremely inefficient! Completely consumes CPU cycles during slow peripheral access (e.g., spending millions of CPU clock cycles waiting for a keypress or disk sector read).

---

### 2.2 Interrupt-Driven I/O
In **Interrupt-Driven I/O**, the CPU issues an I/O command to the device controller, saves process context, and **immediately switches to executing other productive processes**. When the device finishes reading/writing data, the controller asserts a hardware **Interrupt Request (IRQ)** line on the system bus.

```
+---------------+     1. Issue Read Command     +--------------------+
|               | ----------------------------> |                    |
|      CPU      |                               | Device Controller  |
|               | <---------------------------- |                    |
+---------------+     2. Hardware IRQ Signal    +--------------------+
        |
        v 3. Save CPU Context (PC, Registers)
        v 4. Lookup Interrupt Vector Table (IVT)
        v 5. Execute Interrupt Service Routine (ISR)
        v 6. Transfer Data Byte to RAM
        v 7. Restore Context & Resume Process
```

* **Advantage:** Eliminates CPU busy-waiting; CPU remains free to execute other processes while I/O is in progress.
* **Disadvantage:** High context-switch overhead for high-speed devices! Transferring a 1 GB file byte-by-byte generates 1 billion hardware interrupts, causing massive CPU performance degradation due to constant ISR invocation and cache pollution.

---

### 2.3 Direct Memory Access (DMA)

#### A. Need for DMA
High-speed devices (HDDs, SSDs, Gigabit NICs) transfer data at rates approaching or exceeding RAM speeds. Interrupt-Driven I/O cannot keep up due to per-byte interrupt handling overhead. **DMA** offloads the entire block data transfer process to a dedicated hardware controller: the **DMA Controller (DMAC)**.

#### B. DMAC Hardware Architecture & Registers
A DMA Controller contains:
1. **Address Register:** Holds the physical starting address in RAM where data is to be read or written.
2. **Byte / Word Count Register (C):** Holds the number of bytes remaining to be transferred.
3. **Control Register:** Specifies transfer direction (Read from Device / Write to RAM or vice versa), transfer mode, and interrupt enable bits.
4. **Handshaking Lines:**
   * **DRQ (DMA Request):** Asserted by the device controller when a data word is ready in its local buffer.
   * **DACK (DMA Acknowledge):** Asserted by the DMAC to inform the device that the bus has been acquired and data transfer is taking place.

```
+---------------------------------------------------------------------------------+
|                              DMA TRANSFER STEPS                                 |
+---------------------------------------------------------------------------------+
| 1. CPU writes Memory Start Address, Byte Count C, and Control Bits into DMAC    |
| 2. CPU commands Device Controller to read physical block into device buffer     |
| 3. Device Buffer receives word -> Asserts DRQ signal to DMAC                     |
| 4. DMAC requests System Bus from CPU (Bus Request / Bus Grant)                   |
| 5. DMAC asserts DACK -> Moves Word directly from Device Buffer to RAM over Bus  |
| 6. DMAC increments Address Register, decrements Byte Count Register C            |
| 7. Steps 3-6 repeat automatically until Byte Count C == 0                       |
| 8. DMAC releases System Bus and issues a SINGLE completion Interrupt to CPU     |
+---------------------------------------------------------------------------------+
```

#### C. DMA Transfer Modes

```
1. Cycle Stealing Mode:
   CPU Bus Access:  [CPU] [DMA] [CPU] [CPU] [DMA] [CPU] (Steals 1 bus cycle per word)

2. Burst Mode (Block Transfer):
   CPU Bus Access:  [CPU] [-------- DMA BURST TRANSFER --------] [CPU] (Locks bus for full block)

3. Fly-By Mode:
   Data Path: Device Controller <============ System Bus ============> RAM (Direct transfer)
```

| Transfer Mode | Mechanism & Bus Behavior | Pros & Cons |
| :--- | :--- | :--- |
| **Cycle Stealing Mode** | DMAC acquires system bus for **1 bus cycle** to transfer a single word, then returns bus control to the CPU. | **Pros:** CPU is never locked out of memory for long periods.<br>**Cons:** Higher bus request/grant arbitration overhead. |
| **Burst Mode (Block Mode)** | DMAC acquires system bus and holds it continuously until the **entire block of data** (e.g., 4 KB) is transferred. | **Pros:** Maximum data transfer throughput; minimum bus arbitration overhead.<br>**Cons:** Locks CPU out of main memory during the entire burst. |
| **Fly-By Mode** | Data flows directly between the device controller and RAM over the data bus without passing through DMAC registers. | **Pros:** Requires only 1 bus cycle per word transfer.<br>**Cons:** Requires hardware support in both controller and motherboard. |

---

## SECTION 3: I/O BUFFERING TECHNIQUES

### 3.1 Need and Purpose of I/O Buffering
Buffering is the technique of allocating kernel memory space to temporarily hold data during I/O transfers.
1. **Speed Mismatch:** Bridges the gap between fast CPU/RAM and slow I/O devices.
2. **Transfer Unit Size Mismatch:** Adapts between character-at-a-time input (keyboard) and block-at-a-time processing (kernel applications).
3. **Copy Semantics:** Guarantees that user buffer data remains unchanged during asynchronous background disk/network writes.

---

### 3.2 Buffering Schemes & Mathematical Performance Analysis

#### Notation for Mathematical Formulas:
* **T:** Time required to input a physical block of data from device into the buffer.
* **C:** Time required by the CPU to process/compute the data block once in memory.
* **M:** Time required to move the data block from the kernel buffer to the user buffer space.

```
1. No Buffering:
   Timeline: |--- Input T ---|--- Process C ---|--- Input T ---|--- Process C ---|
   Total Time per Block = T + C

2. Single Buffering:
   Timeline: Input T into Kernel Buffer ---> Move M to User Space ---> Process C (Parallel with next Input T)
   Total Time per Block = max(T, C) + M

3. Double Buffering (Dual Buffering):
   Buffer 1: [ Filling with Input T ]
   Buffer 2: [ Processing C in parallel ]
   Total Time per Block = max(T, C + M)  or  max(T, C)
```

| Buffering Scheme | Architecture & Working Mechanics | Execution Time per Block Formula |
| :--- | :--- | :--- |
| **No Buffering** | OS transfers data directly between device and user memory space. Process blocks completely during input/output. | **Time = T + C** |
| **Single Buffering** | OS allocates a single kernel buffer. Device writes block into kernel buffer (takes time T). OS moves block to user space (takes M), and CPU processes it (takes C) while device reads next block. | **Time = max(T, C) + M** |
| **Double Buffering (Dual Buffering)** | OS allocates two kernel buffers (Buffer A and Buffer B). While device fills Buffer A (time T), CPU processes Buffer B (time C + M). When done, buffers swap roles. | **Time = max(T, C + M)**<br>*(If M is negligible, Time = max(T, C))* |
| **Circular Buffering** | OS allocates a queue of N kernel buffers arranged in a bounded ring. Used when I/O arrives in heavy, unpredictable bursts. | Smooths out bursty traffic as long as average process rate >= average arrival rate. |

---

## SECTION 4: DISK STRUCTURE, PHYSICAL GEOMETRY & PERFORMANCE PARAMETERS

### 4.1 Physical Disk Geometry
A Hard Disk Drive (HDD) consists of a stack of rigid platters coated with magnetizable material, rotating on a central spindle at constant high speed (e.g., 5400 RPM, 7200 RPM, 10000 RPM, 15000 RPM).

```
                      PHYSICAL DISK GEOMETRY
                      
                   +--------------------------+
                   |       Spindle Motor      |
                   +--------------------------+
                                ||
       Platter 1  ====[==========||==========]====  <-- Read/Write Head 0
                      [          ||          ]      <-- Read/Write Head 1
       Platter 2  ====[==========||==========]====  <-- Read/Write Head 2
                      [          ||          ]      <-- Read/Write Head 3
                                ||
                                ||
                      +--------------------+
                      | Actuator Arm Assembly
                      +--------------------+

  Top View of a Platter Surface:
       +------------------------------------+
       |   Track (Concentric Ring)          |
       |     Sector (512B or 4096B Arc)     |
       |       Cylinder (Vertical Set)      |
       +------------------------------------+
```

* **Platter:** Flat circular disk coated with magnetic recording material.
* **Surface:** Both top and bottom sides of a platter are recorded on by dedicated Read/Write heads.
* **Track:** Concentric circular rings on a platter surface.
* **Sector:** A subdivision of a track, representing the smallest physical unit of storage (traditionally 512 bytes, modern Advanced Format uses 4096 bytes / 4 KB).
* **Cylinder:** The set of all tracks across all platter surfaces that reside at the exact same radial arm position.
* **Constant Angular Velocity (CAV) vs. Zoned Bit Recording (ZBR):**
  * **CAV:** Disk rotates at constant angular speed. Outer tracks move physically faster than inner tracks, so outer sectors are physically wider (lower data density).
  * **ZBR:** Disk tracks are grouped into concentric zones. Outer zones contain more sectors per track than inner zones, maximizing storage capacity.

---

### 4.2 Disk Performance Parameters & Formulas

```
+---------------------------------------------------------------------------------+
|                       TOTAL DISK ACCESS TIME COMPONENTS                         |
+---------------------------------------------------------------------------------+
| Total Access Time (Ta) = Seek Time (Ts) + Rotational Latency (Tr) + Transfer (Tt)|
+---------------------------------------------------------------------------------+
```

#### 1. Seek Time (Ts)
The time required for the disk actuator arm to move the Read/Write head to the specified track/cylinder.
* **Formula:** `Ts = (m x n) + s`
  * `m` = Constant factor depending on disk drive hardware.
  * `n` = Number of cylinders traversed.
  * `s` = Startup time of the actuator arm.
* Typical average seek times range from **3 ms to 12 ms**.

#### 2. Rotational Latency / Rotational Delay (Tr)
The time required for the target sector to rotate under the Read/Write head once the head is positioned on the correct track.
* **Average Rotational Latency:** On average, the disk must rotate half a revolution to reach the target sector.
* **Formula:** `Average Tr = 0.5 x (60 / RPM) seconds = (30 / RPM) seconds`
  * For 7200 RPM disk: `Average Tr = 30 / 7200 = 0.004167 sec = 4.17 ms`.
  * For 10000 RPM disk: `Average Tr = 30 / 10000 = 0.003 sec = 3.0 ms`.
  * For 15000 RPM disk: `Average Tr = 30 / 15000 = 0.002 sec = 2.0 ms`.

#### 3. Transfer Time (Tt)
The time required to transfer data to or from the disk surface as it rotates underneath the head.
* **Formula:** `Tt = b / (r x N)`
  * `b` = Number of bytes to be transferred.
  * `N` = Total number of bytes per track.
  * `r` = Rotational speed in revolutions per second (`r = RPM / 60`).

#### 4. Total Access Time (Ta)
* **Formula:** `Ta = Seek Time (Ts) + Rotational Latency (Tr) + Transfer Time (Tt)`

---

## SECTION 5: DISK SCHEDULING ALGORITHMS & SOLVED BENCHMARK NUMERICALS

When multiple processes issue I/O requests for different cylinders, the OS orders requests using **Disk Scheduling Algorithms** to minimize total head movement (Seek Time) and maximize throughput.

---

### 5.1 Algorithm Definitions & Strategies

1. **FCFS (First-Come, First-Served):**
   * **Strategy:** Services requests strictly in arrival order.
   * **Pros:** Completely fair; zero starvation risk; simple queue implementation.
   * **Cons:** High seek time; wild head swings across the disk surface.
2. **SSTF (Shortest Seek Time First):**
   * **Strategy:** Selects the request closest to the current head position.
   * **Pros:** Minimizes total seek time for static queues.
   * **Cons:** Causes **starvation** for distant cylinder requests under heavy load.
3. **SCAN (Elevator Algorithm):**
   * **Strategy:** Head moves in one direction servicing requests until it reaches the **physical end of the disk (0 or Max)**, then reverses direction.
   * **Pros:** Bounded wait times; eliminates starvation.
   * **Cons:** Forces unnecessary sweeps to the physical disk boundary even if no requests exist there.
4. **C-SCAN (Circular SCAN):**
   * **Strategy:** Head moves in one direction servicing requests to the physical disk boundary, then **jumps back to cylinder 0 without servicing requests** on the return trip, and sweeps again.
   * **Pros:** Provides uniform response time for all cylinders.
   * **Cons:** Return jump count inflates total head movement distance.
5. **LOOK:**
   * **Strategy:** Same as SCAN, but head **"looks ahead"** and reverses direction immediately after servicing the last pending request in that direction, without traveling to the physical disk boundary.
   * **Pros:** Eliminates wasted boundary sweeps; highly efficient.
6. **C-LOOK (Circular LOOK):**
   * **Strategy:** Same as C-SCAN, but the head moves only as far as the furthest request in the current direction, then **jumps directly to the lowest requested cylinder** and resumes scanning.
   * **Pros:** Combines uniform wait time of C-SCAN with boundary efficiency of LOOK.

---

### 5.2 Solved Standard Benchmark Numerical (Master PYQ Problem 1)

#### Problem Statement:
Consider a disk drive with 200 cylinders numbered **0 to 199**. The queue of pending requests in FIFO order is:
`98, 183, 37, 122, 14, 124, 65, 67`
The disk read/write head is initially positioned at **cylinder 53** and is **moving towards cylinder 0 (Left / Decreasing)**.

Calculate the step-by-step head movements, service sequence, and Total Seek Distance (in cylinders) for all 6 algorithms:

---

#### 1. FCFS Algorithm
* **Service Order:** `53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67`
* **Head Movements Calculation:**
  * |98 - 53| = 45
  * |183 - 98| = 85
  * |37 - 183| = 146
  * |122 - 37| = 85
  * |14 - 122| = 108
  * |124 - 14| = 110
  * |65 - 124| = 59
  * |67 - 65| = 2
* **Total Seek Time:** 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = **640 Cylinders**

---

#### 2. SSTF Algorithm
* **Starting Position:** 53
* **Step-by-Step Closest Selection:**
  * From 53: Closest is 65 (|65 - 53| = 12)
  * From 65: Closest is 67 (|67 - 65| = 2)
  * From 67: Closest is 37 (|37 - 67| = 30)
  * From 37: Closest is 14 (|14 - 37| = 23)
  * From 14: Closest is 98 (|98 - 14| = 84)
  * From 98: Closest is 122 (|122 - 98| = 24)
  * From 122: Closest is 124 (|124 - 122| = 2)
  * From 124: Closest is 183 (|183 - 124| = 59)
* **Service Order:** `53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183`
* **Total Seek Time:** 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = **236 Cylinders**

---

#### 3. SCAN Algorithm (Moving Towards 0)
* **Strategy:** Move Left towards cylinder 0, service all requests, hit physical boundary 0, then reverse Right.
* **Requests Left of 53 (Sorted Descending):** 37, 14
* **Requests Right of 53 (Sorted Ascending):** 65, 67, 98, 122, 124, 183
* **Service Trajectory:** `53 -> 37 -> 14 -> 0 (Boundary) -> 65 -> 67 -> 98 -> 122 -> 124 -> 183`
* **Calculation:**
  * Left leg: (53 - 0) = 53
  * Right leg: (183 - 0) = 183
* **Total Seek Time:** 53 + 183 = **236 Cylinders**

---

#### 4. C-SCAN Algorithm (Moving Towards 0)
* **Strategy:** Move Left towards boundary 0 servicing requests, hit 0, jump to boundary 199 without servicing, then move Left servicing remaining requests.
* **Service Trajectory:** `53 -> 37 -> 14 -> 0 (Boundary) -> 199 (Boundary) -> 183 -> 124 -> 122 -> 98 -> 67 -> 65`
* **Calculation:**
  * Leg 1 (53 to 0): |0 - 53| = 53
  * Jump (0 to 199): |199 - 0| = 199
  * Leg 2 (199 to 65): |65 - 199| = 134
* **Total Seek Time:** 53 + 199 + 134 = **386 Cylinders**

---

#### 5. LOOK Algorithm (Moving Towards 0)
* **Strategy:** Move Left servicing requests down to lowest request (14), then reverse Right servicing remaining requests up to highest request (183). No boundary trips!
* **Service Trajectory:** `53 -> 37 -> 14 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183`
* **Calculation:**
  * Left leg (53 to 14): |14 - 53| = 39
  * Right leg (14 to 183): |183 - 14| = 169
* **Total Seek Time:** 39 + 169 = **208 Cylinders**

---

#### 6. C-LOOK Algorithm (Moving Towards 0)
* **Strategy:** Move Left servicing requests down to 14, jump directly to highest request (183), then move Left servicing down to 65.
* **Service Trajectory:** `53 -> 37 -> 14 -> 183 -> 124 -> 122 -> 98 -> 67 -> 65`
* **Calculation:**
  * Leg 1 (53 to 14): |14 - 53| = 39
  * Jump (14 to 183): |183 - 14| = 169
  * Leg 2 (183 to 65): |65 - 183| = 118
* **Total Seek Time:** 39 + 169 + 118 = **326 Cylinders**

---

### 5.3 Solved Standard Benchmark Numerical (Master PYQ Problem 2)

#### Problem Statement:
A disk queue has requests on cylinders: `2069, 1212, 2296, 2800, 544, 1618, 356, 1523`. The disk head is currently positioned at **cylinder 2150**. The disk has cylinders numbered **0 to 4999**. The initial direction is **towards 4999 (Right / Increasing)**.

Calculate the total head movement for FCFS, SCAN, C-SCAN, LOOK, and C-LOOK:

---

#### 1. FCFS Algorithm
* **Service Trajectory:** `2150 -> 2069 -> 1212 -> 2296 -> 2800 -> 544 -> 1618 -> 356 -> 1523`
* **Calculation:** 81 + 857 + 1084 + 504 + 2256 + 1074 + 1262 + 1167 = **7585 Cylinders**

---

#### 2. SCAN Algorithm (Towards 4999)
* **Right Requests:** 2296, 2800
* **Left Requests:** 2069, 1618, 1523, 1212, 544, 356
* **Service Trajectory:** `2150 -> 2296 -> 2800 -> 4999 (Boundary) -> 2069 -> 1618 -> 1523 -> 1212 -> 544 -> 356`
* **Calculation:** (4999 - 2150) + (4999 - 356) = 2849 + 4643 = **7492 Cylinders**

---

#### 3. C-SCAN Algorithm (Towards 4999)
* **Service Trajectory:** `2150 -> 2296 -> 2800 -> 4999 (Boundary) -> 0 (Boundary) -> 356 -> 544 -> 1212 -> 1523 -> 1618 -> 2069`
* **Calculation:** (4999 - 2150) + (4999 - 0) + (2069 - 0) = 2849 + 4999 + 2069 = **9917 Cylinders**

---

#### 4. LOOK Algorithm (Towards 4999)
* **Service Trajectory:** `2150 -> 2296 -> 2800 -> 2069 -> 1618 -> 1523 -> 1212 -> 544 -> 356`
* **Calculation:** (2800 - 2150) + (2800 - 356) = 650 + 2444 = **3094 Cylinders** (or |2800-2150| + |356-2800| = **7183 Cylinders total sweep**)

---

#### 5. C-LOOK Algorithm (Towards 4999)
* **Service Trajectory:** `2150 -> 2296 -> 2800 -> 356 -> 544 -> 1212 -> 1523 -> 1618 -> 2069`
* **Calculation:** (2800 - 2150) + (2800 - 356) + (2069 - 356) = 650 + 2444 + 1713 = **4807 Cylinders**

---

### 5.4 Master Algorithm Efficiency Comparison Table

| Algorithm | Head Direction | Service Sequence (200 Cylinder Problem) | Total Seek Time | Efficiency Rank | Starvation Risk? |
| :--- | :---: | :--- | :---: | :---: | :---: |
| **LOOK** | Left (towards 0) | `53 -> 37 -> 14 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183` | **208 Cylinders** | **1st (Best)** | Low |
| **SSTF** | Closest First | `53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183` | **236 Cylinders** | **2nd** | **HIGH** |
| **SCAN** | Left (towards 0) | `53 -> 37 -> 14 -> 0 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183` | **236 Cylinders** | **2nd** | None |
| **C-LOOK** | Left (towards 0) | `53 -> 37 -> 14 -> 183 -> 124 -> 122 -> 98 -> 67 -> 65` | **326 Cylinders** | **4th** | None |
| **C-SCAN** | Left (towards 0) | `53 -> 37 -> 14 -> 0 -> 199 -> 183 -> 124 -> 122 -> 98 -> 67 -> 65` | **386 Cylinders** | **5th** | None |
| **FCFS** | Arrival Order | `53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67` | **640 Cylinders** | **6th (Worst)** | None |

---

## SECTION 6: UNIVERSITY TERM-END EXAM QUESTION BANK & SOLVED MODEL ANSWERS (UNIT 6 ONLY)

### Question 1 (10 Marks):
**A disk queue has requests on cylinders 2069, 1212, 2296, 2800, 544, 1618, 356, 1523. The disk head is currently positioned at cylinder 2150. The disk has cylinders numbered 0 to 4999. Calculate the total head movement required to service all requests using FCFS, SCAN, and C-SCAN (assuming initial head movement towards higher cylinders).**

#### Solved Model Answer:

**Given:**
* Queue = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523]
* Initial Head = 2150
* Direction = Towards 4999 (Increasing / Right)
* Disk Range = 0 to 4999

---

#### Part I: FCFS Algorithm
* **Service Trajectory:** `2150 -> 2069 -> 1212 -> 2296 -> 2800 -> 544 -> 1618 -> 356 -> 1523`
* **Head Movements:**
  * |2069 - 2150| = 81
  * |1212 - 2069| = 857
  * |2296 - 1212| = 1084
  * |2800 - 2296| = 504
  * |544 - 2800| = 2256
  * |1618 - 544| = 1074
  * |356 - 1618| = 1262
  * |1523 - 356| = 1167
* **Total FCFS Distance:** 81 + 857 + 1084 + 504 + 2256 + 1074 + 1262 + 1167 = **7585 Cylinders**

---

#### Part II: SCAN Algorithm (Towards 4999)
* **Requests Right of 2150 (Ascending):** 2296, 2800
* **Requests Left of 2150 (Descending):** 2069, 1618, 1523, 1212, 544, 356
* **Service Trajectory:** `2150 -> 2296 -> 2800 -> 4999 (Boundary) -> 2069 -> 1618 -> 1523 -> 1212 -> 544 -> 356`
* **Calculation:**
  * Right leg: (4999 - 2150) = 2849
  * Left leg: (4999 - 356) = 4643
* **Total SCAN Distance:** 2849 + 4643 = **7492 Cylinders**

---

#### Part III: C-SCAN Algorithm (Towards 4999)
* **Service Trajectory:** `2150 -> 2296 -> 2800 -> 4999 (Boundary) -> 0 (Boundary) -> 356 -> 544 -> 1212 -> 1523 -> 1618 -> 2069`
* **Calculation:**
  * Leg 1 (2150 to 4999): (4999 - 2150) = 2849
  * Jump (4999 to 0): 4999
  * Leg 2 (0 to 2069): (2069 - 0) = 2069
* **Total C-SCAN Distance:** 2849 + 4999 + 2069 = **9917 Cylinders**

---

### Question 2 (5 Marks):
**Differentiate between Programmed I/O, Interrupt-Driven I/O, and Direct Memory Access (DMA).**

#### Solved Model Answer Table:

| Criterion | Programmed I/O | Interrupt-Driven I/O | Direct Memory Access (DMA) |
| :--- | :--- | :--- | :--- |
| **CPU Involvement** | Continuous CPU polling loop. | CPU handles each byte via ISR interrupts. | CPU setup & completion interrupt only. |
| **Hardware Required** | Basic Controller Registers. | Interrupt Controller (PIC/APIC). | DMA Controller (DMAC). |
| **Data Path** | Device -> CPU -> RAM | Device -> CPU -> RAM | Device -> System Bus -> RAM (Direct) |
| **Context Switching** | None (CPU busy-waits). | High (Per-byte/word interrupt). | Minimum (1 interrupt per block). |
| **Suitable For** | Very simple, slow hardware. | Low/medium speed devices (Keyboard). | High-speed block devices (Disk, NIC). |

---

### Question 3 (5 Marks):
**Explain Single, Double, and Circular Buffering along with execution time formulas.**

#### Solved Model Answer Summary:
* **Single Buffering:** Time per block = `max(T, C) + M`.
* **Double Buffering:** Time per block = `max(T, C + M)`. Eliminates CPU idle time when input time matches compute time.
* **Circular Buffering:** Bounded queue of N buffers; smooths out unpredictable, bursty I/O traffic.

---

### Question 4 (5 Marks):
**Explain physical disk geometry and performance parameters (Seek Time, Rotational Latency, Transfer Time, Access Time).**

#### Solved Model Answer Summary:
* **Disk Geometry:** Stack of platters rotating on a spindle. Tracks are concentric rings; Sectors are 512B/4KB arcs; Cylinders are vertical track sets across platters.
* **Seek Time (Ts):** Time to move actuator arm to track (`Ts = m x n + s`).
* **Rotational Latency (Tr):** Delay for sector to rotate under head (`Average Tr = 30 / RPM seconds`).
* **Transfer Time (Tt):** Time to transfer data bytes (`Tt = b / (r x N)`).
* **Total Access Time (Ta):** `Ta = Ts + Tr + Tt`.
