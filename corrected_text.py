import string
import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import pipeline

grammar_corrector = pipeline('text2text-generation', model="facebook/bart-large-cnn")

import nltk
nltk.download('stopwords')
nltk.download("punkt_tab")
nltk.download('wordnet')


def clean_and_correct_text(text):
    # Lowercasing
    text = text.lower()

    # Removing punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Removing numbers (optional)
    text = re.sub(r'\d+', '', text)

    # Removing extra spaces
    text = ' '.join(text.split())

    text = str(TextBlob(text).correct())
    # print(text)

    text = grammar_corrector(text)[0]["generated_text"]

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

   

    return text

# input_text = "Thiss is an exampel text with sum erors and gramatical issues."

# corrected_text = clean_and_correct_text(input_text)
# print(corrected_text)
