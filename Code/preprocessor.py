from directory_explorer import DirectoryExplorer
from file_loader import FileLoader
from interface import Interface

class Preprocessor:

    def preprocess():
        # Load and process files
        for file_path in self.directory_explorer.find_files_according_to_formats():
            print(f"File: {file_path}")
            
            # Load the file
            df = self.file_loader.load_file(file_path)