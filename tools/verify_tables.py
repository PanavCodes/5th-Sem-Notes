from pathlib import Path

def is_delim(s):
    s = s.strip()
    return s.startswith("|") and s.endswith("|") and "-" in s and len(s.replace("|", "").replace("-", "").replace(":", "").replace(" ", "")) == 0

for u in [5, 6, 7, 8, 9, 10]:
    for p in Path(f"FIMIS/Unit_{u}").glob("*pyq-bank*.md"):
        lines = p.read_text(encoding="utf-8").splitlines()
        print(f"\n=== UNIT {u}: {p.name} ===")
        table_count = 0
        for i, l in enumerate(lines):
            if is_delim(l):
                table_count += 1
                delim_cols = len([c for c in l.split("|")[1:-1]])
                header = lines[i-1]
                header_cols = len([c for c in header.split("|")[1:-1]])
                print(f"Table #{table_count} (line {i}): {delim_cols} cols | Header match: {header_cols == delim_cols}")
                # check all rows in this table
                row_idx = i + 1
                row_errs = 0
                while row_idx < len(lines):
                    r = lines[row_idx].strip()
                    if not r.startswith("|"):
                        break
                    row_cols = len([c for c in r.split("|")[1:-1]])
                    if row_cols != delim_cols:
                        row_errs += 1
                        print(f"  Row {row_idx} column mismatch: expected {delim_cols}, got {row_cols} -> {r[:60]}")
                    row_idx += 1
                if row_errs == 0:
                    print(f"  All {row_idx - i - 1} rows have exact {delim_cols} columns!")
