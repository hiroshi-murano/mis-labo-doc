
<!-- TOC -->

- [1. 基本テンプレート](#1-%E5%9F%BA%E6%9C%AC%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88)
- [2. json](#2-json)
    - [2.1. 書き込み](#21-%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF)
    - [2.2. 読み込み](#22-%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF)
- [3. テキストファイル](#3-%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB)
    - [3.1. 書き込み](#31-%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF)
    - [3.2. 読み込み](#32-%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF)

<!-- /TOC -->

# 1. 基本テンプレート
<a id="markdown-%E5%9F%BA%E6%9C%AC%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88" name="%E5%9F%BA%E6%9C%AC%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88"></a>





```
import datetime


def func1():
    """
    """

    today = datetime.datetime.now()
    print(today.strftime("%Y/%m/%d %H:%M:%S"))


if __name__ == '__main__':

    func1()
```


# 2. json
<a id="markdown-json" name="json"></a>

## 2.1. 書き込み
<a id="markdown-%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF" name="%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF"></a>

```
import json
import codecs

dictData = {}
dictData['名前'] = '斉藤'
dictData['年齢'] = 25
dictData['体重'] = 54.3
dictData['入社日'] = '1995-09-15'

json_text = json.dumps(dictData, ensure_ascii=False, indent=2)

fp = codecs.open('sample.json', 'w', 'utf-8')
fp.write(json_text)
fp.close()
```


## 2.2. 読み込み
<a id="markdown-%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF" name="%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF"></a>

```
import json
import codecs

fp = codecs.open('sample.json', 'r', 'utf-8')
json_text = fp.read()
fp.close()

dictData = json.loads(json_text)
print(dictData)
```



# 3. テキストファイル
<a id="markdown-%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB" name="%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB"></a>

## 3.1. 書き込み
<a id="markdown-%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF" name="%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF"></a>

```
import codecs

text = 'ああああああ\nいいいいいいい\nうううううう'

fp = codecs.open('sample.txt', 'w', 'utf-8')
fp.write(text)
fp.close()
```


## 3.2. 読み込み
<a id="markdown-%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF" name="%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF"></a>

```
import codecs

fp = codecs.open('sample.txt', 'r', 'utf-8')
text = fp.read()
fp.close()

print(text)
```