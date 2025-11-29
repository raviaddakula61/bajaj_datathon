🏥 Medical Invoice Extraction System
Powered by FastAPI + Groq LLaMA + Tesseract OCR + Streamlit

This project extracts structured JSON data from medical invoices using a hybrid pipeline:

🖼 OCR Engine (Images → Tesseract, PDFs → Poppler)

🧠 LLM Processing (Groq API – LLaMA-3 models)

🧮 Post-processing (Totals, mismatch detection, fraud flags)

💻 Frontend → Streamlit Web App

⚡ Backend → FastAPI extraction API

Designed for accuracy, speed, fraud detection, and real-world hospital bill variations.

🚀 Features

✔ Extract fields: invoice ID, dates, patient details, hospital details
✔ Extract & structure line items, amounts, unit prices, descriptions
✔ Auto-compute totals if missing
✔ Detect fraud using total mismatch checks
✔ Supports JPG / PNG / JPEG / PDF invoices
✔ Uses Groq (LLaMA-3) for highly accurate reasoning
✔ Clean JSON output
✔ Streamlit demo interface
✔ Production-ready FastAPI backend
