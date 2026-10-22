"""Derive views/connections.md and check references. Run: python3 tools/build_connections.py"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
ids = set()
for f in (root / "sources").glob("*.md"):
    t = f.read_text()
    ids |= set(re.findall(r"^# ([A-Z]+-\d+):", t, re.M))
    ids |= set(re.findall(r"^(?:Account ID|Contact ID|Product ID|Capability ID): (\S+)", t, re.M))
rows, errors = [], []
for f in ("interpretations.md", "decisions.md"):
    for block in re.split(r"^## ", (root / "records" / f).read_text(), flags=re.M)[1:]:
        rid = block.split("\n")[0].strip()
        if not re.match(r"(INT|DEC)-\d+", rid):
            continue
        ev = re.search(r"^Evidence: (.*)$", block, re.M)
        rel = re.search(r"^Related: (.*)$", block, re.M)
        st = re.search(r"^Status: (.*)$", block, re.M)
        if not ev: errors.append(f"{rid}: no evidence")
        refs = [x.strip() for x in ((ev.group(1) if ev else "") + "," + (rel.group(1) if rel else "")).split(",") if x.strip()]
        for r in refs:
            if r not in ids and not re.match(r"(INT|DEC)-\d+", r):
                errors.append(f"{rid}: unknown reference {r}")
        rows.append((rid, st.group(1) if st else "?", ev.group(1) if ev else "", rel.group(1) if rel else ""))
out = ["# Connections (derived view; do not edit)", "", "| Record | Status | Evidence | Related |", "|---|---|---|---|"]
out += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
(root / "views" / "connections.md").write_text("\n".join(out) + "\n")
print("\n".join(errors) or "checks passed")
sys.exit(1 if errors else 0)
