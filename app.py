from fastapi import FastAPI, HTTPException
import uvicorn
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel
from ScribeSense.pipeline.prediction import PredictionPipeline


class TextRequest(BaseModel):
    text: str = "What is Text Summarization?"
    length_penalty: float = 0.8

app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.post("/predict", tags=["prediction"])
async def predict_route(request: TextRequest):
    try:
        
        prediction_pipeline = PredictionPipeline()
        
        summarized_text = prediction_pipeline.predict(request.text, request.length_penalty)
        return {"summary": summarized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
