# DocSummarizer API

A lightweight FastAPI service for summarizing plain text and uploaded documents using Gemini.

## Why this project name?

The repository currently uses a generic name (`doc_text_summarization`) that is functional but not very polished. A cleaner and more professional name is:

- `doc-summarizer-api`

This name is:
- clear and searchable
- aligned with the app's purpose
- cleaner for GitHub and deployment platforms

## Features

- Summarize plain text
- Summarize uploaded documents (PDF, DOCX, TXT, and similar supported formats via `textract`)
- Chat about a summary
- Translate text into another language

## Tech stack

- Python
- FastAPI
- Google Generative AI (Gemini)
- `textract` for document parsing

## Project structure

```text
.
├── main.py
├── my_lib/
│   └── summary.py
├── requirements.txt
├── Dockerfile
├── heroku.yml
├── README.md
├── LICENSE
└── .gitignore
```

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set your Gemini API key

```bash
export GEMINI_API_KEY="your_api_key_here"
```

5. Run the app

```bash
uvicorn main:app --reload
```

The app will be available at:

```text
http://localhost:8000
```

## API endpoints

### 1) Summarize text

```bash
curl -X POST "http://localhost:8000/summarize/text" \
  -H "accept: application/json" \
  -F "text=Your long text here..."
```

Response example:

```json
{
  "summary": "This text discusses..."
}
```

### 2) Summarize uploaded file

```bash
curl -X POST "http://localhost:8000/summarize/file" \
  -H "accept: application/json" \
  -F "file=@/path/to/document.pdf"
```

Response example:

```json
{
  "summary": "The document explains..."
}
```

### 3) Chat about a summary

```bash
curl -X POST "http://localhost:8000/chat" \
  -F "summary=Short summary text" \
  -F "question=Can you make it shorter?"
```

### 4) Translate text

```bash
curl -X POST "http://localhost:8000/translate" \
  -F "text=Hello world" \
  -F "target_language=French"
```

## Environment variables

```bash
GEMINI_API_KEY=your_gemini_api_key
```

## Notes

This repository is a working prototype/demo and is not completely production-hardened. The core functionality works, but some areas should be improved before using it in production.

## Is the code obsolete?

The code is not obsolete in the sense that it still works as a demo API, but it is not production-ready as-is.

Main concerns:
- The API key is hardcoded in `main.py` instead of being secured via environment variables only.
- CORS is configured incorrectly and uses a specific app URL instead of a proper list of allowed origins.
- The app is tightly coupled to one model and model configuration.
- `textract` may require system dependencies and can be fragile in some environments.
- Error handling and validation should be strengthened for production use.

In short:
- Functional: Yes
- Production-ready: Not yet
- Obsolete: No

## Recommended next improvements

- Remove hardcoded secret values
- Use environment-driven CORS configuration
- Add input validation and robust error handling
- Add tests
- Use a more standard document extraction flow for deployment environments
- Add proper logging and health checks

## License

This project is licensed under the MIT License.
