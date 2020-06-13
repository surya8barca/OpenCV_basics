import cv2
import os

video = cv2.VideoCapture(0,)
frames=1;
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');
name=input('Enter Name:')
parent_dir=os.getcwd()
path=os.path.join(parent_dir,name)
os.mkdir(path)

while True:
    frames+=1;
    check,frame=video.read()
    cv2.imwrite(os.path.join(path,name+str(frames)+'.jpg'),frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for x,y,w,h in faces:
        
        gray=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('Capturing',gray)

    if cv2.waitKey(1)==27:
        break

    
print(frames)
video.release()
cv2.destroyAllWindows()
