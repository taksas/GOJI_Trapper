import imgsim
import shutil
import cv2
import glob

#Win10/11標準フォントでは表示できないようなニッチな文字は除くコード…なものの、処理がおっっっそい

img0 = cv2.imread('forbidden.jpg')

for file in glob.glob('./kanji_READY/*.jpg'):
  try:
    shutil.copyfile(file, 'proc.jpg')
    img1 = cv2.imread('proc.jpg')
    vtr = imgsim.Vectorizer()
    vec0 = vtr.vectorize(img0)
    vec1 = vtr.vectorize(img1)
    dist = imgsim.distance(vec0, vec1)
    if dist == 0.0:
        print(file)
        shutil.move(file,'./kanji_FORBIDDEN')
  except Exception:
    pass
        