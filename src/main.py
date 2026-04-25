# from .nlp import generate_embeddings, detect_vagueness
from data.dataset_loader import load_movies_database
from nlp.embedding import generate_embeddings_batch
from pipeline.build_features import build
from tqdm import tqdm
import pickle   

if __name__ == "__main__":
    print("Please, query the system for some movie recommendation: ")
    user_query = input()
    
    movies = load_movies_database("data/raw/TMDB_movie_dataset_v11.csv")
    
    build(movies)
    
    with open("movies_scores.pkl", "rb") as f:
        movies = pickle.load(f)

    for m in movies[:20]:
        print(m.title)
        print("funny:", m.funny_score)
        print("tension:", m.tense_score)
        print("action:", m.action_score)
        print("-----")

    # query_embeddings = generate_embeddings(user_query)
    
    # vague_terms = detect_vagueness(user_query)
    
    # if not vague_terms:
    #     print("There is no fuzziness in this query..")
    # else:    
    #     for fuzzy_term in vague_terms:
    #         print(f"Fuzzy term: {fuzzy_term}")
    
        