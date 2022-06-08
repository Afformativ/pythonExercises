#https://www.practicepython.org/ (exercise #11)
#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, 
#a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
#Take this opportunity to practice using functions, described below.
a=int(input('pls input ur number: '))
flag=True
if(a==2 or a==3):
    print('number is prime')
for i in range(2,a//2+1):
    if(a%i==0):
        flag=False
if(flag==True):
    print('number is prime')
else:
    print('number is not prime')