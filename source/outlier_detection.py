import logging
from typing import List
from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to detect outliers in the given DataFrame.

        Parameters:
        df (pd.DataFrame): The dataframe containing features for outlier detection.

        Returns:
        pd.DataFrame: A boolean dataframe indication where outliers are located.
        """
        pass

class ZScoreOutlierDetection(OutlierDetectionStrategy):
    def __init__(self, threshold=3):
        self.threshold = threshold

    def detect_outliers(self, df):
        logging.info("Detecting outliers using Z-score method.")
        z_scores = np.abs((df - df.mean())/df.std())
        outliers = z_scores > self.threshold
        logging.info(f"Outliers detected with Z-score threshold: {self.threshold}.")
        return outliers

class IQROutliersDetection(OutlierDetectionStrategy):
    def detect_outliers(self, df: pd.DataFrame):
        logging.info("Detecting outliers using IQR method.")
        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)
        IQR = q3 - q1
        outliers = (df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR))
        logging.info("Outliers detected using the IQR method.")
        return outliers
    
class OutlierDetector:
    def __init__(self, strategy: OutlierDetectionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: OutlierDetectionStrategy):
        logging.info("Switching outlier detection strategy.")
        self.strategy = strategy

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Executing outlier detection strategy.")
        return self.strategy.detect_outliers(df)
    
    def handle_outliers(self, df:pd.DataFrame, method="remove", **kwargs) -> pd.DataFrame:
        outliers = self.detect_outliers(df)
        if method =="remove":
            logging.info("Removing outliers from the dataset.")
            df_cleaned = df[(~outliers).all(axis=1)]
        elif method =="cap":
            logging.info("Capping outliers from the dataset.")
        else:
            logging.warning(f"Unknown method '{method}'. No outlier handling performed.")
            return df
        logging.info("Outlier handling completed.")
        return df_cleaned

    def visualize_outliers(self, df: pd.DataFrame, features: list) -> List[plt.Figure]:
        figures = []
        for feature in features:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x=df[feature], ax=ax)
            ax.set_title(f"Boxplot of {feature}")
            figures.append(fig)
            plt.close(fig)  # Optional: prevent inline display
        logging.info("Outlier visualization completed.")
        return figures