"""
This function calculates the p-value from the experimental result from the null
"""

def pval(null_data, test_stat):

    tot = filter(lambda x: x >= test_stat, null_data)
    pval = (float(len(tot))) / float(len(null_data))

    return pval