#import regex
import re
print("Our Magical Calculator")
print("Type 'quit' to exit\n")

#initializing previous total variable
previous = 0
#initializing variable which the calc will refer to to see if it should keep running
run = True

def performMath():
    #getting run and previous into the function's scope
    global run
    global previous
    equation = ""

    #checking if a calculation has already been run, if not asking for an input
    if previous == 0: 
        equation = input("Enter equation:")
    else: 
        equation = input(str(previous))

    #Checking if someone wants to quit or clear
    if equation == 'quit':
        print('Googbye, human')
        run = False
    elif equation == 'clear':
        previous = 0
        print('cleared\n')
    #using regex to strip extraneous chars, helps to make eval statement safe.
    else: 
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            #if no previous value exists just evaluation input equation
            previous = eval(equation)
        else:
            #if previous value exists evaluate it with most recent input
            previous = eval(str(previous)+equation) 

while run:
    performMath()