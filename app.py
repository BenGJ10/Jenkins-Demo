from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask app deployed using Jenkins CI/CD."

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is running"
    }), 200

@app.route("/api")
def api():
    return jsonify({
        "application": "Flask Jenkins Demo",
        "version": "1.0",
        "message": "Hello from Flask API!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)