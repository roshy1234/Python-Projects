import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS 9000: ')
        self.moves: dict = {'rock':'🪨','paper':'📜','scissors':'✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.i = 0
        self.j = 0

    def play_game(self):
        user_move: str = input('Rock,Paper,Scissors? >> ').lower() #Rock -> rock

        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)


    def display_moves(self,user_move: str,ai_move: str):
        print('____')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('____')

    def check_moves(self,user_move: str,ai_move: str):

        if user_move == ai_move:
            print('It\'s a is a tie!')
            print(f'Your Score: {self.i}')
            print(f'Opponent Score: {self.j}')

        elif user_move == 'rock' and ai_move == 'scissors':
            print('You Win!')
            self.i+=1
            print(f'Your Score: {self.i}')
            print(f'Opponent Score: {self.j}')

        elif user_move == 'scissors' and ai_move == 'paper':
            print('You Win!')
            self.i+=1
            print(f'Your Score: {self.i}')
            print(f'Opponent Score: {self.j}')

        elif user_move == 'paper' and ai_move == 'rock':
            print('You Win!')
            self.i+=1
            print(f'Your Score: {self.i}')
            print(f'Opponent Score: {self.j}')

        else:
            print('AI wins!')
            self.j+=1
            print(f'Your Score: {self.i}')
            print(f'Opponent Score: {self.j}')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()