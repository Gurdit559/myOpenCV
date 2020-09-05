import cv2
import numpy as np
down=2
bil=7

c=cv2.imread("car2.png")
print("image size",c.shape)
cc=cv2.resize(c,(800,800))
#g=cv2.cvtColor(cc,cv2.COLOR_BGR2GRAY)
#cv2.imshow("g",g)
#cv2.imshow("pic1",cc)
for i in range(down):
    c1=cv2.pyrDown(cc)
c2=cv2.resize(c1,(800,800))
#cv2.imshow("down",c1)
for j in range(bil):
    c3=cv2.bilateralFilter(c1,d=9,sigmaColor=9,sigmaSpace=7 )
#cv2.imshow("bil",c3)
for k in range(down):
    c4=cv2.pyrUp(c3)
#cv2.imshow("c4",c4)
greyc4=cv2.cvtColor(c4,cv2.COLOR_RGB2GRAY)
# cv2.imshow("greyc4img",greyc4)
gblur=cv2.medianBlur(greyc4,7)

#cv2.imshow("medblur",gblur)

img_edge=cv2.adaptiveThreshold(gblur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)
#cv2.imshow("edge",img_edge)

img_edge=cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
cartoon=cv2.bitwise_and(c2,img_edge)

cv2.imshow("cartoon",cartoon)

cc=cv2.resize(cc,(700,700))
cartoon=cv2.resize(cartoon,(700,700))
stack=np.hstack([cc,cartoon])

cv2.imshow("stacked images",stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
