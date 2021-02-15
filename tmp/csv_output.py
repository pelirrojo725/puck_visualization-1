import numpy as np
import cv2
import sys

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

file_name = sys.argv[2] + '.csv'

np.savetxt(file_name, img, delimiter=',')
