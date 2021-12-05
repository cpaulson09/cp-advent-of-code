lines = open('day4example.txt', 'r').readlines()
bingoNumbers = map(int, lines[0].split(','))

#  setup
newBoard = {
	0: [],
	1: [],
	2: [],
	3: [],
	4: [],
}
boards = {
	0: newBoard,
}
bingoBoard = {} # for final answer

# draw out each board
def createBoards(lines, boards, newBoard):
	boardIndex = 0
	rowIndex = 0
	for line in lines[2:]:
		numberRow = map(int, line.split())
		numberDict = {numberRow[i]: False for i in range(0, len(numberRow))}
		if len(numberRow) == 0:
			boardIndex += 1
			rowIndex = 0
			boards[boardIndex] = numberDict
		else:
			boards[boardIndex][rowIndex] = numberDict
			rowIndex += 1

def checkBoardsForBingo(boards):
	columnCount = 0
	for board in boards:
		rows = boards[board]
		for row in rows:
			if all(value == True for value in rows[row].values()):
				return True
			if list(rows[row])[-1]:
				columnCount += 1
	if columnCount == 5: # column bingo!
		return True
	else:
		return False

def calculateAnswer(board, bingoNumberCalled):
	unmarkedSum = 0
	print board

	for rows in board:
		row = board[rows]
		for number in row:
			if row[number] == False:
				unmarkedSum += number
	finalAnswer = unmarkedSum * bingoNumberCalled
	print'final answer: ', finalAnswer	

# Program start
createBoards(lines, boards, newBoard)

for bingoNumberCalled in bingoNumbers:
	for board in boards:
		rows = boards[board]
		for row in rows: # row of the board
			r = rows[row]
			for value in r: # value within each board row
				if value == bingoNumberCalled:
					r[value] = True
	bingo = checkBoardsForBingo(boards)
	if bingo:
		bingoBoard = boards[board]
		calculateAnswer(bingoBoard, bingoNumberCalled)
		break
