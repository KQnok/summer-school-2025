import re
from collections import Counter
from typing import Tuple, List
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

SPAM_LABEL = 'spam'
MIN_WORD_LENGTH = 3

def load_dataset(file_path: str) -> Tuple[List[str], List[str]]:
    texts, labels = [], []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                label, text = line.strip().split('\t', maxsplit=1)
                labels.append(label.lower())
                texts.append(text)
            except ValueError:
                continue
    return texts, labels


def preprocess_text(text: str, stemmer: PorterStemmer, stopwords: set) -> List[str]:
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    words = [stemmer.stem(word) for word in word_tokenize(text)]
    return [word for word in words if word not in stopwords and len(word) >= MIN_WORD_LENGTH]


def analyze_word_frequencies(words: List[str]) -> List[Tuple[str, int]]:
    return Counter(words).most_common(10)

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip() for line in f}

def main():
    stemmer = PorterStemmer()
    stopwords = load_stopwords('stopwords.csv')

    texts, labels = load_dataset('sample.tsv')

    spam_words, ham_words = [], []
    for text, label in zip(texts, labels):
        words = preprocess_text(text, stemmer, stopwords)
        (spam_words if label == SPAM_LABEL else ham_words).extend(words)

    spam_top = analyze_word_frequencies(spam_words)
    ham_top = analyze_word_frequencies(ham_words)

    print("Топ-10 слов в спам-сообщениях:")
    for word, count in spam_top:
        print(f"{word}: {count}")

    print("\nТоп-10 слов в не-спам-сообщениях:")
    for word, count in ham_top:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()