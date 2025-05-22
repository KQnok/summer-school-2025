from collections import Counter
import re

print("Введите зашифрованный текст:")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)

all_text = ''.join(lines)

def filter_russian_chars(text: str) -> str:
    return re.sub(r'[^0-9а-яё ]', '', text.lower())

rus_text = filter_russian_chars(all_text)

words = rus_text.split(' ')
word_counts = Counter(words)
result = [word for word in words if word_counts[word] <= 1] #если тут вместо 1 поставить 4, то это шикарно работает для про(выявлено научным методом тыка)

print(' '.join(result))

