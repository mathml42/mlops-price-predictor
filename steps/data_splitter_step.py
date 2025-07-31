import logging
from zenml import step
from typing import Tuple, Annotated
import pandas as pd
from source.data_splitter import DataSplitter, SimpleTrainTestSplitStrategy

@step
def data_splitter_step(df:pd.DataFrame,target_column: str,
                       strategy:str="train_test"
                       )-> Tuple[
                           Annotated[pd.DataFrame, "X_train"],
                           Annotated[pd.DataFrame, "X_test"],
                           Annotated[pd.Series, "y_train"],
                           Annotated[pd.Series, "y_test"],
                       ]:
    if (df is None) or (target_column is None):
        raise FileNotFoundError("Dataframe not found.")
    if strategy=="train_test":
        splitter = DataSplitter(SimpleTrainTestSplitStrategy())
    else:
        raise ValueError(f"Unsupported data split strategy:{strategy}.")
    X_train, X_test, y_train, y_test = splitter.split(df,target_column)
    return X_train, X_test, y_train, y_test