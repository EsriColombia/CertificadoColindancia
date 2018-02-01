import arcpy

tColindantes="C:/Users/fvelez/Documents/fede/inclam/Topaipi Limitada/CATASTRO_25823.gdb/Colindantes_Tabla"
tLinderos="C:/Users/fvelez/Documents/fede/inclam/Topaipi Limitada/CATASTRO_25823.gdb/Colindantes_Linderos"

#c = arcpy.da.UpdateCursor(tColindantes,field_names=["src_CIP","nbr_CIP","Buscar_Matricula","NodosColindantes"],where_clause="src_CIP=\'00040\'")
c = arcpy.da.UpdateCursor(tColindantes,field_names=["src_CIP","nbr_CIP","LENGTH"],where_clause="nbr_CIP is not null")

for row in c:
    print row[2]

    cursorColindantesLinderos =arcpy.da.SearchCursor(tLinderos,["CIP_1","LENGTH"],where_clause="CIP=\'{0}\' and CIP_1=\'{1}\'".format(row[0],row[1]))
    LinderosColindantes=0
    i=0
    for r in cursorColindantesLinderos:
        print ("CIP SCR:{0} CIP COL:{1} Distancia: {2} ".format(row[0],row[1],r[1]))
        if (i==0):
          LinderosColindantes=r[1]
        else:
          LinderosColindantes=LinderosColindantes+r[1]
        i=i+1
    print("Campo:{0}".format(LinderosColindantes))
    row[2]=LinderosColindantes
    c.updateRow(row)

del c
del cursorColindantesLinderos