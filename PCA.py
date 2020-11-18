# Imports
import cv2
import numpy as np
from numpy import linalg as la

# This is the value of k, this needs to be changed when changing the amount of Principal Components.
k = 100

# Read in Scenery Image S from the Images folder.
image = cv2.imread('./Images/S.jpg')

# Store the height and width of the image into their respective attributes.
height = int(image.shape[0])
width = int(image.shape[1])

# Make a copy of the original image. This will be used to place the reconstructed patches back into later in
# the program.
reconstructedImage = np.copy(image)

# Variables initialised for use later in the program.
patchPixelSize = 16
j = patchPixelSize
lastJ = 0
columns = []
columnMeans = []
maxK = 768


# This function finds the mean of each channel in each column and adds it to a 'Column Mean' array.
# The mean is the subtracted from the column data to give the Mean Adjusted Data which is then returned.
def getColumnMean(column):
    mean = np.mean(column, axis=0)
    column = column - mean
    columnMeans.append(mean)
    return column


# This function adds the mean back onto the now uncompressed data. For every patch, the associated mean from
# the 'Column Mean' array is added back in. The newly readjusted patch is then returned.
def addMean(patch, patchNum):
    patch = patch + columnMeans[patchNum]
    return patch


# This function reshapes the array. Each patch in the uncompressed data is still in the format of a (768x1) column
# for all three channels. This function simply restructures each 768 column into 16x16 patches with all three channels
# once again. From here, the newly reshaped array is passed on to the reconstructAndSaveImage function where the
# entire image is reconstructed.
def restructureData(columns, k):
    reshapedArray = []
    for i in range(columns.shape[1]):
        reshaped = columns[:, i].reshape((16, 16, 3))
        reshapedArray.append(reshaped)
    reconstructAndSaveImage(reshapedArray, k)


# This function is for Part 2 of Question A. Using the function argpartition(), the indices of the maximum 10 Eigen
# Values are returned into the topVals array. The indices of the Eigen Values are associated with their
# corresponding Eigen Vectors (i.e. the corresponding Eigen Vector and Eigen Value will have the same index in their
# respective arrays). The Eigen Vector and Eigen Value at each of the 10 maximum indices are then multiplied. From here
# the resultant column is restructured into the original RGB format (16x16x3). The image is then displayed and saved in
# the Images folder as 'PC' with the respective index (0-9).
def findFirstTenPrincipleComponents(vals, vecs):
    topVals = np.argpartition(vals, -10)[-10:]
    for index in range(0, len(topVals)):
        vecVal = vecs[:, index] * vals[index]
        pc = vecVal.reshape(16, 16, 3)
        cv2.imwrite("./Images/PC" + str(index) + ".jpg", pc)
        cv2.imshow("PC" + str(index), pc)
        # cv2.waitKey(0)


# In this function, the idea is to take each patch from the 'columns' array, compress the data and then uncompress it.
# This process needs to be done patch by patch and so the first step is to extract the patch. To find the compressed
# data, the transpose of this data needs to be multiplied with the transpose of the reduced vectors from above.
# Once the compressed data has been found, we immediately need to uncompress it. To do this, we multiply the reduced
# vectors by the compressed data from the previous line. At this stage, the data is still adjusted from above (where the
# mean had been subtracted from the original data). The last step in this loop is to readjust the data back to the
# initial values with the mean added on. This is done through the 'addMean' function.
# A copy of the columns array is made so that the data can be slotted in in place as well as a counter.
# At this stage, the data is correct for the reconstructed image, however it is still in the wrong format (768x1). The
# last step before creating the new reconstructed image is to restructure the data back into a (16x16x3) format. This
# is done through the restructureData function.
def getUncompressedData(columns, reducedVecs, k):
    uncompressed = np.copy(columns)
    patchCounter = 0
    for vec in range(0, columns.shape[1]):
        currentPatch = columns[:, vec]
        compressed = np.matmul(np.matrix.transpose(reducedVecs), currentPatch.T)
        uncompressedPatch = np.matmul(reducedVecs, compressed)
        destandardisedPatch = addMean(uncompressedPatch, patchCounter)
        uncompressed[:, vec] = destandardisedPatch
        patchCounter = patchCounter + 1
    restructureData(uncompressed, k)


