from .models.model_utils import load_model, preprocess_data
import pandas as pd

def validate_input(data):

    # Check if data is a dictionary
    required_fields = ['GP', 'PTS', 'FGM', 'MIN', 'FTA', 'FTM', 'REB', 'OREB', 'FGA']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Champs manquants: {', '.join(missing_fields)}"

    # Check lenght of each field
    first_length = len(data[required_fields[0]])
    for field in required_fields:
        if len(data[field]) != first_length:
            return False, f"Le champ {field} n'a pas la même longueur que les autres champs"
        
    # Check if each field is numeric
    for field in required_fields:
        if not data[field].isnumeric():
            return False, f"Le champ {field} n'est pas numérique"
        
    # Check if each field is positive
    for field in required_fields:
        if data[field] < 0:
            return False, f"Le champ {field} n'est pas positif"

    return True, ""



def make_prediction(data):
    model = load_model()

    df = pd.DataFrame(data, index=[0])

    processed_data = preprocess_data(df)

    prediction = model.predict(processed_data)

    response = {
        'prediction': prediction[0]
    }

    return response


