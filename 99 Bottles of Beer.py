"""
-----------------------------------------------TASK-----------------------------------------------------------

    Create a program that prints out every line to the song "99 bottles of beer on the wall."
    This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

----------------------------------------------RULES-----------------------------------------------------------
    - If you are going to use a list for all of the numbers, do not manually type them all in.
    Instead, use a built in function.

    - Besides the phrase "take one down," you may not type in any numbers/names of numbers
    directly into your song lyrics.

    - Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

    - Put a blank line between each verse of the song.
-------------------------------------------------------------------------------------------------------------
"""

botls = 99
while botls > 0:
    if botls != 1:
        print('{0} bottles of beer on the wall, {0} bottles of beer'.format(str(botls)))
    else:
        print('{0} bottle of beer on the wall, {0} bottle of beer'.format(str(botls)))
    botls -= 1
    print('Take one down and pass it around, {0} bottles of beer on the wall.\n'.format(str(botls)))
print('No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, '
      '99 bottles of beer on the wall.')