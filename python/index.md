# 基本テンプレート

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


# json

## 書き込み

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


## 読み込み

```
import json
import codecs

fp = codecs.open('sample.json', 'r', 'utf-8')
json_text = fp.read()
fp.close()

dictData = json.loads(json_text)
print(dictData)
```



# テキストファイル

## 書き込み

```
import codecs

text = 'ああああああ\nいいいいいいい\nうううううう'

fp = codecs.open('sample.txt', 'w', 'utf-8')
fp.write(text)
fp.close()
```


## 読み込み

```
import codecs

fp = codecs.open('sample.txt', 'r', 'utf-8')
text = fp.read()
fp.close()

print(text)
```