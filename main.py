from flask import Flask, jsonify

app = Flask(__name__)

app.route('/')
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# An enpoint to return an object of schoos
@app.route('/schools', methods=['GET'])
def get_schools():
    schools = [
        {'name': 'ABC High School', 'location': 'New York'},
        {'name': 'XYZ Academy', 'location': 'Los Angeles'},
        {'name': '123 Institute', 'location': 'Chicago'}
    ]
    return jsonify(schools)
print("Starting development server")
print("new line added")
print("trying to get a conflict")