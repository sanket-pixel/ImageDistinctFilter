import os
from folder_manager import FolderManager
from image_utils import ImageUtils
import cv2
from tqdm import tqdm

class ImageProcessor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.folder_manager = FolderManager(input_folder, output_folder)

    def process_images(self):
        # Get the list of image files in the input folder
        image_files = self._get_image_files()

        # Create the output folder if it doesn't exist
        self.folder_manager.create_folder_structure()

        # Keep track of unique images
        unique_images = []
        
        # Initialize the progress bar
        progress_bar = tqdm(total=len(image_files), desc="Processing Images")

        # Iterate through the image files
        for k, image_file in enumerate(image_files):
            if not os.path.exists(image_file):
                progress_bar.update(1)  # Update the progress bar
                continue
            # Flag to determine if the image is unique
            unique = True
            # Compare the current image with unique images
            for unique_image in unique_images:
                if self._compare_images(image_file, unique_image):
                    unique = False
                    break
            # Move the image to the output folder if it's unique
            if unique:
                self.folder_manager.move_image(image_file, self._get_output_image_path(image_file))
                unique_images.append(image_file)
                
            progress_bar.update(1) 
                    
    def _compare_images(self, image1, image2):
        # Load the images using OpenCV
        img1 = cv2.imread(image1)
        img2 = cv2.imread(image2)
        
        if img1 is None or img2 is None :
            return True

        # Preprocess the images using ImageUtils functions
        preprocessed_img1 = ImageUtils.preprocess_image_change_detection(img1)
        preprocessed_img2 = ImageUtils.preprocess_image_change_detection(img2)
        
        # Check if the sizes of the preprocessed images match
        if preprocessed_img1.shape != preprocessed_img2.shape:
            # Resize the larger image to match the size of the smaller image
            if preprocessed_img1.size > preprocessed_img2.size:
                preprocessed_img1 = cv2.resize(preprocessed_img1, (preprocessed_img2.shape[1], preprocessed_img2.shape[0]))
            else:
                preprocessed_img2 = cv2.resize(preprocessed_img2, (preprocessed_img1.shape[1], preprocessed_img1.shape[0]))


        # Compare the preprocessed images using ImageUtils function
        score, _, _ = ImageUtils.compare_frames_change_detection(preprocessed_img1, preprocessed_img2, min_contour_area=100)

        # Adjust the score threshold based on your requirements
        score_threshold = 1000000

        # Return True if the images are similar (score is below the threshold), False otherwise
        return score < score_threshold

    def _get_image_files(self):
        # Get the list of image files in the input folder
        image_files = []
        for root, dirs, files in os.walk(self.input_folder):
            for file in files:
                if file.lower().endswith(('.png')):
                    image_files.append(os.path.join(root, file))
        return image_files

    def _get_output_image_path(self, image_file):
        # Get the output image path for a given input image path
        filename = os.path.basename(image_file)
        return os.path.join(self.output_folder, filename)
