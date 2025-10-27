import os
from src.data_preprocessing.preprocessing import preprocess_data
from src.feature_extraction.features import feature_engineering
from src.models.train_model import train_model
import pandas as pd
import glob
from tqdm import tqdm

if __name__ == '__main__':
    # Define paths
    main_folder = 'STData'
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'
    model_dir = 'src/models'
    config_path = 'config/config.json'

    # Create directories if they don't exist
    os.makedirs(raw_data_dir, exist_ok=True)
    os.makedirs(processed_data_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)

    # Step 1: Data Preprocessing
    print("\nStarting data preprocessing...")
    preprocess_data(main_folder, raw_data_dir)
    print("\nData preprocessing finished.")

    # Step 2: Feature Extraction
    print("\nStarting feature extraction...")
    participant_folders = glob.glob(os.path.join(main_folder, '[0-9]*'))
    all_participant_features = []
    for participant_folder in tqdm(participant_folders, desc="Extracting features"):
        participant_id = os.path.basename(participant_folder)
        try:
            eye_path = glob.glob(os.path.join(participant_folder, '**', '*_EYE.csv'), recursive=True)[0]
            ivt_path = glob.glob(os.path.join(participant_folder, '**', '*_IVT.csv'), recursive=True)[0]
        except IndexError:
            print(f"\nSkipping participant {participant_id} due to missing EYE or IVT files.")
            continue

        eye_df = pd.read_csv(eye_path)
        ivt_df = pd.read_csv(ivt_path)

        participant_features = feature_engineering(eye_df, ivt_df)
        participant_features['participant_id'] = participant_id
        all_participant_features.append(participant_features)

    merged_participants_df = pd.DataFrame(all_participant_features)
    processed_data_path = os.path.join(processed_data_dir, 'merged_participants.csv')
    merged_participants_df.to_csv(processed_data_path, index=False)
    print("\nFeature extraction finished.")

    # Step 3: Model Training
    print("\nStarting model training...")
    model_path = os.path.join(model_dir, 'kmeans_model.pkl')
    train_model(config_path, processed_data_path, model_path)
    print("\nModel training finished.")