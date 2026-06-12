from sklearn.metrics.pairwise import cosine_similarity
from nlp.embedding import get_model
import numpy

_model = get_model()

FUNNY_REF = _model.encode("funny comedy humor hilarious")
TENSION_REF = _model.encode("tense suspense scary horror")
ACTION_REF =  _model.encode("action fight explosion fast intense")
ROMANCE_REF = _model.encode("romance love relationship romantic passionate heartwarming couple")
SCIENCE_FICTION_REF = _model.encode("science fiction space future technology alien universe galaxy dystopia")
TERROR_REF = _model.encode("horror terror fear frightening supernatural monster creature blood")
DRAMA_REF = _model.encode("drama emotional conflict struggle heartbreak tragedy grief loss personal")

def similarity(a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
    return cosine_similarity([a], [b])[0][0]

def compute_funny_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, FUNNY_REF)

def compute_tension_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, TENSION_REF)

def compute_action_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, ACTION_REF)

def compute_romance_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, ROMANCE_REF)

def compute_science_fiction_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, SCIENCE_FICTION_REF)

def compute_terror_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, TERROR_REF)

def compute_drama_score(movie_embedding: numpy.ndarray):
    return similarity(movie_embedding, DRAMA_REF)