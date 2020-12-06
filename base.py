import os
from os.path import isdir, isfile, join


class Base():
    def __init__(self, dir):
        self.dir = dir
    
    def __get_files(self, file_dir_list):
        """
        Returns all the files in the
        list of files and directories

        Args:
            file_dir_list (list)
        """

        return [f for f in os.listdir(self.dir) if isfile(join(self.dir, f))]
    
    def __get_directories(self, file_dir_list):
        """
        Returns all the files in the
        list of files and directories

        Args:
            file_dir_list (list)
        """

        return [f for f in os.listdir(self.dir) if isdir(join(self.dir, f))]
    
    def get_output(self):
        """
        Returns the files and directories of
        the current directory passed
        """

        file_dir_list = os.listdir(self.dir)

        return self.__get_files(file_dir_list), \
            self.__get_directories(file_dir_list)
