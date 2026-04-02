from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "imdb_top_1000.csv"
FIGURES_DIR = ROOT / "reports" / "figures"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["No_of_Votes"] = df["No_of_Votes"].astype(str).str.replace(",", "", regex=False).astype(int)
    df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
    return df


def drama_vs_non_drama(df: pd.DataFrame) -> Tuple[float, float, float]:
    genres = df.assign(Genre=df["Genre"].str.split(", ")).explode("Genre")
    drama_avg = genres.groupby("Genre")["IMDB_Rating"].mean().loc["Drama"]
    overall_avg = df["IMDB_Rating"].mean()

    is_drama = df["Genre"].fillna("").str.contains(r"(^|, )Drama(,|$)", regex=True)
    t_stat, p_value = stats.ttest_ind(
        df.loc[is_drama, "IMDB_Rating"],
        df.loc[~is_drama, "IMDB_Rating"],
        equal_var=False,
        nan_policy="omit",
    )
    return drama_avg, overall_avg, float(p_value)


def votes_rating_correlation(df: pd.DataFrame) -> float:
    return float(df["No_of_Votes"].corr(df["IMDB_Rating"]))


def movies_per_decade(df: pd.DataFrame) -> pd.Series:
    decade = (df["Released_Year"] // 10 * 10).dropna().astype(int).astype(str) + "s"
    return decade.value_counts().sort_index()


def save_figures(df: pd.DataFrame, out_dir: Path = FIGURES_DIR) -> Dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    paths: Dict[str, Path] = {}

    genres_df = df.assign(Genre=df["Genre"].str.split(", ")).explode("Genre")
    avg_rating_per_genre = genres_df.groupby("Genre")["IMDB_Rating"].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 7))
    sns.barplot(x=avg_rating_per_genre.index, y=avg_rating_per_genre.values, hue=avg_rating_per_genre.index, palette="viridis", legend=False)
    plt.title("Average IMDb Rating by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average IMDb Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    p1 = out_dir / "avg_rating_by_genre.png"
    plt.savefig(p1, dpi=200, bbox_inches="tight")
    plt.close()
    paths["genre_ratings"] = p1

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="No_of_Votes", y="IMDB_Rating", data=df, alpha=0.6)
    plt.xscale("log")
    plt.title("IMDb Rating vs Number of Votes")
    plt.xlabel("Number of Votes (log scale)")
    plt.ylabel("IMDb Rating")
    plt.tight_layout()
    p2 = out_dir / "votes_vs_rating.png"
    plt.savefig(p2, dpi=200, bbox_inches="tight")
    plt.close()
    paths["votes_vs_rating"] = p2

    decade_counts = movies_per_decade(df)
    plt.figure(figsize=(12, 7))
    sns.barplot(x=decade_counts.index, y=decade_counts.values, hue=decade_counts.index, palette="plasma", legend=False)
    plt.title("Number of IMDb Top 1000 Titles by Decade")
    plt.xlabel("Decade")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    p3 = out_dir / "titles_by_decade.png"
    plt.savefig(p3, dpi=200, bbox_inches="tight")
    plt.close()
    paths["titles_by_decade"] = p3

    return paths


def build_summary(df: pd.DataFrame) -> str:
    drama_avg, overall_avg, p_value = drama_vs_non_drama(df)
    corr = votes_rating_correlation(df)
    decade_counts = movies_per_decade(df)
    top_decade = decade_counts.sort_values(ascending=False).index[0]

    return (
        f"Drama average rating: {drama_avg:.3f}\n"
        f"Overall average rating: {overall_avg:.3f}\n"
        f"Drama vs non-Drama Welch t-test p-value: {p_value:.4f}\n"
        f"Votes/rating correlation: {corr:.3f}\n"
        f"Most represented decade: {top_decade} ({int(decade_counts[top_decade])} titles)\n"
    )


if __name__ == "__main__":
    df = load_data()
    save_figures(df)
    print(build_summary(df))
