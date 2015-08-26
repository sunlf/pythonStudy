import pymongo
conn = pymongo.MongoClient("localhost",27017)
db = conn.test
for student in db.students.find():
	print(student.age)