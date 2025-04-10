
import tempfile
import textract
from fastapi import UploadFile, HTTPException
from google.generativeai import GenerativeModel

def extract_text_with_textract(file: UploadFile) -> str:
    try:
        with tempfile.NamedTemporaryFile(delete=True, suffix=f"_{file.filename}") as temp_file:
            temp_file.write(file.file.read())
            temp_file.flush()
            text_bytes = textract.process(temp_file.name)
            return text_bytes.decode("utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text extraction failed: {str(e)}")

def summarize_text(text: str, model: GenerativeModel) -> str:
    prompt = f"Summarize the following content:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gem summarization error: {str(e)}")
