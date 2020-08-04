import cv2
import numpy as np
img=cv2.imread("messi1.jpg")
print(img.shape)   # gives rows,columns and number of channels
print(img.size)    # gives size of the image
print(img.dtype)   # datatype of image
#b,g,r=cv2.split(img)
#img=cv2.merge((b,g,r))
def onclick(event,x,y,flag,para):
    if event==cv2.EVENT_LBUTTONDOWN:
        font=cv2.FONT_HERSHEY_SIMPLEX
        #text=str(x)+","+str(y)
        #cv2.putText(img,text,(x,y),font,0.5,(255,0,0),2)
        cv2.imshow("image",img)

cv2.imshow("image",img)
ball=img[307:347,322:366]    # ROI(region of interestvery important format is [y1:y2,x1:x2]
img[310:350,67:111]=ball


cv2.setMouseCallback("image",onclick)
cv2.waitKey(0) & 0xff==ord('q')

cv2.destroyAllWindows()
