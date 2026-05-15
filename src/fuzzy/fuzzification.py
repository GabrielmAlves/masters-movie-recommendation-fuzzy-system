from fuzzy.linguistic_variables import duration_sets

def fuzzify_duration(duration):
    membership_values = {}
    
    for term, function in duration_sets.items():
        membership_values[term] = function(duration)
        
    return membership_values