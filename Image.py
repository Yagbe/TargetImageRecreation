import cv2 as cv

def shift_hue(image, target_hue):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    hsv_image[:, :, 0] = target_hue

    shifted_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    return shifted_image

def get_hue(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hue_values = hsv_image[:, :, 0]
    return hue_values

input_image = cv.imread('images/random_image_ (8).jpg')
resized_input = cv.resize(input_image, (800, 600), interpolation=cv.INTER_LINEAR)

desired_width = 800
desired_height = 600
resized_image = cv.resize(input_image, (desired_width, desired_height), interpolation=cv.INTER_LINEAR)

target_hue = 90  

result_image = shift_hue(resized_image, target_hue)
hue_values = get_hue(resized_image)
for row in hue_values:
    print(row) 

cv.imwrite('shifted_image.jpg', result_image)
cv.imshow('Shifted Image', result_image)
cv.imshow("Original",resized_input)
cv.waitKey(0)
cv.destroyAllWindows()
