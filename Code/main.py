from directory_explorer import DirectoryExplorer
from file_loader import FileLoader
from interface import Interface

class MainApp:
    def __init__(self):
        self.interface = Interface()
        self.directory_explorer = DirectoryExplorer()
        self.file_loader = FileLoader()

    def run(self, allowed_formats):
        """
        Main method that loads and processes the files.
        """
        folder_path = self.interface.select_folder()
        file_path = self.directory_explorer.find_files_according_to_formats(folder_path, allowed_formats)
        
        # Load and process files
        for file_path in self.directory_explorer.find_files_according_to_formats():
            print(f"File: {file_path}")
            
            # Load the file
            df = self.file_loader.load_file(file_path)
            
        

if __name__ == "__main__":
    allowed_formats = ['.csv', '.xlsx', '.ods', '.txt']

    # Create an instance of MainApp
    mainapp = MainApp()

    # Call the run method to start the process
    mainapp.run(allowed_formats)