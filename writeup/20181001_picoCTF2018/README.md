## PicoCTF 2018 ##
## Introduction ##

hello! I'm yotti.<br>
今回はpicoCTFの問題を解いてみました.やった感じ,ビギナーズ向けのctfでした<br>
writeup書くほどでもないと思いましたが, 一応書き残しておきます-<br>
ctf初心者とか,最近やったばっかりとかの人にはかなり良いと思います！<br>
それ問題を解いたのに,"you or one of your teammates have already tried this solutions"<br>
となり解いたことにならなかった問題が多々あり困ってます(現在進行形)<br>
I don't know what is this problem for us, please teach me to solve its problem!!<br>

URL:https://2018game.picoctf.com/problems

前半はコマンドの使用方法とかで簡単なので飛ばします.<br>
pint100くらいから解説します(それでも簡単だが....)



## HEEEEEEERE'S Johnny! - Points: 100 - ##

問題文は以下のとおり

```
Okay, so we found some important looking files on a linux computer. 
Maybe they can be used to get a password to the process. 
Connect with nc 2018shell3.picoctf.com 42165. Files can be found here: passwd shadow.
```

これはjohn the ripperを使う問題っぽいですね、passwdとshadowファイルが与えられています.
では早速解いていきましょう！！

とりあえず nc 2018shell3.picoctf.com 42165に接続してみます。

```
net40-dhcp179:file yotti$ nc 2018shell3.picoctf.com 42165
Username: test
Password: test  
Failed Login!
```

解析したユーザー名とアドレスを入力するようですね.早速johnでpassファイルを解析しますー。

```
net40-dhcp179:file yotti$ cat shadow 
root:$6$HRMJoyGA$26FIgg6CU0bGUOfqFB0Qo9AE2LRZxG8N3H.3BK8t49wGlYbkFbxVFtGOZqVIq3qQ6k0oetDbn2aVzdhuVQ6US.:17770:0:99999:7:::
net40-dhcp179:file yotti$ cat passwd 
root:x:0:0:root:/root:/bin/bashnet40-dhcp179:file yotti$ 
```

unshadowを使ってshadowファイルとpasswdファイルをjohnに解析できる形式にします。

```
net40-dhcp179:file yotti$ /usr/local/Cellar/john/1.8.0/share/john/unshadow  passwd shadow > testfile
net40-dhcp179:file yotti$ /usr/local/Cellar/john/1.8.0/share/john/john  --wordlist=/usr/local/Cellar/john/1.8.0/share/john/password.lst --users=root ./testfile 
root:kissme:0:0:root:/root:/bin/bash
1 password hash cracked, 0 left
```

はい解析できましたね。<br>
user:root<br>
pass:kissme<br>

loginしてみましょー

```
net40-dhcp179:file yotti$   nc 2018shell2.picoctf.com 5221
Username: root
Password: kissme
picoCTF{J0hn_1$_R1pp3d_289677b5}
```

出ましたね.``picoCTF{J0hn_1$_R1pp3d_289677b5}``
今後も色々使うと思うのでもっとjohnの使い方についてマスターしたいと思います...


## strings - Points: 100 ##
question:
```
Can you find the flag in this file without actually running it? 
You can also find the file in /problems/strings_4_40d221755b4a0b134c2a7a2e825ef95f on the shell server.
```
これは,stringsとgrepを使えば解けます
```
net40-dhcp48:file yotti$ strings strings | grep pico
picoCTF{sTrIngS_sAVeS_Time_d3ffa29c}
```

``picoCTF{sTrIngS_sAVeS_Time_d3ffa29c}``

## pipe - Points: 110 ##
question:
```
During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with 2018shell3.picoctf.com 2015.
```
grepとnc使えば解けます

```
net40-dhcp48:file yotti$ nc 2018shell3.picoctf.com 2015  >> test
test.txt   test.txt~  testfile   
net40-dhcp48:file yotti$ nc 2018shell3.picoctf.com 2015  >> output
net40-dhcp48:file yotti$ cat output | grep pico
picoCTF{almost_like_mario_8861411c}
```
``picoCTF{almost_like_mario_8861411c}``

## Inspect Me - Points: 125 ##

question:
```
Inpect this code! http://2018shell3.picoctf.com:56252 (link)
```

web問題は苦手ですが,これは簡単なのでいけますw

sourceを見れば, flagが書いてあります。<br>
index.html, css,　my.jsにそれぞれ書いてありました

index.html
```
       :                      :
  JS (JavaScript)
  </p>
  <!-- I learned HTML! Here's part 1/3 of the flag: picoCTF{ur_4_real_1nspe -->
```

mycss.css
```
       :                :
#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* I learned CSS! Here's part 2/3 of the flag: ct0r_g4dget_098df0d0} */
```

myjs.js
```
          :        :
window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* I learned JavaScript! Here's part 3/3 of the flag:  */
```

合わせると, ``picoCTF{ur_4_real_1nspect0r_g4dget_098df0d0}``

## grep 2 - Points: 125 ##

question:
```
This one is a little bit harder. Can you find the flag in /problems/grep-2_4_06c2058761f24267033e7ca6ff9d9144/files on the shell server? Remember, grep is your friend.
``` 

これもgrep使う問題です.今回はフォルダごとgrepを使います.
オプション-rを使ってフォルダ探索するだけです

```
yocchi@pico-2018-shell-3:~$ grep -r "pico" /problems/grep-2_4_06c2058761f24267033e7ca6ff9d9144/files
/problems/grep-2_4_06c2058761f24267033e7ca6ff9d9144/files/files4/file1:picoCTF{grep_r_and_you_will_find_036bbb
25}  
```
