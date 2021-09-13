from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route
def bye():
    return"bye!!"

if __name__ == "__main__":
    app.run()