from abc import ABC, abstractmethod
import pandas as pd

# Abstract base class for Data Inspection Stratgies
# Sub-class must implement inspect method
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of inspeciton

        Parameter:
        df(pd.DataFrame): The dataframe on which inspection performs.

        Return:
        None: This method prints results directly.
        """
        pass

class DataTypeInspectionStrategy():
    def inspect(self, df:pd.DataFrame):
        """
        Performs on dataframe and shows data types of columns.

        Parameter:
        df(pd.DataFrame): The dataframe on which inspection performs.

        Return: 
        None: Prints the data types of each columns.
        """
        print("\nData Types and Non-null values count:")
        d_types = df.info()
        print(d_types)
    
class DataStatsInspectionStrategy():
    def inspect(self, df:pd.DataFrame):
        """
        Performs statistical inspeciton on dataframe.

        Parameter:
        df(pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Just prints the statistical behavior of dataframe.
        """
        print('\nStatistical behaviour of data on Numerical type:')
        print(df.describe())
        print('\nStatistical behaviour of data on Categorical type:')
        print(df.describe(include=['O']))

class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initialize the Data Inspector using a specific strategy.

        Parameters:
        strategy(DataInspectionStrategy): New strategy to be used.

        Returns: None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets the new strategy to the DataInspector.

        Parameters:
        strategy(DataInspectionStrategy): New strategy to be used.

        Return:
        None
        """
        self._strategy = strategy
    
    def execute_inspection(self, df: pd.DataFrame):
        """
        Starts the specified inspectionto the data frame.

        Parameters:
        df(pd.DataFrame): DataFrame for inspection.

        Return:
        Prints Inspection results
        """
        strategy = self._strategy
        strategy.inspect(df)
    
if __name__=="__main__":
    # # Read data frame from a CSV file
    # df = pd.read_csv("../extracted_data/AmesHousing.csv")
    # # Strategy to be implemented by inspector
    # inspector = DataInspector(DataTypeInspectionStrategy())
    # # Executing the inspection to DataFrame df
    # inspector.execute_inspection(df)

    # # Changing the type of strategy to be implemented 
    # inspector.set_strategy(DataStatsInspectionStrategy())
    # inspector.execute_inspection(df)   # Executing the inspection to DataFrame df
    pass