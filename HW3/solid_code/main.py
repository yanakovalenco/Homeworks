from heroes import SuperHero, Superman, ChackNorris
from places import Place, Kostroma, Tokyo


def create_news(hero, place):
    print(f'{hero.name} saved the {place.city_name}!')


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo())
