# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Raster_Mean.py
# Created on: 2018-04-02 16:52:33.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
RasterMath_gdb = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\6\\data\\RasterMath.gdb"
Name = "UFO_Year2007"
UFO_Year2007 = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\6\\data\\RasterMath.gdb\\UFO_Year2007"
Output_Values = UFO_Year2007
UFO_Mean = "X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\6\\data\\RasterMath.gdb\\UFO_Mean"

# Process: Iterate Rasters
arcpy.IterateRasters_mb(RasterMath_gdb, "UFO_Year*", "", "NOT_RECURSIVE")

# Process: Collect Values
arcpy.CollectValues_mb("X:\\Hostgator\\homework\\Courses\\GSP537\\labs\\6\\data\\RasterMath.gdb\\UFO_Year2007")

# Process: Cell Statistics
arcpy.gp.CellStatistics_sa(Output_Values, UFO_Mean, "MEAN", "DATA")
