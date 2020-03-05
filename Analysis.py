#Demographic information: Age,Gender,Edu_Level,Edu_Years,Martial_Status,Disabled
from Demographic_Reader import *
from CUDIT_Reader import *
from IDAS_Reader import *
from CEQ_Reader import *
from IV_Reader import *
from stripchart import *
from null import *
from pval import *
from scipy.stats import ttest_ind, mannwhitneyu, pearsonr
from Random import *

def main():
    #first we start with analyzing the demographic information
    mean_age, num_male, num_female, mean_edu_level, mean_edu_years, mean_marital, num_disabled, num_not_disabled = demographic_read('Demographic Info Numbers.csv')
    # print 'Mean age: ', mean_age
    # print 'Number of males: ', num_male
    # print 'Number of females: ', num_female
    # print 'Mean education level: ', mean_edu_level
    # print 'Mean years of education: ', mean_edu_years
    # print 'Mean number of spouses: ', mean_marital
    # print 'Number of disabled persons: ', num_disabled
    # print 'Number of not disabled persons: ', num_not_disabled

    #then we analyze the independent variables
    IV, IV_mean, IV_med, IV_low, IV_high, low_index, high_index = IV_read('IV_final.csv')


    # pyplot.figure()
    # pyplot.hist(IV, 20)
    # pyplot.title('Probability distribution for IV score')
    # pyplot.show()

    #Then we analyze the dependent variables
    CUDIT = cudit_read('CUDIT_final.csv')
    IDAS = idas_read('IDAS_final.csv')
    CEQ = ceq_read('CEQ_final.csv')

    #First we observe the correlation between IV and DV's
    # pyplot.figure()
    # pyplot.scatter(IV, CUDIT)
    # pyplot.title('Scatterplot of CUDIT vs. IV')
    # pyplot.xlabel('IV Score')
    # pyplot.ylabel('CUDIT Score')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.scatter(IV, IDAS)
    # pyplot.title('Scatterplot of IDAS vs. IV')
    # pyplot.xlabel('IV Score')
    # pyplot.ylabel('IDAS Score')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.scatter(IV, CEQ)
    # pyplot.title('Scatterplot of CEQ vs. IV')
    # pyplot.xlabel('IV Score')
    # pyplot.ylabel('CEQ Score')
    # pyplot.show()

    CUDIT_corr = pearsonr(IV,CUDIT)
    IDAS_corr = pearsonr(IV,IDAS)
    CEQ_corr = pearsonr(IV,CEQ)

    print "Correlation between independent variable and CUDIT is: ", CUDIT_corr[0]
    print "Correlation between independent variable and IDAS is: ", IDAS_corr[0]
    print "Correlation between independent variable and CEQ is: ", CEQ_corr[0]

    CUDIT_low = [CUDIT[i] for i in low_index]
    CUDIT_high = [CUDIT[i] for i in high_index]
    IDAS_low = [IDAS[i] for i in low_index]
    IDAS_high = [IDAS[i] for i in high_index]
    CEQ_low = [CEQ[i] for i in low_index]
    CEQ_high = [CEQ[i] for i in high_index]
    test_CUDIT = np.mean(CUDIT_high) - np.mean(CUDIT_low)
    test_IDAS = np.mean(IDAS_high) - np.mean(IDAS_low)
    test_CEQ = np.mean(CEQ_high) - np.mean(CEQ_low)

    # pyplot.figure()
    # pyplot.hist(CUDIT_low, 20)
    # pyplot.title('Probability Distribution for CUDIT_low Score')
    # pyplot.xlabel('CUDIT_low Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(CUDIT_high, 20)
    # pyplot.title('Probability Distribution for CUDIT_high Score')
    # pyplot.xlabel('CUDIT_high Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(IDAS_low, 20)
    # pyplot.title('Probability Distribution for IDAS_low Score')
    # pyplot.xlabel('IDAS_low Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(IDAS_high, 20)
    # pyplot.title('Probability Distribution for IDAS_high Score')
    # pyplot.xlabel('IDAS_high Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(CEQ_low, 20)
    # pyplot.title('Probability Distribution for CEQ_low Score')
    # pyplot.xlabel('CEQ_low Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(CEQ_high, 20)
    # pyplot.title('Probability Distribution for CEQ_high Score')
    # pyplot.xlabel('CEQ_high Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()

    #CUDIT data shows skewed right, IDAS shows roughly normal, and CEQ data shows skewed left
    #We use the log transform for CUDIT, and the square transform for CEQ
    log_CUDIT_low = np.log(CUDIT_low)
    log_CUDIT_high = np.log(CUDIT_high)
    fifth_CEQ_low = np.power(CEQ_low,5)
    fifth_CEQ_high = np.power(CEQ_high,5)
    #
    # pyplot.figure()
    # pyplot.hist(log_CUDIT_low, 20)
    # pyplot.title('Probability Distribution for log(CUDIT_low) Score')
    # pyplot.xlabel('log(CUDIT_low) Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(log_CUDIT_high, 20)
    # pyplot.title('Probability Distribution for log(CUDIT_high) Score')
    # pyplot.xlabel('log(CUDIT_high) Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(fifth_CEQ_low, 20)
    # pyplot.title('Probability Distribution for Transformed CEQ_low Score')
    # pyplot.xlabel('Transformed CEQ_low Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()
    #
    # pyplot.figure()
    # pyplot.hist(fifth_CEQ_high, 20)
    # pyplot.title('Probability Distribution for Transformed CEQ_high Score')
    # pyplot.xlabel('Transformed CEQ_high Score')
    # pyplot.ylabel('Frequency')
    # pyplot.show()

    #Calculating descriptive statistics
    CUDIT_low_mean = np.mean(CUDIT_low)
    CUDIT_high_mean = np.mean(CUDIT_high)
    CUDIT_low_var = np.var(CUDIT_low)
    CUDIT_high_var = np.var(CUDIT_high)
    log_CUDIT_low_mean = np.mean(log_CUDIT_low)
    log_CUDIT_high_mean = np.mean(log_CUDIT_high)
    log_CUDIT_low_var = np.var(log_CUDIT_low)
    log_CUDIT_high_var = np.var(log_CUDIT_high)
    CEQ_low_mean = np.mean(CEQ_low)
    CEQ_high_mean = np.mean(CEQ_high)
    CEQ_low_var = np.var(CEQ_low)
    CEQ_high_var = np.var(CEQ_high)
    fifth_CEQ_low_mean = np.mean(fifth_CEQ_low)
    fifth_CEQ_high_mean = np.mean(fifth_CEQ_high)
    fifth_CEQ_low_var = np.var(fifth_CEQ_low)
    fifth_CEQ_high_var = np.var(fifth_CEQ_high)
    IDAS_low_mean = np.mean(IDAS_low)
    IDAS_high_mean = np.mean(IDAS_high)
    IDAS_low_var = np.var(IDAS_low)
    IDAS_high_var = np.var(IDAS_high)

    print "Mean/Variance for CUDIT_low: ", CUDIT_low_mean, CUDIT_low_var
    print "Mean/Variance for CUDIT_high: ", CUDIT_high_mean, CUDIT_high_var
    print "Mean/Variance for log(CUDIT_low): ", log_CUDIT_low_mean, log_CUDIT_low_var
    print "Mean/Variance for log(CUDIT_high): ", log_CUDIT_high_mean, log_CUDIT_high_var
    print "Mean/Variance for CEQ_low: ", CEQ_low_mean, CEQ_low_var
    print "Mean/Variance for CEQ_high: ", CEQ_high_mean, CEQ_high_var
    print "Mean/Variance for transformed CEQ_low: ", fifth_CEQ_low_mean, fifth_CEQ_low_var
    print "Mean/Variance for transformed CEQ_high: ", fifth_CEQ_high_mean, fifth_CEQ_high_var
    print "Mean/Variance for IDAS_low: ", IDAS_low_mean, IDAS_low_var
    print "Mean/Variance for IDAS_high: ", IDAS_high_mean, IDAS_high_var


    #Welch's t-test, 2-sided, assumes unequal variance
    t_CUDIT, p_CUDIT_ttest = ttest_ind(log_CUDIT_low, log_CUDIT_high, equal_var = False)
    t_IDAS, p_IDAS_ttest = ttest_ind(IDAS_low, IDAS_high, equal_var = False)
    t_CEQ, p_CEQ_ttest = ttest_ind(fifth_CEQ_low, fifth_CEQ_high, equal_var = False)

    print "p-value for CUDIT under Welch's t-test is: ", p_CUDIT_ttest / 2
    print "p-value for IDAS under Welch's t-test is: ", p_IDAS_ttest / 2
    print "p-value for CEQ under Welch's t-test is: ", p_CEQ_ttest / 2

    #Mann-Whitney rank test
    U_CUDIT, p_CUDIT_MWU = mannwhitneyu(CUDIT_low,CUDIT_high,True,'less')
    U_IDAS, p_IDAS_MWU = mannwhitneyu(IDAS_low,IDAS_high,True,'greater')
    U_CEQ, p_CEQ_MWU = mannwhitneyu(CEQ_low,CEQ_high,True,'greater')

    print "p-value for CUDIT under Mann-Whitney U test is: ", p_CUDIT_MWU
    print "p-value for IDAS under Mann-Whitney U test is: ", p_IDAS_MWU
    print "p-value for CEQ under Mann-Whitney U test is: ", p_CEQ_MWU

    #Randomization
    null_CUDIT, null_IDAS, null_CEQ = Random(IV, CUDIT, IDAS, CEQ)

    pyplot.figure()
    pyplot.hist(null_CUDIT,20)
    pyplot.axvline(test_CUDIT, color = 'r')
    pyplot.title('Null Distribution For CUDIT With Test Statistic')
    pyplot.xlabel('Difference In Mean')
    pyplot.ylabel('Frequency')
    pyplot.show()

    pyplot.figure()
    pyplot.hist(null_IDAS, 20)
    pyplot.axvline(test_IDAS, color='r')
    pyplot.title('Null Distribution For IDAS With Test Statistic')
    pyplot.xlabel('Difference In Mean')
    pyplot.ylabel('Frequency')
    pyplot.show()

    pyplot.figure()
    pyplot.hist(null_CEQ, 20)
    pyplot.axvline(test_CEQ, color='r')
    pyplot.title('Null Distribution For CEQ With Test Statistic')
    pyplot.xlabel('Difference In Mean')
    pyplot.ylabel('Frequency')
    pyplot.show()

    p_CUDIT_rand = pval(null_CUDIT, test_CUDIT)
    p_IDAS_rand = 1-pval(null_IDAS, test_IDAS)
    p_CEQ_rand = 1-pval(null_CEQ, test_CEQ) #Need to adjust in accordance to the different alternative hypothesis

    print "p-value for CUDIT under randomization is: ", p_CUDIT_rand
    print "p-value for IDAS under randomization is: ", p_IDAS_rand
    print "p-value for CEQ under randomization is: ", p_CEQ_rand




if __name__ == "__main__":
    main()