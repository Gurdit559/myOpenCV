# pyramid representation is a type of multi-scale signal representation in which a signal or an image is subject
# to repeated smoothing and subsampling
# gaussian pyramid , laplacian pyramid

# laplacian: a level in laplacian pyramid is formed by the difference between that level in gaussian pyramid
# and its expanded version of its upper level in guassian pyramid ( no readymade laplacian function present)
import cv2
import numpy as np

img=cv2.imread("messi1.jpg")
lr=cv2.pyrDown(img)   # reduce the resolution of the image
lr2=cv2.pyrDown(lr)
hr=cv2.pyrUp(img)
#cv2.imshow("OG",img)
#cv2.imshow("pyr_d",lr)
#cv2.imshow("pyr_d_2",lr2)
#cv2.imshow("pyr_up",lr)
layer=img.copy()
gp=[layer]                      # gaussian pyramid
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer) # convert integer to string 1st parameter has to be a string

layer=gp[5]
cv2.imshow("upper level guassian pyramid",layer)
lp=[layer]

for i in range(5,0,-1):              #laplacian : works like edge detection
    size = (gp[i - 1].shape[1], gp[i - 1].shape[0])  # the 2 images do not have the  same size so we need to reshape it
    guassian_extended=cv2.pyrUp(gp[i],dstsize=size)
    #cv2.imshow("gg",guassian_extended)
    laplacian=cv2.subtract(gp[i-1],guassian_extended)
    cv2.imshow(str(i),laplacian)

cv2.imshow("OG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
