import os

imgServer = 'http://pic.ctrip.com/osdcar/site/airport/'
imgSqlFormat ="INSERT INTO OSD_StoreDrawingMap(MapItemCode,MapItemType,MapUrl,PointX,PointY,IsActive,DataChange_CreateUserID,DataChange_LastUserID,DataChange_CreateTime) VALUES('{0}',3,'{1}',0,0,1,0,0,NOW());"

def handlerPic(img):
	airPortCode = img[0:3]
	imgPath = imgServer+img
	return imgSqlFormat.format(airPortCode,imgPath)

def save(str):
	fout = open('C:\\drawMappint.sql','wt')
	print(str,file=fout)
	fout.close()

def getSqlStr():
	res = ''
	filepath = 'C:\\airPortPic'
	isExist = os.path.exists(filepath)
	if(isExist):
		picArr = os.listdir(filepath)
		if len(picArr)>0:
			for img in picArr:
				if(img.find('.jpg')>-1):
					res+=handlerPic(img)+'\n'
	return res

sqlStr = getSqlStr()

save(sqlStr)


