from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for users
users = [
    {"id": 1, "name": "User 1", "email": "user1@example.com"},
    {"id": 2, "name": "User 2", "email": "user2@example.com"}
]

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
