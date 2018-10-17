# MEEPWN 2018 #

hello. I'm yotti.<br>

では解説してきたいと思います.<br>
今回解いた問題は,"White Snow Black Shadow"です.<br>
他は難しくて私には解けませんでた^^;

まずファイルを解凍すると,evidence.jpgというファイルが出てきます.<br>
これを見てみると,名探偵コナンの画像ファイルでした笑.<br>

![](file/evidence.jpg)

なんだか少し親近感が湧きつつ,解析を進めていきます<br>
まず画像にファイルが埋め込まれていないか調べてみます.<br>

'''

net40-dhcp179:file yotti$ binwalk -e evidence.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
217428        0x35154         End of Zip archive

'''