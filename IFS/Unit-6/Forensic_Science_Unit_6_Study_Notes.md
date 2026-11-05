# Unit 6: Digital Forensics — Comprehensive Study Notes

This comprehensive, exam-oriented study notes document covers **Unit 6: Digital Forensics** as specified in the NMIMS Course Policy (`IFS Course policy 2026-27 (1).docx`). It is grounded in the primary lecture slide deck **`IFS PPT Unit 6_2025.pptx`** and supported by authoritative reference texts including Richard Saferstein's *Criminalistics: An Introduction to Forensic Science* (Chapter 19), *Guide to Computer Forensics and Investigations* (Bill Nelson et al.), *Introduction to Forensic Psychology* (Bartol & Bartol), B.R. Sharma's *Forensic Science in Criminal Investigation and Trials* (Chapter 26), and Gautam Biswas's *Review of Forensic Medicine and Toxicology*.

---

## Course Policy & Learning Objective Alignment

* **Course Outcome (CO):** **CO5** — Demonstrate understanding of digital forensic principles and cybercrime typologies through case-based reasoning.
* **Bloom's Taxonomy Level:** **K2 (Understand) / K3 (Apply)** — Demonstration of theoretical comprehension, threat classification, digital evidence extraction mechanics, and practical application of forensic tools to digital investigations.

---

## Section 1: Introduction to Cybercrime & Computer Crimes

### 1.1 Core Definitions & Conceptual Foundations

* **Cybercrime (Computer Crime):** Any criminal activity that involves the use of a computer, a networked device, or digital system as a **tool**, a **target**, or a **place** (medium) to commit illegal acts [Slide 1; Saferstein, Ch. 19; B.R. Sharma, Ch. 26].
* **The Dual Taxonomy of Cybercrimes:**
  1. **Cyber-Enabled Crimes:** Traditional crimes (such as financial fraud, harassment, theft, child exploitation, and extortion) that are enhanced, scaled, or facilitated by the internet or computer networks [Slide 1].
  2. **Cyber-Dependent Crimes:** Offenses that can only be committed through the use of digital technologies and computers as both the tool and target (such as hacking, malware distribution, ransomware, and Distributed Denial of Service / DDoS attacks) [Slide 2].

```
                             CLASSIFICATION OF CYBERCRIMES
                                           │
            ┌──────────────────────────────┴──────────────────────────────┐
            ▼                                                             ▼
   CYBER-ENABLED CRIMES                                       CYBER-DEPENDENT CRIMES
(Traditional crimes facilitated by IT)                    (Crimes existing solely in digital space)
   • Online Fraud & Bank Scams                               • Hacking & System Intrusion
   • Cyberstalking & Harassment                              • Virus / Worm / Ransomware Spread
   • Intellectual Property Theft                             • DDoS Attacks on Infrastructure
   • Identity Theft & Phishing                               • Logic Bombs & System Sabotage
```

---

### 1.2 Comparison: Conventional Crimes vs. Computer Crimes

The primary distinction between conventional (traditional) crimes and computer crimes lies in the tools, methods, physical proximity, and nature of the affected assets [Slide 2–3, 13–15]:

| Comparative Dimension | Conventional (Physical) Crimes | Computer (Cyber) Crimes |
| :--- | :--- | :--- |
| **Primary Medium** | Physical tools (weapons, physical force, direct interpersonal interaction) [Slide 13]. | Digital systems, computers, software, and electronic communication networks [Slide 13]. |
| **Mode of Operation** | Requires direct physical presence at the scene of the crime [Slide 14]. | Executed remotely across virtual environments without physical proximity to the victim [Slide 14]. |
| **Geographical Reach** | Generally localized and confined to a specific physical geographic area [Slide 14]. | Global reach; can be executed instantaneously from anywhere in the world across borders [Slide 14]. |
| **Target / Asset Type** | Affects tangible physical property, bodily safety, or real-world structures [Slide 3]. | Targets intangible digital assets (information, databases, system integrity, financial records) [Slide 3]. |
| **Technical Expertise** | Requires physical planning, stealth, or force; minimal technical knowledge [Slide 15]. | Demands specialized technical expertise in networking, coding, and system exploitation [Slide 15]. |
| **Physical Evidence** | Leaves physical trace evidence (fingerprints, DNA, bloodstains, toolmarks) [B.R. Sharma, Ch. 26]. | Leaves intangible, volatile digital artifacts (log files, IP addresses, memory dumps, MAC times) [Slide 20]. |
| **Jurisdiction & Laws** | Well-established local legal codes (e.g., IPC, CrPC) with clear physical boundaries [Slide 15]. | Evolving international legal frameworks facing severe jurisdictional and extradition hurdles [Slide 15]. |

---

### 1.3 Reasons & Motivations for the Commission of Computer Crimes

Understanding why individuals or organized groups engage in cybercrime is essential for threat assessment and digital risk management [Slide 3–4, 12]:

