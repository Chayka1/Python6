def task_1_1():
    kuku = {'а': 1, 'б': 2, 'в': 3}


def task_1_2():
    a = {}


def task_1_3():
    dct = {'Джеймс': 12345}

    if 'Джеймс' in dct:
        print(dct['Джеймс'])
    else:
        print('Ключ не найден!')


def task_1_4():
    dct = {'Джим': 12345}

    if 'Джим' in dct:
        del dct['Джим']

def task_1_5():
    myset = {10, 20, 30, 40}


def task_1_6():
    set1 = {10, 20, 30, 40}
    set2 = {50, 60, 70, 80}
    set3 = set()

    set3.update(set1)
    set3.update(set2)


def task_1_7():
    set1 = {10, 20, 30, 40}
    set2 = {50, 10, 70, 30}
    set3 = set()

    set3 = set1.intersection(set2)


def task_1_8():
    pass



if __name__ == '__main__':
    task_1_7()
