import pandas as pd

def preprocessing(data):
    data = data.drop(['Name'], axis=1)
    data.loc[:, '3P%'] = data.loc[:, '3P%'].fillna(0)
    data = data.drop_duplicates()

    features = ['GP', 'PTS', 'FGM', 'MIN', 'FTA', 'FTM', 'REB', 'OREB', 'FGA']

    data = data[features]

    return data

