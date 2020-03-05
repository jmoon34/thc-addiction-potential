import numpy as np
def IV_read(file_string):
    data = [] #initialize data array
    #read data
    input = open(file_string, 'rU')
    input.readline()
    for line in input:
        data.append(line.strip('\n').split(','))
    input.close()
    #initialize arrays for control and treatment group
    IV = []

    #add values accordingly
    for entry in data:
        for i in range(len(entry)):
            if i==1:
                entry[i] = float(entry[i])/12
            else:
                entry[i] = float(entry[i])

        IV.append(sum(entry))

    IV_mean = np.mean(IV)
    IV_med = np.median(IV)
    IV_low = []
    low_index = []
    IV_high = []
    high_index = []
    for i in range(np.size(IV)):
        if IV[i] < 28:
            IV_low.append(IV[i])
            low_index.append(int(i))
        else:
            IV_high.append(IV[i])
            high_index.append(int(i))






    return IV, IV_mean, IV_med, IV_low, IV_high, low_index, high_index