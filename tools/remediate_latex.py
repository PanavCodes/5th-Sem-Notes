#!/usr/bin/env python3
"""
tools/remediate_latex.py
Exhaustive remediation of LaTeX math, display brackets, currency symbols, and broken line-wraps across FIMIS notes & PYQs.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def fix_file(path: Path):
    if not path.exists():
        return
    content = path.read_text(encoding="utf-8")
    original = content

    # 1. Convert all display brackets \\[ ... \\] to $$ ... $$
    content = re.sub(r"\\\[(.*?)\\\]", r"$$\n\1\n$$", content, flags=re.DOTALL)
    # Strip any trailing backslash from the end of display math before closing $$
    content = re.sub(r"\\\s*\n\$\$", r"\n$$", content)

    # 2. Fix $\text{₹} ... $ and $\text{₹...}$
    # e.g. $\text{₹}10\text{ Lakh}$ -> ₹10 Lakh
    def repl_rupee(m):
        val = m.group(1).strip()
        unit = m.group(2).strip() if m.group(2) else ""
        unit = re.sub(r"\s+", " ", unit)
        return f"₹{val} {unit}".strip()

    content = re.sub(
        r"\$\\text\{₹\}\s*([0-9,.]+)\s*(?:\\text\{\s*([A-Za-z\s]+)\s*\})?\$",
        repl_rupee,
        content,
        flags=re.DOTALL
    )

    # e.g. $\text{₹1,00,000}$ -> ₹1,00,000
    content = re.sub(
        r"\$\\text\{₹\s*([0-9,.]+)\s*\}\$",
        r"₹\1",
        content
    )

    # 3. Fix $\text{Rs. } ... $ and $\text{Rs } ... $ and $\text{INR } ... $
    def repl_rs(m):
        prefix = m.group(1) if m.group(1) else ""
        val = m.group(2).strip()
        unit = m.group(3).strip() if m.group(3) else ""
        unit = re.sub(r"\s+", " ", unit)
        p = "≈ " if "approx" in prefix else ""
        return f"{p}₹{val} {unit}".strip()

    content = re.sub(
        r"\$(\\approx\s*)?\\text\{(?:Rs\.?|INR)\s*\}\s*([0-9,.]+)\s*(?:\\text\{\s*([A-Za-z\s/]+)\s*\})?\$",
        repl_rs,
        content,
        flags=re.DOTALL
    )

    # 4. Fix arrows in prose
    content = content.replace(r"$\rightarrow$", "→")

    # 5. Fix €
    content = re.sub(r"\$\\text\{€\}\s*([0-9,.]+)\$", r"€\1", content)

    # 6. Specific file patches
    # Unit 9 PYQ
    if path.name == "fimis-unit9-factoring-forfaiting-pyq-bank.md":
        content = re.sub(
            r"80\%\s*\(\s*\$\\text\{₹\}8\\text\{\s*Lakh\}\s*\*\*\)",
            r"80% (₹8 Lakh)**",
            content
        )
        content = re.sub(
            r"80\%\s*\(\s*₹8\s*Lakh\s*\)\s*\*\*",
            r"80% (₹8 Lakh)**",
            content
        )
        content = content.replace(
            "`📊 Diagram Required: YES | Type: Platform Architecture | Source: Pathak Ch. 20\n/ Slide Unit 9`",
            "`📊 Diagram Required: YES | Type: Platform Architecture | Exam Sketch Target: TReDS Auction Architecture`"
        )
        content = content.replace(
            "`📊 Diagram Required: YES | Type: Structural Comparison | Source: Unit-9.pptx /\nPathak Ch. 20`",
            "`📊 Diagram Required: YES | Type: Structural Comparison | Exam Sketch Target: Factoring vs Forfaiting Comparison Matrix`"
        )
        # Fix line 124-125 wrap
        content = re.sub(
            r"advances \*\*80% \(.*?Lakh\}\)\*\*\.",
            r"advances **80% (₹8 Lakh)**.",
            content,
            flags=re.DOTALL
        )
        content = re.sub(
            r"refund of the \$\\text\{₹\}8\\text\{ Lakh\}\$ advance",
            r"refund of the ₹8 Lakh advance",
            content
        )

    # Unit 5 PYQ
    if path.name == "fimis-unit5-financial-markets-pyq-bank.md":
        content = re.sub(
            r"\(\$T \\le 1\\text\{ year\}\$ vs\. \$T >\s*\n\s*1\\text\{ year\}\$\)",
            r"($T \\le 1\\text{ year}$ vs. $T > 1\\text{ year}$)",
            content
        )
        content = re.sub(
            r"\(\$P_{\\text\{cap\}}\s*\\le\s*1\.20\s*\\times\s*\n\s*P_{\\text\{floor\}}\$\)",
            r"($P_{\\text{cap}} \\le 1.20 \\times P_{\\text{floor}}$)",
            content
        )
        content = re.sub(
            r"\(\$T = 90\\text\{ to \}\s*\n\s*180\\text\{ days\}\$\)",
            r"($T = 90\\text{ to } 180\\text{ days}$)",
            content
        )
        content = re.sub(
            r"\$38\.25\\text\{\s*\n?\s*times\}\$",
            r"38.25 times",
            content
        )
        content = content.replace("($\\approx \n51\\%\\$", "($\\approx 51\\%\\$")
        content = content.replace("($\\approx\n51\\%\\$", "($\\approx 51\\%\\$")
        content = re.sub(r"\(\$\\approx\s*\n\s*51\\%\$\s*listing gain\)", r"($\\approx 51\\%$ listing gain)", content)

    # Unit 6 PYQ
    if path.name == "fimis-unit6-financial-instruments-pyq-bank.md":
        content = content.replace(r"$\text{₹}25,000$", "₹25,000")
        content = content.replace(r"($\text{₹}100$)", "(₹100)")
        content = content.replace(r"$\text{₹}5\text{ Lakhs}$", "₹5 Lakh")
        content = content.replace(r"$\text{₹}1\text{ Lakh}$", "₹1 Lakh")
        content = content.replace(r"$\text{₹}5,000,000$ ($\text{₹}5\text{ L}$)", "₹50,00,000 (₹5 L)")
        content = content.replace(r"$\text{₹}100,000$ ($\text{₹}1\text{ L}$)", "₹1,00,000 (₹1 L)")
        content = content.replace(r"Typically $\text{₹}5\text{ Crores}$ (Interbank)", "Typically ₹5 Crores (Interbank)")
        content = re.sub(r"\$\\text\{₹\}3,000\\text\{\s*\n?\s*Crores?\}\$", "₹3,000 Crore", content)
        content = content.replace(r"$\text{₹}1,60,000\text{ Crores}$", "₹1,60,000 Crore")
        content = content.replace(r"$\text{₹}53,124\text{ Crore}$", "₹53,124 Crore")
        content = content.replace(r"($>\text{₹}20,000\text{ Crores}$ annually)", "(> ₹20,000 Crore annually)")
        content = content.replace(r"$\text{₹}3,000\text{ Crore}$", "₹3,000 Crore")
        content = content.replace(r"$\text{₹}65$", "₹65")
        content = content.replace(r"$\text{₹}97$", "₹97")
        content = content.replace(r"$\text{₹}83.50/USD$", "₹83.50/USD")
        content = re.sub(r"\$\\text\{₹\}500\\text\{\s*\n?\s*Crore\}\$", "₹500 Crore", content)
        content = content.replace(r"$\text{₹}150$", "₹150")
        content = re.sub(r"SOFR \$\+\s*150\\text\{\s*\n?\s*bps\}\$", r"$\text{SOFR} + 150\text{ bps}$", content)
        content = content.replace(r"$\text{₹}83$", "₹83")
        content = content.replace(r"$\text{₹}90/USD$", "₹90/USD")

    # Unit 6 Study Notes
    if path.name == "fimis-unit6-financial-instruments-study-notes.md":
        content = content.replace(
            r"($₹9,000\text{ crore fresh issue} + ₹375\text{ crore offer for sale}$)",
            r"(₹9,000 crore fresh issue + ₹375 crore offer for sale)"
        )
        content = content.replace(r"$1\text{ USD} = ₹84.50$", "1 USD = ₹84.50")
        content = content.replace(r"$₹9,375\text{ crore}$", "₹9,375 crore")
        content = content.replace(r"$S_0 = ₹100$", r"$S_0 =$ ₹100")
        content = content.replace(r"$K = ₹100$", r"$K =$ ₹100")
        content = content.replace(r"$P = ₹5$", r"$P =$ ₹5")
        content = content.replace(r"$S_0 + P = ₹105$", r"$S_0 + P =$ ₹105")
        content = content.replace(r"$S_T = ₹70$", r"$S_T =$ ₹70")
        content = content.replace(r"$K - S_T = 100 - 70 = +₹30$", r"$K - S_T = 100 - 70 = +30$ (₹30)")
        content = content.replace(r"$₹70$", "₹70")
        content = content.replace(r"$70 + 30 = ₹100$", r"$70 + 30 = 100$ (₹100)")
        content = content.replace(r"$100 - 105 = -₹5$", r"$100 - 105 = -5$ (-₹5)")
        content = content.replace(r"$S_T = ₹150$", r"$S_T =$ ₹150")
        content = content.replace(r"$₹0$", "₹0")
        content = content.replace(r"$₹150$", "₹150")
        content = content.replace(r"$150 - 105 = +₹45$", r"$150 - 105 = +45$ (+₹45)")
        content = content.replace(r"$K = ₹110$", r"$K =$ ₹110")
        content = content.replace(r"$P = ₹4$", r"$P =$ ₹4")
        content = content.replace(r"$S_0 - P = ₹96$", r"$S_0 - P =$ ₹96")
        content = content.replace(r"$S_T = ₹100$", r"$S_T =$ ₹100")
        content = content.replace(r"($₹100$)", "(₹100)")
        content = content.replace(r"($₹4$)", "(₹4)")
        content = content.replace(r"$₹104$", "₹104")
        content = content.replace(r"$104 - 100 = +₹4$", r"$104 - 100 = +4$ (+₹4)")
        content = content.replace(r"$S_T = ₹140$", r"$S_T =$ ₹140")
        content = content.replace(r"$110 + 4 = ₹114$", r"$110 + 4 = 114$ (₹114)")
        content = content.replace(r"$114 - 100 = +₹14$", r"$114 - 100 = +14$ (+₹14)")

    # Unit 7 PYQ
    if path.name == "fimis-unit7-financial-services-pyq-bank.md":
        content = re.sub(
            r"\(\$1 -\s*\n\s*\\text\{Recovery Rate\}\$\)",
            r"($1 - \\text{Recovery Rate}$)",
            content
        )

    # Unit 7 Study Notes
    if path.name == "fimis-unit7-financial-services-study-notes.md":
        content = content.replace(r"$16B", r"\$16B")
        content = content.replace("for $16 Billion", "for \\$16 Billion")
        content = content.replace("a $16 Billion acquisition", "a \\$16 Billion acquisition")
        content = content.replace("funding of $150,000$ from", "funding of \\$150,000 from")
        content = content.replace(r"($240 \text{ months} \times ₹5,000$)", "(240 months × ₹5,000)")
        content = content.replace(
            r"\mathbf{\text{₹}49,95,740}",
            r"\mathbf{\text{Rs. } 49,95,740} \text{ (₹49.95 Lakh)}"
        )

    # Unit 8 PYQ
    if path.name == "fimis-unit8-leasing-hire-purchase-pyq-bank.md":
        content = re.sub(
            r"\$60\\% -\s*\n\s*80\\%\$",
            r"$60\\% - 80\\%$",
            content
        )

    # Unit 8 Study Notes
    if path.name == "fimis-unit8-leasing-hire-purchase-study-notes.md":
        content = content.replace(r"$\approx \text{₹1,00,000,000}$", "≈ ₹10 Crore")
        content = content.replace(r"$\text{₹50,000 per unit}$", "₹50,000 per unit")
        content = content.replace(r"$\text{₹2,000 per laptop per month}$", "₹2,000 per laptop per month")
        content = content.replace(r"$\text{₹4,00,000 total monthly rental}$", "₹4,00,000 total monthly rental")
        content = content.replace(r"$\text{₹15 crore}$", "₹15 Crore")
        content = content.replace(r"$\text{₹75 crore}$", "₹75 Crore")
        content = content.replace(r"$Dep = \text{₹3,00,000 per year}$", r"$Dep = \text{Rs. } 3{,}00{,}000\text{/year}$ (₹3,00,000 per year)")
        content = content.replace(r"$\approx \text{₹8,98,000}$", r"$\approx \text{Rs. } 8{,}98{,}000$ (₹8,98,000)")
        content = content.replace(r"$P = \text{₹80,000}$", r"Financed Principal $P =$ ₹80,000")
        content = content.replace(r"$\text{₹2,000/mo}$", "₹2,000/mo")
        content = content.replace(r"$\text{₹1 crore}$", "₹1 crore")
        content = content.replace(r"$\text{₹2 crore}$", "₹2 crore")
        content = content.replace(r"$\text{₹5 lakh}$", "₹5 lakh")
        content = content.replace(r"$\text{₹1,00,000}$", "₹1,00,000")
        content = content.replace(r"$\text{₹25,00,000,000}$", "₹250 Crore")
        content = content.replace(r"$\text{₹40,00,000,000}$", "₹400 Crore")
        content = content.replace(r"$\text{₹40 crore}$", "₹40 Crore")
        content = content.replace(r"$\text{₹25 crore}$", "₹25 Crore")
        content = content.replace(r"$\text{₹1,000,000,000}$", "₹100 Crore")
        content = content.replace(r"$\text{₹100 crore}$", "₹100 Crore")
        content = content.replace(r"$\text{₹10,000,000}$", "₹1 Crore")
        content = content.replace(r"$\text{₹3,60,000 per year}$", "₹3,60,000 per year")
        content = content.replace(r"$\text{₹3,42,000}$", "₹3,42,000")
        content = content.replace(r"$\text{₹3,42,000 per year}$", "₹3,42,000 per year")
        content = content.replace(r"$(+\text{₹1,02,000})$", "(+₹1,02,000)")
        content = content.replace(r"$\text{₹20,000}$", "₹20,000")
        content = content.replace(r"$\text{₹80,000}$", "₹80,000")
        content = content.replace(r"$\text{₹16,000}$", "₹16,000")
        content = content.replace(r"$\text{₹96,000}$", "₹96,000")
        content = content.replace(r"$\text{₹4,000 per month}$", "₹4,000 per month")
        content = content.replace(r"$\text{₹1,16,000}$", "₹1,16,000")
        content = content.replace(r"$\text{₹5,00,000}$", "₹5,00,000")
        content = content.replace(r"$\text{₹4,00,000}$", "₹4,00,000")
        # In formulas
        content = content.replace(r"\text{₹3,60,000}", r"\text{Rs. } 3{,}60{,}000")
        content = content.replace(r"\text{₹2,52,000}", r"\text{Rs. } 2{,}52{,}000")
        content = content.replace(r"\text{₹3,00,000}", r"\text{Rs. } 3{,}00{,}000")
        content = content.replace(r"\text{₹90,000}", r"\text{Rs. } 90{,}000")
        content = content.replace(r"\text{₹2,52,000 (Lease Rent)}", r"\text{Rs. } 2{,}52{,}000 \text{ (Lease Rent)}")
        content = content.replace(r"\text{₹90,000 (Lost Tax Shield)}", r"\text{Rs. } 90{,}000 \text{ (Lost Tax Shield)}")
        content = content.replace(r"\text{₹3,42,000 per year}", r"\text{Rs. } 3{,}42{,}000 \text{ per year}")
        content = content.replace(r"(\text{₹10,00,000})", r"(\text{Rs. } 10{,}00{,}000)")
        content = content.replace(r"(\text{₹8,98,000})", r"(\text{Rs. } 8{,}98{,}000)")
        content = content.replace(r"+\text{₹1,02,000}", r"+\text{Rs. } 1{,}02{,}000")
        content = content.replace(
            r"$\text{₹80,000} \times 10\% \times 2 = \text{₹16,000}$",
            r"$\text{Rs. } 80{,}000 \times 10\% \times 2 = \text{Rs. } 16{,}000$ (₹16,000)"
        )
        content = content.replace(
            r"$\text{₹80,000} + \text{₹16,000} = \text{₹96,000}$",
            r"$\text{Rs. } 80{,}000 + \text{Rs. } 16{,}000 = \text{Rs. } 96{,}000$ (₹96,000)"
        )
        content = content.replace(
            r"$\text{₹96,000} / 24 = \text{₹4,000 per month}$",
            r"$\text{Rs. } 96{,}000 / 24 = \text{Rs. } 4{,}000\text{/month}$ (₹4,000/month)"
        )
        content = content.replace(
            r"Down Payment ($\text{₹20,000}$) $+$ Instalments ($\text{₹96,000}$) = $\text{₹1,16,000}$",
            r"Down Payment (₹20,000) + Instalments (₹96,000) = ₹1,16,000"
        )

    # Unit 10 PYQ
    if path.name == "fimis-unit10-consumer-finance-private-capital-pyq-bank.md":
        content = re.sub(
            r"\$r = \\text\{Periodic Monthly Interest Rate \}\s*\\left\(\\frac\{\\text\{Annual\s*\n\s*Rate\}\}\{12 \\times 100\}\\right\)\$",
            r"$r = \\text{Periodic Monthly Interest Rate } \\left(\\frac{\\text{Annual Rate}}{12 \\times 100}\\right)$",
            content
        )
        content = re.sub(
            r"\(\$75\\% -\s*\n\s*90\\%\$\)",
            r"(75% - 90%)",
            content
        )

    # Unit 10 Study Notes
    if path.name == "fimis-unit10-notes.md":
        content = content.replace("**$16 Billion**", "**\\$16 Billion**")
        content = content.replace("($24.4 Billion Going-Private Buyout)", "(\\$24.4 Billion Going-Private Buyout)")
        content = content.replace("**$24.4 Billion**", "**\\$24.4 Billion**")
        content = content.replace("via $15 Billion in debt", "via \\$15 Billion in debt")
        content = content.replace("price of $13.75 per share", "price of \\$13.75 per share")

    # Unit 1
    if path.name == "fimis-unit1-pyq-bank-v2.md":
        content = content.replace("**$1.2 billion**", "**\\$1.2 billion**")
        content = content.replace("secure a $600 million emergency loan", "secure a \\$600 million emergency loan")
    if path.name == "fimis-unit1-study-notes-v2.md":
        content = content.replace("falling to **$1.2 billion**", "falling to **\\$1.2 billion**")

    if content != original:
        path.write_text(content, encoding="utf-8")
        print(f"Remediated: {path.name}")
    else:
        print(f"Unchanged: {path.name}")


def main():
    import glob
    for p in sorted(glob.glob("FIMIS/**/*.md", recursive=True)):
        fix_file(Path(p))


if __name__ == "__main__":
    main()
