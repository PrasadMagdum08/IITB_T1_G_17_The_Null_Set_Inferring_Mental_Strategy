import json
import pandas as pd
from sklearn.cluster import KMeans
import joblib
import pickle

def train_model(config_path, data_path, model_path):
    with open(config_path) as f:
        config = json.load(f)

    data = pd.read_csv(data_path)

    # Impute missing values
    numeric_cols = data.select_dtypes(include=['number']).columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    features = data.drop('participant_id', axis=1)

    kmeans = KMeans(
        n_clusters=config['model_settings']['n_clusters'],
        random_state=config['model_settings']['random_state'],
        n_init=config['model_settings']['n_init']
    )

    kmeans.fit(features)

    with open(model_path, 'wb') as f:
        pickle.dump(kmeans, f)

    print('KMeans model trained and saved successfully!')