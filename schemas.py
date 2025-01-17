from pydantic import BaseModel 

class Sentiment(BaseModel):
    time: str
    text: str