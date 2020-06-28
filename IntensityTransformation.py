import numpy as np


def Negative(intensity_2d):
    neg_intensity = []
    L = np.array(intensity_2d).max()

    for i in range(len(intensity_2d)):
        collect_neg_intensity = []
        for j in range(len(intensity_2d[i])):
            r = intensity_2d[i][j]
            s = L - 1 - r
            collect_neg_intensity.append(s)
        neg_intensity.append(collect_neg_intensity)
    return neg_intensity


def Log(intensity_2d, c=1):
    log_intensity = []
    for i in range(len(intensity_2d)):
        collect_log_intensity = []
        for j in range(len(intensity_2d[i])):
            r = intensity_2d[i][j]
            s = c * np.log(1+r)
            collect_log_intensity.append(s)
        log_intensity.append(collect_log_intensity)
    return log_intensity
