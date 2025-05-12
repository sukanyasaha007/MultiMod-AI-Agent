from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from app.agent import MultiModalAgent
from app.utils import save_upload_file
import os

app = FastAPI()
agent = MultiModalAgent()

@app.post("/upload/")
async def upload_files(image: UploadFile = File(...), doc: UploadFile = File(...)):
    image_path = save_upload_file(image, "data/wildfire_images")
    doc_path = save_upload_file(doc, "data/sample_docs")
    return {"image_path": image_path, "doc_path": doc_path}

@app.post("/query/")
async def query_agent(question: str = Form(...)):
    response = agent.answer_question(question)
    return JSONResponse(content={"response": response})
