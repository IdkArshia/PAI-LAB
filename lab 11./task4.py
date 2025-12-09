import cv2
import numpy as np

img1=cv2.imread("images.jpeg")
img2=np.zeros((300,300,3),dtype="uint8")

if img1 is None:
    print("error unable to load image")

else:
    cv2.imshow("original image",img1)
    cv2.putText(img1,"A parrot",(10,10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(img2,"this is blank image",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow(" image with text",img1)
    cv2.imshow("blank image with text",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()