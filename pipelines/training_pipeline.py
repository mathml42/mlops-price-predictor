from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_value_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from steps.data_splitter_step import data_splitter_step
from steps.model_building_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step
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
    cleaned_data, plot = outlier_detection_step(transformed_data,
                                                features=["Gr Liv Area", "SalePrice"])
    
    X_train, X_test, y_train, y_test = data_splitter_step(cleaned_data, target_column="SalePrice")
    
    model = model_building_step(X_train=X_train, y_train=y_train)

    evaluation_metrics, mse = model_evaluator_step(
        model, X_test, y_test
    )

    return model

if __name__=="__main__":
    # run ml pipeline
    run = ml_pipeline()