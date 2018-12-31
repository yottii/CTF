# X-mas_CTF_2018

## Introduction

こんにちは、今回はxmas_ctf2018のwriteupを書いていこうと思います。<br>
基本的に簡単な問題しか解いていません...TT<br>
とりあえず解いた問題はこんな感じ...
こんにちは
º£²ó¤È¤¤¤¿ÌäÂê¤Ï

Rev
 - Endress Chrismas

forensic
 - Santa The Weaver
 - Oh Chrismas Tree
 - 

misc
 - Santa's Security Levels
 - the ultimate chrismas game


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
{this_is_not_the_flag_you_are_looking_for}はそれっぽいデスが完全にfakeですね。
その上の文字列がflagっぽいです<br>
 - IEC as_tr33_1s_th1s_a 
 - IEC _flag_i_wond3r}.. 
 - IEC _flag_i_wond3r}.. 
¤³¤ì¤é¤òÁÈ¤ß¹ç¤ï¤»¤ë¤È...<br>
これらを組みわせると...<br>
¤Ï¤¤flag¤¬½Ð¤Æ¤­¤Þ¤·¤¿¤Í¡£
はい、flagが出てきました！

## 