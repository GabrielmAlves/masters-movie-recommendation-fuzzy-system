from dataclasses import dataclass

@dataclass
class ModelConfig:
    name: str
    embedding_dim: int
    
@dataclass
class RetrievalConfig:
    top_k: int
    similarity_threshold: float

@dataclass
class FuzzyConfig:
    enabled: bool
    
@dataclass
class Config:
    model: ModelConfig
    retrieval: RetrievalConfig
    fuzzy: FuzzyConfig