import random
import re

def play():
    userInput = askUser()
    p = re.compile('([rsp])')
    while re.match('[rsp]', userInput)==None:
        userInput = askUser()
    computer = random.choice(['r', 's', 'p'])
    
def askUser():
    user = input("Enter your option between 'r', 's', 'p' >>>>>>").lower()
    return user

play()
    