from fastapi import FastAPI, status, Depends, HTTPException
import json
import schemas
from routers import sentiment_routers

app = FastAPI()

app.include_router(sentiment_routers.router)


