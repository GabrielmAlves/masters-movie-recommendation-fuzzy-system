class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
    
    def __repr__(self):
        return (
            f"Rule(IF={self.antecedent}, "
            f"THEN={self.consequent})"
        )