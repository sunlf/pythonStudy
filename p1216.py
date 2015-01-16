from random import randint
randNum = randint(5,10)

print 'guess what i think'
bingo = False

while  bingo ==False:
	answer = input()

	if answer<randNum:
		print 'too small!'

	if answer>randNum:
		print 'too big'

	if answer == randNum:
		print 'BINGO!'
		bingo = True