#!/usr/bin/env python3
"""
Sequential PYQ Bank Generator for FIMIS Units 5, 6, 7, 8, 9, 10
Leverages authenticated NotebookLM session with the FIMIS Course Notebook (281e880e-f4ff-4c4d-8742-69f52ce631cc).
Optimized for NotebookLM token limits (<4500 characters per prompt).
"""

import os
import re
import sys
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FIMIS_NOTEBOOK_ID = "281e880e-f4ff-4c4d-8742-69f52ce631cc"

UNITS = {
    8: {
        "title": "Equipment Leasing & Hire Purchase",
        "slug": "leasing-hire-purchase",
        "slide_anchor": "Unit-8.pptx",
        "folder": "FIMIS/Unit_8",
        "subtopics": """1. Equipment Leasing Framework: Lessor vs Lessee, asset financing without full upfront capex.
2. Types of Leases: Operating Lease (< economic life, cancellable, lessor maintains, obsolescence risk on lessor); Finance Lease (covers asset life, non-cancellable, lessee maintains/insures, nominal purchase option); Sale & Leaseback (capital unlocking, e.g., IndiGo aircraft); Leveraged Lease (3-party: Lessee, Lessor/Equity, Lender/Debt).
3. Ind AS 116 Impact: Elimination of off-balance-sheet operating lease accounting; mandatory recognition of Right-of-Use (ROU) Asset and Lease Liability on balance sheet.
4. Lease Evaluation & Net Advantage of Leasing (NAL): Theoretical framework (Lease vs Borrow-and-Buy discounted at after-tax cost of debt); NAL = Asset Price - PV of [After-tax Rent + Lost Depreciation Tax Shield + Lost Salvage Value]; Decision rule: NAL > 0 -> Lease, NAL < 0 -> Buy; Standard worked numericals.
5. Hire Purchase (HP): Legal definition, possession on day 1 vs ownership transfer on final instalment, down payment, hypothecation charge, repossession rights upon default.
6. Tax Treatment of HP: Hirer gets double tax shield (interest deduction + asset depreciation deduction).
7. Mathematics of HP: Flat Interest vs Effective Reducing Rate; Formula: Effective Rate approx Flat Rate * [2n / (n + 1)], EMI calculation.
8. Comparative Analysis: Leasing vs Hire Purchase across 6+ statutory and operational parameters."""
    },
    10: {
        "title": "Consumer Finance & Private Capital",
        "slug": "consumer-finance-private-capital",
        "slide_anchor": "Course Syllabus & Consumer Finance Slide Deck",
        "folder": "FIMIS/Unit_10",
        "subtopics": """1. Consumer Finance Infrastructure: Revolving Credit (Credit cards, personal lines) vs Instalment Credit (Auto loans, consumer durables); The 40-50% Fixed Obligation to Income Ratio (FOIR) / EMI capacity benchmark; Macro role in consumption smoothing.
2. Credit Cards & Payment Mechanisms: Transaction lifecycle (Cardholder, Merchant, Acquirer, Card Network, Issuer), Billing cycle, Grace / Interest-free period, Minimum Amount Due (MAD), Compound interest on rollover balance, Interchange fees, Digital payment rails (UPI, Auto-Pay).
3. Credit Rating Systems & Bureau Scoring: Credit Information Companies (CIBIL, Experian, Equifax, CRIF High Mark); Scoring parameters (Repayment history 35%, Credit utilization 30%, Credit age/mix, Inquiries); CIBIL score bands (300-900) and risk thresholds.
4. Securitization & Asset-Backed Securities (ABS): Securitization mechanics (Originator -> SPV -> Investors), Pass-Through Certificates (PTCs) vs Pay-Through Securities; True Sale criterion, Bankruptcy remoteness, Credit enhancements (Cash collateral, over-collateralization, subordination); SARFAESI Act 2002 recovery provisions.
5. Housing Finance & Mortgage Markets: Fixed vs Floating rate home loans, Loan-to-Value (LTV) limits, National Housing Bank (NHB) regulatory supervisory role, Priority Sector Lending (PSL) mortgage limits.
6. Private Placement & Qualified Institutional Placements (QIPs): Section 42 of Companies Act 2013, Advantages over public issues, SEBI QIP framework for rapid capital raising.
7. Private Equity (PE) & Venture Capital (VC): Investment lifecycle (Seed / Angel, Early Stage, Growth Capital, Bridge / Pre-IPO, Leveraged Buyout / LBO); Alternative Investment Funds (AIF) Category I, II, III under SEBI regulations; Valuation methods and Exit routes (IPO, Strategic M&A, Secondary Sale, Promoter Buyback)."""
    }
}


