import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import pickle as pkl

from load_data import load_data
from preprocess import preprocess_data
from model_train import train_model
from evaluate import evaluate_model

if __name__ == "__main__":
    file_path = "../data/Medical Cost Personal Dataset - Regression.csv"

    df = load_data(file_path=file_path)
    data_set_dict, transformer = preprocess_data(df)
    model = train_model(data_set_dict)

    metrics = evaluate_model(data_set_dict, model)
    print(metrics)

    # Preparing a Pipeline
    pipeline = Pipeline([
        ('transformer', transformer),
        ('model', model)
    ])

    filename = '../models/pipeline_random_forest.pkl'
    pkl.dump(pipeline, open(filename, 'wb'))

