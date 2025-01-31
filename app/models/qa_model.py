# from transformers import pipeline

# def load_qa_model():
#     """Load a pre-train question answering model"""
#     qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
#     return qa_pipeline
from transformers import BertForQuestionAnswering, Trainer, TrainingArguments
import torch

def fine_tune_model(train_dataset, eval_dataset, model_name="bert-base-uncased"):
    model = BertForQuestionAnswering.from_pretrained(model_name)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',          # output directory
        num_train_epochs=3,              # number of training epochs
        per_device_train_batch_size=8,   # batch size for training
        per_device_eval_batch_size=8,    # batch size for evaluation
        warmup_steps=500,                # number of warmup steps for learning rate scheduler
        weight_decay=0.01,               # strength of weight decay
        logging_dir='./logs',            # directory for storing logs
    )

    trainer = Trainer(
        model=model,                         # the instantiated 🤗 Transformers model to be trained
        args=training_args,                  # training arguments, defined above
        train_dataset=train_dataset,         # training dataset
        eval_dataset=eval_dataset            # evaluation dataset
    )

    trainer.train()
    model.save_pretrained("./models/my_trained_model")
    return model
