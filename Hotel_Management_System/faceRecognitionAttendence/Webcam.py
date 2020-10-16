from cv2 import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings

fd_WebCam = cv2.CascadeClassifier(os.path.join(
    settings.BASE_DIR, 'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))


class MyWebCam(object):

    def __init__(self):
        self.seen = cv2.VideoCapture(0)


    def get_video(self):
        bin , img = self.seen.read()

        grayImg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        faces = fd_WebCam.detectMultiScale(grayImg , 1.3 , 5)
        for(x , y , w , h) in faces:
            cv2.rectangle(img , (x, y) , (x + w , y + h) , (255 , 0 , 0) , 2)
        flip_Frame = cv2.flip(img , 1)
        ret , jpeg = cv2.imencode('.jpg' , flip_Frame)
        return jpeg.tobytes()
    
    def __del__(self):
        self.seen.release()
