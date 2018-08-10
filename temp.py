import cv2
from matplotlib import pyplot as plt
from consts import *
import numpy as np

src = cv2.imread('samples\sample.jpg')
pacmans = cv2.inRange(src, PACMAN_LOWER, PACMAN_UPPER)
kernel = np.ones((5,5))
pacmans = cv2.morphologyEx(pacmans, cv2.MORPH_CLOSE, kernel)
pacmans = cv2.morphologyEx(pacmans, cv2.MORPH_OPEN, kernel)

blue = np.zeros(src.shape, dtype=np.uint8)
blue[:] = (0, 255, 0)
blue = cv2.bitwise_and(blue, blue, mask = pacmans)


cv2.imshow('', cv2.subtract(src, blue))
cv2.waitKey(0)
