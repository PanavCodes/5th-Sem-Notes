# Unit 5: Instrumental Methods in Forensics — Comprehensive Study Notes (Updated)

This comprehensive, exam-oriented study-notes document provides exhaustive, textbook-grade coverage of **Unit 5: Instrumental Methods in Forensics** as outlined in the NMIMS Course Policy (`IFS Course policy 2026-27 (1).docx`). It is built directly from the primary lecture slide decks **`Unit 5_Forensic_Spectroscopy_2025 (1).pptx`** and **`Spectroscopic Techniques in Forensic Science_2025.pptx`**, enriched with YouTube lecture transcripts (`UV - Visible Spectroscopy`, `Learn Forensics: Mass Spectrometry`, `ATOMIC ABSORPTION SPECTROSCOPY! @afrs`, `Atomic Emission Spectroscopy`, `IR Spectroscopy and Mass Spectrometry`), and grounded in authoritative reference texts including Richard Saferstein's *Criminalistics: An Introduction to Forensic Science*, Richard Li's *Forensic Biology*, Michael J. Allen's *Foundations of Forensic Document Analysis*, Gautam Biswas's *Review of Forensic Medicine and Toxicology*, and B.R. Sharma's *Forensic Science in Criminal Investigation and Trials*.

---

## Course Policy & Learning Objective Alignment

* **Course Outcome (CO):** **CO4** — Utilize instrumental and photographic methods to analyze and document forensic evidence.
* **Bloom's Taxonomy Level:** **K3 (Apply)** — Demonstration of theoretical comprehension, operational selection, data interpretation, and practical application of analytical instruments and imaging protocols to physical evidence.

---

## Section 1: Chromatographic Methods

### 1.1 Fundamental Principles of Chromatography
Chromatography (derived from Greek *chroma* = color, *graphein* = to write) is a physical separation technique in which the components of a complex mixture are distributed between two immiscible phases: a **stationary phase** (a solid bed or a liquid film coated on a solid support) and a **mobile phase** (a liquid solvent or carrier gas) that flows over or through the stationary phase [Saferstein, Ch. 12; Allen, Ch. 7].

```
                          Chromatographic Separation
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
    STATIONARY PHASE                                      MOBILE PHASE
    (Solid bed or liquid film)                            (Gas or Liquid solvent)
            │                                                     │
            └──────────────────────────┬──────────────────────────┘
                                       ▼
                       DIFFERENTIAL RETENTION / AFFINITY
      • High affinity for Stationary Phase ──► Retarded (Elutes Later)
      • High affinity for Mobile Phase     ──► Unretarded (Elutes Earlier)
```

#### Separation Mechanisms:
1. **Adsorption Chromatography:** Based on solute competition for active surface sites on a solid stationary phase (e.g., silica gel or alumina). Molecules with stronger polar or hydrogen-bonding interactions bind tightly and migrate slowly.
2. **Partition Chromatography:** Based on the differential solubility and equilibrium distribution of a solute between two immiscible liquid phases (or a liquid stationary phase coated on a solid matrix and a liquid/gas mobile phase). Governed by the partition coefficient:
   $$K = \frac{C_{\text{stationary}}}{C_{\text{mobile}}}$$
   where $C_{\text{stationary}}$ is the equilibrium concentration of analyte in the stationary phase and $C_{\text{mobile}}$ is the concentration in the mobile phase.
3. **Ion-Exchange & Size-Exclusion Modes:** Ion-exchange relies on electrostatic attraction between charged analyte ions and fixed ionic groups on a resin bed; size-exclusion (gel filtration) separates macromolecular species based on molecular size and steric exclusion from porous stationary beads [Li, Ch. 9].

---

### 1.2 Thin Layer Chromatography (TLC)

#### Principles & Mechanisms:
TLC is a planar form of liquid-solid adsorption or liquid-liquid partition chromatography. The stationary phase consists of a thin, uniform layer (typically $0.25\text{ mm}$ thick) of adsorbent (silica gel, alumina, or cellulose) bound to a glass, aluminum, or plastic plate. The mobile phase is an organic solvent mixture that migrates up the plate by **capillary action** [Saferstein, Ch. 12].

#### Working Stages:
1. **Sample Spotting:** Micro-liter volumes of questioned and known reference solutions are applied as tiny spots along a baseline origin $1–2\text{ cm}$ from the bottom edge using glass capillaries.
2. **Development:** The spotted plate is placed vertically inside a sealed, vapor-saturated developing chamber containing the solvent mixture below the origin line.
3. **Elution:** Solvents travel upward; analytes partition continuously between the moving solvent and silica adsorbent.
4. **Drying & Visualization:** The plate is removed, the solvent front is immediately marked, and the plate is dried.

#### Quantitative Parameter — Retention Factor ($R_f$):
The relative migration distance of a substance is expressed as the retention factor ($R_f$), defined as:
$$R_f = \frac{\text{Distance traveled by solute spot from origin}}{\text{Distance traveled by solvent front from origin}} = \frac{d_{\text{solute}}}{d_{\text{solvent}}}$$

*Assumptions & Constraints:* $R_f$ values range between $0.00$ and $1.00$. $R_f$ is a relative physical constant under strictly controlled temperature, chamber saturation, stationary phase activity, and solvent composition. It provides **preliminary screening (Category C)** data, not absolute structural proof [Saferstein, Ch. 12].

##### Worked Example 1 (TLC $R_f$ Calculation):
*Problem:* A questioned black ballpoint ink spot extracted from a forged check is analyzed by TLC alongside a known reference ink. The solvent front travels $8.00\text{ cm}$ from the origin line. Component Spot A moves $3.60\text{ cm}$, Spot B moves $5.20\text{ cm}$, and reference Spot R moves $3.60\text{ cm}$. Calculate the $R_f$ values and evaluate the match.
*Calculation:*
1. For Spot A: 
   $$R_{f, \text{A}} = \frac{3.60\text{ cm}}{8.00\text{ cm}} = 0.450$$
2. For Spot B: 
   $$R_{f, \text{B}} = \frac{5.20\text{ cm}}{8.00\text{ cm}} = 0.650$$
3. For Reference Spot R: 
   $$R_{f, \text{R}} = \frac{3.60\text{ cm}}{8.00\text{ cm}} = 0.450$$
*Conclusion:* Spot A matches Reference Spot R ($R_f = 0.450$), indicating identical chromatographic mobility under test conditions. Spot B represents a distinct dye component ($R_f = 0.650$).

#### Visualization Techniques:
* **Shortwave / Longwave UV Light ($254\text{ nm} / 365\text{ nm}$):** Visualizes UV-fluorescent dyes or quenches fluorescent indicators ($\text{Zn}_2\text{SiO}_4:\text{Mn}$) embedded in $F_{254}$ silica plates (appearing as dark spots on a glowing green background).
* **Chemical Reagents:**
  * *Iodine Vapor:* Sublimes and reversibly dissolves in lipophilic/unsaturated organic spots, forming yellow-brown bands.
  * *Ninhydrin Spray:* Reacts with primary amino acids and amphetamine-type drugs to form Ruhemann's purple spots.
  * *Acidified Potassium Permanganate / Dragendorff's Reagent:* Visualizes alkaloids and basic synthetic drugs.

#### Subsections for TLC:
* **Instrumentation:** Minimal hardware required—glass tanks, silica $G/F_{254}$ plates, micro-capillaries, UV viewing cabinet, spray chamber.
* **Outputs:** Planar chromatogram displaying discrete colored/fluorescent spots and calculated $R_f$ values.
* **Forensic Applications:** Rapid screening of seized drug powders (heroine, cocaine, cannabis extracts), ballpoint/gel pen ink dyes, explosives residues, and toxicological organophosphate pesticides [Allen, Ch. 7].
* **Advantages:** Low cost, high sample throughput (multiple samples spotted on one plate), minimal solvent consumption, non-destructive optical visualization allowing spot recovery.
* **Limitations & Interferences:** Low chromatographic resolution (broad spots), susceptible to chamber edge effects and temperature fluctuations, overlapping $R_f$ values among analogues, non-conclusive alone.
* **Sample Restrictions & Destructive Effects:** Sample must be soluble in volatile organic solvents. Non-destructive if UV viewed; destructive if chemically sprayed with corrosive stains.

---

### 1.3 Gas Chromatography (GC)

#### Principles & Components:
Gas chromatography is a dynamic separation technique where the mobile phase is an inert carrier gas (Helium, Nitrogen, or Hydrogen) and the stationary phase is a microscopic layer of viscous liquid or polymer coated on the inner wall of a narrow capillary column (Gas-Liquid Chromatography, GLC) or solid adsorbent particles packed inside a column (Gas-Solid Chromatography, GSC) [Saferstein, Ch. 12; Evans-Nguyen, Ch. 1]. Separation depends on analyte volatility (boiling point) and thermodynamic partition between the moving gas and stationary liquid film inside a temperature-programmed oven.

```
                           Gas Chromatograph (GC)
                                       │
  ┌──────────────┐    ┌────────────────┴──────────────┐    ┌──────────────┐
  │ Carrier Gas  │───►│ Heated Injector Port          │───►│ Column Oven  │
  │ (He / N2 / H2)    │ (Split / Splitless / Headspace)    │ (Capillary)  │
  └──────────────┘    └───────────────────────────────┘    └──────┬───────┘
                                                                  │
  ┌──────────────┐    ┌───────────────────────────────┐           │
  │ Data System  │◄───│ Detector (FID / ECD / MS)     │◄──────────┘
  │ (Chromatogram)    │                               │
  └──────────────┘    └───────────────────────────────┘
```

