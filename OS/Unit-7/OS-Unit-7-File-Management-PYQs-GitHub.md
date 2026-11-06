# Operating Systems (OS) - Unit 7: File Management PYQs Master Exam Guide

## Comprehensive University Previous Year Questions (PYQ) Bank & Model Solutions
### Course Outcome: CO-3 (Simulate Memory Management, I/O Management, and File Management Strategies)

---

## SECTION 1: 10-MARK CORE UNIVERSITY LONG ANSWER QUESTIONS

### Question 1 (10 Marks)
**Define a file and list various file attributes. Explain the three primary file allocation methods (Contiguous Allocation, Linked Allocation, and Indexed Allocation) in detail along with their advantages, disadvantages, and a comparative analysis.**

*Source Alignment: University Re-Exam 2022–23 (Q4b), Technical Publications PYQ Bank.*

---

#### Solved Model Answer:

#### 1. Concept of a File & File Attributes (2 Marks)
A **File** is a named collection of logically related information recorded on non-volatile secondary storage (such as hard disks, SSDs, or optical media). From an operating system perspective, a file represents a uniform, logical abstraction of physical storage, hiding hardware-specific sector layouts behind a linear logical address space.

Operating systems maintain metadata associated with each file. These **File Attributes** include:
1. **Name:** Human-readable string identifying the file in a directory structure.
2. **Identifier:** A unique non-human-readable tag (e.g., inode number or system file ID) used internally by the kernel.
3. **Type:** Specifies the file format (e.g., executable, text, directory, system) for systems supporting multiple file types.
4. **Location:** Pointer to the physical storage device and disk block address occupied by the file.
5. **Size:** Current size of the file in bytes, words, or physical blocks (and maximum allowed size, if bounded).
6. **Protection / Access Control:** Security flags controlling Read (`r`), Write (`w`), and Execute (`x`) permissions for different user classes.
7. **Time, Date, and User Identification:** Timestamps tracking file creation, last modification, and last access, used for monitoring and system backups.

---

#### 2. Contiguous Allocation Method (2.5 Marks)

##### Mechanics & Address Translation
In **Contiguous Allocation**, each file occupies a set of physically adjacent blocks on the secondary storage device. Disk addresses define a linear sequence on disk sectors.

* **Directory Entry:** Requires only two parameters: the **Starting Block Address ($b$)** and the **Length / Count of Allocated Blocks ($n$)**.
* **Address Translation:** To access logical block $i$ within a file starting at physical block $b$, the operating system computes the physical block address directly in $O(1)$ time:

$$\text{Physical Block Address} = b + i \quad (\text{where } 0 \le i < n)$$

##### Advantages
1. **High I/O Performance:** Minimal disk seek time and rotational latency because adjacent file blocks reside on adjacent physical disk cylinders.
2. **Efficient Direct / Random Access:** Any arbitrary logical block $i$ can be read directly without traversing intermediate block pointers.
3. **Simple Directory Structure:** Directory entries remain extremely small, storing only starting address and length.

##### Disadvantages
1. **External Fragmentation:** Over time, deleting files creates scattered free holes across the disk. A new file request of length $N$ cannot be allocated if no single contiguous hole of size $N$ exists, even if total free space exceeds $N$.
2. **Size Declaration Constraint:** The maximum file size must be known at the time of file creation, making dynamic file growth difficult.
3. **Compaction Overhead:** Resolving external fragmentation requires expensive disk compaction, moving millions of sectors across storage.

---

#### 3. Linked (Chained) Allocation Method (2.5 Marks)

##### Mechanics & FAT Variation
In **Linked Allocation**, each file is stored as a linked list of disk blocks scattered anywhere across the physical storage media.

* **Directory Entry:** Contains pointers to the **First (Start) Block** and the **Last (End) Block** of the file.
* **Block Pointer Overhead:** Each physical block contains data plus a pointer field storing the physical disk address of the next contiguous block. The last block contains a null pointer (e.g., `-1`).
* **File Allocation Table (FAT) Variation:** Instead of embedding pointers inside physical data blocks, the **File Allocation Table (FAT)** extracts all block pointers into a single centralized table cached in main memory. The directory stores only the starting block number, and traversing the FAT array in memory yields fast block lookups without extra disk seeks.

