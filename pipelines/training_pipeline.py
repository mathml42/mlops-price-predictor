from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_value_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step

from zenml import pipeline, Model

@pipeline(
    model = Model(
        # The name uniquely identifies this model
        name= "house_price_predictor"
    )
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion step
    data = data_ingestion_step(
        file_path = "/Users/himanshu/dev/study_p/mlops-price-predictor/data/archive.zip"
    )

    # Handle Missing Values
    filled_data = handle_missing_values_step(data)

    transformed_data = feature_engineering_step(filled_data,
                                                strategy="log", 
                                                features=["Gr Liv Area", "SalePrice"])

    return transformed_data

if __name__=="__main__":
    # run ml pipeline
    run = ml_pipeline()