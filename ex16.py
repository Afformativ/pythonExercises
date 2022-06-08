#https://www.w3resource.com/python-exercises/python-functions-exercises.php (Exercise #3)
#Write a Python function to multiply all the numbers in the list: (8, 2, 3, -1, 7)
a = [8, 2, 3, -1, 7]

def multiplylist():
    mult=1
    for i in range(len(a)):
        mult*=a[i]
    return mult
print(multiplylist())