import os
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askdirectory

class Preprocess:
    def __init__(self):
        self.dataframes = []

    def select_folder(self):
        # Open a dialog to select a folder
        folder_path = askdirectory(title="Select a folder")
        
        if folder_path:
            return folder_path
        else:
            print("No folder was selected.")

    def read_files_from_directory(self, directory):
        """
        Read files from a directory and return a list of DataFrames.
        """
        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if filename.endswith(".csv"):
                df = pd.read_csv(file_path)
                self.dataframes.append(df)

            elif filename.endswith((".xlsx", ".xls")):
                df = pd.read_excel(file_path)
                self.dataframes.append(df)

            elif filename.endswith(".ods"):
                df = pd.read_excel(file_path, engine='odf')
                self.dataframes.append(df)


if __name__ == "__main__":
    # Initialize tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Create an instance of Preprocess
    preprocessor = Preprocess()
    
    # Call the select_folder method to start the process
    preprocessor.select_folder()

    # You can check if any dataframes were loaded
    if preprocessor.dataframes:
        print(f"{len(preprocessor.dataframes)} files were loaded successfully.")
    else:
        print("No files were loaded.")
