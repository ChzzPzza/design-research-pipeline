# --- Design Research Pipeline (Phi-4 summary + chart code) ---

$root        = "F:\Personal\Project\design_research"
$normalized  = "$root\outputs\processed\discover_normalized.jsonl"
$insights    = "$root\outputs\processed\discover_insights.md"
$chartDir    = "$root\outputs\charts"
$chartScript = "$chartDir\themes_bar_chart.py"

cd $root

# 1) Ingest / normalize
Write-Host "`n[1/3] Normalizing raw research data..."
python "$root\scripts\ingest.py"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Ingest step failed. Check Python output." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $normalized)) {
    Write-Host "Expected file not found: $normalized" -ForegroundColor Red
    exit 1
}

Write-Host "Ingest complete."
Write-Host "   → $normalized"

# 2) Summarize insights with phi4 (markdown report)
Write-Host "`n[2/3] Summarizing insights with phi4..."

$prompt = @"
You are a senior design research analyst.

The data below is a JSONL list of records with fields like:
- study_id
- source (primary / secondary)
- participant_id
- role
- date
- text

Task:
1. Read all records and cluster them into 3–8 key themes.
2. For each theme, output:
   - Theme name
   - 1–2 sentence description
   - Approximate frequency (number of records)
   - 2–3 short representative quotes (paraphrase lightly if needed).
3. Add a final section called "Implications for design" with 3–6 bullets.

Return markdown only, in this structure:

## Themes

### [Theme Name]
- Description: ...
- Approx. frequency: N
- Quotes:
  - "..."
  - "..."

## Implications for design
- Bullet 1
- Bullet 2
- ...
"@

$data = Get-Content $normalized -Raw
$fullPrompt = $prompt + "`n`nDATA (JSONL records):`n" + $data

$fullPrompt | ollama run phi4:14b > $insights

if ($LASTEXITCODE -ne 0) {
    Write-Host "Summarization step failed. Check Ollama output." -ForegroundColor Red
    exit 1
}

Write-Host "Insights written to:"
Write-Host "   → $insights"

# 3) Generate Python bar-chart code with phi4
Write-Host "`n[3/3] Generating bar chart code with phi4..."

if (-not (Test-Path $chartDir)) {
    New-Item -ItemType Directory -Path $chartDir | Out-Null
}

$chartPrompt = @"
You are a Python and data visualization assistant.

You will be given a JSONL dataset of design research records with a 'text' field.

1. First, cluster the records into 3–8 themes based on the 'text' content.
2. Count how many records fall into each theme.
3. Write a complete Python script that:
   - imports matplotlib.pyplot as plt
   - defines two lists: 'themes' and 'counts'
   - fills them with your clustered theme names and counts
   - plots a horizontal bar chart of counts per theme
   - sets axis labels and a short title
   - calls plt.tight_layout() and plt.show()
4. Output ONLY valid Python code. No explanations, comments, or markdown.

Use short, human-readable theme names like "Onboarding friction", "Navigation confusion".
"@

$fullChartPrompt = $chartPrompt + "`n`nDATA (JSONL records):`n" + $data

$fullChartPrompt | ollama run phi4:14b > $chartScript

if ($LASTEXITCODE -ne 0) {
    Write-Host "Chart code generation step failed. Check Ollama output." -ForegroundColor Red
    exit 1
}

# Clean up any markdown fences and force UTF-8 encoding using .NET
$content = Get-Content $chartScript -Raw
$content = $content -replace '```python', '' -replace '```', ''
[System.IO.File]::WriteAllText($chartScript, $content, [System.Text.Encoding]::UTF8)

Write-Host "Chart script written to:"
Write-Host "   → $chartScript"
Write-Host "`nPipeline finished successfully.`n"
