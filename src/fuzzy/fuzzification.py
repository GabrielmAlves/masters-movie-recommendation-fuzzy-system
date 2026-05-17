from fuzzy.linguistic_variables import duration_sets
from fuzzy.emotion_variables import tension_sets

def fuzzify_duration(duration):
    membership_values = {}
    
    for term, function in duration_sets.items():
        membership_values[term] = function(duration)
        
    return membership_values

def fuzzify_tension(tension_score):
    return {
        term: fn(tension_score)
        for term, fn in tension_sets.items()
    }