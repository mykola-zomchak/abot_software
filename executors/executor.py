from abc import ABC, abstractmethod


class Executor(ABC):

    @property
    @abstractmethod
    def window_name(self): pass

    @property
    @abstractmethod
    def region(self): pass

    @abstractmethod
    def __enter__(self): pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb): pass
