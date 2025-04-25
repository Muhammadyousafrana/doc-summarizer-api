from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from google.generativeai import GenerativeModel
import google.generativeai as genai
import os
from my_lib.summary import extract_text_with_textract, summarize_text

app = FastAPI(title="Universal Text & Document Summarizer")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDAju0CDpdBD4eUx_JjQyCpAi8DwDRYWH8")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=GEMINI_API_KEY)
model = GenerativeModel("learnlm-1.5-pro-experimental")

@app.get("/")
async def root():
    return {"message": "Welcome to the Summarization API. Use /summarize/text to summarize text. and use /summarize/file to summarize the file"}


@app.post("/summarize/text")
async def summarize_plain_text(text: str = Form(...)):
    summary = summarize_text(text, model)
    return JSONResponse(content={"summary": summary})

@app.post("/summarize/file")
async def summarize_file(file: UploadFile = File(...)):
    content = extract_text_with_textract(file)
    if not content.strip():
        raise HTTPException(status_code=400, detail="Empty or unreadable document.")
    summary = summarize_text(content, model)
    return JSONResponse(content={"summary": summary})

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
