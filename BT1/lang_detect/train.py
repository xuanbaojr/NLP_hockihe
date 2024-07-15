# import necessary libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Load the data
data = pd.read_csv("./dataset/comments.csv")
print(data.head())

# Null values
print("checking any null values or not")
print(data.isnull().sum())

# Languages present in this dataset
print("value_counts")
print(data["Language"].value_counts())

# Split the data into training and tet sets
x = np.array(data["Text"])
y = np.array(data["Language"])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Multinomial Naive Bayes algorithm
model = MultinomialNB()
model.fit(X_train, y_train)

# Score
print("score", model.score(X_test, y_test))

# Predict
user_input = input("Enter a text: ")
data = cv.transform([user_input]).toarray()
output = model.predict(data)
print(output)


# SVM, Decision tree, logistic regression,...