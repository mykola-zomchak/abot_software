import numpy as np
from models.field import Field
from models.characters import Pacman
from parsers.image_parser import ImageParser
import cv2

PACMAN_LOWER = np.array([0, 220, 240])
PACMAN_UPPER = np.array([60, 250, 255])
WALL_LOWER = np.array([190, 60, 10])
WALL_UPPER = np.array([255, 70, 50])


class PacmanParser(ImageParser):

    def parse(self, image: np.ndarray):
        field = Field()
        box = self.__field_rect(image)
        cropped = self.__cropp(image, box)
        pacman = self.__pacman_contour(cropped)
        field.pacman = Pacman(*self.__center(pacman))
        cv2.circle(cropped, (field.pacman.x, field.pacman.y), 2, (0, 0, 255), 2)
        field.image = cropped
        return field

    def __walls(self, image: np.ndarray):
        return cv2.inRange(image, WALL_LOWER, WALL_UPPER)

    def __field_rect(self, image: np.ndarray):
        return cv2.boundingRect(self.__walls(image))

    def __pacman_contour(self, image: np.ndarray):
        pacman = cv2.inRange(image, PACMAN_LOWER, PACMAN_UPPER)
        _, contours, h = cv2.findContours(pacman, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return max(contours, key=lambda c: cv2.contourArea(c))

    def __center(self, contour: np.ndarray):
        M = cv2.moments(contour)
        return int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])

    def __cropp(self, image: np.ndarray, rect: tuple):
        return image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]].copy()