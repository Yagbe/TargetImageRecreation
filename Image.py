import cv2 as cv
import numpy as np
import random

def shift_hue(image, target_hue):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Set the hue channel to the target hue
    hsv_image[:, :, 0] = target_hue

    shifted_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    return shifted_image
def shift_hue_and_saturation(image, target_hue, target_saturation):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Shift hue
    hsv_image[:, :, 0] = target_hue

    # Shift saturation
    hsv_image[:, :, 1] = target_saturation

    shifted_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    return shifted_image
def crop_to_squares(image, square_size):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    height, width, _ = image.shape

    min_dim = min(height, width)
    x_start = (width - min_dim) // 2
    y_start = (height - min_dim) // 2

    cropped_image = image[y_start:y_start + min_dim, x_start:x_start + min_dim]

    cropped_image = cv.resize(cropped_image, (square_size, square_size), interpolation=cv.INTER_LINEAR)

    return cropped_image

def crop_and_resize(image, desired_width, desired_height):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    height, width, _ = image.shape

    crop_x = (width - desired_width) // 2
    crop_y = (height - desired_height) // 2

    cropped_image = image[crop_y:crop_y + desired_height, crop_x:crop_x + desired_width]

    return cropped_image

def get_hue(image):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    return hue_values

def stitch_images_nxn(images, n):
    num_images = len(images)

    if num_images == 0:
        print("Error: No images provided.")
        return None

    height, width, _ = images[0].shape

    for i in range(num_images):
        image = images[i]
        if image is None:
            print(f"Error: Failed to load image {i}.")
            return None
        images[i] = cv.resize(image, (width, height), interpolation=cv.INTER_LINEAR)

    canvas_height = height * n
    canvas_width = width * n
    stitched_image = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    for i in range(n):
        for j in range(n):
            image_index = i * n + j

            if image_index < num_images:
                image = images[image_index]
                x_start = j * width
                x_end = (j + 1) * width
                y_start = i * height
                y_end = (i + 1) * height
                stitched_image[y_start:y_end, x_start:x_end] = image

    return stitched_image

def pixelate_image(image, pixel_size):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    height, width, _ = image.shape

    small_image = cv.resize(image, (1280 // pixel_size, 1060 // pixel_size), interpolation=cv.INTER_LINEAR)

    pixelated_image = cv.resize(small_image, (1080, 800), interpolation=cv.INTER_NEAREST)

    return pixelated_image

def calculate_num_subimages(total_pixels, subimage_pixels):
    return total_pixels // subimage_pixels

def generate_subimages(image, num_subimages):
    if image is None:
        print("Error: Failed to load the image.")
        return None

    height, width, _ = image.shape

    subimage_height = height // num_subimages
    subimage_width = width // num_subimages

    subimages = []

    for i in range(num_subimages):
        for j in range(num_subimages):
            y_start = i * subimage_height
            y_end = (i + 1) * subimage_height
            x_start = j * subimage_width
            x_end = (j + 1) * subimage_width

            subimage = image[y_start:y_end, x_start:x_end]
            subimages.append(subimage)

    return subimages
image_path = f'target_image.jpg'
image = cv.imread(image_path)

if image is not None:
    # Load your target pixelated image
    pixel_size = 20 
    pixelated_image = pixelate_image(image, pixel_size)

    target_height, target_width, _ = pixelated_image.shape

    total_pixels = target_height * target_width

    n = calculate_num_subimages(total_pixels, pixel_size * pixel_size)
    
    screen_width = 800
    screen_height = 600

    resized_images = []

    for i in range(n):
        image_path = f'images/rimage ({random.randint(2, 200)}).jpg'
        image = cv.imread(image_path)
        
        if image is not None:
            resized_image = cv.resize(image, (target_width, target_height), interpolation=cv.INTER_LINEAR)
            resized_images.append(resized_image)
        else:
            print(f"Error: Failed to load image {i}.")

    stitched_image = stitch_images_nxn(resized_images, int(n**0.5))

    stitched_image = cv.resize(stitched_image, (target_width, target_height), interpolation=cv.INTER_LINEAR)
# Get the hue values from the pixelated image
target_hue = get_hue(pixelated_image)

# Shift the hue of the stitched image while keeping saturation at 50%
shifted_image = shift_hue_and_saturation(stitched_image, target_hue, 127)  # 127 for 50% saturation

cv.imshow(f'Stitched Image ({target_width}x{target_height})', shifted_image)
cv.imshow("Pixelated Target Image", pixelated_image)
cv.imwrite("OutputImage.jpg", shifted_image)
cv.waitKey(0)
cv.destroyAllWindows()
