
# application of image pyramids is image blending
# 5 steps for image blending
#1) load the 2 images say apple and orange
#2) find the guassian pyramid for apple and orange (levels 6 for this case)
#3) from the guassian pyramid find their laplacian pyramids
#4) now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
#5) from this joint image pyramids reconstruct original image
import cv2
import numpy as np
apple=cv2.imread("apple.jpg")
orange=cv2.imread("orange.jpg")
apple=cv2.resize(apple,(512,512))
print(apple.shape)
print(orange.shape)
apple_orange=np.hstack((apple[:,:256],orange[:,256:]))

#generate guassian pyramid for apple
apple_copy=apple.copy()
gp_apple=[apple_copy]

for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate guassian pyramid for orange
orange_copy=orange.copy()
gp_orange=[orange_copy]

for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#generate laplacian pyramid for apple ie level in the laplacian pyramid is formed by the  difference
# between the level in the guassian pyramid is for and extended version of its upper level in the guassian
apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    guassian_expanded=cv2.pyrUp(gp_apple[i])
    laplacian=cv2.subtract(gp_apple[i-1],guassian_expanded)
    lp_apple.append(laplacian)

orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    guassian_expanded=cv2.pyrUp(gp_orange[i])
    laplacian=cv2.subtract(gp_orange[i-1],guassian_expanded)
    lp_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n=n+1
    cols,rows,channels=apple_lap.shape
    laplacian=np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
# reconstruct the image
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)


cv2.imshow("apple_orange",apple_orange)
cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("reconstruct",apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()