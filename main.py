from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from app.ocr import extract_text
from app.llm import call_groq
from app.postprocess import validate_totals

app = FastAPI(title="Bajaj Datathon API")

# -------------------------------
# CORS Settings
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # allow all frontend clients
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Health Check
# -------------------------------
@app.get("/")
def root():
    return {"status": "FastAPI running with ChatGroq!"}

# -------------------------------
# Webhook Endpoint (Use This)
# -------------------------------
@app.post("/webhook")
async def webhook_receiver(request: Request):
    """
    This endpoint receives POST events from external services
    (Bajaj Datathon will call this URL).
    """
    data = await request.json()
    print("Webhook Received:", data)

    return {
        "status": "Webhook received successfully",
        "received_data": data
    }

# -------------------------------
# Extract Invoice Endpoint
# -------------------------------
@app.post("/extract")
async def extract_bill(file: UploadFile = File(...)):
    """
    Upload invoice image → OCR → LLM → post-processing.
    """
    try:
        image_bytes = await file.read()
        text = extract_text(image_bytes, file.content_type)

        raw_output = call_groq(text)
        final_output = validate_totals(raw_output)

        return {"status": "success", "data": final_output}

    except Exception as e:
        return {"status": "error", "message": str(e)}
