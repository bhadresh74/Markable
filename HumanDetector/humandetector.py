import os
import shutil
import glob
import time

import preprocess
import boundingbox

# call findhumans to draw bounding box around the images
def findhumans(inputPath):
    outputPath = inputPath + "output/"

    # Create output directory
    if os.path.exists(outputPath):
        shutil.rmtree(outputPath)
        os.makedirs(outputPath)
    else:
        os.makedirs(outputPath)

    # Start running time
    start_time = time.time()

    print "All images are being processed..."

    # Load input images from the given input path
    for inputImage in glob.glob(inputPath + '*.jpg'):

        # Perform pre-processing on each input image
        heightImage, original, th3 = preprocess.perform(inputImage)

        # Draw bounding box on processed image and save it into output directory
        boundingbox.draw(heightImage, original, inputImage, outputPath, th3)

    print "Bounding box has been drawn on all images successfully !!"

    # Display running time
    print "Total run time: --- %s seconds ---" % (time.time() - start_time)