from random import choice
game_choice=['rock','paper','scissors']
def rock_paper_scissors(no_of_rounds):
    player_score=0
    computer_score=0
    for round in range(no_of_rounds):
        computer_choice=choice(game_choice)
        player_choice=input('Select between rock,paper and scissors: ')
        print(f'Your choice was {player_choice}')
        print(f'Computer choice was {computer_choice}')
        if computer_choice=='rock' and player_choice=='rock':
            print('It\'s a draw. None gets a point')
        elif computer_choice=='rock' and player_choice=='paper':
            print('Paper beats rock. Player gets a point')
            player_score+=1
        elif computer_choice=='rock' and player_choice=='scissors':
            print('Rock beats scissors.Computer gets a point')
            computer_score+=1
        elif computer_choice=='paper' and player_choice=='paper':
            print('It\'s a draw. None gets a point')
        elif computer_choice=='paper' and player_choice=='rock':
            print('Paper beats rock. Computer gets a point')
            computer_score+=1
        elif computer_choice=='paper' and player_choice=='scissors':
            print('Scissors beats paper.Player gets a point')
            player_score+=1
            computer_score+=1
        elif computer_choice=='scissors' and player_choice=='scissors':
            print('It\'s a draw. None gets a point')
        elif computer_choice=='scissors' and player_choice=='paper':
            print('Scissors beats paper.Computer gets a point')
            computer_score+=1
        elif computer_choice=='paper' and player_choice=='scissors':
            print('Scissors beats paper.Player gets a point')
            player_score+=1
    print(f'''
    The scores are as follows:-
    COMPUTER={computer_score}
    YOU={player_score}
    ''')
    if computer_score>player_score:
        print('Computer won.Better luck next time')
    else:
        print('Congratulations! You won')

try:
    player_name=input('Please enter your name: ')
    player_age=int(input('Please enter your age: '))
    no_of_rounds=int(input('Enter the number of rounds you want to play for: '))
    rock_paper_scissors(no_of_rounds)
    question=input('Do you want to play again? ')
    if question.lower()[:1]=='y':
        print('Let\s play then!')
    else:
        print('Ok then, see you next time')
except ValueError:
    print('Please enter a valid value')

