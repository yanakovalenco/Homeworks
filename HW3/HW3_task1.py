def cash(func):
    res = {}

    def wrapper(*args):
        if args not in res:
            res[args] = func(*args)
        return res[args]

    return wrapper


@cash
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    my_result = cash(multiplier)
    print(my_result(0))
    print(my_result(1))
    print(my_result(0))
