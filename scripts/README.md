# Design Research Pipeline Documentation

## 🧭 Overview

**Goal:**  
A repeatable, terminal-driven system that:
1. Ingests qualitative research data (interviews, surveys, etc.)
2. Normalizes it into consistent JSONL format  
3. Summarizes insights with an open-weight reasoning model (Phi-4)  
4. Generates optional charts automatically (Matplotlib-based)
5. Outputs clean, presentation-ready artifacts (Markdown + Python chart)

---

## 📁 Directory Structure

```
design_research/
├── discover/
│   ├── primary_research/
│   ├── secondary_research/
│   └── clustered_topics/
├── define/
│   ├── insights/
│   ├── themes/
│   ├── opportunities/
│   └── redefined_briefs/
├── develop/
│   ├── ideation/
│   ├── evaluation/
│   └── prototypes/
├── deliver/
│   ├── test_results/
│   ├── iterations/
│   └── outcomes/
├── scripts/
│   ├── ingest.py
│   └── run_pipeline.ps1
└── outputs/
    ├── processed/
    │   ├── discover_normalized.jsonl
    │   ├── discover_insights.md
    └── charts/
        └── themes_bar_chart.py
```

---

## ⚙️ Pipeline Summary

### 1️⃣ `ingest.py`
Normalizes all raw research files in `/discover` into a unified structure.

**Supported input formats**
- `.csv` with headers (`participant_id`, `role`, `date`, `text`)
- `.txt` (each line = one response)

**Output**
`outputs/processed/discover_normalized.jsonl`

**Run manually**
```powershell
cd F:\Personal\Project\design_research
python .\scripts\ingest.py
```

---

### 2️⃣ `run_pipeline.ps1`
Automates the full process.

**Core steps**
1. Ingest normalization (`ingest.py`)
2. Summarize insights with Phi-4 (`ollama run phi4:14b`)
3. Generate a chart script from the same dataset (Matplotlib)
4. Auto-clean encoding and Markdown fences

**Run**
```powershell
cd F:\Personal\Project\design_research
.\scripts\run_pipeline.ps1
```

**Output**
- `discover_normalized.jsonl` — normalized source data  
- `discover_insights.md` — Phi-4 markdown summary (themes + implications)  
- `themes_bar_chart.py` — auto-generated chart script  

---

### 3️⃣ Run chart

```powershell
python .\outputs\charts\themes_bar_chart.py
```

If encoding or backtick issues appear, the pipeline now cleans those automatically.

---

## 🧩 Installed Components

| Tool | Installed via | Purpose |
|------|----------------|----------|
| **Ollama** | Manual install | Run local LLMs (Phi-4 Reasoning, etc.) |
| **Python** | Scoop | Main scripting environment |
| **Matplotlib** | pip | Chart visualization |
| **Scikit-Learn** | pip | Optional clustering support |
| **Scoop** | Core package manager | Manages tools like Python, Git, etc. |

---

## 💡 Usage Flow

1. Drop transcripts or survey CSVs into:  
   `discover/primary_research/`
2. Run:
   ```powershell
   .\scripts\run_pipeline.ps1
   ```
3. View outputs:
   - `outputs/processed/discover_insights.md` → open in VS Code for presentation use  
   - `outputs/charts/themes_bar_chart.py` → run to visualize results  

---

## 🧠 Model Stack

| Phase | Model | Function |
|--------|--------|-----------|
| Normalization | — | Python script only |
| Insight synthesis | `phi4:14b` | Reasoning & clustering themes |
| Chart code generation | `phi4:14b` | Generates matplotlib code |
| (Future) Embeddings | `nomic-embed-text` | Clustering & semantic search (when supported) |

---

## ⚙️ System Rules

- Always **Scoop-install** tools first (`scoop install python`, etc.)  
- Use **pip** only for Python-specific libraries (e.g., matplotlib, scikit-learn)  
- Keep scripts UTF-8 encoded  
- Run from terminal with explicit `cd` into the project root

---

## 🧩 Next Steps

- Add embeddings back once Ollama updates CLI support (`ollama embed`).  
- Extend the pipeline with sentiment charts, word clouds, or cross-case synthesis.  
- Add a `spip` helper to automatically check Scoop before pip for new packages.
