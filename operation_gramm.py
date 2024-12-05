def find_non_term_epsilon(grammaire):
    """
    Identifie les non-terminaux qui produisent 'E' (directement ou indirectement).
    :param grammaire: Instance de Grammaire
    :return: Un ensemble contenant les non-terminaux qui produisent 'E'.
    """
    epsilon_non_terminaux = set()
    changement = True

    while changement:
        changement = False
        for non_terminal, productions in grammaire.regles.items():
            if non_terminal not in epsilon_non_terminaux:
                for production in productions:
                    if production == "E":
                        epsilon_non_terminaux.add(non_terminal)
                        changement = True
                        break
                    if all(symbole in epsilon_non_terminaux for symbole in production):
                        epsilon_non_terminaux.add(non_terminal)
                        changement = True
                        break

    return epsilon_non_terminaux
