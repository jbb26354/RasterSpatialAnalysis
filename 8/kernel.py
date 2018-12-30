'''
This function returns a ignition probability including spreading and spotting
from neighboring cells to the central cell
Author: Dr. Ray Huang
Year:   2018

Inputs (arguments):
    stat  - 5x5 array of current cell states
    ndvi  - 5x5 array of ndvi
    windd - 5x5 array of wind directions
    winds - 5x5 array of wind speed
    elev  - 5x5 array of elevation
'''
import math, random

# dictionary of fire state factors, derived from Gaussian distribution, derived from Equation 1
dicstate = {20:0.50, 21:0.52, 22:0.52, 23:0.50, 24:0.47, 25:0.42, 26:0.36, 27:0.31, 28:0.27, 29:0.23}

# cell directions in relation to the central cell in a 5x5 processing window
celldir = [[315.0, 333.435, 0.0, 26.565, 45.0],
           [296.565, 315.0, 0.0, 45.0, 63.435],
           [90.0, 270.0, None, 90.0, 90.0],
           [243.435, 225.0, 180.0, 135.0, 116.565],
           [225.0, 206.565, 180.0, 153.435, 135.0]]

def ignitionprob(stat, ndvi, windd, winds, elev, cellsize):
    # First, compute spreading probability
    if stat[2][2] == 0 or stat[2][2] == 30:  # unvegetated or burned cell
        return 0.0
    Pspreading = 0.0
    Pnot = 1.0
    for i in range(1, 4):
        for j in range(1, 4):
            if i == 2 and j == 2: continue
            if stat[i][j] in [-99, 0, 10, 30]: continue      # if cell(i,j) is not on fire, -99 represents nodata

            # probability contributed by the burning stage factor
            Px = dicstate[stat[i][j]]

            # probability contributed by ndvi
            nbar = (ndvi[j][i] + ndvi[2][2]) / 2.0
            Pn = 0.41 - 0.20 / math.pow(nbar * 3 + 1, 2)

            # probability contributed by wind. 
            alpha = windangle(windd[i][j], i, j)      # unit: degree
            Pw = 1.2 * (1.0 - 1 / math.pow(winds[i][j]*0.5+1.0, 0.50)) * math.cos(alpha * math.pi / 180)

            # probability contributed by slope gradient
            theta = slope(elev, cellsize, i, j)     # gets slope gradient, unit: gradian
            Ps = math.tan(theta / 2) / 2
            Pij = 1 - (1.0 - Px) * (1.0 - Pn) * (1 - Pw) * (1 - Ps)
            Pnot *= (1.0 - Pij)

    Pspreading = 1.0 - Pnot
    # print spreading probability
    print "Spreading probability = {0}".format(Pspreading)
    
    # Second, compute fire spotting probabilty
    Pspotting = 0.0
    Pnot = 1.0
    for i in range(0, 5):
        for j in range(0, 5):
            if i in [1, 2, 3] and j in [1, 2, 3]: continue
            if not stat[i][j] in range(21, 22): continue            # cell(i, j) is not in maximum fire condition
            Pn = 1.0 * math.log10(ndvi[i][j] + 1.0) + 0.046         # probability contributed by ndvi of cell(i,j)
            alpha = windangle(windd[i][j], i, j)                    # unit: degree
            dist = math.sqrt((i - 2)**2 + (j - 2)**2)
            s = winds[i][j] / 6.0 - 2.0                 # normalize wind speed
            Pw = (0.3578 + s / math.sqrt(1.0 + s**2) * 0.4) * math.cos(alpha * math.pi / 180) * 2 / dist
            theta = slope(elev, cellsize, i, j)         # slope in gradian
            Ps = - math.tan(theta / 2.0)                # probability contributed by slope
            Pij = 1 - (1 - Pn) * (1 - Pw) * (1 - Ps)
            if Pij < 0: Pij = 0
            Pnot *= (1 - Pij)
    Pspotting = 1.0 - Pnot
    # print spotting probability
    print "Spotting probability = {0}".format(Pspotting)

    # compute the overall ignition probability
    Pignition = 1.0 - (1.0 - Pspreading) * (1.0 - Pspotting) + random.random() * 0.15
    if Pignition >= 1.0: Pignition = 1.0
    return Pignition


# the following function computes slope between the burining cell and the current cell
# it returns a slope in gradian
def slope(elev, cellsize, row, col):
    dist = math.sqrt((row - 2)**2 + (col - 2)**2) * cellsize
    return math.atan(elev[2][2] - elev[row][col]) / dist

# the following function computes the angle between wind direction and fire advance direction.
# it returns an angle in degrees
def windangle(windir, row, col):
    alpha = abs(windir - celldir[row][col])
    if alpha > 180: alpha = 360 - alpha
    if alpha < -180: alpha += 360
    return alpha


    