#### Key Components & Operational Stages:
1. **Carrier Gas Supply:** High-purity gas ($>99.999\%$) regulated by mass flow controllers.
2. **Inlet System (Injector):**
   * *Split Injection:* High concentrations of analyte; a major portion ($1:20$ to $1:100$) of vaporized sample is vented, preventing column overload.
   * *Splitless Injection:* Trace-level analysis; the entire vaporized sample is swept onto the column (high sensitivity for accelerants and environmental toxins).
   * *Headspace Sampling (Static/Dynamic):* Essential for volatile ignitable liquid residues in fire debris or blood alcohol analysis. Sealed vials are heated to establish vapor-liquid equilibrium; gas phase is sampled without injecting non-volatile blood/debris matrices [Evans-Nguyen, Ch. 2, 3].
3. **Capillary Column & Oven:** Open tubular fused-silica capillary columns ($15–60\text{ m}$ length, $0.10–0.53\text{ mm}$ internal diameter) coated with stationary phases such as $100\%$ dimethylpolysiloxane (HP-1, non-polar) or $5\%$ phenyl-methylpolysiloxane (HP-5MS). Oven temperature is ramped dynamically (e.g., $40^\circ\text{C}$ to $300^\circ\text{C}$ at $10^\circ\text{C/min}$) to resolve complex mixtures.
4. **Detectors:**
   * *Flame Ionization Detector (FID):* Universal detector for hydrocarbons; sample is burned in a hydrogen-air flame, generating ions that create an electrical current proportional to carbon atom count. Highly linear, robust.
   * *Electron Capture Detector (ECD):* Specific for halogenated compounds (organochlorine pesticides, alkyl halides, explosives like PETN/RDX); uses a Radioactive $^{63}\text{Ni}$ beta emitter source to capture electrons, causing a current drop. Extremely sensitive ($\text{pg}$ level).
   * *Nitrogen-Phosphorus Detector (NPD):* Selective for nitrogen/phosphorus-containing drugs and organophosphates.

