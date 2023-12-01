import joblib

def load_model(model_path='models/model_1.pkl'):
    """
    Load the model from the given path.
    
    Parameters
    ----------
    model_path : str, optional
        Path to the model to load. The default is 'models/model_1.pkl'.
    
    Returns
    -------
    model : sklearn.linear_model.LogisticRegression
        The loaded model."""
    
    with open(model_path, 'rb') as file:
        model = joblib.load(file)
        
    return model
