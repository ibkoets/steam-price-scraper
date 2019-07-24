#This will be used to create an API for the Steam price checker
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '<h1>You have started a new Flask page for your web API</h1>'


if __name__ == '__main__':   
    app.run(debug=True)


