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

    set3 = set1 & set2


def task_1_8():
    set1 = {10, 20, 30, 40}
    set2 = {50, 10, 70, 30}
    set3 = set()

    set3 = set1 - set2


def task_1_9():
    set1 = {10, 20, 30, 40}
    set2 = {50, 10, 70, 30}
    set3 = set()

    set3 = set2 - set1


def task_1_10():
    set1 = {10, 20, 30, 40}
    set2 = {50, 10, 70, 30}
    set3 = set()

    set3 = set1 ^ set2


def task_1_11():
    numbers = [1, 2, 3, 4, 5]

    a = {}
    num = 0

    for i in numbers:
        num += 10
        a[i] = num

    print(a)


def task_1_12():
    test_averages = {'Джанель': 98, 'Сэм': 87, 'Дженнифер': 92,
    'Томас': 74, 'Салли': 89, 'Зеб':84}

    high_scores = {}

    for k, v in test_averages.items():
        if v >= 90:
            high_scores[k] = v


def task_2_1():
    dct_1 = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'CS104': 1244, 'CS105': 1411}
    dct_2 = {'CS101': 'Хайнс', 'CS102': 'Альвардо', 'CS103': 'Рич', 'CS104': 'Берк', 'CS105': 'Ли'}
    dct_3 = {'CS101': '8:00', 'CS102': '9:00', 'CS103': '10:00', 'CS104': '11:00', 'CS105': '13:00'}

    course_number = input('Введите номер курса: ')
    print(f'Аудитория номер: {dct_1[course_number]}\n'
          f'Имя преподователя: {dct_2[course_number]}\n'
          f'Время проведения курса: {dct_3[course_number]}')


if __name__ == '__main__':
    task_2_1()
