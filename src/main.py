from data.dataset_loader import load_movies_database
from pipeline.build_features import build
from ml.data_extract import get_distribution
from ml.nlp import detect_vagueness
from query.query_interpreter import interpret_query
from ranking.ranker import rank_movies
from fuzzy.fuzzification import fuzzify_duration, fuzzify_tension
import pickle

from fuzzy.defuzzification import centroid_defuzzification
from fuzzy.inference import mamdani_inference
from fuzzy.aggregation import aggregate_rule_outputs

if __name__ == "__main__":
    print("Qual tipo de filme você gostaria?")
    user_query = input()
    
    detected_vague_terms = detect_vagueness(user_query)
    
    if not detected_vague_terms:
        print("Essa requisição não tem termo fuzzy..")
    else:    
        for fuzzy_term in detected_vague_terms:
            print(f"Termo fuzzy detectado: {fuzzy_term}")
    
    movies = load_movies_database("data/raw/TMDB_movie_dataset_v11.csv")
    
    build(movies)
    
    with open("movies_scores.pkl", "rb") as f:
        movies = pickle.load(f)
        
    duration_distribution = get_distribution(
        movies,
        "duration"
    )

    print("\nDistribuição da duração:")
    for key, value in duration_distribution.items():
        print(f"  {key}: {value}")


    tension_distribution = get_distribution(
        movies,
        "tense_score"
    )

    print("\nDistribuição de tensão:")
    for key, value in tension_distribution.items():
        print(f"  {key}: {value}")


    funny_distribution = get_distribution(
        movies,
        "funny_score"
    )

    print("\nDistribuição de engraçado:")
    for key, value in funny_distribution.items():
        print(f"  {key}: {value}")


    action_distribution = get_distribution(
        movies,
        "action_score"
    )
    
    romance_distribution = get_distribution(
        movies,
        "romance_score"
    )
    
    sci_fi_distribution = get_distribution(
        movies,
        "sci_fi_score"
    )
    
    drama_distribution = get_distribution(
        movies,
        "drama_score"
    )
    
    terror_distribution = get_distribution(
        movies,
        "terror_score"
    )

    print("\nDistribuição de ação:")
    for key, value in action_distribution.items():
        print(f"  {key}: {value}")
    
    print("Distribuição de romance: ")
    for key, value in romance_distribution.items():
        print(f"  {key}: {value}")
    
    print("Distribuição de ficção científica: ")
    for key, value in sci_fi_distribution.items():
        print(f"  {key}: {value}")
    
    print("Distribuição de drama: ")
    for key, value in drama_distribution.items():
        print(f"  {key}: {value}")
    
    print("Distribuição de terror: ")
    for key, value in terror_distribution.items():
        print(f"  {key}: {value}")
    
    interpreted_query = interpret_query(detected_vague_terms)
    
    m_ranked = rank_movies(
        movies,
        interpreted_query
    )
    
    print("\nTop recomendações:\n")

    for movie in m_ranked[:10]:
        print(movie.title)
        print("Grau de engraçado:", movie.funny_score)
        print("Grau de ação:", movie.action_score)
        print("Grau de tensão", movie.tense_score)
        print("Grau de romance: ", movie.romance_score)
        print("Grau de ficção científica: ", movie.sci_fi_score)
        print("Grau de drama: ", movie.drama_score)
        print("Duração do filme:", movie.duration)
        print("------")
    
    movie = m_ranked[0]

    rule_outputs = mamdani_inference(
        movie,
        interpreted_query
    )
    
    aggregated_output = aggregate_rule_outputs(
        rule_outputs
    )

    for key, value in aggregated_output.items():
        print(f"Agregação das regras: {aggregated_output}")

    for output in rule_outputs:
        print(f"Output das regras: {rule_outputs}")

    print(movie.title)
    print(fuzzify_duration(movie.duration))