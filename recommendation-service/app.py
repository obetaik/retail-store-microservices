# Recommendation Service (recommendation-service/app.py)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/recommendation/<user_id>')
def get_recommendation(user_id):
    return jsonify({"user_id": user_id, "recommendations": ["1", "2"]})

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)


