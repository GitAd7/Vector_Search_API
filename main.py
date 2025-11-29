from fastapi import FastAPI
from app.models import AnalyzeRequest, SummarizeRequest, SearchRequest
from app.nlp_utils import analyze_text, summarize_text
from app.vector_store import vectorStore

app = FastAPI(
    title="NLP and Vector Search API",
    description="An API for text analysis, summarization, and vector-based search using FastAPI.",
    version="1.0.0"
)

# Initialize the vector store
vector_store = vectorStore()

@app.post("/analyze", summary="Analyze Text", description="Analyze the sentiment and extract keywords from the provided text.")
def analyze(request: AnalyzeRequest):
    result = analyze_text(request.text)
    return result

@app.post("/summarize", summary="Summarize Text", description="Generate a summary for the provided text.")
def summarize(request: SummarizeRequest):
    result = summarize_text(request.text)
    return result

@app.post("/search", summary="Vector Search", description="Search for similar texts in the vector store based on the provided query.")
def search(request: SearchRequest): 
    results = vector_store.search(request.text)
    return {"results": results}

@app.get("health", summary="Health Check", description="Check the health status of the API.")
def health_check():
    return {"status": "API is running smoothly."}