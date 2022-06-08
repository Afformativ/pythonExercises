#https://www.practicepython.org/ (exercise #1)
#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#	(Hint: order of operations exists in Python)
	
#    Print out that many copies of the previous message on separate lines.
#	(Hint: the string "\n is the same as pressing the ENTER button)
a=input('Name: ')
b=int(input('Age: '))
repeat=int(input('How many times u want to repeat: '))
с=100-b
for i in range(repeat):
    print(a,'will be 100 in ',100-b+2022,' year')