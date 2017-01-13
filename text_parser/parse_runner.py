import sys
import os

import argparse

from text_handler import TextHandler

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path + '/file_storage')


class DefaultFileAction(argparse.Action):
    """
      Default handler for file path
    """

    def __call__(self, parser, namespace, values, option_string=None):
        file_pth = self._path_prefix(values)
        lst_of_path = []
        for pth in file_pth:
            if not os.path.isfile(pth):
                raise argparse.ArgumentError(self, "Following file does not exist: {}".format(pth))
            lst_of_path.append(pth)
        setattr(namespace, self.dest, lst_of_path)

    @staticmethod
    def _path_prefix(value):
        return tuple(file_path + "/" + element if "/" not in element else value for element in value)


def main(argv):
    """
     Commandline args parser
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-f", "--file_path", nargs='+', action=DefaultFileAction,
                        help="specify file name or absolute path to file in case if not situated in file_storage dir")
    group.add_argument("-u", "--underscore", type=str,
                       help="Get underscore text lines by specified pattern")
    group.add_argument("-c", "--color", type=str,
                       help="Get colored text lines by specified pattern")
    group.add_argument("-m", "--machine", type=str,
                       help="Get in machine code")
    group.required = True
    args = parser.parse_args()
    tr = TextHandler(file_path=args.file_path,
                     underscore=args.underscore,
                     color=args.color,
                     machine=args.machine)

    for i, m, s in tr.run():
        print '\033[91m' + "line number:" + '\033[94m' + '\033[92m' + " {}: ".format(
            i) + '\033[0m' '\033[91m' + "positions:" + '\033[94m' + '\033[92m' + " {}".format(m) + '\033[0m'
        print "__" * 120
        print s
        print "__" * 120


if __name__ == "__main__":
    main(sys.argv)
