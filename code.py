import cv2
import numpy as np
import cv2 as cv

image = None
res = None


image =  cv.imread("photo.jpg",1)
res =  cv.xphoto.oilPainting(image, 7, 1)
cv.imshow("Original Image",image)
cv.imshow("New Image",res)
cv.waitKey(0)
cv.destroyAllWindows()
