#usr/bin/env python3

import numpy as np
import math as m
import time as t

threshold = 0.7
max_objects = 10
valid_boxes = []

for i in range(max_objects):
	if detection_score[i] > threshold:
		valid_boxes.append(detection_boxes[i])

midpoints = []
num_boxes = len(valid_boxes)
for i in range(num_boxes):
	x = valid_boxes[i][3] - valid_boxes[i][1]
	y = valid_boxes[i][2] - valid_boxes[i][0]
	midpoints.append(x,y)