1. **Anonymity & Masking:** The perception of anonymity provided by the internet, VPNs, proxy servers, and encrypted dark web networks emboldens perpetrators, making identity tracing difficult [Slide 3].
2. **High Financial Gain:** Cybercriminals target online banking, cryptocurrency wallets, corporate databases, and ransomware extortion schemes for immense financial returns [Slide 4].
3. **Political & Ideological Motives:** Hacktivists and state-sponsored threat actors target government infrastructure, defense portals, or corporate targets to advance political agendas [Slide 4].
4. **Revenge & Personal Grievances:** Disgruntled employees (insiders), ex-partners, or rival businesses execute cyber-attacks to cause reputational or operational damage [Slide 4].
5. **Low Risk of Detection:** The faceless, borderless nature of cyberspace means attackers face a low probability of immediate physical apprehension [B.R. Sharma, Ch. 26].
6. **Lack of Awareness / Ignorance:** Users or novice hackers may not comprehend the legal severity of digital actions (e.g., downloading pirated software, running stresser tools) [Slide 4].

---

### 1.4 The CIA Triad in Information Security

All digital system operations and security assessments revolve around maintaining the **CIA Triad** [Slide 12]:

* **Confidentiality:** Ensuring that sensitive data is protected from unauthorized access or disclosure (e.g., encryption, access control lists) [Slide 12].
* **Integrity:** Ensuring that data remains accurate, complete, and untampered throughout its lifecycle (e.g., cryptographic hashing, write-blockers) [Slide 12].
* **Availability:** Ensuring that digital systems, networks, and data remain accessible to authorized users when needed (mitigating DDoS, power outages, system crashes) [Slide 12].

---

## Section 2: Security Breaches & Malware Typologies

### 2.1 Mechanics of Digital Security Breaches

A **security breach** refers to any unauthorized access to digital systems, networks, or databases to steal, alter, or destroy data [Slide 5].

#### The 5 Stages of an Attack Lifecycle:
1. **Reconnaissance:** Preliminary research and information gathering regarding the target system (network scanning, OSINT, social engineering) [Slide 16].
2. **Initial Access:** Exploiting system vulnerabilities, weak passwords, or unpatched software to gain entry (phishing emails, exploit kits) [Slide 16].
3. **Privilege Escalation:** Gaining higher-level administrative privileges (root/system access) to control the network [Slide 6].
4. **Data Exfiltration or Destruction:** Stealing sensitive corporate data, deploying ransomware, or deleting critical databases [Slide 17].
5. **Covering Tracks:** Hiding malicious presence by clearing system logs, altering timestamps, or executing anti-forensic tools [Slide 17].

```
                               STAGES OF A SECURITY BREACH
                                            │
  ┌─────────────────────────────────────────┼─────────────────────────────────────────┐
  ▼                                         ▼                                         ▼
1. RECONNAISSANCE ──► 2. INITIAL ACCESS ──► 3. PRIVILEGE ESCALATION ──► 4. EXFILTRATION ──► 5. COVERING TRACKS
 (Scanning / OSINT)   (Phishing / Exploit)   (Admin / Root Control)     (Data Theft / Loss)   (Log Deletion / Timestomping)
```

---

### 2.2 Malware & Threat Typologies Detailed Breakdown

Malicious software (**Malware**) includes any program or code designed to disrupt, damage, or gain unauthorized access to digital systems [Slide 18–22; Saferstein, Ch. 19; B.R. Sharma, Ch. 26].

```
                                  MALWARE TYPOLOGIES
                                          │
    ┌──────────────┬──────────────┬───────┴──────┬──────────────┬──────────────┐
    ▼              ▼              ▼              ▼              ▼              ▼
  VIRUS          WORM       TROJAN HORSE     TRAP DOOR   SUPER ZAPPING    LOGIC BOMB
(Needs Host & (Self-Spreads   (Disguised as  (Hidden Code  (Privilege     (Triggered by
 User Action)  Independently) Clean App)      Backdoor)    Bypass Tool)   Condition)
```

#### 1. Computer Virus vs. Computer Worm (The Core Distinction)

| Attribute | Computer Virus | Computer Worm |
| :--- | :--- | :--- |
| **Host File Requirement** | **Requires a Host File:** Must attach itself to an executable (`.exe`, `.docm`) file or document [Slide 18]. | **Standalone Program:** Operates independently without needing a host program or file [Slide 19]. |
| **Activation & Propagation**| **Requires Human Action:** Spreads only when a human user executes the infected file or opens an attachment [Slide 20]. | **Self-Replicating:** Spreads automatically across networks without human intervention [Slide 19]. |
| **Primary Impact** | Alters or corrupts files, damages software, and infects secondary storage drives [Slide 18]. | Consumes network bandwidth and memory resources, slowing or crashing entire systems [Slide 19]. |