#### Chromatogram Parameters:
* **Retention Time ($t_R$):** Elapsed time from sample injection to maximum detector peak response.
* **Adjusted Retention Time ($t'_R$):** $t'_R = t_R - t_m$, where $t_m$ is the void time (elution of an unretained gas like methane).
* **Peak Area & Height:** Proportional to analyte mass/concentration; quantified via multi-point calibration curves.

#### Subsections for GC:
* **Outputs:** Retention-time chromatograms showing signal intensity (pA or mV) versus time (minutes).
* **Forensic Applications:** Blood alcohol concentration (BAC) determination via static headspace GC-FID, ignitable liquid residue (gasoline, kerosene, diesel) classification in fire debris [Evans-Nguyen, Ch. 3], arson accelerants, volatile poisons (cyanide, solvent sniffing), and seized drug purity analysis.
* **Advantages:** Exceptional separation power ($>100,000$ theoretical plates), high sensitivity ($\text{ng}$ to $\text{pg}$ detection limit), rapid analysis time ($10–30\text{ min}$), excellent quantitation precision.
* **Limitations & Restrictions:** **Strictly restricted to volatile and thermally stable compounds** (boiling points $<350–400^\circ\text{C}$). Thermolabile species (e.g., proteins, explosive salts, LSD, quaternary ammonium compounds) undergo thermal degradation inside the hot injector unless chemically derivatized (TMS/silylation).
* **Interferences & Destructive Effects:** Matrix interferences from pyrolyzed substrate materials (softwood, carpets, plastics) in arson samples [Evans-Nguyen, Ch. 3]; destructive to injected sample aliquot (combusted in FID).

---

### 1.4 High-Performance Liquid Chromatography (HPLC / LC)

#### Principles & Mechanisms:
HPLC is a high-resolution column liquid chromatography technique operating under elevated hydraulic pressures ($100–600\text{ bar} / 1500–8700\text{ psi}$). The mobile phase is a liquid solvent pumped through a stainless-steel column packed with tiny, highly uniform stationary-phase particles ($1.8–5\text{ }\mu\text{m}$ diameter) [Saferstein, Ch. 12; Evans-Nguyen, Ch. 1].

#### Separation Modes:
1. **Normal-Phase HPLC:** Polar stationary phase (silica gel, cyano) + non-polar mobile phase (hexane, methylene chloride). Retention increases with analyte polarity.
2. **Reversed-Phase HPLC (RP-HPLC — Standard Forensic Mode):** Non-polar stationary phase (octadecylsilane, $\text{C}_{18}$, or phenyl-bound silica) + polar mobile phase (mixtures of water/buffers with methanol or acetonitrile). Non-polar analytes bind strongly to the hydrophobic $\text{C}_{18}$ chains and elute later; polar compounds elute earlier. Isocratic or gradient elution (varying organic solvent ratio over time) is used.

```
                         Reversed-Phase HPLC (RP-HPLC)
                                       │
  ┌──────────────┐    ┌────────────────┴──────────────┐    ┌──────────────┐
  │ Solvent      │───►│ High-Pressure Dual Pumps      │───►│ Autosampler  │
  │ Reservoirs   │    │ (Isocratic / Gradient Mix)    │    │ Injector     │
  └──────────────┘    └───────────────────────────────┘    └──────┬───────┘
                                                                  │
  ┌──────────────┐    ┌───────────────────────────────┐           │
  │ Waste /      │◄───│ Detector (UV-Vis / PDA /      │◄──────────┤ C18 Column   │
  │ Mass Spec    │    │ Fluorescence / EC)            │           │ (Thermostated│
  └──────────────┘    └───────────────────────────────┘           └──────────────┘
```

#### Key Components:
1. **High-Pressure Reciprocating Pumps:** Deliver pulseless, precise solvent flow rates ($0.1–5.0\text{ mL/min}$).
2. **Autosampler / Rheodyne Injector:** Introduces fixed sample volumes ($1–50\text{ }\mu\text{L}$) into high-pressure flow without pressure drops.
3. **Guard Column & Analytical Column:** Protects expensive analytical columns from particulate matter and irreversibly bound impurities.
4. **Detectors:**
   * *Photodiode Array (PDA / DAD):* Acquires full UV-Vis absorption spectra ($190–800\text{ nm}$) continuously for every eluting peak, providing 3D data (time, wavelength, absorbance) [Evans-Nguyen, Ch. 1].
   * *Fluorescence Detector:* High sensitivity for naturally fluorescent analytes (LSD, aflatoxins, polycyclic aromatic hydrocarbons).
   * *Electrochemical Detector (ECD):* High selectivity for easily oxidized/reduced biological molecules (catecholamines, neurotransmitters).

#### Subsections for HPLC:
* **Outputs:** HPLC chromatograms exhibiting retention time ($t_R$), peak symmetry, and UV-Vis spectra via DAD.
* **Forensic Applications:** Thermolabile, polar, and high-molecular-weight analytes—thermolabile organic explosives (TNT, RDX, HMX, PETN), thermally unstable pharmaceuticals, illicit synthetic cannabinoids, plant toxins (strychnine, ricin, morphine), ink dye comparisons, and biological metabolites [Evans-Nguyen, Ch. 1].
* **Advantages:** Operates at **ambient temperatures** (ideal for heat-sensitive drugs/explosives without decomposition), versatile mobile-phase tuning, non-destructive to eluting analytes (allowing fraction collection).
* **Limitations:** Lower peak capacity than capillary GC, higher operating solvent costs, sensitive to mobile-phase gas bubbles (requires online vacuum degassers).
* **Interferences & Sample Restrictions:** Solvents must be LC-grade and filtered ($0.22\text{ }\mu\text{m}$); samples must be entirely particulate-free and soluble in mobile phase.

---

### 1.5 Hyphenated Techniques: GC-MS and LC-MS/MS

#### Complementary Separation–Identification Architecture:
Hyphenated techniques couple high-efficiency physical separation instruments (GC or LC) directly to structural mass spectrometers (MS). The chromatograph serves as an online purification system that resolves complex mixtures into single components, while the mass spectrometer functions as a universal, highly specific detector that identifies each eluting peak via mass-to-charge ($m/z$) measurements [Saferstein, Ch. 12; Evans-Nguyen, Ch. 1].

#### Mass Spectrometry Ionization Interfaces:
* **GC-MS Interfaces (Gas Phase):**
  * *Electron Ionization (EI — "Hard" Ionization):* Energetic electrons ($70\text{ eV}$) emitted from a tungsten filament collide with vaporized sample molecules, knocking out an electron to form a radical cation molecular ion ($M^{+\bullet}$) [Evans-Nguyen, Ch. 1; CrashCourse Transcript]:
    $$\text{M} + e^- (70\text{ eV}) \longrightarrow \text{M}^{+\bullet} + 2e^-$$
    Excess vibrational energy causes reproducible fragmentation into a characteristic pattern (molecular "fingerprint") searchable against spectral databases (NIST, Wiley, SWGDRUG).
  * *Chemical Ionization (CI — "Soft" Ionization):* Uses a reagent gas (methane, isobutane, ammonia) ionized by electrons to softly transfer a proton to the analyte [Evans-Nguyen, Ch. 1]:
    $$\text{CH}_4 + e^- \longrightarrow \text{CH}_4^{+\bullet} + 2e^-, \quad \text{CH}_4^{+\bullet} + \text{CH}_4 \longrightarrow \text{CH}_5^+ + \text{CH}_3^\bullet$$
    $$\text{CH}_5^+ + \text{M} \longrightarrow [\text{M} + \text{H}]^+ + \text{CH}_4$$
    Yields strong protonated pseudo-molecular ions $[\text{M}+\text{H}]^+$ with minimal fragmentation, confirming molecular weight.
* **LC-MS Interfaces (Atmospheric Pressure Ionization, API):**
  * *Electrospray Ionization (ESI):* Liquid eluent passes through a heated stainless-steel capillary held at high DC voltage ($3–5\text{ kV}$). Aerosol charged droplets evaporate under nitrogen nebulizing gas; Coulombic repulsion causes "Coulomb explosions," releasing gas-phase pseudo-molecular ions ($[\text{M}+\text{H}]^+$ in positive mode, $[\text{M}-\text{H}]^-$ in negative mode) without thermal decomposition [Evans-Nguyen, Ch. 1; Li, Ch. 11].
  * *Atmospheric Pressure Chemical Ionization (APCI):* Corona discharge needle ionizes evaporated solvent vapors, which chemically ionize non-polar/moderately polar analytes [Evans-Nguyen, Ch. 1].

#### Comparison: GC-MS vs. LC-MS/MS

| Parameter | GC-MS | LC-MS / LC-MS/MS |
| :--- | :--- | :--- |
| **Analyte Compatibility** | Volatile, thermally stable, low-molecular-weight ($<600\text{ Da}$) compounds [Evans-Nguyen, Ch. 1]. | Non-volatile, polar, thermolabile, high-molecular-weight ($>100\text{ kDa}$) species [Evans-Nguyen, Ch. 1]. |
| **Sample Derivatization** | Frequently required for polar species (OH, NH, COOH groups) to increase volatility. | Rarely required; liquid samples analyzed directly. |
| **Ionization Mode** | Hard EI ($70\text{ eV}$) or Soft CI at high vacuum. | Soft API (ESI or APCI) at atmospheric pressure. |
| **Fragmentation Output** | Rich EI fragmentation spectra; highly reproducible; extensive commercial library matching (NIST/SWGDRUG) [Evans-Nguyen, Ch. 1]. | Minimal in ESI source; requires Tandem MS (MS/MS with CID collision cell) to induce structural fragmentation [Evans-Nguyen, Ch. 1]. |
| **Primary Forensic Uses** | Seized drug powders, accelerants in fire debris, volatile toxicology, explosives (TNT, RDX) [Evans-Nguyen, Ch. 1]. | Targeted urine/blood toxicological screening, biomolecules, thermolabile designer drugs, rodenticides, peptides [Li, Ch. 11]. |

---

### 1.6 Corrected Forensic Method-Selection Logic

The selection of chromatographic and analytical techniques must follow a rigorous, objective decision logic based on analytical goals and chemical properties.

> **CRITICAL CORRECTION (TLC Scope):** Preliminary slide schematics incorrectly suggested that TLC is restricted to volatile samples. **This is scientifically false.** TLC operates at ambient room temperature and is widely used for non-volatile dyes, solid drug powders, and non-volatile inks. GC requires volatility; TLC, HPLC, and LC-MS handle non-volatile and thermolabile analytes.

```
                          Forensic Method-Selection Logic
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
IS THE ANALYTE VOLATILE & THERMOSTABLE?                IS THE ANALYTE NON-VOLATILE / THERMOLABILE?
        │                                                                 │
  ┌─────┴─────┐                                                     ┌─────┴─────┐
  ▼           ▼                                                     ▼           ▼
GAS PHASE   LIQUID/SOLID                                        POLAR/LARGE   DYES/INKS
  │           │                                                     │           │
  ▼           ▼                                                     ▼           ▼
GC-FID     GC-MS (EI)                                            LC-MS/MS     TLC / RP-HPLC
(Screening) (Confirmatory)                                       (Confirmatory) (Screening/Prep)
```

#### Structured Method-Selection Criteria:
1. **Analytical Objective:**
   * *Screening / Preliminary (Category C/B):* TLC, GC-FID, UV-Vis. Fast, inexpensive, eliminates non-matches.
   * *Confirmatory / Definitive (Category A):* GC-MS, LC-MS/MS, FTIR, Raman. Provides structural identification meeting SWGDRUG court standards.
2. **Analyte Volatility & Thermal Stability:**
   * Volatile & thermostable $\longrightarrow$ GC or GC-MS.
   * Thermolabile or non-volatile $\longrightarrow$ TLC, HPLC, or LC-MS/MS.
3. **Sample Matrix & Compatibility:**
   * Complex biological fluids (blood, urine) $\longrightarrow$ Requires SPE/protein precipitation followed by LC-MS/MS or Headspace GC-FID (for alcohol).
   * Fire debris $\longrightarrow$ Passive headspace charcoal strip extraction followed by GC-MS [Evans-Nguyen, Ch. 2, 3].
4. **Required Identification Strength:**
   * Retention times and $R_f$ values match reference standards under identical conditions but are **not unique on their own**. Hyphenated mass spectrometry or vibrational spectroscopy is required for absolute legal confirmation.

---

## Section 2: Spectroscopic Methods

### 2.1 Electromagnetic Spectrum & Mathematical Foundations
Spectroscopy is the study of the interaction between electromagnetic radiation (EMR) and matter. EMR exhibits dual wave-particle properties [Saferstein, Ch. 10; NG Rao, Ch. 31].

```
                                  Electromagnetic Spectrum
  ◄──────────────────────────────────────────────────────────────────────────────────────────►
  Gamma Rays     X-Rays       Ultraviolet     Visible     Infrared      Microwaves    Radio Waves
  (10^-12 m)   (10^-10 m)     (200-400 nm)  (400-700 nm) (2.5-25 µm)    (10^-2 m)      (10^2 m)
  High Energy / High Frequency ───────────────────────────────► Low Energy / Low Frequency
```

#### Fundamental Mathematical Relationships:
1. **Wave Equation:**
   $$c = \lambda \nu \implies \nu = \frac{c}{\lambda}$$
   where $c$ is the speed of light in a vacuum ($2.998 \times 10^8\text{ m/s}$ or $3.00 \times 10^{10}\text{ cm/s}$), $\lambda$ is wavelength in meters ($\text{m}$) or nanometers ($\text{nm}$, $1\text{ nm} = 10^{-9}\text{ m}$), and $\nu$ is frequency in hertz ($\text{Hz}$ or $\text{s}^{-1}$).
2. **Planck's Quantum Equation:**
   $$E = h \nu = \frac{h c}{\lambda} = h c \tilde{\nu}$$
   where $E$ is photon energy in joules ($\text{J}$) or electron-volts ($\text{eV}$, $1\text{ eV} = 1.602 \times 10^{-19}\text{ J}$), $h$ is Planck's constant ($6.626 \times 10^{-34}\text{ J}\cdot\text{s}$), and $\tilde{\nu}$ is wavenumber in $\text{cm}^{-1}$.
3. **Wavenumber Definition:**
   $$\tilde{\nu} = \frac{1}{\lambda\text{ (in cm)}} = \frac{10^4}{\lambda\text{ (in }\mu\text{m)}} = \frac{10^7}{\lambda\text{ (in nm)}}$$
4. **Beer–Lambert Law (Quantitative Foundation):**
   When monochromatic light passes through a homogeneous absorbing medium, the decrease in light intensity is proportional to path length and concentration [Saferstein, Ch. 12; NG Rao, Ch. 31]:
   $$A = -\log_{10}(T) = -\log_{10}\left(\frac{I}{I_0}\right) = \epsilon b c$$
   *Symbols & Units:*
   * $A$: Absorbance (unitless optical density).
   * $T$: Transmittance ($I / I_0$, ratio of transmitted light $I$ to incident light $I_0$).
   * $\epsilon$: Molar absorptivity (extinction coefficient, $\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$).
   * $b$ (or $l$): Sample path length ($\text{cm}$, standard cuvette $b = 1.00\text{ cm}$).
   * $c$: Analyte concentration ($\text{mol}\cdot\text{L}^{-1}$ or $\text{M}$).

*Assumptions & Limitations of Beer–Lambert Law:* Valid only for dilute solutions ($c \le 0.01\text{ M}$), monochromatic radiation, non-scattering media, and in the absence of solute-solute association, dissociation, or chemical reaction.

##### Worked Example 2 (EMR Wavelength, Frequency, Energy, Wavenumber Conversion):
*Problem:* An infrared absorption band for a functional group occurs at a wavelength $\lambda = 2.50\text{ }\mu\text{m}$. Calculate its wavenumber ($\tilde{\nu}$ in $\text{cm}^{-1}$), frequency ($\nu$ in $\text{Hz}$), and photon energy ($E$ in Joules).
*Calculation:*
1. Convert wavelength to $\text{cm}$ and $\text{m}$:
   $$\lambda = 2.50\text{ }\mu\text{m} = 2.50 \times 10^{-4}\text{ cm} = 2.50 \times 10^{-6}\text{ m}$$
2. Wavenumber ($\tilde{\nu}$):
   $$\tilde{\nu} = \frac{1}{2.50 \times 10^{-4}\text{ cm}} = 4000\text{ cm}^{-1}$$
3. Frequency ($\nu$):
   $$\nu = \frac{c}{\lambda} = \frac{3.00 \times 10^8\text{ m/s}}{2.50 \times 10^{-6}\text{ m}} = 1.20 \times 10^{14}\text{ s}^{-1}\text{ (Hz)}$$
4. Energy ($E$):
   $$E = h \nu = (6.626 \times 10^{-34}\text{ J}\cdot\text{s}) \times (1.20 \times 10^{14}\text{ s}^{-1}) = 7.95 \times 10^{-20}\text{ J}$$

##### Worked Example 3 (Beer–Lambert Law Concentration Calculation):
*Problem:* A solution of codeine in $0.1\text{ M HCl}$ placed in a $1.00\text{ cm}$ cuvette exhibits a percent transmittance $\%T = 25.0\%$ at $\lambda_{\text{max}} = 284\text{ nm}$. The molar absorptivity $\epsilon$ of codeine at $284\text{ nm}$ is $1.55 \times 10^3\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$. Calculate the molar concentration of codeine.
*Calculation:*
1. Calculate Transmittance ($T$) and Absorbance ($A$):
   $$T = \frac{25.0}{100} = 0.250$$
   $$A = -\log_{10}(0.250) = \log_{10}(4.00) = 0.6021$$
2. Apply Beer–Lambert Law ($A = \epsilon b c$):
   $$c = \frac{A}{\epsilon b} = \frac{0.6021}{(1.55 \times 10^3\text{ L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}) \times (1.00\text{ cm})} = 3.88 \times 10^{-4}\text{ mol/L}$$
*Result:* Codeine concentration is $3.88 \times 10^{-4}\text{ M}$ ($0.116\text{ g/L}$).

---

### 2.2 UV-Visible Spectroscopy

#### Principle & Molecular Transitions:
UV-Vis spectroscopy ($190–800\text{ nm}$) measures the absorption of ultraviolet and visible photons that induce **outer-shell electronic transitions** from bonding/non-bonding ground-state orbitals ($\pi, n$) to higher-energy antibonding molecular orbitals ($\pi^*$) [Saferstein, Ch. 12; Vidya-mitra Transcript].

```
                     UV-Vis Electronic Transitions
         Energy
           │                  ┌───────────┐
           │                  │  π* (Anti-│
           │                  │   bonding)│
           │                  └─────┬─────┘
           │             π ──► π*   │   n ──► π*
           │            (Conjugated)│  (Heteroatoms: O, N, S)
           │                  ┌─────┴─────┐
           │                  │ n / π     │
           │                  │ (Ground)  │
           │                  └───────────┘
           └───────────────────────────────────►
```

#### Structural Concepts:
* **Chromophore:** An unsaturated functional group containing $\pi$ electrons capable of absorbing UV-Vis light (e.g., $\text{C=C}$, $\text{C=O}$, $\text{N=N}$, aromatic rings) [Saferstein, Ch. 12].
* **Auxochrome:** A saturated functional group with non-bonding unshared pairs of electrons (e.g., $-\text{OH}$, $-\text{NH}_2$, $-\text{Cl}$) that, when attached to a chromophore, modifies both the wavelength and intensity of absorption.
* **Spectral Shifts:**
  * *Bathochromic Shift (Red Shift):* Shift of $\lambda_{\text{max}}$ to longer wavelengths (lower energy) due to conjugation or solvent effects.
  * *Hypsochromic Shift (Blue Shift):* Shift of $\lambda_{\text{max}}$ to shorter wavelengths (higher energy).
  * *Hyperchromic Effect:* Increase in absorption intensity ($\epsilon$).
  * *Hypochromic Effect:* Decrease in absorption intensity ($\epsilon$).

#### Instrumentation & Schematic:
UV-Vis spectrophotometers utilize a Deuterium arc lamp (UV region $190–380\text{ nm}$) and a Tungsten-halogen lamp (Visible region $380–800\text{ nm}$), a monochromator (diffraction grating), quartz/fused silica cuvettes ($1.0\text{ cm}$ path length; glass absorbs UV $<320\text{ nm}$), and a Photomultiplier Tube (PMT) or Photodiode Array (PDA) detector [Applied Forensic Video Transcript; Evans-Nguyen, Ch. 1].

```
                       UV-Vis Spectrophotometer
                                  │
  ┌──────────────┐    ┌───────────┴──┐    ┌──────────────┐    ┌──────────────┐
  │ Light Source │───►│ Monochro-    │───►│ Beam Splitter│───►│ Sample Cell  │
  │ (D2 / W)     │    │ mator        │    │              │    │ (Quartz)     │
  └──────────────┘    └──────────────┘    └──────┬───────┘    └──────┬───────┘
                                                 │                   │
                                                 ▼                   ▼
                                          ┌──────────────┐    ┌──────────────┐
                                          │ Reference    │    │ Photodetector│
                                          │ Cell (Blank) │───►│ (PMT / PDA)  │
                                          └──────────────┘    └──────────────┘
```

#### Subsections for UV-Vis:
* **Outputs:** Absorption spectrum plotting Absorbance ($A$) versus Wavelength ($\lambda$ in $\text{nm}$), displaying characteristic $\lambda_{\text{max}}$ absorption bands.
* **Forensic Applications:**
  1. *Drug Screening:* Qualitative confirmation of drugs of abuse based on reported $\lambda_{\text{max}}$ (e.g., Cocaine at $233\text{ nm}$ in $0.2\text{ N H}_2\text{SO}_4$, Codeine at $284\text{ nm}$, MDMA at $286\text{ nm}$, Heroin at $278\text{ nm}$) [Vidya-mitra Transcript; Saferstein, Ch. 12].
  2. *Breath Alcohol Determination:* Quantitative estimation of ethanol via reaction with acidic potassium dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$, orange), which is reduced to green chromium ions ($\text{Cr}^{3+}$); measured by absorbance drop at $440\text{ nm}$ [Vidya-mitra Transcript].
  3. *Bloodstain Aging:* Enzymatic activity ratio determinations (LDH, SGOT, SGPT) measured at $340\text{ nm}$ [Vidya-mitra Transcript].
  4. *Inks, Dyes, & Fibers:* Comparison of dye absorption profiles in questioned document inks and textile fibers [Vidya-mitra Transcript].