##### Advantages
1. **Zero External Fragmentation:** Any free disk block on the system-wide free list can satisfy an allocation request.
2. **Dynamic File Growth:** Files can expand dynamically without declaring initial size; no disk space compaction is ever required.
3. **Simple Allocation Routine:** Finding a free block requires taking any available block from the free list.

##### Disadvantages
1. **Inefficient Direct / Random Access:** Accessing logical block $i$ requires traversing the block pointers sequentially from the start block, incurring up to $i$ individual disk read operations.
2. **Pointer Overhead:** Disk space is wasted storing 4-byte or 8-byte pointer addresses inside every data block (reducing usable block data capacity).
3. **Reliability Risks:** A single corrupted pointer breaks the chain, rendering all subsequent blocks of the file inaccessible.

---

#### 4. Indexed Allocation Method & UNIX Inodes (2.5 Marks)

##### Mechanics & Index Block Structure
**Indexed Allocation** brings together all disk block pointers for a file into a single dedicated block known as the **Index Block** (or File Map Table).

* **Directory Entry:** Contains only the physical address of the file's **Index Block**.
* **Direct Address Lookup:** The $i^{\text{th}}$ entry in the index block stores the physical disk address of the $i^{\text{th}}$ data block of the file.

##### Handling Large Files (Multi-level Indexing & UNIX Inode)
When a file outgrows the pointer capacity of a single index block, systems use:
1. **Linked Scheme:** Links multiple index blocks together via pointers.
2. **Multilevel Indexing:** A first-level index block points to second-level index blocks, which point to data blocks.
3. **Combined Scheme (UNIX Inode):** An inode contains direct pointers (e.g., 12 entries) for small files, plus **Single Indirect**, **Double Indirect**, and **Triple Indirect** pointers for exponentially larger files.

##### Advantages
1. **Supports Efficient Direct Access:** Reading logical block $i$ requires looking up entry $i$ in the index block directly without traversing intermediate data blocks.
2. **Zero External Fragmentation:** Data blocks can be allocated anywhere on disk.
3. **Dynamic Expansion:** Files can grow dynamically by allocating new blocks and updating index entries.

##### Disadvantages
1. **Index Pointer Overhead:** Requires allocating an entire index block even for tiny files consisting of only 1 or 2 data blocks.
2. **Multiple Disk Reads:** Accessing a data block requires an initial disk read for the index block unless the index block is cached in RAM.

---

#### 5. Master Comparison Matrix of File Allocation Methods (0.5 Marks)

| Criteria / Feature | Contiguous Allocation | Linked Allocation | FAT (Linked Variant) | Indexed Allocation (UNIX Inode) |
| :--- | :--- | :--- | :--- | :--- |
| **Pre-allocation Requirement** | Required (Size declared upfront) | Not Required | Not Required | Not Required |
| **Directory Entry Contents** | Start Block Address & Length | Start Block & End Block | Start Block Number | Index Block Address / Inode Number |
| **Direct / Random Access** | **Fast** ($O(1)$ calculation) | **Very Slow** ($O(i)$ chain) | Moderate (Memory lookup) | **Fast** ($O(1)$ index lookup) |
| **External Fragmentation** | **High** (Requires compaction) | **None** | **None** | **None** |
| **Internal Fragmentation** | Only in the last block | Only in the last block | Only in the last block | In last block + entire unused index blocks |
| **Pointer Storage Overhead** | None | 4–8 bytes per data block | In-memory FAT array | 1 dedicated Index Block per file minimum |

---

### Question 2 (10 Marks)
**What do you mean by file management? Explain the various file directory structures (Single-Level, Two-Level, Hierarchical/Tree-Structured, Acyclic Graph, and General Graph) in an operating system along with common directory operations.**

*Source Alignment: University Special Re-Exam 2022–23 (Q7a), Mix PYQ Solutions (Q6).*

---

#### Solved Model Answer:

#### 1. Concept of File Management & Common Directory Operations (3 Marks)
**File Management** is the operating system subsystem responsible for organizing, storing, retrieving, manipulating, and protecting files on secondary storage. It maps abstract logical files onto physical storage blocks, manages metadata via directory structures, enforces access permissions, and controls space allocation.

