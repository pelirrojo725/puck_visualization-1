import cv2
import os
import sys

base_dir = '/home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/var/model_data/Temp'
input_dir = '/home/samuel/Desktop/Classes/CSC_300/puck_visualization_system/puck_visualization_program/var/model_data/cropped_unsorted'

my_files = [f for f in os.listdir(base_dir)]

# base_x and base_y are the x and y of the first position crop
# if the camera is moved recrop position one and set the base_x and base_y to the new x and y value
# do not change the width or height
base_x = 415
base_y = 456
w = 143
h = 141


for files in my_files:
     fbase = files.split('.')[0]
     img = cv2.imread(base_dir + '/' + files)
     
     # Do not change the x and y offsets in the lists
     x = [0, 95, 252, 252, 99, -160, -114, 12,
          179, 333, 429, 429, 337, 186, 18, -112]

     y = [0, -131, -84, 78, 133, 2, -160, -274,
          -299, -231, -90, 80, 227, 295, 276, 165]

     count = 1
     for x, y in zip(x, y):
          filename = input_dir + '/' + fbase + '_' + str(count) + '.jpg'

          new_x = base_x + x
          new_y = base_y + y

          crop_img = img[new_y:new_y + h, new_x:new_x + w]
          cv2.imwrite(filename, crop_img)

          count += 1
