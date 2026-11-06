# Operating Systems (OS) - Unit 7: File Management
## Comprehensive Master Study Notes & University Exam Guide
### Course Outcome: CO-3 (Simulate Memory Management, I/O Management, and File Management Strategies)

---

## SECTION 1: OVERVIEW & BASIC FILE CONCEPTS

### 1.1 Concept of a File
In an operating system, a **File** is a named collection of related information that is recorded on secondary storage (such as a hard disk, SSD, or optical drive). From the perspective of a user or application, a file represents a contiguous logical address space that abstracts away the physical properties of underlying storage media.

```
+-----------------------------------------------------------------+
|                        USER / APPLICATION                       |
|  Logical View: Named stream of bytes / structured records       |
+-----------------------------------------------------------------+
                                |
                                v System Calls (read, write, seek)
+-----------------------------------------------------------------+
|                     FILE SYSTEM SUBSYSTEM                       |
|  Maps logical file offsets to physical disk block addresses     |
+-----------------------------------------------------------------+
                                |
                                v Block I/O Requests
+-----------------------------------------------------------------+
|                    PHYSICAL STORAGE MEDIA                       |
|  Sectors, Tracks, Cylinders, Flash Blocks                       |
+-----------------------------------------------------------------+
```

#### Key Characteristics of Files:
* **Persistence:** Data written to a file remains intact after system shutdowns or process terminations.
* **Abstraction:** The OS hides hardware-specific details (sector size, cylinder layout, flash pages) behind a uniform file abstraction.
* **Name & Space:** Files are identified by symbolic names within a hierarchical directory structure.

---

### 1.2 File Attributes
Every file is defined by a set of metadata properties maintained by the operating system file system layer:

| File Attribute | Description & Purpose |
| :--- | :--- |
| **Name** | Human-readable symbolic string used to identify the file within a directory. |
| **Identifier** | Unique system-internal number (e.g., inode number or file ID) used by the kernel to reference the file. |
| **Type** | Indicates the nature or format of the file (e.g., text, executable, directory, system device). |
| **Location** | Pointer to the physical disk device and starting block addresses where file data resides. |
| **Size** | Current size of the file in bytes, words, or physical disk blocks. |
| **Protection Flags** | Access control permissions determining who can read, write, execute, or modify the file. |
| **Timestamps** | Historical tracking data including Creation Time, Last Modification Time, and Last Access Time. |

---

### 1.3 Essential File Operations
The operating system provides a set of system calls allowing programs to manipulate files:

1. **Create:** Allocates a new entry in the directory structure and assigns initial metadata without allocating data blocks until writing occurs.
2. **Write:** Writes data at the current file position pointer, increasing file size and allocating physical disk blocks as needed.
3. **Read:** Reads data from the current file position pointer into a user memory buffer and advances the pointer.
4. **Reposition (Seek):** Modifies the current file position pointer to a specified target offset without performing I/O.
5. **Delete:** Removes the directory entry, reclaims allocated physical blocks to the free-space list, and destroys metadata.
6. **Truncate:** Clears file contents and resets file size to zero while retaining the existing directory entry and metadata.
7. **Open:** Searches the directory structure, checks access permissions, and copies file metadata into kernel RAM tables for fast execution.
8. **Close:** Flushes buffered modifications to disk, decrements the active open count, and frees kernel table entries.

---

### 1.4 File Types, Extensions, and Internal File Structures

```
File Structure Progression:
1. Byte Sequence (Unstructured):
   [ Byte 0 ][ Byte 1 ][ Byte 2 ][ Byte 3 ] ... [ Byte N ]

2. Record Sequence (Fixed/Variable Length):
   [ Record 1: 80B ][ Record 2: 120B ][ Record 3: 80B ]

3. Tree Structure (Complex / B-Tree):
   [ Root Key Index ] ---> [ Sub-Index Block ] ---> [ Data Records ]
```

* **Byte Sequence:** The file is viewed as an unstructured series of 8-bit bytes (used by UNIX, Linux, and Windows). The OS imposes no internal format; application software interprets the meaning of bytes.
* **Record Sequence:** The file is viewed as a sequence of fixed-length or variable-length logical records.
* **Tree Structure:** The file is organized as a hierarchical tree of records indexed by key fields (e.g., IBM mainframe ISAM files).

