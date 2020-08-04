import cv2
import numpy as np
# masks are the binary images that indicate the pixel in which an operation is to be
#performed
img=cv2.imread("blackwhite.jpg")
print(img.shape)
img2=np.zeros((339,509,3),np.uint8)
cv2.rectangle(img2,(200,0),(300,100),(255,255,255),-1)
bitand=cv2.bitwise_and(img,img2)
bitor=cv2.bitwise_or(img,img2)
bitnot=cv2.bitwise_not(img)
bitxor=cv2.bitwise_xor(img,img2)
cv2.imshow("image",img)
cv2.imshow("image2",img2)
cv2.imshow("image3",bitand)
cv2.imshow("image4",bitor)
cv2.imshow("image5",bitnot)
cv2.imshow("image6",bitxor)

cv2.waitKey(0)
cv2.destroyAllWindows()