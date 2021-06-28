import csv
import shutil
from os import path
from twarc import Twarc


consumer_key = ''
consumer_secret= ''
access_token= ''
access_token_secret= ''


def hydrate_tweets_texts_per_pld(pld, output_directory_hydrated_tweets, id_directory):
    id_link = id_directory+'tweet_ids_'+pld+'.txt'
    t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)
    hydrated_tweets_text_file = open(output_directory_hydrated_tweets+'hydrated_texts_'+pld+'.txt', 'w', errors='ignore')
    for tweet in t.hydrate(open(id_link)):
        hydrated_tweets_text_file.writelines(tweet['full_text'])
    hydrated_tweets_text_file.close()


def hydrate_tweets_descriptions_per_pld(pld, output_directory_hydrated_tweets, id_directory):
    id_link = id_directory+'tweet_ids_'+pld+'.txt'
    t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)
    hydrated_tweets_text_file = open(output_directory_hydrated_tweets+'hydrated_descriptions_'+pld+'.txt', 'w', errors='ignore')
    for tweet in t.hydrate(open(id_link)):
        hydrated_tweets_text_file.writelines(tweet['user']['description'])
    hydrated_tweets_text_file.close()


def collect_hydrated_tweets(input_file_name_left, input_file_name_right, output_directory_hydrated_tweets, id_directory):
    with open(input_file_name_left, newline='') as left_train:
        left_plds = csv.reader(left_train, delimiter=' ', quotechar='|')
        for pld in left_plds:
            hydrate_tweets_texts_per_pld(pld[0], output_directory_hydrated_tweets, id_directory)
    with open(input_file_name_right, newline='') as right_train:
        right_plds = csv.reader(right_train, delimiter=' ', quotechar='|')
        for pld in right_plds:
            hydrate_tweets_texts_per_pld(pld[0], output_directory_hydrated_tweets, id_directory)


def collect_hydrated_tweets_descriptions(input_file_name_left, input_file_name_right, output_directory_hydrated_tweets, id_directory):
    with open(input_file_name_left, newline='') as left_train:
        left_plds = csv.reader(left_train, delimiter=' ', quotechar='|')
        for pld in left_plds:
            hydrate_tweets_descriptions_per_pld(pld[0], output_directory_hydrated_tweets, id_directory)
    with open(input_file_name_right, newline='') as right_train:
        right_plds = csv.reader(right_train, delimiter=' ', quotechar='|')
        for pld in right_plds:
            hydrate_tweets_descriptions_per_pld(pld[0], output_directory_hydrated_tweets, id_directory)


def collect_hydrated_tweets(input_file_name, output_directory_hydrated_tweets, id_directory):
    with open(input_file_name, newline='') as train:
        plds = csv.reader(train, delimiter=' ', quotechar='|')
        for pld in plds:
            hydrate_tweets_texts_per_pld(pld[0], output_directory_hydrated_tweets, id_directory)


def collect_hydrated_tweets_test_data_descriptions(input_file_name, output_directory_hydrated_tweets, id_directory):
    with open(input_file_name, newline='') as train:
        plds = csv.reader(train, delimiter=' ', quotechar='|')
        for pld in plds:
            hydrate_tweets_descriptions_per_pld(pld[0], output_directory_hydrated_tweets, id_directory)


def move_hydrated_tweets_to_pol_directory():
    input_file_name_left = '../../../input_data/left_train.csv'
    input_file_name_right = '../../../input_data/right_train.csv'
    with open(input_file_name_left, newline='') as left_train:
        left_plds = csv.reader(left_train, delimiter=' ', quotechar='|')
        for pld in left_plds:
            source_path_texts = '../resources/hydrated_tweets_texts/hydrated_texts_'+pld[0]+'.txt'
            if path.exists(source_path_texts):
                shutil.move(source_path_texts, '../resources/hydrated_tweets_texts/left/hydrated_texts_'+pld[0]+'.txt')
    with open(input_file_name_right, newline='') as right_train:
        right_plds = csv.reader(right_train, delimiter=' ', quotechar='|')
        for pld in right_plds:
            source_path_texts = '../resources/hydrated_tweets_texts/hydrated_texts_' + pld[0] + '.txt'
            if path.exists(source_path_texts):
                shutil.move(source_path_texts,
                            '../resources/hydrated_tweets_texts/right/hydrated_texts_' + pld[0] + '.txt')


def move_hydrated_tweets_to_pol_directory_descriptions():
    input_file_name_left = '../../../input_data/left_train.csv'
    input_file_name_right = '../../../input_data/right_train.csv'
    with open(input_file_name_left, newline='') as left_train:
        left_plds = csv.reader(left_train, delimiter=' ', quotechar='|')
        for pld in left_plds:
            source_path_texts = '../resources/hydrated_tweets_descriptions/hydrated_descriptions_'+pld[0]+'.txt'
            if path.exists(source_path_texts):
                shutil.move(source_path_texts, '../resources/hydrated_tweets_descriptions/left/hydrated_descriptions_'+pld[0]+'.txt')
    with open(input_file_name_right, newline='') as right_train:
        right_plds = csv.reader(right_train, delimiter=' ', quotechar='|')
        for pld in right_plds:
            source_path_texts = '../resources/hydrated_tweets_descriptions/hydrated_descriptions_' + pld[0] + '.txt'
            if path.exists(source_path_texts):
                shutil.move(source_path_texts,
                            '../resources/hydrated_tweets_descriptions/right/hydrated_descriptions_' + pld[0] + '.txt')





