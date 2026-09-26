# 📚 IVP Unit 4: Morphological Image Processing — Comprehensive Study Notes

---

## 📌 Document Overview & Exam Scope Notice

* **Course:** Image and Video Processing (IVP)
* **Unit:** Unit 4 — Morphological Image Processing
* **Target Assessment:** University Term-End Examinations, Class Tests, and Laboratory Viva
* **Format:** GitHub Flavored Markdown (GFM) with LaTeX Math
* **Scope Boundary Notice:** This study guide strictly covers the prescribed **Unit 4 Syllabus Topics**:
  1. **Fundamental Binary Morphological Operations:** Dilation, Erosion, Opening, and Closing.
  2. **Hit-or-Miss Transformation:** Foreground/background pattern matching, composite structuring elements, and dual formulation.
  3. **Boundary Extraction:** Binary inner boundary derivation ($\beta(A) = A - (A \ominus B)$) and edge extraction.
  4. **Thinning and Thickening:** Sequential morphological filtering, hit-or-miss relationship, and shape skeletonization.
  5. **Grayscale Morphology:** Function dilation, erosion, opening, closing, morphological gradient, and top-hat/bottom-hat transformations.

---

## 📑 Table of Contents

1. [Section 1: Fundamentals of Mathematical Morphology](#section-1-fundamentals-of-mathematical-morphology)
   * 1.1 [What is Mathematical Morphology?](#11-what-is-mathematical-morphology)
   * 1.2 [Binary Images, Sets, Foreground, and Background](#12-binary-images-sets-foreground-and-background)
   * 1.3 [Structuring Elements (SE), Origins, Reflection, and Translation](#13-structuring-elements-se-origins-reflection-and-translation)
2. [Section 2: Fundamental Binary Morphological Operations](#section-2-fundamental-binary-morphological-operations)
   * 2.1 [Morphological Dilation](#21-morphological-dilation)
   * 2.2 [Morphological Erosion](#22-morphological-erosion)
   * 2.3 [Dilation vs. Erosion Comparison](#23-dilation-vs-erosion-comparison)
   * 2.4 [Morphological Opening](#24-morphological-opening)
   * 2.5 [Morphological Closing](#25-morphological-closing)
   * 2.6 [Opening vs. Closing Comparison](#26-opening-vs-closing-comparison)
   * 2.7 [Duality and Fundamental Algebraic Properties](#27-duality-and-fundamental-algebraic-properties)
   * 2.8 [Step-by-Step Worked Numerical Example: Binary Operations](#28-step-by-step-worked-numerical-example-binary-operations)
3. [Section 3: Hit-or-Miss Transformation (HMT)](#section-3-hit-or-miss-transformation-hmt)
   * 3.1 [Concept, Purpose, and Shape Matching](#31-concept-purpose-and-shape-matching)
   * 3.2 [Mathematical Formulation & Dual Structuring Elements](#32-mathematical-formulation-dual-structuring-elements)
   * 3.3 [Composite Structuring Element Notation (Hits, Misses, Don't Cares)](#33-composite-structuring-element-notation-hits-misses-dont-cares)
   * 3.4 [Step-by-Step Worked Example: Corner & Landmark Detection](#34-step-by-step-worked-example-corner-landmark-detection)
4. [Section 4: Morphological Algorithms: Boundary Extraction](#section-4-morphological-algorithms-boundary-extraction)
   * 4.1 [Boundary Extraction Concept and Mathematical Derivation](#41-boundary-extraction-concept-and-mathematical-derivation)
   * 4.2 [Structuring Element Connectivity & Boundary Thickness](#42-structuring-element-connectivity-boundary-thickness)
   * 4.3 [Step-by-Step Worked Numerical Example: Inner Boundary Extraction](#43-step-by-step-worked-numerical-example-inner-boundary-extraction)
5. [Section 5: Morphological Algorithms: Thinning and Thickening](#section-5-morphological-algorithms-thinning-and-thickening)
   * 5.1 [Morphological Thinning](#51-morphological-thinning)
   * 5.2 [Sequential Thinning & Structuring Element Sequences](#52-sequential-thinning-structuring-element-sequences)
   * 5.3 [Morphological Thickening](#53-morphological-thickening)
   * 5.4 [Duality between Thinning and Thickening](#54-duality-between-thinning-and-thickening)
   * 5.5 [Application to Skeletonization and Pruning](#55-application-to-skeletonization-and-pruning)
6. [Section 6: Grayscale Morphology](#section-6-grayscale-morphology)
   * 6.1 [Extension from Binary Sets to Intensity Functions](#61-extension-from-binary-sets-to-intensity-functions)
   * 6.2 [Flat vs. Non-Flat Structuring Functions](#62-flat-vs-non-flat-structuring-functions)
   * 6.3 [Grayscale Dilation and Grayscale Erosion](#63-grayscale-dilation-and-grayscale-erosion)
   * 6.4 [Grayscale Opening and Grayscale Closing](#64-grayscale-opening-and-grayscale-closing)
   * 6.5 [Grayscale Morphological Gradient](#65-grayscale-morphological-gradient)
   * 6.6 [Top-Hat and Bottom-Hat Transformations](#66-top-hat-and-bottom-hat-transformations)
   * 6.7 [Step-by-Step Worked Numerical Example: Grayscale Operations](#67-step-by-step-worked-numerical-example-grayscale-operations)
7. [Section 7: Master Comparison Tables](#section-7-master-comparison-tables)
8. [Section 8: Formula Master Reference Sheet](#section-8-formula-master-reference-sheet)
9. [Section 9: Common Exam Mistakes & Pitfalls](#section-9-common-exam-mistakes-pitfalls)
10. [Section 10: Unit 4 Quick Revision & Coverage Checklist](#section-10-unit-4-quick-revision-coverage-checklist)

---

## Section 1: Fundamentals of Mathematical Morphology

### 1.1 What is Mathematical Morphology?

**Mathematical Morphology** is a branch of digital image processing based on set theory that analyzes the geometric structures and spatial shapes within images. Introduced by Georges Matheron and Jean Serra in the late 1960s, morphological operations extract image components that are useful in representing and describing region shapes—such as boundaries, skeletons, convex hulls, and structural textures.

Unlike linear spatial filtering (which relies on convolution and frequency response), morphological processing operates via non-linear set operations (intersections, unions, inclusions, shifts, maxima, and minima) using a small spatial probe known as a **Structuring Element (SE)**.

```text
+-----------------------------------------------------------------------+
|                    MATHEMATICAL MORPHOLOGY PIPELINE                   |
|                                                                       |
|  [ Input Image A ]  <--->  [ Structuring Element B ]                  |
|          |                            |                               |
|          +------------+---------------+                               |
|                       |                                               |
|                       v                                               |
|           Set Theoretic Operations                                    |
|   (Translations, Intersections, Fits/Hits, Max/Min)                   |
|                       |                                               |
|                       v                                               |
|            [ Morphological Output Image ]                             |
+-----------------------------------------------------------------------+
```

---

### 1.2 Binary Images, Sets, Foreground, and Background

In binary mathematical morphology, an image $A$ is represented as a 2D mathematical set defined on the 2D integer grid $\mathbb{Z}^2$:

1. **Foreground Pixels ($1$ or White):** Belong to the set $A$. These represent the object(s) under analysis:
   $$A = \{(x,y) \mid I(x,y) = 1\}$$
2. **Background Pixels ($0$ or Black):** Belong to the complement set $A^c$. These represent the non-object background:
   $$A^c = \{(x,y) \mid I(x,y) = 0\}$$

#### Key Set-Theoretic Notations:
* **Element Inclusion:** $(x,y) \in A$ means pixel $(x,y)$ is foreground.
* **Subset / Fitting:** $B \subseteq A$ means every element of set $B$ is contained within set $A$.
* **Intersection / Hitting:** $A \cap B \neq \emptyset$ means set $A$ and set $B$ share at least one common foreground pixel.
* **Disjoint / Missing:** $A \cap B = \emptyset$ means set $A$ and set $B$ have no overlapping foreground pixels.
* **Set Difference:** $A - B = A \cap B^c = \{w \mid w \in A \text{ and } w \notin B\}$.

---

### 1.3 Structuring Elements (SE), Origins, Reflection, and Translation

A **Structuring Element (SE)**, denoted as $B$, is a small binary pattern (matrix) used as a geometric probe to interact with the input image $A$.

#### 1. The SE Origin $(0,0)$:
Every structuring element has a designated reference point called its **Origin**. 
* The origin is conventionally located at the center pixel of the SE grid (e.g., $(1,1)$ in a $3 \times 3$ grid).
* The origin determines the exact pixel location in the output image where the result of the set operation is recorded.
* *Note:* The origin does not strictly have to be inside the SE boundary, though center positioning is standard for isotropic filtering.

#### 2. Translation $(B)_z$:
The translation of set $B$ by point $z = (z_1, z_2) \in \mathbb{Z}^2$ shifts every coordinate $b \in B$ by $z$:
$$(B)_z = \{c \mid c = b + z, \text{ for } b \in B\}$$

#### 3. Reflection $\hat{B}$:
The reflection of set $B$, denoted as $\hat{B}$, is the set of points rotated $180^\circ$ around its origin:
$$\hat{B} = \{w \mid w = -b, \text{ for } b \in B\}$$
> 🧠 **Must Understand:** If a structuring element is symmetric about its origin (such as a $3 \times 3$ square, cross, or disk), its reflection is identical to itself ($\hat{B} = B$).

#### Standard $3 \times 3$ Structuring Elements:

```text
1. 3x3 Full Square (8-Connected):     2. 3x3 Cross / Diamond (4-Connected):
      [ 1  1  1 ]                           [ 0  1  0 ]
      [ 1 (1) 1 ]                           [ 1 (1) 1 ]
      [ 1  1  1 ]                           [ 0  1  0 ]
   (Origin at center)                    (Origin at center)

3. Horizontal Line SE (1x3):          4. Vertical Line SE (3x1):
      [ 1 (1) 1 ]                           [ 1 ]
                                            [(1)]
                                            [ 1 ]
```

---

## Section 2: Fundamental Binary Morphological Operations

### 2.1 Morphological Dilation

#### 1. Purpose & Plain-Language Explanation:
Dilation **expands** or **thickens** foreground objects in a binary image. It bridges small disconnections, fills narrow gaps or holes, and smooths outer contours by adding pixels to object boundaries.

#### 2. Mathematical Definition:
The dilation of image $A$ by structuring element $B$, denoted $A \oplus B$, is defined as:
$$A \oplus B = \{z \mid (\hat{B})_z \cap A \neq \emptyset\}$$

In set terms, $A \oplus B$ is the set of all spatial translations $z$ such that the reflected structuring element $\hat{B}$ translated by $z$ overlaps (hits) $A$ by at least one foreground pixel.

When $B$ is symmetric ($\hat{B} = B$), this simplifies to:
$$A \oplus B = \{z \mid (B)_z \cap A \neq \emptyset\} = \bigcup_{b \in B} (A)_b$$

#### 3. Operational Algorithm:
1. Center the SE origin at every pixel location $(x,y)$ in the image.
2. If **at least one** active foreground pixel ($1$) of the SE overlaps with a foreground pixel ($1$) in $A$ (a **hit**), set the output pixel at $(x,y)$ to $1$.
3. Otherwise, set the output pixel to $0$.

---

### 2.2 Morphological Erosion

#### 1. Purpose & Plain-Language Explanation:
Erosion **shrinks** or **thins** foreground objects in a binary image. It removes small isolated noise specks, eliminates narrow protrusions, and breaks thin bridges connecting larger regions.

#### 2. Mathematical Definition:
The erosion of image $A$ by structuring element $B$, denoted $A \ominus B$, is defined as:
$$A \ominus B = \{z \mid (B)_z \subseteq A\}$$

In set terms, $A \ominus B$ is the set of all spatial translations $z$ such that the translated structuring element $(B)_z$ is **completely contained** (fits) within $A$.

#### 3. Operational Algorithm:
1. Center the SE origin at every pixel location $(x,y)$ in the image.
2. If **every** active foreground pixel ($1$) of the SE overlaps with a foreground pixel ($1$) in $A$ (a **fit**), set the output pixel at $(x,y)$ to $1$.
3. Otherwise, set the output pixel to $0$.

---

### 2.3 Dilation vs. Erosion Comparison

| Characteristic | Morphological Dilation ($A \oplus B$) | Morphological Erosion ($A \ominus B$) |
| :--- | :--- | :--- |
| **Primary Effect** | Expands / thickens foreground objects | Shrinks / thins foreground objects |
| **Set Condition** | **Hitting / Overlap:** $(B)_z \cap A \neq \emptyset$ | **Fitting / Inclusion:** $(B)_z \subseteq A$ |
| **Logical Operator** | OR / Maximum over neighborhood | AND / Minimum over neighborhood |
| **Noise Handling** | Fills small interior dark holes/gaps | Removes small isolated bright noise specks |
| **Boundary Effect** | Appends pixels to object boundaries | Strips pixels from object boundaries |
| **Object Topology** | May merge separate close objects | May split or disconnect thin objects |

---

### 2.4 Morphological Opening

#### 1. Purpose & Plain-Language Explanation:
Morphological Opening **smooths object contours**, breaks narrow thin connections, and **completely removes small isolated foreground objects/specks** that are smaller than the structuring element, without significantly changing the overall area or size of the remaining large objects.

#### 2. Mathematical Definition & Order of Operations:
Opening of set $A$ by structuring element $B$, denoted $A \circ B$, is defined as **Erosion followed by Dilation**:
$$A \circ B = (A \ominus B) \oplus B$$

> ⭐ **Must Remember for Exams:** In Opening, **EROSION IS APPLIED FIRST**, then Dilation.
> 
> $$\text{Opening Sequence:} \quad A \xrightarrow{\text{Erosion with } B} (A \ominus B) \xrightarrow{\text{Dilation with } B} (A \circ B)$$

#### 3. Geometric Interpretation (Rolling Ball Analogy):
$A \circ B$ is equal to the union of all translations of $B$ that fit completely inside $A$:
$$A \circ B = \bigcup \{(B)_z \mid (B)_z \subseteq A\}$$
Imagine "rolling" the structuring element $B$ inside the object $A$. Any region inside $A$ that is too small for $B$ to fit into is permanently erased.

---

### 2.5 Morphological Closing

#### 1. Purpose & Plain-Language Explanation:
Morphological Closing **smooths object contours**, fuses narrow breaks and long thin gulfs, **fills small dark holes/pinholes**, and bridges gaps inside foreground regions without significantly changing the overall size of the major objects.

#### 2. Mathematical Definition & Order of Operations:
Closing of set $A$ by structuring element $B$, denoted $A \bullet B$, is defined as **Dilation followed by Erosion**:
$$A \bullet B = (A \oplus B) \ominus B$$

> ⭐ **Must Remember for Exams:** In Closing, **DILATION IS APPLIED FIRST**, then Erosion.
> 
> $$\text{Closing Sequence:} \quad A \xrightarrow{\text{Dilation with } B} (A \oplus B) \xrightarrow{\text{Erosion with } B} (A \bullet B)$$

#### 3. Geometric Interpretation:
Closing fills any boundary indentation or internal background region that cannot accommodate the structuring element $B$ when rolled on the outside of $A$.

---

### 2.6 Opening vs. Closing Comparison

| Feature | Morphological Opening ($A \circ B$) | Morphological Closing ($A \bullet B$) |
| :--- | :--- | :--- |
| **Sequence** | **Erosion FIRST**, then Dilation | **Dilation FIRST**, then Erosion |
| **Formula** | $A \circ B = (A \ominus B) \oplus B$ | $A \bullet B = (A \oplus B) \ominus B$ |
| **Primary Effect** | Removes small foreground specks/protrusions | Fills small background holes/bridges gaps |
| **Boundary Smoothing** | Smooths object contours from the **outside** | Smooths object contours from the **inside** |
| **Set Relation** | **Sub-idempotent:** $A \circ B \subseteq A$ | **Super-idempotent:** $A \subseteq A \bullet B$ |
| **Application** | Background noise suppression | Hole filling & gap connection |

---

### 2.7 Duality and Fundamental Algebraic Properties

#### 1. Duality Theorems:
Dilation and Erosion are duals of each other with respect to set complementation:
$$(A \ominus B)^c = A^c \oplus \hat{B}$$
$$(A \oplus B)^c = A^c \ominus \hat{B}$$

Similarly, Opening and Closing are duals:
$$(A \circ B)^c = A^c \bullet \hat{B}$$
$$(A \bullet B)^c = A^c \circ \hat{B}$$

> 🧠 **Must Understand:** Dilating the foreground is mathematically equivalent to eroding the background with a reflected structuring element!

#### 2. Key Algebraic Properties:

* **Idempotency (Repeat Application produces NO further change):**
  $$(A \circ B) \circ B = A \circ B$$
  $$(A \bullet B) \bullet B = A \bullet B$$
  *Once an image is opened or closed, repeating the same operation with the same SE has zero additional effect.*

* **Increasing / Monotonicity:**
  $$\text{If } A \subseteq C, \text{ then } (A \ominus B) \subseteq (C \ominus B) \text{ and } (A \oplus B) \subseteq (C \oplus B)$$

* **Translation Invariance:**
  $$(A)_z \oplus B = (A \oplus B)_z$$
  $$(A)_z \ominus B = (A \ominus B)_z$$

---

### 2.8 Step-by-Step Worked Numerical Example: Binary Operations

#### ❓ Problem Statement:
Given a $5 \times 5$ binary image matrix $A$ (where $1 = \text{foreground}$ and $0 = \text{background}$):

```math
A = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

And a $3 \times 3$ cross-shaped Structuring Element $B$ (4-connected) with origin at center $(1,1)$:

```math
B = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}
```

*Assumption:* Zero-padding for pixels outside the image boundary.

Compute:
1. Erosion $A \ominus B$
2. Dilation $A \oplus B$
3. Opening $A \circ B = (A \ominus B) \oplus B$

---

#### 💡 Step-by-Step Solution:

##### 1. Calculating Erosion $A \ominus B$:
For $A \ominus B$ at pixel $(r,c)$, the cross SE $B$ must **fit completely** inside $A$. That is, the center pixel $(r,c)$, top $(r-1,c)$, bottom $(r+1,c)$, left $(r,c-1)$, and right $(r,c+1)$ must ALL be $1$ in $A$.

* **Center $(2,2)$ (Row 2, Col 2):**
  * Neighbors in $A$: Center=1, Top=1, Bottom=1, Left=1, Right=1.
  * All active pixels in $B$ match $1$s in $A$. **FIT! Output = 1.**

* **All other pixels $(r,c) \neq (2,2)$:**
  * For example, at $(1,2)$ (Row 1, Col 2), the Top neighbor in $A$ is Row 0 Col 2 = $0$. **FAIL! Output = 0.**
  * At $(2,1)$ (Row 2, Col 1), the Left neighbor in $A$ is Row 2 Col 0 = $0$. **FAIL! Output = 0.**

Resulting Eroded Matrix $A \ominus B$:

```math
A \ominus B = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

---

##### 2. Calculating Dilation $A \oplus B$:
For $A \oplus B$ at pixel $(r,c)$, if **at least one** active neighbor of $B$ centered at $(r,c)$ hits a $1$ in $A$, output is $1$. Because the cross SE is symmetric, this is equivalent to: output$(r,c) = 1$ if $A(r,c)$ **or any of its four 4-connected neighbors** — top $(r-1,c)$, bottom $(r+1,c)$, left $(r,c-1)$, right $(r,c+1)$ — is $1$.

* Original $3 \times 3$ block of $1$s spans rows $1..3$ and cols $1..3$.
* **Every** original foreground pixel stays $1$ (it hits itself).
* **Every** foreground pixel also switches its four cardinal neighbors on, so the block grows outward by one pixel along each edge — not just at the single midpoint of each side:
  * Top edge (row $1$, cols $1..3$) pushes row $0$, cols $1..3$ to $1$.
  * Bottom edge (row $3$, cols $1..3$) pushes row $4$, cols $1..3$ to $1$.
  * Left edge (col $1$, rows $1..3$) pushes col $0$, rows $1..3$ to $1$.
  * Right edge (col $3$, rows $1..3$) pushes col $4$, rows $1..3$ to $1$.
* The four corner pixels of the $5 \times 5$ grid — $(0,0)$, $(0,4)$, $(4,0)$, $(4,4)$ — stay $0$ because the cross SE never reaches diagonally.

Resulting Dilated Matrix $A \oplus B$:

```math
A \oplus B = \begin{bmatrix} 0 & 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 & 0 \end{bmatrix}
```

---

##### 3. Calculating Opening $A \circ B = (A \ominus B) \oplus B$:
Opening dilates the eroded image $A \ominus B$ using $B$:
* Input matrix to dilate: $A \ominus B$ (which contains a single $1$ at $(2,2)$).
* Dilating a single $1$ at $(2,2)$ with cross SE $B$ places the shape of $B$ centered at $(2,2)$.

Resulting Opened Matrix $A \circ B$:

```math
A \circ B = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

---

## Section 3: Hit-or-Miss Transformation (HMT)

### 3.1 Concept, Purpose, and Shape Matching

The **Hit-or-Miss Transformation (HMT)** is a fundamental morphological tool for **binary pattern recognition**, **landmark detection**, and **shape extraction**. While standard erosion detects where a foreground shape fits, HMT simultaneously searches for specific **foreground configurations (hits)** AND specific **background configurations (misses)**.

It is used to locate specific pixel configurations such as:
* Isolated single foreground pixels.
* Line end-points and junction/branch points.
* Corners (e.g., upper-right corner of a rectangle).

---

### 3.2 Mathematical Formulation & Dual Structuring Elements

The Hit-or-Miss transform of set $A$ by a composite structuring element pair $B = (B_1, B_2)$ is defined as:
$$A \circledast B = (A \ominus B_1) \cap (A^c \ominus B_2)$$

Where:
* $B_1$ is the **foreground structuring element** (searches for "hits" in $A$).
* $B_2$ is the **background structuring element** (searches for "misses" in $A$, i.e., hits in $A^c$).
* $A^c$ is the set complement (background) of image $A$.
* $B_1$ and $B_2$ must be mutually disjoint: $B_1 \cap B_2 = \emptyset$.

```text
+-----------------------------------------------------------------------+
|                    HIT-OR-MISS TRANSFORM PIPELINE                     |
|                                                                       |
|  [ Image A ] -------------> [ Erode with B1 ] -------+                 |
|                                                       |               |
|                                                       v               |
|                                                  [ INTERSECT ] ----> [ Result ]
|                                                       ^               |
|                                                       |               |
|  [ Complement A^c ] ------> [ Erode with B2 ] -------+                 |
+-----------------------------------------------------------------------+
```

---

### 3.3 Composite Structuring Element Notation (Hits, Misses, Don't Cares)

Rather than maintaining two separate matrices $B_1$ and $B_2$, HMT is conventionally represented using a single **composite $3 \times 3$ matrix** containing three symbol values:

1. **$1$ (Foreground Hit):** Must match a foreground pixel ($1$) in $A$ ($B_1$).
2. **$0$ (Background Miss):** Must match a background pixel ($0$) in $A$ ($B_2$).
3. **$x$ or $\times$ (Don't Care):** Ignored during comparison; can match either $0$ or $1$.

#### Example: Upper-Right Corner Detector Structuring Element:

```math
B = \begin{bmatrix} x & 0 & 0 \\ 1 & 1 & 0 \\ x & 1 & x \end{bmatrix}
```

Here:
* $B_1$ (Hits) = $\{(1,0), (1,1), (2,1)\}$
* $B_2$ (Misses) = $\{(0,1), (0,2), (1,2)\}$
* $x$ (Don't Care) = $\{(0,0), (2,0), (2,2)\}$

---

### 3.4 Step-by-Step Worked Example: Corner & Landmark Detection

#### ❓ Problem Statement:
Find all locations in image $A$ that match the upper-right corner probe $B$:

```math
A = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}, \quad
B = \begin{bmatrix} x & 0 & 0 \\ 1 & 1 & 0 \\ x & 1 & x \end{bmatrix}
```

---

#### 💡 Step-by-Step Solution:

1. **Construct Complement Image $A^c$:**

```math
A^c = \begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\ 1 & 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 \end{bmatrix}
```

2. **Erode $A$ with $B_1$ (Foreground Hits):**
   $B_1$ requires $1$s at center $(1,1)$, left $(1,0)$, and bottom $(2,1)$.
   * Testing location $(1,2)$ (Row 1, Col 2 in $A$):
     * Center $(1,2)=1$, Left $(1,1)=1$, Bottom $(2,2)=1$. **FIT! Output = 1.**
   * All other locations fail $B_1$ inclusion.

```math
(A \ominus B_1) = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

3. **Erode $A^c$ with $B_2$ (Background Misses):**
   $B_2$ requires $1$s in $A^c$ at top $(0,1)$, top-right $(0,2)$, and right $(1,2)$ relative to the origin. *Border convention:* pixels outside the $4 \times 5$ image are treated as $0$ in **both** $A$ and $A^c$ during erosion (the same zero-padding convention used everywhere else in this example) — $A^c$ is **not** re-extended to $1$ outside the image.
   * At $(1,2)$: Top $(0,2)=1$, Top-Right $(0,3)=1$, Right $(1,3)=1$. **FIT!**
   * At $(1,3)$: Top $(0,3)=1$, Top-Right $(0,4)=1$, Right $(1,4)=1$. **FIT!**
   * At $(2,3)$: Top $(1,3)=1$, Top-Right $(1,4)=1$, Right $(2,4)=1$. **FIT!**
   * At $(3,3)$: Top $(2,3)=1$, Top-Right $(2,4)=1$, Right $(3,4)=1$. **FIT!**
   * All other locations fail because at least one of the three required $1$s falls on a $0$ pixel of $A^c$ (or off the image edge).

```math
(A^c \ominus B_2) = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 \end{bmatrix}
```

> ⚠️ **Common slip:** it's tempting to stop at the first fit found and assume the pattern only matches once. Always scan every candidate location — here $B_2$ alone fits at **four** locations; it's only the intersection with $A \ominus B_1$ below that narrows this down to the single corner pixel.

4. **Intersect Results:**

```math
A \circledast B = (A \ominus B_1) \cap (A^c \ominus B_2) = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

The Hit-or-Miss transform successfully pinpoints the exact upper-right corner pixel at coordinate $(1,2)$!

---

## Section 4: Morphological Algorithms: Boundary Extraction

### 4.1 Boundary Extraction Concept and Mathematical Derivation

The boundary of a binary object $A$, denoted $\beta(A)$, can be derived morphologically by eroding $A$ with a suitable structuring element $B$ and subtracting the eroded image from the original image $A$.

#### Mathematical Derivation:
$$\beta(A) = A - (A \ominus B) = A \cap (A \ominus B)^c$$

```text
+-----------------------------------------------------------------------+
|                     BOUNDARY EXTRACTION MECHANISM                     |
|                                                                       |
|   [ Original Object A ]   -   [ Eroded Object (A ⊖ B) ]   =  [ β(A) ] |
|                                                                       |
|      1 1 1 1 1                   0 0 0 0 0                   1 1 1 1 1|
|      1 1 1 1 1                   0 1 1 1 0                   1 0 0 0 1|
|      1 1 1 1 1                   0 1 1 1 0                   1 0 0 0 1|
|      1 1 1 1 1                   0 1 1 1 0                   1 0 0 0 1|
|      1 1 1 1 1                   0 0 0 0 0                   1 1 1 1 1|
+-----------------------------------------------------------------------+
```

---

### 4.2 Structuring Element Connectivity & Boundary Thickness

The choice of structuring element $B$ controls **which** pixels erosion strips away, and therefore how thick and how connected the resulting boundary $\beta(A) = A - (A \ominus B)$ is:

1. **Underlying principle:** $\beta(A)$ keeps exactly the foreground pixels that erosion removes — i.e. every foreground pixel that has at least one SE-neighbor position falling outside $A$. A larger SE reaches farther into the interior before a pixel survives erosion, so it strips (and therefore keeps in the boundary) a wider rim.
2. **Typical $3 \times 3$ case:** with a $3 \times 3$ cross (4-connected) SE, erosion only requires the 4-connected neighbors to be foreground, so it tends to leave diagonal-only connections in the boundary it exposes; with a $3 \times 3$ square (8-connected) SE, erosion also requires the diagonal neighbors, so it tends to strip a boundary that stays 4-connected. These tendencies hold for simple, convex shapes (like the rectangle in the worked example below) but are **not guaranteed for arbitrary shapes** — thin spurs, concave corners, or 1-pixel-wide regions can produce boundaries whose connectivity doesn't follow this rule of thumb.
3. **Larger structuring elements ($5 \times 5$, $7 \times 7$, ...):** erode further into the interior before a pixel survives, so they generally expose a thicker boundary ($2$ or more pixels wide) rather than the crisp $1$-pixel-thick rim a $3 \times 3$ SE produces.

The worked example in §4.3 below uses a $3 \times 3$ square SE on a filled rectangle — a case where the square SE does strip a 4-connected, 1-pixel-thick boundary, illustrated concretely with the actual matrices.

---

### 4.3 Step-by-Step Worked Numerical Example: Inner Boundary Extraction

#### ❓ Problem Statement:
Given binary image $A$ ($1 = \text{foreground}$):

```math
A = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

Extract the inner boundary $\beta(A)$ using $3 \times 3$ square SE $B$:

```math
B = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}
```

---

#### 💡 Step-by-Step Solution:

1. **Erode $A$ with $3 \times 3$ Square $B$ ($A \ominus B$):**
   A pixel at $(r,c)$ survives erosion only if all 8 neighbors and center are $1$.
   * Interior pixels $(2,2)$ and $(2,3)$ are completely surrounded by $1$s in $A$.
   * All boundary pixels at rows 1 and 4, cols 1 and 4 fail erosion.

```math
A \ominus B = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

2. **Subtract Eroded Matrix from Original Image ($\beta(A) = A - (A \ominus B)$):**

```math
\beta(A) = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 1 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

The resulting matrix contains a clean, 1-pixel-thick inner boundary mask!

---

## Section 5: Morphological Algorithms: Thinning and Thickening

### 5.1 Morphological Thinning

#### 1. Definition and Purpose:
Thinning reduces binary objects to **1-pixel-thick linear structures** or skeletons while preserving object topology (connectivity and Euler number).

#### 2. Mathematical Formulation:
Thinning of set $A$ by structuring element $B$, denoted $A \otimes B$, is defined using the Hit-or-Miss transform:
$$A \otimes B = A - (A \circledast B) = A \cap (A \circledast B)^c$$

Thinning subtracts from $A$ any pixel location that matches the hit-or-miss pattern $B$.

---

### 5.2 Sequential Thinning & Structuring Element Sequences

In practice, thinning with a single SE is directional. To thin an object symmetrically from all sides, thinning is applied **sequentially** using a sequence of rotated structuring elements $\{B\} = \{B^1, B^2, B^3, \dots, B^8\}$:

$$A \otimes \{B\} = \left( \left( \dots \left( (A \otimes B^1) \otimes B^2 \right) \dots \right) \otimes B^8 \right)$$

The sequence is repeatedly cycled until convergence is reached (i.e., when a full pass produces no further pixel deletions: $A_k = A_{k-1}$).

#### 💡 Worked Example: One Thinning Pass with $B^1$

Take a small $5 \times 5$ "plus" shape $A$ and the Golay pattern $B^1$ (below): center must be foreground, the entire bottom row of the SE must be foreground, and the entire top row must be background (left/right columns are don't-care):

```math
A = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}, \quad
B^1 = \begin{bmatrix} 0 & 0 & 0 \\ x & 1 & x \\ 1 & 1 & 1 \end{bmatrix}
```

Testing every foreground pixel of $A$ as a candidate center for $B^1$:
* $(1,2)$: top row $(0,1),(0,2),(0,3) = 0,0,0$ ✓; bottom row $(2,1),(2,2),(2,3) = 1,1,1$ ✓. **Match.**
* $(2,1)$: top row $(1,0),(1,1),(1,2) = 0,0,1$ — fails (top-right is $1$, must be $0$).
* $(2,2)$: top row $(1,1),(1,2),(1,3) = 0,1,0$ — fails (top-center is $1$).
* $(2,3)$: top row $(1,2),(1,3),(1,4) = 1,0,0$ — fails (top-left is $1$).
* $(3,2)$: top row $(2,1),(2,2),(2,3) = 1,1,1$ — fails (top row must be all $0$).

Only $(1,2)$ matches, so $A \otimes B^1 = A - \{(1,2)\}$ removes just the top arm of the plus shape:

```math
A \otimes B^1 = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
```

$B^1$ is built to catch a foreground pixel that sticks out from a flat, fully-foreground edge below it with nothing but background above it — exactly the top arm here. A full thinning pass repeats this test with each rotated $B^2, \dots, B^8$ against the *updated* image, and the whole sequence cycles until nothing changes.

#### Standard 8-Neighbor Thinning Structuring Element Sequence (Golay Alphabet):

```math
B^1 = \begin{bmatrix} 0 & 0 & 0 \\ x & 1 & x \\ 1 & 1 & 1 \end{bmatrix}, \quad
B^2 = \begin{bmatrix} x & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & x \end{bmatrix}, \quad
B^3 = \begin{bmatrix} 1 & x & 0 \\ 1 & 1 & 0 \\ 1 & x & 0 \end{bmatrix}, \dots
```
*(Rotated by $45^\circ$ for each step).*

---

### 5.3 Morphological Thickening

#### 1. Definition and Purpose:
Thickening is the morphological dual of thinning. It expands binary shapes by appending pixels to outer boundaries based on background pattern matching.

#### 2. Mathematical Formulation:
Thickening of set $A$ by structuring element $B$, denoted $A \odot B$, is defined as:
$$A \odot B = A \cup (A \circledast B)$$

> ⚠️ **Origin must sit in the background:** for this union to actually add pixels, $B$'s foreground-hit part $B_1$ must **not** contain the origin (the origin position must be one of $B_2$'s background-miss cells instead). If $B_1$ included the origin, every location that matches $B$ would already have a foreground pixel at the origin — it would already be in $A$, and the union $A \cup (A \circledast B)$ would add nothing.

Sequential thickening uses a sequence of structuring elements:
$$A \odot \{B\} = \left( \left( \dots \left( (A \odot B^1) \odot B^2 \right) \dots \right) \odot B^8 \right)$$

#### 💡 Worked Example: Reversing the Thinning Pass Above

Start from the thinned shape $A_1 = A \otimes B^1$ from §5.2 (the plus with its top arm removed), and design a pattern $D$ (origin in the background, per the warning above) whose foreground part is the bottom row and whose background part is the top row **and the center**:

```math
A_1 = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}, \quad
D = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}
```

Scanning every location, the only fit is at $(1,2)$: its center and top row are all $0$ in $A_1$ (matching $D$'s background part), and its bottom row $(2,1),(2,2),(2,3) = 1,1,1$ (matching $D$'s foreground part). No other location satisfies both conditions simultaneously. So $A_1 \circledast D = \{(1,2)\}$, and:
$$A_1 \odot D = A_1 \cup \{(1,2)\}$$
which restores the original plus shape $A$ — concretely demonstrating that thickening adds a pixel exactly where the background pattern matches.

---

### 5.4 Duality between Thinning and Thickening

Thickening of a set $A$ is equivalent to the complement of the thinning of $A$'s complement ($A^c$):
$$(A \odot B)^c = A^c \otimes B$$

> 🧠 **Must Understand:** To thicken $A$, thin the background $A^c$ and take the complement of the result! This requires the foreground/background parts of the pattern applied to $A^c$ to be handled consistently with $B$'s parts on $A$ — concretely, thinning $A^c$ with $B$ means testing $B_1$ against $A^c$'s foreground (i.e. $A$'s background) and $B_2$ against $A^c$'s background (i.e. $A$'s foreground), which is exactly the composite pattern $D$ used above, mirrored.

---

### 5.5 Application to Skeletonization and Pruning

1. **Skeletonization:** Extracts the medial axis of a shape. A skeleton represents the structural backbone of an object while remaining equidistant to object boundaries.
2. **Pruning:** Post-processing operation applied after skeletonization/thinning to eliminate small unwanted "parasitic spurs" (branch artifacts) caused by boundary noise.

---

## Section 6: Grayscale Morphology

### 6.1 Extension from Binary Sets to Intensity Functions

Grayscale morphology extends set-theoretic binary operations to continuous or digital intensity functions $f(x,y)$, where pixel values represent height/elevation on a 3D topographic surface:
* **Bright pixels (high intensities):** Represent peaks/hills.
* **Dark pixels (low intensities):** Represent valleys/basins.

Operations act on intensity profiles using minimum ($\min$) and maximum ($\max$) neighborhood operations.

> 📎 **Scope note:** the syllabus for this unit names "Grayscale Morphology" together with dilation, erosion, opening, closing, morphological gradient, and top-hat/bottom-hat (§6.3–§6.6 below). Skeletonization and pruning (§5.5) are included here as useful, closely related extensions of thinning/thickening, but check with your course source before treating them as individually examinable topics in their own right.

---

### 6.2 Flat vs. Non-Flat Structuring Functions

1. **Flat Structuring Element ($b(s,t) = 0$):**
   * A flat SE defined over a spatial domain $B$. It has zero height value throughout.
   * Simplifies operations to standard neighborhood $\min$ and $\max$ calculations.
2. **Non-Flat Structuring Element ($b(s,t)$):**
   * Has a defined height profile $b(s,t)$ added to or subtracted from image intensities.

---

### 6.3 Grayscale Dilation and Grayscale Erosion

#### 1. Grayscale Dilation:
For an image $f(x,y)$ and a flat structuring element $b$ over domain $B$:
$$(f \oplus b)(x,y) = \max_{(s,t) \in B} \{ f(x-s, y-t) \}$$

* **Effect:** Increases overall brightness, expands bright intensity peaks, and fills/suppresses small dark details/valleys.

#### 2. Grayscale Erosion:
For an image $f(x,y)$ and a flat structuring element $b$ over domain $B$:
$$(f \ominus b)(x,y) = \min_{(s,t) \in B} \{ f(x+s, y+t) \}$$

* **Effect:** Decreases overall brightness, expands dark valleys, and suppresses small bright details/spikes (salt noise).

---

### 6.4 Grayscale Opening and Grayscale Closing

#### 1. Grayscale Opening:
$$(f \circ b) = (f \ominus b) \oplus b$$
* **Effect:** Removes small **bright details (peaks)** that are smaller than the structuring element, while preserving dark backgrounds and overall intensity levels.

#### 2. Grayscale Closing:
$$(f \bullet b) = (f \oplus b) \ominus b$$
* **Effect:** Fills small **dark details (valleys/holes)** that are smaller than the structuring element, while preserving bright regions.

---

### 6.5 Grayscale Morphological Gradient

The **Morphological Gradient** enhances intensity edges and object boundaries by computing the difference between grayscale dilation and erosion:
$$g = (f \oplus b) - (f \ominus b)$$

Because dilation expands bright regions and erosion shrinks them, their difference yields a symmetric boundary edge map highlighting regions of rapid intensity variation.

---

### 6.6 Top-Hat and Bottom-Hat Transformations

#### 1. Top-Hat Transformation (White Top-Hat):
$$T_{\text{hat}}(f) = f - (f \circ b)$$
* **Purpose:** Isolates **bright features/objects** that are smaller than the structuring element on a dark or uneven background (e.g., detecting bright micro-calcifications in mammograms).

#### 2. Bottom-Hat Transformation (Black Top-Hat):
$$B_{\text{hat}}(f) = (f \bullet b) - f$$
* **Purpose:** Isolates **dark features/objects** that are smaller than the structuring element on a bright or uneven background (e.g., extracting dark blood vessels).

---

### 6.7 Step-by-Step Worked Numerical Example: Grayscale Operations

#### ❓ Problem Statement:
Given a $4 \times 4$ grayscale image patch $f$:

```math
f = \begin{bmatrix} 10 & 12 & 15 & 20 \\ 11 & 85 & 14 & 18 \\ 13 & 15 & 16 & 22 \\ 12 & 14 & 18 & 25 \end{bmatrix}
```

*(Notice the isolated bright noise spike of value $85$ at $(1,1)$).*

Apply a flat $3 \times 3$ square structuring element $b$ ($3 \times 3$ neighborhood centered at target pixel) to compute for interior pixels $(1,1)$ and $(1,2)$:
1. Grayscale Dilation $(f \oplus b)$
2. Grayscale Erosion $(f \ominus b)$
3. Grayscale Morphological Gradient $g = (f \oplus b) - (f \ominus b)$

---

#### 💡 Step-by-Step Solution:

##### 1. Grayscale Dilation $(f \oplus b) = \max \text{ in } 3 \times 3 \text{ neighborhood}$:

* **At Pixel $(1,1)$ (Value 85):**
  * Neighborhood values (rows 0..2, cols 0..2):
    $$\begin{bmatrix} 10 & 12 & 15 \\ 11 & 85 & 14 \\ 13 & 15 & 16 \end{bmatrix}$$
  * Maximum value = $85$. Output $(1,1) = 85$.

* **At Pixel $(1,2)$ (Value 14):**
  * Neighborhood values (rows 0..2, cols 1..3):
    $$\begin{bmatrix} 12 & 15 & 20 \\ 85 & 14 & 18 \\ 15 & 16 & 22 \end{bmatrix}$$
  * Maximum value = $85$. Output $(1,2) = 85$.

---

##### 2. Grayscale Erosion $(f \ominus b) = \min \text{ in } 3 \times 3 \text{ neighborhood}$:

* **At Pixel $(1,1)$ (Value 85):**
  * Minimum in neighborhood $\{10, 12, 15, 11, 85, 14, 13, 15, 16\} = 10$.
  * Output $(1,1) = 10$.
  *(The bright spike $85$ is completely erased!)*

* **At Pixel $(1,2)$ (Value 14):**
  * Minimum in neighborhood $\{12, 15, 20, 85, 14, 18, 15, 16, 22\} = 12$.
  * Output $(1,2) = 12$.

---

##### 3. Morphological Gradient $g = (f \oplus b) - (f \ominus b)$:

* **At Pixel $(1,1)$:**
  $$g(1,1) = 85 - 10 = 75$$
* **At Pixel $(1,2)$:**
  $$g(1,2) = 85 - 12 = 73$$

Both pixels exhibit high gradient values, indicating strong local boundary variations!

---

## Section 7: Master Comparison Tables

### Table 7.1: Fundamental Binary Morphological Operations

| Operation | Formula | Order of Steps | Primary Objective | Boundary / Area Change |
| :--- | :--- | :--- | :--- | :--- |
| **Dilation** | $A \oplus B$ | Single step | Fill holes, bridge gaps | Expands foreground |
| **Erosion** | $A \ominus B$ | Single step | Remove noise, disconnect bridges | Shrinks foreground |
| **Opening** | $A \circ B$ | Erosion $\to$ Dilation | Remove small specks, smooth outer contours | Preserves major size ($A \circ B \subseteq A$) |
| **Closing** | $A \bullet B$ | Dilation $\to$ Erosion | Fill holes/cracks, smooth inner contours | Preserves major size ($A \subseteq A \bullet B$) |
| **Hit-or-Miss** | $A \circledast B$ | $(A \ominus B_1) \cap (A^c \ominus B_2)$ | Exact pattern / landmark detection | Outputs single-pixel location masks |

---

### Table 7.2: Binary vs. Grayscale Morphology

| Domain | Underlying Mathematics | Dilation Action | Erosion Action | Key Filters |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Morphology** | Set Theory ($\cap, \cup, \subseteq$) | Overlap / Hit test | Inclusion / Fit test | Boundary extraction, Thinning, Skeletonization |
| **Grayscale Morphology** | Function Min/Max Calculus | Neighborhood Maximum ($\max$) | Neighborhood Minimum ($\min$) | Morphological Gradient, Top-Hat, Bottom-Hat |

---

## Section 8: Formula Master Reference Sheet

$$\text{Binary Dilation:} \quad A \oplus B = \{z \mid (\hat{B})_z \cap A \neq \emptyset\}$$

$$\text{Binary Erosion:} \quad A \ominus B = \{z \mid (B)_z \subseteq A\}$$

$$\text{Morphological Opening:} \quad A \circ B = (A \ominus B) \oplus B$$

$$\text{Morphological Closing:} \quad A \bullet B = (A \oplus B) \ominus B$$

$$\text{Duality Relations:} \quad (A \ominus B)^c = A^c \oplus \hat{B}, \quad (A \circ B)^c = A^c \bullet \hat{B}$$

$$\text{Hit-or-Miss Transform:} \quad A \circledast B = (A \ominus B_1) \cap (A^c \ominus B_2)$$

$$\text{Boundary Extraction:} \quad \beta(A) = A - (A \ominus B)$$

$$\text{Morphological Thinning:} \quad A \otimes B = A - (A \circledast B)$$

$$\text{Morphological Thickening:} \quad A \odot B = A \cup (A \circledast B)$$

$$\text{Thickening Duality:} \quad (A \odot B)^c = A^c \otimes B$$

$$\text{Grayscale Dilation (Flat SE):} \quad (f \oplus b)(x,y) = \max_{(s,t) \in B} \{ f(x-s, y-t) \}$$

$$\text{Grayscale Erosion (Flat SE):} \quad (f \ominus b)(x,y) = \min_{(s,t) \in B} \{ f(x+s, y+t) \}$$

$$\text{Morphological Gradient:} \quad g = (f \oplus b) - (f \ominus b)$$

$$\text{Top-Hat Transformation:} \quad T_{\text{hat}}(f) = f - (f \circ b)$$

$$\text{Bottom-Hat Transformation:} \quad B_{\text{hat}}(f) = (f \bullet b) - f$$

---

## Section 9: Common Exam Mistakes & Pitfalls

1. ❌ **Reversing Order of Operations in Opening vs. Closing:**
   * *Mistake:* Writing Opening as Dilation followed by Erosion.
   * *Correction:* Opening is **Erosion FIRST**, then Dilation. Closing is **Dilation FIRST**, then Erosion.

2. ❌ **Confusing Fit (Erosion) and Hit (Dilation):**
   * *Mistake:* Thinking erosion requires only a single matching pixel.
   * *Correction:* Erosion requires ALL active $1$s of the SE to match $1$s in $A$ (**Fitting**). Dilation requires at least ONE active $1$ of the SE to match a $1$ in $A$ (**Hitting**).

3. ❌ **Forgetting Set Complement in Hit-or-Miss Transform:**
   * *Mistake:* Computing HMT as $(A \ominus B_1) \cap (A \ominus B_2)$.
   * *Correction:* The second term MUST be eroded on the **complement image $A^c$**: $(A \ominus B_1) \cap (A^c \ominus B_2)$.

4. ❌ **Incorrect Boundary Extraction Subtraction Order:**
   * *Mistake:* Subtracting $A$ from eroded image: $(A \ominus B) - A$.
   * *Correction:* Always subtract the smaller eroded image from the original image: $\beta(A) = A - (A \ominus B)$.

5. ❌ **Mixing Flat and Non-Flat Grayscale Operations:**
   * *Mistake:* Adding SE values when evaluating flat SE operations.
   * *Correction:* For flat SE ($b=0$), grayscale dilation is strictly neighborhood $\max$, and erosion is strictly neighborhood $\min$.

---

## Section 10: Unit 4 Quick Revision & Coverage Checklist

* [x] **Dilation ($A \oplus B$):** Expands foreground, fills holes, uses neighborhood OR / Max.
* [x] **Erosion ($A \ominus B$):** Shrinks foreground, removes specks, uses neighborhood AND / Min.
* [x] **Opening ($A \circ B$):** Erosion then Dilation. Removes small noise, smooths contours ($A \circ B \subseteq A$).
* [x] **Closing ($A \bullet B$):** Dilation then Erosion. Fills small holes, bridges gaps ($A \subseteq A \bullet B$).
* [x] **Hit-or-Miss ($A \circledast B$):** $(A \ominus B_1) \cap (A^c \ominus B_2)$. Shape & landmark detection.
* [x] **Boundary Extraction ($\beta(A)$):** $A - (A \ominus B)$. Extracts 1-pixel-thick inner boundary.
* [x] **Thinning ($A \otimes B$):** $A - (A \circledast B)$. Skeletonization and linear structure reduction.
* [x] **Thickening ($A \odot B$):** $A \cup (A \circledast B)$. Boundary expansion dual to thinning.
* [x] **Grayscale Dilation/Erosion:** Max/Min intensity filtering over local SE neighborhood.
* [x] **Top-Hat / Bottom-Hat:** $f - (f \circ b)$ highlights bright details; $(f \bullet b) - f$ highlights dark details.

---
