# Project structure influenced by https://github.com/techwithtim/Flask-Web-App-Tutorial.
# All other code original.
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)