* **Advantages:** Non-destructive to liquid solutions, fast, highly reproducible, precise for quantitative analysis via Beer's Law.
* **Limitations & Interferences:** Broad, featureless absorption bands; **presumptive / screening technique only (Category C)** because many isomeric or structurally related compounds share identical $\lambda_{\text{max}}$; cannot provide definitive identification without chromatography or MS.

---

### 2.3 Infrared (IR) & FTIR Spectroscopy

#### Principle & Molecular Vibrations:
IR spectroscopy ($4000–400\text{ cm}^{-1}$, mid-IR region) measures the absorption of infrared photons that excite **molecular vibrational transitions** (stretching and bending of covalent bonds) [Saferstein, Ch. 12; Allen, Ch. 7].

*Selection Rule for IR Activity:* A molecular vibration is IR-active **only if it causes a net change in the dipole moment ($\frac{d\mu}{dq} \neq 0$)** of the molecule [Slide 208]. Homonuclear diatomic molecules ($\text{N}_2, \text{O}_2, \text{H}_2$) have no dipole change and are IR-inactive; heteronuclear bonds ($\text{C=O}, \text{O–H}, \text{N–H}, \text{C–H}$) absorb intensely [Evans-Nguyen, Ch. 1].

Vibrational energy levels are quantized:
$$E_v = \left(v + \frac{1}{2}\right) h \nu_0$$
Vibrational modes include:
* *Stretching Vibrations:* Symmetric and asymmetric changes in interatomic distance along the bond axis.
* *Bending Vibrations:* In-plane (scissoring, rocking) and out-of-plane (wagging, twisting) changes in bond angle.

#### Spectral Regions:
1. **Functional Group Region ($4000–1500\text{ cm}^{-1}$):** Absorptions characteristic of specific functional groups:
   * $\text{O–H} / \text{N–H}$ stretch: $3600–3200\text{ cm}^{-1}$ (broad for $\text{O–H}$, sharp for $\text{N–H}$).
   * $\text{C–H}$ stretch: $3100–2850\text{ cm}^{-1}$ (alkenes/aromatics $>3000\text{ cm}^{-1}$, alkanes $<3000\text{ cm}^{-1}$).
   * $\text{C}\equiv\text{C} / \text{C}\equiv\text{N}$ stretch: $2260–2100\text{ cm}^{-1}$.
   * $\text{C=O}$ stretch: $1750–1650\text{ cm}^{-1}$ (intense sharp peak characteristic of ketones, esters, carboxylic acids).
   * $\text{C=C}$ aromatic stretch: $1600, 1500\text{ cm}^{-1}$.
