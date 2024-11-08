import os
import pandas as pd

class FileLoader:
    """
    Class responsible for loading datasets based on their file type.
    """
    def concatenate_files(self, file_paths):
        """
        Concatenates the dataframes of the files into a single dataframe.
        :param file_paths: List of paths to the files.
        :return: pandas DataFrame with all the files content.
        """
        df = pd.DataFrame()

        for filepath in file_paths:
            file_df = self._load_file(filepath)
            df = pd.concat([df, file_df], ignore_index=True)

        return df

    def _load_file(self, filepath):
        """
        Loads the dataframe of the file based on its file extension.
        :param file_paths: List of paths to the files.
        :return: pandas DataFrame with the file content.
        """
        _, ext = os.path.splitext(filepath)
        
        if ext == '.csv':
            delimiter = self.detect_delimiter(filepath)
            return pd.read_csv(filepath , delimiter=delimiter)
        elif ext in ['.xls', '.xlsx']:
            return pd.read_excel(filepath)
        elif ext == '.ods':
            return pd.read_excel(filepath, engine='odf')
        elif ext == '.txt':
            delimiter = self.detect_delimiter(filepath)
            return pd.read_csv(filepath, delimiter=delimiter)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
        
    def detect_delimiter(self, filepath):
        """
        Detects the delimiter used in a CSV file by checking the first line.
        :param filepath: Path to the CSV file.
        :return: The detected delimiter (either ',' or ';').
        """
        with open(filepath, 'r') as file:
            first_line = file.readline()
            # Count occurrences of different delimiters
            comma_count = first_line.count(',')
            semicolon_count = first_line.count(';')
            
            # Determine which delimiter is used
            if comma_count > semicolon_count:
                return ','
            elif semicolon_count > comma_count:
                return ';'
            else:
                raise ValueError("Could not determine the delimiter; counts are equal or both are zero.")