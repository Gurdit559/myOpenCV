from cv2 import cv2
#print(cv2.__version__)

img=cv2.imread('lena.jpg',0)    #wrong file name entered will not give an error
print(img)

cv2.imshow('image',img) # to display image

k=cv2.waitKey(0)  & 0xFF==ord("w")  # display the image till close is clicked
if k==27:
    cv2.destroyAllWindows()     # destroy all the windows created
elif k== ord("s"):
    cv2.imwrite("lena_copy.png",img)   # to write the image //it will create a copy


