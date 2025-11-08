from pathlib import Path
import csv
import json

ROOT = Path(r"F:\Personal\Project\design_research")
DISCOVER = ROOT / "discover"
OUT = ROOT / "outputs" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

out_file = OUT / "discover_normalized.jsonl"

def normalize_csv(path: Path, method: str):
    """
    Expected columns (case-insensitive):
      participant_id, role, date, text, study_id (optional)
    """
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                "study_id": row.get("study_id", path.stem),
                "source": method,
                "participant_id": row.get("participant_id", ""),
                "role": row.get("role", ""),
                "date": row.get("date", ""),
                "text": row.get("text", "").strip(),
            })
    return rows

def normalize_txt(path: Path, method: str):
    """
    Treat each line as one response (good for quick dumps).
    """
    rows = []
    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            text = line.strip()
            if not text:
                continue
            rows.append({
                "study_id": path.stem,
                "source": method,
                "participant_id": f"{path.stem}_L{i}",
                "role": "",
                "date": "",
                "text": text,
            })
    return rows

all_rows = []

# primary research (interviews, surveys)
for p in (DISCOVER / "primary_research").glob("*"):
    if p.suffix.lower() == ".csv":
        all_rows.extend(normalize_csv(p, "primary"))
    elif p.suffix.lower() == ".txt":
        all_rows.extend(normalize_txt(p, "primary"))

# secondary research (desk, analogous)
for p in (DISCOVER / "secondary_research").glob("*"):
    if p.suffix.lower() == ".csv":
        all_rows.extend(normalize_csv(p, "secondary"))
    elif p.suffix.lower() == ".txt":
        all_rows.extend(normalize_txt(p, "secondary"))

with out_file.open("w", encoding="utf-8") as f:
    for row in all_rows:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"Normalized {len(all_rows)} records → {out_file}")
