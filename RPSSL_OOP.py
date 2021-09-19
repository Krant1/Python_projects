from random import choice
class RockPaperScissorsSl():
    def __init__(self):
        self.game_choice=['rock','paper','scissors','spock','lizard']
        self.game_dict={'rock':0,'paper':1,'scissors':2,'spock':3,'lizard':4}
        self.player_score=0
        self.computer_score=0

    def game(self):
        self.no_of_rounds=int(input('How many rounds do you want to play for? '))
        for round in range(self.no_of_rounds):
            self.computer_choice=choice(self.game_choice)
            self.player_choice=input('Select between rock, paper, scissors, spock and lizard: ')
            print(f'Your choice was {self.player_choice}')
            print(f'Computer\'s choice was {self.computer_choice}')
            self.player_value=self.game_dict.get(self.player_choice)
            self.computer_value=self.game_dict.get(self.computer_choice)
            self.result_matrix=[[0,2,1,1,2],[1,0,2,2,1],[2,1,0,1,2],[2,1,2,0,2],[1,2,1,2,0]]
            self.result_value=self.result_matrix[self.computer_value][self.player_value]
            self.result=['It\'s a draw','You won!','Computer won, better luck next time']
            print(self.result[self.result_value])

class User():
    def __init__(self):
        self.player_name=input('What is your name? ')
        self.player_age=int(input('What is your age? '))
        self.rock_paper_scissors=RockPaperScissorsSl()
    
user_1=User()
user_1.rock_paper_scissors.game()
question=input('Do you want to play again? ')
if question.lower()[:1]=='y':
        print('Let\s play then!')
        user_1=User()
        user_1.rock_paper_scissors.game()
else:
        print('Ok then, see you next time')