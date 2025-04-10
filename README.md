# doc_text_summarization
## for text summarization
```sh
curl -X 'POST' \
  'https://probable-broccoli-p4wjvrgjp4j3r5g-8000.app.github.dev/summarize/text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=As%20undesireable%20as%20it%20might%20be%2C%20more%20often%20than%20not%20there%20is%20extremely%20useful%20information%20embedded%20in%20Word%20documents%2C%20PowerPoint%20presentations%2C%20PDFs%2C%20etc%E2%80%94so-called%20%E2%80%9Cdark%20data%E2%80%9D%E2%80%94that%20would%20be%20valuable%20for%20further%20textual%20analysis%20and%20visualization.%20While%20several%20packages%20exist%20for%20extracting%20content%20from%20each%20of%20these%20formats%20on%20their%20own%2C%20this%20package%20provides%20a%20single%20interface%20for%20extracting%20content%20from%20any%20type%20of%20file%2C%20without%20any%20irrelevant%20markup.'
```

## for document summarization

```sh
curl -X 'POST' \
  'https://probable-broccoli-p4wjvrgjp4j3r5g-8000.app.github.dev/summarize/file' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@Lecture Agenda Entrepeneurship and Leadership  21 SE Lecture 5 Financial Viability  Feb19, 2025 Dr. M Rizwan.docx;type=application/vnd.openxmlformats-officedocument.wordprocessingml.document'
```