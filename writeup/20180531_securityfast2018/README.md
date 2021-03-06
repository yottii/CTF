今回はsecurityfast2018で解けた問題の解説等を書いていこと思います。<br>
今回チャレンジした問題は以下のものです。

## Misc ##
51 point EveryWhere<br>
51 point Mr.reagan

## Rev ##
51 point Bluepil

## Crypto ##
51 The Oracle

上記の問題です。<br>
正直高ポイントの問題を解こうとしましたが全く歯が立たなかったです。<br>
では解説をしていきたいと思います。


## 51/Misc EveryWhere ##

この問題は画像との差分を出す問題でした。<br>
まずEveryWhere.tar.gz形式なのでファイルを解凍します。<br>
そしてファイルの形式を調べると

```
net40-dhcp199:ctf yotti$ file everywhere
everywhere: JPEG image data
```

imageファイルだということがわかりました。

そこからeverywhereファイルに拡張子をつけます.そうすると

![](image/everyware.jpg)

以上のような画像にが出現しました。<br>
そこからステガノグラフィーの解析を使って色のバイトを抜いたりしましたが
何も情報は得ることができませんでした。<br?
そこで煮た画像を探して差分を探すことにしました。<br>
googleの画像検索するとほぼ似た画像が出てきました。<br>
同じ画像サイズで差分を取ってあげると。。。<br>

![](image/everywhere.png)

flagを入手できましたね。

`sctf{y0u_411_100k_th3_54m3_t0_m3}`

文字列が出てきました！

## 51/Misc mr.reagan ##

まずはファイルの形式を調べます。<br>
そうすると

```
net40-dhcp199:ctf yotti$ file mrreagan 
mrreagan: x86 boot sector; partition 1: ID=0x72, starthead 13, startsector 
1920221984, 1816210284 sectors, code offset 0x52, OEM-ID "NTFS    ", 
sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, heads 255, 
hidden sectors 128, dos < 4.0 BootSector (0x80)
```

となり、ファイルの形式がNTFSということがわかります。<br>
これをマウントしてあげると、、、

```
$Info : c2N0ZnszbD
$Secure : NjdHIwbTRn
$Boot : bjN0MWNfcH
$Extend : VsNTNfdzRz
$LogFile : X2Y0azN9Cg
Morpheus.txt : This line is tapped, so I must be brief.
Tank.txt : 73656366
Dozer.txt : 73656366
Trinity.txt : I was looking for an answer. It’s the question that drives us mad.
Neo.txt : What is the Matrix.
```

というファイルがマウントされます。<br>
これらのファイルの

`c2N0ZnszbDNjdHIwbTRnbjN0MWNfcHVsNTNfdzRzX2Y0azN9Cg`

をbase64でデコードしてあげると、、、、

Flag : `sctf{3l3ctr0m4gn3t1c_pul53_w4s_f4k3}`

というflagが出てきました。
