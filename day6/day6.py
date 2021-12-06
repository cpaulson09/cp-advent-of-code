# fishes = map(int, open("day6example.txt", 'r').readlines()[0].split(','))
# print fishes

# for day in range(256):
# 	for i, fishTimer in enumerate(fishes):
# 		if fishTimer == 0:
# 			fishes[i] = 7		# reset fish timer
# 			fishes.append(9)	# add new fish
# 	fishes = [fish - 1 for fish in fishes]
# print len(fishes)

fish = [[int(f) for f in open("day6example.txt").read().split(',')].count(i) for i in range(9)]
for i in range(18):
	fish.append(fish.pop(0))	# add # fish birthing (fish born) to 8 day column
	fish[6] += fish[8]			# reset fishes (6 days) for each born
print(sum(fish))