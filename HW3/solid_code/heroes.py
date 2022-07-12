from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def ultimate(self):
        pass

    def attack(self):
        self.fire_a_gun()

    def fire_a_gun(self):
        print('PIU PIU')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def roundhouse_kick(self):
        print('Bump')


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        self.incinerate_with_lasers()


class ChackNorris(SuperHero):

    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', True)

    def ultimate(self):
        self.roundhouse_kick()
