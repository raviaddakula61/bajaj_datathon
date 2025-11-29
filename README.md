AI-Driven Medical Invoice Extraction (FastAPI + Streamlit + Groq)

This repository contains an end-to-end system for extracting structured data from medical invoices using a combination of:

OCR (Tesseract + Poppler)

LLM (Groq LLaMA-3)

FastAPI backend

Streamlit frontend

Fraud detection rules

Automatic total validation

🔥 Features
1. OCR Extraction

Image support → Tesseract

PDF support → Poppler + Tesseract

Automatic text cleanup

2. LLM-Based Extraction (Groq LLaMA-3)

Extracts:

Invoice ID

Dates

Seller & Buyer details

Line items

Taxes, discounts

Totals + printed totals

3. Fraud Detection

Flags:

Computed total ≠ printed total

Missing fields

Suspicious items

4. FastAPI Backend

A clean REST API:
POST /extract → returns JSON.

5. Streamlit UI

Beautiful drag-and-drop interface for demo.

🧱 Architecture Overview
Streamlit UI  →  FastAPI Backend  →  OCR  →  Groq LLaMA-3 → Post-processor → JSON output

📁 Project Structure
bajaj_datathon/
│
├── main.py                 # FastAPI backend
│
├── app/
│   ├── ocr.py              # Tesseract + Poppler OCR
│   ├── llm.py              # Groq LLM extraction
│   ├── prompts.py          # JSON extraction prompt
│   ├── postprocess.py      # Total validation + fraud checks
│
├── frontend/
│   └── app.py              # Streamlit UI
│
├── requirements.txt
└── README.md

🔑 Environment Variables

Create .env inside project root (DO NOT PUSH IT):

GROQ_API_KEY=your_groq_api_key
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
POPPLER_PATH=C:\poppler\Library\bin

▶️ Running Backend (FastAPI)
uvicorn main:app --reload


Open API docs:
http://127.0.0.1:8000/docs

▶️ Running Frontend (Streamlit)
streamlit run frontend/app.py


UI opens at:
http://localhost:8501

📌 Sample JSON Output
{
  "invoice_id": "CR33504",
  "invoice_date": "13-Jan-2013",
  "seller_details": { ... },
  "buyer_details": { ... },
  "line_items": [
    {"description": "ROOM RENT", "amount": 4000},
    {"description": "PHARMACY", "amount": 2765.54}
  ],
  "sub_total": 15143.54,
  "final_total": 15143.54,
  "printed_total": 14343.54,
  "fraud_flags": ["total_mismatch"]
}

🧠 Model Prompt (LLM Extraction Logic)

Located in app/prompts.py.
Includes:

Rule-based constraints

Strict JSON formatting

Fraud detection logic

⭐ Differentiators (For Datathon Pitch)

Hybrid OCR + LLM pipeline

Automated fraud detection

Full PDF + Image support

Ultra-fast inference (Groq accelerators)

Production-grade API design

Clean frontend for demo
