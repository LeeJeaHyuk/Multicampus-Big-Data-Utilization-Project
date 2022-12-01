import pandas as pd

def selectparam(csv_name, index):
    file_path = './modeldata/' + csv_name + '.csv'
    df = pd.read_csv(file_path)

    df_drop = df.loc[[index]].dropna(axis=1)
    dict = df_drop.to_dict('list')
    if 'date' in dict:
        dict.pop('date')
    if 'data_name' in dict:
        dict.pop('data_name')
    if 'scaler' in dict:
        dict.pop('scaler')
    if 'best_score' in dict:
        dict.pop('best_score')

    return dict