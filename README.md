# Week 1 Python Git Lab 

**Dataset chosen:** 
> Flights  https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv  
> Recommended columns: `month` (category), `passengers` (numeric)

**How to run**
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
pip install pandas matplotlib
pip freeze > requirements.txt
python analyze.py
```

**What it does**
- Prints dataset summary (rows/cols, columns list, first 5 rows, grouped averages)
- Generates `output/chart.png`

**Example output**
`output/sample_chart.png` is included as a visual example. Your script run should generate/overwrite `output/chart.png`.

**Reflection (write 3–5 sentences)**
Replace this section with your own reflection:
- What was the hardest part?
- What did you learn about Git commits (small commits, staging, meaningful messages)?

**Generative AI Disclosure (if applicable)**
- Tool used:
- What it was used for:
  - ...
  - ...
- What I personally verified/changed:
  - ...
  - ...
