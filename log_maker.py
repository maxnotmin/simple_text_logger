#!/usr/bin/python3
import os, sys
import datetime
import time
from inspect import currentframe, getframeinfo
import hashlib
import json
from collections import deque


class SimpleLogMaker():
    """
    This class should be use to log errors and successes of submitted data to a function.
    You can give a path to a an existing directory or give it a name of a new directory
    to write your logs to.
    Args:
        :param the_data =  list, str, bool, dict, None
        :param the_error = Exception Error
        :param the_status = REST call status if there is one
        :param the_dir_name = the path to the directory where the logs will be written
        :param the_log_name = the base name of each logfile

    It's best used within a TRY EXCEPT
    Example usage:

        def YouFunction(your_data=[{}]):
            try:
                the_path_to_logs = r'main_dir/log_dir'
                the_log = ITPALogMaker(the_data=your_data,
                                       the_dir_name=the_path_to_logs,
                                       log_note='This is some a note about the log')
                the_log.make_dir()
                the_log.make_log()
            except Exception as my_error:
                the_log = ITPALogMaker(the_data=your_data,
                                       the_error=my_error,
                                       the_dir_name=the_path_to_logs,
                                       log_note='This is some a note about the log')
                the_log.make_dir()
                the_log.make_log()
    Depending on the size / length of the data, it will only write a limited amount of the data
    to cut down on file size.
    Example:
         If your data is a list with over 100 items, it will only write list[0:100]

    """

    def __init__(self, the_data, the_error='', the_status=None, the_dir_name='',
                  the_log_name='', log_note=''):
        self.the_data = the_data
        self.raw_data = None
        self.the_error = the_error
        self.the_status = the_status
        self.log_note = log_note
        self.the_dir_name = the_dir_name
        self.the_log_name = the_log_name
        self.ab_path = os.path.abspath(__file__)
        self.cur_dir = os.getcwd()

    def make_dir(self):
        """
        This function will create a directory for your log files if it does not already exist
        :return: None
        """
        if not os.path.exists(self.the_dir_name):
            os.makedirs(self.the_dir_name)

    def make_log(self):
        """
        This will write a file to log the data, success | error of
        :return: None
        """
        self.make_dir()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.the_dir_name + "/" + self.the_log_name + "_" + str(timestr) + ".txt", "w") as file:
            file.write("######## " + str(now_time) + " ########")
            file.write("\n")
            file.write(self.log_note)
            file.write("\n")
            file.write("\n")
            file.write("######## " + "WHAT SCRIPT CALLED LOG MAKER" + " ########")
            file.write("\n")
            file.write(str(self.ab_path))
            file.write("\n")
            file.write("\n")
            file.write("######## " + "THE DATA" + " ########")
            file.write("\n")
            file.write(str(self.the_data))
            file.write("\n")
            file.write("\n")
            if len(self.the_error) > 2:
                file.write("######## " + "ERROR" + " ########")
                the_line_num = getframeinfo(currentframe())
                file.write("\n")
                file.write("LINE: " + str(the_line_num.lineno))
                file.write("\n")
                file.write(str(self.the_error))
                file.write("\n")
                file.write("\n")
            if self.the_status is not None:
                file.write("######## " + "REST STATUS" + " ########")
                file.write("\n")
                file.write(str(self.the_status))
                file.write("\n")
                file.write("\n")

    def __repr__(self):

        all_the_data = {
            'calling_file': __file__,
            'the_data': str(self.the_data),
            'the_error': str(self.the_error),
            'the_dir_name': str(self.the_dir_name),
            'the_log_name': str(self.the_log_name)
        }

        line1 = "ITPALogMaker was called by {calling_file} with the attributes of:"
        line2 = "\n"
        line3 = "the_data : {the_data}"
        line4 = "\n"
        line5 = "the_error : {the_error}"
        line6 = "\n"
        line7 = "the_dir_name : {the_dir_name}"
        line8 = "\n"
        line9 = "the_log_name : {the_log_name}"

        main_text = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9
        print("__repr__: ", all_the_data['calling_file'])
        return main_text.format(calling_file=all_the_data['calling_file'],
                                the_data=all_the_data['the_data'],
                                the_error=all_the_data['the_error'],
                                the_dir_name=all_the_data['the_dir_name'],
                                the_log_name=all_the_data['the_log_name'])

    #TODO Implement 'WITH OPEN' better
    #def __enter__(self):
    #    if self.the_data is None:
    #        self.the_data = []
    #        raise IOError("NO DATA")
    #        return self.the_data


    #TODO Implement 'WITH OPEN' better
    #def __exit__(self, exc_type, exc_val, exc_tb):
    #    self.the_data = self.raw_data
    #    return self.the_data