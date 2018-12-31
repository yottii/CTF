# X-mas_CTF_2018

## Introduction

こんにちは、今回はxmas_ctf2018のwriteupを書いていこうと思います。<br>
基本的に簡単な問題しか解いていません...TT<br>
とりあえず解いた問題はこんな感じ...

Rev
 - Endress Chrismas

forensic
 - Santa The Weaver
 - Oh Chrismas Tree
 - 

misc
 - Santa's Security Levels
 - the ultimate chrismas game

## Oh Chrismas Tree [forensic/25point]

この問題は画像からflagを抽出問題ですね.画像はこちら<br>
-[](https://github.com/yottii/CTF/blob/master/writeup/20181221_x-masCTF2018/file/MerryChristmas.jpg)

クリスマスっぽい画像ですねぇ<br>
まずそれっぽい文字列がないか探していきます。
```
Copyright (c) 1998 Hewlett-X-MAS{0_Chr15tm
desc
sRGB IEC61966-2.1
sRGB IEC61966-2.1
XYZ
XYZ
XYZ
XYZ
XYZ
desc
IEC as_tr33_1s_th1s_a
IEC _flag_i_wond3r}..
desc
.IEC 61966-2.1 Default RGB colour space - sRGB
.IEC 61966-2.1 Default RGB colour space - sRGB
desc
,Reference Viewing Condition in IEC61966-2.1
,Reference Viewing Condition in IEC61966-2.1
view
XYZ
meas
sig
CRT curv
^L*^LC^L\^Lu^L
 A l
!H!u!
"'"U"
#8#f#
$M$|$
%8%h%
&'&W&
'I'z'
(?(q(
)8)k)
*5*h*
+6+i+
test
{this_is_not_the_flag_you_are_looking_for}P
```
{this_is_not_the_flag_you_are_looking_for}はそれっぽいデスが完全にfakeですね。<br?
その上の文字列がflagっぽいです<br>
 - Hewlett-X-MAS{0_Chr15tm 
 - IEC as_tr33_1s_th1s_a 
 - IEC _flag_i_wond3r}.. 
これらを組みわせると...<br>
` X-MAS{0_Chr15tmas_tr33_1s_th1s_a_flag_i_wond3r}`
はい、flagが出てきました！

## Santa's Security Level
これは音声ファイルが渡され、それを解析する問題ですね<br>

-[](https://github.com/yottii/CTF/tree/master/writeup/20181221_x-masCTF2018/file/message.mp3)

聞いてみると,どうやらモールス信号だということがわかります。<br>
音声を文字に起こしてみると....

``` 
--. .. - .... ..- -... -.-. --- -- --. --- --- --- --. .- .-.. -..- -- .- ...
```

文字にするソフト等はフリーであるので探してみてください。
この文字列をローマ字に直すと
```
githubcomgooogalxmas
```

これはどうやらサイトのようですね<br>
github.com/googalxmas

ここにアクセスすると...

```
Santa doesn't like people searching for his flags, but you look like a nice person. Anyway here's your flag:

vF ur uNq nAlguvat pbasvqraGvNy gb fnl, ur jebgr Vg ia pvcure, gung vF, ol FB punaTvat gur beqre bs gur Yrggref bs gur nycuNorg, gung abg n j beQ pbhyq or ZnQR bHg.
```

これはシーザー暗号だと思われます, 前に作ったシーザー暗号解読プログラムで直してみると....<br>
プログラム:[シーザープログラム](https://github.com/yottii/SecurityTools/blob/master/rot/rot.py)

```
iS he hAd aNything confidenTiAl to say, he wrote It vn cipher, that iS, by SO chanGing the order of the Letters of the alphAbet, that not a w    orD could be MaDE oUt
```

is he had anything confidential to say, he wrote it vn cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.

つまり, 先ほどの大文字部分がflagになるっぽいとのことです...<br>

```
X-MAS{SANTAISSOGLADMEU}
```

結構苦労しました<br>
英語力もないのでこれから身につけていきたいですね...<br>


##  MessageFromSanta[forensic/50point]

この問題は画像ファイルを組み合わせる問題です.
パズルみたいで楽しかった