---

## SECTION 2: FILE ACCESS METHODS

The access method dictates the logical sequence in which records or bytes inside a file are retrieved and processed.

```
Sequential Access:
  [ Record 0 ] ---> [ Record 1 ] ---> [ Record 2 ] ---> [ Record 3 ]
  (Must read records in linear order)

Direct / Random Access:
  Target Block N = Direct Address Calculation (Offset x Record Size)
  (Jump directly to Block N without reading intermediate blocks)
```

### 2.1 Sequential Access
* **Mechanism:** Data is processed in order, one byte or record after another.
* **Operations:** `read_next()` advances the file pointer automatically; `write_next()` appends data at the end of the file. `rewind()` resets the pointer to the beginning.
* **Best Used For:** Sequential media like magnetic tapes, continuous log streams, text processing, and audio/video playback.

---

### 2.2 Direct Access (Random Access)
* **Mechanism:** Allows programs to read or write disk blocks in any arbitrary order without traversing intermediate records.
* **Operations:** `read(n)` and `write(n)` take an explicit block number `n` as an argument. Alternatively, applications call `seek(offset)` followed by standard read or write calls.
* **Best Used For:** Immediate key lookups, relational database management systems (RDBMS), and swap files.

---

### 2.3 Indexed Sequential Access
* **Mechanism:** Combines sequential convenience with direct index efficiency. An **Index Table** contains pointers to primary data blocks sorted by key fields.
* **Execution Flow:** To locate record $K$, the OS searches the Index Table to find the target block address, jumps directly to that block, and performs a short sequential search within the block.

---

## SECTION 3: FILE DIRECTORIES & SYSTEM STRUCTURE

A directory acts as a symbol table that maps human-readable file names to their system-internal metadata records (File Control Blocks or Inodes).

### 3.1 Directory System Operations
The operating system provides specific system primitives for directory management:
* **Create File / Mkdir:** Adds a new named node to the directory hierarchy.
* **Delete File / Rmdir:** Removes a named entry from the directory structure.
* **Opendir / Readdir:** Opens a directory stream and iterates through its entries.
* **Rename:** Changes the symbolic name associated with a file entry.
* **Link:** Creates a secondary name pointer (hard or symbolic link) referencing an existing file.
* **Unlink:** Removes a link reference, deleting the physical file only when the link count reaches zero.

---

### 3.2 Directory Structure Architectures

```
1. Single-Level Directory:
   [ Root Directory ] ---> [ File A ][ File B ][ File C ][ File D ]

2. Two-Level Directory:
   [ Root Directory ] ---> [ User 1 Directory ] ---> [ File A ][ File B ]
                      ---> [ User 2 Directory ] ---> [ File A ][ File C ]

3. Hierarchical / Tree-Structured Directory:
   [ Root / ] ---> [ /bin ]
              ---> [ /home ] ---> [ /user1 ] ---> [ file.txt ]

4. Acyclic Graph Directory (Sharing via Links):
   [ User A Directory ] ---(Hard Link)---> [ Shared File X ]
   [ User B Directory ] ---(Soft Link)---> [ Shared File X ]
```

| Structure Type | Architecture & Working Principles | Primary Advantages | Main Disadvantages |
| :--- | :--- | :--- | :--- |
| **Single-Level Directory** | All files reside in a single flat directory namespace. | Extremely simple to implement. | Name collision issues; poor organization for large files. |
| **Two-Level Directory** | Master Directory points to separate User File Directories (UFD). | Prevents name collisions between different users. | Isolates users; impedes file sharing between users. |
| **Hierarchical / Tree Directory** | Tree structure of directories allowing subdirectories of arbitrary depth. | Excellent organizational grouping; uses Absolute and Relative paths. | Traversing deep directory trees requires multiple disk seeks. |
| **Acyclic Graph Directory** | Allows directories to share sub-files/directories via Hard or Soft Links. | Flexible collaboration and shared file access without duplicate copies. | Dangling pointers; cycles during recursive directory traversals. |
| **General Graph Directory** | Graph structure allowing arbitrary links without cycle restriction. | Maximum flexibility for complex links. | Requires expensive garbage collection algorithms or cycle detection. |

