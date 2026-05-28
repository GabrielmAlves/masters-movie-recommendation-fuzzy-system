from src.fuzzy.recommendation_rules import recommendation_rules
from src.fuzzy.operators import fuzzy_and, fuzzy_or
from src.fuzzy.fuzzification import (
    fuzzify_duration,
    fuzzify_tension,
    fuzzify_funny,
    fuzzify_action
)

def mamdani_inference(movie, interpreted_query):
    rule_outputs = []
    
    duration_values = fuzzify_duration(movie.duration)
    tension_values = fuzzify_tension(movie.tense_score)
    funny_values = fuzzify_funny(movie.funny_score)
    action_values = fuzzify_action(movie.action_score)
    
    for rule in recommendation_rules:
        antecedent_scores = []
        
        for variable, term in rule.antecedent.items():
            if variable == "duração":
                antecedent_scores.append(duration_values[term])
            elif variable == "emoção":
                if term == "engraçado":
                    antecedent_scores.append(funny_values["engraçado"])
                elif term in ["tenso", "assustador"]:
                    antecedent_scores.append(tension_values["tenso"])
                elif term == "ação":
                    antecedent_scores.append(action_values["ação"])
    
        if not antecedent_scores:
            continue
        
        firing_strength = antecedent_scores[0]
        
        for score in antecedent_scores[1:]:
            firing_strength = fuzzy_and(firing_strength, score)
        
        rule_outputs.append((rule.consequent, firing_strength))
    
    return rule_outputs