import cv2
import numpy as np

img=cv2.imread("img1.jpeg")

if img is not None:

    cv2.imshow("original image",img)
    blur_img=cv2.GaussianBlur(img,(7,7),0)
    crop_img=blur_img[100:300,0:400]
    cv2.imshow("blurred and cropped image",crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()