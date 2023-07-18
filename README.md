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


## Questions and Answers

Please find below the answers to the questions:

### What did you learn after looking at our dataset?

After analyzing the dataset, the following observations were made:

- The dataset consists of camera images captured from cameras installed inside the parking lot.
- The dataset showcases various scenarios, including changing weather conditions, different times of the day, and variations in crowd and car density.
- The dataset provides a realistic representation of the challenges faced in autonomous parking.
- The diversity in weather conditions, time of day, and crowd and car variation helps in training deep learning models to handle different environmental conditions and challenges.

### How does your program work?

The program works by utilizing image processing techniques and contour analysis to identify and filter out duplicate and similar images. Here's an overview of the program's workflow:

1. The program reads the images from the input folder.
2. It applies preprocessing techniques to enhance the images and remove noise.
3. The program compares each image with the remaining images using contour analysis and assigns scores based on contour areas.
4. Based on a user-defined score threshold, the program determines if the images are similar or unique.
5. The program moves the unique images to the output folder, ensuring that only distinct enough images remain.

### What values did you decide to use for input parameters and how did you find these values?

The value for the score threshold was chosen to be 1000000. Firstly I gave two similar images which gave a score of zero. Then I gave two entirely distinct images, after which I got a value over 2000000. This gave me an intuitive range of these values. Then I chose several values like 1000, 10000 etc and finally tried 1000000 and observed that this value preserved all distinct images (visually) and removed duplicates. 

### What would you suggest to implement to improve data collection of unique cases in the future?

To improve data collection of unique cases in the future, consider the following suggestions:

- Collect images from diverse parking lot scenarios, including different layouts, sizes, and structures.
- Include images captured in extreme weather conditions, such as heavy rain, snow, or fog.
- Capture images showcasing a wide range of vehicle types, including different car models, sizes, and shapes.
- Include challenging cases such as narrow parking spaces, complex intersections, and crowded parking lots.

By collecting a diverse and comprehensive dataset that covers a wide range of unique cases, the models trained on this data will have better generalization and performance when applied to real-world autonomous parking scenarios.

### Any other comments about your solution?

The solution provided is a practical approach to filter and retain distinct enough images from a given dataset. It utilizes image processing techniques and contour analysis for image comparison. However, further enhancements can be made by exploring advanced techniques such as deep learning-based image similarity metrics or feature extraction approaches.

The solution serves as a starting point for image filtering and provides the foundation for building more sophisticated systems for autonomous parking using deep learning.
