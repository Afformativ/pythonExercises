#https://www.w3resource.com/python-exercises/python-functions-exercises.php (Exercise #4)
#Write a Python program to reverse a string: 
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

a=input('pls input string: ')

def reverse():
    b=[]
    for i in range(len(a)):
        b.append(a[len(a)-1-i])
    b=''.join(b)
    return b
print(reverse())
