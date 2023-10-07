
import cv2 as cv 


# Input image
input_image = cv.imread('images/random_image_ (119).jpg')

# Desired size
desired_width = 800  # Replace with your desired width
desired_height = 600  # Replace with your desired height

# Resize input image to the desired size
resized_image = cv.resize(input_image, (desired_width, desired_height), interpolation=cv.INTER_LINEAR)

# Save the resized image
cv.imwrite('resized_image.jpg', resized_image)


# Desired "pixelated" size
w, h = (128,128)

# Resize input to "pixelated" size
temp = cv.resize(resized_image, (w, h), interpolation=cv.INTER_LINEAR)

# Initialize output image
output = cv.resize(temp, (800, 600), interpolation=cv.INTER_NEAREST)

cv.imshow('Input', resized_image)
cv.imshow('Output', output)

cv.waitKey(0)