import numpy as np
import matplotlib.pyplot as pyplot
def null(file_string, mean_diff):
    # Read in the data
    data = []
    input = open(file_string, 'rU')
    input.readline() # Remove headers
    for line in input:
        data.append((line.strip('\n')))
    input.close()
    # Convert to a numpy array
    pop = np.array(data).astype(float)
    print pop
    null = []

    for i in range(0, 10000):
        pop_control = np.random.choice(pop, size = 12)
        pop_treat = np.random.choice(pop, size = 12)
        null.append(np.mean(pop_treat) - np.mean(pop_control))

    #computing 5 means
    fivemeans=[]
    for i in range(5):
        randtwelve = np.random.choice(pop, size=12)
        fivemeans.append(np.mean(randtwelve))

    print "Look over here"
    print fivemeans

    pyplot.figure()
    pyplot.hist(null, bins = 20)
    # Plot difference in means of our samples
    pyplot.axvline(mean_diff, color = 'r')
    pyplot.show()

    return null