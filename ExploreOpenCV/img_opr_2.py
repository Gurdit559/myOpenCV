import cv2
img=cv2.imread("messi1.jpg")
img2=cv2.imread("mlogo.jpg")

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
#fin=cv2.add(img,img2)                   #add 2 images must have same size ie rows & column
fin=cv2.addWeighted(img,0.7,img2,0.3,0)
cv2.imshow("image",fin)
cv2.waitKey(0)
cv2.destroyAllWindows()