import imgsim
import shutil
import cv2
import glob

import pandas as pd
import numpy as np
import csv


with open("data0_test.csv", encoding='UTF-8') as file_name:
    img0 = np.loadtxt(file_name, delimiter=",", dtype = "unicode")

img1 = np.loadtxt('data1_test.csv')


for i in range(7):
  print(img0[i])
  for j in range(7):
    dist = imgsim.distance(img1[i].astype(object),img1[j].astype(object))

    if dist < 10 and dist != 0.0:
      print('--' + img0[j])

        