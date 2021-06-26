# Mid-Term Assignment

### Assignment Questions

For this assignment, there were two parts: PCA for Image Reconstruction and a Short Creative Project. 

The objective of Question A was to use PCA for Image Reconstruction. Within this question, there were four subsections:

1. Compute PCA using 16x16 non-overlapping patches taken from the image. Reconstruct the whole image where each patch is reconstructed against *k* principal components. Store reconstructed images where *k=10* and *k=100*.
2. Store as 16x16 images the first ten principal components.
3. Explain how to select a better value for *k* and compute and store the corresponding reconstructed image.
4. Comment on the quality of reconstructed images found in the subsections above.

For Question B, I decided to try Image-Stitching. This question involved taking 2 images capturing an overlapping region and reconstruct a panoramic view using local descriptors.

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
    * Part 3
      * 'R732.jpg' is the reconstructed image for the new better value of k (k=732).
  
  * Question B
    * 'Left.jpg' is the first of the two images used for Image Stitching.
    * 'Right.jpg' is the second of the two images used for Image Stitching.
    * 'Panorama.jpg' is the resultant panoramic view image of the Image Stitching process.

## References
 * Scenery Image S: https://pixabay.com/photos/avenue-trees-away-walk-green-2215317/
  * Question A PCA Code - This video was used initially for understanding of PCA through MATLAB code (in greyscale): https://www.youtube.com/watch?v=nX7GAJULn60
  * Question B Image Stitching Images were taken from: 
    http://web.cecs.pdx.edu/~fliu/project/stitch/dataset.html?fbclid=IwAR0IdQ1duIavwUpksJvilfiYJavMCHD8LRCpdYj0YVkUlICY8rCNAd6n-H0
  * Question B Image Stitching Code - These tutorials were used as a basis for the Image Stitching code through SIFT: 
    * https://pylessons.com/OpenCV-image-stiching/
    * https://pylessons.com/OpenCV-image-stiching-continue/
  * A Practical Introduction to Computer Vision with OpenCV - Kenneth Dawson-Howe
