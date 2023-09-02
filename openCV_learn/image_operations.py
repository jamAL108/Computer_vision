import cv2

def XY_cal(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x)
        print(y)
img = cv2.imread('messi.jpg')
img2 = cv2.imread('goat.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
blue,green,red = cv2.split(img)
print(blue)
merged_img = cv2.merge((blue , green,red))
resized_merged_img = cv2.resize(merged_img,(780,520))
worldcup = resized_merged_img[283:359,505:599]
dest_x = 50
dest_y = 283
resized_merged_img[dest_y:dest_y + worldcup.shape[0], dest_x:dest_x + worldcup.shape[1]] = worldcup
image = cv2.addWeighted(img, .9 , img2 ,.1)
cv2.imshow('image',resized_merged_img)
#cv2.setMouseCallback('image', XY_cal)
cv2.waitKey(0)
cv2.destroyAllWindows()