import cv2
import os

video = cv2.VideoCapture(0)
video.set(3,640) #breadth
video.set(4,480) #lenght
frames=1;
count=0;
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');

face_id=input('Enter Id of Person:' )



while True:
    frames+=1;
    check,frame=video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for x,y,w,h in faces:
        
        gray=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
        count+=1;
        cv2.imwrite("Dataset/User."+str(face_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
        cv2.imshow('Capturing',frame)

    if(cv2.waitKey(1)==27 or count==100) :
        break

    

video.release()
cv2.destroyAllWindows()
