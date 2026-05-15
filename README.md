# Exploring-and-Visualizing-a-simple-dataset

This project demonstrates how to load, inspect, summarize, and visualize the Iris dataset using `pandas`, `matplotlib`, and `seaborn`.

## Setup

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python analyze_iris.py
```

## What the script does

- Loads Iris CSV data with `pandas.read_csv(...)`
- Displays dataset structure using:
  - `.shape`
  - `.columns`
  - `.head()`
- Creates visualizations with `matplotlib` + `seaborn`:
  - Scatter plot
  - Histogram
  - Box plot

Generated images are saved in the `plots/` directory.
