# 🧠 Citation Metrics Self-Assessment Tool

This tool analyzes Google Scholar citation metrics exported via [Publish or Perish](https://harzing.com/resources/publish-or-perish) to flag potential patterns of:
- Citation manipulation
- Low individual contribution
- Excessive reliance on inflated citation strategies

---

## 📥 How to Get Your Metrics CSV from Google Scholar

1. Install the latest version of **Publish or Perish** from [harzing.com](https://harzing.com/resources/publish-or-perish)
2. Run a search using your **Google Scholar Profile ID**
3. Once loaded, go to:  
   **File → Export → Export to CSV file**
4. Save the file as `pop-metrics.csv` in the same folder as this script

> ⚠️ **Important:** The included `pop-metrics.csv` is **synthetically generated** for demonstration. Replace it with your real data for accurate analysis.

![Publish or Perish Export Example](https://via.placeholder.com/700x200.png?text=Screenshot+of+CSV+Export+in+Publish+or+Perish)

---

## 📊 Tool Functionality

This Python script:

✔️ Detects potential citation manipulation patterns  
✔️ Benchmarks metrics against **departmental norms**  
✔️ Flags suspicious values with explanations  
✔️ Highlights top 3 outliers per metric  

---

## 🎯 Percentile-Based Flagging System

- **🔴 Red Flag (↑)** = Above 90th percentile (where high values are suspicious)
- **🟡 Warning (↓)** = Below 10th percentile (where low values are problematic)

---

## 📌 Analysis Criteria

| # | Metric                | Description                          | Suspicious Direction | Percentile | Rationale |
|---|-----------------------|--------------------------------------|----------------------|------------|-----------|
| 1 | `Authors_Paper`       | Avg. authors per paper               | High (↑)             | 90th       | Inflated co-authorship |
| 2 | `hI_index/h_index`    | Individual contribution index        | Low (↓)              | 10th       | Low personal input |
| 3 | `hm_index/h_index`    | Harmonic mean h-index                | Low (↓)              | 10th       | Dominant co-authors |
| 4 | `hA`                  | Author diversity                     | Low (↓)              | 10th       | Narrow collaboration |
| 5 | `g_index/h_index`     | High-impact skew                     | High (↑)             | 90th       | Citation stacking |
| 6 | `e_index/h_index`     | Excess citations beyond h²           | High (↑)             | 90th       | Artificial boosting |
| 7 | `h_coverage`          | % citations in h-core                | High (↑)             | 90th       | Concentrated impact |
| 8 | `g_coverage`          | % citations in top g papers          | High (↑)             | 90th       | "Blockbuster" dependence |
| 9 | `star_count/Papers`   | Share of highly cited papers         | High (↑)             | 90th       | Selective promotion |
|10 | `Cites_Author_Year`   | Citations per author per year        | High (↑)             | 90th       | Possible self-citation |

---

## 📈 Sample Output

```plaintext
🔍 Analyzing: author7
⚠️ 1. Low hI/h ratio: 0.38 (10th percentile: 0.41) — Suggests low individual contribution
⚠️ 2. High Authors_Paper: 9.4 (90th percentile: 8.6) — Potential inflated co-authorship
⚠️ 3. Low hA: 2.1 (10th percentile: 3.5) — Limited co-author diversity
-----------------------------------------------------------------------

---

## 🔗 Learn More

🧵 [Read the LinkedIn post that inspired this project](https://www.linkedin.com/posts/nimaafraz_is-your-h-index-telling-the-truth-or-just-activity-7347945048233136130-JXKY)

---

## 🛠️ Requirements

- Python 3.x
- Standard libraries: `csv`, `statistics`

---

## 📎 File Structure

```

📁 your-repo/
├── pop-metrics.csv         # Replace this with real output from Publish or Perish
├── citation\_selfcheck.py   # Python script
├── README.md               # You're here

```

---

## 📬 Feedback & Contributions

Open to feedback and PRs — especially for improvements on percentile estimation, graphical summaries, or integration with APIs like Semantic Scholar or OpenAlex.

---

© 2025 [Nima Afraz](https://www.nima.ie) · Released under the MIT License
```

