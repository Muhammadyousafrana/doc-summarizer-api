from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from google.generativeai import GenerativeModel
import google.generativeai as genai
import os
from my_lib.summary import extract_text_with_textract, summarize_text

# Initialize FastAPI
app = FastAPI(title="Universal Text & Document Summarizer")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://summarization-app.streamlit.app"],  # Replace "*" with ["https://yourfrontend.com"] for production
    allow_credentials=True,
    allow_methods=["https://summarization-app.streamlit.app"],
    allow_headers=["https://summarization-app.streamlit.app/"],
)

# ✅ Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDAju0CDpdBD4eUx_JjQyCpAi8DwDRYWH8")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=GEMINI_API_KEY)
model = GenerativeModel("gemma-3-12b-it")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": (
            "Welcome to the Summarization API. "
            "Use /summarize/text to summarize text, and /summarize/file to summarize uploaded documents."
        )
    }

# 🧾 Text Summarization Endpoint
@app.post("/summarize/text")
async def summarize_plain_text(text: str = Form(...)):
    summary = summarize_text(text, model)
    return JSONResponse(content={"summary": summary})

# 📎 File Upload + Summarization Endpoint
@app.post("/summarize/file")
async def summarize_file(file: UploadFile = File(...)):
    content = extract_text_with_textract(file)
    if not content.strip():
        raise HTTPException(status_code=400, detail="Empty or unreadable document.")
    summary = summarize_text(content, model)
    return JSONResponse(content={"summary": summary})

# 💬 Chat About Summary Endpoint
@app.post("/chat")
async def chat_about_summary(
    summary: str = Form(...),
    question: str = Form(...)
):
    prompt = (
        f"You are a helpful assistant. Below is a summary, followed by user input.\n\n"
        f"Summary:\n{summary}\n\n"
        f"User Input:\n{question}\n\n"
        f"Determine whether the user is asking a question about the summary or giving feedback to improve it.\n"
        f"If it's a question, answer it clearly using information from the summary.\n"
        f"If it's feedback (like 'make it better'), rewrite the summary with a bit more detail.\n"
        f"Important: DO NOT explain your reasoning or comment on the user's input. Only provide the answer or the improved summary directly."
    )
    response = model.generate_content(prompt)
    return JSONResponse(content={"response": response.text})

# 🌍 Translation Endpoint
@app.post("/translate")
async def translate_text(
    text: str = Form(...),
    target_language: str = Form(...)
):
    prompt = (
        f"Translate the following text into {target_language}:\n\n"
        f"Text:\n{text}\n\n"
        f"Only return the translated text, without explanation or comments."
    )
    try:
        response = model.generate_content(prompt)
        return JSONResponse(content=response.text.strip())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during translation: {str(e)}")
