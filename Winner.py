def winner(final_score, player):	
	score = max(final_score)
	winner = []
	for i in range(len(final_score)):
		if final_score[i] == score:
			winner.append(i)
	if len(winner) == 2:
		return print('\nIts a tie between {} and {} with score = {}'.format(player[winner[0]].name, player[winner[1]].name, score))
	elif len(winner) == 3:
		return print('\nIts a tie between {},{} and {} with score of {}'.format(player[winner[0]].name, player[winner[1]].name,player[winner[2]].name, score))
	elif len(winner) == 4:
		return print('\nAll of you tied with a score of {}'.format(score))
	else:
		return print('\nWinner is {} with score of {}'.format(player[winner[0]].name, score))