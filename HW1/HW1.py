from itertools import combinations  # для задачи 4 (про бананы)
from functools import reduce  # для задачи 5


# Задача №1.
# Написать метод domain_name, который вернет домен из url адреса:

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


# Задача №2.
# Написать метод int32_to_ip, который принимает на вход 32-битное целое число
# (integer) и возвращает строковое представление его в виде IPv4-адреса:

def int32_to_ip(int32):
    return '.'.join([str((int32 >> 8 * i) % 256) for i in [3, 2, 1, 0]])


assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"


# Задача №3.
# Написать метод zeros, который принимает на вход целое число (integer) и
# возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

def zeros(n):
    res = 0
    while n >= 5:
        n //= 5
        res += n
    return res


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(10_000) == 2499


# Задача №4.
# Написать метод bananas, который принимает на вход строку и
# возвращает количество слов «banana» в строке.

def bananas(s: str) -> set:
    result = set()
    for i in combinations(range(len(s)), len(s) - 6):
        new_word = list(s)
        for j in i:
            new_word[j] = '-'
        word = ''.join(new_word)
        if word.replace('-', '') == 'banana':
            result.add(word)
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


# Задача №5.
# Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
# предел (limit), после чего попробуйте сгенерировать по порядку все числа.
# Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

def count_find_num(primesL, limit):
    base_num = reduce((lambda a, b: a * b), primesL, 1)
    if base_num > limit:
        return []
    nums = [base_num]
    for i in primesL:
        for n in nums:
            num = n * i
            while (num <= limit) and (num not in nums):
                nums.append(num)
                num *= i

    return [len(nums), max(nums)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
