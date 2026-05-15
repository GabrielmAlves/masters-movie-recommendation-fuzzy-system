from ml.nlp import vague_terms

def interpret_query(query):
    interpreted = {}
    
    for category, term in vague_terms.items():
        interpreted[category] = term
        
    return interpreted