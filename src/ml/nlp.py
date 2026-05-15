from sentence_transformers import SentenceTransformer
from .dictionary import vague_terms
from config.loader import load_config
import numpy

config = load_config()
model = SentenceTransformer(config.model.name)

def generate_embeddings(user_query: str) -> numpy.ndarray:
    query_embedding = model.encode(user_query)
    
    return query_embedding

def detect_vagueness(user_query: str) -> list[str]:
    terms = []
    
    for category, words in vague_terms.items():
        for word in words:
            if word in user_query:
                terms.append((category, word))
                
    return terms