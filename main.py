import os
import sys
from image_processor import ImageProcessor
from folder_manager import FolderManager

def main():
    # Check if the input folder path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_folder_path>")
        return

    # Get the input folder path from the command-line argument
    input_folder_path = sys.argv[1]

    # Define the output folder path
    output_folder_path = "data/output"

    # Create instances of ImageProcessor and FolderManager
    image_processor = ImageProcessor(input_folder_path, output_folder_path)
    folder_manager = FolderManager(input_folder_path, output_folder_path)

    # Create the output folder structure
    folder_manager.create_folder_structure()

    # Process the images and move unique images to the output folder
    image_processor.process_images()

    print("Image processing completed successfully.")

if __name__ == "__main__":
    main()
