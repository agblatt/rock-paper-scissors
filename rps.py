#bo3 rock paper scissors game


import random


class Game:
	def __init__(self):
		self.moves = ['rock', 'paper', 'scissors']
		self.conditions = {
			'rock': 'scissors',
			'paper': 'rock',
			'scissors': 'paper'
		}
		self.scores = {'user': 0, 'computer': 0}

	def game_loop(self):
		while self.scores['user'] != 2 and self.scores['computer'] != 2:
			userChoice, computerChoice = self.choices()
			print(f'\nuser picked: {userChoice}\ncomputer picked: {computerChoice}')

			check = self.win_condition_check(userChoice, computerChoice)

		self.win_message()

	def choices(self):
		userChoice = ''

		while userChoice not in self.moves:
			userChoice = input('rock, paper, or scissors? ').lower()

		computerChoice = random.choice(self.moves)

		return userChoice, computerChoice

	def win_condition_check(self, userChoice, computerChoice):
		if userChoice == computerChoice:
			print('--> there has been a tie\n')
			return
		elif self.conditions[userChoice] == computerChoice:
			print('--> user wins this time\n')
			self.scores['user'] += 1
			return
		else:
			print('--> computer wins this time\n')
			self.scores['computer'] += 1
			return

	def win_message(self):
		for player, score in self.scores.items():
			if score == 2:
				winner = player
			else:
				loser = player

		print(f'--> game over! {winner} has won {self.scores[winner]} to {self.scores[loser]}')


if __name__ == '__main__':
	Game().game_loop()