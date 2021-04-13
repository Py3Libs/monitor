import os
import time
from abstracts.monitor import IFileObserver, IFolderMonitor


class FolderMonitor(IFolderMonitor):

    def __init__(self, src_path=""):
        self.__observers:list[IFileObserver] = []
        self.__src_path = src_path if src_path else os.getcwd()

    def attach(self, observer=None):
        try:
            if observer:
                self.__observers.append(observer)

        except Exception as e:
            raise e

    def detach(self, observer=None):
        try:
            if observer:
                self.__observers.remove(observer)
                
        except Exception as e:
            raise e

    def notify(self, files=[]):
        try:
            for obs in self.__observers:
                obs.update(files)

        except Exception as e:
            raise e

    def start(self, period=60):
        try:
            while True:
                files = [f for f in os.listdir(self.__src_path) if os.path.isfile(os.path.join(self.__src_path, f))]
                if files:
                    self.notify(files)

                time.sleep(period)

        except Exception as e:
            raise e