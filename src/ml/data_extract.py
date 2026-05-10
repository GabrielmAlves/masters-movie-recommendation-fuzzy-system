import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(durations):
    plt.hist(durations, bins=30)

    plt.xlabel("Duration (minutes)")
    plt.ylabel("Number of movies")
    plt.title("Movie Duration Distribution")

    plt.show()

def get_percentiles(data):
    return np.percentile(data, [25, 50, 75])

def get_duration_distribution(data):
    filtered_movies = [
        m for m in data
        if m.duration is not None
        and 60 <= m.duration <= 240
    ]
    
    durations = [m.duration for m in filtered_movies]
    if not durations:
        return {}       
    
    percentiles = get_percentiles(durations)
    
    distribution_information = {
        "percentiles": {
            "25%": percentiles[0],
            "50%": percentiles[1],
            "75%": percentiles[2]
        },
        "max": max(durations),
        "min": min(durations),
        "mean": sum(durations) / len(durations),
        "std": np.std(durations)
    }
    
    plot_histogram(durations)
    
    return distribution_information

def get_data_distribution(data, data_type: str):
    match data_type:
        case "duration": return get_duration_distribution(data)