from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage (for demo purposes)
users = []

# Welcome route (optional)
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the User Management API!"}), 200

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Validation check
    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and Email are required fields'}), 400

    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - update user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user), 200

# DELETE - delete user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': f'User {user_id} deleted successfully'}), 200

# Run the app
if __name__ == '__main__':
    print(" Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
