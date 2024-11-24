import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Функція для обробки тексту
def process_text(input_file, output_file):
    # Зчитування тексту з файлу
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено!")
        return
    
    # Токенізація по словах
    tokens = word_tokenize(text)

    # Видалення пунктуації
    tokens_no_punct = [word for word in tokens if word not in string.punctuation]

    # Видалення стоп-слів
    stop_words = set(stopwords.words('english'))
    tokens_no_stopwords = [word for word in tokens_no_punct if word.lower() not in stop_words]

    # Лемматизація
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens_no_stopwords]

    # Стеммінг
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in lemmatized_tokens]

    # Запис обробленого тексту в інший файл
    processed_text = ' '.join(stemmed_tokens)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_text)

    print(f"Оброблений текст збережено у файл {output_file}")

# Виконання функції
process_text('text.txt', 'processed_text.txt')
