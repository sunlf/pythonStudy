# -*- coding:utf-8 -*-
import urllib2
import json
from city import city

cityname = '广州'
citycode = city.get(cityname)
if citycode:
	url = ('http://www.weather.com.cn/data/cityinfo/%s.html'%citycode)
	content = urllib2.urlopen(url).read()
	datadic = json.loads(content)
	print type(datadic)
