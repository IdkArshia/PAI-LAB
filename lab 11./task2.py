import cv2
import numpy as np

img1=np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(200,200),50,255,-1)
cv2.rectangle(img1,(50,50),(150,150),255,-1)

cv2.imshow("blank image with rectangle and circle",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()