from nlp import generate_embeddings, detect_vagueness

if __name__ == "__main__":
    print("Please, query the system for some movie recommendation: ")
    user_query = input()
    
    query_embeddings = generate_embeddings(user_query)
    
    vague_terms = detect_vagueness(user_query)
    
    if not vague_terms:
        print("There is no fuzziness in this query..")
        
    for fuzzy_term in vague_terms:
        print(f"Fuzzy term: {fuzzy_term}")