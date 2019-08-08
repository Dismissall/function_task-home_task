def pow_func(a, b):
    """
    Finding the power of number a
    :param a: :type: int
    :param b: :type: int
    :return: pow(a,b)
    :type: int
    """
    return a ** b


def check_div_func(a, b):
    """
    Check divisibility numbers a & b
    :param a: :type: int
    :param b: :type: int
    :return: :type: str
    """
    if a % b == 0 or b % a == 0:
        return "YES"
    else:
        return "NO"


def second_max_func(lst1):
    """
    Ищем второй максимум
    :param lst1: :type:list
    :return: :type:list :type:int :type:None
    """
    copy_lst = sorted(lst1, key=int, reverse=True)
    if len(copy_lst) > 1:
        max_element = copy_lst[0]
        for x in range(0, len(copy_lst)):
            if max_element > copy_lst[x]:
                return copy_lst[x]
    elif len(copy_lst) == 1:
        return copy_lst
    else:
        pass


def win_row_function(lst1):
    """
    а1<a2>a3<... Проверяем сисок на заданную логику
    :param lst1: :type: list
    :return: :type: str
    """
    count = 0
    if len(lst1) < 3:
        return "R U serious?"
    for x in range(1, len(lst1)):
        if x % 2 != 0 and lst1[x] > lst1[x - 1]:
            count += 1
        elif x % 2 == 0 and lst1[x] < lst1[x - 1]:
            count += 1
    if count == len(lst1) - 1:
        return "HELL YEAH!!!"
    else:
        return "YOU WRONG! YOU WRONG! YOU WROOOOOOOONG!"


def operation_func(a, b, c):
    """
    Знаю, что eval() использовать крайне нежелательно.
    Но писать парсер для мат. операций... Ну, такое.
    :param a: :type: int
    :param b: :type: int
    :param c: :type: ?
    :return:
    """
    if type(c) is not str:
        return "I dont know what's happend"
    else:
        string = str(a) + c + str(b)
        return eval(string)


if __name__ == '__main__':
    print("Find power number:")
    print(pow_func(3, 4))

    print("\nCheck division:")
    print(check_div_func(2, 4))

    print("\nTry to do something with two numbers")
    print(operation_func(1, 2, "*"))

    print("\nFind second max of list")
    print("Enter size of list:")
    n = int(input())
    print("Enter values of list:")
    lst = list(map(int, input().rstrip().split()))
    print(second_max_func(lst))

    print("\nWin_row or...")
    print("Enter size of list:")
    n = int(input())
    print("Enter values of list:")
    lst = list(map(int, input().rstrip().split()))
    print(win_row_function(lst))
