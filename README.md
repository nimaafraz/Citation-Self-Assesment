# Citation Metrics Self-Assessment Tool

**Is your h-index telling the truth—or just a beautiful lie?**  
This tool allows you to **analyze Google Scholar profiles** to detect red flags such as inflated co-authorship, self-citation patterns, and over-reliance on blockbuster papers.

🔗 **[LinkedIn explainer post](https://www.linkedin.com/posts/nimaafraz_is-your-h-index-telling-the-truth-or-just-activity-7347945048233136130-JXKY)**

---

## 📥 How to Export Your Google Scholar Report via *Publish or Perish*

1. Download and install [Publish or Perish](https://harzing.com/resources/publish-or-perish).
2. Open the application and go to the **Google Scholar Profile** tab.
3. Enter the researcher's profile ID (e.g., `qc6CJjYAAAAJ`) or search by name.
4. Click **Lookup** to fetch results.
5. Once the data loads, click **File → Export**.
6. Select **CSV (Comma-separated values)** and export the full report.

📸 *Sample screenshot goes here*  
(*Insert your own screenshot here as a placeholder showing the export button in Publish or Perish.*)

---

## 📊 What This Tool Does

- Detects **citation manipulation patterns** (e.g., low individual contribution, high author inflation).
- Compares each metric against department norms (based on quantiles).
- Flags concerning patterns and prints explanations.
- Lists the **top 3 most extreme cases** in each category.

---

## 🛠 How to Use

1. Clone this repository.
2. Replace the `pop-metrics.csv` file with your own export from Publish or Perish.
3. Run:

```bash
python analyze_citations.py
