# Design Research Pipeline Setup Guide

A full terminal-based installation and setup walkthrough for Windows 11.

---

## 0. Open PowerShell

1. Press **Start**, type `PowerShell`.
2. Open **Windows PowerShell** or **Windows Terminal (PowerShell)**.

All commands below are entered there.

---

## 1. Install Scoop (tool manager)

```powershell
# Allow local scripts (one-time)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Scoop
Invoke-Expression (New-Object Net.WebClient).DownloadString('https://get.scoop.sh')
```

Close and reopen PowerShell afterward.

---

## 2. Install Python with Scoop

```powershell
# Check Scoop works
scoop --version

# Install Python
scoop install python

# Confirm install
python --version
```

---

## 3. Install Ollama (local LLM runner)

Use Winget (built into Windows 11):

```powershell
winget install Ollama.Ollama
```

After install, close and reopen PowerShell, then:

```powershell
ollama --version

# Pull the model
ollama pull phi4:14b
```

---

## 4. Install Python libraries (Matplotlib + Scikit-Learn)

Try Scoop first, then pip as fallback:

```powershell
scoop search matplotlib
scoop search scikit-learn

# Install via pip (likely needed)
pip install matplotlib scikit-learn
```

---

## 5. Create the project folders

```powershell
# Go to your main project directory
cd F:\Personal\Project

# Create root folder
mkdir design_research
cd .\design_research

# Double Diamond structure
mkdir discover, define, develop, deliver, scripts, outputs

# Subfolders
mkdir .\discover\primary_research
mkdir .\discover\secondary_research
mkdir .\discover\clustered_topics

mkdir .\define\insights
mkdir .\define\themes
mkdir .\define\opportunities
mkdir .\define\redefined_briefs

mkdir .\develop\ideation
mkdir .\develop\evaluation
mkdir .\develop\prototypes

mkdir .\deliver\test_results
mkdir .\deliver\iterations
mkdir .\deliver\outcomes

mkdir .\outputs\processed
mkdir .\outputs\charts
```

---

## 6. Create script files

```powershell
cd .\scripts
New-Item ingest.py -ItemType File
New-Item run_pipeline.ps1 -ItemType File
cd ..
code .
```

This opens the project in **VS Code**.

---

## 7. Paste in the scripts

- Open `scripts/ingest.py` → paste your **ingest.py** code.  
- Open `scripts/run_pipeline.ps1` → paste your working **run_pipeline.ps1**.  
- Save both.

---

## 8. Add test data

```powershell
cd F:\Personal\Project\design_research
ni .\discover\primary_research\test_interview.txt -ItemType File
```

Open `test_interview.txt` and paste:

```
I struggled to find the export button on the dashboard.
The onboarding felt long, so I skipped it.
The visual design is nice, but the navigation labels are confusing.
```

Save.

---

## 9. Test ingest step

```powershell
cd F:\Personal\Project\design_research
python .\scripts\ingest.py
```

Expected output:

```
Normalized 3 records → F:\Personal\Project\design_research\outputs\processed\discover_normalized.jsonl
```

---

## 10. Run the full pipeline

```powershell
cd F:\Personal\Project\design_research
.\scripts\run_pipeline.ps1
```

You should see all stages complete successfully.

Outputs created:

```
outputs\processed\discover_normalized.jsonl
outputs\processed\discover_insights.md
outputs\charts\themes_bar_chart.py
```

---

## 11. Run chart

```powershell
cd F:\Personal\Project\design_research
python .\outputs\charts\themes_bar_chart.py
```

If it fails for missing libraries, install them using pip or Scoop.

---

## 12. Daily usage flow

When starting a new case study:

1. Add raw data into:

   ```text
   F:\Personal\Project\design_research\discover\primary_research\
   ```

2. Run pipeline:

   ```powershell
   cd F:\Personal\Project\design_research
   .\scripts\run_pipeline.ps1
   ```

3. Review outputs:
   - `outputs/processed/discover_insights.md` → open in VS Code for presentation
   - `outputs/charts/themes_bar_chart.py` → run for visuals

---

## ✅ Summary

This setup gives you a full **Double Diamond design research workflow** powered by:

- **Scoop** for dependency management  
- **Python** for ingestion and normalization  
- **Ollama + Phi‑4** for AI synthesis  
- **Matplotlib** for automatic visualization  

You can reproduce this on any Windows machine using only PowerShell and VS Code.
