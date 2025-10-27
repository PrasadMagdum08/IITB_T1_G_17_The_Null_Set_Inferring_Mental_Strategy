import pandas as pd
import numpy as np

def feature_engineering(eye_df, ivt_df):
    eye_df['Timestamp'] = pd.to_datetime(eye_df['Timestamp'], errors='coerce')
    ivt_df['Timestamp'] = pd.to_datetime(ivt_df['Timestamp'], errors='coerce')

    eye_numeric_cols = eye_df.select_dtypes(include=[np.number]).columns
    eye_outlier_cols = []
    for col in eye_numeric_cols:
        Q1 = eye_df[col].quantile(0.25)
        Q3 = eye_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        if((eye_df[col] < lower) | (eye_df[col] > upper)).any():
            eye_outlier_cols.append(col)

    for col in eye_df.columns:
        if eye_df[col].isnull().any():
            if col in eye_outlier_cols:
                eye_df[col] = eye_df[col].fillna(eye_df[col].median())
            elif eye_df[col].dtype in ["float64", "int64"]:
                eye_df[col] = eye_df[col].fillna(eye_df[col].mean())
            else:
                eye_df[col] = eye_df[col].fillna(eye_df[col].mode()[0])

    eye_df['PupilAvg'] = (eye_df['ET_PupilLeft'] + eye_df['ET_PupilRight']) / 2
    pupil_mean = eye_df['PupilAvg'].mean()
    pupil_std = eye_df['PupilAvg'].std()

    ivt_numeric_cols = ivt_df.select_dtypes(include=[np.number]).columns
    ivt_outlier_cols = []
    for col in ivt_numeric_cols:
        Q1 = ivt_df[col].quantile(0.25)
        Q3 = ivt_df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        if((ivt_df[col] < lower) | (ivt_df[col] > upper)).any():
            ivt_outlier_cols.append(col)

    for col in ivt_df.columns:
        if ivt_df[col].isnull().any():
            if col in ivt_outlier_cols:
                ivt_df[col] = ivt_df[col].fillna(ivt_df[col].median())
            elif ivt_df[col].dtype in ["float64", "int64"]:
                ivt_df[col] = ivt_df[col].fillna(ivt_df[col].mean())
            else:
                ivt_df[col] = ivt_df[col].fillna(ivt_df[col].mode()[0])

    fixation_mean = ivt_df['Fixation Duration'].mean()
    fixation_std = ivt_df['Fixation Duration'].std()
    n_fix = ivt_df['Fixation Index'].nunique()

    saccade_mean = ivt_df['Saccade Amplitude'].mean()
    saccade_std = ivt_df['Saccade Amplitude'].std()
    n_sacc = ivt_df['Saccade Index'].nunique()

    participant_features = {
        'fixation_mean': fixation_mean,
        'fixation_std': fixation_std,
        'n_fixations': n_fix,
        'saccade_mean': saccade_mean,
        'saccade_std': saccade_std,
        'n_saccades': n_sacc,
        'pupil_mean': pupil_mean,
        'pupil_std': pupil_std
    }

    return participant_features