2. **Fingerprint Region ($1500–400\text{ cm}^{-1}$):** Complex pattern of bending and skeletal vibrations unique to the entire molecular structure. A $100\%$ match in the fingerprint region between an unknown and a reference standard provides **definitive structural identification (Category A)** [Saferstein, Ch. 12; CrashCourse Transcript].

```
                     FTIR Spectrometer (Michelson Interferometer)
                                          │
  ┌──────────────┐    ┌───────────────────┴───────────────────┐    ┌──────────────┐
  │ Broadband IR │───►│ Michelson Interferometer              │───►│ Sample /     │
  │ Source       │    │ (Beam Splitter, Fixed/Moving Mirror)  │    │ ATR Crystal  │
  └──────────────┘    └───────────────────────────────────────┘    └──────┬───────┘
                                                                          │
  ┌──────────────┐    ┌───────────────────────────────────────┐           │
  │ FTIR Spectrum│◄───│ Fourier Transform Computer            │◄──────────┘
  │ (%T vs cm-1) │    │ (Decodes Interferogram Signal)        │
  └──────────────┘    └───────────────────────────────────────┘
```

#### Attenuated Total Reflectance (ATR-FTIR) Accessory:
Modern forensic FTIR utilizes ATR accessories. The solid or liquid sample is pressed against a high refractive index crystal (Diamond, Germanium, or Zinc Selenide, $n_1 \approx 2.4–4.0$). The IR beam undergoes total internal reflection inside the crystal, creating an **evanescent wave** that penetrates $0.5–2.0\text{ }\mu\text{m}$ into the sample surface. Absorbance occurs at characteristic frequencies before the beam returns to the detector [Evans-Nguyen, Ch. 1].

```
                            ATR-FTIR Sampling Mechanism
                                         │
                                  Anvil / Pressure Tower
                                  ┌──────────────────────┐
                                  │    Solid Sample      │
                                  └──────────────────────┘
  IR Beam From ────────────────► ════════════════════════ ───► Transmitted IR Beam
  Interferometer                  Diamond / Ge Crystal        To Detector
                                   (Evanescent Wave 1-2 µm)
```

#### Subsections for FTIR:
* **Outputs:** IR spectrum plotting Percent Transmittance ($\%T$) or Absorbance ($A$) versus Wavenumber ($\text{cm}^{-1}$). Peaks are displayed inverted when plotted as $\%T$.
* **Forensic Applications:** Definitive identification of seized illicit drug salts and free bases (e.g., differentiating cocaine $\text{HCl}$ from crack cocaine) [Saferstein, Ch. 12], synthetic opioids, explosives (RDX, TNT, PETN), vehicular paint chip binders, synthetic fibers, automotive plastics, questioned document toners, and breath alcohol analysis (Intoxilyzer 8000 operating at $3.39\text{ }\mu\text{m}$ and $3.48\text{ }\mu\text{m}$ $\text{C–H}$ stretches) [Saferstein, Ch. 12].
* **Advantages:** Category A confirmatory technique, non-destructive (with ATR), rapid ($<1\text{ minute}$ scan via FTIR interferograms), no KBr pellet pressing required for ATR.
* **Limitations & Sample Restrictions:** Water absorbs intensely in the IR region ($3300\text{ cm}^{-1}$ and $1640\text{ cm}^{-1}$) and destroys alkali halide optics; aqueous samples cannot be analyzed directly [Slide 208]. Mixtures produce overlapping spectra requiring prior chromatographic separation.

---

### 2.4 Atomic Absorption (AAS) & Atomic Emission (AES / ICP-AES) Spectroscopy

#### Atomic vs. Molecular Spectroscopy:

| Parameter | Atomic Spectroscopy (AAS / AES) | Molecular Spectroscopy (UV-Vis / FTIR) |
| :--- | :--- | :--- |
| **Species Examined** | Free, unbonded gaseous atoms [Slide 191; AFRS Transcript]. | Intact polyatomic molecules or ions [Slide 191]. |
| **Energy Transitions** | Electronic transitions between discrete atomic orbitals ($3s \to 3p$). | Combined electronic, vibrational, and rotational transitions. |
| **Spectral Appearance** | **Narrow, sharp line spectra** ($<0.01\text{ nm}$ bandwidth) [Slide 193]. | Broad absorption bands ($10–50\text{ nm}$ width). |
| **Primary Information** | Elemental composition and elemental quantification. | Chemical structure, functional groups, and molecular identity. |

#### Atomic Absorption Spectroscopy (AAS):
* **Principle:** Measures the absorption of resonance light by ground-state free gas-phase atoms. The ground-state atoms absorb light at element-specific wavelengths corresponding to their atomic excitation energies [Slide 196; AFRS Transcript].
* **Instrumentation & Schematic:**
  1. *Radiation Light Source:* **Hollow Cathode Lamp (HCL)** featuring a cylinder cathode constructed from the specific element being analyzed (e.g., Lead, Barium, Antimony). Emits extremely sharp line spectra unique to that element, avoiding spectral overlap [AFRS Transcript].
  2. *Atomizer:* Converts liquid/solid sample into free ground-state gas atoms.
     - *Flame Atomizer (FAAS):* Acetylene/air flame ($2100–2400^\circ\text{C}$). High throughput, moderate sensitivity ($\text{ppm}$).
     - *Graphite Furnace Atomizer (GFAAS / ETAAS):* Electrothermally heated graphite tube ($2000–3000^\circ\text{C}$). High sensitivity ($\text{ppb}$ level, micro-liter sample size) [AFRS Transcript; Biswas, Ch. 5].
  3. *Monochromator & Detector:* Isolates the specific resonance spectral line; Photomultiplier Tube (PMT) measures light attenuation [AFRS Transcript].

```
                     Atomic Absorption Spectrophotometer (AAS)
                                        │
  ┌──────────────┐    ┌─────────────────┴─┐    ┌──────────────┐    ┌──────────────┐
  │ Hollow Cath- │───►│ Atomizer          │───►│ Monochro-    │───►│ PMT Detector │
  │ ode Lamp     │    │ (Flame / Graphite)│    │ mator        │    │              │
  └──────────────┘    └───────────────────┘    └──────────────┘    └──────────────┘
```

#### Atomic Emission Spectroscopy (AES / ICP-AES):
* **Principle:** Measures the intensity of light emitted by thermally/electrically excited gas-phase atoms as they drop from excited electronic states back to lower/ground energy states [Slide 193; AES Transcript].
* **Excitation Sources:**
  * *Inductively Coupled Plasma (ICP):* High-energy argon plasma torch sustained by radiofrequency (RF) magnetic field ($6000–10,000\text{ K}$). Complete atomization, minimal chemical matrix interferences [AES Transcript; Saferstein, Ch. 10].
  * *Direct Current (DC) Arc / AC Spark:* Electrical discharges between carbon electrodes for solid alloys and metals [Saferstein, Ch. 10].

```
                 Inductively Coupled Plasma Atomic Emission (ICP-AES)
                                         │
  ┌──────────────┐    ┌──────────────────┴┐    ┌──────────────┐    ┌──────────────┐
  │ Sample Aerosol│───►│ Argon Plasma Torch│───►│ Monochro-    │───►│ Detector     │
  │ (Nebulizer)  │    │ (6,000-10,000 K)  │    │ mator / Grating   │ (PMT / CCD)  │
  └──────────────┘    └───────────────────┘    └──────────────┘    └──────────────┘
```

#### Subsections & Comparisons for AAS / AES:

| Parameter | Atomic Absorption (AAS) | Atomic Emission (ICP-AES) |
| :--- | :--- | :--- |
| **Measured Signal** | Attenuation (absorption) of light from HCL source [Slide 196]. | Intensity of light emitted by excited atoms in plasma/flame [Slide 193]. |
| **Light Source** | Element-specific Hollow Cathode Lamp (HCL) required [AFRS Transcript]. | No external lamp; sample plasma emits its own light [AES Transcript]. |
| **Multi-Element Ability**| Single-element sequential analysis per lamp. | **Simultaneous multi-element analysis** ($>70$ elements in one run) [AES Transcript]. |
| **Linear Dynamic Range**| Narrow ($10^2$ to $10^3$). | Wide ($10^5$ to $10^6$). |
| **Forensic Uses** | Gunshot Residue (GSR: $\text{Pb, Ba, Sb}$) [Biswas, Ch. 5], heavy metal toxicology (Arsenic, Mercury in hair/nails) [Slide 197]. | Trace element profiling of glass fragments, automotive paint layers, metal alloys, soil comparison [Slide 197; Saferstein, Ch. 10]. |
| **Destructive Effects**| **Destructive** (sample is atomized and consumed in flame/plasma) [Slide 194, 195]. | **Destructive** (sample atomized) [Slide 194, 195]. |

---

### 2.5 Mass Spectrometry (MS)

#### Principle & Ionization Mechanisms:
Mass spectrometry converts sample molecules into gas-phase ions, separates these ions based on their **mass-to-charge ratio ($m/z$)**, and records the relative abundance of each ion [Evans-Nguyen, Ch. 1; Learn Forensics Transcript].

