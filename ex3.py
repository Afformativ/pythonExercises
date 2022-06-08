#https://www.practicepython.org/ (exercise #12)
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.

a=[int(i) for i in input().split()]
b=[]

def FirstAndLast():
    b.append(a[0])
    b.append(a[len(a)-1])

FirstAndLast()
print(b)