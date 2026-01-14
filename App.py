from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "BOT WORKS"

if __name__ == '__main__':
    app.run()
