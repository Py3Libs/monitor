import abc


class IObserver(abc.ABC):

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError


class IFileObserver(IObserver):

    @abc.abstractmethod
    def update(self, files:list):
        raise NotImplementedError


class ISubject(abc.ABC):

    @abc.abstractmethod
    def attach(self, observer:IObserver):
        raise NotImplementedError

    @abc.abstractmethod
    def detach(self, observer:IObserver):
        raise NotImplementedError

    @abc.abstractmethod
    def notify(self):
        raise NotImplementedError


class IFolderMonitor(ISubject):

    @abc.abstractmethod
    def __init__(self, src_path:str):
        raise NotImplementedError

    @abc.abstractmethod
    def notify(self, files:list):
        raise NotImplementedError

    @abc.abstractmethod
    def start(self, period:int):
        raise NotImplementedError