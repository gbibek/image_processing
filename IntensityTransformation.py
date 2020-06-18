import numpy as np


def Negative(intensity_2d):
    neg_intensity = []
    L = np.array(intensity_2d).max()

    for i in range(len(intensity_2d)):
        collect_neg_intensity = []
        for j in range(len(intensity_2d[i])):
            s = L - 1 - intensity_2d[i][j]
            collect_neg_intensity.append(s)
        neg_intensity.append(collect_neg_intensity)
    return neg_intensity
