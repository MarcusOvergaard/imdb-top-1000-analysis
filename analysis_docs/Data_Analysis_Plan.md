# Data Analysis Plan for IMDb Top 1000 Dataset

This document outlines the analytical intent behind the project, the hypotheses being tested, the transformations applied, and the limitations that shape interpretation.

## Dataset

- **File:** `data/imdb_top_1000.csv`
- **Source:** Kaggle
- **Dataset page:** https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
- **License:** CC0 1.0 Public Domain Dedication

## Analytical Goal

The purpose of this project is not to claim a definitive ranking of film quality. It is to demonstrate a concise exploratory data analysis workflow using a public dataset: question formulation, preprocessing, visualization, basic statistical testing, and honest interpretation.

## Why These Hypotheses?

The selected hypotheses are deliberately simple but useful for a portfolio context:

1. **Genre comparison** shows category-based aggregation and handling of multi-label fields.
2. **Votes vs rating correlation** shows relationship analysis between a popularity-related variable and a scoring variable.
3. **Decade representation** shows temporal grouping and counting logic.

Together, they demonstrate core EDA skills without pretending to solve a large research question.

## Important Caveats

Before interpreting any result, the dataset itself imposes strong constraints:

- It is already a **Top 1000** list, so it is heavily filtered.
- It likely reflects **popularity bias** and **survivorship bias**.
- It may reflect **recency effects**, because newer films can dominate current top-lists.
- It is not a representative sample of all films ever released.
- IMDb ratings are user-generated and therefore reflect audience behavior, not an objective measure of artistic quality.

## Hypothesis 1

### Statement
Movies tagged with **Drama** have a higher average IMDb rating than the rest of the dataset.

### Why it matters
This hypothesis tests a common intuition that drama-heavy titles are more critically admired or more likely to score highly in elite rankings.

### Data preparation
- Load the dataset into a pandas DataFrame.
- Split the `Genre` column into multiple labels where needed.
- Create an exploded genre table for average genre-level summaries.
- Create a title-level Drama vs non-Drama split for a cleaner inferential comparison.

### Visualization
- Bar chart of average IMDb rating by genre.

### Statistical treatment
- Report average rating for Drama.
- Report overall average IMDb rating.
- Run a **Welch t-test** comparing Drama-tagged titles vs non-Drama titles.

### Interpretation caution
Because many titles belong to multiple genres, genre-level comparisons should be treated as approximate rather than definitive.

## Hypothesis 2

### Statement
There is a positive correlation between **number of votes** and **IMDb rating**.

### Why it matters
This explores whether more widely engaged titles also tend to receive higher ratings inside this curated top-list.

### Data preparation
- Clean `No_of_Votes` by removing commas and converting to integer.
- Extract `IMDB_Rating` as numeric.

### Visualization
- Scatter plot of `No_of_Votes` vs `IMDB_Rating`.
- Use a logarithmic x-axis because vote counts span a wide range.

### Statistical treatment
- Calculate the Pearson correlation coefficient.

### Interpretation caution
A positive correlation does **not** imply that vote count causes higher ratings. Both variables may be influenced by other factors such as visibility, cultural impact, or recency.

## Hypothesis 3

### Statement
Movies released in the **1990s** have the highest representation in the IMDb Top 1000 list.

### Why it matters
This tests a common cultural claim that the 1990s were a dominant era for highly regarded mainstream cinema.

### Data preparation
- Convert `Released_Year` to numeric.
- Derive a decade label from the year.

### Visualization
- Bar chart of number of titles by decade.

### Statistical treatment
- Count titles per decade and compare them directly.

### Interpretation caution
Any observed decade dominance may reflect list-construction effects, changing rating behavior over time, or recent audience preferences rather than a timeless measure of quality.

## Conclusion Framing

This project should be understood as a reproducible EDA exercise. Its strength is not that it proves deep truths about cinema, but that it demonstrates:

- structured thinking,
- transparent assumptions,
- basic statistical literacy,
- and cautious interpretation of imperfect data.

## Possible Extensions

- Compare IMDb ratings with `Meta_score`.
- Explore whether runtime is associated with rating.
- Investigate gross revenue patterns for top-ranked titles.
- Fit a regression model using rating as the outcome.
- Package the results in an interactive dashboard.
