import logging
import re

import sys

logging.basicConfig(level=logging.INFO)


class TextHandler(object):
    def __init__(self, *args, **kwargs):
        self.file_path = kwargs.get("file_path")
        self.kwargs = kwargs

    @property
    def logger(self):
        return logging.getLogger(self.__class__.__name__ + "." + sys._getframe(1).f_code.co_name + ":")

    @property
    def get_file_name(self):
        return self.file_path.split("/")[-1]

    @property
    def get_pattern(self):
        choices = self.kwargs
        for key, value in choices.iteritems():
            if value and key != "file_path":
                return key, value

    @property
    def open_files(self):
        print "__" * 120
        print "Following file were selected: {}".format(self.get_file_name)
        print "__" * 120
        print "\n"
        with open(self.file_path) as f:
            content = f.readlines()
            return content

    def make_action(self, indexes, text):
        operation, pattern = self.get_pattern
        if operation == "underscore":
            return text + self._underscore_text(indexes, text)
        elif operation == "color":
            return self._colorize_text(pattern, text)
        elif operation == 'machine':
            return self._machinize_text(text)

    def run(self):
        _, pattern = self.get_pattern
        opened_file = self.open_files
        for row_number, row in enumerate(opened_file):
            match_indexes = [(m.start(0), m.end(0)) for m in re.finditer(pattern, row)]
            if match_indexes:
                yield (row_number, match_indexes, self.make_action(match_indexes, row))

    @staticmethod
    def _colorize_text(pattern, text):
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
        for k, v in ind:
            text = text.replace(text[k:v], "^" * (v - k))
        return "".join([c if c == "^" else " " for c in text])

    @staticmethod
    def _machinize_text(st):
        return repr(st)
