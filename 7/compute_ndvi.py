
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

env.workspace = "X:\Hostgator\homework\Courses\GSP537\labs\7\data\Schultz.gdb"
env.overwriteOutput = True

prered = Raster("AST17042B2")
prenir = Raster("AST17042B3")
prendvi = (prenir * 1.0 - prered) / (prenir + prered)
prendvi.save("prendvi")

postred = Raster("AST14506B2")
postnir = Raster("AST14506B3")
postndvi = (postnir * 1.0 - postred) / (postnir + postred)
postndvi.save("postndvi")

prendvi  = Raster("SHULTZ/prendvi")
postndvi = Raster("SHULTZ/postndvi")

dndvi = prendvi - postndvi

dndvi.save("diffndvi")