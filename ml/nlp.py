from sentence_transformers import SentenceTransformer
from dictionary import vague_terms
import numpy

model = SentenceTransformer("all-MiniLM-L6-v2")

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