#https://www.w3resource.com/python-exercises/python-functions-exercises.php (Exercise #6)
#Write a Python function to check whether a number is in a given range.

rangeLeft=int(input('pls input left measure: '))
rangeRight=int(input('pls input right measure: '))

def Range():
    flag=True
    while flag:
        n=input('Please input number: ')
        if n == 'exit':
            flag=False
        num=int(n)
        if(num<=rangeRight and rangeLeft<=num):
            print('Num is in the range!')
        else:
            print('Num is not in the range')
Range()