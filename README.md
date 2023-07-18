# Image Distinct Filter

Image Distinct Filter is a Python application that helps remove duplicate and similar images from a given image folder. It uses image processing techniques to compare images and retain only the unique ones.

## Features

- Removes duplicate and similar images from a folder
- Retains only distinct enough images
- Provides a customizable score threshold for image comparison
- Supports custom image preprocessing and contour area threshold

## Folder Structure

The project has the following folder structure:
```
├── folder_manager.py # Class to manage folders and image operations
├── image_processor.py # Class to process and filter images
├── image_utils.py # Utility functions for image processing
├── main.py # Entry point of the application
├── README.md # Documentation and instructions
└── requirements.txt # Required dependencies
```
## Code Explanation

The code in this project consists of the following classes:

- `ImageProcessor`: This class is responsible for processing and filtering images. It uses the `FolderManager` class to manage folders and image operations. The `ImageUtils` module provides utility functions for image processing. The class has a `process_images()` method that iterates through the input images, compares them, and moves the unique images to the output folder.

- `FolderManager`: This class handles folder management and image operations. It provides methods to create the required folder structure, copy or move images between folders, and generate output image paths.

- `ImageUtils`: This module contains utility functions for image processing. It includes functions for drawing color masks, preprocessing images for change detection, and comparing frames using contour analysis.

The general flow of the code is as follows:

1. The `main.py` script serves as the entry point for the application. It takes the input folder path as a command-line argument and initiates the image processing flow.

2. The `ImageProcessor` class is responsible for processing and filtering images. It creates an instance of the `FolderManager` class to manage folders and image operations.

3. The `ImageProcessor` class's `process_images()` method is called, which performs the following steps:
   - Retrieves the list of image files in the input folder.
   - Creates the output folder if it doesn't exist.
   - Iterates through the image files.
   - Compares the current image with the remaining images to determine uniqueness.
   - Moves the unique images to the output folder.

4. The `_compare_images()` method in the `ImageProcessor` class compares two images using the utility functions from `ImageUtils`. It preprocesses the images, calculates the score based on contour analysis, and determines if the images are similar based on a score threshold.

5. The `FolderManager` class manages folders and image operations. It provides methods to create the required folder structure, copy or move images between folders, and generate output image paths.

6. The `ImageUtils` module contains utility functions for image processing. It includes functions to draw color masks, preprocess images for change detection, and compare frames using contour analysis.

The code follows a modular structure, separating the responsibilities into different classes and functions. The `ImageProcessor` class orchestrates the image processing flow, leveraging the functionalities provided by the `FolderManager` class for folder management and the `ImageUtils` module for image processing tasks.


## Getting Started

To get started with the Image Distinct Filter, follow these steps:

1. Clone the repository: `git clone https://github.com/sanket-pixel/ImageDistinctFilter.git`
2. Navigate to the project directory: `cd ImageDistinctFilter`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use the Image Distinct Filter, follow these steps:

1. Place your input images in the specified input folder.
2. Run the `main.py` script: `python main.py <input_folder_path>`
   - Replace `<input_folder_path>` with the path to your input folder.
3. The script will process the images, remove duplicates, and save the distinct images in the output folder.
4. You can find the output images in the specified output folder.

Note: Adjust the score threshold and other parameters in the `ImageProcessor` class based on your requirements.