#### 2. Specific Virus Categories & Symptoms:
* **Boot Sector Virus:** Infects the Master Boot Record (MBR) or boot sector of storage drives, executing before the OS loads [Slide 19].
* **Web Scripting Virus:** Embedded in website scripts (e.g., JavaScript) that execute when a user visits a compromised webpage [Slide 19].
* **Polymorphic Virus:** Modifies its underlying code/signature every time it infects a new file while keeping its function identical, evading signature-based antivirus scanners [Slide 19].
* **Metamorphic Virus:** Completely rewrites its structure and code architecture during every propagation cycle, making detection exceptionally difficult [Slide 19].
* **Macro Virus:** Written in macro languages (e.g., VBA) embedded inside office documents (Word, Excel) that trigger upon opening [Slide 19].
* **Common Virus Symptoms:** Unexpected pop-up ads, browser homepage changes, unauthorized contacts sent from user email, frequent blue screen of death (BSOD) crashes, slow system performance, and unknown startup applications [Slide 19–20].

#### 3. Trojan Horse
* **Mechanism:** Malware disguised as legitimate, safe, or desirable software (e.g., a free game, utility tool) [Slide 20].
* **Delivery:** Uses social engineering to trick the user into installing it. Once executed, it opens a backdoor for remote administrative control [Slide 20].
* **Real-World Examples:** *Rakhni Trojan* (delivers ransomware/cryptominers), *Tiny Banker Trojan* (steals financial banking credentials) [Slide 21].

#### 4. Trap Door (Backdoor)
* **Mechanism:** A hidden defect, deliberate bypass, or secret access point embedded in software source code by developers or attackers [Slide 21].
* **Impact:** Enables malicious actors to bypass standard authentication mechanisms and gain full access to system data [Slide 21].

#### 5. Super Zapping
* **Mechanism:** Unauthorized use of specialized utility software (historically derived from IBM mainframe "Superzap" maintenance tools) to bypass system controls [Slide 21].
* **Impact:** Overrides installed security features, master keys, or access controls to modify or exfiltrate protected databases directly [Slide 21].

#### 6. Logic Bomb
* **Mechanism:** Malicious code inserted into a software program that remains dormant until specific predetermined conditions or triggers are met [Slide 21].
* **Triggers:** A specific date/time (time bomb), deletion of an employee's user account, or a specific database entry [Slide 21].
* **Real-World Example:** *Duronio's Logic Bomb* (UBS PaineWebber case where a former employee set a logic bomb to delete financial files on a specific date) [Slide 21].

---

## Section 3: Cybercrime Categories & Cyber Threats

### 3.1 Major Categories of Cybercrimes

#### 1. Hacking & System Intrusion
* **Definition:** Unauthorized intrusion into a computer or network system to bypass security controls [Slide 22].
* **Key Mechanisms:** Network scanning, exploiting unpatched software bugs, SQL Injection (SQLi), brute-force password cracking, and zero-day exploits [Slide 12, 22].

#### 2. Intellectual Property Rights (IPR) Cybercrimes
* **Software Piracy:** Unauthorized copying, distribution, or commercial sale of copyrighted software or digital media (music, movies) [Slide 7].
* **Cybersquatting:** Unauthorized registration and trafficking of internet domain names identical or deceptively similar to established trademarks or corporate names [Slide 7].
* **Trade Secret Theft:** Illegal acquisition, exfiltration, or disclosure of confidential corporate trade secrets or proprietary algorithms via cyber espionage [Slide 8].
* **Patent Infringement:** Unauthorized commercial production, use, or sale of a patented digital or technological invention [Slide 8].

#### 3. Computer Terrorism & Critical Infrastructure Threats
* **Critical Infrastructure Attacks:** Cyber-attacks targeting essential public utilities (power grids, water treatment, air traffic control) to cause chaos [Slide 8].
* **Data Breaches & Extortion:** Exfiltrating massive government/corporate databases to blackmail institutions or publish classified materials [Slide 8].
* **Distributed Denial of Service (DDoS) Attacks:** Flooding target servers or web portals with immense illegitimate traffic from infected botnets (**Zombies**) to take them offline [Slide 9].
* **Website Defacement & Hijacking:** Modifying official web pages or social media accounts to post propaganda, false information, or cause panic [Slide 9].

#### 4. Cyber Hate Speech & Harassment
* **Social Media Abuse:** Targeted abusive messaging or hate speech directed at individuals based on ethnicity, race, or religion [Slide 9].
* **Online Extremist Forums:** Dedicated online platforms used to spread radicalization and incite physical violence [Slide 10].
* **Cyberbullying:** Systematic harassment, intimidation, or humiliation of individuals (frequently adolescents) using digital media [Slide 10].
* **Doxing:** Publishing an individual's private identifying information (home address, phone number, financial details) online with malicious intent to incite harassment [Slide 10].

#### 5. Private & National Security Threats
* Cyber espionage, unauthorized interception of defense communications, and state-sponsored cyber warfare targeting national sovereignty [Slide 8, 11].

---

### 3.2 Specific Cyber Threat Typologies

#### 1. Spamming
* **Definition:** Sending unsolicited bulk electronic messages indiscriminately, primarily for advertising or malware distribution [Slide 22].
* **Characteristics:** Mass distribution, lack of recipient consent, commercial/malicious intent, high frequency, and severe inbox congestion [Slide 22–23].

