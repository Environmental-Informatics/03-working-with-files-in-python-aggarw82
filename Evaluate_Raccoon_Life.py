""" Program to read data from file, process it
    and write processed data to a file
    
    Some funcitons for this excercise have been
    defined in util_fun.py

    Author: Varun Aggarwal
    Username: aggarw82
    Github: https://github.com/Environmental-Informatics/03-working-with-files-in-python-aggarw82
"""

# import libraries
import numpy as np
import ast 

# import user defined funcitons
import util_fun as uf



def readFile(fileName):
    """Read file and return a list of lines

    fileName: name of the file to read
    datalines: list of lines
    """

    data = open(fileName,"r") 
    datalines = data.read().splitlines() # readfile and remove endOfLine characters (if any)
    data.close() 
    return datalines

def writeHeader(fileName):
    """Write header block in specified format

    fileName: name of the file
    """
    
    data = open(fileName,"w") 

    # writeFile
    data.write("Raccoon name: {0}\n".format(name))
    data.write("Average location: {0:.2f}, {1:.2f}\n".format(avg_X, avg_Y))
    data.write("Distance traveled: {0:.2f}\n".format(total_dist))
    data.write("Average energy level: {0:.2f}\n".format(avg_energy))
    data.write("Raccoon end state: {0}\n\n".format(last_line))
    data.close() 

def writeData(fileName, datalines):
    """Write data in specific format

    fileName: name of the file
    """
    
    data = open(fileName,"a") 

    # writeFile
    data.write("Date,Time,X,Y,Asleep,Behavior Mode,Distance\n")
    for i in range(len(datalines["Day"])):
        data.write("{0},{1},{2},{3},{4},{5},{6}\n".format(datalines["Day"][i],datalines["Time"][i],datalines["X"][i],datalines["Y"][i],datalines["Asleep"][i],datalines["Behavior Mode"][i],datalines["Distance"][i]))
    data.close() 

def convertDatatype(inpList):
    """Convert datatype of each element
    of inpList 

    inpList: Input list
    dataTypes: define datatypes 
    """

    dataTypes = [int, float, complex, str]
    for i in dataTypes:
        try:
            return i(inpList)
        except ValueError:
            pass

def listToDictionary(datalines, keys):
    """ create a dictionary of data using keys 

    datalines: list of lines
    keys: keys from dictionary
    """

    dictionary = {} # empty
    for i, key in enumerate(keys):
        temp_data = [j.split(",")[i] for j in datalines]            # read each column
        dictionary[key] = [convertDatatype(x) for x in temp_data]   # convert datatype of elements
    return dictionary


# read Data File
datalines = readFile("2008male00006.txt")

header, last_line, datalines = y=uf.extract_exception_lines(datalines)

# create dictionary for input file
datalines = listToDictionary(datalines, header)
datalines["Distance"] = uf.list_sum(uf.list_distance(datalines["X"], datalines["Y"]))

# write the header block
name = last_line.split()[0]
avg_energy = uf.list_mean(datalines["Energy Level"])
avg_X = uf.list_mean(datalines["X"])
avg_Y = uf.list_mean(datalines["Y"])
total_dist = datalines["Distance"][-1]
writeHeader('Georges_life.txt.txt')

# write data to file
writeData('Georges_life.txt.txt', datalines)
