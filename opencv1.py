from types import FrameType
import cv2
import numpy as np
# import cv2 as cv

#open a picture
#img=cv.imread("cat.jpg")
#cv.imshow("CAT",img)
#cv.waitKey(0)

#open a video
#capture=cv.VideoCapture("Tuza.webm")

#while True:
#    isTrue,frame=capture.read()
#    cv.imshow("Video",frame)
#    if cv.waitKey(20) & 0xFF==ord("d"):
#        break
#capture.release()
#cv.destroyAllWindows()

img=cv2.imread("ronaldo.jpg")

kennel=np.ones((2,2),np.uint8)

imgConv=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgConv,(7,7),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kennel,iterations=1)
imgErode=cv2.erode(imgCanny,kennel,iterations=1)

#cv2.imshow("cat",imgConv)
#cv2.imshow("blur image",imgBlur)
#cv2.imshow("canny image",imgCanny)
#cv2.imshow("dialate image",imgDialation)
#cv2.imshow("Eroded image",imgErode)
verctasck=np.vstack((imgDialation,imgErode))
imgstack=np.hstack((imgCanny,imgConv))
cv2.imshow("stack images",imgstack)
cv2.imshow("ver stack",verctasck)

width,height=250,350
img=cv2.imread("cards.jpg")
pt1=np.float32([[326,116],[481,196],[210,332],[367,417]])
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pt1,pt2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("warped image",imgOutput)
cv2.waitKey(0)