A **Directory** is a specialized container file that maintains mappings between human-readable file names and physical file locations (such as inode numbers or disk block addresses).

##### Common System-Call Operations on Directories:
1. **Create (`mkdir`):** Allocates a new directory structure and initializes special default entries (`.` for current directory, `..` for parent directory).
2. **Delete (`rmdir`):** Removes an empty directory from the file system hierarchy and reclaims its disk space.
3. **Opendir / Readdir:** System calls allowing applications to open a directory stream and read its entries sequentially.
4. **Rename (`rename`):** Changes the name of an existing directory or file entry within the hierarchy.
5. **Link (`link`):** Creates an entry in a directory pointing to an existing file, enabling file sharing across paths.
6. **Unlink (`unlink`):** Removes a directory entry. If the link count reaches zero, the physical file data blocks are reclaimed.

---

#### 2. Detailed Analysis of Directory Structures (6 Marks)

##### A. Single-Level Directory
In a **Single-Level Directory**, all files reside in a single, flat root directory shared by all users on the system.

* **Advantages:** Extremely simple to implement; low lookup overhead for small file counts.
* **Disadvantages & Limitations:**
  * **Name Collision Problem:** Two users cannot create files with identical names (e.g., `test.c`).
  * **No User Grouping:** Files cannot be logically grouped by project, user, or file type.

##### B. Two-Level Directory
A **Two-Level Directory** isolates files by user. The master structure is a **Master File Directory (MFD)** containing pointers to individual **User File Directories (UFDs)**.

* **Mechanics:** When a user logs in, the OS opens their dedicated UFD. File names need only be unique within that user's UFD.
* **Advantages:** Completely eliminates name collisions between different users; provides user isolation.
* **Disadvantages:** Prevents easy file sharing between users; requires specifying full path names (e.g., `/UserA/file1`) to access files in another UFD.

##### C. Hierarchical / Tree-Structured Directory
In a **Hierarchical Directory**, the directory structure is organized as an arbitrary-depth tree rooted at a single **Root Directory (`/`)**. Directories contain both data files and subdirectories.

* **Pathnames:**
  * **Absolute Pathname:** Specifies the complete path starting from the root directory (e.g., `/usr/ast/courses/os/handout.txt`).
  * **Relative Pathname:** Specifies the path relative to the process's **Current Working Directory (CWD)** (e.g., `courses/os/handout.txt`).
* **Advantages:** Highly scalable; allows logical grouping of files; eliminates naming collisions across subdirectories.

##### D. Acyclic Graph Directory
An **Acyclic Graph Directory** extends the tree structure by allowing subdirectories and files to be shared concurrently between different parent directories without permitting cycles.

* **Sharing Mechanisms:**
  1. **Hard Links:** Directory entries point directly to the shared file's physical identifier (e.g., UNIX inode). The inode maintains a **Link Count**. Deleting a file decrements the count; space is reclaimed only when link count reaches zero.
  2. **Soft / Symbolic Links (Symlinks):** Directory entries point to a special link file containing the text string of the target file's path. If the target file is deleted, the symlink becomes a **Dangling Pointer**.
* **Advantages:** Flexible file sharing; avoids storing duplicate file copies.
* **Disadvantages:** Complex traversal algorithms; risk of dangling pointers.

##### E. General Graph Directory
A **General Graph Directory** relaxes the acyclic constraint, allowing directory links to form cycles or loops.

* **Problem:** Standard recursive tree-traversal algorithms (e.g., disk usage calculation, search) can enter infinite loops.
* **Garbage Collection & Cycle Detection:** Requires reference counting combined with full-scale graph garbage collection algorithms (e.g., mark-and-sweep) to detect unreachable isolated cycles and reclaim storage space.

---

#### 3. Summary Comparison Table of Directory Structures (1 Mark)

| Directory Structure | Naming Collision Risk | File Sharing Support | Search Efficiency | Cycle Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Single-Level** | **Extreme** (All names global) | None | Slow linear search | None |
| **Two-Level** | **Low** (Isolated per user) | Restricted / Difficult | Fast within UFD | None |
| **Hierarchical Tree**| **Zero** (Scoped to directory)| None | Efficient path traversal | None |
| **Acyclic Graph** | **Zero** | **Full** (Hard & Soft links) | Efficient | None (Acyclic) |
| **General Graph** | **Zero** | **Full** | Complex (Needs cycle check)| **High** (Needs Garbage Collection) |

