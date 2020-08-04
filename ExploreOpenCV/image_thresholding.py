# thresholding is a popular segmentation technique
# used for seperating an object from a background
# the process involves comparing each pixel of an image with a predefined threshold value
# divides all the pixel of the input image into 2 groups
# first group involves pixels having lower than the threshold value and the group 2 contains
# pixels higher than the threshold value.

import cv2
import numpy as np

img=cv2.imread("gradient.jpg")
#cv2.imshow("image",img)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)# thresholding gives 2 results ret and thresholded value of an image

_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()

# binary threshold either 0 or 1 black or white in our image

# binary thresholding:  if pixel value is less than 127 then pixel value is assigned 0 (black) and above 127 pixels assigned value 255(white)

# binary_inv thresholding vice versa opposite of above

# binary_trunc : upto threshold value pxels will remain same and after that value it will change

# thresh_tozero : if pixel value is less than threshold the pixel value is assigned to 0

