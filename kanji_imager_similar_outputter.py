import imgsim
import shutil
import cv2
import glob

import pandas as pd
import numpy as np
import csv

#data0とdata1から似ている文字リストを生成してkanji_similarフォルダ内にテキストファイルとして出力

with open("data0.csv", encoding='UTF-8') as file_name:
    img0 = np.loadtxt(file_name, delimiter=",", dtype = "unicode")

img1 = np.loadtxt('data1.csv')


for i in range(12817):
  print(img0[i] + '  -  ' + str(i))
  output = []
  for j in range(12817):
    dist = imgsim.distance(img1[i].astype(object),img1[j].astype(object))

    if dist < 1.7 and dist != 0.0:
      print('--' + img0[j])
      output += img0[j]

  with open('./kanji_similar/' + img0[i] + '.txt', 'w', encoding='UTF-8') as f:
    for d in output:
        f.write("%s\n" % d)

        