---

#### Hard Links vs. Soft (Symbolic) Links

```
Hard Link:
  [ Directory Entry A ] --+
                          |---> [ Physical Inode 1042 ] ---> [ Disk Data Blocks ]
  [ Directory Entry B ] --+     (Link Count = 2)

Soft (Symbolic) Link:
  [ Directory Entry C ] ---> [ Inode 2050 ] ---> [ Path String "/home/user/fileA" ]
                                                       |
                                                       v
                                            [ Target Inode 1042 ]
```

* **Hard Link:** A directory entry that points directly to the physical inode of an existing file. The inode tracks a reference counter (`link_count`). The physical data persists until all hard links are unlinked (`link_count == 0`).
* **Soft Link (Symbolic Link / Shortcut):** A special file containing a text path string pointing to another file. If the original target file is deleted or moved, the symbolic link becomes a **dangling link**.

---

### 3.3 Directory Implementation Methods
1. **Linear List:** Directory entries are stored sequentially in a fixed or growing list. Finding an entry requires linear search $O(N)$.
2. **Hash Table:** Directory entries are stored in a hash array indexed by a hash function computed from the filename. Offers $O(1)$ search performance. Collisions are handled via chaining or open addressing.

---

## SECTION 4: FILE ALLOCATION METHODS

File allocation techniques determine how secondary storage blocks are assigned to files to balance access speed, space utilization, and dynamic file expansion.

---

### 4.1 Contiguous Allocation

```
Directory Entry:
+-----------+-------------+--------+
| File Name | Start Block | Length |
+-----------+-------------+--------+
|  report   |     19      |   6    |  --> Occupies Blocks: 19, 20, 21, 22, 23, 24
+-----------+-------------+--------+
```

* **Mechanism:** Each file occupies a contiguous set of physical disk blocks.
* **Address Mapping:** To access block offset $i$ of a file starting at block $b$:
  $$	ext{Physical Block Address} = b + i$$
* **Pros:** Excellent I/O performance; minimal seek delay; supports direct access in $O(1)$ calculation time.
* **Cons:** Causes severe **External Fragmentation** over time; requires pre-allocating file size upfront.
* **Enhancement (Extents):** Extends contiguous allocation by assigning disk space in large contiguous chunks called **extents**, linking additional extents as the file grows.

---

### 4.2 Linked (Chained) Allocation

```
Directory Entry:
+-----------+-------------+-----------+
| File Name | Start Block | End Block |
+-----------+-------------+-----------+
|   data    |      9      |    25     |  --> Block 9 -> Block 16 -> Block 1 -> Block 10 -> Block 25 (-1/EOF)
+-----------+-------------+-----------+
```

* **Mechanism:** Files are stored as a linked list of disk blocks scattered across the drive. Each block contains a pointer field to the next block address.
* **FAT Variant (File Allocation Table):** Pointers are removed from individual data blocks and gathered into an in-memory **File Allocation Table (FAT)**.
* **Pros:** Zero external fragmentation; files can grow dynamically without declaring size upfront.
* **Cons:** Extremely slow direct access ($O(i)$ chain traversal needed); pointer storage overhead; corrupted pointers break the remaining file chain.

---

### 4.3 Indexed Allocation (and UNIX Inode Architecture)

```
Directory Entry:
+-----------+-------------+
| File Name | Index Block |
+-----------+-------------+
|   image   |     19      |
+-----------+-------------+

Index Block (Block 19):
[ Pointer 0 ] -> Block 9
[ Pointer 1 ] -> Block 16
[ Pointer 2 ] -> Block 1
[ Pointer 3 ] -> Block 10
[ Pointer 4 ] -> Block 25
```

* **Mechanism:** Consolidates all block pointers for a file into a single dedicated **Index Block**.
* **Pros:** Supports fast direct access ($O(1)$ lookup inside index block); eliminates external fragmentation.
* **Cons:** High index block overhead for small files.

