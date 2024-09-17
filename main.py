import cv2
import numpy as np

#read the image in normal and grayscale
image = cv2.imread(r"static\images\man.jpg", cv2.IMREAD_UNCHANGED)
imageGray = cv2.imread(r"static\images\man.jpg", cv2.IMREAD_GRAYSCALE)

#get the dimensions to eventually resize images to fit screen
height = int(image.shape[0] / 7)
width = int(image.shape[1] / 7)

#resize images
image = cv2.resize(image, (width, height))
imageGray = cv2.resize(imageGray, (width, height))

#show images to the screen
# cv2.imshow("Image", image)
# cv2.imshow("Image Gray", imageGray)

#cropping the images to just get the man
cropMan = image[125: 485, 255: 600]
cropManGray = imageGray[125: 485, 255: 600]

#show the cropped images
# cv2.imshow("Cropped Man", cropMan)
# cv2.imshow("Cropped Man Gray", cropManGray)

#Drawing a box around the man
manWithBox = cv2.rectangle(image, (255, 125), (600, 485), (255, 0, 0), 3)
manWithBoxGray = cv2.rectangle(imageGray, (255, 125), (600, 485), (1, 255, 0), 3)

#Show the boxed man
# cv2.imshow("Boxed man", manWithBox)
# cv2.imshow("Boxed man Gray", manWithBoxGray)


cv2.waitKey(0)
cv2.destroyAllWindows()
