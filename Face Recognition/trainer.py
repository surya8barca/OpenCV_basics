import cv2
import os
import numpy as np
from PIL import Image

path='Dataset'

recognizer=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');

def getimagesandlabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids=[]

    for imagePath in imagePaths:
        PIL_img=Image.open(imagePath).convert('L')
        img_numpy=np.array(PIL_img,'uint8')

        id=int(os.path.split(imagePath)[-1].split('.')[1])
        faces=detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids 

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getimagesandlabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('Trainer/trainer.yml')
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
