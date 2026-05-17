import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(values, attribute_name: str):
    plt.hist(values, bins=30)

    plt.xlabel(attribute_name)
    plt.ylabel("Frequency")
    plt.title(f"{attribute_name} Distribution")

    plt.show()


def get_percentiles(data):
    return np.percentile(data, [25, 50, 75])


def get_distribution(data, attribute_name: str):
    values = []

    for movie in data:
        value = getattr(movie, attribute_name, None)

        if value is None:
            continue

        if attribute_name == "duration":
            if not (60 <= value <= 240):
                continue

        values.append(value)

    if not values:
        return {}

    percentiles = get_percentiles(values)

    distribution_information = {
        "percentiles": {
            "25%": percentiles[0],
            "50%": percentiles[1],
            "75%": percentiles[2]
        },
        "max": np.max(values),
        "min": np.min(values),
        "mean": np.mean(values),
        "std": np.std(values)
    }

    plot_histogram(values, attribute_name)

    return distribution_information