#### Instrumentation Architecture:
1. **Sample Inlet:** GC capillary column outlet, LC interface, or direct insertion probe.
2. **Ion Source:**
   * *Electron Ionization (EI — GC-MS):* $70\text{ eV}$ electron beam knocks out an electron, forming radical cation $M^{+\bullet}$ and extensive fragment ions [Evans-Nguyen, Ch. 1].
   * *Chemical Ionization (CI):* Methane reagent gas forms $[\text{M}+\text{H}]^+$ pseudo-molecular ions [Evans-Nguyen, Ch. 1].
   * *Electrospray Ionization (ESI — LC-MS):* High-voltage aerosol evaporation yielding $[\text{M}+\text{H}]^+$ or $[\text{M}-\text{H}]^-$ ions [Evans-Nguyen, Ch. 1; Li, Ch. 11].
3. **Mass Analyzer:**
   * *Quadrupole Mass Filter:* Four parallel hyperbolic steel rods supplied with combined Radiofrequency (RF) and Direct Current (DC) voltages. Operates as a mass filter allowing only specific $m/z$ trajectories to reach detector [Evans-Nguyen, Ch. 1].
   * *Time-of-Flight (TOF):* Accelerates ions into a field-free drift tube; ions separate by velocity—lighter ions travel faster and arrive earlier ($t \propto \sqrt{m/z}$). High resolution (accurate mass to $4$ decimal places).
   * *Ion Trap & Orbitrap:* Electrostatic trapping of ions; Orbitrap provides ultra-high resolution ($>100,000$).
4. **Detector:** Electron Multiplier or Faraday Cup.

```
                           Quadrupole Mass Analyzer
                                       │
                         High-Voltage Quadrupole Rods
                         (Combined RF and DC Potentials)
                               ┌──────────────┐
                               │  Rod 1 (+)   │
                               └──────────────┘
  Gaseous Ions From ──►  • (m/z 1)  • (m/z 2)  • (m/z 3)  ──► Stable Trajectory
  Ion Source           ┌──────────────┐  (Resonant Ion Hits Detector)
                       │  Rod 2 (-)   │
                       └──────────────┘
```

#### Mass Spectrum Data Interpretation:
* **Mass-to-Charge Ratio ($m/z$):** For singly charged ions ($z = +1$), $m/z$ equals nominal/exact ionic mass in unified atomic mass units ($\text{u}$ or $\text{Da}$) [Evans-Nguyen, Ch. 1].
* **Molecular Ion Peak ($M^{+\bullet}$):** Ion corresponding to the intact radical cation formed by electron removal. Gives the unfragmented molecular weight [Evans-Nguyen, Ch. 1].
* **Base Peak:** The most intense peak in the spectrum, arbitrarily set to $100\%$ relative abundance. All other peak heights are scaled relative to the base peak [Evans-Nguyen, Ch. 1].
* **Isotope Ratios ($M+1, M+2$):**
  * *Chlorine:* Natural abundance $^{35}\text{Cl} : ^{37}\text{Cl} \approx 3:1$ ($75.8\% : 24.2\%$). A monomolecular chlorine compound displays an $M:M+2$ peak ratio of $3:1$ [Evans-Nguyen, Ch. 1].
  * *Bromine:* Natural abundance $^{79}\text{Br} : ^{81}\text{Br} \approx 1:1$ ($50.7\% : 49.3\%$). Displays an $M:M+2$ peak ratio of $1:1$ [Evans-Nguyen, Ch. 1].
  * *Carbon ($M+1$):* $^{13}\text{C}$ abundance is $1.11\%$ per carbon atom.

##### Worked Example 4 (Mass Spectrometry $m/z$ & Isotope Ratio Interpretation):
*Problem:* A mass spectrum of an unknown seized illicit drug exhibit exhibits a base peak at $m/z = 58$, a distinct molecular ion peak at $m/z = 181$ ($100\%$ relative height), and a secondary isotope peak at $m/z = 183$ ($32.5\%$ relative height). Evaluate the molecular weight and elemental composition.
*Interpretation:*
1. The intact molecular weight is $181\text{ g/mol}$ (singly charged molecular ion $M^{+\bullet}$ at $m/z = 181$).
2. The ratio of peak heights at $m/z = 181$ ($M$) and $m/z = 183$ ($M+2$) is $100 : 32.5 \approx 3:1$.
3. An $M:M+2$ ratio of $3:1$ is the diagnostic isotopic signature of **one Chlorine atom** ($^{35}\text{Cl} / ^{37}\text{Cl}$).
4. Base peak at $m/z = 58$ corresponds to a stable iminium fragment ion ($[\text{CH}_2=\text{N(CH}_3)_2]^+$), characteristic of local anesthetic or sympathomimetic amine drugs.

---

### 2.6 X-Ray Spectrometry: XRD vs. XRF

#### X-Ray Diffraction (XRD) — Crystalline Structure:
* **Principle:** Monochromatic X-rays ($\text{Cu } K_\alpha, \lambda = 1.5418\text{ \AA}$) collide with ordered atomic planes in a solid crystalline lattice. Scattered X-rays undergo constructive interference at specific angles governed by **Bragg's Law** [Saferstein, Ch. 10; Slide 209]:
  $$n \lambda = 2 d \sin \theta \implies d = \frac{n \lambda}{2 \sin \theta}$$
  *Symbols & Units:*
  * $n$: Order of reflection (integer, $n = 1, 2, 3\dots$).
  * $\lambda$: X-ray wavelength ($\text{\AA}$ or $\text{nm}$).
  * $d$: Interplanar lattice spacing ($\text{\AA}$ or $\text{nm}$).
  * $\theta$: Bragg diffraction angle (degrees).

```
                            Bragg's X-Ray Diffraction (XRD)
                                          │
  Incident X-Rays (λ)                                   Diffracted X-Rays
  ───────►  \                                                 /  ───────►
             \                                               /
    Plane 1  ─●───────────────●───────────────●─────────────●─
              │               │               │
              │  d (Spacing)  │               │
    Plane 2  ─●───────────────●───────────────●─────────────●─
             /                                               \
  ───────►  /                                                 \
```

##### Worked Example 5 (Bragg's Law Calculation):
*Problem:* Crystalline drug powder ($\text{LSD HCl}$) analyzed with $\text{Cu } K_\alpha$ X-rays ($\lambda = 1.5418\text{ \AA}$) produces a primary diffraction peak at $2\theta = 18.40^\circ$ ($n = 1$). Calculate the interplanar crystal spacing ($d$).
*Calculation:*
1. Calculate Bragg angle $\theta$:
   $$\theta = \frac{2\theta}{2} = \frac{18.40^\circ}{2} = 9.20^\circ$$
2. Calculate $\sin(9.20^\circ)$:
   $$\sin(9.20^\circ) = 0.1599$$
3. Apply Bragg's Law ($d = \frac{\lambda}{2 \sin \theta}$):
   $$d = \frac{1.5418\text{ \AA}}{2 \times 0.1599} = \frac{1.5418}{0.3198} = 4.821\text{ \AA} = 0.4821\text{ nm}$$

#### Energy-Dispersive X-Ray Fluorescence (EDXRF) — Elemental Analysis:
* **Principle:** High-energy primary X-rays eject inner-shell ($K$ or $L$) electrons from sample atoms. Outer-shell electrons drop to fill the vacancies, emitting characteristic secondary fluorescent X-rays whose energies identify the element [Saferstein, Ch. 10; Evans-Nguyen, Ch. 1].
* **SEM-EDX (Gunshot Residue Analysis):** A Scanning Electron Microscope (SEM) focuses an electron beam onto microscopic particles; Energy-Dispersive X-Ray Spectrometry (EDX) detects characteristic X-rays, simultaneously determining morphology and elemental composition of primer GSR ($\text{Pb, Ba, Sb}$) [Saferstein, Ch. 10; Biswas, Ch. 5].

#### Comparison: XRD vs. XRF

| Parameter | X-Ray Diffraction (XRD) | X-Ray Fluorescence (XRF) |
| :--- | :--- | :--- |
| **Primary Output** | Crystal structure, mineral phase, polymorph identity [Slide 209]. | Bulk elemental composition ($\text{Na}$ to $\text{U}$) [Evans-Nguyen, Ch. 1]. |
| **Governing Law** | Bragg's Law ($n\lambda = 2d\sin\theta$) [Slide 209]. | Moseley's Law ($E \propto (Z - \sigma)^2$). |
| **Sample State** | Crystalline solid powders required [Slide 209]. | Solid, powder, liquid, or film. |
| **Polymorph Discrimination**| **Yes** (differentiates Calcite $\text{CaCO}_3$ from Aragonite $\text{CaCO}_3$). | **No** (only measures total Calcium and Carbon). |
| **Forensic Uses** | Illicit drug polymorphs, explosive salts, soil mineralogy, cement [Slide 209]. | Glass comparisons, automotive paints, alloys, GSR particles (SEM-EDX) [Saferstein, Ch. 10]. |

---

## Section 3: Advanced & Supplementary Analytical Methods

### 3.1 Raman Spectroscopy
* **Principle:** Inelastic scattering of monochromatic laser light ($532\text{ nm}, 785\text{ nm}$, or $1064\text{ nm}$). Incident photons exchange energy with molecular vibrations, emitting scattered photons at shifted frequencies (Stokes and Anti-Stokes shifts) [Evans-Nguyen, Ch. 1].
* **Selection Rule:** Requires a change in **molecular polarizability ($\frac{d\alpha}{dq} \neq 0$)**.
* **Forensic Value:** Non-destructive, non-contact analysis of evidence directly through transparent plastic bags or glass vials; insensitive to water interference (ideal for aqueous samples) [Evans-Nguyen, Ch. 1].

