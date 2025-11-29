import streamlit as st
import requests
import json

FASTAPI_URL = "http://127.0.0.1:8000/extract"

st.set_page_config(page_title="Medical Invoice Extractor", layout="centered")

# ---------------------------- UI HEADER ----------------------------
st.title("🏥 Medical Invoice Extractor")
st.markdown(
    """
    Upload a medical invoice or hospital bill and extract **structured JSON data**  
    using OCR + Groq LLM-powered backend.
    """
)

st.divider()

# -------------------------- FILE UPLOADER ---------------------------
uploaded_file = st.file_uploader(
    "📤 Upload invoice image or PDF",
    type=["png", "jpg", "jpeg", "pdf"],
    help="Supported formats: PNG, JPG, JPEG, PDF"
)

# ---------------------------- EXTRACT BUTTON ----------------------------
if st.button("🔍 Extract Invoice Data"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a file first.")
    else:
        with st.spinner("⏳ Extracting... Please wait..."):

            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }

            try:
                response = requests.post(FASTAPI_URL, files=files, timeout=120)

                # Try to decode JSON
                try:
                    data = response.json()
                except:
                    st.error("❌ Server returned invalid JSON.")
                    st.code(response.text)
                    st.stop()

                # Show output nicely
                st.success("✅ Extraction Completed Successfully!")
                st.subheader("📦 Extracted JSON Output")
                st.json(data)

            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to FastAPI server. Is it running?")
            except Exception as e:
                st.error(f"⚠️ Unexpected Error: {str(e)}")

st.divider()

st.markdown(
    """
    💡 *Tip:* Keep invoices clear & well-lit for best OCR accuracy.
    """
)
