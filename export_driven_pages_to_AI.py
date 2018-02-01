import os
import arcpy

# set input and output arguments
input_mxd = r"C:\Users\fvelez\Documents\fede\inclam\Topaipi\Acta de colindancia topaipi.mxd"
output_folder = r"C:\Users\fvelez\Documents\fede\inclam\Topaipi\Reportes"
field_name = r"CIP"

# export each data driven page out as a jpeg
mxd = arcpy.mapping.MapDocument(input_mxd)
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "PREDIO", df)[0]
print (lyr.name)


for i in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = i
    row = mxd.dataDrivenPages.pageRow
    # I've created a variable page_name to store the current page name
    page_name = row.getValue(field_name)
    print (page_name)
    arcpy.AddMessage("Processing {}".format(page_name))
    arcpy.mapping.ExportToJPEG(mxd, os.path.join(output_folder,  "Acta de colindancia.jpg"))
    #arcpy.mapping.ExportReport(lyr, r"C:\Guillermo\Inclam\testrc_report4.rlf", r"C:\Guillermo\Inclam\Report.pdf")
    arcpy.mapping.ExportReport(lyr, r"C:\Users\fvelez\Documents\fede\inclam\Nueva carpeta\Reportes\Reporte completo6.rlf", r"C:\Users\fvelez\Documents\fede\inclam\Topaipi\Reportes\Acta" + str(page_name) +" Topaipi"+ ".pdf")

    #arcpy.mapping.ExportToAI(map_document=mxd, out_ai=os.path.join(output_folder,  page_name + ".ai"), data_frame="PAGE_LAYOUT", df_export_width=1600,df_export_height=1200,resolution=300, image_quality="BEST", colorspace="CMYK" ,  picture_symbol="VECTORIZE_BITMAP", convert_markers=True)
    #arcpy.mapping.ExportToPDF (map_document=mxd, out_pdf=os.path.join(output_folder,  page_name + ".pdf"), data_frame= "PAGE_LAYOUT", df_export_width=1600, df_export_height=1200, resolution=300, image_quality="BEST", colorspace="CMYK", compress_vectors = True, image_compression="ADAPTIVE", picture_symbol="VECTORIZE_BITMAP", convert_markers=False, embed_fonts=True, layers_attributes= "NONE", georef_info= False, jpeg_compression_quality= 80)
    #arcpy.mapping.ExportToAI(mxd, os.path.join(output_folder,  page_name + ".ai"))
del mxd
