# IMDb Top 1000 Movies Data Analysis

An exploratory data analysis project built around a public IMDb Top 1000 dataset. The purpose is not to claim an objective truth about film quality, but to demonstrate a disciplined analytical workflow: define testable questions, clean and transform data, visualize findings, and discuss limitations without pretending the data says more than it does.

## Project Overview

This project investigates three compact hypotheses about titles in the IMDb Top 1000 dataset:

1. Do titles tagged with **Drama** have a slightly higher average IMDb rating than the rest of the dataset?
2. Is there a positive relationship between **number of votes** and **IMDb rating**?
3. Are films from the **1990s** the most represented decade in the Top 1000 list?

These are intentionally modest questions. They were chosen because they let me show category analysis, correlation analysis, temporal aggregation, and cautious interpretation in a reproducible way.

## Skills Demonstrated

- Data loading and cleaning with **pandas**
- Handling multi-label categorical data (`Genre`)
- Exploratory data analysis and visualization with **matplotlib** and **seaborn**
- Basic inferential statistics with a **Welch t-test**
- Communicating limitations, bias, and interpretive uncertainty
- Structuring a small project beyond a single notebook using a reusable Python module

## Why this project matters

The point of this repository is not just to produce three charts. It is to show the ability to:
- turn vague intuitions into measurable hypotheses,
- write reproducible analysis code,
- separate reusable logic from notebook exploration,
- communicate findings clearly,
- and avoid overclaiming from biased data.

## Dataset

- **Source:** Kaggle
- **Dataset:** [IMDb Dataset of Top 1000 Movies and TV Shows](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
- **Local file:** `data/imdb_top_1000.csv`
- **License:** CC0 1.0 Public Domain Dedication

This is not a neutral sample of all cinema. Because it is already a curated top-list, the data likely reflects:
- popularity bias,
- survivorship bias,
- platform-user bias,
- and some recency effects.

That makes it useful for exploratory work, but weak as evidence for universal claims about film quality.

## Analytical Framing

### Why these hypotheses?
They form a compact EDA exercise that demonstrates practical skills:
- category comparison,
- relationship analysis,
- decade-based aggregation,
- and basic statistical checking.

### Why should anyone care?
Because in a portfolio project, the value is not the domain alone. The value is showing that raw columns can be turned into interpretable questions, evidence, and caveats.

### Did I control for genre overlap?
Partially. Genre-level averages are computed on an exploded genre table because a title can belong to multiple genres. For the inferential comparison, the notebook also evaluates a **Drama vs non-Drama** split at the title level.

### Did I test statistical significance?
Yes, in a limited way. The project includes a **Welch t-test** for Drama vs non-Drama. That is an improvement over comparing raw averages alone, but it is still a simple inferential check rather than a full model.

### Is IMDb Top 1000 representative of film quality?
No. It is better understood as a ranked perception-and-popularity dataset than an objective measure of artistic merit.

## Results Summary

Current results from the dataset:

- **Drama average rating:** `7.959`
- **Overall average rating:** `7.949`
- **Votes / rating correlation:** `0.495`
- **Most represented decade:** `2010s` with `242` titles
- **Second most represented decade:** `2000s` with `237` titles
- **1990s representation:** `150` titles

Interpretation:
- Drama titles score **slightly** higher on average, but the effect is small.
- More-voted titles tend to have higher ratings within this dataset, with a **moderate positive correlation**.
- The hypothesis that the **1990s dominate the Top 1000 is false** in this sample.

## Figures

The charts are generated programmatically from `src/analysis.py` and saved into `reports/figures/`.

> Note: if the images are missing after cloning, run `python src/analysis.py` after installing the dependencies.

### Average IMDb Rating by Genre
![Average IMDb Rating by Genre](reports/figures/avg_rating_by_genre.png)

### IMDb Rating vs Number of Votes
![IMDb Rating vs Number of Votes](reports/figures/votes_vs_rating.png)

### Number of Titles by Decade
![Number of Titles by Decade](reports/figures/titles_by_decade.png)

## Project Structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   └── imdb_top_1000.csv
├── notebooks/
│   └── Visualize.ipynb
├── src/
│   └── analysis.py
├── reports/
│   └── figures/
│       ├── avg_rating_by_genre.png
│       ├── votes_vs_rating.png
│       └── titles_by_decade.png
└── analysis_docs/
    └── Data_Analysis_Plan.md
```

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- Jupyter Notebook or JupyterLab

### Installation

```bash
git clone https://github.com/MarcusOvergaard/imdb_analysis_project.git
cd imdb_analysis_project
pip install -r requirements.txt
```

### Run the notebook

```bash
jupyter lab
```

Then open `notebooks/Visualize.ipynb`.

### Generate the figures

```bash
python src/analysis.py
```

This recreates the charts in `reports/figures/` and prints a small numeric summary to the terminal.

## Limitations

- The dataset is pre-filtered and not representative of all films.
- Genre comparisons are imperfect because titles can belong to multiple genres.
- Correlation between votes and ratings does not imply causation.
- The t-test is a simple inferential check, not a complete modeling strategy.
- The project emphasizes clarity and reproducibility over advanced modeling.

## Future Improvements

- Control jointly for genre and release decade.
- Compare IMDb rating with `Meta_score`, runtime, and gross revenue.
- Add confidence intervals and stronger statistical reporting.
- Build an interactive dashboard version in Streamlit or Plotly Dash.

## License

This repository is released under **CC0 1.0 Universal**.

Dataset source and license:
- Kaggle: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
- CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/
