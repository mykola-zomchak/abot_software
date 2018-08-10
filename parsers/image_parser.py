from abc import ABC, abstractmethod
import numpy


class ImageParser(ABC):

    @abstractmethod
    def parse(self, image: numpy.ndarray): pass
