class Movie:
    def __init__(self, title, release_date, duration, adult, overview, popularity, genres, vote_count, vote_average):
        self.title = title
        self.release_date = release_date
        self.duration = duration
        self.is_adult = adult
        self.overview = overview
        self.popularity = popularity
        self.genres = genres
        self.vote_count = vote_count
        self.vote_average = vote_average
        self.embedding = None
        self.funny_score = None
        self.tense_score = None
        self.action_score = None
        
    def __repr__(self):
        return f"Movie(title={self.title}, duration={self.duration})"