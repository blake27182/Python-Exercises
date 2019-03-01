game = [[2, 2, 1],
		[2, 2, 0],
		[1, 1, 1]]
def winner(board):
	xdim = len(game[0])
	ydim = len(game)
	for i in range(xdim+ydim-1):
		plr = 0
		# print(i)
		if i < xdim:
			y = 0
			x = i
		if i >= xdim:
			y = i-xdim+1
			x = 0
		# print(x,y)
		if game[y][x] != 0:
			if y == 0: #in the top row
				if x == 0: #and on the left column
					if game[y][x] == game[y+1][x+1] and game[y][x] == game[y+2][x+2]: #check diagonal
						plr = game[y][x]
						break
				if game[y][x] == game[y+1][x] and game[y][x] == game[y+2][x]: #check down
					plr = game[y][x]
					break
				if x == xdim-1: #on the right side
					if game[y][x] == game[y+1][x-1] and game[y][x] == game[y+2][x-2]:
						plr = game[y][x]
						break
			if x == 0: #is on the left column
				if game[y][x] == game[y][x+1] and game[y][x] == game[y][x+2]: #check right
					plr = game[y][x]
					break
	if plr == 0:
		return False
	else:
		return plr
		
if __name__=="__main__":
	print(winner(game))