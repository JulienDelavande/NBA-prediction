import joblib

def load_model(model_path='models/model_1.pkl'):
    with open(model_path, 'rb') as file:
        model = joblib.load(file)
        print(f'type du model ------- {type(model)}')
    return model
