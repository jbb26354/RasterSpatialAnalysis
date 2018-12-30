'''
This script tests the kernek function
'''
import kernel   # imports the kernel module

# print a start message
print "\n=================================================================="
print "Test the fire model kernel function ..."

# define input data (arguments) as 5 x 5 matrices
# argument 1: the current states of a processing window
stat = [[10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10],
        [21, 10, 10, 10, 10]]

# argument 2: an NDVI values matrix (amount of fuel available)
ndvi = [[0.2, 0.21621622, 0.13772455, 0.125, 0.16564417],
        [0.22077923, 0.19205298, 0.11377245, 0.17006803, 0.23404256],
        [0.1780822, 0.15646258, 0.16883117, 0.1971831, 0.25547445],
        [0.23404256, 0.21985815, 0.19444445, 0.1970803, 0.2361111],
        [0.2, 0.14102565, 0.20567375, 0.22222222, 0.2361111]]

# argument 3: a wind direction matrix (degrees)
wind = [[228.02113, 228.01082, 228.0004, 227.98988, 227.97925],
        [228.02544, 228.01518, 228.00482, 227.99437, 227.98381],
        [228.02959, 228.01939, 228.00911, 227.9987, 227.9882],
        [228.03358, 228.02345, 228.01323, 228.0029, 227.99246],
        [228.03743, 228.02737, 228.01721, 228.00694, 227.99657]]

# argument 4: a wind speed matrix (meters/second)
wins = [[13.619459, 13.629055, 13.638596, 13.648081, 13.657509],
        [13.618012, 13.627638, 13.637209, 13.646723, 13.65618],
        [13.616548, 13.626204, 13.635803, 13.645348, 13.654835],
        [13.615066, 13.624751, 13.63438, 13.643954, 13.653471],
        [13.613566, 13.623281, 13.63294, 13.642543, 13.652089]]

# argument 5: an elevation metrix (meters)
elev = [[2438.2336, 2436.6128, 2435.656, 2434.7534, 2433.9302],
        [2437.1211, 2435.6978, 2434.7439, 2433.863, 2433.1575],
        [2436.6663, 2435.2529, 2434.3806, 2433.5044, 2432.8291],
        [2435.377, 2434.0872, 2433.3362, 2432.603, 2432.0032],
        [2433.8435, 2432.7673, 2432.1641, 2431.697, 2431.2285]]

# argument 6: cell size (meters)
cellsize = 15.0

# call the ignitionprob() function in the kernel module
prob = kernel.ignitionprob(stat, ndvi, wind, wins, elev, cellsize)

# print the result
print "Final ignition probability for the central cell = {0}".format(prob)
