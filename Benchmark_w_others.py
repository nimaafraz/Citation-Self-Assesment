import csv
import statistics

def calculate_department_norms(csv_file):
    """Calculate department averages and percentiles for key metrics"""
    with open(csv_file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    numeric_fields = [
        'Authors_Paper', 'Papers_Author', 'h_index', 'hI_index', 'hI_norm', 'hm_index', 'hA',
        'g_index', 'e_index', 'h_coverage', 'g_coverage', 'star_count',
        'Cites_Author', 'Cites_Author_Year', 'Papers'
    ]

    for row in data:
        for field in numeric_fields:
            try:
                row[field] = float(row[field])
            except (ValueError, TypeError, KeyError):
                row[field] = 0.0

    def safe_quantile(values, q_index):
        if len(values) > 1:
            return statistics.quantiles(values, n=10)[q_index]
        return 0.0

    norms = {
        'avg_authors_per_paper': statistics.mean([row['Authors_Paper'] for row in data]),
        'p90_authors_per_paper': safe_quantile([row['Authors_Paper'] for row in data], 8),

        'avg_hI_ratio': statistics.mean([row['hI_index']/row['h_index'] for row in data if row['h_index'] > 0]),
        'p10_hI_ratio': safe_quantile([row['hI_index']/row['h_index'] for row in data if row['h_index'] > 0], 0),

        'avg_hm_ratio': statistics.mean([row['hm_index']/row['h_index'] for row in data if row['h_index'] > 0]),
        'p10_hm_ratio': safe_quantile([row['hm_index']/row['h_index'] for row in data if row['h_index'] > 0], 0),

        'avg_g_ratio': statistics.mean([row['g_index']/row['h_index'] for row in data if row['h_index'] > 0]),
        'p90_g_ratio': safe_quantile([row['g_index']/row['h_index'] for row in data if row['h_index'] > 0], 8),

        'avg_e_ratio': statistics.mean([row['e_index']/row['h_index'] for row in data if row['h_index'] > 0]),
        'p90_e_ratio': safe_quantile([row['e_index']/row['h_index'] for row in data if row['h_index'] > 0], 8),

        'avg_h_coverage': statistics.mean([row['h_coverage'] for row in data]),
        'p90_h_coverage': safe_quantile([row['h_coverage'] for row in data], 8),

        'avg_g_coverage': statistics.mean([row['g_coverage'] for row in data]),
        'p90_g_coverage': safe_quantile([row['g_coverage'] for row in data], 8),

        'avg_cites_author_year': statistics.mean([row['Cites_Author_Year'] for row in data]),
        'p90_cites_author_year': safe_quantile([row['Cites_Author_Year'] for row in data], 8),

        'avg_hA': statistics.mean([row['hA'] for row in data]),
        'p10_hA': safe_quantile([row['hA'] for row in data], 0),

        'avg_star_ratio': statistics.mean([row['star_count']/row['Papers'] for row in data if row['Papers'] > 0]),
        'p90_star_ratio': safe_quantile([row['star_count']/row['Papers'] for row in data if row['Papers'] > 0], 8)
    }
    
    return norms, data

def analyze_profile(row, norms):
    flags = []
    h_index = row['h_index'] if row['h_index'] > 0 else 1

    if row['Authors_Paper'] > norms['p90_authors_per_paper']:
        flags.append(f"High Authors_Paper: {row['Authors_Paper']:.1f} (90th percentile: {norms['p90_authors_per_paper']:.1f}) — May indicate inflated co-authorship.")

    hI_ratio = row['hI_index'] / h_index
    if hI_ratio < norms['p10_hI_ratio']:
        flags.append(f"Low hI/h ratio: {hI_ratio:.2f} (10th percentile: {norms['p10_hI_ratio']:.2f}) — Suggests low individual contribution.")

    hm_ratio = row['hm_index'] / h_index
    if hm_ratio < norms['p10_hm_ratio']:
        flags.append(f"Low hm/h ratio: {hm_ratio:.2f} (10th percentile: {norms['p10_hm_ratio']:.2f}) — Co-authorship heavily dilutes contribution.")

    if row['hA'] < norms['p10_hA']:
        flags.append(f"Low hA (authorship diversity): {row['hA']:.1f} (10th percentile: {norms['p10_hA']:.1f}) — Frequent repetition of same co-authors.")

    g_ratio = row['g_index'] / h_index
    if g_ratio > norms['p90_g_ratio']:
        flags.append(f"High g/h ratio: {g_ratio:.2f} (90th percentile: {norms['p90_g_ratio']:.2f}) — Suggests few highly cited papers skew impact.")

    e_ratio = row['e_index'] / h_index
    if e_ratio > norms['p90_e_ratio']:
        flags.append(f"High e/h ratio: {e_ratio:.2f} (90th percentile: {norms['p90_e_ratio']:.2f}) — Indicates uneven distribution in h-core.")

    if row['h_coverage'] > norms['p90_h_coverage']:
        flags.append(f"High h_coverage: {row['h_coverage']:.1f}% (90th percentile: {norms['p90_h_coverage']:.1f}%) — Citations highly concentrated in h-core.")

    if row['g_coverage'] > norms['p90_g_coverage']:
        flags.append(f"High g_coverage: {row['g_coverage']:.1f}% (90th percentile: {norms['p90_g_coverage']:.1f}%) — Impact clustered in top g papers.")

    if row['Papers'] > 0:
        star_ratio = row['star_count'] / row['Papers']
        if star_ratio > norms['p90_star_ratio']:
            flags.append(f"High Star Paper Ratio: {star_ratio:.2f} (90th percentile: {norms['p90_star_ratio']:.2f}) — Reliance on few 'blockbuster' papers.")

    if row['Cites_Author_Year'] > norms['p90_cites_author_year']:
        flags.append(f"High Cites/Author/Year: {row['Cites_Author_Year']:.2f} (90th percentile: {norms['p90_cites_author_year']:.2f}) — Possible self-citation or tight citation circle.")

    return flags

def print_worst_performers(data):
    print("\n📉 Top 3 Researchers with Worst Metrics:")
    metrics = {
        'Authors_Paper': True,
        'hI_index': False,
        'hm_index': False,
        'hA': False,
        'g_index': True,
        'e_index': True,
        'h_coverage': True,
        'g_coverage': True,
        'star_count': True,
        'Cites_Author_Year': True
    }

    for metric, higher_is_worse in metrics.items():
        sorted_data = sorted(data, key=lambda x: x.get(metric, 0), reverse=higher_is_worse)
        print(f"\n🔻 Worst in {metric}:")
        for i, row in enumerate(sorted_data[:3]):
            name = row.get('Query', 'Unknown')
            value = row.get(metric, 0)
            print(f"  {i+1}. {name}: {metric} = {value:.2f}")



def main():
    norms, data = calculate_department_norms("pop-metrics.csv")
    for row in data:
        name = row.get('Query', 'Unknown Researcher')
        print(f"\n🔍 Analyzing: {name}")
        flags = analyze_profile(row, norms)
        if flags:
            for i, flag in enumerate(flags, 1):
                print(f"⚠️ {i}. {flag}")
        else:
            print("✅ No red flags detected.")
        print("-" * 60)
    print_worst_performers(data)

if __name__ == "__main__":
    main()
