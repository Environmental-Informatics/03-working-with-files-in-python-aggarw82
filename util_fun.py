	""" Necesssary functions for this excercise
	Including sum, avg and distance

	Author: Varun Aggarwal
	Username: aggarw82
	Github: https://github.com/Environmental-Informatics/03-working-with-files-in-python-aggarw82
"""

import numpy as np

# extract header and remarks from file
def extract_exception_lines(datalines):
	# remove white spaces from headers, remarks, data
    return [i.strip() for i in datalines[0].split(",")], datalines[-1], datalines[1:-1]

# calculate mean of list
def list_mean(inpList):
	return np.mean(inpList)

# calculate cumulative sum of list
def list_sum(inpList):
	return list(np.cumsum(inpList))

# calculate euclidean distance between two points
def distance(A, B):
	return np.sqrt((A[0] - A[1])**2 + (B[0] - B[1])**2) 

# calculate distance between coordiantes
def list_distance(X, Y):
	dist = [0] # first element
	for i in range(len(X)-1):
		dist.append(distance( (X[i],X[i+1]) , (Y[i],Y[i+1]) ))
	return dist