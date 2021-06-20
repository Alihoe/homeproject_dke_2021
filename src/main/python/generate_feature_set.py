import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

from collections import Counter
from itertools import repeat, chain

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))


def flatten_lists(the_lists):
    result = []
    for _list in the_lists:
        result += _list
    return result


def list_sorted_by_frequency(input_list):
    ordered_list = list(chain.from_iterable(repeat(i, c) for i, c in Counter(input_list).most_common()))
    without_punctuation = [w.translate(str.maketrans('', '', string.punctuation)) for w in ordered_list]
    no_letters = [w for w in without_punctuation if len(w) > 2]
    no_http = [w for w in no_letters if w != 'https']
    return list(dict.fromkeys(no_http))


def generate_feature_set():
    all_words = []
    for f in os.listdir('../resources/hydrated_tweets_texts/left'):
        with open('../resources/hydrated_tweets_texts/left/' + f, 'r', errors='ignore') as file_content:
            text = file_content.read()
        word_tokens = word_tokenize(text)
        filtered = [w for w in word_tokens if w not in stop_words]
        words = [w.lower() for w in filtered]
        all_words.append(words)
        all_words = flatten_lists(all_words)
    for f in os.listdir('../resources/hydrated_tweets_texts/right'):
        with open('../resources/hydrated_tweets_texts/right/' + f, 'r', errors='ignore') as file_content:
            text = file_content.read()
        word_tokens = word_tokenize(text)
        filtered = [w for w in word_tokens if w not in stop_words]
        words = [w.lower() for w in filtered]
        all_words.extend(words)
    all_words = list_sorted_by_frequency(all_words)
    word_features = all_words[:6000]
    print(word_features)
    word_features_file = open('word_feature_set.txt', 'w')
    for element in word_features:
        word_features_file.write(element)
        word_features_file.write('\n')
    word_features_file.close()

