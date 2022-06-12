import shutil
import glob

from PIL import Image 
import imagehash 

import datetime

#見た目が近似している漢字をリスト化して表示(ImageHash改良版)

i = 0
j = 0

img = [[0] * 2 for i in range(12817)]

for file1 in glob.glob('./kanji_READY/*.jpg'):
  shutil.copyfile(file1, 'proc3.jpg')
  # print(file1.replace('./kanji_READY\\', '').replace('.jpg', ''))
  img[i][j] = file1.replace('./kanji_READY\\', '').replace('.jpg', '')
  j += 1
  img[i][j] = imagehash.phash(Image.open('proc3.jpg')) 
  i += 1
  j -= 1


k = 0
for p in range(12816):
  print(img[k][0] + '-' + str(img[k][1]))
  k +=1



        