---

### Question 3 (10 Marks)
**Explain the Virtual File System (VFS) architecture in Linux/UNIX operating systems. Describe the four primary VFS objects (Superblock, Inode, Dentry, and File) and explain how open-file tables manage concurrent file access.**

*Source Alignment: Technical Publications, TechNeo Exam Pack.*

---

#### Solved Model Answer:

#### 1. Need & Purpose of VFS Abstraction (2.5 Marks)
Modern operating systems must simultaneously support diverse physical file systems (such as Linux `ext4`, Windows `NTFS`, DOS `FAT32`, Network File System `NFS`, and optical `ISO9660`). Without an abstraction layer, applications would need custom code for every file system type.

The **Virtual File System (VFS)** is an object-oriented kernel abstraction layer that presents a single, uniform file system interface (`read()`, `write()`, `open()`, `close()`) to user-space applications regardless of the underlying physical file system or storage hardware.

```
+-----------------------------------------------------------------+
|                    USER SPACE APPLICATIONS                      |
|                  System Calls: open(), read(), write()          |
+-----------------------------------------------------------------+
                               |
                               v
+-----------------------------------------------------------------+
|                  VIRTUAL FILE SYSTEM (VFS)                      |
|       Provides uniform interface & object-oriented dispatch     |
+-----------------------------------------------------------------+
          /                    |                    \
         v                     v                     v
+-----------------+   +-----------------+   +-----------------+
|  ext4 Driver    |   |   NTFS Driver   |   |   NFS Driver    |
+-----------------+   +-----------------+   +-----------------+
         |                     |                     |
         v                     v                     v
+-----------------------------------------------------------------+
|               SECONDARY STORAGE / NETWORK MEDIA                 |
+-----------------------------------------------------------------+
```

---

#### 2. The Four Primary VFS Objects (5 Marks)

The Linux VFS uses four primary object types, each associated with an operations vector containing function pointers to physical driver implementations:

##### 1. Superblock Object (`struct super_block`)
* **Role:** Represents an entire mounted physical file system.
* **Information Stored:** Total block count, free block count, block size, file system status flags, and physical device identifier.
* **Operations Vector:** `struct super_operations` (contains function pointers for mounting, unmounting, allocating inodes, and syncing metadata).

##### 2. Inode Object (`struct inode`)
* **Role:** Represents a specific physical file or directory on disk.
* **Information Stored:** File size, device ID, owner UID/GID, access permissions, creation/modification timestamps, and disk block pointers.
* **Key Characteristic:** Stores all file attributes *except* the file name.
* **Operations Vector:** `struct inode_operations` (contains pointers for `create()`, `lookup()`, `link()`, `mkdir()`, `rmdir()`).

##### 3. Dentry Object (`struct dentry`)
* **Role:** Represents a single directory entry component in a pathname (e.g., `/usr`, `/bin`, `/python`).
* **Information Stored:** Maps a file name string to its corresponding `inode` pointer. Includes pointers to parent and child dentries.
* **Optimization:** Dentries are cached in RAM in the **Dentry Cache (`dcache`)** to dramatically speed up path lookup operations without reading physical disk blocks.
* **Operations Vector:** `struct dentry_operations` (contains pointers for `d_compare()`, `d_delete()`, `d_release()`).

##### 4. File Object (`struct file`)
* **Role:** Represents an open file instance created in memory when a process invokes `open()`.
* **Information Stored:** Current file position offset pointer (`f_pos`), access mode flags (read-only, write-only, append), reference count, user credential bindings, and pointer to the corresponding dentry.
* **Operations Vector:** `struct file_operations` (contains pointers for `read()`, `write()`, `seek()`, `mmap()`, `poll()`).

---

#### 3. Open-File Tables & Concurrent Access Management (2.5 Marks)

To manage files opened concurrently by multiple processes, the OS kernel uses a three-tier table hierarchy:

