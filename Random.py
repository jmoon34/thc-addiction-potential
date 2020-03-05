import numpy as np
def Random(indep, cudit, idas, ceq):
    IV = indep
    CUDIT = cudit
    IDAS = idas
    CEQ = ceq
    null_CUDIT = []
    null_IDAS = []
    null_CEQ = []

    x = range(79)
    for i in range(10000):
        np.random.shuffle(x)
        rand_low_index = []
        rand_high_index = []
        IV_rand = [IV[k] for k in x]
        for j in range(np.size(IV_rand)):
            if IV_rand[j] < 28:
                rand_low_index.append(j)
            else:
                rand_high_index.append(j)

        CUDIT_rand_low = [CUDIT[i] for i in rand_low_index]
        CUDIT_rand_high = [CUDIT[i] for i in rand_high_index]
        IDAS_rand_low = [IDAS[i] for i in rand_low_index]
        IDAS_rand_high = [IDAS[i] for i in rand_high_index]
        CEQ_rand_low = [CEQ[i] for i in rand_low_index]
        CEQ_rand_high = [CEQ[i] for i in rand_high_index]

        null_CUDIT.append(np.mean(CUDIT_rand_high) - np.mean(CUDIT_rand_low))
        null_IDAS.append(np.mean(IDAS_rand_high) - np.mean(IDAS_rand_low))
        null_CEQ.append(np.mean(CEQ_rand_high) - np.mean(CEQ_rand_low))

    return null_CUDIT, null_IDAS, null_CEQ
