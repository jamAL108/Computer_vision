import cv2
import numpy as np

messi = cv2.imread('./images/messi.jpg')
messi = cv2.resize(messi,(640,540))
layer = messi.copy()
# cv2.imshow('image',messi)


# guassian pyramid
gp =[layer]
for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),messi)



def build_laplacian_pyramid(image, levels):
    pyramid = []
    for _ in range(levels):
        # Compute Gaussian and down-sampled version
        next_image = cv2.pyrDown(image)

        # Calculate the Laplacian
        h, w = image.shape[:2]
        expanded = cv2.pyrUp(next_image, dstsize=(w * 2, h * 2))
        laplacian = cv2.subtract(image, expanded)
        
        pyramid.append(laplacian)
        image = next_image

    pyramid.append(image)  # The last level is the base image
    return pyramid
laplacian_pyramid = build_laplacian_pyramid(messi, 4)

# Display the levels of the Laplacian pyramid
for i, level in enumerate(laplacian_pyramid):
    cv2.imshow(f'Level {i}', level)


cv2.waitKey(0)
cv2.destroyAllWindows()