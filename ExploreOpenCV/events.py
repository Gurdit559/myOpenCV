import cv2
import numpy as np
#ev=[i for i in dir(cv2) if "EVENT" in i]
#print(ev)

def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," , ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(x)+", "+str(y)
        cv2.putText(img,text,(x,y),font,0.6,(250,250,0),3)
        cv2.imshow("image",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]  # blue channel
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(blue)+","+str(green)+","+str(red)
        cv2.putText(img,text,(x,y),font,0.6,(0,250,250),3)
        cv2.imshow("image",img)


#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("lena.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
