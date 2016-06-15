import cv2
import numpy as np
from skimage.measure import label
from skimage.measure import regionprops
import os

# Draw bounding box around the image
def draw(heightImage, original, inputImage, outputPath, th3):

    # Label image regions
    label_image = label(th3)

    # Find interested region
    findRegions = regionprops(label_image)
    areaRegion = [[0, 0, 0, 0, 0]]

    # Iterate through all possible regions
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