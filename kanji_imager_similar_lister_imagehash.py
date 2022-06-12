import shutil
import glob

from PIL import Image 
import imagehash 

import datetime

#見た目が近似している漢字をリスト化して表示(ImageHash版)

for file1 in glob.glob('./kanji_READY/*.jpg'):
  dt_now = datetime.datetime.now()
  print(file1 + dt_now.strftime('(%H:%M:%S)'))
  
  for file2 in glob.glob('./kanji_READY/*.jpg'):

    shutil.copyfile(file1, 'proc1.jpg')
    shutil.copyfile(file2, 'proc2.jpg')
    
    img0 = imagehash.phash(Image.open('proc1.jpg')) 
    img1 = imagehash.phash(Image.open('proc2.jpg')) 

    hash = img0 - img1
    if hash < 5 and hash != 0:
      print('--' + file2)

        