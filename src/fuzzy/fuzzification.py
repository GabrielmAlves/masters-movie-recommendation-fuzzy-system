from fuzzy.linguistic_variables import duration_sets
from fuzzy.emotion_variables import tension_sets, funny_sets, action_sets, romance_sets, science_fiction_sets, horror_sets, drama_sets

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

def fuzzify_funny(funny_score):
    return {
        term: fn(funny_score)
        for term, fn in funny_sets.items()
    }

def fuzzify_action(action_score):
    return {
        term: fn(action_score)
        for term, fn in action_sets.items()
    }

def fuzzify_romance(romance_score):
    return {
        term: fn(romance_score)
        for term, fn in romance_sets.items()
    }

def fuzzify_science_fiction(sci_fi_score):
    return {
        term: fn(sci_fi_score)
        for term, fn in science_fiction_sets.items()
    }

def fuzzify_terror(terror_score):
    return {
        term: fn(terror_score)
        for term, fn in horror_sets.items()
    }

def fuzzify_drama(drama_score):
    return {
        term: fn(drama_score)
        for term, fn in drama_sets.items()
    }