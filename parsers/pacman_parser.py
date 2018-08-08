import numpy
from models.field import Field
from parsers.image_parser import ImageParser


class PacmanParser(ImageParser):

    def parse(self, image: numpy.ndarray) -> Field:
        return Field()
