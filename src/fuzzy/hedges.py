import math

def apply_hedge(value, hedge):

    match hedge:

        case "muito":
            return value ** 2

        case "bem":
            return value ** 2

        case "extremamente":
            return value ** 3

        case "super":
            return value ** 2.5

        case "pouco":
            return math.sqrt(value)

        case "um pouco":
            return value ** 0.7

        case "levemente":
            return value ** 0.5

        case "meio":
            return value ** 0.8

        case _:
            return value