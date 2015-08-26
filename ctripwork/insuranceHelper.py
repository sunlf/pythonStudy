import os
import sys
sys.path.append('../')
import xlrd
import untity
root = "C:\\OSD3Path"

xlsPath = os.path.join(root,"insurance.xlsx");
sqlPath = os.path.join(root,"insuranceUpdate.sql");
sqlFormat = "UPDATE OSDInsuranceDetail set DetailShortName='{0}',DetailNameEn='{1}',DetailDesc='{2}',DetailShortDesc='{3}' where itemCode='{4}';"
if os.path.isfile(xlsPath):
	workbook = xlrd.open_workbook(xlsPath)
	table = workbook.sheets()[0]
	nrows = table.nrows
	ncols = table.ncols
	sqlres = ""
	for rownum in range(1,nrows):
		sx = table.cell_value(rownum,1)
		enname = table.cell_value(rownum,2)
		shortname = table.cell_value(rownum,4)
		des = table.cell_value(rownum,5)
		desshort = table.cell_value(rownum,6)
		#print(sx+"***"+enname+"***"+des+"***"+desen)
		sql = sqlFormat.format(shortname,enname,des,desshort,sx)
		sqlres +=sql+"\n"
else:
	print("not exist")
if sqlres!="":
	untity.save(sqlres,sqlPath)