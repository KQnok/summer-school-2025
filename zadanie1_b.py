from collections import Counter

print("Введите зашифрованный текст:")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)

all_text = ''.join(lines)
rus_text = ''.join([char for char in all_text.lower() if char in "1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя "])

words = rus_text.split(' ')
word_counts = Counter(words)
result = [word for word in words if word_counts[word] <= 4]

print(' '.join(result))

