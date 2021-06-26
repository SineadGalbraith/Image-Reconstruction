# Question A

### Part 1

The code for this part of Question A can be found in PCA.py. This code has been fully commented explaining the process of PCA (please note also that the code may take a couple of minutes to run).

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

To compute the PCA of this image at the various k values, I followed the following process:

Initially, the image is read in and split into 16x16 patches with all three channels. Then, for simplicity, the patch is transformed from 16x16x3 to a vector of 768x1. This vector is then adjusted by its mean. To do this, the mean is found for all 3 channels in the patch and subtracted from the original data. The mean-adjusted vector is then added to an array of vectors. This process is repeated for every 16x16 patch within the image; the resulting array contains all of the patches in vector form.

Once this array of vectors has been created and all of the patches have been added to it, the covariance matrix is found. To do this, I use the NumPy function cov(). The resultant covariant matrix is then used to find all of the Eigen Vectors and Values. From here, depending on the value of k, the number of Eigen Vectors found in the previous step is reduced to match the value of k (i.e only k columns of the Eigen Vectors are used). 

Once the reduced vectors have been found, the vector array column containing all of the patch data as well as the reduced vectors is passed to a function called getUncompressedData. This function aims to find the data needed to reconstruct the image. Within this function, every patch is taken and compressed. This is done by multiplying the transpose of the patch and the transpose of the reduced vectors. Immediately after this step, the data is uncompressed. To do this, the compressed data is multiplied by the reduced vectors. Seeing as the mean was subtracted from the data earlier on, the data now needs to be readjusted by adding the mean back on. This process is completed by calling a function addMean which adds each respective patch mean onto the uncompressed data. 

Once the uncompressed data has been found, it needs to be restructured. Currently the data is in the form 768x1, however it needs to be put back into the original patch form of 16x16x3. This is done through a function called restructureData. 

Finally, the patches are simply reconstructed into the new resultant image. In the same way that the image was deconstructed above, it is reconstructed here. Once the reconstructed image is complete, it is saved to the Images folder.

### Part 2

The code for this part of Question A can also be found in PCA.py. The function used to find the first ten principal components is commented fully.

The resulting first 10 principal components for the entire set of Eigen Vectors and Values (in RGB form) can be seen below:

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

To find the first ten principal components, I used the following process:

Firstly, I found the indices of the 10 maximum Eigen Values. Then, using these indices, I found the associated Eigen Vectors (the indices of the Eigen Values represent the corresponding Eigen Vectors). Once I had both the Eigen Value and Eigen Vector, I simply multiplied these values together to get the appropriate principal component. I then reshaped this new variable to be 16x16x3 (a 16x16 patch) and saved the patch as an image in the same way as all prior images have been saved.
### Part 3

The code for this part of Question A can be found in PCA.py also. As seen from Part 1, it is clear that the larger the amount of Eigen Vectors used, the more accurate the reconstructed image will be. In order to optimise the value of k, I believe that keeping k as close to the maximum amount of Eigen Vectors will allow the reconstructed image to be as close to the original as possible. For this reason, I decided to base my approach to this problem as follows:
 
  * Given that the patches are 16x16 pixels with 3 channels, when transformed from a patch to a single vector, this vector will consist of one column with 768 rows (relating to all of the patches). As a result of this, 768 will be the maximum amount of Eigen Vectors for any one patch. 
  * If the Eigen Values were to be plotted, the graph would begin (at the index 0) at the maximum value and slowly decrease until the value is nearly zero (index N). For this reason, I want to include as many of the high Eigen Values as possible. 
  * Due to this, I have decided to set a threshold value for the minimum Eigen Value. By setting a threshold (in this case, I have set the minimum threshold as 1), all Eigen Values below this threshold will not be considered as part of k. 
  * A counter is used to keep track of the amount of Eigen Values below the threshold. Once this number has been obtained, it is subtracted from the maximum (768) to leave the new value of k (in this case the new value of k is 732).
  
The resulting image 'R732.jpg' can be found in the Images folder and also seen below:
  
<p align="center">
  <img src="https://github.com/SineadGalbraith/CS7GV1ComputerVision/blob/master/Images/R732.jpg" width="670" height="446">
</p>


### Part 4

As seen from Parts 1 and 3 of Question A, the higher the value of k, the better quality and consistency of the reconstructed image. 

When k=10, the patches within the image are very noticeable. The overall image structure is not too bad however; it is still possible to see most of the image and to understand what the image is showing. The colour remains the same but the presence of random red or blue pixels is seen widely across the image. If you look closely at the image also, it looks slightly blurred due to the patch lines being very obvious to the eye.

When k=100, the patches within the images are significantly less noticeable. The image looks smoother overall with the scene being very clear and obvious. However, interestingly, the colour in this image is slightly different to the original, the image appears to be lighter. There are arguably more 'random' value pixels visible in this image also by comparison to the image where k=10. Overall this image is a lot smoother and less blurred but also not particularly accurate given the colour difference.

Finally, when k=732, the image is very close to the original. This is to be expected however as the maximum number of Eigen Values/Vectors is 768 and so there isn't a big difference with this k value and the maximum k value. The colouring of the image is very similar to the original, with no significant differences. It is also rather difficult to spot any anomalies within the pixels (i.e. any 'random' pixel values as seen in the two previous images).

It is very clear from comparing these three images that the higher the amount of Eigen Vectors used, the better quality the image will be. For the lower values of k, the image appears patchy and almost blurred, however this is reduced almost entirely for the higher values of k.
