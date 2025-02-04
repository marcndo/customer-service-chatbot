from app.routes import main
from dotenv import load_dotenv


load_dotenv()

if __name__ == '__main__':
    app.run(debug=True)