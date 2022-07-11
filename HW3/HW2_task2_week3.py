from dataclasses import dataclass  # для задачи 2
from datetime import datetime, timedelta  # для задачи 2
from typing import Generator, List, Tuple  # для задачи 2


# Задача 2. Задача на разжатие массива.
# У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. Для эффективности дни проката хранятся
# периодами дат. Вам дан class Movie.
# Реализуйте у него метод schedule. Он будет генерировать дни, в которые показывают фильм.


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date in self.dates:
            step = 0
            while date[0] + timedelta(days=step) <= date[1]:
                yield date[0] + timedelta(days=step)
                step += 1


m = Movie('sw', [(datetime(2020, 1, 1), datetime(2020, 1, 7)), (datetime(2020, 1, 15), datetime(2020, 2, 7))])

for d in m.schedule():
    print(d)
