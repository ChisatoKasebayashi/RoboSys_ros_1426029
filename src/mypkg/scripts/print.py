#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def input_data(message):
	print("-----------Received words------------")

if __name__ == '__main__':
	rospy.init_node('print')
	sub = rospy.Subscriber('word_data',Int32,input_data)
	rate = rospy.Rate(1)
 	while not rospy.is_shutdown():
		rate.sleep()
