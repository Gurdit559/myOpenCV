import cv2
import numpy as np
img=cv2.imread("smarties.png")

def nothing(x):
    pass
cv2.namedWindow("tracking")  # for getting the upper and lower value of color for detection
cv2.createTrackbar("LH","tracking",0,255,nothing) #lower hue
cv2.createTrackbar("LS","tracking",0,255,nothing) #lower saturation value
cv2.createTrackbar("LV","tracking",0,255,nothing) #lower value
cv2.createTrackbar("UH","tracking",255,255,nothing) # upper hue
cv2.createTrackbar("US","tracking",255,255,nothing) # upper saturation
cv2.createTrackbar("UV","tracking",255,255,nothing) # upper value


while(True):

    cv2.imshow("image",img)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("LH","tracking")
    l_s = cv2.getTrackbarPos("LH", "tracking")
    l_v = cv2.getTrackbarPos("LH", "tracking")

    u_h=cv2.getTrackbarPos("UH","tracking")
    u_s = cv2.getTrackbarPos("US", "tracking")
    u_v = cv2.getTrackbarPos("UV", "tracking")


    #l_b=np.array([110,50,50])               # lower color range of blue colour threshold
    #u_b=np.array([130,255,255])

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,l_b,u_b)    # select hsv to show only blue color(show in white)

    res=cv2.bitwise_and(img,img,mask=mask)   #apply mask for lower and upper blue value

    cv2.imshow("image",img)
    cv2.imshow("maskk",mask)
    cv2.imshow("ress",res)

    k=cv2.waitKey(1)& 0xff
    if k==27:
        break


cv2.destroyAllWindows()