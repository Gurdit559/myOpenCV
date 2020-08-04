import cv2
import numpy as np

cap=cv2.VideoCapture("vtest.avi")
ret,frame1=cap.read()  # read video frame by frame
ret,frame2=cap.read()
#print(frame1)
#cv2.imshow("frame1",frame1)
#cv2.imshow("frame2",frame2)
#print(frame2)
while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2) # find absolute diff betw first and second frame
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY) # convert diff into grayscale to find contours later better in gray as compared to color
    cv2.imshow("grayscale",gray)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    cv2.imshow("gb",blur)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY) # dilate the thresholded image to fill in all the holes for better contours lower the value more tightly fit it is
    dilate=cv2.dilate(thresh,None,iterations=2)
    contours,hierarchy=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(hierarchy) #image topology info
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)# -1 for applying all contours
    #It is considering the rope in the image as moving object as well and below code will discard that by putting a threshold to the height and width
    for c in contours:
        (x,y,w,h)=cv2.boundingRect(c) #gives the x , y coord and width and height
        # find area of the contour and if the area is less than certain value then we ignore that
        # and if its greater than a certain value then we draw a rectangle around it
        if cv2.contourArea(c)<900:
            continue # do nothing
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Status: {}".format("movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,
        1,(0,0,255),3)

    cv2.imshow("feed",frame1)
    frame1=frame2
    ret,frame2=cap.read()


    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()