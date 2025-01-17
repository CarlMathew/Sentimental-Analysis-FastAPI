import joblib
import pandas as pd
model = joblib.load("..\models\sentiment_model.pkl")


test = pd.DataFrame(
    {
        "Time of Tweet": ["morning", "noon", "noon"],
        "text": ["The product is okay, but it could be better.", "I absolutely love this product; it works perfectly", "The product stopped working after just one week. Very disappointing."]

    }
)

prediction = model.predict(test)
print(prediction)