import random
import re

def play():
    userInput = askUser()
    p = re.compile('([rsp])')
    while re.match('[rsp]', userInput)==None:
        userInput = askUser()
    computer = random.choice(['r', 's', 'p'])
    
    if(userInput == computer):
        print("It\'s a tie!")
        askUser()
    
    if isWin(userInput, computer):
        print('Yay! you have won the game!')
    else:
        print('Sorry, you have lost the game :(')
def isWin(userInput, computer):
    if (userInput=='r' and computer=='s') or (userInput == 'p' and computer== 'r') or(userInput=='s' and computer=='p'):
        return True
    return False
def askUser():
    user = input("Enter your option between 'r', 's', 'p' >>>>>> ").lower()
    return user

play()
    