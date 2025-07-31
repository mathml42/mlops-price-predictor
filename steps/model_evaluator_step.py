from zenml import step
import logging
from sklearn.pipeline import Pipeline
from source.model_evaluator import ModelEvaluator, RegressionModelEvaluationSrategy
import pandas as pd
from typing import Tuple, Annotated


@step(enable_cache=False)
def model_evaluator_step(
    trained_model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series
) -> Tuple[Annotated[dict, "MSE & R2"], Annotated[float, "MSE"]]:
    """
    Evaluates the trained model using ModelEvaluator and RegressionModelEvaluationStrategy.

    Parameters:
    trained_model (Pipeline): The trained pipeline containing the model and preprocessing steps.
    X_test (pd.DataFrame): The test data features.
    y_test (pd.Series): The test data labels/target.

    Returns:
    dict: A dictionary containing evaluation metrics.
    """
    # Ensure the inputs are of the correct type
    if not isinstance(X_test, pd.DataFrame):
        raise TypeError("X_test must be a pandas DataFrame.")
    if not isinstance(y_test, pd.Series):
        raise TypeError("y_test must be a pandas Series.")
    
    logging.info("Applying the same preprocessing to the test data.")

    # Apply the preprocessing and model prediction
    X_test_preprocessed = trained_model.named_steps["preprocessor"].transform(X_test)

    # Initialize the evaluator with the regression strategy
    evaluator = ModelEvaluator(RegressionModelEvaluationSrategy())

    # Perform the evaluation
    evaluation_metrics = evaluator.evaluate(
        trained_model.named_steps["model"], X_test_preprocessed, y_test
    )

    # Ensure that the evaluation metrics are returned as a dictionary
    if not isinstance(evaluation_metrics, dict):
        raise ValueError("Evaluation metrics must be returned as a dictionary.")
    mse = evaluation_metrics.get("Mean Squared Error", None)
    return evaluation_metrics, mse