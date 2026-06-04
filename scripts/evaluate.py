import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(data_set_dict: dict, model) -> dict:
    """
    Model evaluation:
    - Calculating mean-squared-error and r2-score
    """

    x_test = data_set_dict["x_test"]
    y_test = data_set_dict["y_test"]

    # print("Out-of-Bag Score:", model.oob_score_)

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    # print("Mean Squared Error:", mse)

    r2 = r2_score(y_test, y_pred)
    # print("R-squared:", np.round(r2, 2))

    N, p = x_test.shape
    adj_r2 = 1-(((1-r2)*(N-1))/(N-p-1))
    # print("Adj. R-squared:", np.round(adj_r2, 2))

    metrics_dict = {
        "oob_score": model.oob_score_,
        "MSE": np.round(mse, 2),
        "R2": np.round(r2, 2),
        "Adj-R2": np.round(adj_r2, 2)
    }

    return metrics_dict