#### UNIX Inode (Combined Indexing Scheme)

```
                       UNIX INODE STRUCTURE
                       
  +-------------------------------------------------+
  | File Metadata (Permissions, Size, Owner, Time)  |
  +-------------------------------------------------+
  | Direct Block Pointer 0                          | ---> [ Data Block ]
  | Direct Block Pointer 1                          | ---> [ Data Block ]
  | ...                                             |
  | Direct Block Pointer 11                         | ---> [ Data Block ]
  +-------------------------------------------------+
  | Single Indirect Pointer                         | ---> [ Index Block ] ---> [ Data Blocks ]
  +-------------------------------------------------+
  | Double Indirect Pointer                         | ---> [ Index Block ] ---> [ Index Blocks ] ---> [ Data Blocks ]
  +-------------------------------------------------+
  | Triple Indirect Pointer                         | ---> [ 3-Level Index Block Hierarchy ]
  +-------------------------------------------------+
```

---

### 4.4 Comprehensive Allocation Method Comparison

| Criterion | Contiguous Allocation | Linked Allocation | Indexed Allocation (UNIX Inode) |
| :--- | :--- | :--- | :--- |
| **Pre-allocation Needed?** | Yes | No | No |
| **Sequential Access Speed** | **Fastest** | Fast | Moderate |
| **Direct Access Speed** | **Fast ($O(1)$)** | **Very Slow ($O(i)$)** | **Fast ($O(1)$)** |
| **External Fragmentation** | **High** | **None** | **None** |
| **Pointer Overhead** | None | 4 bytes per block | Full index block per file |

---

## SECTION 5: FREE-SPACE MANAGEMENT

The operating system tracks unused disk blocks using a **Free-Space List**.

```
1. Bit Vector / Bitmap:
   Block Status: [ 0:Used ][ 1:Free ][ 1:Free ][ 0:Used ][ 1:Free ]
   Bitmap Word: 01101... (1 bit per physical block)

2. Linked Free List:
   [ Free Block 2 ] ---> [ Free Block 5 ] ---> [ Free Block 8 ] ---> [ Free Block 11 ]

3. Grouping:
   [ First Free Block ] ---> Stores Addresses of N-1 Free Blocks + Pointer to Next Group Block

4. Counting:
   [ Start Free Block: 12 ][ Continuous Free Count: 8 ]
```

### 5.1 Free-Space Techniques

1. **Bit Vector / Bitmap:** A string of bits where `1` indicates a free block and `0` indicates an allocated block. Compact and fast, but requires hardware bit-scan instructions.
2. **Linked List (Free List):** A linked chain connecting all free disk blocks. Allocating or freeing a block involves updating head pointers without external fragmentation.
3. **Grouping:** Stores the addresses of $N$ free blocks inside the first free block. The $N^{	ext{th}}$ entry is a pointer to another block containing the next group of free block addresses.
4. **Counting:** Stores the starting disk address of a contiguous free region along with a count of contiguous free blocks, reducing table size when contiguous runs exist.

---

## SECTION 6: FILE SHARING, ACCESS CONTROL & PROTECTION

In multi-user operating systems, access control mechanisms protect files against unauthorized reading, modification, or deletion.

### 6.1 Access Rights & User Classifications
Permissions are divided into functional operations:
* **Read (r):** Read file content or view directory listing.
* **Write (w):** Modify file content or add/remove files in a directory.
* **Execute (x):** Execute binary program files or traverse directory trees.

#### UNIX User Classifications:
1. **Owner (User / u):** The user who created the file.
2. **Group (g):** A defined collection of users sharing access permissions.
3. **World (Others / o):** All other system users.

```
UNIX Permission Representation:
   File Type    Owner (u)    Group (g)    Others (o)
      -            rwx          r-x          r--
   (Regular)    (Read/Write/ (Read/Exec   (Read Only)
                 Execute)     Only)
```

---

### 6.2 Access Control Lists (ACL)
An **Access Control List (ACL)** attaches a detailed list to every file naming specific users/groups and their explicit permissions (e.g., `User Alice: Read/Write`, `User Bob: Read-Only`). Provides fine-grained security, but introduces table storage overhead.

