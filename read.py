import cv2 as cv

img = cv.imread('Images/cat.jpg') #imread() method takes the path to an image and returns that in a matrix of pixels

cv.imshow('Cat', img) #imshow() this displays the image in a new windows, it takes two parameters one for the name of the  window and the other for the matrix of pixels.

cv.waitKey(0)