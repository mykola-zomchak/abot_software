from abc import ABC, abstractmethod


class ParsedScreen(ABC):
    @property
    @abstractmethod
    def image(self): pass
