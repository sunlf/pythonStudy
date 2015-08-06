import os
from untity import save 

path10 = 'C:\\cashBack\\back10.txt'
path12 = 'C:\\cashBack\\back12.txt'
formatsql = "INSERT INTO OSD_BOMItem(BomItemCode,BomCode,ItemName,ItemDesc,ItemType,SortNum,VendorBomID,IsFilter,IsActive,DataChange_CreateUserID,DataChange_LastUserID) \
VALUES('{0}','{1}','return','{2}','P',5,'{3}',0,1,0,0);"

def getTxt(path):
	res = []
	try:
		file = open(path)
		str = file.read()
		arr = str.split('\n')
		for a in arr:
			res.append(a.split('\t'))		
	except Exception:
		raise
	else:
		pass
	finally:
		file.close()
	return res


def action(path,pname,savepath):
	sqlStr = ''
	strArr = getTxt(path)
	for item in strArr:
		bomCode = item[0]
		vendorBomID = item[1]
		sql = formatsql.format('cashBack',bomCode,pname,vendorBomID)
		sqlStr+=sql+'\n'
	save(sqlStr ,savepath)


action(path10,'10%','C:\\cashBack\\back10.sql')

#print("--------------------------")
action(path12,'12%','C:\\cashBack\\back12.sql')




