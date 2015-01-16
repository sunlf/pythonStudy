# -*- coding:utf-8 -*-
city = {};
try:
	weatherfile = file('weather.txt')
	datalist = weatherfile.readlines()
	count = 0
	for w in datalist:
		warr = w.split('=')
		if len(warr)==2:
			cityId = warr[0]
			cityname = warr[1].replace('\n','')
			city[cityname] = cityId
			count = count+1	
except Exception, e:
	raise
else:
	pass
finally:
	pass