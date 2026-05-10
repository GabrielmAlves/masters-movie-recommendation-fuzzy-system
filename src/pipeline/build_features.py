import pickle
import numpy as np
from tqdm import tqdm
from nlp.embedding import generate_embedding, generate_embeddings_batch
from data.movie import Movie
from scoring.feature_extraction import (
    compute_funny_score,
    compute_tension_score,
    compute_action_score
)

MOVIES_PICKLE_FILE = "movies_clean.pkl"
MOVIES_SCORES_PICKLE_FILE = "movies_scores.pkl"

def save_movie_scores(movies: list[Movie]):
    with open(MOVIES_SCORES_PICKLE_FILE, "wb") as movie_scores_file:
        pickle.dump(movies, movie_scores_file)

def save_movies(movies: list[Movie]):
    with open(MOVIES_PICKLE_FILE, "wb") as movie_file:
        pickle.dump(movies, movie_file)

def load_movies(movies_file: str) -> list[Movie]:
    with open(movies_file, "rb") as movie_file:
        loaded_movies = pickle.load(movie_file)

    return loaded_movies

def normalize(score: float) -> float:
    return (score + 1) / 2

def build(movies: list[Movie]):
    print("Obtendo filmes..")
    
    save_movies(movies)
    loaded_movies = load_movies(MOVIES_PICKLE_FILE)
    
    print(f"{len(movies)} filmes carregados")
    
    print("Gerando embeddings das descrições dos filmes...")
    
    movies_description = [m.overview for m in loaded_movies]
    embeddings = generate_embeddings_batch(movies_description)
            
    for m, emb in zip(loaded_movies, embeddings):
        m.embedding = emb
    
    print("Calculando scores...")
    
    for movie in tqdm(loaded_movies):
        movie.funny_score = normalize(compute_funny_score(movie.embedding))
        movie.tense_score = normalize(compute_tension_score(movie.embedding))
        movie.action_score = normalize(compute_action_score(movie.embedding))
        
    print("Salvando scores...")
    
    save_movie_scores(loaded_movies)
    
    print("Finalizado!")
    
    
    