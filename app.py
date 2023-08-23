from fastapi import FastAPI
import uvicorn
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi import Response
from src.textSummarizer.pipeline.prediction import PredictionPipeline

text: str = "What is the text Summarization"

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful !!")
    except Exception as e:
        return Response(f"Error occurred ! {e}")


@app.post("/predict")
async def predict_route(text: str):  #
    try:
        obj = PredictionPipeline()
        result_text = obj.predict(text)
        return {"result": result_text}
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
