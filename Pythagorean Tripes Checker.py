try:
    lst_sides = input('Please, enter 3 sides of any triangle (separated by space)'). split()
    for i in range(len(lst_sides)):
        lst_sides[i] = int(lst_sides[i])
    lst_sides.sort()
    print(lst_sides)
    if lst_sides[2]**2 == (lst_sides[0]**2 + lst_sides[1]**2):
        print('Your triangle is a Pythagorean')
    else:
        print('Not Pythogorean triangle')
except Exception:
    print('Error')