from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Dummy data for demonstration
user_profiles = {}
recommendations = {
    'pop': ['Song A', 'Song B'],
    'rock': ['Song C', 'Song D']
}

@app.route('/user', methods=['POST'])
def create_user_profile():
    data = request.json
    user_id = data.get('user_id')
    user_profiles[user_id] = {
        'dob': data.get('dob'),
        'gender': data.get('gender'),
        'favorite_artists': data.get('favorite_artists')
    }
    return jsonify({'message': 'User profile created successfully.'}), 201


@app.route('/recommendations/<string:genre>', methods=['GET'])
def get_recommendations(genre):
    return jsonify({'recommendations': recommendations.get(genre, [])})


if __name__ == '__main__':
    app.run(debug=True)
