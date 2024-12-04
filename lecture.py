from grammaire import Grammaire

def read_entry(file):
    grammaire = Grammaire()
    with open(file, 'r') as f:
        for ligne in f:
            ligne = ligne.strip().replace(" ", "")
            if ligne:
                try:
                    gauche, droite = ligne.split(":")
                    grammaire.new_prod_rules(gauche, droite)
                    if gauche not in grammaire.non_terminaux:
                        grammaire.non_terminaux.add(gauche)
                    for char in droite:
                        if char.islower():
                            grammaire.terminaux.add(char)
                        elif char.isupper():
                            grammaire.non_terminaux.add(char)
                except ValueError:
                    print(f"Il manque une partie droite ou une partie gauche à la ligne : {ligne}")
    return grammaire