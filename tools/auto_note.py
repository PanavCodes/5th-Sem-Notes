#!/usr/bin/env python3
"""
End-to-End Automated Note & PYQ Generation Engine via NotebookLM
Workflow:
  1. Slide Deck Analysis (extracts topics, exact formulas/numbers from PPTX/PDF)
  2. Applies Domain-Calibrated Master Meta-Prompt (Study Notes or PYQ Bank)
  3. Queries NotebookLM directly using your authenticated Google account & course notebook
  4. Formats & saves the generated Markdown in standard <Subject>/Unit_<X>/ directory
  5. Updates README.md (Exam Timetable & Subject Matrix)
  6. Commits and pushes automatically to GitHub
"""

import os
import sys
import re
import json
import argparse
import tempfile
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SUBJECTS = {
    "AI": {
        "name": "Artificial Intelligence",
        "code": "702CO0C076",
        "default_folder": "AI",
        "notebook_match": "Artificial Intelligence",
        "domain": "ALGORITHMIC, MATH & VISION",
    },
    "IVP": {
        "name": "Image and Video Processing",
        "code": "702EX0E020",
        "default_folder": "IVP",
        "notebook_match": "IVP",
        "domain": "ALGORITHMIC, MATH & VISION",
    },
    "OS": {
        "name": "Operating Systems",
        "code": "702CO0C056",
        "default_folder": "OS",
        "notebook_match": "OS",
        "domain": "TECHNICAL & SYSTEMS",
    },
    "SE": {
        "name": "Software Engineering",
        "code": "702IT0C041",
        "default_folder": "SE",
        "notebook_match": "Software Engineering",
        "domain": "TECHNICAL & SYSTEMS",
    },
    "5G": {
        "name": "5G for Everyone",
        "code": "Open Elective",
        "default_folder": "5G",
        "notebook_match": "5G",
        "domain": "TECHNICAL & SYSTEMS",
    },
    "FIMIS": {
        "name": "Financial Inst., Markets, Instruments & Services (FIMIS)",
        "code": "702TF0I001",
        "default_folder": "FIMIS",
        "notebook_match": "FIMIS",
        "domain": "THEORY, GOVERNANCE & FINANCE",
    },
    "IFS": {
        "name": "Introduction to Forensic Science (IFS)",
        "code": "Open Elective",
        "default_folder": "IFS",
        "notebook_match": "IFS",
        "domain": "THEORY, GOVERNANCE & FINANCE",
    },
    "ARVR": {
        "name": "Intro to Virtual Reality & Augmented Reality",
        "code": "Open Elective",
        "default_folder": "ARVR",
        "notebook_match": "ARVR",
        "domain": "INTERACTIVE & APPLIED GRAPHICS",
    },
}


def clean_citations(text: str) -> str:
    """Remove NotebookLM reference citations like [38], [244, 245]."""
    return re.sub(r"[ \t]*\[\d+(?:[,\s]+\d+)*\]", "", text)


