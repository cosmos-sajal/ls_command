#!/usr/local/bin/python3

import os 
import getopt, sys

from base import Base
from print_output import Print


class Main():
    def __init__(self):
        self.argument_list = sys.argv[1:]
        self.options = "laR"
        self.arguments, self.values = \
            getopt.getopt(self.argument_list, self.options, [])
        self.cwd = os.getcwd()
    
    def parse_arguments(self):
        base_obj = Base(self.cwd)
        files, dirs = base_obj.get_output()
        
        print_obj = Print(files, dirs)
        print_obj.print_output()

        # for arg, value in self.arguments:
        #     print(arg)
        #     print(value)


if __name__ == "__main__":
    main = Main()
    main.parse_arguments()
