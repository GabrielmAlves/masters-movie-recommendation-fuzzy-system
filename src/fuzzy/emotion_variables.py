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

funny_sets = {
    "pouco engraçado": lambda x: trapezoidal(
        x,
        0.43, 0.43,
        0.50, 0.53
    ),
    "engraçado": lambda x: triangular(
        x,
        0.51, 0.55, 0.60
    ),
    "muito engraçado": lambda x: trapezoidal(
        x,
        0.57, 0.62,
        0.76, 0.76
    )
}

action_sets = {
    "pouca ação": lambda x: trapezoidal(
        x,
        0.43, 0.43,
        0.49, 0.52
    ),
    "ação moderada": lambda x: triangular(
        x,
        0.50, 0.54, 0.59
    ),
    "muita ação": lambda x: trapezoidal(
        x,
        0.57, 0.61,
        0.72, 0.72
    )
}