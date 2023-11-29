import pickle

def load_model(model_path='models/model_1.pkl'):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

