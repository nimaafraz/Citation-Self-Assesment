Here's the complete `README.md` content for your GitHub repository, including:

* Instructions on generating the CSV report from Publish or Perish
* Tool description
* Detailed table of criteria with 90th/10th percentile logic
* Link to your LinkedIn article
* Note about the synthetic dataset

---

```markdown
# 🧠 Citation Metrics Self-Assessment Tool

This tool analyzes Google Scholar citation metrics exported via [Publish or Perish](https://harzing.com/resources/publish-or-perish) to flag potential patterns of manipulation, low individual contribution, or excessive reliance on inflated citation strategies.

---

## 📥 How to Get Your Metrics CSV from Google Scholar

1. Install the latest version of **Publish or Perish** from [harzing.com](https://harzing.com/resources/publish-or-perish).
2. Run a search using your **Google Scholar Profile**.
3. Once loaded, go to:  
   **File → Export → Export to CSV file**.
4. Save the file as `pop-metrics.csv` and place it in the same folder as this script.

> 📌 The `pop-metrics.csv` file currently in this repository is **synthetically generated** and should be **replaced** with real data from actual scholar profiles for accurate analysis.

![Placeholder for Publish or Perish Screenshot](https://via.placeholder.com/700x200.png?text=Insert+Screenshot+of+Export+from+Publish+or+Perish)

---

## 📊 What This Tool Does

This Python script:

- Detects citation manipulation or unethical trends (e.g. excessive co-authorship, inflated g-index, narrow collaboration circles).
- Compares each metric against **departmental norms** (using quantile-based thresholds).
- Flags suspicious values and explains **why** each is concerning.
- Prints the **top 3 researchers** for each “worst” metric to highlight outliers.

---

### 🎯 How the Percentile Flagging Works

- **90th Percentile** (`↑`): If your value is **higher than 90%** of peers, and high values are suspicious, it gets flagged.
- **10th Percentile** (`↓`): If your value is **lower than 90%** of peers, and low values are problematic, it gets flagged.

This **relative comparison** ensures fairness across disciplines and collaboration cultures.

---

### 📌 Red Flag Criteria Summary

| # | Criterion                     | Description                                                                 | Suspicious When...                | Percentile Used |
|---|-------------------------------|-----------------------------------------------------------------------------|-----------------------------------|------------------|
| 1 | `Authors_Paper`              | Average number of authors per paper                                         | Extremely high                    | 90th (↑)         |
| 2 | `hI_index / h_index`         | Individual h-index (co-authorship normalized)                               | Very low                          | 10th (↓)         |
| 3 | `hm_index / h_index`         | Harmonic h-index (more punishing to large author lists)                     | Very low                          | 10th (↓)         |
| 4 | `hA`                         | Authorship diversity: variety of co-authors                                 | Very low                          | 10th (↓)         |
| 5 | `g_index / h_index`          | High impact skew (g-index larger than h-index)                              | Extremely high                    | 90th (↑)         |
| 6 | `e_index / h_index`          | Excess citations in h-core beyond h²                                        | Extremely high                    | 90th (↑)         |
| 7 | `h_coverage`                 | % of citations concentrated in h-core                                       | Extremely high                    | 90th (↑)         |
| 8 | `g_coverage`                 | % of citations in top g papers                                              | Extremely high                    | 90th (↑)         |
| 9 | `star_count / Papers`       | Share of highly cited “blockbuster” papers                                  | Extremely high                    | 90th (↑)         |
|10 | `Cites_Author_Year`         | Citations per author per year                                               | Extremely high (self-citation?)   | 90th (↑)         |

---

## 📈 Sample Output

```

🔍 Analyzing: author7
⚠️ 1. Low hI/h ratio: 0.38 (10th percentile: 0.41) — Suggests low individual contribution.
⚠️ 2. High Authors\_Paper: 9.4 (90th percentile: 8.6) — May indicate inflated co-authorship.
⚠️ 3. Low hA (authorship diversity): 2.1 (10th percentile: 3.5) — Frequent repetition of same co-authors.
---------------------------------------------------------------------------------------------------------

```

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

