from interface import Interface
from directory_explorer import DirectoryExplorer
from file_loader import FileLoader
from dataframe_preprocessor import DataframePreprocessor
from save_file import SaveFile

from parameters import folder_path

class MainApp:

    def run(self):
        """
        Main method that loads and processes the files.
        """
        #interface = Interface()
        #folder_path = interface.select_folder()

        directory_explorer = DirectoryExplorer()
        file_path = directory_explorer.find_files_according_to_formats(folder_path)
        
        file_loader = FileLoader()
        df = file_loader.load_files(file_path)

        dataframe_preprocessor = DataframePreprocessor()
        df = dataframe_preprocessor.clean_dataframe(df)

        save_file = SaveFile(df)
        save_file.dataframe_to_parquet("output.parquet")
            
        

if __name__ == "__main__":
    # Create an instance of MainApp
    mainapp = MainApp()

    # Call the run method to start the process
    mainapp.run()