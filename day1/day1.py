numbers = open('data.txt', 'r').readlines()
increases = 0
previous = numbers[0].strip() # assign 1st number to previous
for number in numbers:
	currentNumber = number.strip()
	print(currentNumber)
	if currentNumber > previous:
		print('increased\n')
		increases += 1
	elif currentNumber == previous:
		print('same number\n')
	else:
		print('decreased\n')
	previous = currentNumber
print(increases)