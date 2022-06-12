import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

import glob

 #常用漢字など、様々な漢字をcharacter_set-masterから読み込み、Windows10/11標準フォントでkanjiディレクトリ内に画像化する

def imager(text):

  # 使うフォント，サイズ，描くテキストの設定
  ttfontname = "C:\\Windows\\Fonts\\yugothl.ttc"
  fontsize = 36
  text = text

  # 画像サイズ，背景色，フォントの色を設定
  canvasSize    = (50, 70)
  backgroundRGB = (255, 255, 255)
  textRGB       = (0, 0, 0)

  # 文字を描く画像の作成
  img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
  draw = PIL.ImageDraw.Draw(img)

  # 用意した画像に文字列を描く
  font = PIL.ImageFont.truetype(ttfontname, fontsize)
  textWidth, textHeight = draw.textsize(text,font=font)
  textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
  draw.text(textTopLeft, text, fill=textRGB, font=font)
  try:
    img.save('./kanji/' + text.replace('\n', '') + '.jpg')
  except Exception:
    pass
  

if __name__ == '__main__':
    for file in glob.glob("./character_set-master/*.txt"):
        with open(file, encoding="utf-8") as f:
            for line in f:
                if len(line) == 2:
                  imager(line)