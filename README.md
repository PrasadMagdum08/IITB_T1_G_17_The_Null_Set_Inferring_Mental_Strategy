### Inferring Mental Strategy (Holistic vs. Piecemeal)

This project aims to infer an individual's mental strategy (holistic vs. piecemeal) based on eye-tracking data and other physiological signals.

### Software And Tools Requirements

- Python 3.10
- Jupyter Notebook
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- HMMlearn
- Flask
- tqdm

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PrasadMagdum08/IITB_T1_G_17_The_Null_Set_Inferring_Mental_Strategy.git
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```
3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the entire data processing and model training pipeline, run the `main.py` script:

```bash
python main.py
```

This will:
1. Preprocess the raw data from the `STData` directory.
2. Extract features from the preprocessed data.
3. Train a KMeans clustering model.
4. Save the trained model to `src/models/kmeans_model.pkl`.

### Dashboard

To view the results on the dashboard, run the `run.py` script:

```bash
python run.py
```

Then, open your web browser and navigate to `http://127.0.0.1:5000/`.

The dashboard displays three charts:
- **Holistic Cluster:** A bar chart showing the `fixation_mean` and `saccade_mean` for participants in the holistic cluster.
- **Piecemeal Cluster:** A bar chart showing the `fixation_mean` and `saccade_mean` for participants in the piecemeal cluster.
- **Holistic vs. Piecemeal:** A pie chart showing the proportion of participants in each cluster.

### Model

The project uses a KMeans clustering model to group participants into two clusters, representing holistic and piecemeal mental strategies. The model is trained on the features extracted from the eye-tracking and IVT data.

The trained model is saved as `src/models/kmeans_model.pkl`.
