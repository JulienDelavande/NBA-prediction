from flask import Flask, request, jsonify
from views import make_prediction, validate_input

app = Flask(__name__)
PORT = 5000
HOST = 'localhost'
DEBUG = True

API_NAME = "NBA Career Longevity Prediction API"
API_VERSION = "1.0"
API_ENDPOINTS = [
        {
            "endpoint": "/predict",
            "method": "POST",
            "description": "Takes player statistics as input and returns a prediction on whether the player will last over 5 years in the NBA.",
            "required_fields": ["GP", "PTS", "FTA", "FTM", "FGA", "DREB", "BLK"],
            "input_format": {
                "GP": "integer or list of integers (Games Played)",
                "FTM": "integer or list of integers (Free Throws Made)",
                "OREB": "integer or list of integers (Offensive Rebounds)",
                "STL": "integer or list of integers (Steals)",
                "BLK": "integer or list of integers (Blocks)",
                "AST": "integer or list of integers (Assists)"
            },
            "output_format": {
                "prediction": "lit of booleans (true if the player is predicted to last more than 5 years, false otherwise)",
                "probabilities": "list of floats (probability of the player lasting more than 5 years)"},
            "example_request": {
                "GP": f"{82} or {[82, 80, 90, 75, 82]}",
                "FTM": f"{400} or {[400, 300, 500, 200, 350]}",
                "OREB": f"{300} or {[300, 200, 400, 100, 250]}",
                "STL": f"{1000} or {[1000, 900, 1100, 800, 950]}",
                "BLK": f"{100} or {[100, 80, 120, 60, 90]}",
                "AST": f"{500} or {[500, 400, 600, 300, 450]}"
            },
            "example_response": {
                    "prediction": f"{True} or {[True, False, True, False, True]}",
                    "probabilities": f"{0.8} or {[0.8, 0.2, 0.9, 0.1, 0.7]}"
                }
        }
    ]

API_INFO = {
    "api_name": API_NAME,
    "version": API_VERSION,
    "status": "OK",
    "message": "Welcome to the NBA Career Longevity Prediction API. Use this API to predict whether NBA players will stay in the league for the next 5 years based on their performance statistics.",
    "endpoints": {
        "/predict": "POST request to make a single or multiple prediction. Requires player statistics as input.",
        "/documentation": "GET request to access the API documentation for detailed usage guidelines."
    },
    "endpoints": API_ENDPOINTS,
    }

API_DOCUMENTATION = {
    "documentation": {
        "overview": "This API predicts whether NBA players will have a career span of over 5 years based on their performance statistics.",
        "version": "1.0",
        "base_url": "https://localhost:500",
        "endpoints": API_ENDPOINTS,
        "errors": {
            "description": "This API uses conventional HTTP response codes to indicate success or failure of an API request.",
            "codes": {
                "200": "Success",
                "400": "Bad Request - The request was unacceptable, often due to missing a required parameter.",
                "404": "Not Found - The requested resource doesn’t exist.",
                "500": "Internal Server Error - We had a problem with our server. Try again later."
            }
        },
        "contact_info": {
            "email": "Julien.DELAVANDE@student.isae-supaero.fr"
        }
    }
}


@app.route('/')
def index():
    return jsonify(API_INFO), 200

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json(force=True)

    is_valid, error_message = validate_input(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    result = make_prediction(data)
    return jsonify(result)

@app.route('/documentation')
def info():
    return jsonify(API_DOCUMENTATION), 200


if __name__ == '__main__':
    app.run(debug=DEBUG, 
            port=PORT,
            host=HOST)
    