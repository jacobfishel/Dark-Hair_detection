# import numpy as np
# import cv2

# #read the image in normal and grayscale
# # image = cv2.imread(r"static\images\man.jpg", cv2.IMREAD_UNCHANGED)
# # imageGray = cv2.imread(r"static\images\man.jpg", cv2.IMREAD_GRAYSCALE)


# #get the dimensions to eventually resize images to fit screen
# # height = int(image.shape[0] / 7)
# # width = int(image.shape[1] / 7)

# # #resize images
# # image = cv2.resize(image, (width, height))
# # imageGray = cv2.resize(imageGray, (width, height))

# # #show images to the screen
# # cv2.imshow("Image", image)
# # cv2.imshow("Image Gray", imageGray)

# #cropping the images to just get the man
# # cropMan = image[125: 485, 255: 600]
# # cropManGray = imageGray[125: 485, 255: 600]

# #show the cropped images
# # cv2.imshow("Cropped Man", cropMan)
# # cv2.imshow("Cropped Man Gray", cropManGray)

# #Drawing a box around the man
# # manWithBox = cv2.rectangle(image, (255, 125), (600, 485), (255, 0, 0), 3)
# # manWithBoxGray = cv2.rectangle(imageGray, (255, 125), (600, 485), (1, 255, 0), 3)

# #Show the boxed man
# # cv2.imshow("Boxed man", manWithBox)
# # cv2.imshow("Boxed man Gray", manWithBoxGray)

# #IMAGE THRESHOLDING
# # _, thresh = cv2.threshold(imageGray, 127, 255, cv2.THRESH_BINARY)
# # adaptiveThresh = cv2.adaptiveThreshold(imageGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
# # cv2.imshow("Thresholded img", thresh)
# # cv2.imshow("Adaptive Thresholded img", adaptiveThresh)


# '''NEW IMAGE TO GET BETTER THRESHOLDING'''
# image = cv2.imread(r"static\images\people-walking.jpg", cv2.IMREAD_UNCHANGED)
# imageGray = cv2.imread(r"static\images\people-walking.jpg", cv2.IMREAD_GRAYSCALE)

# #Apply gaussian blur to smooth out image
# image = cv2.GaussianBlur(image, (5, 5), 0)
# imageGray = cv2.GaussianBlur(imageGray, (5, 5), 0)

# # get the dimensions to eventually resize images to fit screen
# height = int(image.shape[0] / 2)
# width = int(image.shape[1] / 2)



# #threshold this img. basic, then adaptive
# _, thresh = cv2.threshold(imageGray, 100, 255, cv2.THRESH_BINARY)
# adaptiveThresh = cv2.adaptiveThreshold(imageGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, -5)
# adaptiveThreshGaussian = cv2.adaptiveThreshold(imageGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, -5)

# method = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)


# # cv2.imshow("Image", imageGray)
# cv2.imshow("Thresholded", thresh)
# # cv2.imshow("Adaptive", adaptiveThresh)
# # cv2.imshow("Gaussian", adaptiveThresh)
# cv2.imshow("Gaussian", method)





# '''Page image'''

# # image = cv2.imread(r"static\images\page.jpg", cv2.IMREAD_UNCHANGED)
# # imageGray = cv2.imread(r"static\images\page.jpg", cv2.IMREAD_GRAYSCALE)

# # # get the dimensions to eventually resize images to fit screen
# # # height = int(image.shape[0] / 2)
# # # width = int(image.shape[1] / 2)

# # # #resize images
# # # image = cv2.resize(image, (width, height))
# # # imageGray = cv2.resize(imageGray, (width, height))

# # image = image[0: 300, 0: 300 ]
# # imageGray = imageGray[0: 300, 0: 300 ]

# # #show images to the screen
# # # cv2.imshow("Image", image)
# # # cv2.imshow("Image Gray", imageGray)

# # #threshold this img. basic, then adaptive
# # _, thresh = cv2.threshold(imageGray, 127, 255, cv2.THRESH_BINARY)
# # adaptiveThresh = cv2.adaptiveThreshold(imageGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# # adaptiveThreshGaussian = cv2.adaptiveThreshold(imageGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)



# # cv2.imshow("Image", imageGray)
# # cv2.imshow("Thresholded", thresh)
# # cv2.imshow("Adaptive", adaptiveThresh)
# # cv2.imshow("Gaussian", adaptiveThreshGaussian)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread(r"static\images\map.png", cv2.IMREAD_GRAYSCALE)
width = img.shape[0] * 3
height = img.shape[1] * 3

img = cv2.resize(img, dsize = (width, height))
adaptiveThreshGaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)
# _, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

cv2.imshow("image", adaptiveThreshGaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()