def slugify(text: str) -> str:
    """Turn title into kebab-case filename slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")


def extract_slide_info(slide_path: Path):
    """Extract slide titles, bullet points, formulas, and slide count from PPTX or PDF."""
    ext = slide_path.suffix.lower()
    slide_data = []

    if ext == ".pptx":
        try:
            from pptx import Presentation
            prs = Presentation(slide_path)
            for idx, slide in enumerate(prs.slides, start=1):
                texts = []
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        for para in shape.text_frame.paragraphs:
                            t = para.text.strip()
                            if t and t not in texts:
                                texts.append(t)
                slide_data.append((idx, texts))
        except Exception as e:
            print(f"Warning: Failed to parse PPTX with python-pptx: {e}")
    elif ext == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(slide_path)
            for idx, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""
                lines = [l.strip() for l in text.splitlines() if l.strip()]
                slide_data.append((idx, lines))
        except Exception as e:
            print(f"Warning: Failed to parse PDF with pypdf: {e}")

    return slide_data


def summarize_slide_topics(slide_data):
    """Summarize slide contents into topic points and numerical hints."""
    if not slide_data:
        return "Cover all topics present in the uploaded slide deck thoroughly."

    slide_count = len(slide_data)
    headings = []
    content_snippets = []

    for idx, lines in slide_data:
        if not lines:
            continue
        first_line = lines[0]
        if len(first_line) < 80 and not any(h == first_line for h in headings):
            headings.append(first_line)
        for line in lines[1:5]:
            if any(num_kw in line.lower() for num_kw in ["formula", "₹", "rate", "cost", "calculation", "rs.", "tax", "%"]):
                content_snippets.append(line)

    summary_lines = [f"- Total Slides in Deck: {slide_count}"]
    if headings:
        summary_lines.append("- Core Slide Topics Extracted:")
        for h in headings[:12]:
            summary_lines.append(f"  • {h}")
    if content_snippets:
        summary_lines.append("- Slide Numerical Parameters / Formulas Detected:")
        for c in content_snippets[:6]:
            summary_lines.append(f"  • {c}")

    return "\n".join(summary_lines)


def get_notebook_id(subject_code: str) -> str:
    """Find the NotebookLM notebook ID matching the subject."""
    info = SUBJECTS.get(subject_code, {})
    match_term = info.get("notebook_match", subject_code).lower()

    try:
        res = subprocess.run(
            ["notebooklm", "list"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True
        )
        lines = res.stdout.splitlines()
        for line in lines:
            if "|" in line:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 4:
                    nb_id, title = parts[1], parts[2]
                    if match_term in title.lower() or subject_code.lower() in title.lower():
                        return nb_id
    except Exception as e:
        print(f"Error querying notebook list: {e}")

    return None


def construct_prompt(subject_code: str, unit_num: str, doc_type: str, slide_path: Path = None, title: str = None) -> str:
    """Build the final optimized prompt to send to NotebookLM."""
    info = SUBJECTS[subject_code]
    subject_name = info["name"]
    domain = info["domain"]
    unit_title = title or f"Unit {unit_num}"
    slide_filename = slide_path.name if slide_path else f"Unit {unit_num} Slides"

    slide_summary = ""
    if slide_path and slide_path.exists():
        slide_data = extract_slide_info(slide_path)
        slide_summary = summarize_slide_topics(slide_data)

    slug_title = slugify(unit_title)
    type_suffix = "study-notes" if doc_type == "notes" else "pyq-bank"
    target_filename = f"{subject_code.lower()}-unit{unit_num}-{slug_title}-{type_suffix}.md"

    if doc_type == "notes":
        prompt = f"""Create a comprehensive study-notes Markdown file `{target_filename}` for **{subject_name} - Unit {unit_num}: {unit_title}** using the uploaded slides (`{slide_filename}`) as the PRIMARY and authoritative syllabus anchor, and textbooks strictly for 5-mark and 10-mark depth.

### EXAM SCOPE & SLIDE TOPICS TO COVER
{slide_summary}
Cover EVERY single concept, model, and slide thoroughly. Do not truncate, skip, or summarize superficially.

### DOMAIN SPECIFICATIONS: [{domain}]
- For {subject_name}, strictly follow the {domain} profile:
  * Theoretical Clarity & Formal Academic Definitions
  * Operational Mechanics & Step-by-Step Workflows / Text or Mermaid Architecture Diagrams
  * Complete worked mathematical calculations and derivations in LaTeX ($...$ and $$...$$) where applicable from the slides.
  * Real-World Institutional / Corporate / System Case Studies.
  * Topic Markers for Revision: ⭐ **Must Remember**, 🧠 **Must Understand**, ⚠️ **Common Exam Pitfalls**.

### DUAL EXAM SCAFFOLDING (5-MARK & 10-MARK)
For EVERY core topic in this Unit, construct two distinct sections:
- ✍️ **5-Mark Quick Shot (7-min write-up)**: Precise definition, 4–5 core technical bullets, and 1 compact summary artifact (3-column comparison table, ASCII workflow, or formula box).
- 📚 **10-Mark Blueprint (15-min essay)**: Exhaustive theoretical mechanics, end-to-end procedural workflows, multi-variable comparison tables (5+ parameters), and complete real-world case study or numerical solution.

### REVISION AUDIT & FORMULAS
Conclude with:
1. Master Formula & Definition Reference Sheet.
2. Corporate Case / Architecture Summary Table.
3. Slide Coverage Audit marking every slide in `{slide_filename}` as Fully Covered.
Formatting: Strictly GitHub Markdown with standard LaTeX ($...$, $$...$$)."""

    else: # pyq
        prompt = f"""Create a comprehensive Markdown file `{target_filename}` containing an exam-oriented, solved Previous-Year Question (PYQ) Bank for **{subject_name} - Unit {unit_num}: {unit_title}**.

### 1. AUTHORITATIVE SCOPE & PRIMARY SOURCE
- **Authoritative Anchor**: `{slide_filename}` is the SOLE syllabus boundary. Cover only topics present in these slides. Discard any PYQs from other units or unlisted topics.
- **Source Documents**: Extract PYQs from all uploaded past examination papers. Use reference textbooks strictly to flesh out complete, high-scoring model answers.

### 2. SYLLABUS SCOPE
{slide_summary}

