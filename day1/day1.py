numbers = open('data.txt', 'r').readlines()
increases = 0
previous = 0
for number in numbers:
	currentNumber = number.strip()
	if currentNumber > previous:
		increases += 1
	previous = currentNumber
print(increases)