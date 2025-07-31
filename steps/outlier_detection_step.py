import logging
from typing import Tuple, List, Annotated
import matplotlib.pyplot as plt
from zenml import step
import pandas as pd
from source.outlier_detection import OutlierDetector, ZScoreOutlierDetection, IQROutliersDetection

@step
def outlier_detection_step(df: pd.DataFrame,
                           features:list,
                           strategy:str = "z_score",
                           method:str = "remove", 
                           threshold:int =3) -> Tuple[Annotated[pd.DataFrame,"Outlier_cleaned"], Annotated[List[plt.Figure], "Plots"]]:
    """Detects and removes outliers using OutlierDetector."""
    logging.info(f"Starting outlier detection step with DataFrame of shape: {df.shape}")

    if df is None:
        logging.error("Received a NoneType DataFrame.")
        raise ValueError("Input df must be a non-null pandas DataFrame.")

    if not isinstance(df, pd.DataFrame):
        logging.error(f"Expected pandas DataFrame, got {type(df)} instead.")
        raise ValueError("Input df must be a pandas DataFrame.")

    df_numeric = df.select_dtypes(include=[int, float])
    if strategy == "z_score":
        detector = OutlierDetector(ZScoreOutlierDetection(threshold))
    elif strategy == "IQR":
        detector = OutlierDetector(IQROutliersDetection())
    else:
        raise ValueError(f"Unsupported feature engineering strategy: {strategy}")
    df_cleaned = detector.handle_outliers(df_numeric, method)
    visualization = detector.visualize_outliers(df_numeric, features)
    return df_cleaned, visualization