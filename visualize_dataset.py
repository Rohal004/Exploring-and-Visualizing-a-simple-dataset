from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "data" / "simple_dataset.csv"
PLOTS_DIR = BASE_DIR / "plots"
HISTOGRAM_BINS = 8


def main() -> None:
    df = pd.read_csv(DATASET_PATH)

    print("Dataset shape:", df.shape)
    print("\nDataset columns:")
    print(df.columns.tolist())
    print("\nDataset preview (.head()):")
    print(df.head())

    PLOTS_DIR.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="SepalLengthCm",
        y="PetalLengthCm",
        hue="Species",
    )
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "scatter_plot.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="SepalLengthCm", kde=True, bins=HISTOGRAM_BINS)
    plt.title("Histogram: Sepal Length Distribution")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "histogram.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Species", y="PetalWidthCm")
    plt.title("Box Plot: Petal Width by Species")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "box_plot.png")
    plt.close()

    print(f"\nPlots saved to: {PLOTS_DIR}")


if __name__ == "__main__":
    main()
