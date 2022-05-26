# Bear
This script adds "くま" to a suitable place in a Japanese sentence so that it becomes to sound like it is spoken by a bear.

## Basic usage
`$ python3 main.py arg`

arg is a japanese sentence which you would like.

## Examples

```
$ python3 main.py 
例文が渡されていません。強制終了します。
$ python3 main.py  そうなの？
そうなのくま？
$ python3 main.py  いまどこいるの？
いまどこいるのくま？
$ python3 main.py  お腹が空いた。。
お腹が空いたくま。。
$ python3 main.py 6月に引っ越し予定なんだ。
6月に引っ越し予定なんだくま。
$ python3 main.py  今日はもう眠い。
今日はもう眠いくま。
$ python3 main.py  すもももももももものうち
すもももももももものうちくま
```
## Dependency
You need to install mecab-python3 and  unidic-lite.

```pip install mecab-python3```

```pip install unidic-lite```
