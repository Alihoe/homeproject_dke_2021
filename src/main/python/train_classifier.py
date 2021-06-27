import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler


def train_classifier(dataset_path):
    dataset = pd.read_csv(dataset_path, encoding='latin1')
    x = dataset.iloc[:, 2:].values
    y = dataset.iloc[:, 1].values
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    classifier = MultinomialNB()
    classifier.fit(x, y)
    return classifier
