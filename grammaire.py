class Grammaire:
    def __init__(self):
        self.axiome = "S"
        self.terminaux = set()
        self.non_terminaux = set()
        self.regles = {}

    def new_prod_rules(self, non_term, prod):
        if non_term not in self.regles:
            self.regles[non_term] = []
        if prod is not None:
            self.regles[non_term].append(prod)

    def __str__(self):
        result = []
        result.append(f"Axiome : {self.axiome}")
        result.append(f"Terminaux : {', '.join(sorted(self.terminaux))}")
        result.append(f"Non-terminaux : {', '.join(sorted(self.non_terminaux))}")
        result.append("Règles :")
        for non_terminal, productions in self.regles.items():
            result.append(f"  {non_terminal} -> {', '.join(productions)}")
        return "\n".join(result)