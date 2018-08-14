from abc import ABC, abstractmethod

from models.parsed_screen import ParsedScreen


class Bot(ABC):

    @abstractmethod
    def make_action(self, parsed: ParsedScreen): pass
