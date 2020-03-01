#bo3 rock paper scissors game


import random


class Game:
    '''
    rock paper scissors game class
    '''
    def __init__(self):
        '''
        init valid moves, win conditions, and scores
        '''
        self.moves = ['rock', 'paper', 'scissors']
        self.conditions = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        self.scores = {'user': 0, 'computer': 0}

    def game_loop(self):
        '''
        game loop
        while scores < 2, loop main functions of game
            get user and computer choice
            check who won the round

        if score == 3, display winner and winners score
        '''
        while self.scores['user'] != 2 and self.scores['computer'] != 2:
            user_choice, computer_choice = self.choices()
            print(f'\nuser picked: {user_choice}\ncomputer picked: {computer_choice}')

            self.win_condition_check(user_choice, computer_choice)

        self.win_message()

    def choices(self):
        '''
        gets users choice from valid moves and generates computers choice
        returns both choices to game_loop
        '''
        user_choice = ''

        while user_choice not in self.moves:
            user_choice = input('rock, paper, or scissors? ').lower()

        computer_choice = random.choice(self.moves)

        return user_choice, computer_choice

    def win_condition_check(self, user_choice, computer_choice):
        '''
        receives params user_choice : str, and computer_choice : str
        checks conditions to see who won the round
            adds 1 to winners score or nothing if theres a tie
        '''
        if user_choice == computer_choice:
            print('--> there has been a tie\n')
            return
        elif self.conditions[user_choice] == computer_choice:
            print('--> user wins this time\n')
            self.scores['user'] += 1
            return
        else:
            print('--> computer wins this time\n')
            self.scores['computer'] += 1
            return

    def win_message(self):
        '''
        displays win message for user whose score == 2
        '''
        for player, score in self.scores.items():
            if score == 2:
                winner = player
            else:
                loser = player

        print(f'--> game over! {winner} has won {self.scores[winner]} to {self.scores[loser]}')


if __name__ == '__main__':
    # run game
    Game().game_loop()
