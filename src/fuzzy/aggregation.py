def aggregate_rule_outputs(rule_outputs):
    aggregated = {}
    
    for consequent, strength in rule_outputs:
        if consequent not in aggregated:
            aggregated[consequent] = strength
        else:
            aggregated[consequent] = max(
                aggregated[consequent],
                strength
            )
            
    return aggregated