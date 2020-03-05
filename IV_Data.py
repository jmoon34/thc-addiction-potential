from stripchart import *
from null import *
from pval import *
from IV_Reader import *
import matplotlib.pyplot as pyplot

def main():
    IV, IV_mean, IV_med, IV_low, IV_high, low_index, high_index = IV_read('IV_final.csv')
    print np.size(IV_low)
    print np.size(IV_high)
    print 'The mean for IV score is: ', np.mean(IV)
    print 'The median for IV score is: ', np.median(IV)

if __name__ == "__main__":
    main()