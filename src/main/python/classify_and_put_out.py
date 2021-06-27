import csv
import shutil

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def classify_and_put_out(dataset_path, classifier, input_file_name_test_plds, output_left, output_right):
    dataset = pd.read_csv(dataset_path, encoding = 'latin1')
    x = dataset.iloc[:, 1:].values
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    y_pred = classifier.predict(x)
    y_proba = classifier.predict_proba(x)
    left = open(output_left, 'a', newline='')
    csv_writer_left = csv.writer(left)
    with open(input_file_name_test_plds, newline='') as train:
        plds = csv.reader(train, delimiter=' ', quotechar='|')
        count = 0
        for pld in plds:
            if y_pred[count] == 'L':
                csv_writer_left.writerow([pld][0] + [y_proba[count][0]])
            count += 1
    left.close()
    right = open(output_right, 'a', newline='')
    csv_writer_right = csv.writer(right)
    with open(input_file_name_test_plds, newline='') as train:
        plds = csv.reader(train, delimiter=' ', quotechar='|')
        count = 0
        for pld in plds:
            if y_pred[count] == 'R':
                csv_writer_right.writerow([pld][0] + [y_proba[count][1]])
            count += 1
    right.close()
    shutil.copyfile(output_left, '../resources/generated_left.csv')
    shutil.copyfile(output_right, '../resources/generated_right.csv')





