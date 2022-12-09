from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from joblib import dump, load

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from preprocessing import VietnamesePreprocessing

app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    result = "Type a comment and submit"
    context = {'request': request, 'result': result}
    return templates.TemplateResponse("index.html", context)


preprocess = VietnamesePreprocessing()
tfidf_vect = load('tfidf_vect.pkl')
model = load('../SpamDetection/spam_model_TF_IDF_NB.pkl')


@app.post('/', response_class=HTMLResponse)
async def index(request: Request, cmt: str = Form(...)):
    cmt = preprocess(cmt)
    data = tfidf_vect.transform([cmt])
    predict = str(model.predict(data))
    if predict == '[1]':
        result = 'Spam comment'
    else:
        result = 'Not Spam'
    context = {'request': request, 'result': result}
    return templates.TemplateResponse("index.html", context)


@app.get("/aaa")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

    #<link href="{{ url_for('static', path='/style.css') }}" rel="stylesheet">