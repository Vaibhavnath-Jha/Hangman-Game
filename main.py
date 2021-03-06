import os
import game
import time
from Winner import winner

class Player:
	def __init__(self, name, score):
		self.name = name
		self.score = score
		
	def display(self):
		print("{:12}{:12d}\n".format(self.name,self.score))

def rules(): #11
    print("\n\t\t\t\t-:GAME RULES:-")
    print("1. You will have 7 tries.\n2. You'll get 1 hint after 3rd try.")
    print("3. If you decide to enter FULL-NAME of the movie, enter as it is. An incorrect guess here means you're OUT")
    print("4. You have to press enter after you make a guess.")
    input('\n\n------------------------------------Press Enter to continue!------------------------------------')
    os.system('clear') 

def player_details():
	print("\t\tChoose Number of Players")
	print("1) One Player\t\t\t\t3) Three Players")
	print("\n2) Two Players\t\t\t\t4) Four Players")
	num_of_players = int(input("\nEnter your choice: "))
	names = ["name_" + str(i) for i in range(num_of_players)]
	while True:
		for i in range(num_of_players):
			names[i] = str(input("\nEnter Player "+str((i+1))+" Name: "))
		os.system('clear')
		print("\nParticipating Players: ")
		for i in range(num_of_players):
			print("\n", names[i])
		if str(input("\nDo you want to change anything?(Y/N): ")).upper() == "N": break
		else: os.system('clear')
	return num_of_players,names

def initialize_player(num_of_players, names):
	player = ['p1','p2','p3','p4']
	for i in range(num_of_players): # Initialization
		player[i] = Player(names[i], 0)
	return player

def start_game(player,num_of_players,names):
	os.system('clear')
	rounds = int(input("\nEnter how many rounds you want to play?: "))
	os.system('clear')
	for round_num in range(rounds):	
		for i in range(num_of_players):
			print("\t-|Round {} Begin|-\n".format(round_num+1))
			print("{}'s turn!\n".format(player[i].name))
			player[i].score += game.hangman() #Call to the actual game
			game.counter = True
			game.exit_token = False
			time.sleep(3)
			os.system('clear')
		print("\n\nScores after round {} are:\n".format(round_num+1))
		print("{:12}{:>12}".format("Player","Score"))
		for i in range(num_of_players):
			player[i].display()
		time.sleep(3)
		os.system('clear')
	print("\tFinal Score!\n")
	print("{:12}{:>12}".format("Player","Score"))
	for i in range(num_of_players):
		player[i].display()
	final_score = []
	for i in range(num_of_players):
		final_score.append(player[i].score)
	winner(final_score, player)
	print("\n\n\t!Thanks for playing!\n")
	
def main():
	rules()
	num_of_players, names = player_details()
	player = initialize_player(num_of_players, names)
	start_game(player, num_of_players, names)


if __name__ == '__main__':
	main()