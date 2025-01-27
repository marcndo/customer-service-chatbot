# Customer Service Chatbot Project

Welcome to the Customer Service Chatbot Project! This repository showcases a complete pipeline for building and deploying an intelligent question-answering (QA) system. The chatbot leverages a fine-tuned Large Language Model (LLM) on a custom dataset from StackOverflow, providing accurate and context-aware responses to user queries. Designed as a modular and extensible solution, this project demonstrates best practices in NLP, data preprocessing, model fine-tuning, and API development.


## Table of Contents.
 * [Introduction](#Introduction)
 * [Features](#Features)
 * [Architecture](#Architecture)
 * [Setup Instructions](#Setup-Instructions)
 * [Usage](#Usage)
 * [Dataset](#Dataset)
 * [Model](#Model)
 * [API Endpoints](#API-Endpoints)
 * [Project Structure](#Project-Structure)
 * [Future Enhancements](#Future-Enhancements)
 * [Contact](#Contact)

   
## Introduction.
This project serves as an end-to-end example of how to build a conversational chatbot that:
1. Processes user queries using Natural Language Processing (NLP) techniques.
2. Fetches relevant answers from a fine-tuned LLM model.
3. Delivers results via a RESTful API.

   
## Objectives
* Demonstrate the application of machine learning techniques in real-world problem-solving.
* Showcase technical skills in NLP, LLM fine-tuning, and API development.
* Provide a portfolio project that highlights expertise in modern AI technologies.


## Features
### Custom Fine-Tuned Model: 
Fine-tuned BERT-based model on StackOverflow QA data.

### Preprocessing Utilities: 
 Includes tokenization, dataset cleaning, and named entity recognition (NER).
 
 ### RESTful API: 
 Simple and efficient Flask-based API for interacting with the chatbot.
 
 ### Extensible Framework:
 Modular design for easy integration of additional features.
 
 ### Automated Tests:
  Unit tests for API routes to ensure code quality and robustness.
  
## Architecture
The architecture follows a modular and layered design:
1. Data Preprocessing Layer:
   * Cleans and tokenizes the StackOverflow dataset.
   * Generates embeddings for efficient text processing.
2. Model Layer:
   * Uses Hugging Face's Transformers library for LLM fine-tuning.
   * Includes spaCy for optional Named Entity Recognition (NER).
## API Layer:
 * Implements a Flask API for user interaction.
 * Includes endpoints for asking questions and retrieving answers.
   
## Setup Instructions
### Prerequisites
Ensure you have the following installed:
 * Python 3.8+
 * pip
 * virtualenv
1. Clone the repository:
   ```bash
    git clone https://github.com/marcndo/customer-service-chatbot.git
    cd customer-service-chatbot
3. Create a virtual environment and activate it:
   ```bash
    virtualenv venv
    venv/bin/activate  # On Windows: venv\Scripts\activate
4. Install dependencies:
   ```bash
    pip install -r requirements.txt
5. Download and preprocess the dataset:
Place the StackOverflow QA dataset in utils/stackoverflow_qa.csv and run:
```python utils/data_loader.py```
6. Fine-tune the model:
   ```bash
   python app/bert_model.py
   ```
8. Run the API:

```bash
python run.py
```

## Usage
Once the API is running, you can interact with the chatbot via the provided endpoints.

Example Query
Send a POST request to /api/ask with a JSON body:

```bash
{
  "question": "How do I install Python packages?"
}
```
The chatbot will respond with a JSON object containing the answer.


## Dataset
The project uses a curated StackOverflow QA dataset. This dataset includes pairs of questions and answers that have been cleaned and preprocessed to optimize model training.

### Preprocessing Steps.
 1. Remove duplicates and irrelevant entries.
 2. Tokenize text using Hugging Face and spaCy tokenizers.
 3. Save the cleaned data to utils/stackoverflow_qa.csv.

    
## Model
### Fine-Tuning
The fine-tuning process uses a pre-trained BERT model and adapts it to the StackOverflow dataset for domain-specific QA tasks.

### Key Libraries
 * Hugging Face Transformers.
 * PyTorch.
 * spaCy (for NER)
   
## API Endpoints
| Endpoint        | Method | Description                         |
|-----------------|--------|-------------------------------------|
| /api/ask        | POST   | Submit a question for an answer    |
| /api/health     | GET    | Check API health status            |
-----------------------------------------------------------------


## Future Enhancements
1. Integrate a frontend interface for improved user experience.
2. Add support for multilingual QA.
3. Implement real-time feedback loops to improve model performance.
4. Explore other transformer models like GPT for enhanced conversational capabilities.

## Contact.
 * Feel free to reach out if you have any questions or suggestions:
 * Email: ndowahmarcel@gmail.com.
 * [LinkedIn](https://www.linkedin.com/in/marcelndowah/)
*Thank you for exploring this project. I hope it demonstrates my skills and passion for AI and NLP development!
