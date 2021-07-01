from random import randint
def user_interface(options):
    for index,option in enumerate(options):
        print(f'{index} = {option}')
    user_input = int(input('Please choose your option : '))
    return user_input

def computer_choice(content):
    computer_chose = randint(0,len(content)-1)
    return computer_chose
    
def check_results(choices, player, computer):
    if player == computer:
        return "Both have choosed same option! It\'s a tie\n"
    elif (player == 0 and computer == len(choices)-1) or (player>computer and not(player==len(choices)-1 and computer==0)):
        return "You have WON the match with Computer\n"
    return "You have LOST the match with Computer\n"

def play():
    print('''
    ---------------------------------
    Welcome to Rock, Paper, Scissors.
    Please pick your weapon.
    ''')
    options_list = ['Rock', 'Paper' , 'Scissors']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)
    print(f'  player chose: {options_list[player_result]}')
    print(f'computer chose: {options_list[computer_result]}')
    results = check_results(options_list,player_result,computer_result)
    print (f'\n{results}')

play_again = ''
while play_again.lower() != 'n':
    play()
    print (f'Do you want to play again? ')
    play_again = input('Please Type \'y\' for yes or \'n\' for no: ')
