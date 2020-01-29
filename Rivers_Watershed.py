# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# RIvers_Watershed.py
# Created on: 2020-01-29 16:10:11.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: RIvers_Watershed <Input_surface_raster> <SQL_Expression> <Output_Feature> <Output_flow_direction_raster> <Output_accumulation_raster> <Output_stream_raster> 
# Description: 
# Creates a hidrographic network from a DEM based on a minimum area threshold
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_surface_raster = arcpy.GetParameterAsText(0)

SQL_Expression = arcpy.GetParameterAsText(1)
if SQL_Expression == '#' or not SQL_Expression:
    SQL_Expression = "VALUE < 100" # provide a default value if unspecified

Output_Feature = arcpy.GetParameterAsText(2)

Output_flow_direction_raster = arcpy.GetParameterAsText(3)

Output_accumulation_raster = arcpy.GetParameterAsText(4)

Output_stream_raster = arcpy.GetParameterAsText(5)

# Local variables:
Output_drop_raster = ""
Set_Null_Output = ""

# Process: Flow Direction
arcpy.gp.FlowDirection_sa(Input_surface_raster, Output_flow_direction_raster, "NORMAL", Output_drop_raster, "D8")

# Process: Flow Accumulation
arcpy.gp.FlowAccumulation_sa(Output_flow_direction_raster, Output_accumulation_raster, "", "FLOAT", "D8")

# Process: Set Null
arcpy.gp.SetNull_sa(Output_accumulation_raster, Output_accumulation_raster, Set_Null_Output, SQL_Expression)

# Process: Stream Link
arcpy.gp.StreamLink_sa(Set_Null_Output, Output_flow_direction_raster, Output_stream_raster)

# Process: Stream to Feature
arcpy.gp.StreamToFeature_sa(Output_stream_raster, Output_flow_direction_raster, Output_Feature, "SIMPLIFY")

