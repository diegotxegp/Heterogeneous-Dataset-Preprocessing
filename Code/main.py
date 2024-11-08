from interface import Interface
from directory_explorer import DirectoryExplorer
from file_loader import FileLoader
from dataframe_preprocessor import DataframePreprocessor

class MainApp:

    def run(allowed_formats):
        """
        Main method that loads and processes the files.
        """
        interface = Interface()
        folder_path = interface.select_folder()

        directory_explorer = DirectoryExplorer()
        file_path = directory_explorer.find_files_according_to_formats(folder_path, allowed_formats)
        
        file_loader = FileLoader()
        df = file_loader.concatenate_files(file_path)

        dataframe_preprocessor = DataframePreprocessor()
        df = dataframe_preprocessor.clean_dataframe(df)
            
        

if __name__ == "__main__":
    ########################################################################
    allowed_formats = ['.csv', '.xlsx', '.ods', '.txt']
    ########################################################################

    # Create an instance of MainApp
    mainapp = MainApp()

    # Call the run method to start the process
    mainapp.run(allowed_formats)