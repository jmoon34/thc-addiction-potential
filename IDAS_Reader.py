#Note that #83 has been left out due to lack of response
import numpy as np
def idas_read(file_string):
    data = [] #initialize data array
    #read data
    input = open(file_string, 'rU')
    input.readline()
    for line in input:
        data.append(line.strip('\n').split(','))
    input.close()
    #initialize arrays for control and treatment group
    idas_sum = []

    #add values accordingly
    for entry in data:
        for i in range(len(entry)):
            entry[i] = float(entry[i])

        idas_sum.append(sum(entry))

    return idas_sum