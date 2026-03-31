from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# data dummy (sementara)
users = {
    "jose": "12345"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({
            "message": "Login successful"
        })
    else:
        return jsonify({
            "message": "Invalid username or password"
        })

if __name__ == "__main__":
    app.run(debug=True)

#PYTHON/API#
