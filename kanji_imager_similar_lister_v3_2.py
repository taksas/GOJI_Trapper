import imgsim
import shutil
import cv2
import glob

import pandas as pd
import numpy as np
import csv


with open("data0.csv", encoding='UTF-8') as file_name:
    img0 = np.loadtxt(file_name, delimiter=",", dtype = "unicode")

img1 = np.loadtxt('data1.csv')

#dist = imgsim.distance(img1[107].astype(object),img1[108].astype(object))
#print('!!' + img0[107] + img0[108] + str(dist))

for i in range(12817):
  print(img0[i] + '  -  ' + str(i))
  for j in range(12817):
    dist = imgsim.distance(img1[i].astype(object),img1[j].astype(object))

    if dist < 1.7 and dist != 0.0:
      print('--' + img0[j])

        