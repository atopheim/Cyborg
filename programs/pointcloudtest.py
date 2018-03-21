#!/usr/bin/env python

import cv2
import rospy
import roslib
import sys, time
import numpy as np
from sensor_msgs.msg import PointCloud2

VERBOSE=False

class image_retriever:

	def __init__(self):
		self.subscriber = rospy.Subscriber('/zed/point_cloud/cloud_registered', PointCloud2, self.callback, queue_size = 1)
		if VERBOSE :
			print 'subscribed to zed camera'

	def callback(self, ros_data):
		points = np.fromstring(ros_data.data, np.uint8)
		print points[0:10]
		time.sleep(1000)

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
