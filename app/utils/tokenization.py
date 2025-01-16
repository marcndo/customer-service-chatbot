def tokenize_text(tokenizer, text):
    return tokenizer(text, return_tensors='pt')