import unittest

from grammaire import Grammaire


class TestGrammaire(unittest.TestCase):
    def test_init_default_values(self):
        grammaire = Grammaire()

        assert grammaire.axiome == "S"
        assert grammaire.terminaux == set()
        assert grammaire.non_terminaux == set()
        assert grammaire.regles == {}

    def test_init_not_none(self):
        grammaire = Grammaire()

        assert grammaire.axiome is not None
        assert grammaire.terminaux is not None
        assert grammaire.non_terminaux is not None
        assert grammaire.regles is not None

    def test_add_new_non_terminal_rule(self):
        grammar = Grammaire()
        grammar.new_prod_rules("A", "a")

        assert "A" in grammar.regles
        assert grammar.regles["A"] == ["a"]

    def test_str(self):
        g = Grammaire()
        g.axiome = "S"
        g.terminaux = {"a", "b"}
        g.non_terminaux = {"S", "A"}
        g.regles = {"S": ["aA"], "A": ["b"]}

        result = str(g)

        expected = ("Axiome : S\n"
                    "Terminaux : a, b\n"
                    "Non-terminaux : A, S\n"
                    "Règles :\n  S -> aA"
                            "\n  A -> b")
        assert result == expected

    def test_str_multiple_prod_rules(self):
        g = Grammaire()
        g.axiome = "S"
        g.terminaux = {"a", "b"}
        g.non_terminaux = {"S", "A", "B"}
        g.new_prod_rules("S", "aA")
        g.new_prod_rules("S", "bB")
        g.new_prod_rules("A", "b")

        result = str(g)

        expected = (
            "Axiome : S\n"
            "Terminaux : a, b\n"
            "Non-terminaux : A, B, S\n"
            "Règles :\n"
            "  S -> aA, bB\n"
            "  A -> b"
        )
        assert result == expected, f"Expected:\n{expected}\nGot:\n{result}"



if __name__ == '__main__':
    unittest.main()
