from abc import ABC, abstractmethod

class Attacker(ABC):
    @abstractmethod
    def attack(self) -> None:
        pass
        
class Defender(ABC):
    @abstractmethod
    def defend(self) -> None:
        pass

class Healer(ABC):
    @abstractmethod
    def heal(self) -> None:
        pass

class Knight(Attacker, Defender, Healer):
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} attacks with sword!")

    def defend(self):
        print(f"{self.name} raises shield!")

    def heal(self):
        print(f"{self.name} uses healing potion!")

# Don't modify the following code
knight = Knight("Sir Galahad")
knight.attack()
knight.defend()
knight.heal()