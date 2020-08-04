# image gradient - is directional change in the intensity or color in an image.


import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("messi1.jpg",cv2.IMREAD_GRAYSCALE)
#img=cv2.imread("sudoku.jpg",cv2.IMREAD_GRAYSCALE)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)# cv_64F is a datatype it can accept negative numbers as well
lap=np.uint8(np.absolute(lap)) # find absolute and convert into usigned 8 bit integer(edge detect)
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0) # 1 for x direction (order of derivative x) and 0 for y
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1) # 1 for y direction (order of derivative y) and 0 for x
sobelX=np.uint8(np.absolute(sobelX)) # (vertical)
sobelY=np.uint8(np.absolute(sobelY)) # unsigned int conversion  (horizontal)
sobelcombined=cv2.bitwise_or(sobelX,sobelY) # add the 2

title=["Messi","laplacian","sobelX","sobelY","sobelcombined"]
images=[img,lap,sobelX,sobelY,sobelcombined]
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()