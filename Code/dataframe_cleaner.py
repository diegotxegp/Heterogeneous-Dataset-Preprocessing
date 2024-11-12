class DataframeCleaner:
    def clean_dataframe(self, dataframe):
        """
        Cleans the dataframe by removing duplicate columns, merging fragmented columns, and dropping empty rows.
        :param dataframe: The dataframe to be cleaned.
        :return: The cleaned dataframe.
        """
        columns = dataframe.columns

        # Filter rows that contain any text matching the column names
        dataframe = dataframe[~dataframe.apply(lambda row: row.astype(str).str.contains('|'.join(columns))).any(axis=1)].reset_index(drop=True)

        df_cleaned = dataframe.dropna().reset_index(drop=True)

        return df_cleaned