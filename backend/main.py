from typing import Union

from fastapi import FastAPI, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .models import DogImage
from .model_utils import get_clf_model, clf_breed


clf_model = get_clf_model()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="backend/templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/predict-breed/")
def predict_breed(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})

@app.post("/api/predict-breed/")
async def predict_breed(dog_image: DogImage):
    image_bytes = dog_image.image_bytes
    respon = clf_breed(clf_model, image_bytes, dog_image.top_n)
    return JSONResponse(respon)
