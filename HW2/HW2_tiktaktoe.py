# Задача 2: Разработать игру «Обратные крестики-нолики» на поле 10 x 10 с правилом «Пять в ряд» – проигрывает тот,
# у кого получился вертикальный, горизонтальный или диагональный ряд из пяти своих фигур (крестиков/ноликов).
# Игра должна работать в режиме «человек против компьютера». Игра может быть консольной или поддерживать графический
# интерфейс (будет плюсом, но не требуется). При разработке игры учесть принцип DRY (don’t repeat yourself) –
# «не повторяйся». То есть минимизировать повторяемость кода и повысить его переиспользуемость за счет использования
# функций. Функции должны иметь свою зону ответственности.

import random
import copy
from itertools import count as count_from


# Проверка проигрыша по диагоналям
def check_diagonal(field: list, symbol: str, length: int, vertical: int, gorizontal: int) -> bool:
    # Аргументы:
    #     symbol - Х или О
    #     length - длина проверяемого квадрата
    #     vertical - смещение по столбцу (выбираем строку)
    #     gorizontal - смещение по строке (выбираем столбец в строке)
    # Результат:
    #     bool - наличие полных линий
    count_left, count_right = 0, 0
    for i in range(length):
        if field[i + vertical][i + gorizontal] == symbol:
            count_right += 1
        if field[i + vertical][length - i - 1 + gorizontal] == symbol:
            count_left += 1
    if count_left == length or count_right == length:
        return True
    return False


# Проверка проигрыша по горизонталям
def check_horizontal(field: list, symbol: str, length: int, vertical: int, horizontal: int) -> bool:
    # Аргументы:
    #     symbol - Х или О
    #     length - длина проверяемого квадрата
    #     vertical - смещение по столбцу (выбираем строку)
    #     horizontal - смещение по строке (выбираем столбец в строке)
    # Результат:
    #     bool - наличие полных линий
    for i in range(length):
        count = 0
        for j in range(length):
            if field[vertical + i][horizontal + j] == symbol:
                count += 1
        if count == length:
            return True
    return False


# Проверка проигрыша по вертикалям
def check_vertical(field: list, symbol: str, length: int, vertical: int, horizontal: int) -> bool:
    # Аргументы:
    #     symbol - Х или О
    #     length - длина проверяемого квадрата
    #     vertical - смещение по столбцу (выбираем строку)
    #     gorizontal - смещение по строке (выбираем столбец в строке)
    # Результат:
    #     bool - наличие полных линий
    for i in range(length):
        count = 0
        for j in range(length):
            if field[horizontal + j][vertical + i] == symbol:
                count += 1
        if count == length:
            return True
    return False


# Проверка проигрыша по всему полю
def check_lose(field: list, symbol: str, lose_length: int, vertical: int, horizontal: int) -> bool:
    # Аргументы:
    #     symbol - Х или О
    #     lose_length - длина проигрышной линии
    #     vertical - длина поля по вертикали
    #     horizontal - длина поля по горизонтали
    # Результат:
    #     bool - наличие проигрыша
    for i in range(0, vertical - lose_length + 1):
        for j in range(0, horizontal - lose_length + 1):
            if check_diagonal(field, symbol, lose_length, i, j) or \
                    check_horizontal(field, symbol, lose_length, i, j) or \
                    check_vertical(field, symbol, lose_length, i, j):
                return True
    return False


# Выбор следующего хода для компьютера
def computer_move(field: list, computer_symbol: str, lose_length: int) -> bool:
    # Аргументы:
    #     field - текущее поле
    #     computer_symbol - Х или О
    #     lose_length - длина проигрышной линии
    # Результат:
    #     bool - компьютер проиграл или сходил
    empty_spots = get_available_spots(field)
    random.shuffle(empty_spots)
    for spot in empty_spots:
        copy_field = copy.deepcopy(field)
        copy_field[spot[0]][spot[1]] = computer_symbol
        if check_lose(copy_field, computer_symbol, lose_length, len(field), len(field)) == False:
            field[spot[0]][spot[1]] = computer_symbol
            return True
    return False


# Выбор следующего хода для игрока
def player_move(field: list, player_symbol: str, lose_length: int, point_dict: dict) -> bool:
    # Аргументы:
    #     field - текущее поле
    #     computer_symbol - Х или О
    #     lose_length - длина проигрышной линии
    #     point_dict - dict для поиска координат за O(1)
    # Результат:
    #     bool - игрок проиграл или сделал ход
    while True:
        player_input = input('Введите точку: ')
        player_point = point_dict.get(player_input, None)
        if not player_point:
            print('Такой точки нет на поле, повторите ввод: ')
            continue
        if field[player_point[0]][player_point[1]] in {'X', 'O'}:
            print('Точка уже занята, повторите ввод: ')
        else:
            break
    field[player_point[0]][player_point[1]] = player_symbol
    if check_lose(field, player_symbol, lose_length, len(field), len(field)):
        return False
    return True


