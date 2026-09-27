from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SWE40006 Task 4 - Docker Web Application</h1>
    <p>Hello from my Python Flask application!</p>
    <p>This application is being prepared for container deployment.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
