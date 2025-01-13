from flask import Blueprint, request, jsonify
from app.models.bert_model import load_bert_model
from app.utils.tokenization import tokenize_text

from app.models.spacy_model import load_spacy_model
from app.utils.ner import extract_entities

main = Blueprint('main', __name__)
tokenizer, model = load_bert_model()

@main.route('/classify', methods=['POST'])
def classify():
    text = request.json.get('text')
    inputs = tokenize_text(tokenizer, text)
    outputs = model(**inputs)
    classification = outputs.logits.argmax().item()
    return jsonify({'classification': classification})

nlp = load_spacy_model()

@main.route('/ner', methods=['POST'])
def ner():
    text = request.json.get('text')
    entities = extract_entities(nlp, text)
    return jsonify({'entities': entities})