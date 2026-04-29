import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("MESSAGE", "Default message 🚀")
    secret = os.getenv("SECRET_MESSAGE", "No secret")
    return f"{message} | {secret}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
