from zenml import pipeline
from pipelines.training_pipeline import ml_pipeline
from steps.dynamic_importer import dynamic_importer
from steps.prediction_service_loader import prediction_service_loader
from steps.predictor import predictor
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
import os

requirement_file = os.path.join(os.path.dirname(__file__), "requirements.txt")

@pipeline
def continuos_deployment_pipeline():
    """Run a training job and deploy an MLflow model deployment."""
    # Run the training pipeline
    trained_model = ml_pipeline()

    # (Re)deploy the trained model
    mlflow_model_deployer_step(
        workers = 3,
        deploy_decision =True,
        model = trained_model
    )

@pipeline(enable_cache=False)
def inference_pipeline():
    """Run a batch inference job with data loaded from an API."""
    # Load batch data for inference
    batch_data = dynamic_importer()

    # Load the deployed model service
    model_deployment_service = prediction_service_loader(
        pipeline_name = "continuos_deployment_pipeline",
        step_name = "mlflow_model_deployer_step"
    )

    # Run predictions on the batch data
    predictor(service = model_deployment_service, input_data = batch_data)