import json
import datetime
import os


class TaskManeger:
    def __init__(self, path_file, to_do_list):
        self.path_file = path_file
        self.to_do_list = to_do_list
        self.loading_task()

    def loading_task(self):
        pass
