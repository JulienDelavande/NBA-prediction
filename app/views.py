import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.model_utils import load_model 
from src.data_processing import preprocessing
import pandas as pd

def is_numeric(value):
    return isinstance(value, (int, float)) or (isinstance(value, list) and all(isinstance(item, (int, float)) for item in value))

def validate_input(data):
    required_fields = ['GP', 'PTS', 'FGM', 'MIN', 'FTA', 'FTM', 'REB', 'OREB', 'FGA']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Champs manquants: {', '.join(missing_fields)}"

    lengths = []
    for field in required_fields:
        value = data[field]
        if not is_numeric(value):
            return False, f"Le champ {field} doit être numérique ou une liste de valeurs numériques."

        if isinstance(value, list):
            lengths.append(len(value))
            if any(item < 0 for item in value):
                return False, f"Tous les éléments du champ {field} doivent être positifs."
        else:
            if value < 0:
                return False, f"Le champ {field} doit être positif."

    if lengths and not all(length == lengths[0] for length in lengths):
        return False, "Toutes les listes doivent avoir la même longueur."

    return True, ""




def make_prediction(data):
    model = load_model()

    df = pd.DataFrame(data, index=[0])

    processed_data = preprocessing(df)

    prediction = model.predict(processed_data).tolist()
    probabilities = model.predict_proba(processed_data).tolist()
    probabilities_1 = [item[1] for item in probabilities]


    response = {
        'prediction': prediction,
        'probabilities of class 1': probabilities_1,
    }



    return response


