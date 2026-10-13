from flask import Flask, jsonify, request

app = Flask(__name__)

# Foundational data store for ACEest Fitness & Gym
programs = {
    "Fat Loss": {"workout": "High-intensity interval training, cardio.", "nutrition": "High protein, caloric deficit."},
    "Muscle Gain": {"workout": "Heavy weightlifting, progressive overload.", "nutrition": "High protein, caloric surplus."},
    "Beginner": {"workout": "Light Strength + Mobility", "nutrition": "Balanced meals."}
}
users = {}

@app.route('/')
def index():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API!"}), 200

@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify({"programs": programs}), 200

@app.route('/programs/<name>', methods=['GET'])
def get_program(name):
    program = programs.get(name)
    if program:
        return jsonify({"program": program}), 200
    return jsonify({"error": "Program not found"}), 404

@app.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data or 'username' not in data or 'program' not in data:
        return jsonify({"error": "Missing user data"}), 400
    
    username = data['username']
    program = data['program']
    
    if program not in programs:
        return jsonify({"error": "Invalid program selected"}), 400
        
    users[username] = {"program": program}
    return jsonify({"message": f"User {username} registered successfully.", "user": users[username]}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    