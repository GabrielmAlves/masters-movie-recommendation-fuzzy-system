import pandas as pd
import ast
from data.movie import Movie

def load_movies_database(path: str) -> list[Movie]:
    dataframe = pd.read_csv(path, low_memory=False)
    
    dataframe = dataframe.sample(frac=0.01, random_state=42)
    
    movies = []
    
    for _, row in dataframe.iterrows():
        try:
            title = row["title"]
            duration = row["runtime"]
            overview = row["overview"]
            genres = row["genres"]
            release_date = row["release_date"]
            is_adult = row["adult"]
            popularity = row["popularity"]
            vote_count = row["vote_count"]
            vote_average = row["vote_average"]
            
            if pd.isna(title) or pd.isna(duration) or pd.isna(overview):
                continue
            
            movie = Movie(
                title=title,
                release_date=release_date,
                duration=float(duration),
                adult=is_adult,
                overview=overview,
                popularity=popularity,
                genres=genres,
                vote_count=vote_count,
                vote_average=vote_average
            )
            
            movies.append(movie)
            
        except Exception:
            continue
    
    return movies