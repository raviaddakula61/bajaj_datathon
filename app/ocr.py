import io
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract

# 🔥 ADD THIS
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


POPLER_PATH = r"C:\Users\user\Documents\datathon\Release-25.11.0-0\poppler-25.11.0\Library\bin"

def extract_text(file_bytes, content_type):
    text = ""

    # ----- PDF Handling -----
    if content_type == "application/pdf":
        try:
            pages = convert_from_bytes(
                file_bytes,
                poppler_path=POPLER_PATH
            )
        except Exception as e:
            raise RuntimeError(f"PDF conversion failed: {e}")

        for page in pages:
            text += pytesseract.image_to_string(page)

        return text

    # ----- Image Handling -----
    try:
        image = Image.open(io.BytesIO(file_bytes))
        return pytesseract.image_to_string(image)
    except Exception as e:
        raise RuntimeError(f"Image reading failed: {e}")