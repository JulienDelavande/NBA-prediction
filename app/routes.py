from flask import render_template, request, jsonify
from .views import make_prediction, validate_input
from app import app



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json(force=True)

    is_valid, error_message = validate_input(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    result = make_prediction(data)
    return jsonify(result)

@app.route('/health')
def health():
    return jsonify({'message': 'OK'}), 200

@app.route('/version')
def version():
    return jsonify({'version': '1.0.0'}), 200

@app.route('/info')
def info():
    return jsonify({'info': 'This is a simple API to predict the number of points a basketball player will score in the next game'}), 200

@app.route('/docs')
def docs():
    return render_template('docs.html')

