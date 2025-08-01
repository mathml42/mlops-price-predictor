from source.ingest_data import DataIngestorFactory
from zenml import step
from typing import Annotated
import pandas as pd

@step
def data_ingestion_step(file_path: str) -> Annotated[pd.DataFrame, "DataFrame"]:
    """Ingest data from a ZIP file using the appropriate DataIngestor."""
    # Determine the file extension.
    file_extension = ".zip" # Since we're dealing with ZIP files, this is hardcoded

    # Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # Ingest the data and load it into a DataFrame
    df = data_ingestor.ingest(file_path)
    return df