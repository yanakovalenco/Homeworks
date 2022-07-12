from functools import wraps
from time import sleep, time


def repeat(
        call_count,  # число, описывающее кол-во раз запуска функций
        start_sleep_time,  # начальное время повтора
        factor,  # во сколько раз нужно увеличить время ожидания
        border_sleep_time  # граничное время ожидания
):
    def decorator(func):
        print(f'Кол-во запусков = {call_count}\nНачало работы')

        @wraps(func)
        def wrapper(*args):
            count = 1
            waiting = start_sleep_time
            for i in range(call_count):
                if waiting < border_sleep_time:
                    waiting *= 2 ** factor
                else:
                    waiting = border_sleep_time
                sleep(waiting)
                res = func(*args)
                print(f'Запуск номер {count}. Ожидание: {waiting} секунд. Результат декорируемой функций = {res}.')
                count += 1

        return wrapper

    return decorator


@repeat(call_count=3, start_sleep_time=0.0003, factor=3, border_sleep_time=3)
def multiplier():
    return time()


if __name__ == '__main__':
    multiplier()
    print('Конец работы')
