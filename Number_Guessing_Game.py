from random import randint
def guessing_game():
    no_of_round=0
    while no_of_round<5:
        player_choice=int(input('Choose a number between 1 and 10: '))
        random_number=randint(1,10)
        if player_choice==random_number:
            print('Congratulations! You guessed it right')
            break
        else: 
            print(f'That was wrong. You have {4-no_of_round} chances left')
            no_of_round+=1

player_name=input('Enter your name: ')
player_age=int(input('Enter your age: '))
guessing_game()
play_again=input('Do you want to play again?: ') 
if play_again.lower()[:1]=='y':
    game()
else:
    print('It\'s alright.See you next time :)') 
