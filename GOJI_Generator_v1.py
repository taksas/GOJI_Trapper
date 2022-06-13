import spacy
import ginza
import regex
import pykakasi


import glob
import re

nlp = spacy.load('ja_ginza')
p1 = regex.compile(r'\p{Script=Han}+')
p2 = regex.compile(r'\p{Script=Latin}+')
p3 = regex.compile(r'\p{Numeric_Type=Numeric}+')
p4 = regex.compile('[0-9]+')
p5 = regex.compile('[０-９]+')
kks = pykakasi.kakasi()



def maker(text):
  texta = re.sub("\《.+?\》", "", text)
  doc = nlp(texta)
  
  # 文節分割
  for sent in doc.sents:
    for span in ginza.bunsetu_spans(sent):
        sp =  str(span).replace('。', '')\
                       .replace('、', '')\
                       .replace(',', '')\
                       .replace('.', '')\
                       .replace('!', '')\
                       .replace('！', '')\
                       .replace('?', '')\
                       .replace('？', '')\
                       .replace('「', '')\
                       .replace('」', '')\
                       .replace('（', '')\
                       .replace('）', '')\
                       .replace('(', '')\
                       .replace(')', '')\
                       .replace('[', '')\
                       .replace(']', '')\
                       .replace('［', '')\
                       .replace('］', '')\
                       .replace('$', '')\
                       .replace('＄', '')\
                       .replace('&', '')\
                       .replace('＆', '')\
                       .replace('%', '')\
                       .replace('％', '')\
                       .replace('-', '')\
                       .replace('＃', '')\
                       .replace('《', '')\
                       .replace('》', '')\
                       .replace('｜', '')\
                       .replace('：', '')\
                       .replace('【', '')\
                       .replace('】', '')\
                       .replace('―', '')\
                       .replace('ー', '')\
                       .replace('-', '')\
                       .replace('『', '')\
                       .replace('』', '')\
                       .replace('【', '')\
                       .replace('】', '')\
                       .replace('　', '')\
                       .replace('\n', '')

        
        if p1.search(sp) != None and p2.search(sp) == None and p3.search(sp) == None and p4.search(sp) == None and p5.search(sp) == None: 

          yomi = ''
          result = kks.convert(sp)
          for result2 in result:
            yomi += result2['hira']


          
          for spa in list(sp):
            if p1.fullmatch(spa):
              try:
                for kanji in glob.glob('./kanji_similar/' + spa + '.txt'):
                  with open(kanji, encoding="utf-8") as f:
                        for line in f:
                            f = open('goji.txt', 'a')
                            output = yomi + '	' + sp.replace(spa, line).replace('\n', '')  + '	' + '名詞' + '	' + '誤字トラッパー' + '\n'
                            f.write(output.replace('\u3094', ''))

              except Exception:
                pass
  
            



if __name__ == '__main__':
    i = 1
    for file in glob.glob('./aozorabunko_text-master/cards/*/*/*/*.txt'):
      print('Loading_NEXT_BOOK (' + str(i) + ') ---> ' + file)
      i += 1
      with open(file, encoding="shift-jis") as f:
            for line in f:
                  maker(line)
