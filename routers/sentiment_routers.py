import joblib
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
import schemas
import json
import os
import pandas as pd
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models_path", "sentiment_model.pkl")

model = joblib.load(model_path)



router = APIRouter(tags=["sentiment"])


@router.get("/GetSentimentValue", status_code=status.HTTP_200_OK)
async def getSentimentValue(payload: schemas.Sentiment = Depends(schemas.Sentiment)):
    print(payload.time)
    print(payload.text)

    data = pd.DataFrame(
        {
            "Time of Tweet": [payload.time],
            "text": [payload.text]

        }
    )

    prediction = model.predict(data)
    return {"status": "success", "prediction": prediction[0]}

