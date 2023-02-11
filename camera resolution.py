import cv2

im = cv2.imread("/home/pi/Desktop/Drone/1.jpg")

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
