from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd

class DataPredict(BaseModel):
    name: str = "udin"
    pclass : int = 3
    sex : str = "male"
    age : float = 20
    sibsp : int = 1
    parch : int = 2
    fare : float = 200

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/titanic/predict")
def predict(datas : list[DataPredict]):
    model = pickle.load(open("./model/knn_titanic.pkl", "rb"))
    datapredict = []
    for data in datas:
        datapredict.append([
            data.pclass,
            data.sex,
            data.age,
            data.sibsp,
            data.parch,
            data.fare
        ])
    X_pred = pd.DataFrame(datapredict, index=[x.name for x in datas], columns=['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare'])
    res = model.predict(X_pred)
    newdata = []
    for i, datum, dat in zip(res, datapredict, datas):
        newdata.append({
            'name': dat.name,
            'pclass': datum[0], 
            'sex': datum[1], 
            'age': datum[2], 
            'sibsp': datum[3], 
            'parch': datum[4], 
            'fare': datum[5],
            'survived': i.item()
        })
    return {"data": newdata}