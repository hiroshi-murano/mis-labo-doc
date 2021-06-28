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


fp = codecs.open('sample.json', 'r', 'utf-8')
json_text = fp.read()
fp.close()

dictData = json.loads(json_text)
print(dictData)
