#set the map document we're working on
mxd = arcpy.mapping.MapDocument(r"C:\Users\almccleary\Documents\IS3020\McCleary_CrimeDensity.mxd")
#set the dataframe and layer we're searching in
df = arcpy.mapping.ListDataFrames(mxd, "Saint Louis")[0]   
lyr = arcpy.mapping.ListLayers(mxd, "countycrime", df)[0]
#select by attribute
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", "UCR_CRIME_ = 111')
#selection is made, time to create layer from selection
