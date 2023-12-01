import numpy as np

def preprocessing(data):
    """
    Preprocess the data before making the prediction.
    
    Parameters
    ----------
    data : pandas.DataFrame
        Data to preprocess.
    
    Returns
    -------
    data : pandas.DataFrame
        Preprocessed data.
    """

    features = ['GP', 'FTM', 'OREB', 'STL', 'BLK', 'AST']
    data = data[features]
    data = np.log1p(data)

    return data