### 3. DOMAIN INSTRUCTIONS: [{domain}]
- Apply domain guidelines for {subject_name}:
  * Detailed statutory/regulatory frameworks or system architecture schemas.
  * Rigorous GitHub LaTeX ($...$ and $$...$$) for all derivations and numerical traces.
  * Complete 4-part real-world cases or ASCII workflows where helpful.

### 4. PYQ EXTRACTION, GROUPING & DEDUPLICATION RULES
- Scan ALL uploaded exam papers for questions matching this unit.
- **Semantic Grouping**: Group questions testing the exact same core concept under a single primary heading.
- For EVERY question inside a group, list:
  * *Exact Question String* | *Exam/Paper Name* | *Year* | *Q. Number* | *Marks*
- Provide **ONE definitive, comprehensive model answer** per group scaled to the highest mark allocation.
- Tag & Draw Diagrams: `📊 Diagram Required: YES | Type: [...] | Exam Sketch Target: [...]`. Immediately beneath this tag, draw the **complete, self-contained ASCII box-and-arrow diagram or Mermaid flowchart** to sketch in the exam hall. Never leave it as an external reference.

### 5. MARK-PROPORTIONAL ANSWER FORMATTING
- **2 Marks**: Formal definition + 2 core bullet points.
- **3–4 Marks**: Precise explanation + key traits/equations + example.
- **5 Marks (Quick Shot)**: Formal definition + 4–5 structured points + 3-column summary table or minimal ASCII workflow.
- **10 Marks (Blueprint)**: Theoretical foundation + end-to-end operational workflow + exhaustive multi-variable comparison table + deep case study.
- Difference questions MUST be answered using a structured Markdown comparison table.

### 6. ANALYTICAL APPENDIX
Conclude with:
1. Topic-Wise Frequency Table (ranked by repetition).
2. Concept Redundancy Map across past years.
3. Question Priority Matrix: 🔥 Very Important (≥3 times), ⭐ Important (1–2 times), 🟡 Moderate Priority.
4. Slide Coverage Audit against past exam papers.

