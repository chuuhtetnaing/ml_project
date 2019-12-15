# new script, dump_model.py, does the creation and dumping of the NeuralNetwork

from joblib import dump
from joblib import load
import pandas as pd
from machine_learning_reviews import Model

gps_df = pd.read_csv('dataset/google-play-store-apps/googleplaystore.csv')
gps_df.dropna(inplace = True)

column_names = ['Category', 'Content Rating', 'Android Ver', 'Size', 'Installs', 'Price', 'Rating', 'Last Updated']
X = gps_df[column_names].copy()
y = gps_df['Reviews'].copy()

import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

if __name__ == "__main__":
	model = Model(X,y)
	filename = 'finalized_google_playstore_for_reviews.sav'
	dump(model, filename)