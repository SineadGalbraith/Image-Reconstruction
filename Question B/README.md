# Question B

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

At this stage, the SIFT process is complete. Next, the keypoints within each of the images need to be matched (if appropriate). To do this, I use another OpenCV function called BFMatcher (Brute-Force Matcher). This matcher works by taking a feature in one image and comparing it to all features in the other image. The features are matched using a distance function and all matches are returned in an array. After this, the function knnMatch() is called. This function uses the array of matches to find the closest 'k' matches, in this case k=2 so the top two matches for each feature will be returned and stored in an array. Once we have the array of matches, we need to distinguish the exact matches. For this reason, the matches array is further filtered. Every match needs to satisfy a ratio; if the ratio is not satisfied, the match is not considered strong enough to be kept and so it will be discarded.

Once all matches have been filtered through, providing that there are more than the minimum number of 'goodMatches', the two images now need to be aligned. In order to align the images, a homorgraphy matrix needs to be obtained for the transformation. The images need to be aligned to the same orientation and using the homography matrix, both images are transformed to the same perspective. Once this has been done, the stitching of the image can begin. 

Using the warpPerspective() function, the 'Right' image is taken first. From here, the perspective of the image is changed so that the 'Left' image can be added onto it. Once the warpPerspective() function has been performed on the 'Right' image, the 'Left' image is applied to this new image and so the whole Panoramic view can be seen as one image.
