import cv2



c_var=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*'XVID')
name_of_file=input('Enter the name of the file:')
out=cv2.VideoWriter('{}.avi'.format(name_of_file),fourcc,20.0,(640,480))



while(c_var.isOpened()):
    ret,c_frame=c_var.read()
    if ret==True:

        out.write(c_frame)

        cv2.imshow('Recording (press Esc to Stop)',c_frame)
        
        if cv2.waitKey(1) == 27: #escape key
            break
    else:
        break


c_var.release()
out.release()
cv2.destroyAllWindows()