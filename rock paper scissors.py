x = 'yes'
while x == 'yes':
	play = ['none','none']
	play [0] = (input("Player 1 enter 'Rock', 'Paper', or 'Scissors': ")).lower()
	play [1] = (input("Player 2 enter 'Rock', 'Paper', or 'Scissors': ")).lower()

	def winner(play):
		if "rock" in play and "paper" in play:
			player = play.index('paper') + 1
			return player

		if "rock" in play and "scissors" in play:
			player = play.index('rock') + 1
			return player

		if "scissors" in play and "paper" in play:
			player = play.index('scissors') + 1
			return player

	print ("Player %s wins!" %(winner(play)))
	x = (input("would you like to keep playing? yes or no: ")).lower()
