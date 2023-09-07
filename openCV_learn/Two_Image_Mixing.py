import cv2
import numpy as np
apple = cv2.imread('./images/apple-fruit.webp')
orange = cv2.imread('./images/orange-fruit.webp')
resized_apple = cv2.resize(apple,(520,520))
resized_orange = cv2.resize(orange,(520,520))

# mixing of image
mixing_image = np.hstack((resized_apple[:,:256],resized_orange[:,256:]))
cv2.imshow('apple',resized_apple)
cv2.imshow('orange',resized_orange)
cv2.imshow('mixed',mixing_image)



cv2.waitKey(0)
cv2.destroyAllWindows()