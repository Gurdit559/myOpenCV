import cv2

cap=cv2.VideoCapture(0);    # device index
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
while(True):
    ret,frame=cap.read()   # ret is true if frame is available. frame will save the frame
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #cv2.imshow("frame",frame)         # for coloured

        out.write(frame)
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # for gray scal webcam frame
        cv2.imshow("frame",grey)
        if cv2.waitKey(1) & 0xff==ord("q"):
            break
    else:
        break



cap.release()
out.release()
cv2.destroyAllWindows()



