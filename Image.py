import cv2 as cv
import random
import numpy as np

def shift_hue(image, target_hue):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hsv_image[:, :, 0] = target_hue
    shifted_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
    return shifted_image

def get_hue(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    return hue_values

def stitch_images_nxn(images, n):
    num_images = len(images)
    
    height, width, _ = images[0].shape

    for image in images[1:]:
        image = cv.resize(image, (width, height), interpolation=cv.INTER_LINEAR)

    canvas_height = height * n
    canvas_width = width * n
    stitched_image = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    for i in range(n):
        for j in range(n):
            image_index = i * n + j
            image = images[image_index]
            x_start = j * width
            x_end = (j + 1) * width
            y_start = i * height
            y_end = (i + 1) * height
            stitched_image[y_start:y_end, x_start:x_end] = image

    return stitched_image

def shift_hue_for_pixel(images, target_image):
    n = len(images)
    height, width, _ = target_image.shape
    shifted_images = []

    for i in range(n):
        image = images[i]
        shifted_image = np.zeros_like(image)

        for y in range(height):
            for x in range(width):
                target_pixel_hue = target_image[y, x, 0]
                shifted_pixel_image = shift_hue(image[y:y+1, x:x+1], target_pixel_hue)
                shifted_image[y:y+1, x:x+1] = shifted_pixel_image

        shifted_images.append(shifted_image)

    return shifted_images
n = 15
images = [cv.imread(f'images/random_image_ ({random.randint(2, 120)}).jpg') for _ in range(n * n)]

desired_width = 400
desired_height = 300

resized_images = [cv.resize(image, (desired_width, desired_height), interpolation=cv.INTER_LINEAR) for image in images]

stitched_image = stitch_images_nxn(resized_images, n)
shift_hue(stitched_image,167)
screen_width = 800
screen_height = 600
stitched_image = cv.resize(stitched_image, (screen_width, screen_height), interpolation=cv.INTER_LINEAR)

cv.imshow(f'Stitched Image ({n}x{n})', stitched_image)
cv.waitKey(0)
cv.destroyAllWindows()

