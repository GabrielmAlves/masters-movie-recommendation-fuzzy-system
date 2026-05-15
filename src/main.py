# from .nlp import generate_embeddings, detect_vagueness
from data.dataset_loader import load_movies_database
from pipeline.build_features import build
from ml.data_extract import get_data_distribution
from ml.nlp import detect_vagueness
from query.query_interpreter import interpret_query
from ranking.ranker import rank_movies
from fuzzy.fuzzification import fuzzify_duration
import pickle   

if __name__ == "__main__":
    print("Please, query the system for some movie recommendation: ")
    user_query = input()
    
    vague_terms = detect_vagueness(user_query)
    
    if not vague_terms:
        print("There is no fuzziness in this query..")
    else:    
        for fuzzy_term in vague_terms:
            print(f"Fuzzy term: {fuzzy_term}")
    
    movies = load_movies_database("data/raw/TMDB_movie_dataset_v11.csv")
    
    build(movies)
    
    with open("movies_scores.pkl", "rb") as f:
        movies = pickle.load(f)
        
    data_distribution = get_data_distribution(movies, "duration")
    print("Data Distribution:")
    for key, value in data_distribution.items():
        print(f"  {key}: {value}")
        
    for movie in movies[:5]:
        print("Título do filme:", movie.title)
        print("Duração do filme:", movie.duration)
        
        print("Fuzzificação da duração do filme:")
        fuzzified_duration = fuzzify_duration(movie.duration)
        for term, value in fuzzified_duration.items():
            print(f"  {term}: {value}")
    
    movies_ranked = sorted(
        movies,
        key=lambda m: fuzzify_duration(m.duration)["curto"],
        reverse=True
    )
    
    print(movies_ranked[:10])
    
    interpreted_query = interpret_query(vague_terms)
    
    m_ranked = rank_movies(
        movies,
        interpreted_query
    )
    
    print("\nTop recommendations:\n")

    for movie in movies_ranked[:10]:
        print(movie.title)
        print("Tension:", movie.tense_score)
        print("Duration:", movie.duration)
        print("------")
    
        