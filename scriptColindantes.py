import arcpy


tColindantes="C:/Users/fvelez/Documents/fede/inclam/Topaipi/CATASTRO_25823.gdb/Colindantes_Tabla"
tNodos="C:/Users/fvelez/Documents/fede/inclam/Topaipi/CATASTRO_25823.gdb/Colindantes_Nodos"

#c = arcpy.da.UpdateCursor(tColindantes,field_names=["src_CIP","nbr_CIP","Buscar_Matricula","NodosColindantes"],where_clause="src_CIP=\'00040\'")
c = arcpy.da.UpdateCursor(tColindantes,field_names=["src_CIP","nbr_CIP","Buscar_Matricula","NodosColindantes"],where_clause="nbr_CIP is not null")

for row in c:
    print row[2]

    cursorColindantesNodos =arcpy.da.SearchCursor(tNodos,["CIP_1","Orden"],where_clause="Lote_ID=\'{0}\' and CIP_1=\'{1}\'".format(row[0],row[1]))
    NodosColindantes=""
    i=0
    for r in cursorColindantesNodos:
        print ("CIP SCR:{0} CIP COL:{1} Matricula: {2} NoNodo_:{3}".format(row[0],row[1],r[0],r[1]))
        if (i==0):
          NodosColindantes=str(r[1])
        else:
          NodosColindantes=NodosColindantes+"-"+str(r[1])
        i=i+1
    print("Campo:{0}".format(NodosColindantes))
    row[3]=NodosColindantes
    c.updateRow(row)

del c
del cursorColindantesNodos