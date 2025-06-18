from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"message":"Fast api is woring"}



@app.get('/about')
def some():
    return {"message":"about is returning"}