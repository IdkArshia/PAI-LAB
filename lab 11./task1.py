import cv2

img=cv2.imread("img1.jpeg")

if img is None:
    print("error unable to load image")

else:
    cv2.imshow("original image",img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    resized=cv2.resize(gray,(150,200))
    cv2.imshow("Gray and resized image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()