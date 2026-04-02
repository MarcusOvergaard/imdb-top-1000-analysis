# IMDB Top 1000 Movies Data Analysis

This project provides a data analysis and visualization of the IMDB Top 1000 movies dataset. It includes a Jupyter Notebook for interactive exploration, a structured data analysis plan, and organized project directories for clarity and ease of use.

## Table of Contents

1.  [Project Overview](#project-overview)
2.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
3.  [Project Structure](#project-structure)
4.  [Data Analysis Plan](#data-analysis-plan)
5.  [Hypotheses and Conclusions](#hypotheses-and-conclusions)
6.  [Contributing](#contributing)
7.  [License](#license)

## 1. Project Overview

This repository contains an exploratory data analysis project focused on the IMDB Top 1000 movies. The goal is to investigate several hypotheses about movie characteristics, ratings, and historical trends using visualization and basic statistical methods.

## 2. Getting Started

### Prerequisites

To run this project, you will need:
*   Python 3.x
*   Jupyter Notebook or Jupyter Lab
*   `pandas` for data manipulation
*   `matplotlib` for plotting
*   `seaborn` for enhanced visualizations

### Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone https://github.com/MarcusOvergaard/imdb_analysis_project.git
    cd imdb_analysis_project
    ```
    (Note: Replace `https://github.com/MarcusOvergaard/imdb_analysis_project.git` with the actual repository URL if this project were hosted.)

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Start Jupyter Notebook or Jupyter Lab:
    ```bash
    jupyter notebook
    # or
    jupyter lab
    ```
    Navigate to the `notebooks/` directory and open `Visualize.ipynb`.

## 3. Project Structure

The project is organized as follows:

```
.
├── README.md                 
├── requirements.txt          # Python dependencies
├── GEMINI.md                 # Gemini CLI specific context and project description
├── data/
│   └── imdb_top_1000.csv     
├── notebooks/
│   └── Visualize.ipynb       # Jupyter Notebook for data analysis and visualizations
└── analysis_docs/
    └── Data_Analysis_Plan.md # Detailed plan of the data analysis, hypotheses, and conclusions
```

## 4. Data Analysis Plan

A detailed data analysis plan, including the rationale, data extraction methods, visualization plans, and confirmation/denial criteria for each hypothesis, can be found in `analysis_docs/Data_Analysis_Plan.md`.

## 5. Hypotheses and Conclusions

This project investigates three main hypotheses:

### Hypothesis 1: Movies belonging to the 'Drama' genre have a higher average IMDb rating compared to other genres in the top 1000 list.
*   **Conclusion:** The hypothesis is **supported**. While the difference is marginal (Drama's average rating is slightly higher than the overall average), it indicates that Drama movies in the Top 1000 indeed have a very slightly elevated average rating. A deeper statistical test would be needed to confirm the statistical significance of this small difference.

### Hypothesis 2: There is a positive correlation between the number of votes a movie receives and its IMDb rating.
*   **Conclusion:** The hypothesis is **supported**. A Pearson correlation coefficient of 0.49 indicates a moderate positive correlation between the number of votes a movie receives and its IMDb rating. This suggests that movies with more votes tend to have higher ratings in this dataset.

### Hypothesis 3: Movies released in the 1990s have a higher representation in the IMDb Top 1000 list compared to other decades.
*   **Conclusion:** The hypothesis is **denied**. The 1990s (with 150 movies) do not have the highest representation in the IMDb Top 1000. Both the 2000s (237 movies) and the 2010s (242 movies) have a significantly higher number of films listed. This indicates that the most recent full decades (2000s and 2010s) are more heavily represented in the current IMDb Top 1000 list.

## 6. Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## 7. License

This project is licensed under the MIT License.

The dataset (IMDb Top 1000) was obtained from Kaggle and is distributed under the MIT License by the original author.
Original source: https://www.kaggle.com/datasets/debanganghosh/imdb-dataset