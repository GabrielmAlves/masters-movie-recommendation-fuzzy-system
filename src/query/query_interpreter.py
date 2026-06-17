from ml.nlp import vague_terms

def interpret_query(detected_terms):
    interpreted = {}

    for category, term in detected_terms:
        interpreted[category] = term

    return interpreted