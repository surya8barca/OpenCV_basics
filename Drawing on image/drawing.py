import cv2
import numpy as np


img=np.zeros([500,500,3],np.uint8)
#img=cv2.imread('img.jpg',1)

img=cv2.line(img,(0,0),(255,500),(0,0,255),1)

img=cv2.rectangle(img,(0,0),(25,50),(0,0,255),-1)
img=cv2.circle(img,(50,60),12,(200,122,255),-1)

cv2.imshow("image",img)

cv2.waitKey(3000)
cv2.destroyAllWindows()