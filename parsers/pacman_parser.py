import numpy as np
from models.field import Field
from parsers.image_parser import ImageParser
import cv2


class PacmanParser(ImageParser):

    def parse(self, image: np.ndarray):
        field = Field()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        box = self._field_rect(hsv)
        image = self._cropp(image, box)
        cropped = self._cropp(hsv, box)

        pacman = self._contour(cropped, PACMAN_LOWER, PACMAN_UPPER)
        field.update_pacman(self._center(pacman) if pacman is not None else (-1, -1))

        ghosts = tuple((g[0], self._contour(cropped, g[1], g[2])) for g in GHOSTS)
        for ghost in ghosts:
            field.update_ghost(ghost[0], self._center(ghost[1]) if ghost[1] is not None else (-1, -1))

        for g in field.ghosts.values():
            cv2.circle(image, (g.x, g.y), 2, (0, 0, 0), 2)
        cv2.circle(image, (field.pacman.x, field.pacman.y), 2, (0, 0, 255), 2)

        field.image = image
        return field

    def _walls(self, image: np.ndarray):
        return cv2.inRange(image, WALL_LOWER, WALL_UPPER)

    def _field_rect(self, image: np.ndarray):
        return cv2.boundingRect(self._walls(image))

    def _contours(self, image: np.ndarray, lower: np.ndarray, upper: np.ndarray, min_area=None):
        mask = cv2.inRange(image, lower, upper)
        if mask is None:
            return []
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]
        if min_area is None:
            return contours
        return filter(lambda c: cv2.contourArea(c) >= min_area, contours)

    def _contour(self, image: np.ndarray, lower: np.ndarray, upper: np.ndarray):
        contours = self._contours(image, lower, upper)
        if len(contours) == 0:
            return None
        return max(contours, key=lambda c: cv2.contourArea(c))

    def _center(self, contour: np.ndarray):
        M = cv2.moments(contour)
        try:
            return int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
        except ZeroDivisionError:
            return contour[0][0]

    def _cropp(self, image: np.ndarray, rect: tuple):
        return image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]].copy()


PACMAN_LOWER = np.array((25, 160, 140))
PACMAN_UPPER = np.array((40, 255, 255))
WALL_LOWER = np.array((110, 190, 190))
WALL_UPPER = np.array((120, 230, 255))

GHOSTS = (('Blinky', np.array((130, 100, 210)), np.array((180, 255, 255))),
          ('Pinky', np.array((160, 50, 50)), np.array((180, 100, 255))),
          ('Inky', np.array((70, 120, 170)), np.array((110, 200, 255))),
          ('Clyde', np.array((10, 180, 220)), np.array((20, 255, 255))))
