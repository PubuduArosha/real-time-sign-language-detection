import cv2 
import time
import uuid
import os

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'

lables = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for lable in lables:

    os.mkdir('Tensorflow\workspace\images\collectedimages\\'+lable)

    cap = cv2.VideoCapture(0)
    print('Collecting imagess for {}'.format(lables))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, lable, lable+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()



