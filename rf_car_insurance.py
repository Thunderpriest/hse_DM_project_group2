import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import roc_auc_score

# read data into pandas data frames
train_df = pd.read_csv("data/car_insurance_train.csv",
                       header=0, index_col=0)
test_df = pd.read_csv("data/car_insurance_test.csv",
                      header=0, index_col=0)


# number of observations (objects) in train and test sets
n_train, n_test = train_df.shape[0], test_df.shape[0]

# auto brand and compenstaed are categorical so we encode these columns
# ex: "Volvo" -> 1, "Audi" -> 2 etc
auto_brand_encoder = preprocessing.LabelEncoder()
auto_brand_encoder.fit(train_df['auto_brand'])
target_encoder = preprocessing.LabelEncoder()
target_encoder.fit(train_df['compensated'])

# form a numpy array to fit as a train set
# X will have encoded columns 'auto_brand' and 'fines'
X = np.hstack([auto_brand_encoder.transform(train_df['auto_brand'])
              .reshape([n_train,1]),
               train_df['fines']
              .reshape([n_train,1])])

# form a numpy array to fit as train set labels
y = target_encoder.transform(train_df['compensated'])

# form a numpy array of a test set
X_test = np.hstack([auto_brand_encoder.transform(test_df['auto_brand'])
              .reshape([n_test,1]),
               test_df['fines']
              .reshape([n_test,1])])

# make an instance of RF classifier
clf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)

# fit X and y (train set and corresponding labels) to the classifier
clf.fit(X,y)

# make predictions. This results in 0.718 AUC score
predicted_labels = clf.predict(X_test)

# turn predictions into data frame and save as csv file
predicted_df = pd.DataFrame(predicted_labels,
                            index = np.arange(1, n_test+1),
                            columns=["compensated"])
predicted_df.to_csv("data/rf_prediction.csv", index_label="id")

## that's for me, you don't know the answers
# expected_labels_df = pd.read_csv("data/car_insurance_test_labels.csv",
#                                  header=0, index_col=0)
# expected_labels = target_encoder.transform(expected_labels_df['compensated'])
# print(roc_auc_score(predicted_labels, expected_labels))

