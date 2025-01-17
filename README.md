The API was built using FastAPI Framework

To run the code on your local server

1. Create a environmental variable
   `python -m venv venv`

2. Activate the virtual environment
   `venv\Scripts\activate`

3. To install the packages in requirements.txt
   `pip install -r requirements.txt`

4. Since this is fastapi framework you can run the API using
   `uvicorn main:app --reload` #make sure that you are in the directory path

The main.py is the main app of this API, all of the api can be seen in the routers folder

`sentiment_routers.py` contains the api and the model path contains the pre-trained model that I used
You can also check the data that I used in the `models/data/sentimental_analysis.csv`

You can modify the model in `models/sentiment_model.py`. I haven't done a fine tuning on it

then dump the model using joblib

```python
#code for dumping
model = joblib.dump(variable_model_name, "root_to_dump.pkl")

#then re run the api again
```

Parameters that is needed for the api

time = "morning | noon | night "
text = text of the sentiment

you can access the api using `https://sentimental-analysis-fastapi.onrender.com/GetSentimentValue`