#### 2. Phishing
* **Definition:** Online fraud where attackers impersonate trustworthy institutions (banks, government portals) to steal credentials, credit card numbers, or PII [Slide 23].
* **Common Tactics:** Sense of urgency/fear, email address spoofing, counterfeit websites, and psychological social engineering [Slide 23–24].

#### 3. Catfishing
* **Definition:** Creating fake online personas or profiles to deceive victims into deceptive romantic or personal relationships [Slide 24].
* **Key Warning Signs:** Minimal social media history, stolen profile photos, avoiding video calls or in-person meetings, rapid emotional attachments ("love bombing"), and eventual requests for money or explicit media [Slide 24–25].
* **Motives:** Financial fraud, identity protection, harassment, personal insecurities, and social engineering data harvesting [Slide 25].

#### 4. Cyberstalking
* **Definition:** Using the internet, emails, social media, or electronic devices to repeatedly monitor, threaten, or harass an individual, causing emotional distress or fear [Slide 25; Bartol & Bartol, Ch. 12; Biswas, Ch. 16].
* **Three Primary Forms:**
  1. **Stalking by Email:** Direct transmission of threatening, hateful, or obscene messages to the victim's inbox [Slide 26].
  2. **Stalking through Internet:** Public harassment via forums, posting victim contact details or morphed images on explicit websites [Slide 26].
  3. **Stalking through Computer Control:** Advanced technocrat stalking where the perpetrator installs spyware/keyloggers to control the victim's computer remotely [Slide 26–27].
* **Statutory Provision (India):** Punishable under **Section 354-D of the Indian Penal Code (IPC)** and **Section 66E/67 of the Information Technology (IT) Act, 2000** [Biswas, Ch. 16].

---

## Section 4: Digital Evidence Extraction & Hard Disk Forensics

### 4.1 Fundamentals of Digital Forensics & Investigation Workflow

**Digital Forensics** is the branch of forensic science encompassing the identification, acquisition, recovery, analysis, and presentation of digital evidence stored on electronic devices and media [Slide 27; Saferstein, Ch. 19].

#### The 5-Stage Investigation Workflow:

```
                            5-STAGE DIGITAL FORENSICS WORKFLOW
                                            │
  ┌─────────────────────────────────────────┼─────────────────────────────────────────┐
  ▼                                         ▼                                         ▼
1. IDENTIFICATION ──► 2. ACQUISITION ───► 3. RECOVERY ─────► 4. ANALYSIS ─────► 5. PRESENTATION
(Locate media,       (Bit-stream image,   (Unallocated space, (Timeline, event  (Expert testimony,
 volatile data)       Chain of Custody)    slack, metadata)    reconstruction)    plain language)
```

1. **Identification:** Locating digital evidence, volatile RAM data, network sockets, running processes, and target storage media [Slide 28].
2. **Acquisition:** Preserving original evidence by creating a **1:1 bit-stream image** while maintaining an unbroken **Chain of Custody** [Slide 28].
3. **Recovery:** Extracting hidden, deleted, or fragmented files from unallocated space, slack space, metadata, and encrypted volumes (always working on copies) [Slide 28–29].
4. **Analysis:** Reconstructing events using log files, MAC timestamps, email headers, registry entries, and authorship analysis [Slide 29].
5. **Presentation:** Documenting findings in a legally admissible report and presenting expert witness testimony in plain language in court [Slide 30].

---

### 4.2 Hard Disk Drive (HDD) Geometry & Architecture

To extract data from a Hard Disk Drive (HDD), examiners must understand its physical and logical architecture [Saferstein, Ch. 19; Nelson et al., Ch. 5]:

* **Platters:** Circular aluminum or glass magnetic disks stacked vertically.
* **Tracks:** Concentric rings on each platter surface where data is recorded magnetically.
* **Sectors:** The smallest addressable unit of physical storage on a disk drive. Standard magnetic sectors hold **512 Bytes** of data (modern Advanced Format drives use 4096-Byte sectors) [Saferstein, Ch. 19].
* **Clusters (Allocation Units):** A logical grouping of contiguous sectors handled by the File System (e.g., FAT32, NTFS). Typical cluster sizes range from 1024 Bytes (2 sectors) to 4096 Bytes (8 sectors) [Saferstein, Ch. 19].

```
                                HARD DISK SECTOR & CLUSTER STRUCTURE
                                ┌───────────────────────────────────┐
                                │        CLUSTER (1024 Bytes)       │
                                ├─────────────────┬─────────────────┤
                                │ SECTOR 1        │ SECTOR 2        │
                                │ (512 Bytes)     │ (512 Bytes)     │
                                └─────────────────┴─────────────────┘
```

---

### 4.3 Data Categories: Visible Data vs. Latent Data

Digital storage media contains two fundamental classes of data [Saferstein, Ch. 19]:

