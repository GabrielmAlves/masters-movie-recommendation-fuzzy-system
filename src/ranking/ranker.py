from fuzzy.hedges import apply_hedge

def compute_movie_score(movie, interpreted_query):
    score = 0
    
    if "emoção" in interpreted_query:
        emotion = interpreted_query["emoção"]
        
        if emotion == "assustador":
            emotion_score = movie.tense_score
            
            if "intensidade" in interpreted_query:
                emotion_score = apply_hedge(
                    emotion_score
                )
            score += emotion_score
    
    return score

def rank_movies(movies, interpreted_query):
     return sorted(
        movies,
        key=lambda m: compute_movie_score(
            m,
            interpreted_query
        ),
        reverse=True
    )