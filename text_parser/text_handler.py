import logging
import re

import sys

logging.basicConfig(level=logging.INFO)

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


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
        print "Following file were selected: {}".format(self.get_file_name)
        print "__" * 40
        with open(self.file_path) as f:
            content = f.readlines()
            return content

    def make_action(self, indexes, text):
        operation, _ = self.get_pattern
        if operation == "color":
            pass
        elif operation == "underscore":
            for k, v in indexes:
                return self.underscore_text(text[k:v])
        elif operation == "machine":
            pass

    def run(self):
        _, pattern = self.get_pattern
        opened_file = self.open_files
        for row_number, row in enumerate(opened_file):
            match_indexes = [(m.start(0), m.end(0)) for m in re.finditer(pattern, row)]
            if match_indexes:
                print match_indexes, row
                # return self.make_action(match_indexes, row)

    @staticmethod
    def _colorize_text(text):
        return YELLOW + text + END

    @staticmethod
    def underscore_text(text):
        return UNDERLINE + text + END

    @staticmethod
    def machinize_text(st):
        return ' '.join(format(ord(x), 'b') for x in st)