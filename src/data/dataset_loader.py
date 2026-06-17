import pandas as pd
from data.movie import Movie

def load_movies_database(path: str) -> list[Movie]:

    columns = [
        "title",
        "runtime",
        "overview",
        "genres",
        "release_date",
        "adult",
        "popularity",
        "vote_count",
        "vote_average"
    ]

    movies = []

    chunks = pd.read_csv(
        path,
        usecols=columns,
        chunksize=10000
    )

    for chunk in chunks:

        chunk = chunk.sample(frac=0.01)

        for _, row in chunk.iterrows():
            try:
                if (
                    pd.isna(row["title"]) or
                    pd.isna(row["runtime"]) or
                    pd.isna(row["overview"])
                ):
                    continue

                movie = Movie(
                    title=row["title"],
                    release_date=row["release_date"],
                    duration=float(row["runtime"]),
                    adult=row["adult"],
                    overview=row["overview"],
                    popularity=row["popularity"],
                    genres=row["genres"],
                    vote_count=row["vote_count"],
                    vote_average=row["vote_average"]
                )

                movies.append(movie)

            except Exception:
                continue

    return movies