import imgsim
import shutil
import cv2
import glob

#見た目が近似している漢字をリスト化してテキストファイルに保存しておく

for file1 in glob.glob('./kanji_READY/*.jpg'):
  print(file1)
  
  for file2 in glob.glob('./kanji_READY/*.jpg'):

  try:
    shutil.copyfile(file1, 'proc1.jpg')
    shutil.copyfile(file2, 'proc2.jpg')

    img0 = cv2.imread('proc1.jpg')
    img1 = cv2.imread('proc2.jpg')

    vtr = imgsim.Vectorizer()
    vec0 = vtr.vectorize(img0)
    vec1 = vtr.vectorize(img1)
    dist = imgsim.distance(vec0, vec1)

    if dist < 20 and dist != 0.0:
      print('--' + file2)
        
  except Exception:
    pass
        