def clean_markdown(text: str) -> str:
    """Clean citations and standardize LaTeX for GitHub Markdown."""
    # Remove citations like [38], [12, 14]
    text = re.sub(r"[ \t]*\[\d+(?:[,\s]+\d+)*\]", "", text)
    # Convert escaped LaTeX delimiters \( and \) to standard $
    text = re.sub(r"\\\\\(", "$", text)
    text = re.sub(r"\\\\\)", "$", text)
    text = re.sub(r"\\\(", "$", text)
    text = re.sub(r"\\\)", "$", text)
    return text.strip()


def build_pyq_prompt(unit_num: int, unit_info: dict) -> str:
    """Construct token-safe, domain-calibrated PYQ Bank prompt (<4500 chars)."""
    unit_title = unit_info["title"]
    slide_anchor = unit_info["slide_anchor"]
    subtopics = unit_info["subtopics"].strip()

    prompt = f"""Generate the complete, unabridged Previous-Year Question (PYQ) Bank for Financial Institutions, Markets, Instruments and Services (FIMIS) - Unit {unit_num}: {unit_title}.

CRITICAL INSTRUCTION: Output the entire, exhaustive Markdown document directly in your chat response. DO NOT summarize, DO NOT create an external file artifact. Begin immediately with '# FIMIS Unit {unit_num}: {unit_title} — Solved Previous Year Question (PYQ) Bank'.

### 1. AUTHORITATIVE SCOPE & PRIMARY SOURCE
- Anchor: '{slide_anchor}' is the SOLE syllabus boundary. Cover only Unit {unit_num} topics. Discard other units.
- Source Docs: Extract PYQs from all uploaded exam papers (Final Exams 2022-2026, Re-Exams, Model Papers). Use reference textbooks (Pathak, Madura) strictly for complete model answers.

### 2. SYLLABUS SCOPE (UNIT {unit_num})
{subtopics}

### 3. DOMAIN INSTRUCTIONS: [THEORY, GOVERNANCE & FINANCE]
- Strictly follow NMIMS MPSTME exam standards.
- Enforce rigorous LaTeX ($...$ and $$...$$) for all financial formulas, ratios, NAL calculations, and interest rates.
- Structure case studies with 4 parts: (1) Background, (2) Structural Mechanism, (3) Regulatory/Market Challenge, (4) Financial Outcome.

### 4. PYQ EXTRACTION, GROUPING & DEDUPLICATION RULES
- Scan ALL uploaded exam papers for Unit {unit_num} questions. Group questions testing the same core concept under a single primary heading.
- For EVERY question inside a group, list: *Exact Question String* | *Exam/Paper Name* | *Year* | *Q. Number* | *Marks*.
- Provide ONE definitive, comprehensive model answer per group scaled to the highest mark allocation.
- Diagram tag: '📊 Diagram Required: YES | Type: [Flow/Workflow] | Source: [Slide/Textbook]'.

### 5. MARK-PROPORTIONAL FORMATTING
- 2 Marks: Formal definition + 2 core bullet points.
- 5 Marks: Formal definition + 4–5 structured points + 3-column summary table or minimal ASCII workflow.
- 10 Marks: Theoretical foundation + end-to-end operational workflow + exhaustive multi-variable comparison table (5+ parameters) + structured 4-part case study or complete numerical solution.
- Difference questions MUST be answered using a structured Markdown comparison table.

### 6. ANALYTICAL APPENDIX
1. Topic-Wise Frequency Table (ranked by past appearances).
2. Concept Redundancy Map across past years.
3. Question Priority Matrix: 🔥 Very Important, ⭐ Important, 🟡 Moderate Priority.
4. Slide Coverage Audit against past exam papers.

Formatting: Clean GitHub Markdown with standard LaTeX ($...$, $$...$$)."""
    return prompt