```
Process A                         System-Wide Open-File Table              System-Wide Inode Table
fd [0, 1, 2]                     +--------------------------+             +-----------------------+
  fd[3] -----------------------> | File Object 1 (Offset 100) | ----------> | Inode Object 101      |
                                 +--------------------------+             | (File: /doc/report)   |
Process B                        | File Object 2 (Offset 0)  | -----------/|                       |
  fd[3] -----------------------> +--------------------------+              +-----------------------+
```

1. **Per-Process File Descriptor Table:** Located inside the process's PCB (`task_struct`). Maps integer file descriptors (`fd 0, 1, 2, 3...`) to entries in the system-wide open file table.
2. **System-Wide Open-File Table:** Maintains one `struct file` instance for every active `open()` call. It tracks per-process file offset pointers (`f_pos`) and access modes.
3. **System-Wide Inode Table:** Stores in-memory `struct inode` instances. If two distinct processes open the same file concurrently, they get separate `file` objects (with independent offset pointers), but both `file` objects point to the **same shared entry** in the system-wide inode table.

---

## SECTION 2: 5-MARK UNIVERSITY SHORT ANSWER & CONCEPTUAL QUESTIONS

### Question 4 (5 Marks)
**Summarize the main file attributes managed by a file system and explain the common system-call operations that can be performed on a file.**

*Source Alignment: University Final Exam AY 2024–25 (Q7c), Final Exam AY 2025–26 (Q7c), FYIT Nov-2016.*

---

#### Solved Model Answer:

#### 1. Main File Attributes (2.5 Marks)
A file system manages metadata properties associated with every file object:
* **Name:** Character string representation human users use to identify the file.
* **Identifier:** System-wide unique numeric tag (e.g., inode number) used internally by the kernel.
* **Type:** Identifies file encoding or structure (e.g., executable `.exe`, text `.txt`, directory).
* **Location:** Pointer address to the storage device and physical disk sectors containing the file data.
* **Size:** Current byte count of the file data (and maximum size limit).
* **Protection:** Access control bits determining Read (`r`), Write (`w`), and Execute (`x`) rights for Owner, Group, and Others.
* **Timestamps & User ID:** Record dates/times of file creation, last access, and last modification, alongside Owner UID.

---

#### 2. Common System-Call File Operations (2.5 Marks)
Operating systems provide primitive system calls to perform actions on files:
1. **Create:** Allocates physical disk space and creates a new metadata entry in the directory structure.
2. **Open:** Loads file attributes and block pointers from disk into kernel memory, returning a file descriptor integer.
3. **Read:** Reads $N$ bytes from the current file offset pointer into a user buffer, advancing the file offset pointer.
4. **Write:** Writes $N$ bytes from a user buffer into the file at the current offset pointer, extending file size if needed.
5. **Reposition (Seek / `lseek`):** Moves the current file position pointer to a specified logical offset without reading/writing data.
6. **Delete / Truncate:** Deletes the directory entry, reclaims physical storage blocks, or resets file length to 0 while maintaining attributes.
7. **Close:** Frees the per-process file descriptor and decrements system-wide open file table reference counts.

---

### Question 5 (5 Marks)
**Explain Record Blocking and its three types (Fixed-Length Blocking, Variable-Length Spanned Blocking, and Variable-Length Unspanned Blocking) in file management.**

*Source Alignment: OS Assignment 1 (Q9), Technical Publications.*

---

#### Solved Model Answer:

#### 1. Concept of Record Blocking & Blocking Factor (1.5 Marks)
In secondary storage management, applications process data in **Logical Records**, whereas storage hardware transfers data in fixed **Physical Blocks** (e.g., 512 bytes or 4 KB disk sectors).

**Record Blocking** is the technique of packing multiple logical records into a single physical block to maximize I/O throughput and minimize hardware Inter-Block Gaps (IBG).

The average number of records per block is called the **Blocking Factor ($F$)**:

$$F = \lfloor \frac{\text{Physical Block Size}}{\text{Logical Record Size}} \rfloor$$

---

#### 2. Types of Record Blocking (3 Marks)

```
1. Fixed-Length Blocking:
   [ Block 1: Record 1 | Record 2 | Record 3 | Wasted Gap ]

2. Variable-Length Spanned Blocking:
   [ Block 1: Record 1 | Record 2 (Part A - Pointer ->) ] ---> [ Block 2: Record 2 (Part B) | Record 3 ]

3. Variable-Length Unspanned Blocking:
   [ Block 1: Record 1 (Large) | Wasted Unused Gap      ] ---> [ Block 2: Record 2 ]
```

