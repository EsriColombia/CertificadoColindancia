import arcpy

data_dict = {}
tPropietarios="C:/Users/fvelez/Documents/fede/inclam/Topaipi/CATASTRO_25823.gdb/Propietarios_Generales"

c = arcpy.da.UpdateCursor(tPropietarios,field_names=["CIP","OrdenG"],where_clause="CIP is not null")

for row in c:
    if row[0] in data_dict:
        # increment counter
        data_dict[row[0]] += 1
    else:
        data_dict[row[0]] = 1
    # update code
    cnt = data_dict[row[0]]
    row[1] = cnt

    c.updateRow(row)

del c
