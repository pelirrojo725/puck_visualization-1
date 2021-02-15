#!/usr/bin/env python3
import cv2
import sys

count = 1.0

for i in range(1, 2):
    img = cv2.imread(sys.argv[1], 1)
    img = cv2.addWeighted(img, count, img, 0, 0)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img_canny = cv2.Canny(img, 25, 75)
    img = cv2.bitwise_not(img_canny)
    filename = sys.argv[2] + "/" + sys.argv[3] + ".pgm"
    cv2.imwrite(filename, img)
    count += .1
