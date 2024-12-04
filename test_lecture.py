import unittest

from lecture import read_entry

class TestLecture(unittest.TestCase):
    def test_read_entry_valid_form_grammar(self):

        result = read_entry('example_files/testFile_1.general')

        assert result.axiome == 'S'
        assert result.terminaux == {'a', 'b'}
        assert result.non_terminaux == {'S', 'A'}
        assert result.regles == {'S': ['aA'], 'A': ['bA', 'b']}

    def test_read_entry_invalid_line_format(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        read_entry('example_files/testFile_2.general')

        sys.stdout = sys.__stdout__
        assert "Il manque une partie droite ou une partie gauche à la ligne : SaB" in captured_output.getvalue()