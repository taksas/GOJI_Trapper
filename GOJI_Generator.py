import spacy
import ginza
import regex
import pykakasi

nlp = spacy.load('ja_ginza')
doc = nlp('新橋で3日昼に「ランチ」をご一緒しましょう！！？次の、十日火曜日はどうですか。')

p1 = regex.compile(r'\p{Script=Han}+')
p2 = regex.compile(r'\p{Script=Latin}+')
p3 = regex.compile(r'\p{Numeric_Type=Numeric}+')
p4 = regex.compile('[0-9]+')
p5 = regex.compile('[０-９]+')

kks = pykakasi.kakasi()

f = open('myfile.txt', 'a')

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
                       .replace('】', '')
        if p1.search(sp) != None and p2.search(sp) == None and p3.search(sp) == None and p4.search(sp) == None and p5.search(sp) == None: 
          print(sp)
          yomi = ''
          result = kks.convert(sp)
          for result2 in result:
            yomi += result2['hira']
          print(yomi)
          output = yomi + '	' + sp  + '	' + '名詞' + '	' + '誤字トラッパー' + '\n'
          f.write(output)