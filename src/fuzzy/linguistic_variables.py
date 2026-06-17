from fuzzy.membership_functions import (
    triangular,
    trapezoidal
)

duration_sets = {
    "curto": lambda x: trapezoidal(
        x,
        60, 60,
        75, 90
    ),
    "médio": lambda x: triangular(
        x,
        80, 95, 120
    ),
    "longo": lambda x: trapezoidal(
        x,
        105, 130,
        240, 240
    )
}