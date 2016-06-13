# Markable

#### This repository contains two task given by Markable, a start up based in Chicago
1. Humand Detector
2. Spring Framework

##### 1. Human Detector
To run the humandetector.py, follow this instruction: 

Input Path format must be: 'C:/CV_Task Examples/'    
Try to run this script as administrator if you have access issues  

Technique: Otsu's thresholding method with basic image processing    
Time Complexity: Less than 1 sec per image    
Accuracy: ~95%

Steps:    
1.Load the image and read it as a grayscale    
2.Downsample the image by 60%   
3.Threshold the image    
4.Consider forground pixels as human    
5.Label the image and find regionprops    
6.Draw bounding box around the interested regionprops    


##### 2. Spring Framework
To deploy this service, run client.java