Formatting: Clean GitHub Markdown with standard LaTeX ($...$, $$...$$)."""

    return prompt, target_filename


def ask_notebooklm(notebook_id: str, prompt_text: str) -> str:
    """Send prompt to NotebookLM via CLI and return the answer."""
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt", encoding="utf-8") as f:
        f.write(prompt_text)
        temp_prompt_path = f.name

    try:
        print("🧠 Querying NotebookLM (synthesizing across your uploaded textbooks, slides & PYQs)...")
        print("   (This typically takes 30-60 seconds for an exhaustive 800-line document)...")
        res = subprocess.run(
            ["notebooklm", "ask", "-n", notebook_id, "--prompt-file", temp_prompt_path, "--new", "--yes"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if res.returncode != 0:
            print(f"Error querying NotebookLM: {res.stderr}")
            return ""

        output = res.stdout
        # Extract Answer body after "Answer:" marker
        if "Answer:" in output:
            answer = output.split("Answer:", 1)[1]
            # Strip trailing "Resumed conversation:" or session markers
            answer = re.sub(r"\nResumed conversation:.*$", "", answer, flags=re.DOTALL)
            return answer.strip()
        return output.strip()
    finally:
        if os.path.exists(temp_prompt_path):
            os.remove(temp_prompt_path)


def find_or_create_unit_dir(subject_code: str, unit_num: str) -> Path:
    """Find existing unit directory or create standard one."""
    subject_dir = REPO_ROOT / SUBJECTS[subject_code]["default_folder"]
    subject_dir.mkdir(parents=True, exist_ok=True)

    for candidate in subject_dir.iterdir():
        if candidate.is_dir():
            m = re.search(r"Unit[_\-]?([0-9]+)", candidate.name, re.IGNORECASE)
            if m and m.group(1) == str(unit_num):
                return candidate

    new_dir = subject_dir / f"Unit-{unit_num}"
    new_dir.mkdir(parents=True, exist_ok=True)
    return new_dir


def update_readme(subject_code: str, unit_num: str, rel_path: Path, doc_type: str):
    """Update README.md with link and updated Units Ready count."""
    readme_path = REPO_ROOT / "README.md"
    if not readme_path.exists():
        return

    content = readme_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    type_label = "Notes" if doc_type == "notes" else "PYQs"
    clean_title = f"Unit {unit_num} {type_label}"
    markdown_link = f"[{clean_title}](./{rel_path.as_posix()})"

    updated = False
    new_lines = []

    for line in lines:
        if f"({subject_code})" in line or (f"**{subject_code}**" in line and "|" in line):
            if rel_path.as_posix() not in line:
                parts = line.split("|")
                if len(parts) >= 5:
                    material_col = parts[4].strip()
                    if material_col and material_col not in ["*(Curriculum tracked)*", "*(In Progress)*"]:
                        material_col += f" • {markdown_link}"
                    else:
                        material_col = markdown_link
                    parts[4] = f" {material_col} "
                    line = "|".join(parts)
                    updated = True
        new_lines.append(line)

    matrix_lines = []
    for line in new_lines:
        if line.startswith(f"| [`/{subject_code}`]"):
            parts = line.split("|")
            if len(parts) >= 5:
                units_cell = parts[3].strip()
                existing_units = [u.strip() for u in units_cell.split(",") if u.strip().isdigit()]
                if unit_num not in existing_units:
                    existing_units.append(str(unit_num))
                    existing_units.sort(key=int)
                    parts[3] = f" {', '.join(existing_units)} "
                    line = "|".join(parts)
                    updated = True
        matrix_lines.append(line)

    if updated:
        readme_path.write_text("\n".join(matrix_lines) + "\n", encoding="utf-8")
        print(f"📖 README.md successfully updated with link: {markdown_link}")


def main():
    parser = argparse.ArgumentParser(description="Auto Note & PYQ Generation Engine via NotebookLM")
    parser.add_argument("--subject", "-s", required=True, help="Subject code (e.g. FIMIS, AI, OS, SE, ARVR)")
    parser.add_argument("--unit", "-u", required=True, help="Unit number (e.g. 8, 9, 2)")
    parser.add_argument("--type", "-t", choices=["notes", "pyq"], default="notes", help="Document type")
    parser.add_argument("--slide", "-f", help="Path to slide PPTX or PDF file")
    parser.add_argument("--title", help="Unit Title override (e.g. 'Equipment Leasing & Hire Purchase')")
    parser.add_argument("--clean-citations", action="store_true", help="Remove NotebookLM [1], [24] citation brackets")
    parser.add_argument("--no-push", action="store_true", help="Save file locally without pushing to GitHub")
    args = parser.parse_args()

    subject = args.subject.upper()
    if subject not in SUBJECTS:
        print(f"Error: Unknown subject '{subject}'. Supported: {', '.join(SUBJECTS.keys())}")
        return

    # 1. Match Notebook
    notebook_id = get_notebook_id(subject)
    if not notebook_id:
        print(f"Error: No NotebookLM notebook found matching subject '{subject}'.")
        print("Run 'notebooklm list' to inspect your available notebooks.")
        return
    print(f"🔗 Connected to Notebook: {subject} ({notebook_id})")

    # 2. Slide path
    slide_path = Path(args.slide) if args.slide else None
    if slide_path and not slide_path.exists():
        print(f"Warning: Slide file not found at '{slide_path}'. Proceeding with unit syllabus prompt.")
        slide_path = None

    # 3. Construct Prompt
    prompt_text, filename = construct_prompt(subject, args.unit, args.type, slide_path, args.title)
    print(f"📝 Prompt prepared for Unit {args.unit} ({args.type.upper()}).")

    # 4. Query NotebookLM
    raw_markdown = ask_notebooklm(notebook_id, prompt_text)
    if not raw_markdown or len(raw_markdown.strip()) < 100:
        print("Error: Received empty or very short response from NotebookLM.")
        return

    print(f"✅ Generated {len(raw_markdown.splitlines())} lines ({len(raw_markdown.split())} words) of content.")

    # 5. Clean citations if requested
    if args.clean_citations:
        print("🧹 Cleaning NotebookLM citation brackets [x]...")
        raw_markdown = clean_citations(raw_markdown)

    # 6. Save to Repo
    unit_dir = find_or_create_unit_dir(subject, args.unit)
    target_path = unit_dir / filename
    target_path.write_text(raw_markdown.strip() + "\n", encoding="utf-8")
    rel_path = target_path.relative_to(REPO_ROOT)
    print(f"💾 File saved to: {rel_path.as_posix()}")

    # 7. Update README
    update_readme(subject, args.unit, rel_path, args.type)

    # 8. Push to GitHub
    if args.no_push:
        print("Skipping Git operations (--no-push passed).")
        return

    print("\n🚀 Committing and pushing to GitHub...")
    try:
        subprocess.run(["git", "add", str(rel_path), "README.md"], check=True)
        commit_msg = f"docs({subject.lower()}): add Unit {args.unit} {args.type} - {args.title or ('Unit ' + str(args.unit))}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\n" + "=" * 60)
        print("🎉 SUCCESS: Entire workflow completed end-to-end!")
        print(f"   URL: https://github.com/PanavCodes/5th-Sem-Notes/blob/main/{rel_path.as_posix()}")
        print("=" * 60)
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")


if __name__ == "__main__":
    main()

