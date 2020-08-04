import cv2
import numpy as np
img=cv2.imread("smarties.png")

def nothing(x):
    pass

cap=cv2.VideoCapture(0);
cv2.namedWindow("tracker")
cv2.createTrackbar("LH","tracker",0,255,nothing)
cv2.createTrackbar("LS","tracker",0,255,nothing)
cv2.createTrackbar("LV","tracker",0,255,nothing)
cv2.createTrackbar("UH","tracker",255,255,nothing)
cv2.createTrackbar("US","tracker",255,255,nothing)
cv2.createTrackbar("UV","tracker",255,255,nothing)

while(True):
    #cv2.imshow("image",img)
    _, img=cap.read()
    lh=cv2.getTrackbarPos("LH","tracker")
    ls=cv2.getTrackbarPos("LS","tracker")
    lv=cv2.getTrackbarPos("LV","tracker")
    uh=cv2.getTrackbarPos("UH","tracker")
    us=cv2.getTrackbarPos("US","tracker")
    uv=cv2.getTrackbarPos("UV","tracker")

    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("mask",mask)
    cv2.imshow("ress",res)

    k=cv2.waitKey(1) & 0xff
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()