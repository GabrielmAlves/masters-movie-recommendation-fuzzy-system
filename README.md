# masters-movie-recommendation-fuzzy-system
Recommendation system that recommends movies to users using fuzzy logic.

This project is being done as the final project of subject Fuzzy Systems (Sistemas Nebulosos) - IA861-A of my masters degree at UNICAMP.

The main idea of the project is allow users to query for some certain type of movie recommendation but also allowing users to make vague and imprecise queries, such as:
- Short/long/etc. duration movies
- Kinda funny/tense/etc. type of movies
- Good/bad/more or less/etc. evaluated movies

There will be 3 main micro-services available to the project: NLP, fuzzy and inference services. The first one will be responsible into embedding user's queries, pre-process it and determine whether or not that query has vague/imprecise terms. If this type of terms are detected, then the fuzzy service will be responsible to fuzzify the query and understand the belongingness of the query to a certain membership function. The final service to be used will be the inference one, which will have a C++ engine that will perform semantic search for movies.
