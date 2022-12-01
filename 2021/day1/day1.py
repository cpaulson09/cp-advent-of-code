# numbers = open('data.txt', 'r').readlines()
# increases = 0
# previous = 0
# for number in numbers:
# 	currentNumber = number.strip()
# 	if currentNumber > previous:
# 		increases += 1
# 	previous = currentNumber
# print(increases)

report_str = open('data.txt', 'r').readlines()
report = list(map(int, report_str))

# count = 0
# part 1
# for x in len(report-1):
#     if report[x+1] > report[x]:
#         count += 1
# part 2
count2 = 0
for x in range(len(report)-3):
    if report[x+3] > report[x]:
        count2 += 1

# print(count)
print(count2)