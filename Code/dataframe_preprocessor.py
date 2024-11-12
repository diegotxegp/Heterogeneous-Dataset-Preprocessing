class DataframePreprocessor:
    def clean_dataframe(self, dataframe):
        """
        Cleans the dataframe by removing duplicate columns, merging fragmented columns, and dropping empty rows.
        :param dataframe: The dataframe to be cleaned.
        :return: The cleaned dataframe.
        """        
        # 1. Identify fragmented columns and merge fragmented rows
        #dataframe = self._clean_columns(dataframe)

        # 2. Remove duplicate columns (keep only the first occurrence)
        dataframe = dataframe.loc[:, ~dataframe.columns.duplicated()]
        
        # 3. Drop empty rows if any
        dataframe.dropna(how='all', inplace=True)
        
        # 4. Reset the index
        dataframe.reset_index(drop=True, inplace=True)
        
        return dataframe

    def merge_fragmented_columns(self, dataframe):
        """
        Merges fragmented columns by combining its parts into a single column.
        :param dataframe: The dataframe to be cleaned.
        :return: The cleaned dataframe.
        """
        # Current column names
        columns = dataframe.columns

        # Filter rows that contain any text matching the column names
        dataframe = dataframe[~dataframe.apply(lambda row: row.astype(str).str.contains('|'.join(columns))).any(axis=1)].reset_index(drop=True)

        merged_columns = dataframe.dropna().reset_index(drop=True)

        return merged_columns