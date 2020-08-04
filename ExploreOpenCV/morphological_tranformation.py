# morphological transformation are simple operations based on image shape
# performed on a binary image
# 2 things required: original image and structuring element or kernel
# kernel: tell u how to change the value of any given pixel by combining it with different amounts of
#         neighbouring pixels

import cv2
import matplotlib.pyplot as plt
import numpy as np
#img=cv2.imread("smarties.png",cv2.IMREAD_GRAYSCALE)
img=cv2.imread("j.png",cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)       # 2X2 square shape kernal
dilation=cv2.dilate(mask,kernal,iterations=3)     # kernal is a shape we want to apply on the image
# removes black spots on masked image
erosion=cv2.erode(mask,kernal,iterations=2) #erodes the boundaries of objects in image
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) # erosion followed by dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) # first dilation then erosion is applied
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) # difference between dilation and erosion of image
mbh=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal)
mm=cv2.morphologyEx(mask,cv2.MORPH_HITMISS,kernal)

title=["smarties","mask","dilation","erosion","opening","closing","mgradient","blackhat","hitmiss"]
images=[img,mask,dilation,erosion,opening,closing,mg,mbh,mm]
for i in range(len(images)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
