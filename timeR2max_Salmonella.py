import numpy
import rsquared

## datapath
path = "/Users/suloff/Desktop/190311_timeR2max/dV_Salmonella"

## n replicates for each concentration of bacteria
filenames = ("bacteria0.txt", "bacteria1c3.txt", "bacteria6c6.txt", "bacteria13c2.txt", "bacteria66.txt", "bacteria260.txt")

## full names
ffilenames = []
for fii in filenames:
    foo = path + "/" + fii
    ffilenames.append(foo)

## time in min
time = numpy.loadtxt("/Users/suloff/Desktop/190311_timeR2max/dV_Salmonella/time.txt")
# print(time)
# print(numpy.shape(time))

## concentration of bacteria in CFU
# concs = [0, 1.3, 6.6, 13.2, 66, 260]

## concentration of bacteria in Abs(OD600) 
concs = [0, 0.007, 0.035, 0.07, 0.35, 1.05]

r_squared = rsquared.get_R2(ffilenames, concs) 
#print(r_squared)

timeR2max = rsquared.find_timeR2max(r_squared, time)
print(timeR2max)

r_threshold = 0.975
timeR2x = rsquared.find_timeR2x(r_squared, time, r_threshold)
print(timeR2x)