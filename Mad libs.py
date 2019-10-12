"""-----------------------------------------------TASK-----------------------------------------------------------
Create a Mad Libs style game, where the program asks the user for certain types of words,
and then prints out a story with the words that the user inputted. The story doesn't have to be too long,
but it should have some sort of story line.

Tip - It's easiest to write out a quick story on a piece of paper or a word document,
and then go back through and see which words the user should be able to change.
"""

try:

    lst = input('Enter your 12 words: ').split()

    print(
        'Today I went to the zoo. I saw a {0} {1} jumping up and down \n'
        'in its tree. He {2} {3} through the large tunnel \n'
        'that led to its {4} {5}. I got some peanuts and passed them \n'
        'through the cage to a gigantic gray {6} towering above my head. Feeding that animal \n'
        'made me hungry. I went to get a {7} scoop of ice cream. It filled my stomach. \n'
        'Afterwards I had to {8} {9} to catch our bus. When I got home I \n'
        '{10}(verb past tense) my mom for a {11} day at the zoo. '.format(
            lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11]
        ))
except Exception:
    print('Somthing was wrong')