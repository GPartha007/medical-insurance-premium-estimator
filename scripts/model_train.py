from sklearn.ensemble import RandomForestRegressor

def train_model(data_set_dict: dict):
    """
    Model training:
    - Using RandomForestRegressor
    """

    x_train = data_set_dict["x_train"]
    y_train = data_set_dict["y_train"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        oob_score=True
    )
    model.fit(x_train, y_train)

    return model

