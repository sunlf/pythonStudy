import os
import sys
sys.path.append('../')
import xlrd
import untity
root = "C:\\database"

countryInfoPath = os.path.join(root,"countryInfo.xlsx"); 
dataPath = os.path.join(root,"数据.xlsx"); 
sqlPath = os.path.join(root,"data20150916.sql");


class Country(object):
	def __init__(self,country,countryId):
		self.country = country
		self.countryId = countryId


class Continent(object):
	def __init__(self,continent,continentId):
		self.continent = continent
		self.continentId = continentId

class  dataModel(object):
	def __init__(self,continent,country,alamoV,avisV,dollarv,enterpriseV,europcarV,hertzV,nationalV,sixtV,thriftyV):
		self.continent = continent
		self.country = country
		self.alamoV = alamoV
		self.avisV = avisV
		self.dollarv = dollarv
		self.enterpriseV = enterpriseV
		self.europcarV = europcarV
		self.hertzV = hertzV
		self.nationalV = nationalV
		self.sixtV = sixtV
		self.thriftyV = thriftyV


if os.path.isfile(countryInfoPath):
	workbook = xlrd.open_workbook(countryInfoPath)
	dataWorkbook = xlrd.open_workbook(dataPath)

	continenttable = workbook.sheets()[0]
	continenttablenrows = continenttable.nrows
	continenttablencols = continenttable.ncols

	countrytable = workbook.sheets()[1]
	countrytablenrows = countrytable.nrows
	countrytablencols = countrytable.ncols

	datatable = dataWorkbook.sheets()[0]
	datatablenrows = datatable.nrows
	datatablencols = datatable.ncols

	countryDict = dict()
	continentDict = dict()

	dataArr = []

	for rownum in range(0,continenttablenrows):
		continentId = continenttable.cell_value(rownum,0)
		continent = continenttable.cell_value(rownum,1)
		#continentArr.append(Continent(continent,continentId))
		continentDict[continent] = continentId

	for rownum in range(0,countrytablenrows):
		countryId = countrytable.cell_value(rownum,0)
		country = countrytable.cell_value(rownum,1)
		#countryArr.append(Country(country,countryId))
		countryDict[country] = countryId

	for rownum in range(1,datatablenrows-1):
		continent = datatable.cell_value(rownum,0)
		country = datatable.cell_value(rownum,1)
		alamoV = datatable.cell_value(rownum,2)
		avisV = datatable.cell_value(rownum,3)
		dollarv = datatable.cell_value(rownum,4)
		enterpriseV = datatable.cell_value(rownum,5)
		europcarV = datatable.cell_value(rownum,6)
		hertzV = datatable.cell_value(rownum,7)
		nationalV = datatable.cell_value(rownum,8)
		sixtV = datatable.cell_value(rownum,9)
		thriftyV = datatable.cell_value(rownum,10)
		dataArr.append(dataModel(continent,country,alamoV,avisV,dollarv,enterpriseV,europcarV,hertzV,nationalV,sixtV,thriftyV))

	sqlFormat = "INSERT into OSDDrivingLicense(ContinentID,ContinentName,CountryID,CountryName,VendorCode,IsActive)\
    value ({0},'{1}',{2},'{3}','{4}',{5});"

	sqlres = ''
	for x in dataArr:
		continent = x.continent
		country = x.country
		alamoV = x.alamoV
		avisV = x.avisV
		dollarv = x.dollarv
		enterpriseV = x.enterpriseV
		europcarV = x.europcarV
		hertzV = x.hertzV
		nationalV = x.nationalV
		sixtV = x.sixtV
		thriftyV = x.thriftyV
		countryId = countryDict[country]
		continentId = continentDict[continent]

		alamoVSql = sqlFormat.format(int(continentId),continent,int(countryId),country,'SD0009',1)
		sqlres += alamoVSql
		sqlres +='\n'

	if sqlres!="":
		untity.save(sqlres,sqlPath)
else:
	print("file not exists")



		
		
		