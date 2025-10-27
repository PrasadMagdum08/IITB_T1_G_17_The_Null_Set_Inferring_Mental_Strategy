import os
import glob
import pandas as pd
from tqdm import tqdm

def load_eye_participant_data(participant_dir):
    """
    Loads EYE dataset for a single participant.
    """
    try:
        eye_path = glob.glob(os.path.join(participant_dir, '**', '*_EYE.csv'), recursive=True)
    except:
        print(f'Missing files in {participant_dir}')
        return None
    
    eye_df_list = []
    for eye_file in tqdm(eye_path, desc="Merging EYE data"):
        temp_eye_df = pd.read_csv(eye_file)

        participant_id = os.path.basename(os.path.dirname(eye_file))
        temp_eye_df['participant_id'] = participant_id

        eye_df_list.append(temp_eye_df)   

    merged_eye_df = pd.concat(eye_df_list, ignore_index=True)
    return merged_eye_df

def load_ivt_participant_data(participant_dir):
    """
    Loads IVT dataset for a single participant.
    """
    try:
        ivt_path = glob.glob(os.path.join(participant_dir, '**', '*_IVT.csv'), recursive=True)
    except:
        print(f'Missing files in {participant_dir}')
        return None

    ivt_df_list = []
    for ivt_file in tqdm(ivt_path, desc="Merging IVT data"):
        temp_ivt_df = pd.read_csv(ivt_file)

        participant_id = os.path.basename(os.path.dirname(ivt_file))
        temp_ivt_df['participant_id'] = participant_id

        ivt_df_list.append(temp_ivt_df)   

    merged_ivt_df = pd.concat(ivt_df_list, ignore_index=True)
    return merged_ivt_df

def preprocess_data(main_folder, raw_data_dir):
    all_eye_data = load_eye_participant_data(main_folder)
    all_ivt_data = load_ivt_participant_data(main_folder)

    all_eye_data.to_csv(os.path.join(raw_data_dir, 'all_participants_eye_raw_dataset.csv'), index=False)
    all_ivt_data.to_csv(os.path.join(raw_data_dir, 'all_participants_ivt_raw_dataset.csv'), index=False)

    print("Raw data merged and saved successfully!")