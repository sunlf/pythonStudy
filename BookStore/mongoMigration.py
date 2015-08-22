import pymongo

conn = pymongo.MongoClient("localhost",27017)
db = conn.bookstore
#db.books.insert({"title":"c# in nutshell","image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif","date_added":1310248056})
#db.books.insert({"title":"大话数据结构","image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif","date_added":1310248056})
db.books.insert({"title":"新概念英语","image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif","date_added":1310248056})
db.books.insert({"title":"Oracle 实用教程","image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif","date_added":1310248056})
db.books.insert({"title":"白夜行","image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif","date_added":1310248056})
db.books.insert({"title":"国富论","image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif","date_added":1310248056})