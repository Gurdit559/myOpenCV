import cv2
import numpy as np
def onclick(event,x,y,flag,para):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),6,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,255,0),2)
        cv2.imshow("image",img)

def click2(event,x,y,flag,para):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(255,255,0),-1)
        newimg=np.zeros((512,512,3),np.uint8)
        newimg[:]=[blue,green,red]
        text=str(blue)+","+str(green)+","+str(red)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(newimg,text,(150,150),font,2,(0,255,255),2)
        cv2.imshow("image1",newimg)


#img=np.zeros((520,520,3),np.uint8)
img=cv2.imread("lena.jpg")
cv2.imshow("image",img)
#cv2.setMouseCallback("image",onclick)     #make lines on numpy image
cv2.setMouseCallback("image",click2)
points=[]
cv2.waitKey(0)
cv2.destroyAllWindows()
