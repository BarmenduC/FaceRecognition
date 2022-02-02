import cv2
import numpy as np
import face_recognition
import os

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)


imgElon = face_recognition.load_image_file('ImageBasic/images.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/images (2).jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)