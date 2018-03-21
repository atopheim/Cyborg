#!/usr/bin/env python

import cv2
import rospy
import roslib
import sys, time
import numpy as np
from sensor_msgs.msg import Image

VERBOSE=False

class image_retriever:

	def __init__(self):
		self.subscriber = rospy.Subscriber('/zed/depth/depth_registered', Image, self.callback, queue_size = 1)
		if VERBOSE :
			print 'subscribed to zed camera'

	def callback(self, ros_data):
		image = np.fromstring(ros_data.data, np.uint8)
		image = image.reshape((720, 1280, 4))
		cv2.imshow("image", image)
		#cv2.imwrite(r"/home/nvidia/ZED.jpg", image)
		cv2.waitKey(35)

def main(args):
	'''Initializes and cleanup ros node'''
	ir = image_retriever()
	rospy.init_node('image_retriever', anonymous=True)
   	try:
		rospy.spin()
	except KeyboardInterrupt: 
		print "Shutting down ROS Image feature detector module"
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
