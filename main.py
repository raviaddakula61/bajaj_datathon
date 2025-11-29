from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.ocr import extract_text
from app.llm import call_groq
from app.postprocess import validate_totals

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "FastAPI running with ChatGroq!"}

@app.post("/extract")
async def extract_bill(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = extract_text(image_bytes, file.content_type)

    raw_output = call_groq(text)
    final_output = validate_totals(raw_output)

    return final_output
