import pyttsx3
# import cv2
# faces_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# import tensorflow as tf
# cap=cv2.VideoCapture(0)
# while True:
#     img=cap.read()
    

#     faces=faces_cascade.detectMultiScale(img,1.5,5)
#     for x,y,w,z in faces[:]:
#         cv2.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
#         saved_faced=img[y:y+z,x:x+w]
#         face_name="faces.png"
#     cv2.imwrite(face_name,saved_faced)
#     cv2.imshow("Bruce's Camera",img)
#     if cv2.waitkey(1) & 0xFF== ord("q"):
#         break

# print(f"Hello world tensorflow here!!! {tf.version}")