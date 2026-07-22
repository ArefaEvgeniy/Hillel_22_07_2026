# from langdetect import detect, detect_langs
import langdetect
import math


text_en = "Hello, world!. This is an example text in English."
text_du = "Hallo, Welt!. Dies ist ein Beispieltext auf Deutsch."
text_ch = "你好，世界！这是中文的示例文本。"
test_ru = "Привет, мир!. Это мові."

print(langdetect.detect(text_en))
print(langdetect.detect_langs(text_du))
print(langdetect.detect_langs(test_ru))
print(langdetect.detect_langs(text_ch))

print(math.sin(34))
print(math.pi)
