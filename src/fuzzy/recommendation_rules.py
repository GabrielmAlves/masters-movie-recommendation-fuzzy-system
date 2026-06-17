from fuzzy.rules import Rule

recommendation_rules = [

    Rule(
        antecedent={
            "duração": "curto",
            "emoção": "engraçado"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "longo",
            "emoção": "tenso"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "curto"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "médio"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "longo"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "emoção": "engraçado"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "emoção": "tenso"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "curto",
            "emoção": "tenso"
        },
        consequent="média"
    ),

    Rule(
        antecedent={
            "duração": "longo",
            "emoção": "engraçado"
        },
        consequent="baixa"
    ),

    Rule(
        antecedent={
            "gênero": "romance"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "gênero": "terror"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "gênero": "ficção científica"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "curto",
            "gênero": "romance"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "curto",
            "gênero": "terror"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "curto",
            "gênero": "ficção científica"
        },
        consequent="média"
    ),

    Rule(
        antecedent={
            "duração": "longo",
            "gênero": "romance"
        },
        consequent="média"
    ),

    Rule(
        antecedent={
            "duração": "longo",
            "gênero": "terror"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "longo",
            "gênero": "ficção científica"
        },
        consequent="alta"
    ),

    # Emotion + genre cross rules
    Rule(
        antecedent={
            "emoção": "engraçado",
            "gênero": "romance"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "emoção": "tenso",
            "gênero": "terror"
        },
        consequent="alta"
    ),

    # Drama rules
    Rule(
        antecedent={
            "gênero": "drama"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "médio",
            "gênero": "drama"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "longo",
            "gênero": "drama"
        },
        consequent="alta"
    ),

    Rule(
        antecedent={
            "duração": "curto",
            "gênero": "drama"
        },
        consequent="média"
    ),
]