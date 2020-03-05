"""
This function generates a distribution of the data in stripchart form
"""

import matplotlib.pyplot as pyplot

def stripchart(data, means):

    chow = data[0]
    hf = data[1]

    x_chow = [1]*len(chow)
    x_hf = [2]*len(hf)

    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    ax.plot(x_chow, chow, marker = 'o', linestyle = 'None')
    ax.plot(x_hf, hf, marker = 'o', linestyle = 'None')

    pyplot.xticks(range(1,3,1), ['Chow', 'High Fat']) # Set some labels
    pyplot.xlim(0.5, 2.5) # Change the x-limits of our plot
    pyplot.ylabel('Bodyweight')

    # Where are the means?
    pyplot.hlines(means[0], 0, 3, colors = 'r')
    pyplot.hlines(means[1], 0, 3, colors = 'b')

    pyplot.show()

    return 0