# Using all of the data found in the previous functions, the image can now be reconstructed. This process is similar
# enough to the deconstruction process of the image into patches. The first step here is to extract each patch (16x16x3)
# from the restructured data array. This patch is then put into the new reconstructed image in the correct place (i.e.
# at the same place as its original patch was in the original image). This is repeated for every patch in the image.
# Once the new reconstructed image has been made, it needs to be saved. The name of the image will be 'R{k}' as per the
# assignment and this image will be saved to the /Images folder/ The image is then shown on screen.
def reconstructAndSaveImage(restructuredArray, k):
    j = patchPixelSize
    lastJ = 0
    counter = 0
    for rows in range(0, height):
        i = patchPixelSize
        lastI = 0
        if j <= height:
            for col in range(0, width):
                if i <= width:
                    patch = restructuredArray[counter]
                    reconstructedImage[lastJ:j, lastI:i] = patch
                    counter = counter + 1
                    lastI = i
                    i = i + patchPixelSize
            lastJ = j
            j = j + patchPixelSize

    name = 'R' + str(k)
    cv2.imwrite("./Images/" + name + ".jpg", reconstructedImage)
    cv2.imshow("Reconstructed Image", reconstructedImage)
    # cv2.waitKey(0)


# This function is for Part 3 of Question A. Within this function, the goal is to find the optimised k value. To do
# this, I have decided to set a threshold of 1 as the minimum value that we want to include in the reduced vectors. A
# counter has been specified to keep track of the amount of Eigen Values that are less than 1. When this loop is
# complete and the number of values have been counted, this amount is then subtracted from the total amount of Eigen
# Values (768) to leave the new version of k. From here, the reduced vectors array is made containing 'k' Eigen Vectors.
# The process then continues the same as with the pre-defined value of k.
def findOptimalKValue(columns, eVals, eVecs):
    valCounter = 0
    for i in range(0, len(eVals)):
        if eVals[i] <= 1:
            valCounter = valCounter + 1
    reducedK = maxK - valCounter
    reducedVecs = eVecs[0:len(eVecs), 0:reducedK]
    getUncompressedData(columns, reducedVecs, reducedK)


# In this section of the code, the original image data is divided into patches. Every row and column is looped
# through and each 16x16 patch is extracted. This patch is then reshaped into a (768x1) column. The 'getColumnMean'
# function is then called. Within this function, the means of the individual channels within the column are found
# and the original mean is taken away from the original column so that the data is now mean-adjusted. This mean-adjusted
# data is then returned. This is the first step of the PCA process.
# A new array called columns has been initialised here. This array will contain the mean-adjusted patch (in column
# format) data for every patch within the image. If this array is empty, then the array will equal the patch (i.e. if it
# is the first patch, the array will be made equal to the first patch data), otherwise the current patch data will be
# added to this array. This process happens for every patch within the image.
for row in range(0, width):
    i = patchPixelSize
    lastI = 0
    if j <= height:
        for col in range(0, height):
            if i <= width:
                currentPatch = image[lastJ:j, lastI:i]
                patchColumn = currentPatch.reshape(768, 1)
                patchColumn = getColumnMean(patchColumn)
                if len(columns) == 0:
                    columns = patchColumn
                else:
                    columns = np.concatenate((columns, patchColumn), axis=1)
                lastI = i
                i = i + patchPixelSize
        lastJ = j
        j = j + patchPixelSize

# Once all of the patches have been added to the 'columns' array, this data can now be used to find the covariance
# matrix. This is the second step of the PCA process. The covariance matrix can be found using the Numpy function cov().
covMatrix = np.cov(columns)

# Now that the covariance matrix has been found, it is possible to find all of the Eigen Values and Eigen Vectors for
# this covariance matrix. This has been done through a function in the numpy library (called linalg) called eig(). This
# is the third step of the PCA process.
eVals, eVecs = la.eig(covMatrix)

# This code is for Question A Part 2, finding the first ten principal components.
findFirstTenPrincipleComponents(eVals, eVecs)

# Once all of the Eigen Values and Eigen Vectors have been found for the covariance matrix, the next step involves
# narrowing down the amount of Eigen Vectors used. We want k (the value that we specified at the beginning of the code)
# Eigen Vectors. To do this, a new list is created containing all rows of the Eigen Vectors (eVecs), but only k columns.
reducedVecs = eVecs[0:len(eVecs), 0:k]

# Get the uncompressed Data using the column vector array, the reduced vectors from about and k.
getUncompressedData(columns, reducedVecs, k)

# Find the new value of K (the better k value). This is Question A Part 3 of the Assignment.
findOptimalKValue(columns, eVals, eVecs)