##### A. Fixed-Length Blocking
* **Structure:** Records have a fixed byte length, and an integral number of records are stored per block.
* **Storage Effect:** Unused space remains at the end of each block if the block size is not an exact multiple of the record size (**Internal Fragmentation**).
* **Usage:** Standard approach for simple sequential files with fixed record schemas.

##### B. Variable-Length Spanned Blocking
* **Structure:** Records have variable byte lengths and are packed continuously without gaps.
* **Spanning Mechanism:** If an incoming record is too large to fit in the remaining space of a block, it is **split (spanned)** across to the next block. A pointer at the end of the first block links to the continuation block.
* **Storage Effect:** Zero wasted space due to record fitting.
* **Trade-off:** Reading or updating a spanned record requires **two physical disk I/O operations**.

##### C. Variable-Length Unspanned Blocking
* **Structure:** Records have variable byte lengths, but **spanning across block boundaries is forbidden**.
* **Storage Effect:** If a record cannot fit in the remaining space of a block, that remaining space is left **unused (wasted gap)**, and the record begins at the start of the next block.
* **Constraint:** A single logical record size cannot exceed the capacity of a single physical block.

---

#### 3. Blocking Types Comparison Table (0.5 Marks)

| Blocking Scheme | Record Size | Spanning Allowed? | Storage Overhead | I/O Operations per Record |
| :--- | :--- | :---: | :--- | :---: |
| **Fixed-Length** | Fixed | No | Internal fragmentation at block end | 1 I/O |
| **Variable Spanned** | Variable | **Yes** | **None** (Tightly packed) | 2 I/Os for spanned records |
| **Variable Unspanned**| Variable | No | Wasted unused gap per block | 1 I/O |

---

### Question 6 (5 Marks)
**Explain Free-Space Management techniques in operating systems, specifically Bit Vector / Bitmap, Linked List (Free-List), Grouping, and Counting.**

*Source Alignment: Technical Publications, TechNeo Exam Pack.*

---

#### Solved Model Answer:

#### 1. Need for Free-Space Management (1 Mark)
To allocate disk blocks quickly when files are created or expanded, the operating system maintains a **Free-Space Management** structure tracking all unallocated physical disk blocks.

---

#### 2. Four Primary Free-Space Management Techniques (4 Marks)

##### A. Bit Vector / Bitmap
The free-space map is implemented as an array of bits, where each bit corresponds to a physical disk block:
* $\text{Bit}[i] = 1 \implies \text{Block } i \text{ is Free}$
* $\text{Bit}[i] = 0 \implies \text{Block } i \text{ is Allocated}$

* **Block Number Calculation:**

$$\text{Block No.} = (\text{Number of words with 0}) \times (\text{Bits per word}) + (\text{Offset of first 1-bit})$$

* **Pros:** Highly efficient; supported by hardware instructions (e.g., find-first-set bit).
* **Cons:** Requires keeping the bitmap in RAM for fast access, which consumes significant memory on massive terabyte disks.

##### B. Linked List (Free-List)
All free disk blocks are chained together in a **Linked List**.
* **Mechanics:** The directory or superblock stores a pointer to the first free block. Each free block contains a pointer address to the next free block on disk.
* **Pros:** Zero memory overhead in RAM (pointers are stored inside unused free disk blocks).
* **Cons:** Inefficient traversal; gathering $N$ free blocks requires $N$ individual disk reads.

##### C. Grouping
A modification of the linked list approach that stores multiple pointers in a single block.
* **Mechanics:** The first free block stores the disk addresses of $n$ free blocks. The first $n-1$ entries are actual free blocks, and the $n^{\text{th}}$ entry points to another block containing the addresses of the next $n$ free blocks.
* **Pros:** The addresses of a large group of free blocks can be fetched in a single disk read.

##### D. Counting
Takes advantage of the fact that multiple contiguous blocks are often created or freed simultaneously.
* **Mechanics:** Instead of tracking individual block addresses, the free list stores entries containing:
  `[ Starting Free Block Address | Count of Contiguous Free Blocks ]`
