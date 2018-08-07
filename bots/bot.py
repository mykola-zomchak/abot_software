from abc import ABC, abstractmethod
from types import FunctionType

from field import Field


class Bot(ABC):

    @abstractmethod
    def get_action(self, field: Field) -> FunctionType: pass