# Генерация нового игрового поля и dict для поиска координат
def new_field(vertical: int = 10, horizontal: int = 10) -> tuple:
    # Аргументы:
    #     horizontal - длина строки
    #     vertical - количество столбцов
    # Результат:
    #     tuple - (<поле>, <dict для поиска координат>)
    count = count_from(1)
    field, point_dict = [], {}
    for i in range(vertical):
        field.append([])
        for j in range(horizontal):
            number = str(next(count))
            field[i].append(number)
            point_dict[number] = (i, j)
    return field, point_dict


# Выбор символа для игры
def chose_your_symbol() -> tuple:
    # Результат:
    #     tuple - (<символ компьютера>, <символ игрока>)
    while True:
        user_symbol = input('Вы хотите играть за X или O? ').upper()
        if user_symbol in {'X', 'O'}:
            break
        else:
            print('Вам доступны только X или O, повторите ввод:')
    computer_symbol = 'O' if user_symbol == 'X' else 'X'
    return user_symbol, computer_symbol


# Определение случайным образом игрока, который будет ходить первым
def choose_first_player(user_symbol: str, computer_symbol: str) -> str:
    # Аргументы:
    #     user_symbol - символ игрока
    #     computer_symbol - символ компьютера
    # Результат:
    #     str - символ первого хода
    symbols = [user_symbol, computer_symbol]
    first_player = symbols[random.choice((0, 1))]
    print(f'В этот раз первым ходит игрок {first_player}')
    return first_player


# Получение списка доступных позиций
def get_available_spots(field: list) -> list:
    # Аргументы:
    #     field - поле
    # Результат:
    #     list - список пустых позиций
    empty_spots = []
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] not in {'O', 'X'}:
                empty_spots.append((i, j))
    return empty_spots


# Проверка поля на ничью
def check_draw(field: list) -> bool:
    # Аргументы:
    #     field - поле
    # Результат:
    #     bool - есть ли ничья
    if len(get_available_spots(field)) == 0:
        return True
    return False


# Итерация игры (ход игрока и компьютера)
def game_move(field: list, user_symbol: str, computer_symbol: str, lose_length: str, point_dict: dict) -> bool:
    # Аргументы:
    #     field - поле
    #     user_symbol - символ игрока
    #     computer_symbol - символ компьютера
    #     lose_length - длина последовательности для проигрыша
    #     point_dict - dict для поиска координат за O(1)
    # Результат:
    #     bool - флаг продолжения или окончания игры
    draw_result = check_draw(field)
    if draw_result:
        print('Ничья!')
        return False
    user_move = player_move(field, user_symbol, int(lose_length), point_dict)
    if not user_move:
        print('Вы проиграли')
        return False
    draw_result = check_draw(field)
    if draw_result:
        print('Ничья!')
        return False
    cpm_point = computer_move(field, computer_symbol, int(lose_length))
    if not cpm_point:
        print('Компьютер проиграл')
        return False
    return True


# Вывод поля
def print_field(field: list) -> None:
    result = ''
    for row in field:
        result += '|' + ('-' * (len(row) * 7 - 1)) + '|\n'
        for cell in row:
            result += '|  ' + cell + (' ' * (4 - len(cell)))
        result += '|\n'
    result += '|' + ('-' * (len(row) * 7 - 1)) + '|\n'
    print(result)


# Запуск игры
def main():
    lose_length = 5  # длина проигрышной комбинации
    vertical_size = 10  # размер поля по вертикали
    horizontal_size = 10  # размер поля по горизонтали
    while True:
        print('Игра в крестики-нолики началась!')
        # выбор символа игрока: Х или О
        user_symbol, computer_symbol = chose_your_symbol()
        # определение случайным образом, кто будет ходить первым
        first_player = choose_first_player(user_symbol, computer_symbol)
        # генерация и вывод нового игрового поля
        field, point_dict = new_field(vertical=vertical_size, horizontal=horizontal_size)
        if first_player == computer_symbol:
            computer_move(field, computer_symbol, lose_length)
        print_field(field)
        while game_move(field, user_symbol, computer_symbol, str(lose_length), point_dict):
            print_field(field)
        while True:
            user_symbol = input('Сыграть ещё раз? (Да/Нет): ').upper()
            if user_symbol in {'ДА', 'НЕТ'}:
                break
            else:
                print('Некорректный ответ на вопрос')
        if user_symbol == 'НЕТ':
            break


main()
