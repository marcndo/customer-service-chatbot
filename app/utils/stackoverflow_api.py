import requests
import pandas as pd
from dotenv import load_dotenv
import os
import time
import json

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv('STACK_OVERFLOW_API_KEY')

# Base URL for Stack Overflow API
BASE_URL_QUESTIONS = 'https://api.stackexchange.com/2.3/questions'
BASE_URL_ANSWERS = 'https://api.stackexchange.com/2.3/questions/{}/answers'

# Parameters for the API call
params_questions = {
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'python',  # You can change this to other tags
    'site': 'stackoverflow',
    'key': API_KEY,
    'pagesize': 100  # Number of questions to fetch per page
}

# Resume state files
QUESTIONS_CSV = 'stackoverflow_questions_with_answers.csv'
STATE_FILE = 'stackoverflow_state.json'

# Function to fetch answers for each question
def fetch_answers_for_question(question_id):
    answers_url = BASE_URL_ANSWERS.format(question_id)
    params_answers = {
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'key': API_KEY,
        'filter': 'withbody'  # Get the full body of the answers
    }

    response = requests.get(answers_url, params=params_answers)
    if response.status_code == 200:
        data = response.json()
        answers = [answer['body'] for answer in data.get('items', [])]
        return answers
    else:
        print(f"Error fetching answers for question {question_id}: {response.status_code}")
        return []

# Function to load state from files
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)
            return state.get('page', 1), state.get('current_count', 0)
    return 1, 0

# Function to save state to file
def save_state(page, current_count):
    state = {'page': page, 'current_count': current_count}
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

# Load progress if the file exists
if os.path.exists(QUESTIONS_CSV):
    all_questions = pd.read_csv(QUESTIONS_CSV).to_dict('records')
else:
    all_questions = []

# Load state for page and count
page, current_count = load_state()

# Total number of questions you want to collect
target_count = 10300

# Start collecting data
while current_count < target_count:
    params_questions['page'] = page

    # Fetch data from Stack Overflow API for questions
    response = requests.get(BASE_URL_QUESTIONS, params=params_questions)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Check if 'items' exist in the response
        if 'items' in data and len(data['items']) > 0:
            for item in data['items']:
                # Fetch the answers for the current question
                answers = fetch_answers_for_question(item['question_id'])

                # Extract relevant fields from each item
                all_questions.append({
                    'question_id': item['question_id'],
                    'title': item['title'],
                    'tags': ', '.join(item['tags']),
                    'link': item['link'],
                    'creation_date': item['creation_date'],
                    'is_answered': item['is_answered'],
                    'view_count': item['view_count'],
                    'answer_count': item['answer_count'],
                    'score': item['score'],
                    'answers': '\n'.join(answers)  # Add answers as a new column (concatenated if multiple answers)
                })

            # Update the count of collected questions
            current_count += len(data['items'])
            print(f"Collected {current_count} questions...")

            # Save progress to CSV
            pd.DataFrame(all_questions).to_csv(QUESTIONS_CSV, index=False)

            # Save current state
            save_state(page, current_count)

            # Increase the page number for the next request
            page += 1
        else:
            print("No more questions found.")
            break
    else:
        print(f"Error: {response.status_code}. Retrying in 10 seconds...")
        time.sleep(10)
        continue

    # Pause for a second to avoid hitting the API rate limit
    time.sleep(1)

print(f"Data collection complete. Saved to {QUESTIONS_CSV}.")
