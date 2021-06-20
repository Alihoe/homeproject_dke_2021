import csv
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from os import path

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))


def count_features_of_pld(pld_text_file_path, features):
    with open(pld_text_file_path) as file_content:
        text = file_content.read()
    word_tokens = word_tokenize(text)
    filtered = [w for w in word_tokens if w not in stop_words]
    words = [w.lower() for w in filtered]
    count_features = []
    for w in features:
        count_features.append(words.count(w))
    return count_features


def generate_labeled_dataset_with_features(output_file_name, input_file_name_left, input_file_name_right, hydrated_tweets_directory):
    data_file = open(output_file_name, 'w')
    csv_writer = csv.writer(data_file)
    # prepare header
    with open('word_feature_set.txt', "r") as feature_set:
        features_new_lines = feature_set.readlines()
    features = []
    for line in features_new_lines:
        features.append(line.replace("\n", ""))
    header = features.copy()
    header.insert(0, "PLD")
    header.insert(1, "bias(L for left and R for right)")
    csv_writer.writerow(header)
    # print data
    with open(input_file_name_left, newline='') as left_train:
        left_plds = csv.reader(left_train, delimiter=' ', quotechar='|')
        for pld in left_plds:
            text_path = hydrated_tweets_directory+'left/hydrated_texts_'+pld[0]+'.txt'
            if path.exists(text_path):
                count_features = count_features_of_pld(text_path, features)
                csv_writer.writerow([pld] + ['L'] + count_features)
    with open(input_file_name_right, newline='') as right_train:
        right_plds = csv.reader(right_train, delimiter=' ', quotechar='|')
        for pld in right_plds:
            text_path = hydrated_tweets_directory+'right/hydrated_texts_' + pld[0] + '.txt'
            if path.exists(text_path):
                count_features = count_features_of_pld(text_path, features)
                csv_writer.writerow([pld] + ['R'] + count_features)
    data_file.close()


def generate_test_dataset_with_features(output_file_name, input_file_name, hydrated_tweets_directory):
    data_file = open(output_file_name, 'w')
    csv_writer = csv.writer(data_file)
    # prepare header
    with open('word_feature_set.txt', "r") as feature_set:
        features_new_lines = feature_set.readlines()
    features = []
    for line in features_new_lines:
        features.append(line.replace("\n", ""))
    header = features.copy()
    header.insert(0, "PLD")
    csv_writer.writerow(header)
    # print data
    with open(input_file_name, newline='') as train:
        plds = csv.reader(train, delimiter=' ', quotechar='|')
        for pld in plds:
            text_path = hydrated_tweets_directory+'hydrated_texts_'+pld[0]+'.txt'
            if path.exists(text_path):
                count_features = count_features_of_pld(text_path, features)
                csv_writer.writerow([pld] + count_features)
    data_file.close()
