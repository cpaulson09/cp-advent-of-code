import re
lines = open('data.txt', 'r').readlines()

total = 0
for line in lines:
	print('line', line)
	# first challenge
	# numbers = []
	# for character in line:
	# 	if character.isnumeric():
	# 		numbers.append(character)

	# second challenge
	numbers = re.findall(r'\d|(?:one|two|three|four|five|six|seven|eight|nine)', line)
	numbers = [int(n) if n.isdigit() else {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}[n] for n in numbers]
	
	print(numbers);
	numToAdd = ''
	if (len(numbers) == 1):
		numToAdd = str(numbers[0]) + str(numbers[0])
	else:
		numToAdd = str(numbers[0]) + str(numbers[-1])
	print(numToAdd)
	total += int(numToAdd)

print(total)

print('Day 01 Part 1:', sum([int(re.findall(r'\d', l)[0] + re.findall(r'\d', l)[-1]) for l in lines]), '\nDay 01 Part 2:', sum([int(''.join([{'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}[d] if d.isalpha() else d for d in [digits[0], digits[-1]]])) for l in lines for digits in [re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l)]]))
