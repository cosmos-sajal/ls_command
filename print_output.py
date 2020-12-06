class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Print():
    def __init__(self, files, dirs):
        self.files = files
        self.dirs = dirs
    
    def __get_printable_string(self, list_of_str):
        """
        Retunrs a printable string from a list

        Args:
            list_of_str (list)
        """

        separator_string = '    '

        return separator_string.join(
            [str(elem) for elem in list_of_str]
        )
    
    def print_output(self):
        file_str = self.__get_printable_string(self.files)
        dir_str = self.__get_printable_string(self.dirs)

        print(f"{file_str}    {bcolors.OKGREEN}{dir_str}{bcolors.ENDC}")
