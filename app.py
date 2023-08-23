from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2template
from startlette.response import RedirectResponse
from fastapi import Response
from src.textSummarizer.pipeline.prediction import PredictionPipeline


text: str = "What is the text Summarization"

app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Succesfull !!")
    except Exception as e:
        return Response(f"Error occurred ! {e}")
      
      
