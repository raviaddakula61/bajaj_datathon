🧾 AI-Driven Medical Invoice Extraction System (FastAPI + Streamlit + Groq)
Bajaj Finserv Datathon – End-to-End Solution

This project is an AI-powered invoice extraction pipeline that converts medical invoices (images/PDFs) into structured JSON using:

OCR → (Tesseract for images + Poppler for PDFs)

LLM Extraction → Groq LLaMA-3 model

FastAPI Backend

Streamlit Frontend

Fraud Detection Rules

Automatic Total Validation

🚀 Architecture Overview
             ┌────────────────────────────┐
             │        Streamlit UI        │
             │  (User Uploads Invoice)    │
             └───────────────┬────────────┘
                             │
                             ▼
                 ┌─────────────────────┐
                 │      FastAPI        │
                 │  /extract endpoint  │
                 └──────────┬──────────┘
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
┌─────────────────┐                   ┌────────────────────┐
│     OCR Engine  │                   │ Groq LLaMA-3 Model │
│ Tesseract/Poppler│  → Extract Text  │  → Extract JSON     │
└─────────────────┘                   └────────────────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │ JSON Post-Processor    │
               │ (Totals, Fraud Flags)  │
               └────────────────────────┘

✨ Key Features
🔍 1. OCR Extraction

Images → Processed with Tesseract

PDFs → Converted using Poppler → OCR via Tesseract

Auto text cleanup + normalization

🤖 2. LLM-Powered Extraction (Groq LLaMA-3)

Extracts:

Invoice ID

Dates

Seller & Buyer Details

Line Items

Tax, Discounts

Printed Total vs Computed Total

⚠️ 3. Fraud Detection

Automatically flags:

total_mismatch

missing fields

suspicious price anomalies

⚙️ 4. FastAPI Backend

/extract → Accepts file → Returns structured JSON

CORS enabled

🖥️ 5. Streamlit Frontend

Simple drag-and-drop UI

Shows extracted JSON output

Clean interface for demo purposes

🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
LLM	Groq API (LLaMA-3)**
OCR (images)	Tesseract
OCR (PDFs)	Poppler
Environment	Python 3.10+
📦 Project Structure
bajaj_datathon/
│
├── main.py                  # FastAPI backend
├── app/
│   ├── ocr.py               # OCR: images + PDFs
│   ├── llm.py               # Groq LLM Extraction
│   ├── prompts.py           # Invoice extraction prompt
│   ├── postprocess.py       # Totals, fraud detection
│
├── frontend/
│   └── app.py               # Streamlit UI
│
├── requirements.txt
└── README.md

🔑 Environment Variables

Create a .env file (DO NOT COMMIT IT):

GROQ_API_KEY=your_key_here
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
POPPLER_PATH=C:\poppler\Library\bin

▶️ Run the Backend (FastAPI)
uvicorn main:app --reload


API URL:
👉 http://127.0.0.1:8000/docs

▶️ Run the Frontend (Streamlit)
streamlit run frontend/app.py


UI URL:
👉 http://localhost:8501

🧪 Sample Output JSON
{
  "invoice_id": "CR33504",
  "invoice_date": "13-Jan-2013",
  "seller_details": { ... },
  "buyer_details": { ... },
  "line_items": [
      {"description": "ROOM RENT", "quantity": 1, "unit_price": 4000, "amount": 4000},
      {"description": "PHARMACY", "amount": 2765.54}
  ],
  "sub_total": 15143.54,
  "final_total": 15143.54,
  "printed_total": 14343.54,
  "fraud_flags": ["total_mismatch"]
}

🧠 Model Prompt (LLM Extraction Logic)

Located in app/prompts.py
Includes rules for:

Normalizing totals

Handling missing data

Fraud detection

Strict JSON enforcement

🧩 Differentiators (Important for Datathon Pitch)
1️⃣ Hybrid OCR + LLM Pipeline

Combines classical OCR + AI extraction → high accuracy.

2️⃣ Fraud Detection Module

Compares printed vs computed totals → flags anomalies.

3️⃣ PDF + Image Support

Supports JPG/PNG/PDF of any quality.

4️⃣ Lightweight + Fast (Groq API)

Uses LLaMA-3 accelerated on Groq → extremely fast inference.

5️⃣ Production-ready APIs

FastAPI conforms to modern REST standards.

📊 Pitch Deck Included

A ready-made architecture pitch deck is provided in:

/pitch_deck/pitch.pdf


Includes:

System Overview

Diagram

Model Stack

Differentiators

Future Enhancements

📘 Future Improvements

Add NER fine-tuning

Support multi-page invoices

Add database storage & analytics

Build web dashboard

🤝 Contributors

A. Ravi Teja (IIT Bhubaneswar)
Project for Bajaj Finserv Datathon 2025
