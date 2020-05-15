import abc


class Weapon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print('attack with sword')


class Knife(Weapon):
    def attack(self):
        print('attack with knifes')


class Character:
    __weapon = None

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def attack(self):
        return self.__weapon.attack()


player1 = Character()
player1.set_weapon(Sword())
player1.attack()

player2 = Character()
player2.set_weapon(Knife())
player2.attack()
