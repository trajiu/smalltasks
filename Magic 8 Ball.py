"""

-----------------------------------------------TASK-----------------------------------------------------------

    I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it
    right side up and it gives an answer by way of a floating die with responses written on it.

----------------------------------------------RULES-----------------------------------------------------------

    Allow the user to enter their question
    Display an in progress message( i.e. "thinking")
    Create 20 responses, and show a random response
    Allow the user to ask another question or quit
----------------------------------------------BONUS-----------------------------------------------------------
    A box for users to enter the question
    At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

"""

import random
import time
answer = \
    {
        1: 'Answer1',
        2: 'Answer2',
        3: 'Answer3',
        4: 'Answer4',
        5: 'Answer5',
        6: 'Answer6',
        7: 'Answer7',
        8: 'Answer8',
        9: 'Answer9',
        10: 'Answer10',
        11: 'Answer11',
        12: 'Answer12',
        13: 'Answer13',
        14: 'Answer14',
        15: 'Answer15',
        16: 'Answer16',
        17: 'Answer17',
        18: 'Answer18',
        19: 'Answer19',
        20: 'Answer20',
    }
question = input('Please, ask a question: ')
print('I\'m thinking...')
time.sleep(3)
print('My answer: {0}'.format(answer[random.randrange(1, 20)]))

