# Задача 1: Разработать программу для вычисления кратчайшего пути для почтальона.
# Описание задачи: Почтальон выходит из почтового отделения, объезжает всех адресатов один раз для вручения посылки
# и возвращается в почтовое отделение. Необходимо найти кратчайший маршрут для почтальона.
#
# Координаты точек:
# Почтовое отделение – (0, 2)
# Ул. Грибоедова, 104/25 – (2, 5)
# Ул. Бейкер стрит, 221б – (5, 2)
# Ул. Большая Садовая, 302-бис – (6, 6)
# Вечнозелёная Аллея, 742 – (8, 3)


def len_way(point1: tuple, point2: tuple) -> float:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def shortest_way():
    post = (0, 2)
    points = [(2, 5), (5, 2), (6, 6), (8, 3)]
    way = [(0, 2)]
    length = [0]
    first_point = post
    while points:
        dict_all = {}
        for point in points:
            dict_all[len_way(first_point, point)] = point
        min_point = (dict_all[min(dict_all)], min(dict_all))
        way.append(min_point[0])
        length.append(min_point[1])
        first_point = min_point[0]  # обновляем стартовую точку
        points.remove(min_point[0])  # обновляем список оставшихся адресов
    all_len = 0
    best_way = ''
    for point, len_between_points in zip(way, length):
        all_len += len_between_points
        if len_between_points != 0:
            best_way += str(point) + str([all_len]) + ' -> '
        else:
            best_way += str(point) + ' -> '
    all_len += len_way(way[-1], post)
    best_way += str(post) + str(all_len) + ' = ' + str(all_len)
    return best_way


print(shortest_way())
