# 1) smoothing to remove noise from the image
# 2) homogeneous filter is the most simple filter each output pixel is the mean of its kernel neighbours
# 3)  in image processing a kernel, convolution matrix or mask is a small matrix , it is used to blurring,sharpening
# ,embossing,edge detection and more.

# 4) in 1 D signals images can be filtered with various low pass filters (LPF) high pass filters (HPF)
# 5) LPF- helps in removing noise from the imaage
# 6) HPF - helps in finding edges in the images
# 7) guassian filter is nothing but using different-weight-kernel, in both x and y direction
# 8) median filter is something that replaces each pixel value with the median of its neighbouring pixel
# this method is great when dealing with salt and pepper noise
# 9) bilateral filter-A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing
# filter for images. It replaces the intensity of each pixel with a weighted average of intensity values
# from nearby pixels. (used when u have to preserve edges)
import cv2        # bgr format
import matplotlib.pyplot as plt   # rgb format
import numpy as np

#img=cv2.imread("opencv-logo.png")
img=cv2.imread("class.png")
#img=cv2.imread("g_blur.jpg")
#cv2.imshow("image",img)
#img=cv2.imread("saltnpepper.jpg")
#img=cv2.imread("lena.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))  #averaging
gblur=cv2.GaussianBlur(img,(5,5),0) # inner values have more weight and outer values will be lesser in matrix
median=cv2.medianBlur(img,3) # 3/ kernel size must always be odd and 1 will give original image
bilat=cv2.bilateralFilter(img,9,75,75) #remove noise and keep edges sharp
title=["OG","2D","blur","gblur","median","bilateralfilter"]
images=[img,dst,blur,gblur,median,bilat]
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()