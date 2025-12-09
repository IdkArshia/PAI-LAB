import cv2

img=cv2.imread("img2.jpg")

if img is not None:
    cv2.imshow("original image",img)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold_img=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)[1]

    (h,w)=threshold_img.shape[:2]
    center=(w//2,h//2)
    m=cv2.getRotationMatrix2D(center,60,1.0)
    rotate_img=cv2.warpAffine(threshold_img,m,(w,h))

    cv2.imshow("binary thresholding and rotation",rotate_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()