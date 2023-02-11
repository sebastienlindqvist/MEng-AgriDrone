import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import argparse
import imutils
import math

class CV:
    def __init__(self):
        self.Photo=0
        self.Photo_copy=0
        self.closest_X=0
        self.closest_Y=0
        
    def get_Photo(self):
        self.Photo=cv2.imread('/home/pi/Desktop/Drone/image.jpg')
        self.Photo=cv2.resize(self.Photo,(1920,1080))
        self.Photo_copy=np.copy(self.Photo)

    def HSV_green(self):
        green_centre=60
        sensitivity=35
        hsv=cv2.GaussianBlur(self.Photo_copy, (13,13),0)
        hsv=cv2.cvtColor(hsv,cv2.COLOR_BGR2HSV)
        lower_green=np.array([green_centre-sensitivity,180,25])
        upper_green=np.array([green_centre+sensitivity,255,255])
        mask1=cv2.inRange(hsv, lower_green, upper_green)
        self.Photo_copy = cv2.bitwise_and(self.Photo_copy, self.Photo_copy, mask= mask1)

    def thresh(self):
        self.Photo_copy=cv2.cvtColor(self.Photo_copy,cv2.COLOR_BGR2GRAY)
        self.Photo_copy = cv2.GaussianBlur(self.Photo_copy, (37, 37), 0)
        self.Photo_copy=cv2.threshold(self.Photo_copy,50,255,cv2.THRESH_BINARY)[1]

    def contours(self):
        cnts = cv2.findContours(self.Photo_copy, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print (cnts)
        cnts = imutils.grab_contours(cnts)
        # loop over the contours
        for c in cnts:
	# compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(self.Photo, [c], -1, (0, 255, 0), 2)
            cv2.circle(self.Photo, (cX, cY), 7, (255, 255, 255), -1)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(self.Photo,(x,y),(x+w,y+h),(255, 255, 255),2)
            cv2.putText(self.Photo, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            #
            if math.sqrt((abs(960-cX)**2)+(abs(540-cY)**2)) < math.sqrt((abs(960-self.closest_X)**2)+(abs(540-self.closest_Y)**2)):
                #finding cloests centre point to centre of camera
                self.closest_X=cX
                self.closest_Y=cY
                #checking if the plants are overlapping
                #print(x+w)
                #print(y+h)
                #print((x+w)/(y+h))
                if (x+w)/(y+h)>1.4:
                    if int(((x+w)/(y+h)))%2==0:
                        cv2.circle(self.Photo, (cX-int(h/2), cY), 7, (255, 0, 0), -1)
                        self.closest_X=cX-int(h/2)
                elif (y+h)/(x+w)>1.4:
                    if int(((y+h)/(x+w)))%2==0:
                        cv2.circle(self.Photo, (cX, cY-int(w/2)), 7, (255, 0, 0), -1)
                        self.closest_Y=cY-int(w/2)
                    
        #print(self.closest_X)
        #print(self.closest_Y)
    def Centre(self):
        self.get_Photo()
        self.HSV_green()
        self.thresh()
        self.contours()
        return self.closest_X,self.closest_Y
            


    def Show(self):
        cv2.imshow('viewer',self.Photo)
        cv2.waitKey()

#computerV=CV()  
#computerV.get_Photo()
#computerV.HSV_green()
#computerV.thresh()
#computerV.contours()
#computerV.Show()
