Text Intelligence API
FastAPI - NLP - Transformers - Docker

This project is a fully functional AI-powered text intelligence API built using FastAPI, SpaCy, and HuggingFace Transformers.
It provides:

-> Sentiment Analysis

-> Keyword Extraction

-> Text Summarization (BART)

-> Entity Recognition

-> Text Cleaning

-> Language Detection

-> Dockerized deployment

-> Auto-generated Swagger Docs


This assignment demonstrates skills in ML model integration, FastAPI backend design, NLP pipelines, and containerized deployment.

Project Structure
text_intelligence_api/
│── app/
│   ├── main.py               # Main FastAPI application
│   ├── models.py             # Pydantic request/response models
│   ├── utils.py              # NLP utilities (summarizer, sentiment, entities)
│   ├── requirements.txt      # Dependencies
│   └── __init__.py
│
│── Dockerfile                # Containerization file
│── README.md                 # Documentation

Features
1. /analyze — Sentiment + Keywords

Uses DistilBERT for sentiment

Uses SpaCy for NLP keyword extraction

2. /summarize — Text Summarization

Uses facebook/bart-large-cnn for high-quality summarization

3. /entities — Named Entity Recognition

Uses SpaCy’s en_core_web_sm model

4. /clean — Text Preprocessing

Lowercasing

Removing special characters

Stripping whitespace

5. Swagger UI

Auto-generated documentation available at:
➡️ http://127.0.0.1:8000/docs

🛠️ Local Installation (Without Docker)
1. Clone the repository
git clone https://github.com/<your-username>/text_intelligence_api.git
cd text_intelligence_api

2. Create Virtual Environment
python -m venv txtapienv # With Python
conda activate txtapienv # With conda (I prefer)


Activate:

Windows:

txtapienv\Scripts\activate


Mac/Linux:

source txtapienv/bin/activate

3. Install Dependencies
pip install -r app/requirements.txt
python -m spacy download en_core_web_sm

4. Start the Server
uvicorn app.main:app --reload

🐳 Running With Docker (Recommended)
1. Build Docker Image
docker build -t text-intel-api .

2. Run the Container
docker run -p 8000:8000 text-intel-api


Your API is now live at:

http://localhost:8000/
http://127.0.0.1:8000/docs