### 3.2 Nuclear Magnetic Resonance (NMR) Spectroscopy
* **Principle:** Analyzes the absorption of radiofrequency (RF) radiation by atomic nuclei with non-zero magnetic moments ($^{1}\text{H}, ^{13}\text{C}, ^{19}\text{F}, ^{31}\text{P}$) placed inside a powerful superconducting magnetic field ($7.0–14.1\text{ Tesla}$) [Evans-Nguyen, Ch. 1].
* **Forensic Value:** Absolute structural elucidation of novel synthetic designer drugs (fentanyl analogues, synthetic cathinones) without requiring authentic reference standards.

### 3.3 Neutron Activation Analysis (NAA) & LIBS
* **NAA:** Sample is irradiated with thermal neutrons inside a nuclear reactor, converting stable isotopes into radioactive isotopes that emit characteristic gamma rays. Ultra-trace sensitivity ($\text{ppb}$ level) for multi-element analysis (Arsenic in hair/nails, bullet lead) [Slide 197; Saferstein, Ch. 10].
* **LIBS (Laser-Induced Breakdown Spectroscopy):** High-energy pulsed laser vaporizes a microscopic surface spot, forming a high-temperature plasma plume whose optical emission lines reveal elemental composition [Saferstein, Ch. 10].

### 3.4 Critical Evaluation of Provenance, Intent, & Forensic Claims

> **SCIENTIFIC QUALIFICATION:** Physical/chemical composition data alone (e.g., matching trace element profiles in glass, paint, or soil) **establishes class association, NOT legal provenance, intent, or criminal causation**. Additional circumstantial and physical evidence is legally required to prove guilt.

---

## Section 4: Forensic Photography, Videography & Imaging

### 4.1 Fundamentals of Forensic Photography

#### The Exposure Triangle:
Forensic photography relies on balancing three camera parameters to achieve sharp, correctly exposed evidence photographs [Saferstein, Ch. 2]:

```
                           The Exposure Triangle
                                     │
            ┌────────────────────────┼────────────────────────┐
            ▼                        ▼                        ▼
    APERTURE (f-stop)        SHUTTER SPEED            ISO SENSITIVITY
    • Controls Light Volume  • Controls Exposure Time • Sensor Signal Gain
    • Controls Depth of Field• Controls Motion Blur   • Higher ISO = Noise/Grain
```

1. **Aperture ($f$-stop):** Diameter of the lens diaphragm opening. Small aperture numbers ($f/2.8$) yield large openings (bright image, shallow depth of field); large aperture numbers ($f/11, f/16$) yield small openings (**deep depth of field**, keeping entire 3D evidence in crisp focus).
2. **Shutter Speed:** Duration of sensor light exposure. Fast speeds ($1/500\text{ s}$) freeze motion; slow speeds ($1/2\text{ s}$, bulb mode) require a heavy tripod for low-light or fluorescence photography.
3. **ISO Sensitivity:** Digital sensor amplification. Low ISO ($100–200$) provides maximum signal-to-noise ratio and finest detail resolution; high ISO ($>3200$) introduces electronic noise and grain.

#### Three-Step Scene Documentation Rule:
1. **Overall / Contextual Views:** Wide-angle shots establishing the entire crime scene location and landmarks.
2. **Medium-Range Views:** Spatial relationship between specific physical evidence items and scene surroundings.
3. **Close-Up 1:1 Views:** Perpendicular ($90^\circ$ angle) macro views showing fine detail. **Must include an ABFO No. 2 metric scale placed parallel on the same focal plane** [Saferstein, Ch. 2].

#### Specialized Lighting Modes:
* **Direct Front Lighting:** General evidence illumination.
* **Oblique / Side Lighting ($15–45^\circ$ angle):** Creates shadows highlighting low-relief textures (dust footprints, toolmarks, indented writing, impression evidence).
* **Transmitted / Backlighting:** Light passes through evidence from behind (watermarks in paper, fabric weaves, glass fractures).
* **Cross-Polarized Lighting:** Polarizing filters on light source and lens at $90^\circ$ orientation eliminate specular glare on reflective surfaces (wet blood, polished metal, plastic bags).

---

### 4.2 Specialized Photographic Techniques
* **Infrared (IR) Photography ($700–1100\text{ nm}$):** Uses IR-sensitive sensors and barrier filters to capture IR reflection/absorbance. Reveals bloodstains on dark/patterned fabrics, soot-covered arson evidence, and ink obliterations [Saferstein, Ch. 2].
* **Ultraviolet (UV) Photography ($200–400\text{ nm}$):**
  * *Reflected UV:* Uses shortwave UV ($254\text{ nm}$) to photograph untreated impressions on nonporous items.
  * *UV-Induced Fluorescence:* Excites visible fluorescence in biological fluids (semen, saliva), latent prints treated with dye stains, or questioned documents.
* **3D Photogrammetry & Laser Scanning:** Captures spatial $(X,Y,Z)$ point clouds to create scale 3D virtual reconstructions of crime scenes.
* **Forensic Videography:** Continuous unedited audio-visual recording providing a spatial walkthrough of the crime scene.

---

### 4.3 Laboratory Photography, Digital Integrity & Legal Admissibility

#### Image Integrity & Chain of Custody:
1. **Master Image Preservation:** Primary raw capture files (RAW or uncompressed TIFF) must be immediately backed up onto write-once media as read-only **Master Copies**.
2. **Working Copies:** All image processing (contrast enhancement, cropping) must be conducted strictly on **Working Copies**.
3. **Enhancement Audit Logs:** Every digital adjustment step (e.g., in Adobe Photoshop) must be recorded in an automated software history log to ensure reproducibility.
4. **Cryptographic Hashes:** Generating MD5 or SHA-256 digital hash values immediately upon offloading verifies that the file bits have not been tampered with.
5. **EXIF Metadata:** Automated embedded metadata (camera model, serial number, timestamp, exposure settings) provides supporting technical context.

#### Corrective Qualifications on Photographic Claims:
* *RAW vs. JPEG:* RAW/TIFF is best practice for court presentation, but high-quality uncompressed JPEG is legally admissible if supported by a secure chain of custody.
* *1:1 Scale:* Macro 1:1 scale is required for friction ridges and toolmarks, but lower reproduction ratios are standard for overall scene context.

---

## Section 5: Evidence Handling, Storage & Chain of Custody

1. **Contamination Control:** Use clean nitril gloves, disposable tools, and clean outer garments.
2. **Packaging Protocols:**
   * *Moist Biological Evidence:* Air-dried and packaged in **breathable paper bags** to prevent fungal mold growth and DNA degradation [Li, Ch. 9].
   * *Fire Debris / Volatile Accelerants:* Sealed in **airtight clean metal paint cans** or specialized nylon/polyester (Kapton) bags to prevent volatile vapor escape [Evans-Nguyen, Ch. 2].
3. **Chain of Custody Ledger:** Continuous written tracking document recording item ID, collector, date/time, transfer signatures, and storage location [Parikh, Ch. 3].
4. **Conceptual Laboratory Safety:** Mandatory use of personal protective equipment (PPE), chemical fume hoods for volatile solvents, and proper chemical waste disposal.

---

## Section 6: Method-Selection Decision Scenarios & Comparison Tables

| Unknown Evidence Type | Primary Screening Technique | Confirmatory Instrumental Method | Key Analytical Target / Marker |
| :--- | :--- | :--- | :--- |
| **White Powder (Suspected Drug)** | Color Spot Tests / TLC | **GC-MS (EI)** or **FTIR (ATR)** | Retention time, EI fragmentation pattern, IR fingerprint spectrum [Saferstein, Ch. 12]. |
| **Fire Debris (Accelerants)** | Passive Headspace Extraction | **GC-MS (TIC & Extracted Ion Profiles)** | Hydrocarbon alkane/aromatic profile ($m/z\text{ 43, 57, 91, 105}$) [Evans-Nguyen, Ch. 3]. |
| **Gunshot Residue (GSR)** | Modified Griess Test (Nitrites) | **SEM-EDX** or **GFAAS / ICP-MS** | Spherical morphology and elemental presence of $\text{Pb, Ba, Sb}$ [Saferstein, Ch. 10; Biswas, Ch. 5]. |
| **Questioned Ink Entries** | Video Spectral Comparator (VSC) / TLC | **HPLC-DAD** or **Micro-Raman** | Dye absorption spectra, solvent profiles [Allen, Ch. 7]. |
| **Automotive Paint Chip** | Stereomicroscopy (Layer Structure) | **Pyrolysis-GC-MS** & **FTIR** & **SEM-EDX** | Organic binder formulation, synthetic polymer class, inorganic pigment elements [Saferstein, Ch. 10]. |
| **Heavy Metal Poisoning (Hair/Nails)**| Colorimetric Screen | **GFAAS** or **ICP-MS** | Quantitation of trace Arsenic, Mercury, or Lead ($\text{ppb}$ level) [Biswas, Ch. 5]. |

---

## Section 7: Practice Questions & Model Answers

*(Explicitly labelled as Practice Questions for exam preparation)*

