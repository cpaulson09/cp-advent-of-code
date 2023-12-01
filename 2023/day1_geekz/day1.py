# Do you have any idea how many letters Santa gets each year before Christmas? Millions of people around the world send letters to Santa every year letting him know what they would like for Christmas. However, the logistics of not only reading those letters, but estimating labor, ordering materials, storing products, and loading up presents at the appropriate time in an efficient order requires a lot of planning.

# Problem: In order to prepare for this Christmas season, some of the head elves would like a report on how many letters are coming 
# from each country. The elves physically receiving the letters have been inputting the country code of the letter into a file named 
# "letters.txt". You need to read this file, and then report how many letters have been sent from each country.

# Example:
# input: letters.txt

# 1 2 34 53 1 53 6 ...
# output: output.txt

# 1:  2
# 2:  1
# 6:  1
# 34: 1
# 53: 2
# Notes: Answer does not need to be sorted. Use any language you like. Post/link results and source code in channel (feel free to add comments and/or ask for help). If you post the answer, you can "hide" it in discord by having two "pipes" on either side. Ex: ||Result||

numbers = open('data.txt', 'r').readline().rstrip().split(' ')
codes = dict()
for number in numbers:
	codes[number] = codes.get(number, 0) + 1
for key, value in sorted(codes.items(), key=lambda x: x[1], reverse=True):
	print(f'{key}:\t', value)
