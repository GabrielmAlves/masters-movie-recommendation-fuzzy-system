from sklearn.metrics.pairwise import cosine_similarity
from nlp.embedding import get_model
import numpy

_model = get_model()

FUNNY_REF = _model.encode("funny comedy humor hilarious")
TENSION_REF = _model.encode("tense suspense scary horror")
ACTION_REF =  _model.encode("action fight explosion fast intense")

def similarity(a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
    return cosine_similarity([a], [b])[0][0]

def compute_funny_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, FUNNY_REF)

def compute_tension_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, TENSION_REF)

def compute_action_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, ACTION_REF)