# Imports
import cv2
import numpy as np

# Read in the first of the overlapping images 'Right.jpg' and convert it from RGB to Gray
originalImageRight = cv2.imread('./Images/Right.jpg')
originalImageRightGrey = cv2.cvtColor(originalImageRight, cv2.COLOR_RGB2GRAY)

# Read in the second of the overlapping images 'Left.jpg' and convert it from RGB to Gray
originalImageLeft = cv2.imread('./Images/Left.jpg')
originalImageLeftGrey = cv2.cvtColor(originalImageLeft, cv2.COLOR_RGB2GRAY)

# This section uses the OpenCV SIFT descriptor function to find the matching features in both of
# the images. We will be using the best-matched SIFT features for the image stitching process.
# For each image, key points and their respective descriptors are extracted.
# These keypoints show the features that have been detected on an image using SIFT. To join together
# the 'Left' and 'Right' images, these keypoints are used to find the overlapping points.
sift = cv2.SIFT_create()
rightKeyPoints, rightDescriptor = sift.detectAndCompute(originalImageRightGrey, None)
leftKeyPoints, leftDescriptor = sift.detectAndCompute(originalImageLeftGrey, None)

# For this code, I will be using the BFMatcher. This matcher will look at the features from both
# of the images (above) and add the top two 'matches' to a list.
match = cv2.BFMatcher()
matches = match.knnMatch(rightDescriptor, leftDescriptor, k=2)

# In order to reduce the chance that a feature may exist more than once within an image, the features
# are cycled through and filtered out based on whether they satisfy a certain ratio. If the ratio of the
# feature is greater than the ratio below, it is considered a match and added to the 'goodMatch' list.
goodMatch = []
for m, n in matches:
    if (m.distance < 0.5 * n.distance):
        goodMatch.append(m)

# A variable called minimumMatches is initialised. If the length of the list 'goodMatch' is not less than the
# minimum matches, we consider this to be an image that can be stitched. Otherwise, a message is printed
# informing the user that there are not enough matches.
# Next, the two images need to be aligned. For this, a homography matrix is needed. RANSAC is used to
# estimate the homography matrix.
# Once the homography matrix has been found, the two images can be stitched together. First of all the view
# needs to be changed so that the images appear in line. To do this, the perspective must be warped. The
# 'Right' image is taken first, without any overlapping, and the 'Left' image is added to it so that the final
# image contains both fully stitched 'sides' in the correct alignment.
minimumMatches = 10
if len(goodMatch) > minimumMatches:
    sourcePoints = np.float32([rightKeyPoints[m.queryIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
    destinationPoints = np.float32([leftKeyPoints[m.trainIdx].pt for m in goodMatch]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(sourcePoints, destinationPoints, cv2.RANSAC, 5.0)
else:
    print("Not enough matches.")

panoramicImage = cv2.warpPerspective(originalImageRight, M, (originalImageLeft.shape[1] + originalImageRight.shape[1], originalImageLeft.shape[0]))
panoramicImage[0:originalImageLeft.shape[0], 0:originalImageLeft.shape[1]] = originalImageLeft

# The new array 'panoramicImage' is then saved to a JPG file in the local contents folder as 'Panorama.jpg' using
# cv2.imwrite() and the image is displayed.
cv2.imwrite("./Images/Panorama.jpg", panoramicImage)
cv2.imshow("Panoramic View", panoramicImage)
cv2.waitKey(0);
