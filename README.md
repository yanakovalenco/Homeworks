# Homeworks
Ответы на задания курса Y_LAB (backend python developer)
Домашние задания находятся в папках по неделям (описания задач также закомментированы).

# HW1

Задача №1. Написать метод domain_name, который вернет домен из url адреса:
Задача №2. Написать метод int32_to_ip, который принимает на вход 32-битное целое число (integer) и возвращает строковое представление его в виде IPv4-адреса
Задача №3. Написать метод zeros, который принимает на вход целое число (integer) и возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) 
заданного числа
Задача №4. Написать метод bananas, который принимает на вход строку и возвращает количество слов «banana» в строке.
Задача №5. Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число, предел (limit), 
после чего попробуйте сгенерировать по порядку все числа.

# HW2

Задача №1. Решение задачи комивояжера.
Задача №2. Игра "обратные крестики-нолики"

# HW3, part 1

Задача №1. Задача на циклический итератор. Надо написать класс CyclicIterator. Итератор должен итерироваться по итерируемому объекту 
(list, tuple, set, range, Range2, и т. д.), и когда достигнет последнего элемента, начинать сначала.
Задача №2. У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. Для эффективности дни проката хранятся периодами дат. 
Вам дан class Movie. Реализуйте у него метод schedule. Он будет генерировать дни, в которые показывают фильм.

# HW3, part 2
Задача №1. Задача на декоратор с кешированием результата. Напишите функцию-декоратор, которая сохранит (закэширует) значение декорируемой функции 
multiplier (Чистая функция). Если декорируемая функция будет вызвана повторно с теми же параметрами — декоратор должен вернуть сохранённый результат, 
не выполняя функцию.

Задача №2. Задача на декоратор с параметрами. Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время. 
Использует наивный экспоненциальный рост времени повтора (factor) до граничного времени ожидания (border_sleep_time).
В качестве параметров декоратор будет получать:
call_count - число, описывающее кол-во раз запуска функций;
start_sleep_time - начальное время повтора;
factor - во сколько раз нужно увеличить время ожидания;
border_sleep_time - граничное время ожидания.

Задача №3. Задача на рефакторинг кода. Посмотреть код в репозиторий (https://github.com/BernarBerdikul/ylab_hw) - Несолидный код. 
И сделать рефакторинг кода в соответствиях с принципами SOLID. Проблемы кода написаны в комментариях в коде.


# HW4
Надо написать логику авторизаций пользователей на основе JWT-токенов. К существующему проекту: 
https://github.com/BernarBerdikul/ylab_hw/tree/main/webinar_num_3.
● В качестве SQL DB: использовать Postgres.
● В качестве NoSQL DB: использовать Redis.
● В качестве Фреймворка: использовать FastAPI.
