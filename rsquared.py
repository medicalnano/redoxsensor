import numpy
from scipy import stats

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
 
def get_R2(filenames, concs):
    
    ## average dV for each x
    bacteria_allConcs_average = []
    for fii in filenames:
        # print(fii)
        
        ## each column in data is one replicate
        data = numpy.loadtxt(fii)
        # print(data)
        # print(numpy.shape(data))
    
        average = data.mean(axis=1)
        # print(average)
        # print(numpy.shape(average))
        
        bacteria_allConcs_average.append(average)
    
    bacteria_allConcs_average = numpy.transpose(numpy.vstack(bacteria_allConcs_average))
    # print(bacteria_allConcs_average)
    # print(numpy.shape(bacteria_allConcs_average))
    
    ## Linear regression to get r_squared for each timepoint (row) 
    r_squared = []
    for row in bacteria_allConcs_average:
        slope, intercept, r, p, err = stats.linregress(concs, row)
        r_squared.append(r * r)
        
    r_squared = numpy.array(r_squared)

    return r_squared
    
def find_timeR2max(r_squared, time):
    r_squared_max = numpy.max(r_squared)
    
    i = numpy.where(r_squared == r_squared_max)[0][0]
    time_r_squared_max = time[i]
    
    return time_r_squared_max

def find_timeR2x(r_squared, time, x):
    r_squared_diff_abs = numpy.absolute(r_squared - x)
    r_squared_diff_abs_min = numpy.min(r_squared_diff_abs)
    
    i = numpy.where(r_squared_diff_abs == r_squared_diff_abs_min)[0][0]
    time_r_squared_x = time[i]
    
    return time_r_squared_x
    