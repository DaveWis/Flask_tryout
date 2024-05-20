from flask import Flask

app = Flask(__name__)

# route
@app.route('/')
def home():
    return "<p>Huiswerk voor hoofdstuk 11!<p>"