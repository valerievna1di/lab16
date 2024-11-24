import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('stopwords')

# Функція для підрахунку кількості слів у тексті
def count_words(text):
    sentences = nltk.sent_tokenize(text)
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        k_words += len(words)
    return k_words

# Функція для очищення тексту від пунктуації та стоп-слів
def clean_text(text):
    # Видалення пунктуації (включаючи всі види лапок)
    no_punct = ''.join([char for char in text if char not in string.punctuation and char not in ['“', '”', '‘', '’', '``', "''"]])
    # Токенізація тексту
    tokens = nltk.word_tokenize(no_punct)
    # Видалення стоп-слів
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens)

# Функція для побудови діаграми найбільш вживаних слів
def most_used_words(text, title):
    words = text.split()
    cnt = Counter(words)
    common_words = cnt.most_common(10)
    x = [item[0] for item in common_words]
    y = [item[1] for item in common_words]
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='pink')
    plt.title(title)
    plt.xlabel("Слова")
    plt.ylabel("Частота")
    plt.xticks(rotation=45, ha="right")  # Обертання підписів на 45 градусів
    plt.tight_layout()  # Автоматичне коригування полів графіку
    plt.show()

# Основний код програми
try:
    with open('carroll-alice.txt', 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

# Вивід кількості слів у початковому тексті
print("Кількість слів у початковому тексті:", count_words(text))

# Побудова діаграми для початкового тексту
most_used_words(text, "10 найбільш вживаних слів у початковому тексті")

# Очищення тексту від пунктуації та стандартних стоп-слів
cleaned_text = clean_text(text)

# Вивід кількості слів у очищеному тексті
print("Кількість слів в обробленому тексті:", count_words(cleaned_text))

# Побудова діаграми для очищеного тексту
most_used_words(cleaned_text, "10 найбільш вживаних слів в обробленому тексті")
