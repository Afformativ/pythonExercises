#https://www.practicepython.org/ (exercise #9)
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
#then tell them whether they guessed too low, too high, or exactly right. 
#(Hint: remember to use the user input lessons from the very first exercise)
#
#Extras:
#
#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

a=random.randint(1,9)
count=0
while True:
    k=input('Write number: ')
    if k=='exit':
        break
    d=int(k)
    if((a-d)<0):
        print('your number is too high')
        count+=1
    elif((a-d)>0):
        print('your number is too low')
        count+=1
    else:
        count+=1
        print('You are exactly right! Number of your tries: ',count)
        a=random.randint(1,9)
        
