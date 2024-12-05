import unittest

from grammaire import Grammaire
from operation_gramm import find_non_term_epsilon


class TestOperationGrammaire(unittest.TestCase):
    def test_find_non_term_epsilon(self):
        grammaire = Grammaire()
        grammaire.non_terminaux = {'S', 'A', 'B'}
        grammaire.terminaux = {'a', 'b'}
        grammaire.new_prod_rules('S', 'Ab')
        grammaire.new_prod_rules('A', 'E')
        grammaire.new_prod_rules('B', 'bB')

        result = find_non_term_epsilon(grammaire)

        assert result == {'A'}

    def test_find_non_term_epsilon_chain(self):
        grammaire = Grammaire()
        grammaire.non_terminaux = {'S', 'A', 'B', 'C'}
        grammaire.terminaux = {'a', 'b'}
        grammaire.regles = {
            'S': ['AC'],
            'A': ['B'],
            'B': ['E'],
            'C': ['c']
        }

        result = find_non_term_epsilon(grammaire)

        assert result == {'A', 'B'}

    def test_find_non_term_epsilon_long_chain(self):
        grammaire = Grammaire()
        grammaire.non_terminaux = {'S', 'A', 'B', 'C', 'D', 'G', 'F'}
        grammaire.terminaux = {'a', 'b', 'c'}
        grammaire.regles = {
            'S': ['AC'],
            'A': ['E'],
            'B': ['E'],
            'C': ['E'],
            'D': ['E'],
            'G': ['c'],
            'F': ['c']
        }

        result = find_non_term_epsilon(grammaire)

        assert result == {'C', 'B', 'D', 'A', 'S'}

if __name__ == '__main__':
    unittest.main()
