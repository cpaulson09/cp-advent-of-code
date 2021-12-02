commands = open('day2.txt', 'r').readlines()
horizontalPosition = 0
verticalPosition = 0
aim = 0
for command in commands:
	move = command.split(' ')[0]
	number = int(command.split(' ')[1].strip())
	if move == 'forward':
		horizontalPosition += number
		verticalPosition -= aim * number
	elif move == 'back':
		horizontalPosition -= number
	elif move == 'up':
		# verticalPosition -= number
		aim -= number
	elif move == 'down':
		# verticalPosition += number
		aim += number
	print(horizontalPosition, verticalPosition, aim)
print(horizontalPosition * -verticalPosition)