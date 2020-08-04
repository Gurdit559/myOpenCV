import cv2
img=cv2.imread("sudoku.jpg")

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#To use adaptive threshold the src image must be in greyscale

# 2 ways to do adaptive thresholding
th2=cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,6)

# here 11 is blocksize (decides the size of the neighbourhood area) and 6 is value of c(constant subtracted from the mean)

th3=cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,6)
cv2.imshow("image",img)
cv2.imshow("image1",th1)
cv2.imshow("th1",img_grey)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
