## PicoCTF 2018 ##
## Introduction ##

hello! I'm yotti.<br>
今回はpicoCTFの問題を解いてみましたー<br>
やった感じ,ビギナーズ向けのctfでした<br>後半解けない問題がありましたが...<br>
ctf初心者とか,最近やったばっかりとかの人にはぴったりだったのではないでしょうか？<br>
それ問題を解いたのに,"you or one of your teammates have already tried this solutions"<br>
となり解いたことにならなかった問題が多々あり困ってます(現在進行形)<br>
I don't know what is this problem for us, please teach me to solve its problem!!<br>


前半はクソ簡単なので飛ばします.<br>
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

loginしてみましょー、

```
net40-dhcp179:file yotti$   nc 2018shell2.picoctf.com 5221
Username: root
Password: kissme
picoCTF{J0hn_1$_R1pp3d_289677b5}
```

出ましたねー、``picoCTF{J0hn_1$_R1pp3d_289677b5}``
今後も色々使うと思うのでもっとjohnの使い方についてマスターしたいと思います...

