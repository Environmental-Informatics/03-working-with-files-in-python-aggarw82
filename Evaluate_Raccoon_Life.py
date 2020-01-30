import numpy as np
import ast 

def convertDatatype(inpList):
    """Convert datatype of each element
    of inpList 

    inpList: Input list
    dataTypes: define datatypes 
    """

    dataTypes = [int, float, str, complex]
    for i in dataTypes:
        try:
            return i(inpList)
        except ValueError:
            pass

def readFile(fileName):
    """Read file and return a list of lines

    fileName: name of the file to read
    datalines: list of lines
    """

    data = open(fileName,"r") 
    datalines = data.read().splitlines() # readfile and remove endOfLine characters (if any)
    data.close() 
    return datalines

def extract_exception_lines(datalines):
    """ extract header and remarks from file

    datalines: list of lines
    """

    return datalines[0], datalines[-1], datalines[1:-1]

def listToDictionary(datalines, keys):
    """ create a dictionary of data using keys 
    from a list of keys

    datalines: list of lines
    keys: keys from dictionary
    """

    dictionary = {} # empty
    for i, key in enumerate(keys):
        temp_data = [j.split(",")[i] for j in datalines] # read each column
        dictionary[key] = [convertDatatype(x) for x in temp_data] # convert datatype of elements
    return dictionary


datalines = readFile("2008male00006.txt")
header, last_line, datalines = extract_exception_lines(datalines)
datalines = listToDictionary(datalines, header.split(","))

# debug
print(datalines)
# print(datalines)
# print(header)
# print(last_line)



