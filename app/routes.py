from flask import Flask, request, jsonify

from views import make_prediction, validate_input

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'}), 200

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


if __name__ == '__main__':
    app.run(debug=True, 
            port=5000,
            host='localhost')