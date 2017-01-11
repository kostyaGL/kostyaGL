import sys
import os

import argparse

from text_handler import TextHandler

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path + '/file_storage')


class DefaultFileAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        file_pth = self._path_prefix(values)
        if not os.path.isfile(file_pth):
            raise argparse.ArgumentError(self, "Following file does not exist: {}".format(file_pth))
        setattr(namespace, self.dest, file_pth)

    @staticmethod
    def _path_prefix(value):
        if "/" not in value:
            return file_path + "/" + value
        return value


def main(argv):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-f", "--file_path", action=DefaultFileAction,
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
        print "line number:{}:postions:{}".format(i, [i for i in m])
        print "__" * 120
        print s


if __name__ == "__main__":
    main(sys.argv)