### 7.1 Short-Answer Questions (3–5 Marks)

#### Practice Question 1 (4 Marks):
*Differentiate between Atomic Absorption Spectroscopy (AAS) and Atomic Emission Spectroscopy (AES) in terms of principles, light sources, and multi-element capabilities.*

##### Model Answer:
1. **Operating Principle:** AAS measures the absorption of resonance light by ground-state free atoms; AES measures the intensity of optical light emitted by atoms thermally/electrically excited in a flame or plasma [Slide 193, 196].
2. **Light Source:** AAS requires element-specific Hollow Cathode Lamps (HCL); AES requires no external lamp as the hot plasma/flame itself excites the sample to emit light [AFRS Transcript; AES Transcript].
3. **Multi-Element Capability:** AAS is typically a single-element sequential method per lamp; ICP-AES allows simultaneous multi-element analysis ($>70$ elements) in a single run [AES Transcript].
4. **Sample Consumption:** Both techniques are destructive as the sample is atomized [Slide 194, 195].

---

#### Practice Question 2 (5 Marks):
*Explain the Beer–Lambert Law. State its mathematical formula, define all symbols with units, and list three operational limitations.*

##### Model Answer:
1. **Definition:** The Beer–Lambert Law states that the absorbance of a monochromatic beam of light passing through a homogeneous solution is directly proportional to the analyte concentration and path length [Saferstein, Ch. 12; NG Rao, Ch. 31].
2. **Mathematical Equation:**
   $$A = \epsilon b c$$
3. **Symbols & Units:**
   * $A$: Absorbance (unitless).
   * $\epsilon$: Molar absorptivity ($\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$).
   * $b$: Path length of sample cuvette ($\text{cm}$).
   * $c$: Concentration ($\text{mol}\cdot\text{L}^{-1}$).
4. **Operational Limitations:**
   * Deviations occur at high concentrations ($>0.01\text{ M}$) due to electrostatic solute interactions.
   * Non-monochromatic light sources introduce non-linear response.
   * Light scattering by suspended particulates or chemical association/dissociation alters measured absorbance.

---

### 7.2 Long-Answer Questions (7–10 Marks)

#### Practice Question 3 (10 Marks):
*A white powder exhibit seized at a crime scene is suspected to contain a mixture of cocaine and cutting agents. Outline a complete instrumental workflow for screening and confirmatory analysis. Justify the choice of each instrument, detail operating principles, and describe the expected outputs.*

##### Model Answer:
1. **Initial Screening (Category C / B):**
   * *Method:* Thin Layer Chromatography (TLC) on $F_{254}$ silica gel plates.
   * *Justification:* Fast, inexpensive, resolves cocaine from cutting agents (procaine, caffeine, sugars).
   * *Output:* Solute spots visualized under $254\text{ nm}$ UV light; calculated $R_f$ values compared against reference standards.
2. **Confirmatory Structural Identification (Category A):**
   * *Method 1:* **Gas Chromatography–Mass Spectrometry (GC-MS with Electron Ionization)** [Saferstein, Ch. 12].
   * *Justification:* GC resolves the volatile mixture components; EI ($70\text{ eV}$) produces reproducible fragmentation.
   * *Output:* GC chromatogram exhibiting retention time ($t_R$), and EI mass spectrum displaying the molecular ion $M^{+\bullet}$ ($m/z = 303$ for cocaine) and base peak ($m/z = 82$, tropane ring ion). Spectrum is matched against NIST/SWGDRUG libraries.
   * *Method 2:* **Fourier Transform Infrared Spectroscopy (ATR-FTIR)** [Saferstein, Ch. 12].
   * *Justification:* Analyzes pure isolated solid powder non-destructively.
   * *Output:* IR spectrum displaying functional group bands ($\text{C=O}$ ester stretch at $1710–1735\text{ cm}^{-1}$, aromatic $\text{C-H}$ stretches) and a unique $100\%$ match in the Fingerprint Region ($1500–400\text{ cm}^{-1}$), confirming cocaine $\text{HCl}$ salt.

---

## Section 8: Glossary of Technical Terms

* **Absorbance ($A$):** Logarithmic ratio of incident to transmitted light intensity ($A = -\log_{10} T$).
* **Base Peak:** The most intense ion peak ($100\%$ relative abundance) in a mass spectrum.
* **Chromophore:** A functional group containing unsaturated $\pi$ bonds responsible for UV-Vis light absorption.
* **Evanescent Wave:** An electromagnetic field formed during ATR total internal reflection that penetrates $0.5–2.0\text{ }\mu\text{m}$ into the sample.
* **Fingerprint Region:** The $1500–400\text{ cm}^{-1}$ region of an IR spectrum displaying unique molecular skeletal vibrations.
* **Hyphenated Technique:** The direct coupling of a chromatographic separation system to a spectroscopic detector (e.g., GC-MS, LC-MS/MS).
* **Molecular Ion ($M^{+\bullet}$):** The radical cation formed in mass spectrometry by the loss of a single electron from the intact molecule.
* **Molar Absorptivity ($\epsilon$):** A constant measuring how strongly a chemical species absorbs light at a specific wavelength ($\text{L}\cdot\text{mol}^{-1}\cdot\text{cm}^{-1}$).
* **Retention Time ($t_R$):** The time elapsed between sample injection and detector peak maximum in chromatography.
* **Wavenumber ($\tilde{\nu}$):** The number of wave cycles per centimeter ($\text{cm}^{-1}$), directly proportional to energy ($\tilde{\nu} = 1/\lambda$).

---

## Section 9: Revision Sheet & Quick Cheat Sheets

### 9.1 Instrumental Technique Summary Cheat Sheet

| Instrument | Primary Signal Measured | Analyte Type | Category (SWGDRUG) | Key Output |
| :--- | :--- | :--- | :--- | :--- |
| **TLC** | $R_f$ value | Non-volatile/volatile mixtures | Category C | Colored/UV spots on plate |
| **GC-FID** | Retention time ($t_R$), flame current | Volatile, thermostable organic compounds | Category B | Chromatogram peaks |
| **HPLC-DAD** | $t_R$ and UV-Vis spectrum | Thermolabile, polar, non-volatile compounds | Category B | 3D chromatogram & UV spectra |
| **UV-Vis** | Absorbance vs. wavelength ($\lambda$) | Conjugated organic molecules, dyes | Category C | Absorption curves ($\lambda_{\text{max}}$) |
| **FTIR** | Transmittance ($\%T$) vs. wavenumber | Organic compounds, polymers, drug salts | Category A | Vibrational spectrum |
| **AAS** | Light absorption by gas atoms | Heavy metals, GSR ($\text{Pb, Ba, Sb}$) | Category B | Element concentration ($\text{ppm/ppb}$) |
| **ICP-AES** | Optical light emission from plasma | Trace metals, glass, alloys, soil | Category B | Line emission spectrum |
| **GC-MS** | Mass-to-charge ratio ($m/z$) | Volatile organic compounds | Category A | Fragmentation mass spectrum |
| **XRD** | X-ray diffraction angle ($2\theta$) | Solid crystalline powders | Category A | Crystal diffractogram peaks |
| **EDXRF** | Secondary X-ray fluorescence energy | Bulk elemental composition | Category B | Elemental energy spectrum |

---

## Section 10: Syllabus-to-Source Coverage Matrix & Honest Completeness Audit

| Course Policy Syllabus Topic | Primary Source Coverage | Supplementary Textbooks / Video | Completeness & Audit Status |
| :--- | :--- | :--- | :--- |
| **Chromatography (TLC, GC, HPLC/LC)** | Unit 5 PPTs; Scion URL | Saferstein Ch. 12; Allen Ch. 7 | **$100\%$ Covered** (TLC flowchart correction integrated). |
| **UV-Visible Spectroscopy** | Unit 5 PPTs; Vidya-mitra Video | Saferstein Ch. 12; NG Rao Ch. 31 | **$100\%$ Covered** (Beer's Law math & worked examples added). |
| **IR & FTIR Spectroscopy** | Unit 5 PPTs; CrashCourse Video | Saferstein Ch. 12; Allen Ch. 7 | **$100\%$ Covered** (Michelson interferometer & ATR added). |
| **AAS & AES / ICP-AES** | Unit 5 PPTs; AFRS & AES Videos | Saferstein Ch. 10; Biswas Ch. 5 | **$100\%$ Covered** (HCL lamp & plasma torch detailed). |
| **Mass Spectrometry (MS)** | Unit 5 PPTs; Learn Forensics Video| Saferstein Ch. 12; Li Ch. 11 | **$100\%$ Covered** (EI/CI/ESI, isotope math, base peak added). |
| **X-Ray Spectrometry (XRD / XRF)**| Unit 5 PPTs | Saferstein Ch. 10; Evans-Nguyen Ch. 1| **$100\%$ Covered** (Bragg's law math & worked examples added). |
| **Forensic Photography & Imaging** | IFS Course Policy | Saferstein Ch. 2; Forensic Texts | **$100\%$ Covered** (Exposure triangle & digital integrity added). |
| **Evidence Handling & Storage** | IFS Course Policy | Li Ch. 9; Evans-Nguyen Ch. 2 | **$100\%$ Covered** (Paper bags vs. metal cans detailed). |

---
