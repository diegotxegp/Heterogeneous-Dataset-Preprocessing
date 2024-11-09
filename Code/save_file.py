import pandas as pd

class SaveFile:
    """
    A class to save a DataFrame as a Parquet file.
    """
    def __init__(self, dataframe):
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("The provided object is not a DataFrame")
        self.dataframe = dataframe
    
    def dataframe_to_parquet(self, path):
        """
        Saves the DataFrame as a Parquet file.

        Parameters:
        path (str): The file path where the parquet file will be saved (including the file name and .parquet extension).
        Returns: None
        """
        try:
            self.dataframe.to_parquet(path, engine='pyarrow')
            print(f"File successfully saved at {path}.")
        except ImportError as e:
            print("You need to install pyarrow to save in Parquet format.")
            raise e
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            raise e
