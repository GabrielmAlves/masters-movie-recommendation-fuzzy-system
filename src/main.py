# from .nlp import generate_embeddings, detect_vagueness
from data.dataset_loader import load_movies_database
from pipeline.build_features import build
from ml.data_extract import get_data_distribution
import pickle   

if __name__ == "__main__":
    print("Please, query the system for some movie recommendation: ")
    user_query = input()
    
    movies = load_movies_database("data/raw/TMDB_movie_dataset_v11.csv")
    
    build(movies)
    
    with open("movies_scores.pkl", "rb") as f:
        movies = pickle.load(f)

    for m in movies[:50]:
        print(m.title)
        print("funny:", m.funny_score)
        print("tension:", m.tense_score)
        print("action:", m.action_score)
        print("-----")

    data_distribution = get_data_distribution(movies, "duration")
    print("Data Distribution:")
    for key, value in data_distribution.items():
        print(f"  {key}: {value}")
    # query_embeddings = generate_embeddings(user_query)
    
    # vague_terms = detect_vagueness(user_query)
    
    # if not vague_terms:
    #     print("There is no fuzziness in this query..")
    # else:    
    #     for fuzzy_term in vague_terms:
    #         print(f"Fuzzy term: {fuzzy_term}")
    
        