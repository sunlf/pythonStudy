import os
import sys
sys.path.append('../')
import xlrd
import untity
root = "C:\\OSD3Path"

class excelMode(object):
	def __init__(self, packageVehicleID,adjustFactor,isActive,provinceNameKey,vehicleCode):
		self.packageVehicleID = packageVehicleID
		self.adjustFactor = adjustFactor
		self.isActive = isActive
		self.provinceNameKey = provinceNameKey
		self.vehicleCode = vehicleCode


xlsPath = os.path.join(root,"xhnf2.xlsx");
sqlPath = os.path.join(root,"xhnf.sql");
sqlFormat = "INSERT INTO dbo.OSD_PackageVehicleConfig( PackageVehicleID ,DiscountChannel ,SortNum ,InsuranceType ,ContractCode ,\
	DataSource ,AdjustFactor ,IsActive ,DataChange_CreateTime , DataChange_LastTime ,UseCarBeginDate ,UseCarEndDate , Priority ,RateCode, \
	ContinentID,CountryID,ProvinceID,CityID) VALUES ( {0} ,14003001,0 ,0, '' ,'' ,{1} , {2} ,GETDATE(),GETDATE(),\
	'2015-09-06 08:41:42' ,'2020-09-06 08:41:42' , 0 ,'',4,66,{3},0);"
if os.path.isfile(xlsPath):
	workbook = xlrd.open_workbook(xlsPath)
	table = workbook.sheets()[2]
	nrows = table.nrows
	ncols = table.ncols
	sqlres = ""
	provinceIdDics = {}
	dataArr = []
	for rownum in range(0,nrows):
		provinceIdInfos = table.cell_value(rownum,1)
		if provinceIdInfos.find('province')>-1:
			provinceNameKey = table.cell_value(rownum,0)
			provinceIds= provinceIdInfos.split('|')[1]
			provinceIdDics[provinceNameKey] = provinceIds
		else:
			vehicleName = table.cell_value(rownum,0)
			if vehicleName !='':
				packageVehicleID = table.cell_value(rownum,2)
				adjustFactorCell = table.cell_value(rownum,5)
				activeStr = table.cell_value(rownum,4)
				provinceNameKey = table.cell_value(rownum,9)
				vehicleCode = table.cell_value(rownum,1)
				isActive= 1
				adjustFactor = 1
				#print(activeStr)
				if adjustFactorCell:
					adjustFactor = 1+float(adjustFactorCell)
				dataArr.append(excelMode(packageVehicleID,adjustFactor,isActive,provinceNameKey,vehicleCode))
	#print(provinceIdDics)
	for x in dataArr:
		provinceIds = provinceIdDics.get(x.provinceNameKey)
		provinceArr = provinceIds.split(',')
		for provinceId in provinceArr:
			comment = "--"+str(provinceId)+"#"+str(int(x.packageVehicleID))+"#"+x.vehicleCode+"#"+str(x.adjustFactor)
			sql = comment+"\n"+sqlFormat.format(int(x.packageVehicleID),x.adjustFactor,x.isActive,provinceId)
			sqlres +=sql+"\n"
		sqlres+='\n'
else:
	print("not exist")

if sqlres!="":
	untity.save(sqlres,sqlPath)


		