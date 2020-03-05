#Demographic information: Age,Gender,Edu_Level,Edu_Years,Martial_Status,Disabled
from Demographic_Reader import *
from stripchart import *
from null import *
from pval import *

def main():
    mean_age, num_male, num_female, mean_edu_level, mean_edu_years, mean_marital, num_disabled, num_not_disabled = demographic_read('Demographic Info Numbers.csv')
    print 'Mean age: ', mean_age
    print 'Number of males: ', num_male
    print 'Number of females: ', num_female
    print 'Mean education level: ', mean_edu_level
    print 'Mean years of education: ', mean_edu_years
    print 'Mean number of spouses: ', mean_marital
    print 'Number of disabled persons: ', num_disabled
    print 'Number of not disabled persons: ', num_not_disabled

if __name__ == "__main__":
    main()