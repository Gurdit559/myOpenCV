# Contours : curve joining all the continous points along the boundary which are having
# the same colour and intensity
# usefull tool for shape analysis,object detection or object recognition
# for better accuracy generally use binary image for finding the contour(gray scale)


import cv2
import numpy as np
img=cv2.imread("opencv-logo.png")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(imgray,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# above contours variable is a python list of all the contours in the image.Each individual contours is a numpy
# array of coordinate (x,y) coordinates of boundary points of the object
# hierarchy contains info about image topology
print("number of contours ="+str(len(contours)))

print(contours[0])
cv2.drawContours(img,contours,11,(0,255,0),3)  # -1 will draw all 9 contours that we found
cv2.imshow("image Gray",imgray)
cv2.imshow("OG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#The main difference between the modes is in the hierarchy that is returned (giving the relationship between one contour and the next).

#CV_RETR_EXTERNAL gives "outer" contours, so if you have (say) one contour enclosing another (like concentric circles), only the outermost is given.
#CV_RETR_LIST gives all the contours and doesn't even bother calculating the hierarchy -- good if you only want the contours and don't care whether one is nested inside another.
#CV_RETR_CCOMP gives contours and organises them into outer and inner contours. Every contour is either the outline of an object, or the outline of an object inside another object (i.e. hole). The hierarchy is adjusted accordingly. This can be useful if (say) you want to find all holes.
#CV_RETR_TREE calculates the full hierarchy of the contours. So you can say that object1 is nested 4 levels deep within object2 and object3 is also nested 4 levels deep.