* **Pros:** Drastically reduces free-list size when contiguous allocation is used.

---

### Question 7 (5 Marks)
**What is an Access Control List (ACL)? Explain file access rights and how user classifications (Owner, Group, World) are managed in UNIX file protection.**

*Source Alignment: Darshan Institute / TechNeo Security & File Systems.*

---

#### Solved Model Answer:

#### 1. Concept of Access Control List (ACL) (2 Marks)
In protection systems, the **Access Matrix** defines user rights over file objects. Because the access matrix is extremely sparse, operating systems implement it using **Access Control Lists (ACLs)**.

An **ACL** is a security list attached to each file object that explicitly specifies which domains or user identities are granted or denied access, alongside their specific permissions:
```
File F1 -> [ User A: Read, Write ; User B: Read ]
File F2 -> [ User A: Read ; User B: Read, Write ; User C: Read ]
```

---

#### 2. UNIX File Protection Scheme (3 Marks)

UNIX/Linux uses a condensed, 9-bit Access Control classification scheme based on three user classes:

##### User Classifications
1. **Owner (`u`):** The user who created or currently owns the file.
2. **Group (`g`):** A set of users sharing group administrative privileges over the file.
3. **Others / World (`o`):** All other general users registered on the system.

##### Access Rights & Bit Notation
Each user class possesses three permission bits:
* **Read (`r` / 4):** Grants permission to read file data or list directory contents.
* **Write (`w` / 2):** Grants permission to modify file data or create/delete directory entries.
* **Execute (`x` / 1):** Grants permission to execute a file as a program or traverse a directory path.

```
9-Bit Permission Representation:  [ r w x ] [ r - x ] [ r - - ]
User Classification:               Owner      Group      Others
Octal Value:                        7          5          4
```

* **System Call (`chmod`):** Command used to modify access control bits (e.g., `chmod 755 file.txt` grants `rwx` to Owner, `r-x` to Group, and `r-x` to Others).

---

### Question 8 (5 Marks)
**Differentiate between Sequential Access, Direct / Random Access, and Indexed Sequential Access methods for files.**

*Source Alignment: Textbook Exercises / Exam Pack (Silberschatz / Tanenbaum).*

---

#### Solved Model Answer:

Operating systems support three fundamental **File Access Methods** determining how records within a file are read and processed:

#### 1. Sequential Access
* **Mechanics:** Information in the file is processed in order, one record after another. A read call reads the next record and automatically increments the current file pointer ($cp = cp + 1$). Rewinding or skipping $N$ records requires sequential pointer updates.
* **Hardware Analogy:** Magnetic tape storage.

#### 2. Direct / Random Access
* **Mechanics:** The file is viewed as a numbered sequence of disk blocks or records. Applications can read or write blocks in any arbitrary order by specifying the logical block number $n$ (e.g., `read n`). The pointer jumps directly ($cp = n$) in $O(1)$ time.
* **Hardware Analogy:** Magnetic hard disks and Solid State Drives.

#### 3. Indexed Sequential Access
* **Mechanics:** An index file is built on top of a sequential file. The index contains pointers to key record blocks. To find a record, the OS searches the primary index first, gets the block pointer, and then performs a short sequential search inside that target block.
* **Usage:** Large database applications requiring fast key-based record searches.

---

#### 4. Structured Comparison Matrix (1 Mark)

| Feature / Criteria | Sequential Access | Direct / Random Access | Indexed Sequential Access |
| :--- | :--- | :--- | :--- |
| **Record Access Order** | Strict sequential order | Arbitrary / Random order | Key-indexed search then sequential |
| **Search Time Complexity**| **Slow** ($O(N)$ traversal) | **Fast** ($O(1)$ block lookup) | **Moderate** ($O(\log N)$ index search) |
| **File Pointer Mechanics**| Auto-increment ($cp = cp + 1$) | Direct jump ($cp = n$) | Index lookup $\to$ pointer jump |
| **Suitable File Systems** | Linked allocation, Tapes | Contiguous & Indexed Allocation | Indexed Allocation / FAT |
| **Primary Use Cases** | Compilers, video/audio logs | Databases, virtual memory paging | Database transaction management |
