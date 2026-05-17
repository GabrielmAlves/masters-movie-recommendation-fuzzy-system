from fuzzy.membership_functions import (
    trapezoidal,
    triangular
)

tension_sets = {
    "leve": lambda x: trapezoidal(
        x,
        0.40,
        0.40,
        0.52,
        0.56
    ),
    "moderado": lambda x: triangular(
        x,
        0.53,
        0.58,
        0.63
    ),
    "tenso": lambda x: trapezoidal(
        x,
        0.60,
        0.66,
        0.82,
        0.82
    )
}