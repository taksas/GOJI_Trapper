<h1>誤字トラッパー</h1>
<h2>Microsoft IMEで誤字を意図的に引き起こす、IME用単語セット</h2>
<br>
<br>
はじまりはこのコピペ。
<br>
<br>

>546 ：Mr.名無しさん：2008/06/05(木) 03:18:01
>
>休み時間ヒマだったので、上司のパソコンに
>
>「うんゆ｣→「運輪」
>「こくどこうつうしょう」→「国土文通省｣
>「せんじつは」→「先曰は」
>「けっさん」→「抉算｣
>「ねんどまつ」→「年度未」
>「しゃちょう」→「杜長｣
>「おくえん」→「憶円｣
>
>などを辞書登録しておいた。
>辛いまだバレていないようだ

<br>
<strong>「これ、自然言語処理と画像の類似度判定使えば、辞書データ作成自動化出来るんじゃね…？」</strong>と思ったのが事の発端。
<br>
<br>
<br>
Python + <br>GiNZA(自然言語処理担当その1) + <br>spaCy(自然言語処理担当その2) + <br>pykakasi(自然言語処理担当その3) + <br>OpenCV(画像の類似度判定) + <br>青空文庫(aozorahackさんのaozorabunko_text（ https://github.com/aozorahack/aozorabunko_text ）を使用) + <br>Rime Academyさんの漢字一覧表（ https://github.com/rime-aca/character_set ）<br><br>を使用しています。
<br>
<br>
<h2>ダウンロード</h2>
生成された生データ自体はgoji.txtですが、サイズが100MBを超えるためgithubに上げられません。
<br>
但し、過去のコミットを漁ることでテスト中のgoji.txtを取得することが出来ます。（重複単語が多いため動作確認にのみの使用をおすすめします）
<br>
<br>
類似度1.7未満、青空文庫の12000件ほどの作品のうち6000件ほどを解析した結果出た出力データとして、goji_similarity_1.7_under7000.txtを置いています（生データのため重複あり）。テストにご利用ください。
<br>
<br>
完成版はこちら（まだ用意出来てないよ！）

<h2>主な登場人物</h2>

<h3>Kanji_Imager.py</h3>

漢字の画像化を行います。Windows10/11標準フォントで出力した文字をjpgで保存。OpenCVの画像の類似度判定を使用できるようにします。

<h3>kanji_imager_forbidden_unpicker.py</h3>

画像化した漢字の内特殊なものはWin10/11標準フォントで表示できません。そういったものを一覧から取り除きます。

<h3>kanji_imager_similar_lister_v3.py</h3>

画像化した漢字を、さらにnumpy配列に変換します。諸事情で漢字と配列データが分かれており、data0.csvに漢字データ、data1.csvの同列に対応する配列データが保存されています。

<h3>kanji_imager_similar_lister_v3_2.py</h3>

画像の類似度判定の厳格性を決定するためのテストコードです。ログに随時類似した漢字を出力します。

<h3>kanji_imager_similar_outputter.py</h3>

画像化した漢字の内、「あるAという漢字に類似する漢字B, C, D, ....」を./kanji_similar/A.txtの中で一行づつB, C, D, ....という風に出力します。

<h3>GOJI_Generator_v1.py</h3>

青空文庫の文書を読み込み、自然言語処理（GiNZA + spaCy）で文節ごとに分け、さらに漢字ごとにkanji_similarディレクトリ内の類似漢字一覧を参照して漢字を置き換えます。
<br>
また、自然言語処理（pykakasi）で生成した文節のふりがなとともにIMEの辞書ファイル形式でgoji.txtに保存します。

<br>
<br>

<h2>その他の登場人物</h2>

<h3>GOJI_Generator_test.py</h3>

ハードコーディングした特定の文字列に対して、文節の分割とふりがなの予測、辞書ファイル用フォーマットの作成を行います。

<h3>kanji_imager_similar_lister_cv2.py</h3>

OpenCVの類似度判定を用いて、2つの漢字の比較をします。

<h3>kanji_imager_similar_lister_imagehash.py</h3>

ImageHashを用いて、画像のハッシュデータの類似度を判定します。OpenCVを用いるよりも高速な処理が可能ですが、精度に問題がありました。


