#https://www.practicepython.org/ (exercise #8)
#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)
a='Yes'

while a=='Yes':
    Player1=input('Player1 please input Rock Paper or Scissors: ')
    Player2=input('Player2 please input Rock Paper or Scissors: ')
    if((Player1=='Rock' and Player2=='Scissors') or (Player1=='Scissors'and Player2=='Paper') or(Player1=='Paper'and Player2=='Rock')):
        print('Player1 wins')
    elif((Player2=='Rock' and Player1=='Scissors') or (Player2=='Scissors'and Player1=='Paper') or (Player2=='Paper'and Player1=='Rock')):
        print('Player2 wins')
    else:
        print('Draw')
    a=input('Do you want to play one more time, write Yes or No: ')