---

## SECTION 7: FILE SYSTEM IMPLEMENTATION & SECONDARY STORAGE

### 7.1 System Data Structures & File Control Block (FCB)

```
Kernel Memory & Disk Data Structures:

Disk:
  +-------------------------------------------------------------+
  | Boot Block | Superblock | Inode Table / FCB | Data Blocks   |
  +-------------------------------------------------------------+

Kernel RAM:
  [ User Process File Descriptor Table ] 
                 |
                 v
  [ System-Wide Open-File Table ] ---> [ In-Memory FCB / Inode Table ]
```

* **File Control Block (FCB):** On-disk structure containing permissions, size, dates, and block pointers for a file (called an Inode in UNIX).
* **System-Wide Open-File Table:** Maintains an entry for every file open across the entire OS, tracking open count and physical lock status.
* **Per-Process File Table:** Maps process file descriptors to entries in the System-Wide Open-File Table, tracking current read/write offset pointers.

---

### 7.2 Virtual File System (VFS) Architecture

```
                 USER APPLICATIONS
                         |
                         v System Calls (read, write)
          +------------------------------+
          |  VIRTUAL FILE SYSTEM (VFS)   |
          |  (Provides Uniform V-Node)   |
          +------------------------------+
             /           |                        v            v             v
       [ ext4 FS ]   [ NTFS FS ]   [ FAT32 FS ]
```

The **Virtual File System (VFS)** layer introduces an object-oriented abstraction that hides specific file system implementations behind a uniform kernel API (`vnode` interface). User programs issue standardized system calls that VFS translates into filesystem-specific drivers (`ext4`, `NTFS`, `NFS`).

---

### 7.3 Record Blocking Methods
* **Fixed-Length Blocking:** Fixed-size logical records are packed into physical blocks. Leaves small internal fragmentation at block ends.
* **Variable-Length Spanned Blocking:** Variable-size records are packed continuously; records larger than remaining block space are **spanned across block boundaries** using pointers. Zero wasted space, but requires multiple I/Os per record.
* **Variable-Length Unspanned Blocking:** Variable-size records are packed without spanning. If a record does not fit in remaining block space, that space is left unused, and the record starts at the next block.

---

## SECTION 8: UNIVERSITY TERM-END EXAM QUESTION BANK & MODEL ANSWERS

### Question 1 (10 Marks):
**Explain Contiguous, Linked, and Indexed File Allocation methods in detail with clean diagrams. Compare them on the basis of access speed, external fragmentation, and direct access support.**

#### Model Answer Summary:
1. **Contiguous Allocation:** Blocks stored sequentially. $O(1)$ direct access formula $b + i$. High external fragmentation.
2. **Linked Allocation:** Blocks connected via pointers (or FAT). Zero external fragmentation. Poor direct access ($O(i)$).
3. **Indexed Allocation:** Consolidated pointers inside Index Block / UNIX Inode. Fast $O(1)$ direct access without external fragmentation.

---

### Question 2 (10 Marks):
**Explain the structure of UNIX Inode with a neat diagram. How does it support small, medium, large, and extremely large files?**

#### Model Answer Summary:
* Contains **Direct Pointers** (typically 12) for fast small-file access.
* Contains **Single Indirect Pointer** for medium files.
* Contains **Double Indirect Pointer** for large files.
* Contains **Triple Indirect Pointer** for multi-gigabyte/terabyte files.

---

### Question 3 (5 Marks):
**Differentiate between Hard Links and Soft (Symbolic) Links.**

#### Model Answer Summary:
* **Hard Link:** Points directly to physical inode; increments link count; valid only within the same filesystem.
* **Soft Link:** Separate file containing path text string; dangling link if original target deleted; works across network/filesystems.

---

### Question 4 (5 Marks):
**Explain the role and architecture of Virtual File System (VFS) in Operating Systems.**

#### Model Answer Summary:
Provides a unified object-oriented interface (`vnode`) that abstracts underlying file system drivers (`ext4`, `NTFS`, `FAT32`), allowing applications to perform operations seamlessly across heterogeneous storage.
