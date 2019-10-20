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