#This is the main server file which will be started by cli at user specified port and url
#Then it will cache the data coming at that url into the cache server.
from cache import set_cache,get_cache,clear_cache
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"message":"Fast api is woring"}



@app.get('/about')
def some():
    return {"message":"about is returning"}