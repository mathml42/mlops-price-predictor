from zenml import step
import pandas as pd
from typing import Annotated
from source.feature_engineering import FeatureEngineer, LogTransformation, MinMaxScaling, StandardScaling, OneHotEncoding

@step
def feature_engineering_step(df: pd.DataFrame, features: list = None, strategy: str ="log" 
                             ) -> Annotated[pd.DataFrame, "Transformed_dataframe"]:
    """Performs feature engineering using FeatureEngineer and selected strategy."""
    
    if features is None:
        features = []
    if strategy == "log":
        engineer = FeatureEngineer(LogTransformation(features))
    elif strategy == "standard_scaling":
        engineer = FeatureEngineer(StandardScaling(features))
    elif strategy == "minmax_scaling":
        engineer = FeatureEngineer(MinMaxScaling(features))
    elif strategy == "onehot_encoding":
        engineer = FeatureEngineer(OneHotEncoding(features))
    else:
        raise ValueError(f"Unsupported feature engineering strategy: {strategy}")
    
    transformed_df = engineer.apply_feature_engineering(df)
    return transformed_df