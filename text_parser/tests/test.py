import unittest
import re
import os

from text_parser.text_handler import TextHandler

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path + '/test_requisites')


class TestFileHandler(unittest.TestCase):
    @staticmethod
    def get_th_instance(fle_path, underscore, color, machine):
        tr = TextHandler(file_path=fle_path,
                         underscore=underscore,
                         color=color,
                         machine=machine)
        return tr

    def test_underscore(self):
        instance = self.get_th_instance(
            fle_path=file_path + "/test_file.txt",
            underscore='\d+',
            color=None,
            machine=None
        )
        res = [_ for _ in instance.run()]
        row_number, pos, text = res[0]
        row_itself, sp_under_row = text.split('\n')
        positions = [(m.start(0), m.end(0)) for m in re.finditer('\d+', row_itself)]
        for ind1, ind2 in positions:
            word_len = ind2 - ind1
            assert len(sp_under_row[ind1:ind2]) == word_len, "Not enough special characters under found pattern"
            assert "^" in sp_under_row[ind1:ind2], "^ character does not displayed"

    def test_color(self):
        expected_res = ["1500", "21213"]
        instance = self.get_th_instance(
            fle_path=file_path + "/test_file.txt",
            underscore=None,
            color='\d+',
            machine=None
        )
        res = [_ for _ in instance.run()]
        row_number, pos, text = res[0]
        assert all(("[32m" in text, "0m" in text)) is True, 'Yellow color in text'
        splitted_text = text.split("[32m")[1:]
        for ind, row in enumerate(splitted_text):
            assert row.startswith(expected_res[ind]), "Was highlighted not digit"
