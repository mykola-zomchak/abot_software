from parsers.image_parser import  ImageParser
from models.field import Field
import numpy

class FlappyParser(ImageParser):
  def parse(self, image: numpy.ndarray):
      self.field = Field()
      self.field.image = image
      return self.field