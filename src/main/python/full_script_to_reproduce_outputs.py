from hydrate_tweets import collect_hydrated_tweets_descriptions, move_hydrated_tweets_to_pol_directory_descriptions
from generate_feature_set import generate_feature_set, generate_feature_set_descriptions
from generate_dataset_with_features import generate_labeled_dataset_with_features

input_file_name_left = '../../../input_data/left_train.csv'
input_file_name_right = '../../../input_data/right_train.csv'
output_directory_tweet_ids = '../resources/tweet_ids/'
output_directory_hydrated_tweets = '../resources/hydrated_tweets_texts/'
output_directory_hydrated_tweets_descriptions = '../resources/hydrated_tweets_descriptions/'
output_file_name_labeled_dataset = 'dataset_labeled'
output_file_name_labeled_dataset_descriptions = 'dataset_labeled_descriptions'

input_file_name_test_plds = '../../../input_data/test.csv'
output_directory_tweet_ids_test_data = '../resources/tweet_ids_test_data/'
output_directory_hydrated_tweets_test_data = '../resources/hydrated_tweets_test_data_texts/'
output_file_name_test_dataset = 'dataset_test_data'
output_left = '../../../output_data/left.csv'
output_right = '../../../output_data/right.csv'

#train the classifier
#collect_tweet_ids_per_pld(input_file_name_left, input_file_name_right, output_directory_tweet_ids)
#collect_hydrated_tweets(input_file_name_left, input_file_name_right, output_directory_hydrated_tweets, output_directory_tweet_ids)
#collect_hydrated_tweets_descriptions(input_file_name_left, input_file_name_right, output_directory_hydrated_tweets_descriptions, output_directory_tweet_ids)
#move_hydrated_tweets_to_pol_directory()
#move_hydrated_tweets_to_pol_directory_descriptions()
#generate_feature_set()
#generate_feature_set_descriptions()
#generate_labeled_dataset_with_features(output_file_name_labeled_dataset, input_file_name_left, input_file_name_right, output_directory_hydrated_tweets)
generate_labeled_dataset_with_features(output_file_name_labeled_dataset_descriptions, input_file_name_left, input_file_name_right, output_directory_hydrated_tweets)
#classifier = train_classifier(output_file_name_labeled_dataset)
#prepare dataset and classify test data
#collect_tweet_ids_per_pld(input_file_name_test_plds, output_directory_tweet_ids_test_data)
#collect_hydrated_tweets(input_file_name_test_plds, output_directory_hydrated_tweets_test_data, output_directory_tweet_ids_test_data)
#generate_test_dataset_with_features(output_file_name_test_dataset, input_file_name_test_plds, output_directory_hydrated_tweets_test_data)
#classify_and_put_out(output_file_name_test_dataset, classifier, input_file_name_test_plds, output_left, output_right)


