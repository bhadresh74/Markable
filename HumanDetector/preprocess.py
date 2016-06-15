import cv2
import numpy as np

# Perform pre-processing
def perform(inputImage):

    # Make a copy of original image
    original = cv2.imread(inputImage)

    # Read image as a grayscale
    img = cv2.imread(inputImage, 0)

    # downsample the image
    img = cv2.resize(img, (0, 0), fx=0.6, fy=0.6)
    original = cv2.resize(original, (0, 0), fx=0.6, fy=0.6)
    heightImage, widthImage = img.shape

    # Threshold the image
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Make the background white and set human pixels as black
    imarray = np.array(th3)
    whitePixels = 0
    blackPixels = 0
    row = len(imarray)
    col = len(imarray[1])
    for i in range(row):
        for j in range(col):
            if imarray[i][j] == 255:
                whitePixels += 1
            else:
                blackPixels += 1
    if whitePixels > blackPixels:
        th3 = ~th3

    # Return height of original image, original image, pre-processed image
    return [heightImage,original,th3]
