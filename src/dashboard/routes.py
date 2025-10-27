from flask import render_template, jsonify
from src.dashboard.app import app
import pandas as pd
import joblib

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    model = joblib.load('src/models/kmeans_model.pkl')
    data = pd.read_csv('data/processed/merged_participants.csv')
    
    # Impute missing values
    numeric_cols = data.select_dtypes(include=['number']).columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    # Predict clusters
    features = data.drop('participant_id', axis=1)
    clusters = model.predict(features)
    data['cluster'] = clusters

    # Separate data into holistic and piecemeal clusters
    holistic_cluster = data[data['cluster'] == 0].to_dict(orient='records')
    piecemeal_cluster = data[data['cluster'] == 1].to_dict(orient='records')

    return jsonify({
        'holistic': holistic_cluster,
        'piecemeal': piecemeal_cluster
    })