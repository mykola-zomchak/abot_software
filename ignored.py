import cv2
import parsers.pacman_parser as pp
src = cv2.imread('samples/cropped.jpg')
field = pp.PacmanParser().parse(src)
cv2.imshow('pacman', field.image)
cv2.waitKey(0)