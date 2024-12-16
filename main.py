from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") 

conn = MongoClient("mongodb://localhost:27017/fastapiTest")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
  docs = conn.fastapiTest.notes.find_one()
  print(docs)
  return templates.TemplateResponse("index.html", {
    "request": request,
    "docs": docs
  })