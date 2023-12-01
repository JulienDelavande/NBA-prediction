import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.model_utils import load_model 
from src.data_processing import preprocessing
import pandas as pd


def is_numeric(value):
    """
    Check if the value is numeric or a list of numeric values.
    
    Parameters
    ----------
    value : int, float or list of int or float
        Value to check.
        
    Returns
    -------
    bool
        True if the value is numeric or a list of numeric values, False otherwise.
    """

    return isinstance(value, (int, float)) or (isinstance(value, list) and all(isinstance(item, (int, float)) for item in value))

def validate_input(data):
    required_fields = ['GP', 'FTM', 'OREB', 'STL', 'BLK', 'AST']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"

    lengths = []
    for field in required_fields:
        value = data[field]
        if not is_numeric(value):
            return False, f"The {field} should be numerical ou a numerical list."

        if isinstance(value, list):
            lengths.append(len(value))
            if any(item < 0 for item in value):
                return False, f"Each elements of {field} should be positif."
        else:
            if value < 0:
                return False, f"The field {field} should be positif."

    if lengths and not all(length == lengths[0] for length in lengths):
        return False, "Each list should have the same length."

    return True, ""


def make_prediction(data):
    """
    Make a prediction on the data.
    
    Parameters
    ----------
    data : dict
        Data to make the prediction on.
    
    Returns
    -------
    response : dict
        Response containing the prediction and the probabilities.
    """

    model = load_model()
    df = pd.DataFrame(data, index=[0])
    processed_data = preprocessing(df)

    prediction = model.predict(processed_data).tolist()
    probabilities = model.predict_proba(processed_data).tolist()
    probabilities_1 = [item[1] for item in probabilities]

    response = {
        'prediction': prediction,
        'probability': probabilities_1,
    }

    return response