| Data Category | Operational Definition | Examples & Locations |
| :--- | :--- | :--- |
| **Visible Data** | Data that the Operating System is aware of and is readily accessible to the user via standard file system operations. | User documents (`.docx`, `.pdf`), spreadsheets, accounting records, pictures, temporary files (`.tmp`), and swap space data [Saferstein, Ch. 19]. |
| **Latent Data** | Hidden or deleted data that the Operating System is *not* aware of, requiring specialized forensic software to recover. | RAM slack, File slack, unallocated disk space, deleted file remnants, and steganographic media [Slide 29; Saferstein, Ch. 19]. |

---

### 4.4 Bit-Stream Imaging vs. Standard Copying

* **Standard Copying / Backup:** Copies only active files recognized by the Operating System. Fails to copy deleted files, slack space, unallocated space, or hidden partitions [Nelson et al., Ch. 1].
* **Bit-Stream Copy (Forensic Image):** An exact bit-by-bit, sector-by-sector duplicate of the entire physical storage medium from the first bit (sector 0) to the very last bit [Slide 28; Saferstein, Ch. 19].
* **Hardware Write-Blockers:** Physical bridging devices connected between the evidence drive and the forensic workstation. They intercept write commands from the OS (e.g., Interrupt 13h) to ensure zero bits are altered on the evidence drive [Nelson et al., Ch. 3].
* **Common Forensic Image Formats:**
  * **RAW / Flat File (`.dd`, `.raw`):** Sequential sector-by-sector copy. Universal compatibility across all tools [Nelson et al., Ch. 3].
  * **Expert Witness Format (`.E01`):** Industry standard (EnCase format). Integrates metadata, case details, compression, and embedded MD5/SHA-1 hashes [Nelson et al., Ch. 3].
  * **Advanced Forensic Format (`.AFF`):** Open-source extensible image format.

---

### 4.5 Slack Space Mechanics & Analysis

**Slack Space** is the unused space created in a disk cluster when a saved file is smaller than the space allocated to it by the file system [Slide 29; Saferstein, Ch. 19].

#### Components of Slack Space:
1. **RAM Slack:** The remaining space from the end of the logical file to the end of that specific physical sector. The OS pads this space with zeros (or data dumped directly from RAM) [Saferstein, Ch. 19].
2. **File Slack (Drive Slack):** The remaining unused sectors within the allocated cluster. File slack contains **orphaned data** from previously deleted files that occupied those sectors [Saferstein, Ch. 19].

#### Mathematical Example of Slack Space Allocation:
* Assume a Cluster size = **1024 Bytes** (composed of two 512-Byte sectors).
* A user saves a small text file of **100 Bytes**.
* **RAM Slack** = $512	ext{ Bytes (Sector 1)} - 100	ext{ Bytes (Data)} = \mathbf{412	ext{ Bytes}}$.
* **File Slack** = **512 Bytes (Sector 2)** (contains orphaned data from previously deleted files).
* **Total Slack Space** = $412 + 512 = \mathbf{924	ext{ Bytes}}$.

```
                              SLACK SPACE DISK CLUSTER ALLOCATION
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 CLUSTER 1 (1024 Bytes)                                 │
├────────────────────────────────────────────────────────┬───────────────────────────────┤
│                        SECTOR 1                        │           SECTOR 2            │
│                       (512 Bytes)                      │          (512 Bytes)          │
├──────────────────────────┬─────────────────────────────┼───────────────────────────────┤
│ ACTIVE DATA              │ RAM SLACK                   │ FILE SLACK                    │
│ (100 Bytes)              │ (412 Bytes - Zeros/RAM)     │ (512 Bytes - Orphaned Data)   │
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

---

### 4.6 File Recovery, File Carving, & Metadata

* **Unallocated Space:** Physical space on a storage drive that the Operating System marks as empty and available for writing new data. Deleted files reside in unallocated space until overwritten [Slide 29; Saferstein, Ch. 19].
* **File Carving (Salvaging):** The process of reassembling and recovering deleted files or fragments from unallocated space based strictly on file headers, footers, and structural magic numbers (without relying on file system tables) [Slide 29; Nelson et al., Ch. 8].
  * *Example File Headers:* JPEG = `FF D8 FF`, PDF = `%PDF`, PNG = `89 50 4E 47`.
* **Metadata Analysis:** Examining embedded file attributes—MAC times (Modified, Accessed, Created timestamps), author details, camera EXIF data, permissions, and file system records (e.g., NTFS Master File Table / MFT) [Slide 28].

---

### 4.7 Order of Volatility (OOV) & Live RAM Acquisition

When responding to an active digital crime scene, evidence must be collected in sequence based on the **Order of Volatility (OOV)**—from the most temporary/volatile data to the most permanent [Nelson et al., Ch. 10]:

```
                            ORDER OF VOLATILITY (MOST TO LEAST VOLATILE)
                                                 │
  ┌──────────────────────────────────────────────┼──────────────────────────────────────────────┐
  ▼                                              ▼                                              ▼
1. CPU Cache & Registers ──► 2. System RAM (Memory) ──► 3. Network Sockets/Logs ──► 4. Hard Disk / SSD ──► 5. Archival Tapes
 (Nanoseconds)                (Volatile - Lost on Power-Off)  (Active Connections)        (Non-Volatile)         (Permanent)
