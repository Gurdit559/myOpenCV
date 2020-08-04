import cv2
import numpy as np
#img=np.zeros((400,400,3),np.uint8)
#cv2.imshow("image",img)

cv2.namedWindow("image")
def position(x):
    print(x)
S="color/grey"
cv2.createTrackbar(S,"image",0,1,position)  # acts like a switch
cv2.createTrackbar("cp","image",0,255,position)
#cv2.createTrackbar("G","image",0,255,position)
#cv2.createTrackbar("R","image",0,255,position)

while(True):
    img = cv2.imread("messi1.jpg")
    pos=cv2.getTrackbarPos("cp","image")
    font=cv2.FONT_HERSHEY_SIMPLEX
    text=str(pos)
    cv2.putText(img,text,(50,50),font,1,(0,0,255),1)

    k=cv2.waitKey(1)& 0xFF
    if k==27:
        break
    #b=cv2.getTrackbarPos("B","image") # get the current position of trackbar
    #g=cv2.getTrackbarPos("G","image")
    #r=cv2.getTrackbarPos("R","image")
    s=cv2.getTrackbarPos(S,"image")
    if s==0:
        pass                       #important if switch 0 then print colored image
    else:
       # img[:]=[b,g,r]        # for colours
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("image", img)
cv2.destroyAllWindows()