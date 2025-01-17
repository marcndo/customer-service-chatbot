# import requests
# import pandas as pd
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from environment variables
# API_KEY = os.getenv('STACK_OVERFLOW_API_KEY')

# # Base URL for Stack Overflow API
# BASE_URL = 'https://api.stackexchange.com/2.3/questions'

# # Parameters for the API call
# params = {
#     'order': 'desc',
#     'sort': 'activity',
#     # Change the tag or remove it
#     'tagged': 'python',  # Use a more common tag like 'python' or remove it
#     'site': 'stackoverflow',
#     'key': API_KEY,
#     'pagesize': 100  # Number of questions to fetch
# }

# # Fetch data from Stack Overflow API
# response = requests.get(BASE_URL, params=params)

# # Check if the request was successful
# if response.status_code == 200:
#     # Print the raw JSON data for debugging
#     data = response.json()
#     print("API Response:", data)  # Check the raw response
    
#     if 'items' in data and len(data['items']) > 0:
#         questions = []
#         for item in data['items']:
#             questions.append({
#                 'question_id': item['question_id'],
#                 'title': item['title'],
#                 'link': item['link'],
#                 'creation_date': item['creation_date'],
#                 'score': item['score'],
#                 'tags': ', '.join(item['tags'])
#             })
        
#         # Convert the data into a DataFrame and save it as CSV
#         df = pd.DataFrame(questions)
#         df.to_csv('stackoverflow_questions.csv', index=False)
#         print("Data saved to stackoverflow_questions.csv")
#     else:
#         print("No items found in the response.")
# else:
#     print(f"Error: {response.status_code}")

# import requests
# import pandas as pd
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from environment variables
# API_KEY = os.getenv('STACK_OVERFLOW_API_KEY')

# # Base URL for Stack Overflow API
# BASE_URL = 'https://api.stackexchange.com/2.3/questions'

# # Parameters for the API call
# params = {
#     'order': 'desc',
#     'sort': 'activity',
#     'tagged': 'python',  # You can change this to other tags
#     'site': 'stackoverflow',
#     'key': API_KEY,
#     'pagesize': 100  # Number of questions to fetch
# }

# # Fetch data from Stack Overflow API
# response = requests.get(BASE_URL, params=params)

# if response.status_code == 200:
#     # Parse JSON response
#     data = response.json()
#     print("API Response:", data)  # Optional: Print raw response for debugging

#     if 'items' in data and len(data['items']) > 0:
#         # Extract relevant fields from each item
#         questions = []
#         for item in data['items']:
#             questions.append({
#                 'question_id': item['question_id'],
#                 'title': item['title'],
#                 'tags': ', '.join(item['tags']),
#                 'link': item['link'],
#                 'creation_date': item['creation_date'],
#                 'is_answered': item['is_answered'],
#                 'view_count': item['view_count'],
#                 'answer_count': item['answer_count'],
#                 'score': item['score']
#             })

#         # Convert the data into a DataFrame
#         df = pd.DataFrame(questions)

#         # Save the data to a CSV file
#         csv_filename = 'stackoverflow_questions.csv'
#         df.to_csv(csv_filename, index=False)

#         print(f"Data successfully saved to {csv_filename}")
#     else:
#         print("No items found in the response.")
# else:
#     print(f"Error: {response.status_code}")
# import requests
# import pandas as pd
# from dotenv import load_dotenv
# import os
# import time

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from environment variables
# API_KEY = os.getenv('STACK_OVERFLOW_API_KEY')

# # Base URL for Stack Overflow API
# BASE_URL = 'https://api.stackexchange.com/2.3/questions'

# # Parameters for the API call
# params = {
#     'order': 'desc',
#     'sort': 'activity',
#     'tagged': 'python',  # You can change this to other tags
#     'site': 'stackoverflow',
#     'key': API_KEY,
#     'pagesize': 100  # Number of questions to fetch per page
# }

# # List to store all the questions
# all_questions = []

# # Total number of questions you want to collect
# target_count = 10300
# current_count = 0
# page = 1

# while current_count < target_count:
#     # Update the page number in the parameters
#     params['page'] = page
    
#     # Fetch data from Stack Overflow API
#     response = requests.get(BASE_URL, params=params)
    
#     if response.status_code == 200:
#         # Parse JSON response
#         data = response.json()

#         # Check if 'items' exist in the response
#         if 'items' in data and len(data['items']) > 0:
#             for item in data['items']:
#                 # Extract relevant fields from each item
#                 all_questions.append({
#                     'question_id': item['question_id'],
#                     'title': item['title'],
#                     'tags': ', '.join(item['tags']),
#                     'link': item['link'],
#                     'creation_date': item['creation_date'],
#                     'is_answered': item['is_answered'],
#                     'view_count': item['view_count'],
#                     'answer_count': item['answer_count'],
#                     'score': item['score']
#                 })
            
#             # Update the count of collected questions
#             current_count += len(data['items'])
#             print(f"Collected {current_count} questions...")

#             # Increase the page number for the next request
#             page += 1
#         else:
#             # No items found, exit the loop
#             print("No more questions found.")
#             break
#     else:
#         print(f"Error: {response.status_code}")
#         break

#     # Pause for a second to avoid hitting the API rate limit
#     time.sleep(1)

# # Convert the data into a DataFrame
# df = pd.DataFrame(all_questions)

# # Save the data to a CSV file
# csv_filename = 'stackoverflow_questions_50k.csv'
# df.to_csv(csv_filename, index=False)

# print(f"Data successfully saved to {csv_filename} with {len(df)} entries.")

import requests
import pandas as pd
from dotenv import load_dotenv
import os
import time

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

# List to store all the questions
all_questions = []

# Total number of questions you want to collect
target_count = 10300
current_count = 0
page = 1

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

while current_count < target_count:
    # Update the page number in the parameters
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

            # Increase the page number for the next request
            page += 1
        else:
            # No items found, exit the loop
            print("No more questions found.")
            break
    else:
        print(f"Error: {response.status_code}")
        break

    # Pause for a second to avoid hitting the API rate limit
    time.sleep(1)

# Convert the data into a DataFrame
df = pd.DataFrame(all_questions)

# Save the data to a CSV file
csv_filename = 'stackoverflow_questions_with_answers.csv'
df.to_csv(csv_filename, index=False)

print(f"Data successfully saved to {csv_filename} with {len(df)} entries.")