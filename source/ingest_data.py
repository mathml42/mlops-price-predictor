import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """
        Abstract method for data ingestion.

        """
        pass

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """
        Ingesting data if it is given as zip file.
        """
        # Check the file path is of zip file.
        if not file_path.endswith('.zip'):
            raise ValueError("Given file is not a zip file.")
        
        # Extracting the zip file using zipfile module.
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall('extracted_data')
        
        exrtacted_files = os.listdir('extracted_data')        # List of all files contained in extracted_data directory.
        csv_files = [f for f in exrtacted_files if f.endswith(".csv")] # List of csv file extracted_data contains.

        # Checking whether it contains a csv or not and if it is then not more than one.
        if len(csv_files) == 0:
            raise FileNotFoundError("No .csv file found in the extracted data.")
        if len(csv_files) > 1:
            raise ValueError("It contains more than 1 .csv file, so specify one")
        
        # Getting the csv file path and import it as DataFrame.
        csv_file_path = os.path.join('extracted_data',csv_files[0])
        df = pd.read_csv(csv_file_path)
        return df
    
# Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")