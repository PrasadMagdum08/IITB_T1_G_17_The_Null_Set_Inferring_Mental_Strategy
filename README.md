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

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
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

1. **Data Preprocessing and Feature Engineering:**
   - Open and run the `notebooks/data_analysis.ipynb` notebook to process the raw data and generate the `merged_participants.csv` file.

2. **Model Training:**
   - Open and run the `notebooks/model_experiments.ipynb` notebook to train the KMeans clustering model and save it as `src/models/kmeans_model.pkl`.

### Model

The project uses a KMeans clustering model to group participants into two clusters, representing holistic and piecemeal mental strategies. The model is trained on the features extracted from the eye-tracking and IVT data.

The trained model is saved as `src/models/kmeans_model.pkl`.