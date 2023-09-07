import cv2
import numpy as np
import matplotlib.pyplot as plt

# normal image
img = cv2.imread('images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
resized_img = cv2.resize(img,(720,520))

# laplacian image
lap_img = cv2.Laplacian(resized_img,cv2.CV_64F,ksize=5) # returns the image in CV_64F in a hexadecimal,
# form where each pixel is in hexadeciaml number
lap_img = np.int8(np.absolute(lap_img))

#sobelX
sobel_X = cv2.Sobel(resized_img,cv2.CV_64F,1,0)
sobel_x = np.uint8(np.absolute(sobel_X))

# sobelY
sobel_Y = cv2.Sobel(resized_img,cv2.CV_64F,0,1)
sobel_y = np.uint8(np.absolute(sobel_Y))

# combining sobel_x and sobel_y
combined_img = cv2.bitwise_or(sobel_y,sobel_x)

# canny Edge Detection
canny_img = cv2.Canny(resized_img,100,200,apertureSize=3)


#making a list for all these images and giving them appropiate titles
images =[resized_img,lap_img,sobel_x,sobel_y,combined_img,canny_img]
titles =['messi','laplacian_img','sobel_x','sobel_y','combined_img','canny_img']

plt.figure(figsize=(10,6))
for i in range(6):
    plt.subplot(3,2,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.yticks([]),plt.xticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


