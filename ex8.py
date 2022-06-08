#https://www.practicepython.org/ (exercise #6)
#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)
a=input('pls input string: ')
a=a.replace(' ','')
c=a[::-1]

flag=True

for j in range(len(a)):
    if(a[j]!=c[j]):
        flag=False

if(flag==True):
    print('string is palindrome')
else:
    print('string is not palindrome')