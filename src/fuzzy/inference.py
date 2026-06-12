from fuzzy.recommendation_rules import recommendation_rules
from fuzzy.operators import fuzzy_and, fuzzy_or
from fuzzy.fuzzification import (
    fuzzify_duration,
    fuzzify_tension,
    fuzzify_funny,
    fuzzify_action,
    fuzzify_romance,
    fuzzify_science_fiction,
    fuzzify_terror,
    fuzzify_drama
)
from fuzzy.aggregation import aggregate_rule_outputs
from fuzzy.defuzzification import centroid_defuzzification

def mamdani_inference(movie, interpreted_query):
    rule_outputs = []

    duration_values = fuzzify_duration(movie.duration)
    tension_values = fuzzify_tension(movie.tense_score)
    funny_values = fuzzify_funny(movie.funny_score)
    action_values = fuzzify_action(movie.action_score)
    romance_values = fuzzify_romance(movie.romance_score)
    sci_fi_values = fuzzify_science_fiction(movie.sci_fi_score)
    terror_values = fuzzify_terror(movie.terror_score)
    drama_values = fuzzify_drama(movie.drama_score)

    for rule in recommendation_rules:
        rule_matches_query = True

        for variable, term in rule.antecedent.items():

            if variable not in interpreted_query:
                rule_matches_query = False
                break

            if interpreted_query[variable] != term:
                rule_matches_query = False
                break

        if not rule_matches_query:
            continue

        antecedent_scores = []

        for variable, term in rule.antecedent.items():

            if variable == "duração":
                antecedent_scores.append(
                    duration_values[term]
                )

            elif variable == "emoção":

                if term == "engraçado":
                    antecedent_scores.append(
                        funny_values["engraçado"]
                    )

                elif term in ["tenso", "assustador"]:
                    antecedent_scores.append(
                        tension_values["tenso"]
                    )

                elif term == "ação":
                    antecedent_scores.append(
                        action_values["ação"]
                    )

            elif variable == "gênero":

                if term == "romance":
                    antecedent_scores.append(
                        romance_values["romance"]
                    )

                elif term == "terror":
                    antecedent_scores.append(
                        terror_values["terror"]
                    )

                elif term == "ficção científica":
                    antecedent_scores.append(
                        sci_fi_values["ficção científica"]
                    )

                elif term == "drama":
                    antecedent_scores.append(
                        drama_values["drama"]
                    )

        if not antecedent_scores:
            continue

        firing_strength = antecedent_scores[0]

        for score in antecedent_scores[1:]:
            firing_strength = fuzzy_and(
                firing_strength,
                score
            )

        print(rule.antecedent)
        print(rule.consequent)
        print(firing_strength)
        print("-----")

        rule_outputs.append(
            (
                rule.consequent,
                firing_strength
            )
        )

    return rule_outputs

def mamdani_score(movie, interpreted_query):
    rule_outputs = mamdani_inference(
        movie,
        interpreted_query
    )

    aggregated_output = aggregate_rule_outputs(
        rule_outputs
    )

    final_score = centroid_defuzzification(
        aggregated_output
    )

    return final_score