def count_to(count):
	
	numbers = ["one","two","three","four","five"]
	for number,pos in zip(numbers,range(count)):
		yield number

count_to_two = lambda : count_to(2)
count_to_five = lambda : count_to(5)

print "counting to two"
for num in count_to_two():
	print num,
print "\n"

print "counting to five"
for num in count_to_five():
	print num,
