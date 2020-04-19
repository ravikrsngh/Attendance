import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
import pytz
from datetime import datetime, timedelta
import time
# import urllib3
# url='http://192.168.43.240:8080/shot.jpg'
# cap=cv2.VideoCapture(0)
# while(cap.isOpened()):
# 	r, frame = cap.read()
# 	cv2.imshow(('Camera', frame)
# 	if(cv2.waitKey(1)& 0xFF == ord('q')):
#
# 		break
# cap.release()
# cv2.destroyAllWindows()
def start_record():
	filename= 'xyz.mp4'
	frames_per_second = 60.0
	my_res = '720p'

	def change_res(cap,width,height):
		cap.set(3,width)
		cap.set(4,height)

	STD_DIMENSIONS = {
		"480p":(640,480),
		"720p":(1280,720),
		"1080p":(1920,1080),
		"4k":(3840,2160),
	}



	def get_dims(cap,res='1080p'):
		width,height = STD_DIMENSIONS['480p']
		if res in STD_DIMENSIONS:
			width,height = STD_DIMENSIONS[res]
		change_res(cap,width,height)
		return width,height


	VIDEO_TYPE = {
	    'avi': cv2.VideoWriter_fourcc(*'XVID'),
	    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
	    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
	}

	def get_video_type(filename):
	    filename, ext = os.path.splitext(filename)
	    if ext in VIDEO_TYPE:
	      return  VIDEO_TYPE[ext]
	    return VIDEO_TYPE['mp4']


	cap=cv2.VideoCapture(0)
	out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, my_res))
	# dims=get_dims(cap,res=my_res)
	t=datetime.now(tz=pytz.utc)
	t1=(t + timedelta(seconds=10))
	while True:
		ret, frame = cap.read()
		out.write(frame)
		cv2.imshow('frame',frame)
		t2=datetime.now(tz=pytz.utc)
		if cv2.waitKey(24) and t2>t1:
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()
