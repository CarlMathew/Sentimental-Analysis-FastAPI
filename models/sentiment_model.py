# Setting up the model
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

df = pd.read_csv("./data/sentiment_analysis.csv")
df = df[["Time of Tweet", "text", "sentiment"]]

one_hot = OneHotEncoder(sparse_output=False)
vectorizer = TfidfVectorizer()


one_hot_pipe = Pipeline([
    ("one_hot", one_hot)
])

vectorizer_pipe = Pipeline([
    ("vectorizer", vectorizer)
])


preprocessor = ColumnTransformer([
    ("one_hot", one_hot_pipe, ["Time of Tweet"]),
    ("vectorizer", vectorizer_pipe, "text")
], remainder = "passthrough")

model = MultinomialNB()


final_pipe = Pipeline([("preprocessor", preprocessor), ("model", model)])

X = df.drop("sentiment", axis = 1)
y = df["sentiment"]

final_pipe.fit(X, y)

joblib.dump(final_pipe, "sentiment_model.pkl")

print("Model saved as sentiment_model.pkl")


