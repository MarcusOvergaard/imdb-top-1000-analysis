# Data Analysis Plan for IMDB Top 1000 Dataset

This plan outlines three hypotheses to test using the `imdb_top_1000.csv` dataset and describes how to visualize and confirm or deny them.

## Dataset:
`imdb_top_1000.csv`

## Hypotheses and Analysis Plan:

### Hypothesis 1: Movies belonging to the 'Drama' genre have a higher average IMDb rating compared to other genres in the top 1000 list.

**Rationale:** Drama is often considered a critically acclaimed genre, and this hypothesis explores if this perception holds true in the IMDb Top 1000.

**Data Extraction:**
1.  Load `imdb_top_1000.csv` into a pandas DataFrame.
2.  Extract the 'Genre' and 'IMDb_Rating' columns.
3.  Handle multiple genres per movie (e.g., by splitting and considering each genre individually or focusing on the primary genre).

**Visualization Plan:**
1.  Create a bar chart. The x-axis will represent different genres (or a selection of top genres), and the y-axis will show the average IMDb rating for movies in that genre.
2.  A clear distinction should be made for the 'Drama' genre.

**Confirmation/Denial:**
1.  Calculate the average IMDb rating for each genre.
2.  Compare the average rating of 'Drama' movies to the overall average rating of all movies and to the averages of other prominent genres.
3.  (Optional for deeper analysis): Perform statistical hypothesis testing (e.g., ANOVA if comparing multiple genres, or a t-test if comparing 'Drama' to a single other genre or the overall average) to determine if observed differences are statistically significant.

### Hypothesis 2: There is a positive correlation between the number of votes a movie receives and its IMDb rating.

**Rationale:** This hypothesis investigates whether movies that are more popular (indicated by a higher number of votes) also tend to have higher IMDb ratings, suggesting that widespread appeal aligns with critical or perceived quality within the top 1000.

**Data Extraction:**
1.  Load `imdb_top_1000.csv`.
2.  Extract the 'No_of_Votes' and 'IMDb_Rating' columns.

**Visualization Plan:**
1.  Create a scatter plot. 'No_of_Votes' will be on the x-axis and 'IMDb_Rating' on the y-axis.
2.  Logarithmic scaling might be applied to the 'No_of_Votes' axis if there's a wide range of values to better visualize the distribution.

**Confirmation/Denial:**
1.  Visually inspect the scatter plot for any discernible trend (upward, downward, or none).
2.  Calculate the Pearson correlation coefficient between 'No_of_Votes' and 'IMDb_Rating'. A coefficient close to +1 would indicate a strong positive correlation, while a value near 0 suggests no linear correlation.

### Hypothesis 3: Movies released in the 1990s have a higher representation in the IMDb Top 1000 list compared to other decades.

**Rationale:** The 1990s is often considered a golden era for cinema. This hypothesis aims to quantify its representation in a curated list of top films.

**Data Extraction:**
1.  Load `imdb_top_1000.csv`.
2.  Extract the 'Released_Year' column.
3.  Derive the decade for each movie from its 'Released_Year'.

**Visualization Plan:**
1.  Create a bar chart. The x-axis will represent different decades (e.g., 1950s, 1960s, ..., 2010s), and the y-axis will show the count of movies released in that decade.

**Confirmation/Denial:**
1.  Count the number of movies for each decade present in the dataset.
2.  Directly compare the count of movies from the 1990s to the counts from other decades.
3.  The highest bar in the chart corresponding to the 1990s would confirm the hypothesis.

## Conclusions (Based on expected results from `Visualize.ipynb`):

### Conclusion for Hypothesis 1: Movies belonging to the 'Drama' genre have a higher average IMDb rating compared to other genres in the top 1000 list.

**Expected Outcome:** Upon running the `Visualize.ipynb` notebook and observing the bar chart for average IMDb rating per genre, we would compare the average rating of 'Drama' with other genres.
**If Confirmed:** If 'Drama' shows a consistently higher average IMDb rating than most other genres, especially the top-ranking ones, the hypothesis would be supported. The bar for 'Drama' would be notably taller.
**If Denied:** If 'Drama's average rating is comparable to or lower than several other prominent genres, the hypothesis would be denied.

### Conclusion for Hypothesis 2: There is a positive correlation between the number of votes a movie receives and its IMDb rating.

**Expected Outcome:** After generating the scatter plot of 'Number of Votes' vs. 'IMDb Rating' and calculating the correlation coefficient in `Visualize.ipynb`:
**If Confirmed:** The scatter plot would show a general upward trend, indicating that as the number of votes increases, the IMDb rating also tends to increase. The calculated Pearson correlation coefficient would be a positive value, ideally above 0.5, suggesting a moderate to strong positive correlation.
**If Denied:** If the scatter plot shows no clear trend, or a downward trend, and the correlation coefficient is close to zero or negative, the hypothesis would be denied.

### Conclusion for Hypothesis 3: Movies released in the 1990s have a higher representation in the IMDb Top 1000 list compared to other decades.

**Expected Outcome:** By examining the bar chart showing the count of movies per decade in `Visualize.ipynb`:
**If Confirmed:** The bar corresponding to the '1990s' decade would be significantly taller than the bars for other decades, indicating a higher number of Top 1000 movies released during that period.
**If Denied:** If another decade has a comparable or higher number of movies, or if the 1990s representation is not notably higher, the hypothesis would be denied.

## Outcome of the Charts:

Based on the provided results from the `Visualize.ipynb` notebook, here are the definitive conclusions for each hypothesis:

### Hypothesis 1: Movies belonging to the 'Drama' genre have a higher average IMDb rating compared to other genres in the top 1000 list.

Result: Average rating for Drama genre: 7.959392265193371
Result: Overall average IMDb rating: 7.949299999999999
**Conclusion:** The hypothesis is **supported**. While the difference is marginal (Drama's average rating is slightly higher than the overall average), it indicates that Drama movies in the Top 1000 indeed have a very slightly elevated average rating. A deeper statistical test would be needed to confirm the statistical significance of this small difference.

### Hypothesis 2: There is a positive correlation between the number of votes a movie receives and its IMDb rating.

Result: Correlation between Number of Votes and IMDb Rating: 0.49
**Conclusion:** The hypothesis is **supported**. A Pearson correlation coefficient of 0.49 indicates a moderate positive correlation between the number of votes a movie receives and its IMDb rating. This suggests that movies with more votes tend to have higher ratings in this dataset.

### Hypothesis 3: Movies released in the 1990s have a higher representation in the IMDb Top 1000 list compared to other decades.

Result:
    1920s: 11
    1930s: 24
    1940s: 35
    1950s: 56
    1960s: 73
    1970s: 76
    1980s: 89
    1990s: 150
    2000s: 237
    2010s: 242
    2020s: 6
**Conclusion:** The hypothesis is **denied**. The 1990s (with 150 movies) do not have the highest representation in the IMDb Top 1000. Both the 2000s (237 movies) and the 2010s (242 movies) have a significantly higher number of films listed. This indicates that the most recent full decades (2000s and 2010s) are more heavily represented in the current IMDb Top 1000 list.