"""
                            [Project] Multiplication Table
You remember those multiplication tables from elementary school, right? The ones where 
you choose a number on the top row and one on the side and see where they meet on the 
chart? Good. It would be easy enough to just write it out, but let's try using Python 
to our advantage.

                                        Goal
Create a program that prints out a multiplication table for the numbers 1 through 9. 
It should include the numbers 1 through 9 on the top and left axises, and it should be 
relatively easy to find the product of two numbers. Do not simply write out every line 
manually (ie print('7 14 21 28 35 49 56 63') ).

                                        Subgoals
As your products get larger, your columns will start to get crooked from the number of 
characters on each line. Clean up your table by evenly spacing columns so it is very easy 
to find the product of two numbers.

Allow the user to choose a number to change the size of the table (so if they type in 12, 
the table printed out should be a 12x12 multiplication table).

"""

while True:
    try:
        input_count = input('Введите размер: ')
        if input_count.lower() == 'q':
            break
        else:
            input_count = int(input_count)
            for i in range(1, input_count+1):
                for j in range(1, input_count+1):
                    print(str(i*j),'\t', end='')
                print()
    except ValueError:
        print('Введите целое число!')
    except Exception:
        print('Error')