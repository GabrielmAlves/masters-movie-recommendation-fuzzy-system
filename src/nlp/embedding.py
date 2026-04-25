from sentence_transformers import SentenceTransformer
from config.loader import load_config
from data.movie import Movie
import numpy
import torch

_model = None

def get_model():
    global _model

    if _model is None:
        config = load_config()

        device = "cuda" if torch.cuda.is_available() else "cpu"
        if torch.cuda.is_available():
            print(torch.cuda.get_device_name(0))
        print(f"Using device: {device}")

        _model = SentenceTransformer(config.model.name, device=device)

    return _model

def generate_embedding(text: str) -> numpy.ndarray:
    model = get_model()
    text_embedding = model.encode(text)
    
    return text_embedding

def generate_embeddings_batch(descriptions: str) ->numpy.ndarray:
    model = get_model()
    return model.encode(descriptions, batch_size=64, show_progress_bar=True)

