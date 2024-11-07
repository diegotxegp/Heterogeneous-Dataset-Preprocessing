import tkinter as tk
from tkinter.filedialog import askdirectory

class Interface:
    """
    Class responsible for handling the user interface.
    """
    def select_folder(self):
        """
        Open a dialog to select a folder.
        :return: Path to the selected folder.
        """
        # Open a dialog to select a folder
        folder_path = askdirectory(title="Select a folder")
        
        if folder_path:
            return folder_path
        else:
            print("No folder was selected.")