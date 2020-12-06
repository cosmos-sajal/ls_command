import getopt, sys


class Main():
    def __init__(self):
        self.argument_list = sys.argv[1:]
        self.options = "laR"
        self.arguments, self.values = \
            getopt.getopt(self.argument_list, self.options, [])
    
    def parse_arguments(self):
        for arg, value in self.arguments:
            print(arg)
            print(value)


if __name__ == "__main__":
    main = Main()
    main.parse_arguments()
