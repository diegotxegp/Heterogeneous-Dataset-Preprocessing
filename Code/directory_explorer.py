import os

from parameters import allowed_formats

class DirectoryExplorer:
    """
    Class responsible for traversing directories and finding files according to the given formats.
    """
    def find_files_according_to_formats(self, base_directory) -> list:
        """
        Walk through all directories and subdirectories, yielding files according to the given formats.
        :yield: File path.
        """
        # Walk through all directories and subdirectories
        file_paths = []
        for root, dirs, files in os.walk(base_directory):
            for file in files:
                # Check if the file has a valid extension
                if file.endswith(allowed_formats):
                    file_paths.append(os.path.join(root, file))
        return file_paths

