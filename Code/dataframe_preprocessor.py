class DataframePreprocessor:
    def clean_dataframe(self, dataframe):
        """
        Cleans the dataframe by removing duplicate columns, merging fragmented columns, and dropping empty rows.
        :param dataframe: The dataframe to be cleaned.
        :return: The cleaned dataframe.
        """
        # 1. Remove duplicate columns (keep only the first occurrence)
        dataframe = dataframe.loc[:, ~dataframe.columns.duplicated()]
        
        # 2. Identify fragmented columns and merge fragmented rows
        dataframe = self._merge_fragmented_columns(dataframe)
        
        # 3. Drop empty rows if any
        dataframe.dropna(how='all', inplace=True)
        
        # 4. Reset the index
        dataframe.reset_index(drop=True, inplace=True)
        
        return dataframe

    def _merge_fragmented_columns(self, dataframe):
        """
        Merges fragmented columns by combining them into a single column.
        :param dataframe: The dataframe to be cleaned.
        :return: The cleaned dataframe.
        """
        # Check if columns contain fragmented values
        for column in dataframe.columns:
            # If there are empty cells in the column, attempt to combine data
            if dataframe[column].isnull().any():
                dataframe[column] = dataframe[column].ffill() + " " + dataframe[column].fillna("")
                dataframe[column] = dataframe[column].str.strip()  # Clean up extra spaces
            
        return dataframe