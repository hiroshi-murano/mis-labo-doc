import codecs


text = 'ああああああ\nいいいいいいい\nうううううう'
fp = codecs.open('sample.txt', "w", "utf-8")
fp.write(text)
fp.close()


fp = codecs.open('sample.txt', "r", "utf_8")
text = fp.read()
fp.close()

print(text)
