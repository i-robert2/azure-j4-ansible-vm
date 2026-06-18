from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/")
def index():
    return jsonify({"app": "notes-api", "host": "configured-by-ansible"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
