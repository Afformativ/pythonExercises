#https://www.practicepython.org/ (exercise #2)
#ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#   If the number is a multiple of 4, print out a different message.
#   Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#	If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
a=int(input('Input number '))
b=int(input('Input number in which you want to divide '))

if (a%2==0):
    print('a is even')
elif(a%2==0 and a%4==0):
    print('a is divisible by 4')
else:
    print('a is odd')

if(a%b==0):
    print('a is divisible by b')
else:
    print('a is not divisible by b')