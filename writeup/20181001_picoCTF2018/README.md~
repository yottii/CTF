## PicoCTF 2018 ##
## Introduction ##

hello! I'm yotti.<br>
今回はpicoCTFの問題を解いてみましたー<br>
やった感じ,ビギナーズ向けのctfでした<br>後半解けない問題がありましたが...<br>
ctf初心者とか,最近やったばっかりとかの人にはぴったりだったのではないでしょうか？<br>
それ問題を解いたのに,"you or one of your teammates have already tried this solutions"<br>
となり解いたことにならなかった問題が多々あり困ってます(現在進行形)<br>
I don't know what is this problem for us, please teach me to solve its problem!!<br>


Forensics Warmup 1 - Points: 50 - (Solves: 9470) Forensics -  
Forensics Warmup 2 - Points: 50 - (Solves: 8980) Forensics -  
General Warmup 1 - Points: 50 - (Solves: 11485) General Skills -  
General Warmup 2 - Points: 50 - (Solves: 11381) General Skills -  
General Warmup 3 - Points: 50 - (Solves: 11221) General Skills -  
Resources - Points: 50 - (Solves: 10234) General Skills -  
Reversing Warmup 1 - Points: 50 - (Solves: 6677) Reversing -  
Reversing Warmup 2 - Points: 50 - (Solves: 8007) Reversing -  
Crypto Warmup 1 - Points: 75 - (Solves: 5080) Cryptography -  
Crypto Warmup 2 - Points: 75 - (Solves: 7699) Cryptography -  
grep 1 - Points: 75 - (Solves: 8061) General Skills -  
net cat - Points: 75 - (Solves: 7215) General Skills -  
HEEEEEEERE'S Johnny! - Points: 100 - (Solves: 2602) Cryptography -  
strings - Points: 100 - (Solves: 5496) General Skills -  
pipe - Points: 110 - (Solves: 4962) General Skills -  
Inspect Me - Points: 125 - (Solves: 6765) Web Exploitation -  
grep 2 - Points: 125 - (Solves: 4739) General Skills -  
Aca-Shell-A - Points: 150 - (Solves: 3133) General Skills -  
Client Side is Still Bad - Points: 150 - (Solves: 6021) Web Exploitation -  
Desrouleaux - Points: 150 - (Solves: 2237) Forensics -  
Logon - Points: 150 - (Solves: 3239) Web Exploitation -  
Reading Between the Eyes - Points: 150 - (Solves: 2426) Forensics -  
Recovering From the Snap - Points: 150 - (Solves: 1962) Forensics -  
admin panel - Points: 150 - (Solves: 3774) Forensics -  
assembly-0 - Points: 150 - (Solves: 1924) Reversing -  
buffer overflow 0 - Points: 150 - (Solves: 2662) Binary Exploitation -  
caesar cipher 1 - Points: 150 - (Solves: 4485) Cryptography -  
environ - Points: 150 - (Solves: 3464) General Skills -  
hertz - Points: 150 - (Solves: 2690) Cryptography -  
hex editor - Points: 150 - (Solves: 3710) Forensics -  
ssh-keyz - Points: 150 - (Solves: 2954) General Skills -  
Irish Name Repo - Points: 200 - (Solves: 3037) Web Exploitation -  
Mr. Robots - Points: 200 - (Solves: 3093) Web Exploitation -  
Truly an Artist - Points: 200 - (Solves: 3169) Forensics -  
be-quick-or-be-dead-1 - Points: 200 - (Solves: 1165) Reversing -  
leak-me - Points: 200 - (Solves: 1897) Binary Exploitation -  
now you don't - Points: 200 - (Solves: 3221) Forensics -  
shellcode - Points: 200 - (Solves: 924) Binary Exploitation -  
what base is this? - Points: 200 - (Solves: 3235) General Skills -  
Buttons - Points: 250 - (Solves: 2534) Web Exploitation -  
got-2-learn-libc - Points: 250 - (Solves: 382) Binary Exploitation -  
rsa-madlibs - Points: 250 - (Solves: 962) Cryptography -  
echooo - Points: 300 - (Solves: 860) Binary Exploitation -  
got-shell? - Points: 350 - (Solves: 523) Binary Exploitation -  
LoadSomeBits - Points: 550 - (Solves: 424) Forensics -  



問題はこんな感じですね、前半はクソ簡単なので省略します。
pint100くらいから解説します(それでも簡単だが....)



## HEEEEEEERE'S Johnny! - Points: 100 - ##

問題文は以下のとおり

```
Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with nc 2018shell3.picoctf.com 42165. Files can be found here: passwd shadow.
```

これはjohn the ripperを使う問題っぽいですね、passwdとshadowファイルが与えられています.
では早速解いていきましょう！！

とりあえず nc 2018shell3.picoctf.com 42165に接続してみます。

'''
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

