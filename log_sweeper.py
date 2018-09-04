#!/usr/bin/python
import os, sys
import time
import datetime


class SimpleLogSweep():
    """
    This class is used to delete files past a certain date. You'll need to provide a directory and
    and a number of days. This class scans through the give folder and gets the DATE MODIFIED of
    each file. If the DATE MODIFIED is older than the give DEL_PATE_DATE, that file will be removed.
    FOVEREVER!
    Args:
        :param the_sweep_dir
        :param del_past_date

    Example you want want to delete all files past the 30 day mark:
    del_files = ITPALogSweep(the_sweep_dir='my_folder', del_past_date=30)
    del_files.delete_files()
    """

    def __init__(self, the_sweep_dir='', del_past_date=30):
        self.the_sweep_dir = the_sweep_dir
        self.del_past_date = del_past_date
        self.now_time = time.time()
        self.desire_del_date = self.days_to_seconds()


    def delete_files(self):
        all_files_in_dir = os.listdir(self.the_sweep_dir)
        delete_date = self.now_time - self.desire_del_date
        print("MASTER DELETE DATE: ", datetime.datetime.fromtimestamp(delete_date))
        for file in all_files_in_dir:
            try:
                the_file_path = self.the_sweep_dir + "/" + file
                print("FILE: ", the_file_path)
                time_file = os.path.getmtime(the_file_path)
                print("MASTER FILE TIME: ", datetime.datetime.fromtimestamp(time_file))
                if delete_date > time_file:
                    print("DELETE THE FILE: ", the_file_path)
                    os.remove(the_file_path)
                else:
                    print("DONT DELETE")
            except Exception as e:
                print("ERROR: ", e)

    def days_to_seconds(self):
        seconds_in_day = 86400
        int_desire = int(self.del_past_date)
        return seconds_in_day * int_desire