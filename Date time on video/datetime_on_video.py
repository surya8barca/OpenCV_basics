import cv2
import datetime



c_var=cv2.VideoCapture(0);

while(c_var.isOpened()):
    ret,c_frame=c_var.read()
    if ret==True:

        font=cv2.FONT_HERSHEY_PLAIN;
        text=str(datetime.datetime.now())
        c_frame=cv2.putText(c_frame,text,(10,50),font,1,(211,125,122),2,cv2.LINE_AA)

        cv2.imshow('Recording (press Esc to Stop)',c_frame)
        
        if cv2.waitKey(1) == 27: #escape key
            break
    else:
        break


c_var.release()
cv2.destroyAllWindows()