import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


IRIS_CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def main() -> None:
    try:
        dataset = pd.read_csv(IRIS_CSV_URL)
    except Exception as error:
        raise SystemExit(f"Failed to load Iris CSV data from {IRIS_CSV_URL}: {error}") from error

    print("Dataset shape:", dataset.shape)
    print("Dataset columns:", list(dataset.columns))
    print("Dataset head:")
    print(dataset.head())

    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=dataset, x="sepal_length", y="petal_length", hue="species")
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "scatter_plot.png"))
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.histplot(dataset["sepal_length"], bins=20, kde=True)
    plt.title("Histogram: Sepal Length Distribution")
    plt.xlabel("Sepal Length")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "histogram.png"))
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.boxplot(data=dataset, x="species", y="petal_width")
    plt.title("Box Plot: Petal Width by Species")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "box_plot.png"))
    plt.close()

    print(f"\nPlots saved in: {output_dir}/")


if __name__ == "__main__":
    main()
