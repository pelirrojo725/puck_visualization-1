import cv2
import numpy as np
import sys

image = cv2.imread(sys.argv[1], 1)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
b = clahe.apply(image[:, :, 0])
g = clahe.apply(image[:, :, 1])
r = clahe.apply(image[:, :, 2])
equalized = np.dstack((b, g, r))
cv2.imwrite(sys.argv[1], equalized)
