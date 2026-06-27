import pandas as pd
import sqlite3

conn = sqlite3.connect('football.db')
pd.read_csv('results.csv').to_sql('results', conn, if_exists='replace', index=False)
pd.read_csv('shootouts.csv').to_sql('shootouts', conn, if_exists='replace', index=False)
print("Created")

import os
import sqlite3
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi


os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME', 'bilala28')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY', 'a51ca52ea80432ba1530efce407c52ac')

api = KaggleApi()
api.authenticate()

# --- The code below (starting from BASE_DIR) was generated with AI assistance. ---
# The rest of the project, including the IPython notebook, was written by a human.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Downloading latest dataset from Kaggle...")
api.dataset_download_files('martj42/international-football-results-from-1872-to-2017', path=BASE_DIR, unzip=True)

db_path = os.path.join(BASE_DIR, 'football.db')
conn = sqlite3.connect(db_path)

pd.read_csv(os.path.join(BASE_DIR, 'results.csv')).to_sql('results', conn, if_exists='replace', index=False)
print("Updated!")