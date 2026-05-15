from fuzzy.hedges import apply_hedge
from fuzzy.fuzzification import fuzzify_duration
from fuzzy.operators import fuzzy_and

def compute_movie_score(movie, interpreted_query):
    scores = []
    
    if "duração" in interpreted_query:
        duration_term = interpreted_query["duração"]
        
        duration_score = fuzzify_duration(movie.duration)[duration_term]
        scores.append(duration_score)
    
    if "emoção" in interpreted_query:
        emotion = interpreted_query["emoção"]
        
        if emotion == "assustador":
            emotion_score = movie.tense_score
        elif emotion == "engraçado":
            emotion_score = movie.funny_score
        else:
            emotion_score = 0
        
        if "intensidade" in interpreted_query:
            emotion_score = apply_hedge(
                emotion_score,
                interpreted_query["intensidade"]
            )
        scores.append(emotion_score)
    
    if not scores:
        return 0
    
    final_score = scores[0]
    
    for score in scores[1:]:
        final_score = fuzzy_and(final_score, score)
        
    return final_score

def rank_movies(movies, interpreted_query):
    
     return sorted(
        movies,
        key=lambda m: compute_movie_score(
            m,
            interpreted_query
        ),
        reverse=True
    )