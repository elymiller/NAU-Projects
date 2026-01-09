import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
from matplotlib.patches import Patch

def plot_mutS_histogram(csv_path):
    # --- Load and prepare data ---
    df = pd.read_csv(csv_path)
    df = df.rename(columns={
        df.columns[0]: "Draw Number",
        df.columns[1]: "P(Ts)",
        df.columns[2]: "P(Tv)",
        df.columns[3]: "P(mutS)"
    })
    df["Draw Number"] = pd.to_numeric(df["Draw Number"], errors="coerce")
    df = df.sort_values("Draw Number").reset_index(drop=True)
    df["Cumulative P(mutS)"] = df["P(mutS)"].cumsum()

    # --- Plotting ---
    sns.set(style="whitegrid", rc={'axes.edgecolor': 'black', 'grid.linestyle': ':'})
    fig, ax = plt.subplots(figsize=(12, 6))

    # Numeric bar chart
    ax.bar(df["Draw Number"], df["P(mutS)"], width=1.0, align="center",
           color="skyblue")
    ax.set_ylim(0,0.11)
    ax.set_xlabel("Steps", fontsize=12, weight="bold")
    ax.set_ylabel("P(mutS)", fontsize=12, color="skyblue", weight="bold")
    
    # Cumulative on twin
    ax2 = ax.twinx()
    line, = ax2.plot(df["Draw Number"], df["Cumulative P(mutS)"],
                     color="red", label="Cumulative P(mutS)")
    ax2.set_ylabel("Cumulative P(mutS)", fontsize=12, color="red", weight="bold")

    # Remove left/right padding
    ax.set_xlim(df["Draw Number"].min() - 0.5, df["Draw Number"].max() + 0.5)

    # Legend at center right
    patch = Patch(facecolor="skyblue", edgecolor="none", label="P(mutS)")
    ax.legend(handles=[patch, line], loc="center right")

    plt.title("P(mutS) Occuring at Each Step vs Cumulative P(mutS)",
              fontsize=12, weight="bold")
    plt.tight_layout()

    # --- Save ---
    output_file = os.path.splitext(csv_path)[0] + "_mutS_histogram.png"
    fig.savefig(output_file, dpi=500)
    plt.close(fig)
    print(f"Plot saved as: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mutS_histogram_plot.py <path_to_csv>")
    else:
        plot_mutS_histogram(sys.argv[1])
