import shutil
import glob

import imgsim
import cv2

import datetime

import csv
import numpy as np

#見た目が近似している漢字をリスト化して表示(機械学習改良版)

i = 0
j = 0

img = [[0] * 7 for i in range(2)]

for file1 in glob.glob('./kanji_test/*.jpg'):
  shutil.copyfile(file1, 'proc4.jpg')

  img0 = cv2.imread('proc4.jpg')
  vtr = imgsim.Vectorizer()
  vec1 = vtr.vectorize(img0)

  img[j][i] = file1.replace('./kanji_test\\', '').replace('.jpg', '')
  j += 1
  img[j][i] = vec1
  j -= 1
  i += 1
  print(type(vec1))




np.savetxt('data1_test.csv', img[1])
with open('data0_test.csv', 'w', encoding='UTF-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(img[0])



        