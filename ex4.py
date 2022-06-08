#Search a list of numbers for another number (ask for input).
#If the number is found, inform the user that their number is in the list.
#If the number is not found, inform the user that their number is not in the list.
a=[int(i) for i in input().split()]
b=int(input('Input a number that youw want to find in list: '))

flag=False
for j in range(len(a)):
    if(b==a[j]):
       flag=True
        
if (flag==True):
    print('Your number is in the list')
else:
    print('Your number isnot in the list')