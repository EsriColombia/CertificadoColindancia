import arcpy
import numpy


Tabla = r"C:/Users/fvelez/Documents/fede/inclam/Topaipi/CATASTRO_25823_Prueba_Acta.gdb/Nodo_Predio"
cursor = arcpy.da.SearchCursor(Tabla,('*'),sql_clause=(None, 'ORDER BY Lote_ID'))
data = arcpy.da.TableToNumPyArray(Tabla, ('Lote_ID'))

del cursor

valores =[c[0] for c in data]

unique, counts = numpy.unique(valores, return_counts=True)
unicoConteo = numpy.asarray((unique, counts)).T

unicosCuenta = numpy.bincount(valores)

for idValues in unicoConteo:
    with arcpy.da.UpdateCursor(Tabla,["Orden", "OrdenSig"],where_clause='Lote_ID = \'{0}\''.format(idValues[0]) ,sql_clause=(None, 'ORDER BY Orden')) as cursor:
        i=1
        for row in cursor:
            if (idValues[1]==str(i)):
                row[1]=1
            else:
                row[1]=row[0]+1
            cursor.updateRow(row)
            i+=1
