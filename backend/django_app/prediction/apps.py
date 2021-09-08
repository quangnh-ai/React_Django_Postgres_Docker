from django.apps import AppConfig
import pandas as pd
from joblib import load
import torch
import os

# from prediction.mlmodel import Model

class PredictionConfig(AppConfig):
    name = 'prediction'

    # Get the root path of the app
    BASE_DIR = os.path.join(os.path.dirname(__file__))

    # Get the path of the mlmodel_folder
    MLMODEL_FOLDER = os.path.join(BASE_DIR, 'mlmodel')
    # Get the path of the model file
    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, 'IRISRandomForestClassifier.joblib')

    # model = Model(input_dim=4)
    # model = torch.load(MLMODEL_FILE)

    mlmodel = load(MLMODEL_FILE)

