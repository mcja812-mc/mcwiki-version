from flask import Flask, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__, static_folder='static')
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'rows.json')

def load_rows():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_rows(rows):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/rows', methods=['GET'])
def get_rows():
    return jsonify(load_rows())

@app.route('/api/rows', methods=['POST'])
def set_rows():
    rows = request.get_json()
    save_rows(rows)
    return jsonify({'ok': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
