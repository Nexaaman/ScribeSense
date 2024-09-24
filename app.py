from fastapi import FastAPI
import uvicorn
import sys
import os

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from ScribeSense.pipeline.prediction import PredictionPipeline
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str = "What is Text Summarization?"


app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python3 main.py")
        return Response("Traning Sucessfully!")
    except Exception as e:
        return Response(f"Error Occured! {e}")
    
@app.post("/predict")
async def predict_route(request: TextRequest):
    try:
        obj = PredictionPipeline()
        text = obj.predict(request.text)
        return {"summary": text} 
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)