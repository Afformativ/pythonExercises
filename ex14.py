#https://www.w3resource.com/python-exercises/python-functions-exercises.php (Exercise #1)
#Write a Python function to find the Max of three numbers.

a=int(input('Write number 1: '))
b=int(input('Write number 2: '))
c=int(input('Write number 3: '))

def min(num1,num2):
    if(num1>num2):
        return num2
    else:
        return num1

print(min(a,min(b,c)))