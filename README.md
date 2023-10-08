# Image Stitching and Pixelation Project

## Overview

This Python project is designed to pixelate a target image and then stitch together a grid of random images to create a final output. The size of the grid is determined based on the dimensions of the pixelated target image.

The project uses the OpenCV library for image processing and manipulation.

## Prerequisites

Before running this project, ensure you have the following dependencies installed:

- Python (3.6 or higher)
- OpenCV (cv2)
- NumPy

You can install OpenCV and NumPy using pip:

```bash
pip install opencv-python numpy
Project Structure
The project consists of the following files and directories:

main.py: The main Python script that performs the pixelation, image stitching, and display.
images/: A directory containing random images to be used for stitching.
images/target_image.jpg: The target image you want to pixelate and stitch.
Usage
Place the target image you want to use in the images/ directory with the filename target_image.jpg.

Run the main.py script using the following command:

bash
Copy code
python main.py
The script will pixelate the target image and determine the grid size based on the pixelated image dimensions.

Random images from the images/ directory will be resized to match the grid size and stitched together.

The final stitched image will be displayed in a window.

Press any key to close the image window.

Customization
You can adjust the pixel_size variable in the main.py script to change the level of pixelation of the target image.

You can modify the images/ directory to include your own random images for stitching.

You can customize the screen width and height for displaying the final stitched image.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project was created as a demonstration of image processing techniques using OpenCV and can serve as a starting point for more complex image manipulation projects.
