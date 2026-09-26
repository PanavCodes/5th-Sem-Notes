# Operating Systems — Unit 5: Memory Management System — Exam-Oriented Numericals Workbook

> **Restoration and source note.** This is an expanded repair of the attached workbook: all 16 problems, topic areas, comparison tables, complete reference strings and detailed working have been retained or rebuilt. Its original missing inputs cannot be verified from the unattached exam papers, lab manuals or books. Figures reconstructed from surviving arithmetic are identified below; illustrative additions are labelled practice data. No example is asserted to be an original exam question.

## Contents

1. [Document structure and source protocol](#1-document-structure-and-source-protocol)
2. [Source-status audit matrix](#2-source-status-audit-matrix)
3. [Section I: Partitioning and contiguous allocation](#3-section-i-partitioning-and-contiguous-allocation)
4. [Section II: Paging and address translation](#4-section-ii-paging-and-address-translation)
5. [Section III: TLB and effective access time](#5-section-iii-tlb-and-effective-access-time)
6. [Section IV: Segmentation](#6-section-iv-segmentation)
7. [Section V: Demand paging](#7-section-v-demand-paging)
8. [Section VI: Page replacement](#8-section-vi-page-replacement)
9. [Section VII: Coverage, correction and verification log](#9-section-vii-coverage-correction-and-verification-log)

## 1. Document structure and source protocol

- **Verified PYQ** requires the actual original exam paper, identical question wording and inputs. **None is independently verified in this revision.**
- **Lab exercise (attribution unverified)** means the previous file associated the example with a lab manual; that manual was not supplied here. A lab exercise is not automatically a PYQ.
- **Reported source (verification pending)** records an attribution *made by the original workbook*, not a checked quotation or a confirmed PYQ.
- **Practice / reconstructed problem** identifies a complete self-contained example reconstructed from figures surviving in the workbook, or explicitly added illustrative data. It is not an exam-paper transcription.
- Allocations use **split free holes**, not indivisible fixed partitions. A failed process stays unallocated; later requests are still assessed. Hole indices remain fixed in physical order. For all page-replacement traces, empty frames fill lowest-numbered first and initial loads count as faults.

## 2. Source-status audit matrix

| Problem | Topic | Attribution in original file (not independently checked) | Status in this workbook |
|---|---|---|---|
| 1.1 | Five-hole placement | Lab manual Exp 8 (claimed in source file) | Lab exercise attribution unverified; inputs reconstructed |
| 1.2 | Six-hole placement | NMIMS/GTU (claimed in source file) | Practice reconstruction; original wording and data unverified |
| 1.3 | Buddy allocation | Textbooks (claimed in source file) | Practice reconstruction |
| 1.4 | Fragmentation and compaction | GTU/TechNeo (claimed in source file) | Practice reconstruction; attributed exam source unverified |
| 2.1 | Paging address calculation | Course notes/Technical Publications (claimed) | Practice reconstruction |
| 2.2 | Paging bit mathematics | Textbook/final exam (claimed) | Practice reconstruction; RAM value explicitly illustrative |
| 2.3 | Hierarchical paging | Textbook (claimed) | Practice reconstruction |
| 3.1 | TLB EAT | 2024–25 Q3b (claimed) | Practice reconstruction; exact paper numerical unverified |
| 3.2 | TLB hit-ratio threshold | Textbook (claimed) | Practice reconstruction |
| 4.1 | Segmentation bounds | Textbook/TechNeo (claimed) | Practice reconstruction |
| 4.2 | Paging versus segmentation | Course exercises (claimed) | Practice example expanded |
| 5.1 | Demand-paging EAT | Mid-sem/textbook (claimed) | Practice reconstruction |
| 5.2 | Dirty-page latency | Textbook (claimed) | Practice reconstruction |
| 6.1 | 15-reference FIFO/LRU/OPT | Lab manual Exp 9 problem 1 (claimed) | Lab exercise attribution unverified; not a verified PYQ |
| 6.2 | 20-reference FIFO/LRU | Final exam/lab (claimed) | Reference string preserved; original-paper status unverified |
| 6.3 | 12-reference Belady anomaly | Lab manual Exp 9 problem 2 (claimed) | Lab exercise attribution unverified; not a verified PYQ |

## 3. Section I: Partitioning and contiguous allocation

### Problem 1.1 — First Fit, Best Fit, Worst Fit and Next Fit: five holes

**Source:** Earlier workbook calls this OS Lab Experiment 8 Problem 1; the manual and original question are not available here. **Practice reconstruction:** holes H2–H5 = 500/200/300/600 KB and requests 212/417/112/426 KB can be recovered from surviving placements. Hole H1 is not recoverable, but the reported First Fit and Best Fit decisions imply 0 ≤ H1 < 112 KB; the wording below is reconstructed, not quoted verbatim.

**Question.** Free holes H1–H5 have sizes x, 500, 200, 300 and 600 KB (where 0 ≤ x < 112 KB) in that order. Processes P1–P4 request 212, 417, 112 and 426 KB. Simulate all four placement strategies, including free-hole states and allocation failures. For this *particular sequence*, which strategy accepts the most requests?

**Convention:** holes are processed in order H1 … H5. A fitting allocation splits that hole. Equal-size Best/Worst Fit candidates use the lowest hole number. For Next Fit the cursor starts at H1, and after allocation the next search **includes the remaining portion of the last chosen hole**; on failure the cursor does not move.

Initial holes (KB): `[x, 500, 200, 300, 600]`, where `0 ≤ x < 112`. Requests (KB): `[212, 417, 112, 426]`. Total initial free memory: `(1600+x) KB`.

##### First Fit — complete step-by-step allocation
| Step and request | Order searched / eligible holes | Decision and subtraction | Free holes H1 … H5 after request (KB) | Total free (KB) |
|---|---|---|---|---:|
| P1 (212 KB) | H1=x, H2=500, H3=200, H4=300, H5=600 | H2: 500 − 212 = 288 KB | `[x, 288, 200, 300, 600]` | 1388+x |
| P2 (417 KB) | H1=x, H2=288, H3=200, H4=300, H5=600 | H5: 600 − 417 = 183 KB | `[x, 288, 200, 300, 183]` | 971+x |
| P3 (112 KB) | H1=x, H2=288, H3=200, H4=300, H5=183 | H2: 288 − 112 = 176 KB | `[x, 176, 200, 300, 183]` | 859+x |
| P4 (426 KB) | H1=x, H2=176, H3=200, H4=300, H5=183 | FAIL: largest free hole 300 KB < 426 KB | `[x, 176, 200, 300, 183]` | 859+x |
**First Fit result:** P1→H2, P2→H5, P3→H2, P4→FAILED. Final holes: `[x, 176, 200, 300, 183]`; final free space: 859+x KB. Conservation: allocated 741 KB + free 859+x KB = 1600+x KB.

##### Best Fit — complete step-by-step allocation
| Step and request | Order searched / eligible holes | Decision and subtraction | Free holes H1 … H5 after request (KB) | Total free (KB) |
|---|---|---|---|---:|
| P1 (212 KB) | H2, H4, H5 | H4: 300 − 212 = 88 KB | `[x, 500, 200, 88, 600]` | 1388+x |
| P2 (417 KB) | H2, H5 | H2: 500 − 417 = 83 KB | `[x, 83, 200, 88, 600]` | 971+x |
| P3 (112 KB) | H3, H5 | H3: 200 − 112 = 88 KB | `[x, 83, 88, 88, 600]` | 859+x |
| P4 (426 KB) | H5 | H5: 600 − 426 = 174 KB | `[x, 83, 88, 88, 174]` | 433+x |
**Best Fit result:** P1→H4, P2→H2, P3→H3, P4→H5. Final holes: `[x, 83, 88, 88, 174]`; final free space: 433+x KB. Conservation: allocated 1167 KB + free 433+x KB = 1600+x KB.

##### Worst Fit — complete step-by-step allocation
| Step and request | Order searched / eligible holes | Decision and subtraction | Free holes H1 … H5 after request (KB) | Total free (KB) |
|---|---|---|---|---:|
| P1 (212 KB) | H2, H4, H5 | H5: 600 − 212 = 388 KB | `[x, 500, 200, 300, 388]` | 1388+x |
| P2 (417 KB) | H2 | H2: 500 − 417 = 83 KB | `[x, 83, 200, 300, 388]` | 971+x |
| P3 (112 KB) | H3, H4, H5 | H5: 388 − 112 = 276 KB | `[x, 83, 200, 300, 276]` | 859+x |
| P4 (426 KB) | None | FAIL: largest free hole 300 KB < 426 KB | `[x, 83, 200, 300, 276]` | 859+x |
**Worst Fit result:** P1→H5, P2→H2, P3→H5, P4→FAILED. Final holes: `[x, 83, 200, 300, 276]`; final free space: 859+x KB. Conservation: allocated 741 KB + free 859+x KB = 1600+x KB.

##### Next Fit — complete step-by-step allocation
| Step and request | Order searched / eligible holes | Decision and subtraction | Free holes H1 … H5 after request (KB) | Total free (KB) |
|---|---|---|---|---:|
| P1 (212 KB) | H1=x, H2=500, H3=200, H4=300, H5=600 | H2: 500 − 212 = 288 KB; cursor → H2 | `[x, 288, 200, 300, 600]` | 1388+x |
| P2 (417 KB) | H2=288, H3=200, H4=300, H5=600, H1=x | H5: 600 − 417 = 183 KB; cursor → H5 | `[x, 288, 200, 300, 183]` | 971+x |
| P3 (112 KB) | H5=183, H1=x, H2=288, H3=200, H4=300 | H5: 183 − 112 = 71 KB; cursor → H5 | `[x, 288, 200, 300, 71]` | 859+x |
| P4 (426 KB) | H5=71, H1=x, H2=288, H3=200, H4=300 | FAIL: largest free hole 300 KB < 426 KB | `[x, 288, 200, 300, 71]` | 859+x |
**Next Fit result:** P1→H2, P2→H5, P3→H5, P4→FAILED. Final holes: `[x, 288, 200, 300, 71]`; final free space: 859+x KB. Conservation: allocated 741 KB + free 859+x KB = 1600+x KB.

**Interpretation:** Because 0 ≤ x < 112, H1 cannot accept P3; all placement choices and the 426-KB failure can be determined despite the lost H1 size. Only total free-memory answers depend on x.

**Comparison:**

| Request | First Fit | Best Fit | Worst Fit | Next Fit |
|---|---|---|---|---|
| P1 (212 KB) | H2 | H4 | H5 | H2 |
| P2 (417 KB) | H5 | H2 | H2 | H5 |
| P3 (112 KB) | H2 | H3 | H5 | H5 |
| P4 (426 KB) | FAILED | H5 | FAILED | FAILED |

**Conclusion:** Best Fit accepts all four requests; the other three reject P4. This is a workload-specific comparison, not a universal claim that Best Fit is always optimal. Under First Fit at P4, free memory exceeds 426 KB but no individual hole is large enough (external fragmentation).

### Problem 1.2 — Six-hole placement with allocation failure (source data incomplete)

**Source status:** the original file attributes this to an NMIMS re-exam / GTU, but no original paper is supplied. **Hole sizes and process request sizes are absent from the attached file.** Unlike Problem 1.1, there are no surviving figures sufficient even to build a clearly tied numerical reconstruction. This is therefore an **incomplete reported question, not a runnable numerical**. Do not use substitute numbers as if they were the original.

**Preserved original question structure:** In order, six holes H1–H6 are to be allocated to five arriving processes P1–P5 using First Fit, Best Fit and Worst Fit. Identify failures, the remaining free holes, and whether any failure is caused by external fragmentation. In the damaged original explanation, First Fit and Best Fit reportedly allocate all five requests, whereas Worst Fit fails at the third request and continues to consider P4 and P5. **These outcome claims cannot be independently checked with the missing inputs.**

#### Calculation framework to use when source figures become available

Let initial hole sizes be `h1, h2, h3, h4, h5, h6` KB and request sizes `r1, r2, r3, r4, r5` KB. Each of the three policies starts from a fresh copy of the **initial** holes.

| Policy | Search/selection rule for each arriving request | Correct update after selecting Hj |
|---|---|---|
| First Fit | Scan H1–H6 in order and choose first `hj ≥ ri`. | `hj ← hj − ri`; all other holes unchanged. |
| Best Fit | Find the smallest eligible hole `hj ≥ ri`; break ties by lowest index. | `hj ← hj − ri`; preserve physical order. |
| Worst Fit | Find the largest eligible hole `hj ≥ ri`; break ties by lowest index. | `hj ← hj − ri`; preserve physical order. |

For each of P1–P5, record the chosen hole, subtraction, all six post-request hole sizes, and the failed processes. On failure, **do not subtract** the request; continue to the following requests. Compare `ri` with both `sum(h1…h6)` and `max(h1…h6)` **at the moment of failure**: if `sum ≥ ri > max`, external fragmentation blocks placement; if `sum < ri`, free memory is insufficient in total. After each step, the sum of *allocated request sizes* plus the remaining free-hole sizes must equal the initial free-space total. Exact totals and outcomes are **not determinable until the omitted inputs are supplied**.

**Correction-log entry:** The original document's “Worst Fit P3 fails” and “First Fit/Best Fit succeed entirely” are unverified rather than numerically proven. The content is retained as a clearly labelled source claim, not silently replaced with an invented question.


### Problem 1.3 — Binary buddy allocation and full coalescing

**Source:** Practice reconstruction from the surviving address layouts and explicit requested sizes (100, 240, 60, 120 KB). Original question wording was missing.

**Question (reconstructed).** A binary-buddy allocator initially owns a free 1024 KB block at address 0. Allocate A = 100 KB, B = 240 KB, C = 60 KB and D = 120 KB; then free A, C, B and D in that order. Record every split, address range, internal fragmentation and legal buddy merge. Addresses below are offsets in KB from start; half-open `[start,end)` excludes end.

**Sizing rule:** allocate the smallest power-of-two block at least as large as the request. For block size B, the buddy of a B-aligned start address a is `a XOR B` (using KB block-address units). Only two **free, equal-size siblings** can merge.

| Event | Operation / block allocation or merge | Complete free blocks after event (KB-offset ranges) | Allocated blocks / wasted internal KB |
|---|---|---|---|
| Initially | Single `[0,1024)` free | `[0,1024)` | None |
| A: 100 | 1024→512+512; `[0,512)`→256+256; `[0,256)`→128+128; allocate `[0,128)` | `[128,256)`, `[256,512)`, `[512,1024)` | A `[0,128)`; 128−100=28 |
| B: 240 | Allocate existing 256-KB `[256,512)` | `[128,256)`, `[512,1024)` | A 28; B `[256,512)` with 256−240=16 |
| C: 60 | `[128,256)`→`[128,192)` + `[192,256)`; allocate `[128,192)` | `[192,256)`, `[512,1024)` | A 28; B 16; C `[128,192)` with 64−60=4 |
| D: 120 | `[512,1024)`→two 256s; `[512,768)`→two 128s; allocate `[512,640)` | `[192,256)`, `[640,768)`, `[768,1024)` | A 28; B 16; C 4; D `[512,640)` with 128−120=8 |
| Release A | Free `[0,128)`; its size-128 buddy `[128,256)` is split/partly used | `[0,128)`, `[192,256)`, `[640,768)`, `[768,1024)` | B, C, D remain |
| Release C | `[128,192)` + `[192,256)`→`[128,256)`; merge with free `[0,128)`→`[0,256)`; B blocks further merge | `[0,256)`, `[640,768)`, `[768,1024)` | B, D remain |
| Release B | `[0,256)` + `[256,512)`→`[0,512)` | `[0,512)`, `[640,768)`, `[768,1024)` | D remains |
| Release D | `[512,640)` + `[640,768)`→`[512,768)`; + `[768,1024)`→`[512,1024)`; + `[0,512)`→`[0,1024)` | `[0,1024)` | None |

**Check after all allocations:** 128+256+64+128 = 576 KB held in allocated blocks; 448 KB available free; 576+448 = 1024 KB. Total allocated internal waste = 28+16+4+8 = **56 KB**. All 1024 KB coalesces on final release.

### Problem 1.4 — Internal/external fragmentation and compaction

**Source:** Practice reconstruction. Original question omitted the layout labels and total memory size; the surviving solution gives OS=300 KB, P1=300 KB, P2=350 KB, P3=400 KB; holes=150, 200 and 348 KB; P4=500 KB. These sum to 2048 KB. Illustrative placement below preserves those sizes.

**Question (reconstructed).** From low to high address: OS 300 KB, P1 300 KB, free H1 150 KB, P2 350 KB, free H2 200 KB, P3 400 KB, free H3 348 KB. Physical memory is 2048 KB; P4 requests 500 KB. Determine occupied/free memory and whether P4 can be allocated; show compaction and post-compaction allocation.

| Before compaction (half-open KB address range) | Segment | Size |
|---|---|---:|
| `[0,300)` | OS | 300 KB |
| `[300,600)` | P1 | 300 KB |
| `[600,750)` | H1 | 150 KB |
| `[750,1100)` | P2 | 350 KB |
| `[1100,1300)` | H2 | 200 KB |
| `[1300,1700)` | P3 | 400 KB |
| `[1700,2048)` | H3 | 348 KB |

**Arithmetic:** occupied = 300+300+350+400 = **1350 KB**; free = 150+200+348 = **698 KB**; 1350+698 = 2048 KB. P4 requires 500 KB > largest hole 348 KB, although 500 KB ≤ total free 698 KB: **external fragmentation**. For these exact variable-sized allocations there is no *internal* fragmentation attributable to partition rounding.

**Compaction (assume movable processes and suitable relocation support):** OS `[0,300)`, P1 `[300,600)`, P2 `[600,950)`, P3 `[950,1350)`; merged free hole `[1350,2048)` = 698 KB. Allocate P4 `[1350,1850)` = 500 KB; remaining hole `[1850,2048)` = **198 KB**. Check: occupied after allocation 1850 KB + free 198 KB = 2048 KB. Compaction cannot itself enlarge total free memory; it joins scattered holes.

## 4. Section II: Paging and address translation

### Problem 2.1 — Paging logical-to-physical address (division/modulo)

**Source:** Practice reconstruction from answer values and the surviving table in the original workbook. The numerical data are recoverable; the course-notes attribution and exact question wording remain unverified.

**Question (reconstructed).** Page size S=1024 bytes. The page table maps page 0 to frame 5, page 1 to frame 2, page 2 to frame 8, page 3 to frame 1 and page 4 to frame 6. Calculate page number, offset and physical address for logical byte addresses 2050, 5000 and 1020. All requested pages are present.

**Method:** page `p=floor(L/S)`; offset `d=L mod S`; physical address `PA=frame[p]×S+d`. Verify `0≤d<1024` and that p exists in the table. Units are bytes throughout.

| Logical L (bytes) | Division | Page p | Offset d | Frame | Physical address (bytes) |
|---:|---|---:|---:|---:|---:|
| 2050 | 2×1024 + 2 | 2 | 2 | 8 | 8×1024 + 2 = **8194** |
| 5000 | 4×1024 + 904 | 4 | 904 | 6 | 6×1024 + 904 = **7048** |
| 1020 | 0×1024 + 1020 | 0 | 1020 | 5 | 5×1024 + 1020 = **6140** |

Page 1 and page 3 entries, although unused in these three requests, remain in the stated mapping; they are not discarded. Each offset is valid and all lookups correspond to existing entries.

### Problem 2.2 — Address bits, page-table size and physical RAM

**Source:** 32-bit logical address width, 12-bit offset/20-bit page split and arithmetic using a 4-byte PTE survive in the attached workbook. Physical RAM value was erased, so physical width cannot be deduced numerically.

**Question (recoverable version).** For 32-bit logical byte addresses, 4-KiB pages and 4-byte page-table entries (PTEs), compute offset/page bits, maximum number of logical pages and a full single-level page table size. If physical RAM has R bytes, express the physical frame count and address bits symbolically rather than inventing R.

1. 4 KiB = 4096 bytes = 2¹² bytes; therefore the offset is **12 bits**.
2. Page-number width = 32−12 = **20 bits**; maximum logical pages = 2²⁰ = **1,048,576**.
3. Full single-level page table = 2²⁰ × 4 = **4,194,304 bytes = 4 MiB** (excluding metadata).
4. If RAM size R is an integral number of frames, physical frames = `R/4096`. If `R=2^r` bytes, frame number uses `r−12` bits and physical byte address uses **r bits**. A numeric answer for either requires the omitted RAM size.

**Check:** 2²⁰ pages × 2¹² bytes = 2³² logical bytes. A page table can be as large as 4 MiB even if many pages are unused in a single-level setup.

### Problem 2.3 — Two-level hierarchical paging bit split

**Source:** practice-style question in the original, with the 10/10/12-bit split intact but its page size, outer entry count and entry byte size blank in the text. The diagram implies 4-KiB pages and 1024 outer and inner slots; **entry size is not recoverable**, so use the symbol E bytes.

**Question (recovered from diagram).** For a 32-bit logical address with a 10-bit outer index p1, 10-bit inner index p2 and 12-bit offset d, determine pages addressed by each inner table, table sizes in terms of entry size E, and how an address is translated by the hierarchy. Do not manufacture a physical address without mappings.

```text
32-bit logical address:
+--------------------+--------------------+--------------------+
| p1: outer (10 bits)| p2: inner (10 bits)| d: offset (12 bits)|
+--------------------+--------------------+--------------------+
```

- Offset: 12 bits ⇒ page size = 2¹² = **4096 bytes**. Total page-number width = 10+10 = **20 bits** and logical capacity = 2³² bytes.
- Outer index p1: 2¹⁰ = **1024 outer entries**, up to 1024 inner tables. Each inner table selects 2¹⁰ = **1024 pages**, spanning 1024×4096 = **4 MiB of logical space**.
- With **E bytes per table entry**, outer table size = `1024E` bytes and one allocated inner table size = `1024E` bytes. Fully allocated tables occupy `(1+1024)×1024E` bytes, excluding allocator metadata. If a course question later supplies E=4 bytes, *then* each table is 4096 bytes = 4 KiB; that is a conditional calculation, not a source figure.
- Given a logical byte address L, `d=L mod 4096`, `p2=floor(L/4096) mod 1024`, `p1=floor(L/(4096×1024))`. Read outer entry p1, then inner entry p2; if both are present and the latter yields frame number f, `PA=4096f+d`. Missing entries mean a missing mapping/page-fault path rather than a deducible PA.

**Check:** p1/p2/d widths add to 32 and every offset stays between 0 and 4095.

## 5. Section III: TLB and effective access time

**Shared assumptions:** single-level page table in RAM; TLB lookup time ε is paid for *every* reference (serial lookup); a hit requires one RAM access to data; a miss requires a page-table RAM access and one data RAM access. No page faults, cache effects or overlap; ns = nanoseconds. For hit probability α and RAM access time m:

```text
T_hit  = ε + m
T_miss = ε + 2m
EAT    = α(ε+m) + (1−α)(ε+2m) = ε+(2−α)m
```

### Problem 3.1 — TLB hit ratio of 80% versus 98%

**Source:** Practice reconstruction from arithmetic in the attached file. Its attribution to NMIMS 2024–25 Q3b is **unverified**.

**Question.** If m=100 ns and ε=20 ns, calculate EAT at TLB hit ratios 80% and 98%. Compare against paging without a TLB under the same one-level assumption.

1. Hit time = 20+100 = **120 ns**; miss time = 20+2(100) = **220 ns**.
2. α=0.80: `EAT = 0.80(120)+0.20(220) = 96+44 = 140 ns`.
3. α=0.98: `EAT = 0.98(120)+0.02(220) = 117.6+4.4 = 122 ns`.
4. Without TLB, an uncached single-level page-table lookup costs **2×100 = 200 ns** per memory reference. The increase from 80% to 98% hit ratio improves EAT by 18 ns, i.e. 18/140 ≈ **12.86% lower latency**; speedup = 140/122 ≈ **1.148×**.

**Checks:** shortcut yields 20+(2−0.80)100=140 ns and 20+(2−0.98)100=122 ns. The theoretical best with this serial TLB is **120 ns**, not the 100 ns RAM-only latency.

### Problem 3.2 — Minimum TLB hit ratio

**Source:** Practice reconstruction: hit=95 ns and miss=175 ns survive in the original inequality; under the shared model, ε=15 ns and m=80 ns. Both original given values were blank, so these inputs are inferred *for this practice example only*.

**Question (reconstructed).** RAM m=80 ns, TLB ε=15 ns. What minimum hit ratio α keeps EAT ≤105 ns?

- Hit=15+80=**95 ns**; miss=15+160=**175 ns**.
- `EAT = 95α + 175(1−α) = 175−80α ns`.
- `175−80α ≤105` ⇒ `80α ≥70` ⇒ **α ≥0.875 = 87.5%**.
- **Boundary check:** 0.875×95+0.125×175 = 83.125+21.875 = **105 ns**. At greater hit ratios, EAT drops.

## 6. Section IV: Segmentation

### Problem 4.1 — Segmented bounds and physical byte addresses

**Source:** The five complete numeric segment-table entries and requested logical addresses survive in the attached workbook, though its paper/book attribution remains unverified.

**Question (restored).** Segment table entries (segment: base address, segment length/limit in bytes): 0:(219,600), 1:(2300,140), 2:(90,100), 3:(1327,580), 4:(1952,96). Validate the logical addresses `(0,430)`, `(1,150)`, `(2,90)`, `(3,580)`, `(4,50)`. On an invalid offset, trap; on a valid offset, compute `PA=base+offset`.

**Hardware rule:** a logical pair `(s,d)` is legal only when s is an existing entry and **0≤d<limit[s]**. A limit specifies the number of available byte offsets, not the final allowed index.

| Segment s | Base (bytes) | Length/limit (bytes) | Valid offset range (bytes) |
|---:|---:|---:|---|
| 0 | 219 | 600 | 0–599 |
| 1 | 2300 | 140 | 0–139 |
| 2 | 90 | 100 | 0–99 |
| 3 | 1327 | 580 | 0–579 |
| 4 | 1952 | 96 | 0–95 |

| Logical address | Segment | Offset | Limit | Bounds check | Physical address or outcome |
|---|---:|---:|---:|---|---|
| `(0,430)` | 0 | 430 | 600 | 0≤430<600, valid | 219+430 = **649** |
| `(1,150)` | 1 | 150 | 140 | 150≥140, invalid | **TRAP: segmentation fault** |
| `(2,90)` | 2 | 90 | 100 | 0≤90<100, valid | 90+90 = **180** |
| `(3,580)` | 3 | 580 | 580 | 580=limit, invalid | **TRAP: segmentation fault** |
| `(4,50)` | 4 | 50 | 96 | 0≤50<96, valid | 1952+50 = **2002** |

**Check:** three legal translations and two traps; the `(3,580)` offset is precisely one past the maximum legal offset 579. No physical address should be issued for either illegal access. Each logical pair stays on a *single row* in the result table.

### Problem 4.2 — Paging versus segmentation: fragmentation comparison

**Source:** The attached file labels this as a comparative *numerical* task but provides **no page size, frame mapping, free-hole sizes or segment request**. There is no recoverable numerical example. Preserve the intended comparison without pretending the missing numerical inputs exist.

**Question as recoverable:** Explain why paging avoids external fragmentation but segmentation can suffer external fragmentation, and specify the numerical inputs required for a worked example.

- **Paging:** Physical memory is divided into equal-sized frames, and fixed-size logical pages can use nonadjacent free frames. If page size is S bytes and the process size is M bytes, it needs `ceil(M/S)` available frames, occupying `ceil(M/S)×S` bytes. Potential *internal fragmentation in the last page* is `ceil(M/S)×S−M` bytes; this does not imply external fragmentation.
- **Segmentation:** A variable-sized segment of T bytes must fit a single free contiguous hole. For hole sizes `h1…hn`, it fails specifically because of external fragmentation when `sum(h1…hn) ≥ T` but `max(h1…hn) < T`. Compaction can create a sufficiently large hole if those allocations may legally be relocated.
- **Outstanding question data:** To produce the promised actual numerical comparison, attach at least S and M for paging, and the free-hole sizes and requested segment T for segmentation. These quantities are absent, so a final numeric address or fragmentation count **cannot be supplied without introducing new practice inputs**.

## 7. Section V: Demand paging

**EAT model used here:** a successful nonfaulting reference consumes `m` ns. A fault consumes **total end-to-end S ns including page-in, any dirty eviction, OS handling and restarted final memory reference**. With fault probability p: `EAT=(1−p)m+pS`. If a different question defines S as service overhead that *excludes* the final memory access, replace S by S+m; do not mix the conventions. 1 ms = 1,000,000 ns.

### Problem 5.1 — Access time and maximum fault probability

**Source:** Practice reconstruction; m=100 ns, S=8 ms, p=0.001 and target EAT≤110 ns emerge from surviving arithmetic and wording. The attached file's original exam attribution remains unverified.

**Question.** RAM reference m=100 ns; total time per page-faulted reference S=8 ms=8,000,000 ns including restart. Find EAT at p=0.001 and maximum p keeping EAT ≤110 ns. Distinguish “at most 10% slower” (≤110 ns) from strict “less than 10% slower” (<110 ns).

1. `EAT = (1−p)100+p(8,000,000) = 100+7,999,900p ns`.
2. p=0.001 ⇒ `EAT=100+7,999.9=8,099.9 ns ≈8.0999 µs` (about **80.999×** 100-ns access).
3. `100+7,999,900p ≤110` ⇒ `p ≤10/7,999,900 = 0.000001250015625…` ≈ **1.25×10⁻⁶**. For *strictly less* than 10% degradation, use `p <10/7,999,900`.
4. Reciprocal threshold for the at-most case: one fault per **799,990 references on average** at the boundary (since 7,999,900/10=799,990); saying “one per 800,000” is a close rounded approximation, **not** the exact bound.

**Check:** at p=10/7,999,900, EAT=110 ns exactly. `S` explicitly includes restart in this practice reconstruction; that assumption is not recoverable from the original damaged question.

### Problem 5.2 — Dirty-victim probability and weighted service time

**Source:** Practice reconstruction; the workbook's original calculation accidentally used 30% for *clean* victims even though the wording says 30% are *dirty*. Explicitly preserve the intended 30%-dirty interpretation. Service times below are total faulted-reference times including restart for consistency with the formula above.

**Question.** RAM m=200 ns; clean-victim fault S_c=5 ms=5,000,000 ns; dirty-victim fault S_d=10 ms=10,000,000 ns; 30% of fault victims are dirty, 70% clean; fault probability p=0.002. Calculate mean fault time and EAT.

1. `S_avg=0.70(5,000,000)+0.30(10,000,000)=3,500,000+3,000,000=6,500,000 ns = 6.5 ms`.
2. `EAT=(1−0.002)(200)+0.002(6,500,000) = 199.6+13,000 = **13,199.6 ns** ≈ **13.1996 µs**`.
3. **Check:** the erroneous old value 8.5 ms would correspond to 70% *dirty*, not 30%. If service times excluded restart, the result would require a different stated convention; do not silently adjust it.

## 8. Section VI: Page replacement

**Common rules for every trace:** initially all frames empty; add page to lowest free frame. FIFO evicts longest resident since most recent loading, and **hits do not reorder it**. LRU evicts page with oldest prior access time, and **hits update recency**. OPT evicts resident with farthest *next* use; “never used again” ranks farther than any finite next use. In multiple “never” ties, evict the lowest-numbered frame. Frame columns show state **after** the current reference; fault counters include initial loads.

### Problem 6.1 — FIFO, LRU and OPT with three frames

**Source:** The complete 15-reference sequence and frame count survive in the attached file. Its “Lab Exp 9” claim was not checked against that manual and does not establish PYQ status.

**Question.** For reference string `4, 7, 6, 1, 7, 6, 4, 2, 1, 7, 2, 3, 4, 3, 2` and **3 initially empty frames**, simulate FIFO, LRU and OPT. Find hits, faults and both ratios.

#### FIFO trace — 15 references
| Step | Ref | F1 | F2 | F3 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 4 | 4 | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 7 | 4 | 7 | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 6 | 4 | 7 | 6 | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 1 | 1 | 7 | 6 | FAULT | Evict 4: earliest loaded resident (FIFO) | 4 |
| 5 | 7 | 1 | 7 | 6 | HIT | Hit: page 7 already in F2; FIFO insertion order unchanged | 4 |
| 6 | 6 | 1 | 7 | 6 | HIT | Hit: page 6 already in F3; FIFO insertion order unchanged | 4 |
| 7 | 4 | 1 | 4 | 6 | FAULT | Evict 7: earliest loaded resident (FIFO) | 5 |
| 8 | 2 | 1 | 4 | 2 | FAULT | Evict 6: earliest loaded resident (FIFO) | 6 |
| 9 | 1 | 1 | 4 | 2 | HIT | Hit: page 1 already in F1; FIFO insertion order unchanged | 6 |
| 10 | 7 | 7 | 4 | 2 | FAULT | Evict 1: earliest loaded resident (FIFO) | 7 |
| 11 | 2 | 7 | 4 | 2 | HIT | Hit: page 2 already in F3; FIFO insertion order unchanged | 7 |
| 12 | 3 | 7 | 3 | 2 | FAULT | Evict 4: earliest loaded resident (FIFO) | 8 |
| 13 | 4 | 7 | 3 | 4 | FAULT | Evict 2: earliest loaded resident (FIFO) | 9 |
| 14 | 3 | 7 | 3 | 4 | HIT | Hit: page 3 already in F2; FIFO insertion order unchanged | 9 |
| 15 | 2 | 2 | 3 | 4 | FAULT | Evict 7: earliest loaded resident (FIFO) | 10 |

**Result:** 10 faults, 5 hits; 10+5=15 references. Hit ratio 33.33%; fault ratio 66.67%.

#### LRU trace — 15 references
| Step | Ref | F1 | F2 | F3 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 4 | 4 | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 7 | 4 | 7 | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 6 | 4 | 7 | 6 | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 1 | 1 | 7 | 6 | FAULT | Evict 4: oldest last use among 4: step 1, 7: step 2, 6: step 3 | 4 |
| 5 | 7 | 1 | 7 | 6 | HIT | Hit: page 7 already in F2; LRU recency updated | 4 |
| 6 | 6 | 1 | 7 | 6 | HIT | Hit: page 6 already in F3; LRU recency updated | 4 |
| 7 | 4 | 4 | 7 | 6 | FAULT | Evict 1: oldest last use among 1: step 4, 7: step 5, 6: step 6 | 5 |
| 8 | 2 | 4 | 2 | 6 | FAULT | Evict 7: oldest last use among 4: step 7, 7: step 5, 6: step 6 | 6 |
| 9 | 1 | 4 | 2 | 1 | FAULT | Evict 6: oldest last use among 4: step 7, 2: step 8, 6: step 6 | 7 |
| 10 | 7 | 7 | 2 | 1 | FAULT | Evict 4: oldest last use among 4: step 7, 2: step 8, 1: step 9 | 8 |
| 11 | 2 | 7 | 2 | 1 | HIT | Hit: page 2 already in F2; LRU recency updated | 8 |
| 12 | 3 | 7 | 2 | 3 | FAULT | Evict 1: oldest last use among 7: step 10, 2: step 11, 1: step 9 | 9 |
| 13 | 4 | 4 | 2 | 3 | FAULT | Evict 7: oldest last use among 7: step 10, 2: step 11, 3: step 12 | 10 |
| 14 | 3 | 4 | 2 | 3 | HIT | Hit: page 3 already in F3; LRU recency updated | 10 |
| 15 | 2 | 4 | 2 | 3 | HIT | Hit: page 2 already in F2; LRU recency updated | 10 |

**Result:** 10 faults, 5 hits; 10+5=15 references. Hit ratio 33.33%; fault ratio 66.67%.

#### OPT trace — 15 references
| Step | Ref | F1 | F2 | F3 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 4 | 4 | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 7 | 4 | 7 | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 6 | 4 | 7 | 6 | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 1 | 1 | 7 | 6 | FAULT | Evict 4: next uses 4→step 7, 7→step 5, 6→step 6; farthest/never | 4 |
| 5 | 7 | 1 | 7 | 6 | HIT | Hit: page 7 already in F2; no replacement | 4 |
| 6 | 6 | 1 | 7 | 6 | HIT | Hit: page 6 already in F3; no replacement | 4 |
| 7 | 4 | 1 | 7 | 4 | FAULT | Evict 6: next uses 1→step 9, 7→step 10, 6→never; farthest/never | 5 |
| 8 | 2 | 1 | 7 | 2 | FAULT | Evict 4: next uses 1→step 9, 7→step 10, 4→step 13; farthest/never | 6 |
| 9 | 1 | 1 | 7 | 2 | HIT | Hit: page 1 already in F1; no replacement | 6 |
| 10 | 7 | 1 | 7 | 2 | HIT | Hit: page 7 already in F2; no replacement | 6 |
| 11 | 2 | 1 | 7 | 2 | HIT | Hit: page 2 already in F3; no replacement | 6 |
| 12 | 3 | 3 | 7 | 2 | FAULT | Evict 1: next uses 1→never, 7→never, 2→step 15; farthest/never | 7 |
| 13 | 4 | 3 | 4 | 2 | FAULT | Evict 7: next uses 3→step 14, 7→never, 2→step 15; farthest/never | 8 |
| 14 | 3 | 3 | 4 | 2 | HIT | Hit: page 3 already in F1; no replacement | 8 |
| 15 | 2 | 3 | 4 | 2 | HIT | Hit: page 2 already in F3; no replacement | 8 |

**Result:** 8 faults, 7 hits; 8+7=15 references. Hit ratio 46.67%; fault ratio 53.33%.

**Critical correction:** At step 4, pages 4, 7 and 6 have next uses 7, 5 and 6. OPT evicts **4**. At LRU step 7, page **1** was last referenced at step 4; pages 7 and 6 at steps 5 and 6: evict **1**. The entire follow-on trace above uses the corrected resident states.

| Algorithm | References | Faults | Hits | Hit ratio | Fault ratio |
|---|---:|---:|---:|---:|---:|
| FIFO | 15 | 10 | 5 | 33.33% | 66.67% |
| LRU | 15 | 10 | 5 | 33.33% | 66.67% |
| OPT | 15 | 8 | 7 | 46.67% | 53.33% |

**Evaluation:** OPT has the lowest fault count for this reference string. Its future knowledge is a benchmark rather than an implementation that predicts arbitrary future memory requests.

### Problem 6.2 — FIFO and LRU on 20 references with four frames

**Source:** Reference string and frame count are preserved exactly from the attached workbook. Its attribution to a final exam and/or lab cannot be established without the source papers; this is an independently recalculated numerical exercise.

**Question.** Reference string `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1`. Four frames start empty. Simulate FIFO and LRU, reporting faults, hits, victim choices and ratios.

#### FIFO trace — 20 references
| Step | Ref | F1 | F2 | F3 | F4 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 7 | 7 | — | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 0 | 7 | 0 | — | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 1 | 7 | 0 | 1 | — | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 2 | 7 | 0 | 1 | 2 | FAULT | Free F4, no victim (initial load) | 4 |
| 5 | 0 | 7 | 0 | 1 | 2 | HIT | Hit: page 0 already in F2; FIFO insertion order unchanged | 4 |
| 6 | 3 | 3 | 0 | 1 | 2 | FAULT | Evict 7: earliest loaded resident (FIFO) | 5 |
| 7 | 0 | 3 | 0 | 1 | 2 | HIT | Hit: page 0 already in F2; FIFO insertion order unchanged | 5 |
| 8 | 4 | 3 | 4 | 1 | 2 | FAULT | Evict 0: earliest loaded resident (FIFO) | 6 |
| 9 | 2 | 3 | 4 | 1 | 2 | HIT | Hit: page 2 already in F4; FIFO insertion order unchanged | 6 |
| 10 | 3 | 3 | 4 | 1 | 2 | HIT | Hit: page 3 already in F1; FIFO insertion order unchanged | 6 |
| 11 | 0 | 3 | 4 | 0 | 2 | FAULT | Evict 1: earliest loaded resident (FIFO) | 7 |
| 12 | 3 | 3 | 4 | 0 | 2 | HIT | Hit: page 3 already in F1; FIFO insertion order unchanged | 7 |
| 13 | 2 | 3 | 4 | 0 | 2 | HIT | Hit: page 2 already in F4; FIFO insertion order unchanged | 7 |
| 14 | 1 | 3 | 4 | 0 | 1 | FAULT | Evict 2: earliest loaded resident (FIFO) | 8 |
| 15 | 2 | 2 | 4 | 0 | 1 | FAULT | Evict 3: earliest loaded resident (FIFO) | 9 |
| 16 | 0 | 2 | 4 | 0 | 1 | HIT | Hit: page 0 already in F3; FIFO insertion order unchanged | 9 |
| 17 | 1 | 2 | 4 | 0 | 1 | HIT | Hit: page 1 already in F4; FIFO insertion order unchanged | 9 |
| 18 | 7 | 2 | 7 | 0 | 1 | FAULT | Evict 4: earliest loaded resident (FIFO) | 10 |
| 19 | 0 | 2 | 7 | 0 | 1 | HIT | Hit: page 0 already in F3; FIFO insertion order unchanged | 10 |
| 20 | 1 | 2 | 7 | 0 | 1 | HIT | Hit: page 1 already in F4; FIFO insertion order unchanged | 10 |

**Result:** 10 faults, 10 hits; 10+10=20 references. Hit ratio 50.00%; fault ratio 50.00%.

#### LRU trace — 20 references
| Step | Ref | F1 | F2 | F3 | F4 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 7 | 7 | — | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 0 | 7 | 0 | — | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 1 | 7 | 0 | 1 | — | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 2 | 7 | 0 | 1 | 2 | FAULT | Free F4, no victim (initial load) | 4 |
| 5 | 0 | 7 | 0 | 1 | 2 | HIT | Hit: page 0 already in F2; LRU recency updated | 4 |
| 6 | 3 | 3 | 0 | 1 | 2 | FAULT | Evict 7: oldest last use among 7: step 1, 0: step 5, 1: step 3, 2: step 4 | 5 |
| 7 | 0 | 3 | 0 | 1 | 2 | HIT | Hit: page 0 already in F2; LRU recency updated | 5 |
| 8 | 4 | 3 | 0 | 4 | 2 | FAULT | Evict 1: oldest last use among 3: step 6, 0: step 7, 1: step 3, 2: step 4 | 6 |
| 9 | 2 | 3 | 0 | 4 | 2 | HIT | Hit: page 2 already in F4; LRU recency updated | 6 |
| 10 | 3 | 3 | 0 | 4 | 2 | HIT | Hit: page 3 already in F1; LRU recency updated | 6 |
| 11 | 0 | 3 | 0 | 4 | 2 | HIT | Hit: page 0 already in F2; LRU recency updated | 6 |
| 12 | 3 | 3 | 0 | 4 | 2 | HIT | Hit: page 3 already in F1; LRU recency updated | 6 |
| 13 | 2 | 3 | 0 | 4 | 2 | HIT | Hit: page 2 already in F4; LRU recency updated | 6 |
| 14 | 1 | 3 | 0 | 1 | 2 | FAULT | Evict 4: oldest last use among 3: step 12, 0: step 11, 4: step 8, 2: step 13 | 7 |
| 15 | 2 | 3 | 0 | 1 | 2 | HIT | Hit: page 2 already in F4; LRU recency updated | 7 |
| 16 | 0 | 3 | 0 | 1 | 2 | HIT | Hit: page 0 already in F2; LRU recency updated | 7 |
| 17 | 1 | 3 | 0 | 1 | 2 | HIT | Hit: page 1 already in F3; LRU recency updated | 7 |
| 18 | 7 | 7 | 0 | 1 | 2 | FAULT | Evict 3: oldest last use among 3: step 12, 0: step 16, 1: step 17, 2: step 15 | 8 |
| 19 | 0 | 7 | 0 | 1 | 2 | HIT | Hit: page 0 already in F2; LRU recency updated | 8 |
| 20 | 1 | 7 | 0 | 1 | 2 | HIT | Hit: page 1 already in F3; LRU recency updated | 8 |

**Result:** 8 faults, 12 hits; 8+12=20 references. Hit ratio 60.00%; fault ratio 40.00%.

| Algorithm | References | Faults | Hits | Hit ratio | Fault ratio |
|---|---:|---:|---:|---:|---:|
| FIFO | 20 | 10 | 10 | 50.00% | 50.00% |
| LRU | 20 | 8 | 12 | 60.00% | 40.00% |

**Check:** LRU saves two faults compared with FIFO for this particular input. The original 6.2 asks only for FIFO/LRU; OPT is already fully demonstrated in Problem 6.1, so a third algorithm is not falsely attributed to this question.

### Problem 6.3 — Belady's anomaly, FIFO with three versus four frames

**Source:** Full 12-reference sequence preserved. The earlier workbook attributes this to Lab Exp 9, but its manual was not attached; treat as lab-style exercise, **not a verified past exam paper**.

**Question.** Reference string `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`. Count FIFO faults with 3 frames and with 4 empty frames and explain the difference.

#### FIFO trace — 3 frames
| Step | Ref | F1 | F2 | F3 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 1 | 1 | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 2 | 1 | 2 | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 3 | 1 | 2 | 3 | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 4 | 4 | 2 | 3 | FAULT | Evict 1: earliest loaded resident (FIFO) | 4 |
| 5 | 1 | 4 | 1 | 3 | FAULT | Evict 2: earliest loaded resident (FIFO) | 5 |
| 6 | 2 | 4 | 1 | 2 | FAULT | Evict 3: earliest loaded resident (FIFO) | 6 |
| 7 | 5 | 5 | 1 | 2 | FAULT | Evict 4: earliest loaded resident (FIFO) | 7 |
| 8 | 1 | 5 | 1 | 2 | HIT | Hit: page 1 already in F2; FIFO insertion order unchanged | 7 |
| 9 | 2 | 5 | 1 | 2 | HIT | Hit: page 2 already in F3; FIFO insertion order unchanged | 7 |
| 10 | 3 | 5 | 3 | 2 | FAULT | Evict 1: earliest loaded resident (FIFO) | 8 |
| 11 | 4 | 5 | 3 | 4 | FAULT | Evict 2: earliest loaded resident (FIFO) | 9 |
| 12 | 5 | 5 | 3 | 4 | HIT | Hit: page 5 already in F1; FIFO insertion order unchanged | 9 |

**Result:** 9 faults, 3 hits; 9+3=12 references. Hit ratio 25.00%; fault ratio 75.00%.

#### FIFO trace — 4 frames
| Step | Ref | F1 | F2 | F3 | F4 | Hit/Fault | Victim/explanation | Cumulative faults |
|---:|---:|---:|---:|---:|---:|---|---|---:|
| 1 | 1 | 1 | — | — | — | FAULT | Free F1, no victim (initial load) | 1 |
| 2 | 2 | 1 | 2 | — | — | FAULT | Free F2, no victim (initial load) | 2 |
| 3 | 3 | 1 | 2 | 3 | — | FAULT | Free F3, no victim (initial load) | 3 |
| 4 | 4 | 1 | 2 | 3 | 4 | FAULT | Free F4, no victim (initial load) | 4 |
| 5 | 1 | 1 | 2 | 3 | 4 | HIT | Hit: page 1 already in F1; FIFO insertion order unchanged | 4 |
| 6 | 2 | 1 | 2 | 3 | 4 | HIT | Hit: page 2 already in F2; FIFO insertion order unchanged | 4 |
| 7 | 5 | 5 | 2 | 3 | 4 | FAULT | Evict 1: earliest loaded resident (FIFO) | 5 |
| 8 | 1 | 5 | 1 | 3 | 4 | FAULT | Evict 2: earliest loaded resident (FIFO) | 6 |
| 9 | 2 | 5 | 1 | 2 | 4 | FAULT | Evict 3: earliest loaded resident (FIFO) | 7 |
| 10 | 3 | 5 | 1 | 2 | 3 | FAULT | Evict 4: earliest loaded resident (FIFO) | 8 |
| 11 | 4 | 4 | 1 | 2 | 3 | FAULT | Evict 5: earliest loaded resident (FIFO) | 9 |
| 12 | 5 | 4 | 5 | 2 | 3 | FAULT | Evict 1: earliest loaded resident (FIFO) | 10 |

**Result:** 10 faults, 2 hits; 10+2=12 references. Hit ratio 16.67%; fault ratio 83.33%.

| Number of frames | References | Faults | Hits | Fault ratio |
|---:|---:|---:|---:|---:|
| 3 | 12 | 9 | 3 | 75.00% |
| 4 | 12 | 10 | 2 | 83.33% |

**Belady's anomaly:** increasing available frames from 3 to 4 increases FIFO faults from 9 to 10. FIFO does not have the *stack property*: at every reference, the pages held with k frames need not be a subset of pages held with k+1 frames. LRU and OPT are stack algorithms and do not exhibit this anomaly for a fixed reference sequence under their standard definitions.

## 9. Section VII: Coverage, correction and verification log

### Numerical-types checklist

- [x] First Fit, Best Fit, Worst Fit and Next Fit with post-request holes, arithmetic, failure reporting and precise cursor convention (1.1).
- [ ] Original six-hole allocation problem (1.2) **cannot be numerically completed without its lost input lists**; complete decision framework retained.
- [x] Buddy-system power-of-two blocks, KB-offset ranges, internal waste, releases and valid buddy merges (1.3).
- [x] External fragmentation versus insufficient total memory; compaction and remaining hole (1.4).
- [x] Paging page number, offsets, frame lookups, logical-to-physical addresses (2.1).
- [x] Logical paging bit split and page table size (2.2); **numeric physical width awaits original RAM size**.
- [x] Two-level page-table index and general size formulas (2.3); **numeric entry-dependent size awaits original PTE size**.
- [x] TLB weighted EAT and minimum hit ratio (3.1–3.2).
- [x] Segmentation table and offset-equals-limit boundary case (4.1).
- [ ] Paging/segmentation *original numerical comparison* not executable because inputs were omitted (4.2); correct symbolic conditions retained.
- [x] Demand-paging EAT and strict versus non-strict probability thresholds (5.1).
- [x] Clean/dirty weighted fault service time and corrected EAT (5.2).
- [x] FIFO, LRU and OPT complete row-by-row frame traces, victim reasons and fault/hit counts (6.1–6.2).
- [x] FIFO Belady anomaly with three versus four frames (6.3).

### Source correction and integrity audit

- **Original numeric data:** Problem 1.1 leaves H1 unresolved as x rather than asserting a guessed size; 1.2 leaves its unattached initial holes and requests unresolved; 2.2 leaves physical RAM R symbolic; 2.3 leaves entry byte size E symbolic; 4.2 leaves its requested comparison numerical explicitly incomplete. Recoverable figures in other sections are identified where used. Paper and lab-manual provenance remains **unverified**.
- **Trace errors fixed:** regeneration corrects LRU step 7 (evict 1) and OPT step 4 (evict 4) of Problem 6.1. All frame states, statuses, victim descriptions and running fault totals in Problems 6.1–6.3 were recomputed by a trace simulator and independently sanity-checked against the stated algorithm rules.
- **Demand-paging fix:** Problem 5.2 weights 70% clean (5 ms) and 30% dirty (10 ms), yielding 6.5 ms and 13,199.6 ns; both problems explicitly state whether restart is included in S.
- **Markdown fix:** the broken HTML segment table is replaced by one address per row; corrupted control characters, empty mathematics and unbalanced fences are excluded. Table of contents points to the nine numbered top-level headings. Structural checks do **not** constitute a live GitHub rendering test or claimed verification against any original exam paper.

**Remaining source action:** Supply the original exam/lab paper, or a legible version of the six-hole example and physical-RAM/page-table-entry values, to resolve the specifically marked gaps. The document otherwise preserves the original workbook's scope and expands the remaining fully solvable numericals; it does not mislabel any as a verified PYQ.

