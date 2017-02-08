#!/usr/bin/env python

import os
import rospy 
from std_msgs.msg import Int32

if __name__ == '__main__':
	rospy.init_node('start_julius')
	pub = rospy.Publisher('start_julius', Int32, queue_size=1)
	ret = os.system('julius -C main.jconf -C am-gmm.jconf -demo -module 50007') # -charconv EUC-JP UTF-8')
#	print ret
