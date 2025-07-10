from transformers import pipeline

summarizer = pipeline("summarization", model="google/flan-t5-base")

def summarize_text(text):
    return summarizer(text[:1000])[0]['summary_text']
