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
> `output/sample_chart.png` is included as a visual example. Your script run should generate/overwrite `output/chart.png`.

**Reflection (write 3–5 sentences)**
Replace this section with your own reflection:
- What was the hardest part?
  - Since the majority of the group members were familiar with the fundamentals of coding, creating the required outputs was not the difficult part. The challenging aspect was that one member's DATA100 instructor was different, which resulted in a minor difference in the repository they used. Additionally, when everyone in the group commits changes at the same time, working simultaneously inside the repository can be a little difficult.
- What did you learn about Git commits (small commits, staging, meaningful messages)?
  - We found that in order to prevent work overlap and unintentional changes, we must constantly communicate with one another as a group, especially when someone wants to make any adjustments, no matter how small.   
  
**Generative AI Disclosure (if applicable)**
- Tool used:
- What it was used for:
  - ...
  - ...
- What I personally verified/changed:
  - ...
  - ...
