# Sinéad Galbraith CS7GV1-Computer Vision Mid Term Assignment

### Setup

The code for this assignment was written in Python through PyCharm. Opencv2 and Numpy need to be installed and imported in order for both pieces of code to run (these packages need to be added on PyCharm too (if applicable)). All Images corresponding to this assignment can be found in the Images folder. The images are read from and written into this folder in the code also. 

The Images folder includes the following images:
  * Question A
    * Part 1
      * 'S.jpg' is the original Scenery Image.
      * 'R10.jpg' is the reconstructed image when k=10.
      * 'R100.jpg' is the reconstructed image when k=100.
    * Part 2
      * 'PC{0-10}.jpg' are the first 10 principal components.
      * 'PC{0-10}Rescaled.jpg' are the first 10 principal components scaled up.
  
  * Question B
    * 'Left.jpg' is the first of the two images used for Image Stitching.
    * 'Right.jpg' is the second of the two images used for Image Stitching.
    * 'Panorama.jpg' is the resultant panoramic view image of the Image Stitching process.

## Question A

### Part 1

The code for this part of Question A can be found in PCA.py. This code has been fully commented explaining the process of PCA (Please not also that the code may take a couple of minutes to run).

***Note that within the code, to change the value of k, the variable 'k' (found on line 7 of the PCA.py file) must be changed.***

The original scenery image S used can be seen below:
<p align="center">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/S.jpg" width="670" height="446">
</p>

The output reconstructed images for K=10 and K=100 can be see below also:

<p align="center">
  K =10 :
</p>
<p align="center">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/R10.jpg" width="670" height="446">
</p>

<p align="center">
  K =100 :
</p>
<p align="center">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/R100.jpg" width="670" height="446">
</p>

All three of these images can be found in the Images folder.

### Part 2

<p align="center">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC0.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC1.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC2.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC3.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC4.jpg" width="120" height="120">
 </p>
<p align="center">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC5.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC6.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC7.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC8.jpg" width="120" height="120">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/PC9.jpg" width="120" height="120">
 </p>

### Part 3

### Part 4

## Question B

The code for Question B can be found in Panorama.py. This code has been fully commented explaining the process of Image Stitching here. 

### Panoramic View Image

The original images used for the Panoramic photo can be seen below: 

<p align="center">
<img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/Left.jpg" width="470" height="311">
<img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/Right.jpg" width="470" height="311">
</p>

The reconstructed panoramic image can be seen below also: 

<p align="center">
<img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/Panorama.jpg" width="1200" height="397">
</p>

All three of these images can be found in the Images folder.

I will now explain the methods and processes that I used to make this panoramic view image from the two above images.

After reading in the two separate images and converting them to greyscale, the first step in the process was to identify the features in both images. To do this, I used the Scale Invariant Feature Transform (SIFT) function that comes with OpenCV. SIFT identifies and extracts keypoints and descriptors based on the features within an image. The image is first considered at a number of scales at the same time and potential features are detected. To identify more reliable features or keypoints, the Difference of Gaussians (DoG) is taken across the number of scales. Using the DoG, keypoints are identified by looking for consistencies across the various scales. Once the potential keypoints have been identified, they must be further verified to ensure they are correct. This is done through two tests. The first test takes the local contrast in an area and checks the associated quadratic graph. If the quadratic is closer to a straight line, the contrast is low and so the keypoint is considered to be inaccurate and is therefore discarded. The second test checks if the keypoint is on an edge. The closer to an edge that a feature is, the larger the principal curvature of the DoG will be. However, the perpendicular curvature will be small. To pass the second test, the ratio of the principal curvature must be below a certain threshold, if not, the keypoint will be discarded. At the end of this step, the accurate keypoints have been identified. Finally, once we have the keypoints identified, the descriptors need to be identified also. The descriptors describe the region around the keypoint. This means that each keypoint can be compared with every other keypoint. To identify the descriptors, the gradients and orientations are taken for the area around each keypoint and a weighted histogram is made for each of the orientations. From here, the descriptor is made by mapping the orientation of every keypoint to the associated histogram bin. 

At this stage, the SIFT process is complete. Next, the keypoints within each of the images need to be matched (if appropriate). To do this, I use another OpenCV function called BFMatcher (Brute-Force Matcher). This matcher works by taking a feature in one image and comparing it to all features in the other image. The features are matched using a distance function and all matches are returned in an array. After this, the function knnMatch() is called. This function uses the array of matches to find the closest 'k' matches, in this case k=2 so the top two matches for each feature will be returned and stored in an array. Once we have the array of matches, we need to distinguish the exact matches. For this reason, the matches array is further filtered. Every match needs to satisfy a ratio, if the ratio is not satisfied, the match is not considered strong enough to be kept and so it will be discarded.

Once all matches have been filtered through, providing that there is more than a minimum number of 'goodMatches', the two images now need to be aligned. In order to align the images, a homorgraphy matrix needs to be obtained for the transformation. The images need to be aligned to the same orientation and using the homography matrix, both images are transformed to the same perspective. Once this has been done, the stitching of the image can begin. 

Using the warpPerspective() function, the 'Right' image is taken first. From here, the perspective of the image is changed so that the 'Left' image can be added onto it. Once the warpPerspective() function has been performed on the 'Right' image, the 'Left' image is applied to this new image and so the whole Panoramic view can be seen as one image.


## References
 * Scenery Image S: https://pixabay.com/photos/avenue-trees-away-walk-green-2215317/
  * Question A PCA Code - This video was used initially for understanding of PCA through MATLAB code (in greyscale): https://www.youtube.com/watch?v=nX7GAJULn60
  * Question B Image Stitching Images were taken from: 
    http://web.cecs.pdx.edu/~fliu/project/stitch/dataset.html?fbclid=IwAR0IdQ1duIavwUpksJvilfiYJavMCHD8LRCpdYj0YVkUlICY8rCNAd6n-H0
  * Question B Image Stitching Code - These tutorials were used as a basis for the Image Stitching code through SIFT: 
    * https://pylessons.com/OpenCV-image-stiching/
    * https://pylessons.com/OpenCV-image-stiching-continue/
  * A Practical Introduction to Computer Vision with OpenCV - Kenneth Dawson-Howe
