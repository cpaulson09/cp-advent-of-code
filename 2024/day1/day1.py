import re
lines = open('data.txt', 'r').readlines()

leftList = []
rightList = []
distances = 0

for line in lines:
	leftList.append(int(line.strip().split('   ')[0]))
	rightList.append(int(line.strip().split('   ')[1]))

leftList = sorted(leftList)
rightList = sorted(rightList)

for i in range(len(leftList)):
	leftNumber = leftList[i]
	rightNumber = rightList[i]

	# first challenge
	# numToAdd = abs(rightNumber - leftNumber)
	 
	# second challenge
	# occurencesInRightList = rightList.count(leftNumber)
	# numToAdd = leftNumber * occurencesInRightList
	
	distances += numToAdd
print(distances)
