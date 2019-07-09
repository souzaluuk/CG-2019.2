import datetime as dt
import statistics as st
import math

def quartis(values):
    meio = len(values)//2

    Q1 = st.median(values[:meio])
    Q2 = st.median(values)
    Q3 = st.median(values[meio:])
    
    # print('Quartis:')
    # print('Q1:',Q1)
    # print('Q2:',Q2)
    # print('Q3:',Q3)

    return [Q1,Q2,Q3]

def noOutliers(values):
    Q1,_,Q3 = quartis(values)

    A = Q3 - Q1
    # print('A:',A)

    minOutlier = Q1 - A * 1.5 # mod outlier min
    maxOutlier = Q3 + A * 1.5 # mod outlier max
    # print('minOutlier:',minOutlier)
    # print('maxOutlier:',maxOutlier)

    inliers = list()
    for value in values:
        if minOutlier <= value <= maxOutlier:
            inliers.append(value)
    return inliers