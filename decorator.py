import time

def time_this(func):
	""" The tim_this decorator """

	def decorated(*args,**kwagrs):
		start = time.time()
		restult = func(*args,**kwagrs)
		print "Ran in ",time.time()-start,"seconds"
		return restult

	return decorated

@time_this
def count(until):
	print "Countint to ",until,"..."
	num = 0
	for i in xrange(to_num(until)):
		num = num+1
	return num

def to_num(numstr):
	return int(numstr.replace(",",""))

for num in ("10,000","100,1000","1,000,000,000"):
	print count(num)
	print "-" * 20
