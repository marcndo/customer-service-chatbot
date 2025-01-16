from transformers import pipeline

def load_qa_model():
    """Load a pre-train question answering model"""
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return qa_pipeline
