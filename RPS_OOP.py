from random import choice
class RockPaperScissors():
    def __init__(self):
        self.game_choice=['rock','paper','scissors']
        self.player_score=0
        self.computer_score=0

    def game(self):
        self.no_of_rounds=int(input('How many rounds do you want to play for? '))
        for round in range(self.no_of_rounds):
            self.computer_choice=choice(self.game_choice)
            self.player_choice=input('Select between rock,paper and scissors: ')
            print(f'Your choice was {self.player_choice}')
            print(f'Computer\'s choice was {self.computer_choice}')
            if self.computer_choice=='rock' and self.player_choice=='rock':
                print('It\'s a draw. None gets a point')
            elif self.computer_choice=='rock' and self.player_choice=='paper':
                print('Paper beats rock. Player gets a point')
                self.player_score+=1
            elif self.computer_choice=='rock' and self.player_choice=='scissors':
                print('Rock beats scissors.Computer gets a point')
                self.computer_score+=1
            elif self.computer_choice=='paper' and self.player_choice=='paper':
                print('It\'s a draw. None gets a point')
            elif self.computer_choice=='paper' and self.player_choice=='rock':
                print('Paper beats rock. Computer gets a point')
                self.computer_score+=1
            elif self.computer_choice=='paper' and self.player_choice=='scissors':
                print('Scissors beats paper.Player gets a point')
                self.player_score+=1
                self.computer_score+=1
            elif self.computer_choice=='scissors' and self.player_choice=='scissors':
                print('It\'s a draw. None gets a point')
            elif self.computer_choice=='scissors' and self.player_choice=='paper':
                print('Scissors beats paper.Computer gets a point')
                self.computer_score+=1
            elif self.computer_choice=='paper' and self.player_choice=='scissors':
                print('Scissors beats paper.Player gets a point')
                self.player_score+=1
        print(f'''
        The scores are as follows:-
        COMPUTER={self.computer_score}
        YOU={self.player_score}
        ''')
        if self.computer_score>self.player_score:
            print('Computer won.Better luck next time')
        else:
            print('Congratulations! You won')

class User():
    def __init__(self):
        self.player_name=input('What is your name? ')
        self.player_age=int(input('What is your age? '))
        self.rock_paper_scissors=RockPaperScissors()
    
user_1=User()
user_1.rock_paper_scissors.game()
question=input('Do you want to play again? ')
if question.lower()[:1]=='y':
        print('Let\s play then!')
        user_1=User()
        user_1.rock_paper_scissors.game()
else:
        print('Ok then, see you next time')