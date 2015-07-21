import os
import time

source = ['F:\\pythonStudy']

target_dir = 'F:\\Backup'

today = target_dir+os.sep+time.strftime('%Y%m%d')

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created director',today)

target = today + os.sep + time.strftime('%H%M%S')+'.zip'

zip_command = "zip -qr {0} {1}".format(target,' '.join(source))

if os.system(zip_command)==0:
	print('Successful backup to',target)
else:
	print('Backup FAILED')