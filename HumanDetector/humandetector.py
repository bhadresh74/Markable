import cv2
import numpy as np
from skimage.measure import label
from skimage.measure import regionprops
import os
import shutil
import glob
import time

print "---------------"
print "INSTRUCTIONS:"
print "---------------"
print "Input Path format must be: 'C:/CV_Task Examples/'"
print "Try to run this script as administrator if you have access issues\n"

# Take input path from user
inputPath = input("Enter the path of your image files:")
outputPath = inputPath+"output/"

# Create output directory
if os.path.exists(outputPath):
    shutil.rmtree(outputPath)
    os.makedirs(outputPath)
else:
    os.makedirs(outputPath)

# Function to draw bounding box around human
def humanDetector(inputPath):

    # Load input images from the given input path
    for inputImage in glob.glob(inputPath + '*.jpg'):
        original = cv2.imread(inputImage)
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

        # Label image regions
        label_image = label(th3)

        # Find interested region
        findRegions = regionprops(label_image)
        areaRegion = [[0, 0, 0, 0, 0]]

        for region in findRegions:

            # Ignore small patches
            if region.area < 100:
                continue

            # Add all interested regions into an array
            minr, minc, maxr, maxc = region.bbox
            areaRegion.append([minr, minc, maxr, maxc, (maxc - minc) * (maxr - minr)])

        # Check width and height of largest bounding box
        areaRegion = np.delete(areaRegion, (0), axis=0)
        row, col = zip(*np.where(areaRegion == np.amax(areaRegion)))[0]
        finalWidth = (areaRegion[row][3] - areaRegion[row][1])
        finalHeight = (areaRegion[row][2] - areaRegion[row][0])

        # If largest bounding box has almost same height as image then draw a bounding box
        # If not then combine various boxes around the human and draw a new bounding box
        if (heightImage - finalHeight) < 100:
            cv2.rectangle(original, (areaRegion[row][1], areaRegion[row][0]),
                          (areaRegion[row][1] + finalWidth, areaRegion[row][0] + finalHeight), (0, 0, 255), 2)
            cv2.imwrite(outputPath + os.path.splitext(os.path.basename(inputImage))[0] + '.jpg', original)
        else:
            minX = areaRegion.min(axis=0)[1]
            minY = areaRegion.min(axis=0)[0]
            maxX = areaRegion.max(axis=0)[3]
            maxY = areaRegion.max(axis=0)[2]
            finalWidth = maxX - minX
            finalHeight = maxY - minY
            cv2.rectangle(original, (minX, minY), (minX + finalWidth, minY + finalHeight), (0, 0, 255), 2)
            cv2.imwrite(outputPath + os.path.splitext(os.path.basename(inputImage))[0] + '.jpg', original)

if __name__ == '__main__':

    # Check for run time
    start_time = time.time()

    # Call human detector
    humanDetector(inputPath)
    print "Total run time: --- %s seconds ---" % (time.time() - start_time)