import matplotlib.pyplot as plt   # reads image in rgb format
import cv2
#img=cv2.imread("lena.jpg")
#img=cv2.resize(img,(255,255),3)
#cv2.imshow("image",img)
#img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#plt.imshow(img2)

img=cv2.imread("gradient.jpg")
cv2.imshow("win1",img)
_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles=["original","binary","binary_inv","trunc","tozero","tozero_inv"]
images=[img,th1,th2,th3,th4,th5]
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()