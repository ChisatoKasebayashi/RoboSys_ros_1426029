#! /usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import print_function
import socket 
from contextlib import closing
import commands
import xml.etree.ElementTree as ET
import rospy
from std_msgs.msg import Int32

def word(recv_data):
	for line in recv_data.split('\n'):
		index = line.find('WORD=')
		if index!=-1:
			line = line[index+6]
			if(line!='<s>' and line!='</s>'):
				return line

def main():
	rospy.init_node('recieve_julius', anonymous=True)
	pub = rospy.Publisher("word_data", Int32, queue_size=1)
	host = 'localhost'
	#port = 50007
	port = 50007
	bufsize = 4096
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host,port))
	while True:
		data = sock.recv(bufsize)
	#	print(data)
		w = word(data)
		if w:
			print(w)
			pub.publish(1)
		else:
			pub.publish(0)
			

#	try:
#		data = ""
#		while True:
#			if "</RECOGOUT>\n." in data:
#				root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.",""))
#				for whypo in root.findall("./SHYPO/WHYPO"):
#					if whypo.get("WORD") in colors.keys():
#						print ("nanika")
#					else:
#						print ("Unknown")
#						data = ""
#			else:
#				data = data + sock.recv(bufsize)
#	except:
#		print("error")

if __name__ == '__main__':
	#try:
	#	rospy.spin()
	#except KeyboardInterrupt:
	#	print("Shutting down")
	main()
