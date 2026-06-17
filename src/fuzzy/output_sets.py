from fuzzy.membership_functions import trapezoidal, triangular

recommendation_sets = {
    "baixa": lambda x: trapezoidal(
        x,
        0.0, 0.0,
        0.25, 0.45
    ),
    
    "média": lambda x: triangular(
        x,
        0.3, 0.5, 0.7
    ),

    "alta": lambda x: trapezoidal(
        x,
        0.6, 0.8,
        1.0, 1.0
    )
}

def fuzzify_recommendation(value):
    return {
        term: membership_function(value)
        for term, membership_function in recommendation_sets.items()
    }