def execute_notebooklm_query(unit_num: int, prompt_text: str) -> str:
    """Send prompt to NotebookLM CLI, handling multi-turn if needed to get unabridged output."""
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt", encoding="utf-8") as f:
        f.write(prompt_text)
        temp_prompt_path = f.name

    try:
        print("🧠 Querying NotebookLM (Turn 1)...")
        res = subprocess.run(
            ["notebooklm", "ask", "-n", FIMIS_NOTEBOOK_ID, "--prompt-file", temp_prompt_path, "--new", "--yes"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if res.returncode != 0:
            print(f"Error querying NotebookLM: {res.stderr}")
            return ""

        output = res.stdout
        answer = output.split("Answer:", 1)[1] if "Answer:" in output else output
        
        # Check conversation ID
        conv_match = re.search(r"conversation:\s*([0-9a-f\-]+)", output, re.IGNORECASE)
        conv_id = conv_match.group(1) if conv_match else None

        # Check if output is a short summary or placeholder
        if len(answer.strip()) < 800 or "compiled and published" in answer or "Studio panel" in answer:
            print(f"ℹ️ Received studio artifact summary ({len(answer.strip())} chars). Requesting full text in Turn 2...")
            if conv_id:
                followup_prompt = (
                    f"Print the entire, unabridged solved PYQ bank document for Unit {unit_num} directly into your "
                    f"chat response right now. Do not write a summary or confirmation note. Output the exact full "
                    f"markdown document starting with # FIMIS Unit {unit_num}."
                )
                res2 = subprocess.run(
                    ["notebooklm", "ask", "-n", FIMIS_NOTEBOOK_ID, "-c", conv_id, followup_prompt],
                    capture_output=True,
                    text=True,
                    encoding="utf-8"
                )
                if res2.returncode == 0:
                    output2 = res2.stdout
                    answer2 = output2.split("Answer:", 1)[1] if "Answer:" in output2 else output2
                    answer2 = re.sub(r"\nConversation:.*$", "", answer2, flags=re.DOTALL)
                    answer = answer2

        answer = re.sub(r"\n(?:New )?conversation:.*$", "", answer, flags=re.DOTALL)
        return answer.strip()
    finally:
        if os.path.exists(temp_prompt_path):
            os.remove(temp_prompt_path)


def process_unit(unit_num: int):
    """Execute end-to-end PYQ generation for a single unit."""
    unit_info = UNITS[unit_num]
    unit_title = unit_info["title"]
    target_folder = REPO_ROOT / unit_info["folder"]
    target_folder.mkdir(parents=True, exist_ok=True)
    target_filename = f"fimis-unit{unit_num}-{unit_info['slug']}-pyq-bank.md"
    target_path = target_folder / target_filename

    print("\n" + "=" * 70)
    print(f"🚀 GENERATING FIMIS UNIT {unit_num} PYQ BANK: {unit_title}")
    print(f"   Target File: {unit_info['folder']}/{target_filename}")
    print("=" * 70)

    # 1. Build prompt
    prompt = build_pyq_prompt(unit_num, unit_info)
    print(f"📝 Prompt prepared ({len(prompt)} chars). Querying NotebookLM...")

    # 2. Query NotebookLM
    raw_markdown = execute_notebooklm_query(unit_num, prompt)
    if not raw_markdown or len(raw_markdown.strip()) < 500:
        print(f"❌ Failed to receive full response for Unit {unit_num} ({len(raw_markdown.strip()) if raw_markdown else 0} chars). Skipping.")
        return False

    # 3. Clean citations and format LaTeX
    print("🧹 Cleaning citation markers and formatting LaTeX...")
    cleaned_markdown = clean_markdown(raw_markdown)

    # 4. Save to repository
    target_path.write_text(cleaned_markdown.strip() + "\n", encoding="utf-8")
    lines_count = len(cleaned_markdown.splitlines())
    words_count = len(cleaned_markdown.split())
    print(f"💾 Saved {lines_count} lines ({words_count} words) to {target_path}")

    # 5. Git Commit
    print("📦 Staging and committing to Git...")
    try:
        subprocess.run(["git", "add", str(target_path)], check=True)
        commit_msg = f"docs(fimis): add Unit {unit_num} PYQ Bank - {unit_title} ({lines_count} lines)"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"✅ Committed Unit {unit_num} PYQ Bank successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git commit warning: {e}")
        return True


def main():
    units_to_run = [8, 10]
    if len(sys.argv) > 1:
        units_to_run = [int(x) for x in sys.argv[1:] if x.isdigit()]

    print(f"Starting sequential PYQ generation for Units: {units_to_run}")
    success_count = 0

    for u in units_to_run:
        ok = process_unit(u)
        if ok:
            success_count += 1

    # Final git push
    print("\n🚀 Pushing all completed PYQ banks to GitHub...")
    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🎉 Successfully pushed all changes to GitHub!")
    except Exception as e:
        print(f"Git push note: {e}")

    print("\n" + "=" * 70)
    print(f"🎉 COMPLETED {success_count}/{len(units_to_run)} UNITS SEQUENTIALLY!")
    print("=" * 70)


if __name__ == "__main__":
    main()
