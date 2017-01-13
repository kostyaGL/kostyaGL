import logging
import re

import sys

logging.basicConfig(level=logging.INFO)


class TextHandler(object):
    """
     Class text handler
    """
    def __init__(self, *args, **kwargs):
        self.file_path = kwargs.get("file_path")
        self.kwargs = kwargs

    @property
    def logger(self):
        """
         Basic logger in std-out
        :return:
        """
        return logging.getLogger(self.__class__.__name__ + "." + sys._getframe(1).f_code.co_name + ":")

    @property
    def get_file_name(self):
        """
         Filename getter
        :return:
        """
        yield "/".join(map(lambda i: i.split("/"), self.file_path))

    @property
    def get_pattern(self):
        """
         Getter for all mutually exlusive parametrs
        :return:
        """
        choices = self.kwargs
        for key, value in choices.iteritems():
            if value and key != "file_path":
                return key, value

    @property
    def open_files(self):
        """
        Context manager
        :return:
        """
        for text_file in self.file_path:
            with open(text_file) as f:
                print "__" * 120
                print '\033[91m' + "Following file were selected: {}".format(text_file.split('/')[-1]) + '\033[0m'
                print "__"*120
                content = f.readlines()
            yield content

    def make_action(self, indexes, text):
        """
         Maker actions for text which was found by reg ex
        :param indexes: list of indexes
        :param text: text line in string
        :return: converted text in string format
        """
        operation, pattern = self.get_pattern
        if operation == "underscore":
            return text + self._underscore_text(indexes, text)
        elif operation == "color":
            return self._colorize_text(pattern, text)
        elif operation == 'machine':
            return self._machinize_text(text)

    @staticmethod
    def _colorize_text(pattern, text):
        """
         Colorizer of text
        :param pattern:
        :param text:
        :return:
        """
        colour_format = '\033[{0}m'
        colour_str = colour_format.format(32)
        reset_str = colour_format.format(0)
        last_match = 0
        formatted_text = ''
        for match in re.finditer(pattern, text):
            start, end = match.span()
            formatted_text += text[last_match: start]
            formatted_text += colour_str
            formatted_text += text[start: end]
            formatted_text += reset_str
            last_match = end
        formatted_text += text[last_match:]

        return formatted_text

    @staticmethod
    def _underscore_text(ind, text):
        """
         Text underscorer
        :param ind: list of indexes
        :param text: str
        :return: str
        """
        for k, v in ind:
            text = text.replace(text[k:v], "^" * (v - k))
        return "".join([c if c == "^" else " " for c in text])

    @staticmethod
    def _machinize_text(st):
        return repr(st)

    def run(self):
        """
         Script runner
        :return: generator
        """
        _, pattern = self.get_pattern
        opened_file = self.open_files
        for txt_file in opened_file:
            for row_number, row in enumerate(txt_file):
                # get indexes by reg ex
                match_indexes = [(m.start(0), m.end(0)) for m in re.finditer(pattern, row)]
                if match_indexes:
                    yield (row_number, match_indexes, self.make_action(match_indexes, row))
