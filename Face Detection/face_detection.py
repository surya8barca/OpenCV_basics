import cv2

video = cv2.VideoCapture(0,)
frames=1;
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');

while True:
    frames+=1;
    check,frame=video.read()

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
