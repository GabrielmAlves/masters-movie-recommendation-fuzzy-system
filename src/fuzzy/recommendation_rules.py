from src.fuzzy.rules import Rule

recommendation_rules = [
    Rule(
        antecedents={
            "duração": "curto",
            "emoção": "engraçado"
        },
        consequent="alta"
    ),

    Rule(
        antecedents={
            "duração": "longo",
            "emoção": "tenso"
        },
        consequent="alta"
    ),

    Rule(
        antecedents={
            "emoção": "engraçado"
        },
        consequent="média"
    ),

    Rule(
        antecedents={
            "emoção": "tenso"
        },
        consequent="média"
    ),

    Rule(
        antecedents={
            "duração": "curto",
            "emoção": "tenso"
        },
        consequent="média"
    ),

    Rule(
        antecedents={
            "duração": "longo",
            "emoção": "engraçado"
        },
        consequent="baixa"
    )
]