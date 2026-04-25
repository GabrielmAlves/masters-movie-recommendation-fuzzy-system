from .schema import Config, ModelConfig, RetrievalConfig, FuzzyConfig
from pathlib import Path
import yaml

def load_config(path:str = None) -> Config:
    if path is None:
        base_dir = Path(__file__).resolve().parent.parent.parent
        path = base_dir / "config" / "config.yaml"
        
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        
    return Config(
        model=ModelConfig(**data["model"]),
        retrieval=RetrievalConfig(**data["retrieval"]),
        fuzzy=FuzzyConfig(**data["fuzzy"]),
    )