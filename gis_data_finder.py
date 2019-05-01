#set the map document we're working on
mxd = arcpy.mapping.MapDocument(r"McCleary_CrimeDensity.mxd")
#set the dataframe and layer we're searching in. 2nd parameter in df is the dataframe you want to work in, enter empty string
#for default df; 2nd parameter in lyr is the layer you want to work in. Case sensitive!
df = arcpy.mapping.ListDataFrames(mxd, "Saint Louis")[0]   
lyr = arcpy.mapping.ListLayers(mxd, "countycrime", df)[0]

#create feature layer (temp layer) to copy to; 1st parameter input layer, 2nd parameter output layer
arcpy.MakeFeatureLayer_management("McCleary_Crime.gdb/countycrime", "Rape_lyr")
#select by attribute
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", "UCR_CRIME_ = 111")
#selection is made, time to copy to new layer from selection
arcpy.CopyFeatures_management("Rape_lyr", "McCleary_Crime.gdb/rape_stats")
