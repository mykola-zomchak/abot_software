from parsers.image_parser import  ImageParser
from models.flappy_grid import FlappyGrid
from games.flappy.flappy import SCREENWIDTH, SCREENHEIGHT
import numpy as np
import cv2

class FlappyParser(ImageParser):
  templates_names = ["parsers/templates/Flappy_Bird_Icon_Template.png"]
  templates = []


#записувати темплейти в словник
  def __init__(self):
    #for name in self.templates_names:
     # self.templates.append(cv2.imread(self.templates_names))
    pass

  def parse(self, image: np.ndarray):
      self.field = FlappyGrid()
      self.field.image = image

      self.template = cv2.imread("parsers/templates/Flappy_Bird_Icon_Template.png")
      top_left, bottom_right = self._get_area(self.field.image, self.template)
      image_copy = self.field.image.copy()
      cv2.rectangle(image_copy, top_left, bottom_right, (0, 255, 255))

      cv2.imshow("Image", image_copy)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

      return self.field


  def _fill_grid(self):
    pass

  def _get_area(self, image: np.ndarray, template: np.ndarray):
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = (max_loc[0] + 45, max_loc[1] + 25)
    bottom_right = (top_left[0] + SCREENWIDTH - 55, top_left[1] + SCREENHEIGHT - 110)
    return (top_left, bottom_right)

  def __find_bird(self):
    pass

  def _find_hole(self):
    pass
