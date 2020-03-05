#Demographic information: Age,Gender,Edu_Level,Edu_Years,Martial_Status,Disabled

import numpy as np
def demographic_read(file_string):
    data = [] #initialize data array
    #read data
    input = open(file_string, 'rU')
    input.readline()
    for line in input:
        data.append(line.strip('\n').split(','))
    input.close()
    #initialize arrays for control and treatment group
    age = []
    gender = []
    edu_level = []
    edu_years = []
    marital = []
    disabled = []
    #add values accordingly
    for entry in data:
        age.append(float(entry[0]))
        marital.append(float(entry[4]))
        disabled.append(float(entry[5]))
        try:
            gender.append(float(entry[1]))
        except:
            pass
        try:
            edu_level.append(float(entry[2]))
        except:
            pass
        try:
            edu_years.append(float(entry[3]))
        except:
            pass


    mean_age = np.mean(age)
    num_female = np.count_nonzero(gender)
    num_male = np.size(gender)-num_female
    mean_edu_level = np.mean(edu_level)
    mean_edu_years = np.mean(edu_years)
    mean_marital = np.mean(marital)
    num_disabled = np.count_nonzero(disabled)
    num_not_disabled = np.size(disabled) - num_disabled


    return mean_age, num_male, num_female, mean_edu_level, mean_edu_years, mean_marital, num_disabled, num_not_disabled