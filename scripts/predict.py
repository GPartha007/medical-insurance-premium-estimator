import pickle as pkl
import pandas as pd
import numpy as np

# load the model
filename = "../models/pipeline_random_forest.pkl"
load_model = pkl.load(open(filename, 'rb'))

# Inputs
input_data = pd.DataFrame(
    data = [[45, 25.175, 'no']], 
    columns = ['age', 'bmi', 'smoker']
)

y_pred = load_model.predict(input_data)

print(f"\n\nPredicted charges($): {np.round(y_pred[0], 3)}\n\n")