```

1. **Registers and CPU Cache** (Nanoseconds)
2. **System RAM / Volatile Memory** (Microseconds; contains active passwords, chat logs, unencrypted keys)
3. **Network State & Sockets** (Active network connections, running processes)
4. **Secondary Storage (Hard Drives, SSDs, Flash Media)** (Persistent non-volatile data)
5. **Backup Tapes and Archival Media** (Permanent long-term storage)

---

## Section 5: Integrity, Preservation & Legal Admissibility

### 5.1 Chain of Custody & Preservation Protocols

* **Chain of Custody:** Sequential, unbroken written documentation detailing the seizure, custody, control, transfer, analysis, and disposition of digital evidence [Slide 28; Saferstein, Ch. 19].
* **Seizure Protocols:**
  * If a system is **powered off**, keep it powered off. Bag and tag all drives, cables, and power adapters in anti-static evidence bags [Nelson et al., Ch. 4].
  * If a system is **powered on**, photograph open windows on screen, perform a live RAM capture, and use write-blockers before shutdown [Slide 28].

---

### 5.2 Cryptographic Hashing for Integrity Verification

A **Cryptographic Hash** is a mathematical algorithm that converts an arbitrary input file or drive image into a fixed-length string of hexadecimal characters (a "digital fingerprint") [Nelson et al., Ch. 6].

#### Fundamental Properties:
* **Unique & One-Way:** Any change—even a single bit flip—completely alters the generated hash value (avalanche effect).
* **Self-Authentication:** Hash values generated during initial acquisition must match the hash values calculated during analysis and court presentation [Nelson et al., Ch. 6].
* **Standard Algorithms:**
  * **MD5 (Message Digest 5):** Produces a 128-bit hash value (32 hex characters).
  * **SHA-1 (Secure Hash Algorithm 1):** Produces a 160-bit hash value (40 hex characters).
  * **SHA-256:** Produces a 256-bit hash value.

---

### 5.3 Legal Admissibility Standards

* **Best Evidence Rule (FRE Rule 1001/1003):** To prove the contents of a file or photo, the court requires the original document. However, Federal Rules of Evidence state that a bit-stream printout or electronic duplicate shown to accurately reflect the data qualifies as an original [Saferstein, Ch. 19; Nelson et al., Ch. 4].
* **FRE Rule 902 (Self-Authentication):** Allows digital evidence to be self-authenticating if accompanied by a certified hash verification and examiner affidavit [Nelson et al., Ch. 4].
* **Indian Statutory Framework:**
  * **Section 65B of the Indian Evidence Act, 1872 (now Sec. 63 of BSA, 2023):** Mandates a signed **65B Certificate** accompanying any electronic record/printout to establish legal admissibility in court.
  * **Information Technology (IT) Act, 2000:** Governs cybercrime offenses, hacking (Sec. 66), identity theft (Sec. 66C), phishing (Sec. 66D), privacy violation (Sec. 66E), and cyberterrorism (Sec. 66F).

---

### 5.4 Specialized Digital Forensic Software Tools

| Forensic Tool | Primary Category | Key Features & Operational Capabilities |
| :--- | :--- | :--- |
| **FTK Imager** | Image Acquisition | Quick, forensically sound data preview, write-blocked bit-stream imaging (`.E01`, `.raw`), and hash verification [Slide 30]. |
| **Autopsy** | Analysis Suite | Open-source GUI digital forensics platform; keyword searching, hash set filtering, web artifact extraction, and deleted file recovery [Slide 30]. |
| **Wireshark** | Network Forensics | Deep packet analyzer; captures live network traffic, analyzes protocol headers, and tracks DDoS / intrusion packets [Slide 30]. |
| **WinHex** | Hex Editor | Low-level disk editor; allows raw sector viewing, manual file carving, hex editing, and slack space inspection [Slide 30]. |
| **EnCase** | Enterprise Suite | Comprehensive commercial suite; hardware write-blocking integration, `.E01` imaging, indexing, and court reporting [Nelson et al., Ch. 6]. |

---

## Section 6: Method-Selection & Case-Based Decision Scenarios

### Scenario 1: Social Media Cyber Hate Speech & Cyberbullying
* **Situation:** An individual posts hateful messages targeting a specific ethnic group on social media, sparking public outrage [Slide 9, 31].
* **Investigation Workflow:**
  1. **Perpetrator Identification:** Extract IP addresses from post headers, query ISP subscriber logs, and analyze social media account metadata (creation date, linked phone numbers) [Slide 31].
  2. **Evidence Extraction:** Preserve social media posts, direct messages, user profiles, comments, and uploaded media using forensically validated web capture tools [Slide 31].
  3. **Integrity Preservation:** Calculate cryptographic hashes (MD5/SHA-256) of captured web pages/data immediately, maintain write-blocked copies, and secure a Section 65B Certificate [Slide 31].
  4. **Recovery of Deleted Messages:** Analyze database files (e.g., SQLite databases on mobile devices), unallocated space, or server backups using tools like Autopsy, FTK Imager, or Cellebrite [Slide 31].

### Scenario 2: Unauthorized Hacking & Corporate Data Exfiltration
* **Situation:** A corporate network suffers a security breach where sensitive trade secrets are stolen [Slide 8, 16].
* **Investigation Workflow:** Perform live RAM capture to preserve active network sockets and running processes; acquire bit-stream images of server drives; analyze firewall/IDS log files; conduct keyword searches for trade secret file headers; verify file integrity with hash comparison against master known file filters (NSRL) [Slide 16–17, 28–30].

---

## Section 7: Practice Questions & Model Answers for Term-End Exams

### 7.1 Short-Answer Questions (3–5 Marks)

#### Question 1 (4 Marks):
**Distinguish between Cyber-enabled crimes and Cyber-dependent crimes with two examples each.**

##### Model Answer:
1. **Cyber-Dependent Crimes (2 Marks):** Crimes that can only be committed using computers or digital technologies as both the tool and target. They cannot exist without digital networks.
   * *Examples:* Hacking into a corporate server, spreading a self-replicating computer worm, or executing a DDoS attack [Slide 2].
2. **Cyber-Enabled Crimes (2 Marks):** Traditional crimes that take place in the physical world but are facilitated, scaled, or accelerated by the use of computers or the internet.
   * *Examples:* Online banking fraud, cyberstalking via social media, or selling pirated software online [Slide 1].

---

#### Question 2 (5 Marks):
**Explain the defining differences between a Computer Virus and a Computer Worm.**

##### Model Answer:
* **Host Requirement (2 Marks):** A computer virus requires an existing host file or executable program (`.exe`, `.docm`) to attach itself to. In contrast, a computer worm is a standalone program that does not require a host file [Slide 18–19].
* **Propagation & Human Action (2 Marks):** A virus relies on human action for activation and spreading (e.g., opening an infected email attachment). A worm requires no human intervention; it automatically self-replicates and spreads across network connections [Slide 19–20].
* **Impact (1 Mark):** Viruses focus primarily on corrupting or deleting target files. Worms focus on consuming network bandwidth and memory, causing severe system slowdowns [Slide 18–19].

---

### 7.2 Long-Answer / Essay Questions (7–10 Marks)

#### Question 3 (10 Marks):
**Explain why prosecuting cybercrime is challenging, and briefly define the following terms: (a) Catfishing, (b) Spamming, (c) Cyberstalking, and (d) Phishing.**

##### Model Answer:

**Part 1: Challenges in Prosecuting Cybercrime (6 Marks):**
1. **Jurisdictional & Transnational Hurdles:** Cybercrimes cross international borders instantaneously, creating complex legal conflicts between nations with differing extradition treaties and laws [Slide 3, 15].
2. **Anonymity & Spoofing:** Attackers hide behind VPNs, TOR networks, proxy servers, and spoofed IP/email addresses, making attribution extremely difficult [Slide 3, 23].
3. **Volatile & Intangible Evidence:** Digital evidence can be deleted, modified, or overwritten within milliseconds. Failing to preserve live RAM or slack space can destroy crucial evidence [Slide 28; Saferstein, Ch. 19].
4. **Lack of Physical Evidence:** Unlike conventional crime scenes, there are no physical bloodstains or footprints—only intangible digital bits that require advanced technical tools to extract [Slide 2, 28].
5. **Encryption & Anti-Forensics:** Threat actors utilize strong end-to-end encryption, steganography, and log-cleaning tools to obfuscate data [Slide 17, 29].
6. **Complexity & Technical Knowledge Gap:** Investigating cybercrime requires specialized technical skills that many traditional law enforcement agencies lack [Slide 15].

**Part 2: Definition of Specific Threat Typologies (4 Marks):**
* **(a) Catfishing (1 Mark):** The practice of creating a fake online persona or profile to deceive victims into deceptive emotional or romantic relationships, often for financial extortion or harassment [Slide 24].
* **(b) Spamming (1 Mark):** Sending unsolicited bulk electronic messages indiscriminately to large numbers of recipients, primarily for commercial advertising or distributing malware links [Slide 22].
* **(c) Cyberstalking (1 Mark):** Repeatedly using online platforms, email, or chat rooms to monitor, threaten, or harass a specific individual, engendering fear and emotional distress [Slide 25].
* **(d) Phishing (1 Mark):** Online fraud where attackers pose as legitimate entities (banks, government agencies) using spoofed emails or fake websites to trick victims into revealing sensitive credentials or PII [Slide 23].

---

## Section 8: Glossary of Digital Forensic & Cybercrime Terms

* **Anti-Forensics:** Techniques and tools used by attackers to manipulate, erase, or obfuscate digital evidence to impede forensic analysis [Slide 17].
* **Bit-Stream Image:** An exact sector-by-sector, bit-by-bit duplicate of a physical storage drive [Slide 28].
* **Cluster:** The smallest logical allocation unit of disk space assigned by a file system [Saferstein, Ch. 19].
* **Doxing:** Publishing private personal or identifying information about an individual online with malicious intent [Slide 10].
* **File Carving:** Reassembling deleted files from unallocated space based on file headers and footers [Slide 29].
* **Logic Bomb:** Dormant malicious code that executes a destructive payload when specific conditions are met [Slide 21].
* **Phishing:** Social engineering fraud aimed at harvesting user credentials via fake websites/emails [Slide 23].
* **Slack Space:** Unused space in a cluster between the end of a saved file and the end of the cluster (includes RAM slack and File slack) [Slide 29].
* **Super Zapping:** Bypassing standard system security controls using utility software to modify protected data [Slide 21].
* **Trojan Horse:** Malware disguised as safe or legitimate software to trick users into installation [Slide 20].
* **Unallocated Space:** Physical disk space marked by the OS as available for writing new data [Slide 29].
* **Write-Blocker:** A hardware or software tool that prevents write commands from reaching an evidence drive during acquisition [Nelson et al., Ch. 3].

---

## Section 9: Quick Revision Sheet & Comparison Matrices

### 9.1 Quick Threat & Malware Summary

| Threat Type | Key Defining Feature | Primary Trigger / Delivery |
| :--- | :--- | :--- |
| **Virus** | Requires a host file; alters existing programs. | Human execution of infected file [Slide 18]. |
| **Worm** | Standalone; self-replicates across networks. | Automatic network propagation [Slide 19]. |
| **Trojan Horse** | Disguised as legitimate software. | Social engineering trickery [Slide 20]. |
| **Logic Bomb** | Dormant code inside software. | Specific date, time, or event trigger [Slide 21]. |
| **Trap Door** | Hidden backdoor in source code. | Secret developer/attacker access point [Slide 21]. |
| **Super Zapping** | Bypasses system security controls. | Privilege override utility tools [Slide 21]. |

---

## Section 10: Syllabus-to-Source Coverage Matrix & Completeness Audit

| Course Policy Syllabus Topic | PPT / Source Reference | Coverage Status | Section in Notes |
| :--- | :--- | :--- | :--- |
| **Definition & Types of Computer Crimes** | `IFS PPT Unit 6_2025.pptx` (Slide 1–2) | Complete | Section 1.1 |
| **Distinction: Computer vs. Conventional Crimes** | `IFS PPT Unit 6_2025.pptx` (Slide 2–3, 13–15) | Complete | Section 1.2 |
| **Reasons for Computer Crimes & CIA Triad** | `IFS PPT Unit 6_2025.pptx` (Slide 3–4, 12) | Complete | Section 1.3, 1.4 |
| **Security Breaches & Breach Lifecycle** | `IFS PPT Unit 6_2025.pptx` (Slide 5–6, 16–17) | Complete | Section 2.1 |
| **Viruses, Worms, Trojans, Trap Doors, Super Zapping, Logic Bombs** | `IFS PPT Unit 6_2025.pptx` (Slide 18–21) | Complete | Section 2.2 |
| **Hacking, IPR Crimes, Computer Terrorism, Hate Speech** | `IFS PPT Unit 6_2025.pptx` (Slide 7–11, 22) | Complete | Section 3.1 |
| **Spamming, Phishing, Catfishing, Cyberstalking** | `IFS PPT Unit 6_2025.pptx` (Slide 22–27) | Complete | Section 3.2 |
| **Digital Evidence Extraction & Forensics Workflow** | `IFS PPT Unit 6_2025.pptx` (Slide 27–30); Saferstein Ch. 19 | Complete | Section 4.1 |
| **HDD Geometry, Visible vs. Latent Data** | Saferstein Ch. 19; Nelson et al. Ch. 5 | Complete | Section 4.2, 4.3 |
| **Bit-Stream Imaging & Write-Blockers** | `IFS PPT Unit 6_2025.pptx` (Slide 28); Nelson et al. Ch. 3 | Complete | Section 4.4 |
| **Slack Space Analysis (RAM & File Slack)** | `IFS PPT Unit 6_2025.pptx` (Slide 29); Saferstein Ch. 19 | Complete | Section 4.5 |
| **File Recovery, Carving, Metadata, OOV** | `IFS PPT Unit 6_2025.pptx` (Slide 28–29); Nelson et al. Ch. 8, 10 | Complete | Section 4.6, 4.7 |
| **Integrity, Preservation, Cryptographic Hashing (MD5/SHA-1)** | `IFS PPT Unit 6_2025.pptx` (Slide 28); Nelson et al. Ch. 6 | Complete | Section 5.1, 5.2 |
| **Legal Admissibility (FRE 902/1001, Sec 65B IEA / IT Act)** | Saferstein Ch. 19; IT Act 2000 | Complete | Section 5.3 |
| **Forensic Software Tools (FTK Imager, Autopsy, Wireshark, WinHex)** | `IFS PPT Unit 6_2025.pptx` (Slide 30) | Complete | Section 5.4 |
