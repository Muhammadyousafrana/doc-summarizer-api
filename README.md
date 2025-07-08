# doc_text_summarization
## for text summarization
```sh
curl -X 'POST' \
  'https://probable-broccoli-p4wjvrgjp4j3r5g-8000.app.github.dev/summarize/text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=your Text Here'
```

## for document summarization

```sh
curl -X 'POST' \
  'https://probable-broccoli-p4wjvrgjp4j3r5g-8000.app.github.dev/summarize/file' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=your doc path here'
```
