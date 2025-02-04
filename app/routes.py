from flask import Blueprint, request, jsonify
from app.models.bert_model import load_bert_model
from app.utils.tokenization import tokenize_text

from app.models.spacy_model import load_spacy_model
from app.utils.ner import extract_entities

from app.models.qa_model import load_qa_model
from app.utils.qa import answer_question

from app import create_app

main = Blueprint('main', __name__)
tokenizer, model = load_bert_model()

app = create_app()

# Home page route
@app.route('/')
def home():
    return "Welcome to the Customer Service Chatbot API!"

# Classifier route
@main.route('/classify', methods=['POST'])
def classify():
    text = request.json.get('text')
    inputs = tokenize_text(tokenizer, text)
    outputs = model(**inputs)
    classification = outputs.logits.argmax().item()
    return jsonify({'classification': classification})

nlp = load_spacy_model()

# Route name entity recognition
@main.route('/ner', methods=['POST'])
def ner():
    text = request.json.get('text')
    entities = extract_entities(nlp, text)
    return jsonify({'entities': entities})

# QA route
qa_pipeline = load_qa_model()
@main.route('/qa', methods=['POST'])
def qa():
    """
    Endpoint for question answering.
    Expects JSON input:
    {
        "question": "What is the capital of France?",
        "context": "France is a country in Europe. Its capital is Paris."
    }
    """
    data = request.json
    question = data.get("question")
    context = data.get("context")

    if not question or not context:
        return jsonify({"error": "Both 'question' and 'context' are required"}), 400

    result = answer_question(qa_pipeline, question, context)
    return jsonify(result)
