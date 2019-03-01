board = [[0,0,0],[0,0,0],[0,0,0]]
count = 0

def changeBoard(plr,row,col):
	y = abs(row-3)
	x = col-1
	if board[y][x] != 0:
		global count
		count-=1
		print("Bitch, you try'na fool?")
	elif plr == 0:
		board[y][x] = 'x'
	elif plr == 1:
		board[y][x] = 'o'

def printyPrint(thing):
	for i in thing:
		print(i)

def checkZero(board):
	for i in board:
		for x in i:
			# print(x)
			if x == 0:
				return True
				break
	return False
	
if __name__=='__main__':
	printyPrint(board)
	while checkZero(board):
		plr = count%2
		inprow = int(input('What row? '))
		inpcol = int(input('What column? '))
		changeBoard(plr,inprow,inpcol)
		printyPrint(board)
		count += 1