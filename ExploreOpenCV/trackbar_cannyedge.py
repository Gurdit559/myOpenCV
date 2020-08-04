import cv2
import numpy as np
cv2.namedWindow("image")

def position(x):
    pass
cv2.createTrackbar("tb1","image",0,255,position)
cv2.createTrackbar("tb2","image",0,255,position)
while (True):
    img = cv2.imread("messi1.jpg", cv2.IMREAD_GRAYSCALE)
    pos=cv2.getTrackbarPos("tb1","image")
    pos2=cv2.getTrackbarPos("tb2","image")
    canny = cv2.Canny(img, pos, pos2)
    cv2.imshow("image",canny)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()