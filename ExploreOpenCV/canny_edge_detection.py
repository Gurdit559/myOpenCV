# canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect wide range of
# edges in images
# canny edge detection algo has 5 steps  (better than other gradient image methods)
# 1) noise reduction
# 2) gradient calculation
# 3) non-maximum suppression
# 4) double threshold
# 5) edge tracking by hysteresis

import cv2
import matplotlib.pyplot as plt
import numpy as np

tb=cv2.createTrackbar("t1",)
img=cv2.imread("messi1.jpg",cv2.IMREAD_GRAYSCALE)
canny=cv2.Canny(img,100,200)

title=["OG","canny"]
images=[img,canny]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()