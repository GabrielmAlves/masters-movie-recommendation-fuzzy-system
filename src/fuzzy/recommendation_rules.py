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
    )
]