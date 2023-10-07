
import cv2 as cv 


input_image = cv.imread('images/random_image_ (119).jpg')

desired_width = 800  
desired_height = 600  

resized_image = cv.resize(input_image, (desired_width, desired_height), interpolation=cv.INTER_LINEAR)

cv.imwrite('resized_image.jpg', resized_image)


w, h = (128,128)

temp = cv.resize(resized_image, (w, h), interpolation=cv.INTER_LINEAR)

output = cv.resize(temp, (800, 600), interpolation=cv.INTER_NEAREST)

cv.imshow('Input', resized_image)
cv.imshow('Output', output)

cv.waitKey(0)
