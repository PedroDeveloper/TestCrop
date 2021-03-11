from os import read
import os 
import cv2



readPath = "C:\\Users\\Pedro\\Desktop\\testes\\2021-03-11"
files = os.listdir(readPath)
for file in files:

        imagePath = readPath +"\\"+ file
        img =  cv2.imread(imagePath)
        y=0
        x=0
        h=550
        w=1200
       
        crop = img[y:y+h, x:x+w]
        cv2.imwrite(readPath+"\\"+file,crop)
        