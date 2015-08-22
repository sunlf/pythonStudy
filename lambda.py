points = [{'x':2,'y':3},{'x':4,'y':1}]
points.sort(key = lambda i:i['y'])
print(points)

listone = [2,3,5]
listtwo = [2*i for i in listone if i>2]
print(listtwo)