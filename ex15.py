#https://www.w3resource.com/python-exercises/python-functions-exercises.php (Exercise #2)
#Write a Python function to sum all the numbers in the list: (8, 2, 3, 0, 7)

a = [8, 2, 3, 0, 7]

def sumlist():
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum
print(sumlist())

