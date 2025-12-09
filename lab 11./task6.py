import cv2 
import numpy as np 

image1 = cv2.imread("img1.jpeg") 
image2 = cv2.imread("img2.jpg") 

image1 = cv2.resize(image1,(image2.shape[1],image2.shape[0]))
blended_image= cv2.add(image1, image2)

gray = cv2.cvtColor(blended_image, cv2.COLOR_BGR2GRAY)

equalized_image= cv2.equalizeHist(gray)

cv2.imshow("Blended  and equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()