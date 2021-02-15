#!/usr/bin/env python
import cv2
import sys

img = cv2.imread(sys.argv[1], 0)
img = cv2.addWeighted(img, 1.5, img, 0, 0)
img = cv2.bilateralFilter(img, 7, 50, 50)
cv2.imwrite(sys.argv[1], img)
