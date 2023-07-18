import os
import shutil


class FolderManager:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def create_folder_structure(self):
        # Create the required folder structure (input and output folders)
        os.makedirs(self.input_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)

    def copy_image(self, source_path, destination_path):
        # Copy the image from the source path to the destination path
        shutil.copy(source_path, destination_path)

    def move_image(self, source_path, destination_path):
        # Move the image from the source path to the destination path
        shutil.copy(source_path, destination_path)
