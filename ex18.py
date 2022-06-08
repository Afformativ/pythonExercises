#https://www.w3resource.com/python-exercises/python-functions-exercises.php (Exercise #5)
#Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument.

a=int(input('pls input number: '))

def fact(num):
    k=1
    while num!=0:
        k*=num
        num=num-1
    return k
print(fact(a))