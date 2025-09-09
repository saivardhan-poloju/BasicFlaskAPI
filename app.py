from flask import Flask, jsonify
import requests
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def home():
    """
    Home endpoint
    ---
    responses:
      200:
        description: Welcome message
    """
    return "Hello Flask"

@app.route("/posts")
def get_posts():
    """
    Get posts from JSONPlaceholder
    ---
    responses:
      200:
        description: A list of posts
        examples:
          application/json: [{"userId": 1, "id": 1, "title": "Post 1", "body": "..." }]
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data[:5])
    else:
        return jsonify({"error": "Failed to fetch posts"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)