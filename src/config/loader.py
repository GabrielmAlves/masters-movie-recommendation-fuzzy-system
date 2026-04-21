from .schema import Config, ModelConfig, RetrievalConfig, FuzzyConfig
import yaml

def load_config(path="config/config.yaml") -> Config:
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        
    return Config(
        model=ModelConfig(**data["model"]),
        retrieval=RetrievalConfig(**data["retrieval"]),
        fuzzy=FuzzyConfig(**data["fuzzy"]),
    )