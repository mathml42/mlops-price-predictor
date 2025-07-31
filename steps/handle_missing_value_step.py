import pandas as pd
from source.handle_missing_values import DropMissingValuesStrategy, FillingMissingValuesStrategy,MissingValueHandler
from zenml import step
from typing import Annotated

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean") -> Annotated[pd.DataFrame, "Cleaned_Dataframe"]:
    """Handles missing values using MissingValueHandler and the specified strategy."""
    if strategy == "drop":
        handler = MissingValueHandler(DropMissingValuesStrategy(axis=0))
    elif strategy in ["mean", "median", "mode", "constant"]:
        handler = MissingValueHandler(FillingMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy {strategy}.")
    
    cleaned_df = handler.handler(df)
    return cleaned_df