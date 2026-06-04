import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.model_selection import train_test_split

def preprocess_data(df: pd.DataFrame) -> list:
    """
    Basic cleaning:
    - Drop less important features
    - Train-test-split
    - Feature encoding
    - Feature Scaling
    """

    # Dropping unecessary features
    df = df.drop(columns=["sex", "region", "children"])

    # Splitting data in to train and test sets
    X = df[['age', 'bmi', 'smoker']]
    Y = df["charges"]

    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, random_state=42, 
        train_size=0.9, 
        shuffle=True,
    )

    # Applying ColumnTransformer
    transformer = ColumnTransformer(transformers=[
        ('t1',RobustScaler(),['age', 'bmi']),
        ('t2',OneHotEncoder(sparse_output = False, drop='first'),['smoker'])
    ],remainder='passthrough')

    x_train_nw = pd.DataFrame(transformer.fit_transform(x_train))
    x_test_nw = pd.DataFrame(transformer.transform(x_test))

    data_set_dict = {
        "x_train": x_train_nw,
        "x_test": x_test_nw,
        "y_train": y_train,
        "y_test": y_test
    }

    return [data_set_dict, transformer]
