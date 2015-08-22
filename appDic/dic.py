import pymongo
conn = pymongo.MongoClient("localhost",27017)
db = conn.dict
db.words.insert({"word":"oralock","definition":"A device attached to rowboat to \
 hold the oars in place"})
db.words.insert({"word":"seminonmadic","definition":"Only partially nomadic"})
db.words.insert({"word":"perturb","definition":"Bother, unsettle, modify"})
