import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =======================
# CONFIG (EDIT THIS ONLY)
# =======================
DATASET_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
CATEGORY_COL = "month"
YEAR_COL = "year"
VALUE_COL = "passengers"
OUTPUT_PATH = os.path.join("output", "chart.png")
HEATMAP_OUTPUT_PATH = os.path.join("output", "heatmap.png")

MONTHS_ORDER = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

def main():
    df = pd.read_csv(DATASET_URL)

    # Terminal summary (required)
    print("Rows, Columns:", df.shape)
    print("Columns:", list(df.columns))
    print("\nFirst 5 rows:")
    print(df.head(5))

    # Clean: keep only needed columns and remove missing values
    df_small = df[[CATEGORY_COL, YEAR_COL, VALUE_COL]].dropna()

    # Convert numeric column safely
    df_small[VALUE_COL] = pd.to_numeric(df_small[VALUE_COL], errors="coerce")
    df_small = df_small.dropna()

    # Group mean by category
    grouped = df_small.groupby(CATEGORY_COL)[VALUE_COL].mean().sort_values(ascending=False)
    

    # Bar Chart
    print("\nAverage values by category:")
    print(grouped)

    # Plot
    os.makedirs("output", exist_ok=True)
    ax = grouped.plot(kind="bar")
    ax.set_title(f"Average {VALUE_COL} by {CATEGORY_COL}")
    ax.set_xlabel(CATEGORY_COL)
    ax.set_ylabel(f"Average {VALUE_COL}")
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=150)
    plt.close()

    print(f"\nSaved chart to: {OUTPUT_PATH}")

    # Heatmap
    pivot_table = df_small.pivot(index=CATEGORY_COL, columns=YEAR_COL, values=VALUE_COL)
    pivot_table = pivot_table.reindex(MONTHS_ORDER)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)
    plt.title(f"Heatmap of Passengers (Month vs Year)")
    plt.tight_layout()
    plt.savefig(HEATMAP_OUTPUT_PATH, dpi=150)
    plt.close()

    print(f"Saved heatmap to: {HEATMAP_OUTPUT_PATH}")


if __name__ == "__main__":
    main()