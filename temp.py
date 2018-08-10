import cv2
from matplotlib import pyplot as plt
from consts import *
import numpy as np

src = cv2.imread('samples\sample.jpg')
image = cv2.inRange(src, PACMAN_LOWER, PACMAN_UPPER)
kernel = np.ones((20,20),np.uint8)
cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# color = 'b', 'g', 'r'
# for i, col in enumerate(color):
#     hist = cv2.calcHist([src], [i], None, [256], [5, 256])
#     plt.plot(hist, color=col)
# plt.show()
cv2.imshow('', image)
cv2.waitKey(0)
