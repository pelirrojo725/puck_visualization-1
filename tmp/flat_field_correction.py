#!/usr/bin/env python
import cv2
from PIL import Image
import sys

# Uses the two images passed in from puck_visulation to convert into
# two channel numpy arrays
INPUT_IMAGE = cv2.imread(sys.argv[1], flags=cv2.IMREAD_GRAYSCALE)
BASE_IMAGE = cv2.imread(sys.argv[2], flags=cv2.IMREAD_GRAYSCALE)

MULTIPLIER = BASE_IMAGE.mean() / INPUT_IMAGE.mean()

INPUT_IMAGE = INPUT_IMAGE * MULTIPLIER
INPUT_IMAGE[INPUT_IMAGE > 255] = 255
INPUT_IMAGE = INPUT_IMAGE.astype('uint8')

NEW_IMAGE = Image.fromarray(INPUT_IMAGE)
NEW_IMAGE.save(sys.argv[1])
