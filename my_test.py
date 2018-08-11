import pyautogui
import screenshooter
import cv2

ss = screenshooter.ScreenShooter("Google Chrome")
cv2.imshow("test", ss.get_screen())
cv2.waitKey()
