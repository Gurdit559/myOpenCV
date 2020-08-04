import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
dt=datetime.datetime.now()
print(dt)
#cap.set(3,800)  #3 is the number for width for camera webcam frame size
#cap.set(4,800)   #4 is the number for height
print(cap.get(3))
print(cap.get(4))

while(True):
    res,frame=cap.read()
    if res ==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        dt = datetime.datetime.now()
        text="Date: "+str(dt)
        #text="width:"+str(cap.get(3))+"height :"+str(cap.get(4))
        frame=cv2.putText(frame,text,(10,50),font,0.4,(250,0,0),2,cv2.LINE_AA)# 1 is fontscale and 2 is thickness
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q') :
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
