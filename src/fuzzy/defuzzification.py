import numpy as np
from fuzzy.output_sets import recommendation_sets

def centroid_defuzzification(aggregated_outputs):
    x_values = np.linspace(0, 1, 1000)
    aggregated_membership = []
    
    for x in x_values:
        memberships = []
        for set_name, activation in aggregated_outputs.items():
            mu = recommendation_sets[set_name](x)
            clipped_mu = min(mu, activation)
            memberships.append(clipped_mu)
        
        aggregated_mu = max(memberships) if memberships else 0
        aggregated_membership.append(aggregated_mu)
        
    aggregated_membership = np.array(aggregated_membership)
    denominator = np.sum(aggregated_membership)
    
    if denominator == 0:
        return 0
    
    numerator = np.sum(x_values * aggregated_membership)
    return numerator / denominator