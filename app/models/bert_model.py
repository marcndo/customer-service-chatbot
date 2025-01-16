from transformers import BertTokenizer, BertForSequenceClassification

def load_bert_model():
    tokenization = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    return tokenization, model