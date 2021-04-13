from abstracts.monitor import IFileObserver
from monitor import FolderMonitor


class MyFolderObs(IFileObserver):
    
    def update(self, files=[]):
        print("show files...")
        for f in files:
            print(f)

if __name__ == "__main__":
    try:
        obs = MyFolderObs()

        test_path = "your watched directory."
        monitor = FolderMonitor(test_path)
        monitor.attach(obs)
        monitor.start(10)

    except Exception as e:
        raise e