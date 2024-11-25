from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

from preprocess.regex_sentence_segmentation import sentence_segmentation
from model.prediction import predict_if_shakespeare


app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.get("/process/", response_class=HTMLResponse)
async def index():
    """Show frontend."""

    with open("web/index.html") as f:
        return f.read()
    

@app.post("/process/")
async def process_text(input_data: TextInput):
    """Process user input and respond."""

    sentences = sentence_segmentation(input_data.text)
    result = predict_if_shakespeare(sentences)

    if result == 1:
        return JSONResponse(content={"processed_text": "It's Shakespeare!"})
    elif result == 0:
        return JSONResponse(content={"processed_text": "It's not Shakespeare"})
    else:
        return JSONResponse(content={"error": "No input text provided"}, status_code=400)
