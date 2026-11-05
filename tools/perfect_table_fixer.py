from pathlib import Path

def is_delim(s):
    s = s.strip()
    return s.startswith("|") and s.endswith("|") and "-" in s and len(s.replace("|", "").replace("-", "").replace(":", "").replace(" ", "")) == 0

def count_cols(s):
    return len([c for c in s.strip().split("|")[1:-1]])

def clean_header_merge(parts):
    joined = " ".join(parts).strip()
    tokens = [t.strip() for t in joined.split("|") if t.strip()]
    return "| " + " | ".join(tokens) + " |"

def repair_content(content: str) -> str:
    lines = content.splitlines()
    output = []
    in_code = False
    i = 0
    n = len(lines)
    
    while i < n:
        line = lines[i]
        s = line.strip()
        
        # Fenced code block check
        if s.startswith("```"):
            in_code = not in_code
            output.append(line)
            i += 1
            continue
            
        if in_code:
            output.append(line)
            i += 1
            continue
            
        # Check if line i is a delimiter
        if is_delim(s):
            num_cols = count_cols(s)
            
            # The header is immediately before delimiter (output[-1], output[-2], ...)
            header_parts = []
            while output:
                prev = output.pop()
                prev_s = prev.strip()
                if not prev_s:
                    continue
                header_parts.insert(0, prev_s)
                clean_h = clean_header_merge(header_parts)
                if count_cols(clean_h) >= num_cols:
                    break
                if prev_s.startswith("|") and any(k in clean_h.lower() for k in ["parameter", "topic", "concept", "rank", "slide", "priority", "rephrased", "question"]):
                    break
                    
            stitched_header = clean_header_merge(header_parts) if header_parts else "| Header |"
            output.append(stitched_header)
            output.append(s)
            i += 1
            
            # Now read data rows
            while i < n:
                cur = lines[i].strip()
                if not cur or cur.startswith("```") or cur.startswith("#") or cur.startswith("---"):
                    break
                if (cur.startswith("* ") or cur.startswith("> ")) and "|" not in cur:
                    break
                    
                row_buf = cur
                while i + 1 < n:
                    next_s = lines[i+1].strip()
                    if not next_s or next_s.startswith("```") or next_s.startswith("#") or next_s.startswith("---"):
                        break
                    if row_buf.startswith("|") and row_buf.endswith("|") and count_cols(row_buf) >= num_cols:
                        break
                    if next_s.startswith("|") and row_buf.startswith("|") and row_buf.endswith("|"):
                        break
                    row_buf = row_buf + " " + next_s
                    i += 1
                    
                output.append(row_buf)
                i += 1
            continue
            
        output.append(line)
        i += 1
        
    return "\n".join(output) + "\n"

# Process all Units 5 through 10
for u in [5, 6, 7, 8, 9, 10]:
    for p in Path(f"FIMIS/Unit_{u}").glob("*pyq-bank*.md"):
        orig = p.read_text(encoding="utf-8")
        repaired = repair_content(orig)
        p.write_text(repaired, encoding="utf-8")
        print(f"Unit {u} ({p.name}): repaired tables successfully.")
