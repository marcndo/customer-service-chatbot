from app import create_app
from app.routes import main
from dotenv import load_dotenv


load_dotenv()
app = create_app()

@app.route('/')
def home():
    return "Welcome to the Customer Service Chatbot API!"

if __name__ == '__main__':
    app.run(debug=True)