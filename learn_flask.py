from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'First flask'


app.run(port=5001, debug=True)