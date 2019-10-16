"""
[PROJECT] Higher-Lower Guessing Game
BASIC GOAL Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is. After every guess, the computer should tell the user if the guess is higher or lower than the answer. When the user guesses the correct number, print out a congratulatory message.

SUB GOALS

Add an introduction message that explains to the user how to play your game.

In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.

At the end of the game, allow the user to decide if they want to play again (without having to restart the program).

"""


import random

def pc_random():
    return random.randrange(1,10)
print("Правила игры: Компьютер загадывает некоторое число от 1 до 10. Пользователь пытается его угадать.\nВводите число от 1 до 10. Угадали, вы, или нет, узнаете из ответа")
try_count = 0
pc_rand = int(pc_random())
while True:
    try:    
        user_answer = input("Please, enter you answer or press Q for exit: ")
        if 'Q'.lower() == str(user_answer.lower()):
                break
        else:
            if int(user_answer) == pc_rand:
                print("Congratulation, you win. This is really {}".format(pc_rand))
                print("fail attempt: {}".format(try_count))
                pc_rand = int(pc_random())
                try_count = 0
            else:
                print("Sorry, you lose.")
                try_count += 1
    except ValueError:
        try_count += 1
        print("Uncorrectly!!!")
    except Exception:
        try_count += 1
        print("Please, try again")