import logging 
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#Abstract Base class for model building strategy
class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series
                            ) -> RegressorMixin:
        """
        Abstract method to build and train a model.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        RegressorMixin: A trained scikit-learn model instance.
        """
        pass

class LinearRegressionStrategy(ModelBuildingStrategy):
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series)-> Pipeline:
        """
        Builds and trains a linear regression model using scikit-learn.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        Pipeline: A scikit-learn pipeline with a trained Linear Regression model.
        """
        # Ensure the inputs are of the correct type
        if not isinstance(X_train, pd.DataFrame):
            raise TypeError("X_train must be a pandas DataFrame.")
        if not isinstance(y_train, pd.Series):
            raise TypeError("y_train must be a pandas Series.")
        
        logging.info("Initializing Linear Regression model with scaling.")

        # Creating a pipeline with standard scaling and linear regression
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LinearRegression())
            ]
        )

        logging.info("Training Linear Regression model.")
        pipeline.fit(X_train, y_train)

        logging.info("Model training completed.")
        return pipeline
    
    # Context Class for Model Building
class ModelBuilder:
    def __init__(self, strategy: ModelBuildingStrategy):
        """
        Initializes the ModelBuilder with a specific model building strategy.

        Parameters:
        strategy (ModelBuildingStrategy): The strategy to be used for model building.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: ModelBuildingStrategy):
        """
        Sets a new strategy for the ModelBuilder.

        Parameters:
        strategy (ModelBuildingStrategy): The new strategy to be used for model building.
        """
        logging.info("Switching model building strategy.")
        self._strategy = strategy

    def build_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
        """
        Executes the model building and training using the current strategy.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        RegressorMixin: A trained scikit-learn model instance.
        """
        logging.info("Building and training the model using the selected strategy.")
        return self._strategy.build_and_train_model(X_train, y_train)