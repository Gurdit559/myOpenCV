# Convert an image into a cartoon format(steps explained below).

### Original Image.

![carr](https://user-images.githubusercontent.com/22385974/92300036-52f19e80-ef75-11ea-89ae-5178ff1dc49a.png)

### cartoon image.

![cartoon](https://user-images.githubusercontent.com/22385974/92300086-b2e84500-ef75-11ea-9969-84f1e9e64238.png)

### Final output.

![st](https://user-images.githubusercontent.com/22385974/92300124-0064b200-ef76-11ea-8168-ef7a0a4b1da2.png)


## Steps:

1) Read the image <br>

2) Resize after checking its original size<br>

3) We need to convert an image to a size different than its original. For this, there are two possible options: <br>
     Upsize the image (zoom in) or <br>
     Downsize it (zoom out). Firstperform pyrDown() <br>
4) Then we apply bilateral filter-A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel<br>
   with a weighted average of intensity values from nearby pixels. (used when u have to preserve edges)<br>

5) Convert it back to original form using pyrUP()<br>

6) Convert the image to a GrayScale<br> 
 need:<br>
Dimension reduction: For e.g. In RGB images there are three color channels and has three dimensions while grayscaled images are single dimensional.<br>
Reduces model complexity: Consider training neural article on RGB images of 10x10x3 pixel.The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input node for grayscaled images.<br>
For other algorithms to work: There are many algorithms that are customized to work only on grayscaled images e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscaled images only<br>

7) apply median blur: The Median blur operation is similar to the other averaging methods. Here, the central element of the image is replaced by the median of all the pixels in the kernel area. This operation processes the edges while removing the noise.<br>

8) Adaptive Thresholding<br>
To use adaptive threshold the src image must be in greyscale<br>
 Adaptive thresholding is the method where the threshold value is calculated for smaller regions. This leads to different threshold values for different regions with respect to the change in lighting.<br>
 here 9 is blocksize (decides the size of the neighbourhood area) and 2 is value of c(constant subtracted from the mean)
 
