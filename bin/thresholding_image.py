#!/usr/bin/env python3
import cv2
import sys
import numpy as np

image = cv2.imread(sys.argv[1], 1)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
b = clahe.apply(image[:, :, 0])
g = clahe.apply(image[:, :, 1])
r = clahe.apply(image[:, :, 2])
equalized = np.dstack((b, g, r))
cv2.imwrite(sys.argv[1], equalized)

img = cv2.imread(sys.argv[1], 0)
img = cv2.medianBlur(img, 9)
img = cv2.dilate(img, (7, 7), iterations=1)
# img = cv2.bilateralFilter(img, 3, 75, 75)
img = cv2.adaptiveThreshold(img, 250, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 13, 1)
cv2.imwrite(sys.argv[1], img)
