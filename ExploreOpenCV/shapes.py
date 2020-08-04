import cv2
import numpy as np
#img=cv2.imread("lena.jpg",1)   #0 if greyscale and 1 if colored

img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(150,150),(0,255,0),5)  #image,start coordinate,endcoordinate,color(bgr),thickness
img=cv2.arrowedLine(img,(150,150),(200,200),(0,0,255),8)
img=cv2.rectangle(img,(20,20),(190,190),(250,0,0),4)  #put -1 instead of 4 to fill the shape
img=cv2.circle(img,(110,120),50,(0,255,0),-1)
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
img=cv2.putText(img,"LENA",(20,90),font,3,(255,255,255),6,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()